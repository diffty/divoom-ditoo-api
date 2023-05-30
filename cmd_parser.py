import re
import pprint 

from enums import CmdType


function_body_template = \
"""
def {py_func}({py_params}) -> {py_return}:
    \"\"\"
    {py_docstring}
    \"\"\"

    params={py_param_dict}

    {py_generated_return}
"""


def javatype_to_pytype(java_type):
    res = re.search("([a-z0-9_]+)\$([a-z0-9_]+)", java_type, re.I)
    if res:
        java_type = "enums." + "".join(map(str.capitalize, res.group(2).split("_")))

    return {
        "void": "None",
        "boolean": "bool",
        "byte[]": "bytearray",
        "List<Integer>": "List[int]",
        "List<byte[]>": "List[bytearray]",
        "String": "str"
    }.get(java_type, java_type)


def process_param_vars(param_name):
    res = re.search("([a-z0-9_]+)\$([a-z0-9_]+)", param_name, re.I)
    if res:
        return "_".join(map(str.lower, res.groups()[1:]))
    else:
        return param_name


def generate_docstring(summary, params, ret, indent=4) -> str:
    docstring = summary + "\n"

    if params:
        docstring += "\nParameters:\n"
        for i, p in enumerate(params):
            docstring += f"\t{process_param_vars(p[1])} ({javatype_to_pytype(p[0])})"
            if i < len(params)-1:
                docstring += "\n"

    pyret = javatype_to_pytype(ret)

    if pyret and pyret != "None":
        docstring += "\nReturns:\n"
        docstring += f"\t{pyret}"

    docstring = "\n".join(map(lambda l: " "*indent + l, docstring.split("\n")))
    return docstring


generated_file = \
"""from typing import List, NewType
from communication import send_msg
import enums


byte = NewType("byte", int)
short = NewType("short", int)


class PixelBean:
    pass


class MultiModeEnum:
    pass


class MultiShowEnum:
    pass


class c:
    pass


class PowerSetInfo:
    pass

"""


with open("../CmdManager.java") as fp:
    file_content = fp.read()
    results = re.finditer(r"public static ([^ ]+) ([a-z0-9_]*)\(([^()]*)\) {(.+?)}", file_content, re.I | re.DOTALL)
    
    for r in results:
        return_type = r.group(1)
        java_func_name = r.group(2)
        params = r.group(3)
        code = r.group(4)
        mentionned_symbols = [r2.group(1) for r2 in re.finditer(r"SppProc\$([a-z0-9_]+)\.SPP_([a-z0-9_]+)", code, re.I)]

        symbol_matchs = list(filter(lambda s: s.group(1) == "CMD_TYPE",
                                    re.finditer(r"SppProc\$([a-z0-9_]+)\.SPP_([a-z0-9_]+)", code, re.I)))
        if symbol_matchs:
            
            params = list(map(lambda p: p.split(" "), map(str.strip, params.split(","))))
            if params == [['']]:
                params = None

            cmd_name = symbol_matchs[0].group(2)
            cmd_code = "enums.CmdType." + cmd_name
            py_func = cmd_name.lower()
            py_params = ", ".join(map(lambda p: f"{process_param_vars(p[1])}: {javatype_to_pytype(p[0])}", params)) if params else ""
            py_return = javatype_to_pytype(return_type)
            py_javacode = "\n".join(list(map(lambda l: l, r.group(0).split("\n"))))
            py_param_dict = "[\n" + ",\n".join(map(lambda p: f"        ({process_param_vars(p[1])}, '{javatype_to_pytype(p[0])}')", params)) + "\n    ]" if py_params else "[]"
            if py_return:
                py_generated_return = f"return send_msg({cmd_code}, params)"
            else:
                py_generated_return = f"send_msg({cmd_code}, params)"
            
            py_docstring = generate_docstring(py_javacode, params, return_type)

            generated_file += function_body_template.format(
                py_func=py_func,
                py_params=py_params,
                py_return=py_return,
                py_docstring=py_docstring,
                py_param_dict=py_param_dict,
                py_generated_return=py_generated_return,
            ) + "\n"


fp = open("commands.py", "w")
fp.write(generated_file)
fp.close()
