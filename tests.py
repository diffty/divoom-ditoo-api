import commands
import enums

#commands.set_box_mode(enums.LightMode.CLOCK, 0x00)
#commands.set_vol(0x9)
#commands.set_play_status(0x02)
commands.set_box_mode(enums.LightMode.CLOCK, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0xff)
