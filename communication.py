from typing import List

import socket


def make_crc(payload: bytes) -> bytearray:
    """ make_crc
    `CRCR` is the CRC of the message including the length (`LLLL PAYLOAD`) in LSB First
    """
    s = sum(payload)
    return s.to_bytes(2, "little")


def make_length(data: bytes, add_itself_to_length=True) -> bytearray:
    """ make_length
    `LLLL` is the length of the `PAYLOAD` string + the length of the CRC (`4`) in number of bytes (`FF` is one byte for example) in LSB First
    """
    length = len(data)
    if add_itself_to_length:
        length += 2
    return length.to_bytes(2, "little")


def make_payload(params: List[tuple[any, str]]):
    payload = bytes()
    for p in params:
        if p[1] == "byte":
            p_byte = p[0].to_bytes(1, 'little')
            if len(p_byte) > 1:
                raise Exception(f"Byte parameter is too long : {p_byte} (size: {len(p_byte)})")
            payload += p_byte
        elif p[1] == "int":
            p_byte = p[0].to_bytes(1, 'little')
            payload += p_byte
        elif p[1] == "bool":
            p_byte = p[0].to_bytes(1, 'little')
            payload += p_byte
        elif p[1] == "bytearray":
            payload += bytes(p[0])
        elif p[1] == "enums.LightMode":
            payload += bytes(p[0])

        else:
            raise Exception("Unsupported data type for parameter " + str(p))
        
    return payload


def send_msg(cmd_type_code: int, params: List[tuple[any, str]]):
    """ send_msg """
    cmd_type_code = cmd_type_code.to_bytes(1, 'little')
    msg = make_msg(cmd_type_code, make_payload(params))
    print(msg.hex())

    import socket

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect(('B1:21:81:2B:A0:1C', 2))

    s.send(msg)

    c = s.recv(1)
    while(c):
        print(c)
        c = s.recv(1)

    s.close()



def receive_msg(msg: bytearray, params: List[str]):
    """ receive_msg """


def make_msg(cmd_type_code, payload):
    length = make_length(cmd_type_code + payload)
    crc = make_crc(length + cmd_type_code + payload)

    full_message  = bytes([0x01])
    full_message += length
    full_message += cmd_type_code
    full_message += payload
    full_message += crc
    full_message += bytes([0x02])

    return full_message


if __name__ == "__main__":
    test_full_message = bytes([0x01, 0x04, 0x00, 0x45, 0x00, 0x49, 0x00, 0x02])
    test_length = bytes([0x04, 0x00])
    test_cmd_code = bytes([0x45])
    test_payload = bytes([0x00])
    test_crc = bytes([0x49, 0x00])

    length = make_length(test_cmd_code + test_payload)
    print(length.hex())

    crc = make_crc(length + test_cmd_code + test_payload)
    print(crc)

    full_msg = make_msg(test_cmd_code, test_payload)
    print(full_msg.hex())


