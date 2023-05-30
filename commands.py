from typing import List, NewType
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


def get_energy_ctrl() -> bytearray:
    """
        public static byte[] A() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_ENERGY_CTRL, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_ENERGY_CTRL, params)


def set_scene_listen_volume(paramByte: byte) -> bytearray:
    """
        public static byte[] A0(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SCENE_LISTEN_VOLUME, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_SCENE_LISTEN_VOLUME, params)


def set_poweron_voice_vol(paramInt: int) -> None:
    """
        public static void A1(int paramInt) {
        byte b = (byte)(paramInt & 0xFF);
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("sendStartVoice ");
        stringBuilder.append(paramInt);
        k.d("octopus.CmdManager", stringBuilder.toString());
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_POWERON_VOICE_VOL, new byte[] { 1, b }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_POWERON_VOICE_VOL, params)


def eye_guard_info() -> None:
    """
        public static void B() {
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_EYE_GUARD_INFO, new byte[] { -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.EYE_GUARD_INFO, params)


def set_sleep_scene(paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] B0(byte[] paramArrayOfbyte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_SCENE, paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.SET_SLEEP_SCENE, params)


def lieght_phone_gif32_word_attr(paramInt: int) -> None:
    """
        public static void B1(int paramInt) {
        k.d("octopus.CmdManager", "set32TextColor");
        byte b1 = (byte)(paramInt >> 16 & 0xFF);
        byte b2 = (byte)(paramInt >> 8 & 0xFF);
        byte b3 = (byte)(paramInt & 0xFF);
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_PHONE_GIF32_WORD_ATTR, new byte[] { 5, b1, b2, b3 }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_PHONE_GIF32_WORD_ATTR, params)


def lieght_set_25dots_pic(paramPixelBean: PixelBean) -> int:
    """
        public static int B2(PixelBean paramPixelBean) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        h h = new h();
        List list = h.c(h.f(paramPixelBean), SppProc$CMD_TYPE.SPP_LIEGHT_SET_25DOTS_PIC);
        for (byte[] arrayOfByte : list)
          p.s().F(arrayOfByte, true); 
        return list.size();
      }
    
    Parameters:
    	paramPixelBean (PixelBean)
    Returns:
    	int
    """

    params=[
        (paramPixelBean, 'PixelBean')
    ]

    return send_msg(enums.CmdType.LIEGHT_SET_25DOTS_PIC, params)


def get_fm_count_or_freq() -> bytearray:
    """
        public static byte[] C() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_FM_COUNT_OR_FREQ, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_FM_COUNT_OR_FREQ, params)


def get_scene() -> bytearray:
    """
        public static byte[] C0() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_SCENE, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_SCENE, params)


def lieght_phone_gif32_word_attr(paramInt: int) -> None:
    """
        public static void C1(int paramInt) {
        k.d("octopus.CmdManager", "set32TextEffect");
        byte b = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_PHONE_GIF32_WORD_ATTR, new byte[] { 2, b }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_PHONE_GIF32_WORD_ATTR, params)


def set_sd_music_play_mode(paramInt: int) -> bytearray:
    """
        public static byte[] C2(int paramInt) {
        byte b = (byte)(paramInt & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_SD_MUSIC_PLAY_MODE, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_SD_MUSIC_PLAY_MODE, params)


def get_fm_current_freq() -> bytearray:
    """
        public static byte[] D() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_FM_CURRENT_FREQ, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_FM_CURRENT_FREQ, params)


def set_sleep_time(paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] D0(byte[] paramArrayOfbyte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_TIME, paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.SET_SLEEP_TIME, params)


def lieght_phone_gif32_word_attr(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> None:
    """
        public static void D1(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
        k.d("octopus.CmdManager", "set32TextFrame");
        byte b1 = (byte)paramInt1;
        byte b2 = (byte)paramInt2;
        byte b3 = (byte)paramInt3;
        byte b4 = (byte)paramInt4;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_PHONE_GIF32_WORD_ATTR, new byte[] { 3, b1, b2, b3, b4 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    	paramInt3 (int)
    	paramInt4 (int)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int'),
        (paramInt3, 'int'),
        (paramInt4, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_PHONE_GIF32_WORD_ATTR, params)


def set_play_status(paramBoolean: bool) -> bytearray:
    """
        public static byte[] D2(boolean paramBoolean) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_PLAY_STATUS, new byte[] { paramBoolean }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_PLAY_STATUS, params)


def get_fm_region() -> bytearray:
    """
        public static byte[] E() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_FM_REGION, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_FM_REGION, params)


def lieght_phone_gif32_word_attr(paramInt: int) -> None:
    """
        public static void E1(int paramInt) {
        k.d("octopus.CmdManager", "set32TextSize");
        byte b = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_PHONE_GIF32_WORD_ATTR, new byte[] { 4, b }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_PHONE_GIF32_WORD_ATTR, params)


def set_last_next(paramBoolean: bool) -> bytearray:
    """
        public static byte[] E2(boolean paramBoolean) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_LAST_NEXT, new byte[] { paramBoolean }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_LAST_NEXT, params)


def hot_send_file_data(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] F(int paramInt, byte[] paramArrayOfbyte) {
        byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 2];
        arrayOfByte[0] = (byte)(byte)(paramInt & 0xFF);
        arrayOfByte[1] = (byte)(byte)(paramInt >> 8 & 0xFF);
        System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 2, paramArrayOfbyte.length);
        return r.c(SppProc$CMD_TYPE.SPP_HOT_SEND_FILE_DATA, arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int'),
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.HOT_SEND_FILE_DATA, params)


def app_new_user_define2020() -> bytearray:
    """
        public static byte[] F0() {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte[] arrayOfByte = new byte[1];
        arrayOfByte[0] = (byte)2;
        return (DeviceFunction.NewAniSendMode2020.getMode() == DeviceFunction.NewAniSendMode2020.SupportNewAniSendMode2020) ? r.c(SppProc$CMD_TYPE.SPP_APP_NEW_USER_DEFINE2020, arrayOfByte) : r.c(SppProc$CMD_TYPE.SPP_SET_USER_GIF, arrayOfByte);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.APP_NEW_USER_DEFINE2020, params)


def lieght_phone_gif32_word_attr(paramInt: int) -> None:
    """
        public static void F1(int paramInt) {
        k.d("octopus.CmdManager", "set32TextSpeed");
        byte[] arrayOfByte = new byte[3];
        arrayOfByte[0] = (byte)1;
        c0.A(paramInt, arrayOfByte, 1, false);
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_PHONE_GIF32_WORD_ATTR, arrayOfByte);
        p.s().A(arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_PHONE_GIF32_WORD_ATTR, params)


def set_play_stop_voice(paramByte: byte) -> bytearray:
    """
        public static byte[] F2(byte paramByte) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("0:1:2:");
        stringBuilder.append(paramByte);
        com.divoom.Divoom.utils.d.a(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SET_PLAY_STOP_VOICE, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_PLAY_STOP_VOICE, params)


def divoom_extern_cmd() -> None:
    """
        public static void G() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_KEY_FUNC.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_user_gif(paramInt: int) -> bytearray:
    """
        public static byte[] G0(int paramInt) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("getSetUserGifSandCmdStart ");
        stringBuilder.append(paramInt);
        k.d("octopus.CmdManager", stringBuilder.toString());
        HotUpdateHandle.o().A();
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SET_USER_GIF, new byte[] { 0, 2, b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_USER_GIF, params)


def set_vol(paramByte: byte) -> bytearray:
    """
        public static byte[] G2(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_VOL, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_VOL, params)


def set_divoom_leave_msg_gif(paramPixelBean: PixelBean) -> List[bytearray]:
    """
        public static List<byte[]> H(PixelBean paramPixelBean) {
        h h = new h();
        return h.c(h.f(paramPixelBean), SppProc$CMD_TYPE.SPP_SET_DIVOOM_LEAVE_MSG_GIF);
      }
    
    Parameters:
    	paramPixelBean (PixelBean)
    Returns:
    	List[bytearray]
    """

    params=[
        (paramPixelBean, 'PixelBean')
    ]

    return send_msg(enums.CmdType.SET_DIVOOM_LEAVE_MSG_GIF, params)


def set_sleep_ctrl_mode() -> bytearray:
    """
        public static byte[] H0() {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_CTRL_MODE, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_SLEEP_CTRL_MODE, params)


def set_alarm_voice_ctrl(paramByte1: byte, paramByte2: byte) -> bytearray:
    """
        public static byte[] H1(byte paramByte1, byte paramByte2) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("0:1:2:");
        stringBuilder.append(paramByte1);
        com.divoom.Divoom.utils.d.a(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SET_ALARM_VOICE_CTRL, new byte[] { paramByte1, paramByte2 }
    
    Parameters:
    	paramByte1 (byte)
    	paramByte2 (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte1, 'byte'),
        (paramByte2, 'byte')
    ]

    return send_msg(enums.CmdType.SET_ALARM_VOICE_CTRL, params)


def set_power_channel(paramInt: int) -> None:
    """
        public static void H2(int paramInt) {
        byte b = (byte)(paramInt & 0xFF);
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_POWER_CHANNEL, new byte[] { 1, b }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_POWER_CHANNEL, params)


def light_current_level() -> bytearray:
    """
        public static byte[] I() {
        com.divoom.Divoom.utils.d.a("----------->");
        return r.c(SppProc$CMD_TYPE.SPP_LIGHT_CURRENT_LEVEL, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.LIGHT_CURRENT_LEVEL, params)


def set_song_dis_ctrl() -> bytearray:
    """
        public static byte[] I0() {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SONG_DIS_CTRL, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_SONG_DIS_CTRL, params)


def set_gif_speed_cmd(paramInt: int) -> None:
    """
        public static void I1(int paramInt) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("setAniSpeed ");
        stringBuilder.append(paramInt);
        k.d("octopus.CmdManager", stringBuilder.toString());
        byte[] arrayOfByte = new byte[2];
        c0.A(paramInt, arrayOfByte, 0, false);
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_GIF_SPEED_CMD, arrayOfByte);
        p.s().F(arrayOfByte, true);
      }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_GIF_SPEED_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void I2() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_CLEAR_SYS_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void J() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_MUSIC_NAME_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def get_sound_ctrl() -> bytearray:
    """
        public static byte[] J0() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_SOUND_CTRL, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_SOUND_CTRL, params)


def set_auto_power_off(paramShort: short) -> bytearray:
    """
        public static byte[] J1(short paramShort) {
        byte b1 = (byte)(paramShort & 0xFF);
        byte b2 = (byte)(paramShort >> 8 & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_AUTO_POWER_OFF, new byte[] { b1, b2 }
    
    Parameters:
    	paramShort (short)
    Returns:
    	bytearray
    """

    params=[
        (paramShort, 'short')
    ]

    return send_msg(enums.CmdType.SET_AUTO_POWER_OFF, params)


def set_play_status(paramBoolean: bool) -> bytearray:
    """
        public static byte[] J2(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_PLAY_STATUS, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_PLAY_STATUS, params)


def get_dialy_time_ext2() -> bytearray:
    """
        public static byte[] K() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_DIALY_TIME_EXT2, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_DIALY_TIME_EXT2, params)


def divoom_extern_cmd() -> None:
    """
        public static void K0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_KARAOKE_CTRL.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd(paramBoolean: bool) -> None:
    """
        public static void K1(boolean paramBoolean) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_AUTO_CONNECT_CFG.value();
        byte b2 = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2 }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_vol(paramInt: int) -> bytearray:
    """
        public static byte[] K2(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SET_VOL, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_VOL, params)


def divoom_extern_cmd() -> None:
    """
        public static void L() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_WIRELESS_MIC_CTRL.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void L0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_RECORD_CTRL.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_poweron_voice_ctrl(paramByte: byte) -> bytearray:
    """
        public static byte[] L1(byte paramByte) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("1:2:");
        stringBuilder.append(paramByte);
        k.d("octopus.CmdManager", stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SET_POWERON_VOICE_CTRL, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_POWERON_VOICE_CTRL, params)


def divoom_extern_cmd(paramInt: int) -> None:
    """
        public static void L2(int paramInt) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SCREEN_DIR_CFG.value();
        byte b2 = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def modify_rhythm_items() -> bytearray:
    """
        public static byte[] M() {
        return r.c(SppProc$CMD_TYPE.SPP_MODIFY_RHYTHM_ITEMS, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.MODIFY_RHYTHM_ITEMS, params)


def set_poweron_voice_vol() -> None:
    """
        public static void M0() {
        byte[] arrayOfByte = new byte[2];
        arrayOfByte[0] = (byte)0;
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_POWERON_VOICE_VOL, arrayOfByte);
        p.s().A(arrayOfByte);
      }
    
    """

    params=[]

    return send_msg(enums.CmdType.SET_POWERON_VOICE_VOL, params)


def divoom_extern_cmd(paramBoolean: bool) -> None:
    """
        public static void M1(boolean paramBoolean) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SppExtCarMode.value();
        byte b2 = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, 1, b2 }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd(paramByte: byte) -> None:
    """
        public static void M2(byte paramByte) {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SCREEN_MIRROR_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, paramByte }
    
    Parameters:
    	paramByte (byte)
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void N0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_GET_NEW_POWER_ON_CHANNEL.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd(paramInt: int) -> None:
    """
        public static void N1(int paramInt) {
        int i = SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_GIF_PLAY_TIME_CFG.value();
        byte[] arrayOfByte = c0.d(c0.d(new byte[0], i, 1, false), paramInt, 2, false);
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, arrayOfByte);
        p.s().A(arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def scroll(paramInt1: int, paramInt2: int) -> None:
    """
        public static void N2(int paramInt1, int paramInt2) {
        byte b1 = (byte)paramInt1;
        byte b2 = (byte)(paramInt2 & 0xFF);
        byte b3 = (byte)(paramInt2 >> 8 & 0xFF);
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("mode ");
        stringBuilder.append(paramInt1);
        stringBuilder.append(" speed ");
        stringBuilder.append(paramInt2);
        k.d("octopus.CmdManager", stringBuilder.toString());
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SCROLL, new byte[] { 0, b1, b2, b3 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SCROLL, params)


def drawing_encode_pic(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] O(int paramInt, byte[] paramArrayOfbyte) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte[] arrayOfByte = GlobalApplication.i().j().PixelEncodeSixteen(paramArrayOfbyte, 1, 0);
        paramArrayOfbyte = new byte[arrayOfByte.length + 1 + 2];
        paramArrayOfbyte[0] = (byte)(byte)(paramInt & 0xFF);
        paramArrayOfbyte[1] = (byte)(byte)(arrayOfByte.length & 0xFF);
        paramArrayOfbyte[2] = (byte)(byte)(arrayOfByte.length >> 8 & 0xFF);
        System.arraycopy(arrayOfByte, 0, paramArrayOfbyte, 3, arrayOfByte.length);
        return r.c(SppProc$CMD_TYPE.SPP_DRAWING_ENCODE_PIC, paramArrayOfbyte);
      }
    
    Parameters:
    	paramInt (int)
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int'),
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.DRAWING_ENCODE_PIC, params)


def set_temp_type() -> bytearray:
    """
        public static byte[] O0() {
        return r.c(SppProc$CMD_TYPE.SPP_SET_TEMP_TYPE, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_TEMP_TYPE, params)


def set_connected_flag(paramByte: byte) -> bytearray:
    """
        public static byte[] O1(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_CONNECTED_FLAG, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_CONNECTED_FLAG, params)


def set_sd_play_music_id(paramInt: int) -> bytearray:
    """
        public static byte[] O2(int paramInt) {
        byte b1 = (byte)(paramInt & 0xFF);
        byte b2 = (byte)(paramInt >> 8 & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_SD_PLAY_MUSIC_ID, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_SD_PLAY_MUSIC_ID, params)


def sand_paint_ctrl(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] P(int paramInt, byte[] paramArrayOfbyte) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        paramArrayOfbyte = GlobalApplication.i().j().PixelEncodeSixteen(paramArrayOfbyte, 1, 0);
        byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 1 + 1 + 2];
        arrayOfByte[0] = (byte)0;
        arrayOfByte[1] = (byte)(byte)(paramInt & 0xFF);
        arrayOfByte[2] = (byte)(byte)(paramArrayOfbyte.length & 0xFF);
        arrayOfByte[3] = (byte)(byte)(paramArrayOfbyte.length >> 8 & 0xFF);
        System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 4, paramArrayOfbyte.length);
        return r.c(SppProc$CMD_TYPE.SPP_SAND_PAINT_CTRL, arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int'),
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.SAND_PAINT_CTRL, params)


def get_time_manage_ctrl(paramByte: byte) -> bytearray:
    """
        public static byte[] P0(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_GET_TIME_MANAGE_CTRL, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.GET_TIME_MANAGE_CTRL, params)


def divoom_extern_cmd(paramInt: int) -> None:
    """
        public static void P1(int paramInt) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_USER_DEFINE_TIME.value();
        byte b2 = (byte)(paramInt & 0xFF);
        byte b3 = (byte)(paramInt >> 8 & 0xFF);
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2, b3 }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_sd_music_position(paramInt: int) -> bytearray:
    """
        public static byte[] P2(int paramInt) {
        byte b1 = (byte)(paramInt & 0xFF);
        byte b2 = (byte)(paramInt >> 8 & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_SD_MUSIC_POSITION, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_SD_MUSIC_POSITION, params)


def get_net_temp_disp_info() -> bytearray:
    """
        public static byte[] Q() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_NET_TEMP_DISP_INFO, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_NET_TEMP_DISP_INFO, params)


def set_system_time() -> bytearray:
    """
        public static byte[] Q0() {
        Calendar calendar = Calendar.getInstance();
        int i = calendar.get(1);
        int j = i / 100;
        int k = calendar.get(2);
        int m = calendar.get(7) - 1;
        int n = calendar.get(5);
        int i1 = calendar.get(11);
        int i2 = calendar.get(12);
        int i3 = calendar.get(13);
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("year: ");
        stringBuilder.append(i);
        stringBuilder.append("day: ");
        stringBuilder.append(n);
        stringBuilder.append("hour : ");
        stringBuilder.append(i1);
        stringBuilder.append(" , minute : ");
        stringBuilder.append(i2);
        stringBuilder.append(" , second : ");
        stringBuilder.append(i3);
        stringBuilder.append("week: ");
        stringBuilder.append(m);
        k.d("octopus.CmdManager", stringBuilder.toString());
        byte b1 = (byte)(i % 100 & 0xFF);
        byte b2 = (byte)(j & 0xFF);
        byte b3 = (byte)(k + 1 & 0xFF);
        byte b4 = (byte)(n & 0xFF);
        byte b5 = (byte)(i1 & 0xFF);
        byte b6 = (byte)(i2 & 0xFF);
        byte b7 = (byte)(i3 & 0xFF);
        byte b8 = (byte)(m & 0xFF);
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_SYSTEM_TIME, new byte[] { b1, b2, b3, b4, b5, b6, b7, b8 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_SYSTEM_TIME, params)


def modify_rhythm_items(paramInt: int) -> bytearray:
    """
        public static byte[] Q1(int paramInt) {
        byte b = (byte)(paramInt & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_MODIFY_RHYTHM_ITEMS, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.MODIFY_RHYTHM_ITEMS, params)


def divoom_extern_cmd() -> None:
    """
        public static void R() {
        int i = SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_GIF_TYPE.value();
        byte[] arrayOfByte = c0.d(new byte[0], i, 1, false);
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, arrayOfByte);
        p.s().A(arrayOfByte);
      }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_hpur_type() -> bytearray:
    """
        public static byte[] R0() {
        return r.c(SppProc$CMD_TYPE.SPP_SET_HPUR_TYPE, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_HPUR_TYPE, params)


def del_leave_msg_gif() -> bytearray:
    """
        public static byte[] R1() {
        return r.c(SppProc$CMD_TYPE.SPP_DEL_LEAVE_MSG_GIF, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.DEL_LEAVE_MSG_GIF, params)


def set_sleep_color(paramByte1: byte, paramByte2: byte, paramByte3: byte) -> bytearray:
    """
        public static byte[] R2(byte paramByte1, byte paramByte2, byte paramByte3) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_COLOR, new byte[] { paramByte1, paramByte2, paramByte3 }
    
    Parameters:
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte')
    ]

    return send_msg(enums.CmdType.SET_SLEEP_COLOR, params)


def get_tool_info(paramInt: int) -> bytearray:
    """
        public static byte[] S0(int paramInt) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_GET_TOOL_INFO, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.GET_TOOL_INFO, params)


def divoom_extern_cmd() -> None:
    """
        public static void S1() {
        // Byte code:
        //   0: invokestatic i : ()Lcom/divoom/Divoom/GlobalApplication;
        //   3: invokestatic s : (Landroid/content/Context;)Ljava/lang/String;
        //   6: astore_0
        //   7: aload_0
        //   8: invokestatic isEmpty : (Ljava/lang/CharSequence;)Z
        //   11: ifne -> 151
        //   14: iconst_0
        //   15: istore_1
        //   16: iload_1
        //   17: bipush #16
        //   19: if_icmpge -> 151
        //   22: aload_0
        //   23: bipush #16
        //   25: anewarray java/lang/String
        //   28: dup
        //   29: iconst_0
        //   30: ldc_w 'en'
        //   33: aastore
        //   34: dup
        //   35: iconst_1
        //   36: ldc_w 'zh-hans'
        //   39: aastore
        //   40: dup
        //   41: iconst_2
        //   42: ldc_w 'zh-hant'
        //   45: aastore
        //   46: dup
        //   47: iconst_3
        //   48: ldc_w 'ja'
        //   51: aastore
        //   52: dup
        //   53: iconst_4
        //   54: ldc_w 'th'
        //   57: aastore
        //   58: dup
        //   59: iconst_5
        //   60: ldc_w 'fr'
        //   63: aastore
        //   64: dup
        //   65: bipush #6
        //   67: ldc_w 'it'
        //   70: aastore
        //   71: dup
        //   72: bipush #7
        //   74: ldc_w 'iv'
        //   77: aastore
        //   78: dup
        //   79: bipush #8
        //   81: ldc_w 'es'
        //   84: aastore
        //   85: dup
        //   86: bipush #9
        //   88: ldc_w 'de'
        //   91: aastore
        //   92: dup
        //   93: bipush #10
        //   95: ldc_w 'ru'
        //   98: aastore
        //   99: dup
        //   100: bipush #11
        //   102: ldc_w 'pt'
        //   105: aastore
        //   106: dup
        //   107: bipush #12
        //   109: ldc_w 'ko'
        //   112: aastore
        //   113: dup
        //   114: bipush #13
        //   116: ldc_w 'nl'
        //   119: aastore
        //   120: dup
        //   121: bipush #14
        //   123: ldc_w 'uk'
        //   126: aastore
        //   127: dup
        //   128: bipush #15
        //   130: ldc_w 'ms'
        //   133: aastore
        //   134: iload_1
        //   135: aaload
        //   136: invokevirtual startsWith : (Ljava/lang/String;)Z
        //   139: ifeq -> 145
        //   142: goto -> 153
        //   145: iinc #1, 1
        //   148: goto -> 16
        //   151: iconst_0
        //   152: istore_1
        //   153: new java/lang/StringBuilder
        //   156: dup
        //   157: invokespecial <init> : ()V
        //   160: astore_2
        //   161: aload_2
        //   162: ldc_w 'setDeviceLanguage '
        //   165: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
        //   168: pop
        //   169: aload_2
        //   170: aload_0
        //   171: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
        //   174: pop
        //   175: aload_2
        //   176: ldc_w ' '
        //   179: invokevirtual append : (Ljava/lang/String;)Ljava/lang/StringBuilder;
        //   182: pop
        //   183: aload_2
        //   184: iload_1
        //   185: invokevirtual append : (I)Ljava/lang/StringBuilder;
        //   188: pop
        //   189: ldc 'octopus.CmdManager'
        //   191: aload_2
        //   192: invokevirtual toString : ()Ljava/lang/String;
        //   195: invokestatic d : (Ljava/lang/String;Ljava/lang/String;)V
        //   198: getstatic com/divoom/Divoom/bluetooth/SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_LANGUAGE : Lcom/divoom/Divoom/bluetooth/SppProc$EXT_CMD_TYPE;
        //   201: invokevirtual value : ()I
        //   204: i2b
        //   205: istore_3
        //   206: iload_1
        //   207: i2b
        //   208: istore #4
        //   210: getstatic com/divoom/Divoom/bluetooth/SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD : Lcom/divoom/Divoom/bluetooth/SppProc$CMD_TYPE;
        //   213: iconst_2
        //   214: newarray byte
        //   216: dup
        //   217: iconst_0
        //   218: iload_3
        //   219: bastore
        //   220: dup
        //   221: iconst_1
        //   222: iload #4
        //   224: bastore
        //   225: invokestatic c : (Lcom/divoom/Divoom/bluetooth/SppProc$CMD_TYPE;[B)[B
        //   228: astore_0
        //   229: invokestatic s : ()Lcom/divoom/Divoom/bluetooth/p;
        //   232: aload_0
        //   233: invokevirtual A : ([B)V
        //   236: return
      }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_sleep_ctrl_mode(paramInt: int) -> bytearray:
    """
        public static byte[] S2(int paramInt) {
        byte b = (byte)(paramInt & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_CTRL_MODE, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_SLEEP_CTRL_MODE, params)


def set_ancs_notice_pic(paramInt1: int, paramInt2: int) -> bytearray:
    """
        public static byte[] T(int paramInt1, int paramInt2) {
        byte[] arrayOfByte = com.divoom.Divoom.utils.r0.d.j(paramInt2);
        byte b1 = (byte)(paramInt1 & 0xFF);
        byte b2 = arrayOfByte[0];
        byte b3 = arrayOfByte[1];
        byte b4 = arrayOfByte[2];
        return r.c(SppProc$CMD_TYPE.SPP_SET_ANCS_NOTICE_PIC, new byte[] { b1, b2, b3, b4 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SET_ANCS_NOTICE_PIC, params)


def app_send_file_data(paramInt: int, paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] T0(int paramInt, byte[] paramArrayOfbyte) {
        byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 2];
        arrayOfByte[0] = (byte)(byte)(paramInt & 0xFF);
        arrayOfByte[1] = (byte)(byte)(paramInt >> 8 & 0xFF);
        System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 2, paramArrayOfbyte.length);
        return r.c(SppProc$CMD_TYPE.SPP_APP_SEND_FILE_DATA, arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int'),
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.APP_SEND_FILE_DATA, params)


def device_update_gif(paramBoolean: bool) -> None:
    """
        public static void T1(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DEVICE_UPDATE_GIF, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.DEVICE_UPDATE_GIF, params)


def set_sleep_light(paramByte: byte) -> bytearray:
    """
        public static byte[] T2(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_SLEEP_LIGHT, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_SLEEP_LIGHT, params)


def app_update_file_info(paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] U0(byte[] paramArrayOfbyte) {
        return r.c(SppProc$CMD_TYPE.SPP_APP_UPDATE_FILE_INFO, paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.APP_UPDATE_FILE_INFO, params)


def set_song_dis_ctrl(paramBoolean: bool) -> bytearray:
    """
        public static byte[] U2(boolean paramBoolean) {
        boolean bool = true;
        if (paramBoolean != true)
          bool = false; 
        byte b = (byte)bool;
        return r.c(SppProc$CMD_TYPE.SPP_SET_SONG_DIS_CTRL, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_SONG_DIS_CTRL, params)


def set_peripherals_device_ctrl() -> None:
    """
        public static void V() {
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_PERIPHERALS_DEVICE_CTRL, new byte[] { 2, 32 }
    
    """

    params=[]

    return send_msg(enums.CmdType.SET_PERIPHERALS_DEVICE_CTRL, params)


def divoom_extern_cmd() -> None:
    """
        public static void V0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SAVE_VOLUME_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def drawing_pad_exit() -> bytearray:
    """
        public static byte[] V1() {
        return r.c(SppProc$CMD_TYPE.SPP_DRAWING_PAD_EXIT, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.DRAWING_PAD_EXIT, params)


def set_sound_ctrl(paramBoolean: bool) -> bytearray:
    """
        public static byte[] V2(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_SOUND_CTRL, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_SOUND_CTRL, params)


def set_android_ancs(paramInt: int) -> bytearray:
    """
        public static byte[] W(int paramInt) {
        int i = paramInt;
        if (paramInt >= 8)
          i = paramInt + 1; 
        byte b = (byte)(i & 0xFF);
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("getPlayNotify            ");
        stringBuilder.append(i);
        LogUtil.e(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SET_ANDROID_ANCS, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_ANDROID_ANCS, params)


def get_stdb_mode() -> bytearray:
    """
        public static byte[] W0() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_STDB_MODE, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_STDB_MODE, params)


def set_energy_ctrl(paramBoolean: bool) -> bytearray:
    """
        public static byte[] W1(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_ENERGY_CTRL, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_ENERGY_CTRL, params)


def get_play_status() -> bytearray:
    """
        public static byte[] X() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_PLAY_STATUS, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_PLAY_STATUS, params)


def eye_guard_info(paramBoolean: bool) -> None:
    """
        public static void X1(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_EYE_GUARD_INFO, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.EYE_GUARD_INFO, params)


def divoom_extern_cmd(paramByte: byte) -> None:
    """
        public static void X2(byte paramByte) {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_RECORD_CTRL.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, paramByte }
    
    Parameters:
    	paramByte (byte)
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def get_play_voice_status() -> bytearray:
    """
        public static byte[] Y() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_PLAY_VOICE_STATUS, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_PLAY_VOICE_STATUS, params)


def drawing_encode_movie_play(paramInt: int, paramArrayOfbyte: bytearray) -> None:
    """
        public static void Y0(int paramInt, byte[] paramArrayOfbyte) {
        byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 4];
        arrayOfByte[0] = (byte)(byte)(paramInt & 0xFF);
        arrayOfByte[1] = (byte)(byte)(paramInt >> 8 & 0xFF);
        arrayOfByte[2] = (byte)(byte)(paramArrayOfbyte.length & 0xFF);
        arrayOfByte[3] = (byte)(byte)(paramArrayOfbyte.length >> 8 & 0xFF);
        System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 4, paramArrayOfbyte.length);
        paramArrayOfbyte = r.c(SppProc$CMD_TYPE.SPP_DRAWING_ENCODE_MOVIE_PLAY, arrayOfByte);
        p.s().A(paramArrayOfbyte);
      }
    
    Parameters:
    	paramInt (int)
    	paramArrayOfbyte (bytearray)
    """

    params=[
        (paramInt, 'int'),
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.DRAWING_ENCODE_MOVIE_PLAY, params)


def set_fm_automatic_search() -> bytearray:
    """
        public static byte[] Y1() {
        return r.c(SppProc$CMD_TYPE.SPP_SET_FM_AUTOMATIC_SEARCH, new byte[] { 0 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_FM_AUTOMATIC_SEARCH, params)


def system_try_color(paramInt: int) -> bytearray:
    """
        public static byte[] Y2(int paramInt) {
        byte b1 = (byte)Color.red(paramInt);
        byte b2 = (byte)Color.green(paramInt);
        byte b3 = (byte)Color.blue(paramInt);
        return r.c(SppProc$CMD_TYPE.SPP_SYSTEM_TRY_COLOR, new byte[] { b1, b2, b3 }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SYSTEM_TRY_COLOR, params)


def get_vol() -> bytearray:
    """
        public static byte[] Z() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_VOL, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_VOL, params)


def drawing_ctrl_movie_play(paramBoolean: bool) -> bytearray:
    """
        public static byte[] Z0(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_DRAWING_CTRL_MOVIE_PLAY, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.DRAWING_CTRL_MOVIE_PLAY, params)


def set_fm_current_freq(paramFloat: float) -> bytearray:
    """
        public static byte[] Z1(float paramFloat) {
        int i = (int)(paramFloat * 10.0F);
        byte b1 = (byte)(i % 100);
        byte b2 = (byte)(i / 100);
        return r.c(SppProc$CMD_TYPE.SPP_SET_FM_CURRENT_FREQ, new byte[] { b1, b2 }
    
    Parameters:
    	paramFloat (float)
    Returns:
    	bytearray
    """

    params=[
        (paramFloat, 'float')
    ]

    return send_msg(enums.CmdType.SET_FM_CURRENT_FREQ, params)


def send_app_newest_time() -> bytearray:
    """
        public static byte[] a() {
        return r.c(SppProc$CMD_TYPE.SPP_SEND_APP_NEWEST_TIME, new byte[] { -1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SEND_APP_NEWEST_TIME, params)


def spp_power_on_off_info() -> bytearray:
    """
        public static byte[] a0() {
        return r.c(SppProc$CMD_TYPE.SPP_SPP_POWER_ON_OFF_INFO, new byte[] { 0 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SPP_POWER_ON_OFF_INFO, params)


def app_big64_user_define(paramInt1: int, paramInt2: int) -> None:
    """
        public static void a1(int paramInt1, int paramInt2) {
        byte[] arrayOfByte1 = new byte[6];
        arrayOfByte1[0] = (byte)4;
        c0.y(paramInt2, 4, arrayOfByte1, 1, false);
        arrayOfByte1[5] = (byte)(byte)paramInt1;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("preViewUserGif  =============   ");
        stringBuilder.append(Arrays.toString(arrayOfByte1));
        LogUtil.e(stringBuilder.toString());
        byte[] arrayOfByte2 = r.c(SppProc$CMD_TYPE.SPP_APP_BIG64_USER_DEFINE, arrayOfByte1);
        p.s().D(arrayOfByte2);
      }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.APP_BIG64_USER_DEFINE, params)


def set_temp_type(paramBoolean: bool) -> bytearray:
    """
        public static byte[] a3(boolean paramBoolean) {
        boolean bool = true;
        if (paramBoolean != true)
          bool = false; 
        byte b = (byte)bool;
        return r.c(SppProc$CMD_TYPE.SPP_SET_TEMP_TYPE, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_TEMP_TYPE, params)


def set_power_channel() -> None:
    """
        public static void b0() {
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_POWER_CHANNEL, new byte[] { 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.SET_POWER_CHANNEL, params)


def app_big64_user_define(paramInt: int) -> None:
    """
        public static void b1(int paramInt) {
        byte[] arrayOfByte = new byte[2];
        arrayOfByte[0] = (byte)5;
        arrayOfByte[1] = (byte)(byte)paramInt;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("removeAllUserGif  =============   ");
        stringBuilder.append(Arrays.toString(arrayOfByte));
        LogUtil.e(stringBuilder.toString());
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_APP_BIG64_USER_DEFINE, arrayOfByte);
        p.s().D(arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.APP_BIG64_USER_DEFINE, params)


def set_hpur_type(paramBoolean: bool) -> bytearray:
    """
        public static byte[] b3(boolean paramBoolean) {
        boolean bool = true;
        if (paramBoolean != true)
          bool = false; 
        byte b = (byte)bool;
        return r.c(SppProc$CMD_TYPE.SPP_SET_HPUR_TYPE, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_HPUR_TYPE, params)


def app_need_get_music_list() -> bytearray:
    """
        public static byte[] c0() {
        return r.c(SppProc$CMD_TYPE.SPP_APP_NEED_GET_MUSIC_LIST, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.APP_NEED_GET_MUSIC_LIST, params)


def app_big64_user_define(paramInt1: int, paramInt2: int) -> None:
    """
        public static void c1(int paramInt1, int paramInt2) {
        byte[] arrayOfByte = new byte[6];
        arrayOfByte[0] = (byte)3;
        c0.y(paramInt2, 4, arrayOfByte, 1, false);
        arrayOfByte[5] = (byte)(byte)paramInt1;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("removeUserGif  =============   ");
        stringBuilder.append(Arrays.toString(arrayOfByte));
        LogUtil.e(stringBuilder.toString());
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_APP_BIG64_USER_DEFINE, arrayOfByte);
        p.s().D(arrayOfByte);
      }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.APP_BIG64_USER_DEFINE, params)


def divoom_extern_cmd(paramArrayOfbyte: bytearray) -> bool:
    """
        public static boolean c2(byte[] paramArrayOfbyte) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("setKeyConfig       ");
        stringBuilder.append(Arrays.toString(paramArrayOfbyte));
        LogUtil.e(stringBuilder.toString());
        int i = paramArrayOfbyte.length;
        byte[] arrayOfByte = new byte[i + 2];
        arrayOfByte[0] = (byte)(byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_KEY_FUNC.value();
        arrayOfByte[1] = (byte)1;
        for (byte b = 0; b < i; b++)
          arrayOfByte[b + 2] = (byte)paramArrayOfbyte[b]; 
        paramArrayOfbyte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, arrayOfByte);
        p.s().F(paramArrayOfbyte, false);
        return true;
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bool
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_tool_info(paramBoolean: bool, paramInt1: int, paramInt2: int) -> bytearray:
    """
        public static byte[] c3(boolean paramBoolean, int paramInt1, int paramInt2) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte[] arrayOfByte = new byte[4];
        arrayOfByte[0] = (byte)3;
        arrayOfByte[1] = (byte)(byte)paramBoolean;
        arrayOfByte[2] = (byte)(byte)(paramInt1 & 0xFF);
        arrayOfByte[3] = (byte)(byte)(paramInt2 & 0xFF);
        k.d("octopus.CmdManager", a0.l(arrayOfByte));
        return r.c(SppProc$CMD_TYPE.SPP_SET_TOOL_INFO, arrayOfByte);
      }
    
    Parameters:
    	paramBoolean (bool)
    	paramInt1 (int)
    	paramInt2 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool'),
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SET_TOOL_INFO, params)


def set_new_mix_music_mode(paramInt: int) -> None:
    """
        public static void d(int paramInt) {
        byte[] arrayOfByte = new byte[2];
        arrayOfByte[0] = (byte)(byte)paramInt;
        arrayOfByte[1] = (byte)-1;
        if (X0()) {
          arrayOfByte = c.b(SppProc$CMD_TYPE.SPP_SET_NEW_MIX_MUSIC_MODE, arrayOfByte);
          d.m().write(arrayOfByte);
        }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_NEW_MIX_MUSIC_MODE, params)


def divoom_extern_cmd() -> None:
    """
        public static void d0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_CLEAR_SYS_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void d1() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_KEY_FUNC.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 2 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def spp_light_arrow_switch(paramByte: byte) -> bytearray:
    """
        public static byte[] d2(byte paramByte) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("----------->setLightMode");
        stringBuilder.append(paramByte);
        com.divoom.Divoom.utils.d.a(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SPP_LIGHT_ARROW_SWITCH, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SPP_LIGHT_ARROW_SWITCH, params)


def set_tool_info(paramInt: int) -> bytearray:
    """
        public static byte[] d3(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SET_TOOL_INFO, new byte[] { 0, b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_TOOL_INFO, params)


def set_mul_device_ctrl(paramMultiModeEnum: MultiModeEnum) -> bytearray:
    """
        public static byte[] e(MultiModeEnum paramMultiModeEnum) {
        byte b1 = (byte)MultiControlEnum.mirrorOrfit._value;
        byte b2 = (byte)paramMultiModeEnum._value;
        return r.c(SppProc$CMD_TYPE.SPP_SET_MUL_DEVICE_CTRL, new byte[] { b1, b2 }
    
    Parameters:
    	paramMultiModeEnum (MultiModeEnum)
    Returns:
    	bytearray
    """

    params=[
        (paramMultiModeEnum, 'MultiModeEnum')
    ]

    return send_msg(enums.CmdType.SET_MUL_DEVICE_CTRL, params)


def sand_paint_ctrl() -> bytearray:
    """
        public static byte[] e0() {
        return r.c(SppProc$CMD_TYPE.SPP_SAND_PAINT_CTRL, new byte[] { 1 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SAND_PAINT_CTRL, params)


def reset_notifications() -> bytearray:
    """
        public static byte[] e1() {
        return r.c(SppProc$CMD_TYPE.SPP_RESET_NOTIFICATIONS, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.RESET_NOTIFICATIONS, params)


def set_box_mode(light_mode: enums.LightMode) -> bytearray:
    """
        public static byte[] e2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, 0, 0, 0, 0, 0 }
    
    Parameters:
    	light_mode (enums.LightMode)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode')
        (0, 'bytes'), (0, 'bytes'), (0, 'bytes'), (0, 'bytes'), (0, 'bytes'),
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def set_tool_info(paramBoolean: bool, paramInt1: int, paramInt2: int) -> bytearray:
    """
        public static byte[] e3(boolean paramBoolean, int paramInt1, int paramInt2) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte[] arrayOfByte = new byte[6];
        arrayOfByte[0] = (byte)1;
        arrayOfByte[1] = (byte)(byte)paramBoolean;
        arrayOfByte[2] = (byte)(byte)(paramInt1 & 0xFF);
        arrayOfByte[3] = (byte)(byte)((paramInt1 & 0xFF00) >> 8);
        arrayOfByte[4] = (byte)(byte)(paramInt2 & 0xFF);
        arrayOfByte[5] = (byte)(byte)((paramInt2 & 0xFF00) >> 8);
        k.d("octopus.CmdManager", a0.l(arrayOfByte));
        return r.c(SppProc$CMD_TYPE.SPP_SET_TOOL_INFO, arrayOfByte);
      }
    
    Parameters:
    	paramBoolean (bool)
    	paramInt1 (int)
    	paramInt2 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool'),
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SET_TOOL_INFO, params)


def set_mul_device_ctrl(paramMultiShowEnum: MultiShowEnum) -> bytearray:
    """
        public static byte[] f(MultiShowEnum paramMultiShowEnum) {
        byte b1 = (byte)MultiControlEnum.setMultiMode._value;
        byte b2 = (byte)paramMultiShowEnum._value;
        return r.c(SppProc$CMD_TYPE.SPP_SET_MUL_DEVICE_CTRL, new byte[] { b1, b2 }
    
    Parameters:
    	paramMultiShowEnum (MultiShowEnum)
    Returns:
    	bytearray
    """

    params=[
        (paramMultiShowEnum, 'MultiShowEnum')
    ]

    return send_msg(enums.CmdType.SET_MUL_DEVICE_CTRL, params)


def set_box_mode(light_mode: enums.LightMode, paramByte: byte) -> bytearray:
    """
        public static byte[] f2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, paramByte }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def set_tool_info(paramInt: int) -> bytearray:
    """
        public static byte[] f3(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SET_TOOL_INFO, new byte[] { 2, b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_TOOL_INFO, params)


def divoom_extern_cmd(paramInt: int) -> None:
    """
        public static void g(int paramInt) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_CLEAR_USER_DEFINE_INDEX.value();
        byte b2 = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd() -> None:
    """
        public static void g0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SCREEN_DIR_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_user_gif(paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] g1(byte[] paramArrayOfbyte) {
        byte[] arrayOfByte = com.divoom.Divoom.led.b.a(paramArrayOfbyte);
        if (arrayOfByte == null)
          return null; 
        paramArrayOfbyte = new byte[arrayOfByte.length + 3];
        paramArrayOfbyte[0] = (byte)1;
        paramArrayOfbyte[1] = (byte)(byte)(arrayOfByte.length & 0xFF);
        paramArrayOfbyte[2] = (byte)(byte)(arrayOfByte.length >> 8 & 0xFF);
        System.arraycopy(arrayOfByte, 0, paramArrayOfbyte, 3, arrayOfByte.length);
        return r.c(SppProc$CMD_TYPE.SPP_SET_USER_GIF, paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.SET_USER_GIF, params)


def set_box_mode(light_mode: enums.LightMode, paramByte1: byte, paramByte2: byte, paramByte3: byte, paramByte4: byte) -> bytearray:
    """
        public static byte[] g2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4) {
        byte[] arrayOfByte = new byte[6];
        arrayOfByte[0] = (byte)paramSppProc$LIGHT_MODE.getCmd_data()[0];
        arrayOfByte[1] = (byte)paramByte1;
        arrayOfByte[2] = (byte)paramByte2;
        arrayOfByte[3] = (byte)paramByte3;
        arrayOfByte[4] = (byte)paramByte4;
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, arrayOfByte);
      }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    	paramByte4 (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte'),
        (paramByte4, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def change_mode(work_mode: enums.WorkMode) -> bytearray:
    """
        public static byte[] g3(SppProc$WORK_MODE paramSppProc$WORK_MODE) {
        byte[] arrayOfByte = new byte[1];
        arrayOfByte[0] = (byte)0;
        arrayOfByte[0] = paramSppProc$WORK_MODE.value();
        return r.c(SppProc$CMD_TYPE.SPP_CHANGE_MODE, arrayOfByte);
      }
    
    Parameters:
    	work_mode (enums.WorkMode)
    Returns:
    	bytearray
    """

    params=[
        (work_mode, 'enums.WorkMode')
    ]

    return send_msg(enums.CmdType.CHANGE_MODE, params)


def set_mul_device_ctrl() -> bytearray:
    """
        public static byte[] h() {
        byte b = (byte)MultiControlEnum.exitMulti._value;
        return r.c(SppProc$CMD_TYPE.SPP_SET_MUL_DEVICE_CTRL, new byte[] { b }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_MUL_DEVICE_CTRL, params)


def divoom_extern_cmd() -> None:
    """
        public static void h0() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SCREEN_MIRROR_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def divoom_extern_cmd(paramBoolean: bool) -> None:
    """
        public static void h1(boolean paramBoolean) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_SAVE_VOLUME_CFG.value();
        byte b2 = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2 }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_box_mode(light_mode: enums.LightMode, paramByte1: byte, paramByte2: byte, paramByte3: byte, paramByte4: byte, paramByte5: byte, paramByte6: byte, paramByte7: byte) -> bytearray:
    """
        public static byte[] h2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4, byte paramByte5, byte paramByte6, byte paramByte7) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, paramByte1, paramByte2, paramByte3, paramByte4, paramByte5, paramByte6, paramByte7 }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    	paramByte4 (byte)
    	paramByte5 (byte)
    	paramByte6 (byte)
    	paramByte7 (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte'),
        (paramByte4, 'byte'),
        (paramByte5, 'byte'),
        (paramByte6, 'byte'),
        (paramByte7, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def drawing_mul_pad_enter(paramInt: int) -> bytearray:
    """
        public static byte[] h3(int paramInt) {
        byte b1 = (byte)Color.red(paramInt);
        byte b2 = (byte)Color.green(paramInt);
        byte b3 = (byte)Color.blue(paramInt);
        return r.c(SppProc$CMD_TYPE.SPP_DRAWING_MUL_PAD_ENTER, new byte[] { b1, b2, b3 }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DRAWING_MUL_PAD_ENTER, params)


def set_peripherals_device_ctrl() -> None:
    """
        public static void i() {
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_PERIPHERALS_DEVICE_CTRL, new byte[] { 4 }
    
    """

    params=[]

    return send_msg(enums.CmdType.SET_PERIPHERALS_DEVICE_CTRL, params)


def set_peripherals_device_ctrl(paramBoolean: bool) -> None:
    """
        public static void i1(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SET_PERIPHERALS_DEVICE_CTRL, new byte[] { 1, b }
    
    Parameters:
    	paramBoolean (bool)
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_PERIPHERALS_DEVICE_CTRL, params)


def set_box_mode(light_mode: enums.LightMode, paramByte1: byte, paramByte2: byte, paramByte3: byte, paramByte4: byte, paramByte5: byte) -> bytearray:
    """
        public static byte[] i2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4, byte paramByte5) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, paramByte1, paramByte2, paramByte3, paramByte4, paramByte5 }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    	paramByte4 (byte)
    	paramByte5 (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte'),
        (paramByte4, 'byte'),
        (paramByte5, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def drawing_mul_encode_gif_play() -> bytearray:
    """
        public static byte[] i3() {
        return r.c(SppProc$CMD_TYPE.SPP_DRAWING_MUL_ENCODE_GIF_PLAY, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.DRAWING_MUL_ENCODE_GIF_PLAY, params)


def app_get_user_define_info(paramInt: int) -> None:
    """
        public static void j(int paramInt) {
        byte b = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_APP_GET_USER_DEFINE_INFO, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.APP_GET_USER_DEFINE_INFO, params)


def get_sd_music_info() -> bytearray:
    """
        public static byte[] j0() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_SD_MUSIC_INFO, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_SD_MUSIC_INFO, params)


def divoom_extern_cmd(paramInt: int) -> None:
    """
        public static void j1(int paramInt) {
        byte b1 = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_USE_USER_DEFINE_INDEX.value();
        byte b2 = (byte)paramInt;
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_box_mode() -> bytearray:
    """
        public static byte[] j2() {
        byte b = (byte)LightEnum.HOT_MODE._value;
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def get_alarm_time_scene() -> bytearray:
    """
        public static byte[] k() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_ALARM_TIME_SCENE, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_ALARM_TIME_SCENE, params)


def get_sd_music_list(paramInt1: int, paramInt2: int) -> bytearray:
    """
        public static byte[] k0(int paramInt1, int paramInt2) {
        byte b1 = (byte)(paramInt1 & 0xFF);
        byte b2 = (byte)(paramInt1 >> 8 & 0xFF);
        byte b3 = (byte)(paramInt2 & 0xFF);
        byte b4 = (byte)(paramInt2 >> 8 & 0xFF);
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("startId ");
        stringBuilder.append(paramInt1);
        stringBuilder.append(", end ");
        stringBuilder.append(paramInt2);
        k.d("octopus.CmdManager", stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_GET_SD_MUSIC_LIST, new byte[] { b1, b2, b3, b4 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.GET_SD_MUSIC_LIST, params)


def send_cur_net_temp(paramByte1: byte, paramByte2: byte) -> bytearray:
    """
        public static byte[] k1(byte paramByte1, byte paramByte2) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("------");
        stringBuilder.append(paramByte1);
        stringBuilder.append("  typeDemo=");
        stringBuilder.append(paramByte2);
        com.divoom.Divoom.utils.d.b(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SEND_CUR_NET_TEMP, new byte[] { paramByte1, paramByte2 }
    
    Parameters:
    	paramByte1 (byte)
    	paramByte2 (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte1, 'byte'),
        (paramByte2, 'byte')
    ]

    return send_msg(enums.CmdType.SEND_CUR_NET_TEMP, params)


def set_system_bright(paramByte: byte) -> bytearray:
    """
        public static byte[] k2(byte paramByte) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("-----------> light");
        stringBuilder.append(paramByte);
        com.divoom.Divoom.utils.d.a(stringBuilder.toString());
        return r.c(SppProc$CMD_TYPE.SPP_SET_SYSTEM_BRIGHT, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_SYSTEM_BRIGHT, params)


def app_big64_user_define() -> None:
    """
        public static void k3() {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_APP_BIG64_USER_DEFINE, new byte[] { 2 }
    
    """

    params=[]

    return send_msg(enums.CmdType.APP_BIG64_USER_DEFINE, params)


def set_mul_device_ctrl() -> bytearray:
    """
        public static byte[] l() {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte b = (byte)MultiControlEnum.getAllInfo._value;
        return r.c(SppProc$CMD_TYPE.SPP_SET_MUL_DEVICE_CTRL, new byte[] { b }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SET_MUL_DEVICE_CTRL, params)


def get_sd_music_list_total_num() -> bytearray:
    """
        public static byte[] l0() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_SD_MUSIC_LIST_TOTAL_NUM, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_SD_MUSIC_LIST_TOTAL_NUM, params)


def get_file_version2_list(paramList: List[int]) -> None:
    """
        public static void l1(List<Integer> paramList) {
        byte[] arrayOfByte2 = c0.d(c0.d(new byte[0], 1, 1, false), paramList.size(), 1, false);
        for (byte b = 0; b < paramList.size(); b++)
          arrayOfByte2 = c0.d(arrayOfByte2, ((Integer)paramList.get(b)).intValue(), 4, false); 
        byte[] arrayOfByte1 = r.c(SppProc$CMD_TYPE.SPP_GET_FILE_VERSION2_LIST, arrayOfByte2);
        p.s().A(arrayOfByte1);
      }
    
    Parameters:
    	paramList (List[int])
    """

    params=[
        (paramList, 'List[int]')
    ]

    return send_msg(enums.CmdType.GET_FILE_VERSION2_LIST, params)


def set_box_mode(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int, paramInt5: int, paramBoolean: bool) -> bytearray:
    """
        public static byte[] l2(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, boolean paramBoolean) {
        byte[] arrayOfByte = new byte[10];
        arrayOfByte[0] = (byte)(byte)LightEnum.LIGHT_MODE._value;
        arrayOfByte[1] = (byte)(byte)(paramInt1 & 0xFF);
        arrayOfByte[2] = (byte)(byte)(paramInt2 & 0xFF);
        arrayOfByte[3] = (byte)(byte)(paramInt3 & 0xFF);
        arrayOfByte[4] = (byte)(byte)(paramInt4 & 0xFF);
        arrayOfByte[5] = (byte)(byte)(paramInt5 & 0xFF);
        arrayOfByte[6] = (byte)(byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, arrayOfByte);
      }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    	paramInt3 (int)
    	paramInt4 (int)
    	paramInt5 (int)
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int'),
        (paramInt3, 'int'),
        (paramInt4, 'int'),
        (paramInt5, 'int'),
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def send_sd_tf_status() -> bytearray:
    """
        public static byte[] m0() {
        k.d("octopus.CmdManager", "");
        return r.c(SppProc$CMD_TYPE.SPP_SEND_SD_TF_STATUS, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SEND_SD_TF_STATUS, params)


def spp_set_mic_switch(paramByte: byte) -> None:
    """
        public static void m2(byte paramByte) {
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_SPP_SET_MIC_SWITCH, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SPP_SET_MIC_SWITCH, params)


def set_alarm_time_gif(paramByte: byte, paramInt: int) -> bytearray:
    """
        public static byte[] n0(byte paramByte, int paramInt) {
        byte[] arrayOfByte = com.divoom.Divoom.utils.r0.d.j(paramInt);
        byte b1 = (byte)(paramByte & 0xFF);
        byte b2 = arrayOfByte[0];
        byte b3 = arrayOfByte[1];
        byte b4 = arrayOfByte[2];
        return r.c(SppProc$CMD_TYPE.SPP_SET_ALARM_TIME_GIF, new byte[] { b1, b2, b3, b4 }
    
    Parameters:
    	paramByte (byte)
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte'),
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_ALARM_TIME_GIF, params)


def send_game_ctrl_info(paramInt: int) -> bytearray:
    """
        public static byte[] n1(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SEND_GAME_CTRL_INFO, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SEND_GAME_CTRL_INFO, params)


def divoom_extern_cmd(paramByte1: byte, paramByte2: byte, paramByte3: byte, paramByte4: byte) -> None:
    """
        public static void n2(byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4) {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_MUSIC_NAME_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 1, paramByte1, paramByte2, paramByte3, paramByte4 }
    
    Parameters:
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    	paramByte4 (byte)
    """

    params=[
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte'),
        (paramByte4, 'byte')
    ]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_mul_box_color(paramPixelBean: PixelBean) -> List[bytearray]:
    """
        public static List<byte[]> o(PixelBean paramPixelBean) {
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        h h = new h();
        return h.c(h.f(paramPixelBean), SppProc$CMD_TYPE.SPP_SET_MUL_BOX_COLOR);
      }
    
    Parameters:
    	paramPixelBean (PixelBean)
    Returns:
    	List[bytearray]
    """

    params=[
        (paramPixelBean, 'PixelBean')
    ]

    return send_msg(enums.CmdType.SET_MUL_BOX_COLOR, params)


def send_game_ctrl_key_up_info(paramInt: int) -> bytearray:
    """
        public static byte[] o1(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SEND_GAME_CTRL_KEY_UP_INFO, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SEND_GAME_CTRL_KEY_UP_INFO, params)


def set_box_mode(paramInt: int) -> bytearray:
    """
        public static byte[] o2(int paramInt) {
        byte[] arrayOfByte = new byte[10];
        arrayOfByte[0] = (byte)(byte)LightEnum.MUSIC_MODE._value;
        arrayOfByte[1] = (byte)(byte)(paramInt & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, arrayOfByte);
      }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def get_auto_power_off() -> bytearray:
    """
        public static byte[] p() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_AUTO_POWER_OFF, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_AUTO_POWER_OFF, params)


def send_game_shark() -> bytearray:
    """
        public static byte[] p1() {
        return r.c(SppProc$CMD_TYPE.SPP_SEND_GAME_SHARK, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.SEND_GAME_SHARK, params)


def divoom_extern_cmd() -> None:
    """
        public static void q() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_AUTO_CONNECT_CFG.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_alarm_listen(paramBoolean: bool, paramByte1: byte, paramByte2: byte) -> bytearray:
    """
        public static byte[] q0(boolean paramBoolean, byte paramByte1, byte paramByte2) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_ALARM_LISTEN, new byte[] { b, paramByte1, paramByte2 }
    
    Parameters:
    	paramBoolean (bool)
    	paramByte1 (byte)
    	paramByte2 (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte')
    ]

    return send_msg(enums.CmdType.SET_ALARM_LISTEN, params)


def send_hotctrl(paramInt1: int, paramInt2: int) -> bytearray:
    """
        public static byte[] q1(int paramInt1, int paramInt2) {
        byte b1 = (byte)paramInt1;
        byte b2 = (byte)paramInt2;
        return r.c(SppProc$CMD_TYPE.SPP_SEND_HOTCTRL, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SEND_HOTCTRL, params)


def send_app_newest_time(paramBoolean: bool) -> bytearray:
    """
        public static byte[] q2(boolean paramBoolean) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SEND_APP_NEWEST_TIME, new byte[] { b }
    
    Parameters:
    	paramBoolean (bool)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SEND_APP_NEWEST_TIME, params)


def divoom_extern_cmd() -> None:
    """
        public static void r() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SppExtCarMode.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, 0 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_alarm_listen_volume(paramByte: byte) -> bytearray:
    """
        public static byte[] r0(byte paramByte) {
        return r.c(SppProc$CMD_TYPE.SPP_SET_ALARM_LISTEN_VOLUME, new byte[] { paramByte }
    
    Parameters:
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_ALARM_LISTEN_VOLUME, params)


def hot_update_file_info(paramc: c) -> bytearray:
    """
        public static byte[] r1(c paramc) {
        byte[] arrayOfByte = new byte[16];
        arrayOfByte[0] = (byte)(byte)(paramc.i() & 0xFF);
        arrayOfByte[1] = (byte)(byte)(paramc.i() >> 8 & 0xFF);
        arrayOfByte[2] = (byte)(byte)(paramc.i() >> 16 & 0xFF);
        arrayOfByte[3] = (byte)(byte)(paramc.i() >> 24 & 0xFF);
        arrayOfByte[4] = (byte)(byte)(int)(paramc.e() & 0xFFL);
        arrayOfByte[5] = (byte)(byte)(int)(paramc.e() >> 8L & 0xFFL);
        arrayOfByte[6] = (byte)(byte)(int)(paramc.e() >> 16L & 0xFFL);
        arrayOfByte[7] = (byte)(byte)(int)(paramc.e() >> 24L & 0xFFL);
        System.arraycopy(paramc.a(), 0, arrayOfByte, 8, 4);
        arrayOfByte[12] = (byte)(byte)(paramc.j() & 0xFF);
        arrayOfByte[13] = (byte)(byte)(paramc.j() >> 8 & 0xFF);
        arrayOfByte[14] = (byte)(byte)(paramc.j() >> 16 & 0xFF);
        arrayOfByte[15] = (byte)(byte)(paramc.j() >> 24 & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_HOT_UPDATE_FILE_INFO, arrayOfByte);
      }
    
    Parameters:
    	paramc (c)
    Returns:
    	bytearray
    """

    params=[
        (paramc, 'c')
    ]

    return send_msg(enums.CmdType.HOT_UPDATE_FILE_INFO, params)


def set_box_mode(paramInt: int) -> bytearray:
    """
        public static byte[] r2(int paramInt) {
        byte b1 = (byte)LightEnum.SPECIAL_MODE._value;
        byte b2 = (byte)(paramInt & 0xFF);
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b1, b2 }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def divoom_extern_cmd() -> None:
    """
        public static void s() {
        int i = SppProc$EXT_CMD_TYPE.SPP_SECOND_SET_GIF_PLAY_TIME_CFG.value();
        byte[] arrayOfByte = c0.d(c0.d(new byte[0], i, 1, false), 65535, 2, false);
        arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, arrayOfByte);
        p.s().A(arrayOfByte);
      }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def get_connected_flag() -> bytearray:
    """
        public static byte[] t() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_CONNECTED_FLAG, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_CONNECTED_FLAG, params)


def divoom_extern_cmd() -> None:
    """
        public static void u() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_USE_USER_DEFINE_INDEX.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b, -1 }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_mix_muise_mode(paramByte: byte) -> None:
    """
        public static void u2(byte paramByte) {
        byte[] arrayOfByte = new byte[1];
        arrayOfByte[0] = (byte)paramByte;
        if (X0()) {
          d.m().write(c.b(SppProc$CMD_TYPE.SPP_SET_MIX_MUISE_MODE, arrayOfByte));
        }
    
    Parameters:
    	paramByte (byte)
    """

    params=[
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_MIX_MUISE_MODE, params)


def divoom_extern_cmd() -> None:
    """
        public static void v() {
        byte b = (byte)SppProc$EXT_CMD_TYPE.SPP_SECOND_GET_USER_DEFINE_TIME.value();
        byte[] arrayOfByte = r.c(SppProc$CMD_TYPE.SPP_DIVOOM_EXTERN_CMD, new byte[] { b }
    
    """

    params=[]

    return send_msg(enums.CmdType.DIVOOM_EXTERN_CMD, params)


def set_device_name(paramString: str) -> bytearray:
    """
        public static byte[] v0(String paramString) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("Set Device Name ");
        stringBuilder.append(paramString);
        k.d("octopus.CmdManager", stringBuilder.toString());
        byte[] arrayOfByte2 = paramString.getBytes();
        byte b = (byte)arrayOfByte2.length;
        byte[] arrayOfByte1 = new byte[arrayOfByte2.length + 1];
        arrayOfByte1[0] = (byte)b;
        System.arraycopy(arrayOfByte2, 0, arrayOfByte1, 1, arrayOfByte2.length);
        return r.c(SppProc$CMD_TYPE.SPP_SET_DEVICE_NAME, arrayOfByte1);
      }
    
    Parameters:
    	paramString (str)
    Returns:
    	bytearray
    """

    params=[
        (paramString, 'str')
    ]

    return send_msg(enums.CmdType.SET_DEVICE_NAME, params)


def send_led_word_cmd(paramInt: int) -> bytearray:
    """
        public static byte[] v1(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_SEND_LED_WORD_CMD, new byte[] { 0, b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.SEND_LED_WORD_CMD, params)


def set_new_mix_music_mode(paramInt1: int, paramInt2: int) -> None:
    """
        public static void v2(int paramInt1, int paramInt2) {
        byte[] arrayOfByte = new byte[2];
        arrayOfByte[0] = (byte)(byte)paramInt1;
        arrayOfByte[1] = (byte)(byte)paramInt2;
        if (X0()) {
          arrayOfByte = c.b(SppProc$CMD_TYPE.SPP_SET_NEW_MIX_MUSIC_MODE, arrayOfByte);
          d.m().write(arrayOfByte);
        }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int')
    ]

    return send_msg(enums.CmdType.SET_NEW_MIX_MUSIC_MODE, params)


def get_box_mode() -> bytearray:
    """
        public static byte[] w() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_BOX_MODE, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_BOX_MODE, params)


def spp_power_on_off_info(paramPowerSetInfo: PowerSetInfo) -> bytearray:
    """
        public static byte[] w0(PowerSetInfo paramPowerSetInfo) {
        k.d("", "");
        byte b1 = paramPowerSetInfo.a;
        byte b2 = (byte)paramPowerSetInfo.b;
        byte b3 = paramPowerSetInfo.c;
        byte b4 = paramPowerSetInfo.f;
        byte b5 = paramPowerSetInfo.d;
        byte b6 = paramPowerSetInfo.e;
        byte b7 = (byte)Color.red(paramPowerSetInfo.g);
        byte b8 = (byte)Color.green(paramPowerSetInfo.g);
        byte b9 = (byte)Color.blue(paramPowerSetInfo.g);
        return r.c(SppProc$CMD_TYPE.SPP_SPP_POWER_ON_OFF_INFO, new byte[] { 1, b1, b2, b3, b4, b5, b6, b7, b8, b9 }
    
    Parameters:
    	paramPowerSetInfo (PowerSetInfo)
    Returns:
    	bytearray
    """

    params=[
        (paramPowerSetInfo, 'PowerSetInfo')
    ]

    return send_msg(enums.CmdType.SPP_POWER_ON_OFF_INFO, params)


def set_mix_muise_mode(paramInt1: int, paramInt2: int, paramBoolean: bool) -> None:
    """
        public static void w2(int paramInt1, int paramInt2, boolean paramBoolean) {
        byte[] arrayOfByte = new byte[3];
        arrayOfByte[0] = (byte)(byte)paramInt1;
        arrayOfByte[1] = (byte)(byte)paramInt2;
        arrayOfByte[2] = (byte)(byte)paramBoolean;
        if (X0()) {
          d.m().write(c.b(SppProc$CMD_TYPE.SPP_SET_MIX_MUISE_MODE, arrayOfByte));
        }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    	paramBoolean (bool)
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int'),
        (paramBoolean, 'bool')
    ]

    return send_msg(enums.CmdType.SET_MIX_MUISE_MODE, params)


def get_file_version(paramInt: int) -> bytearray:
    """
        public static byte[] x(int paramInt) {
        byte b = (byte)paramInt;
        return r.c(SppProc$CMD_TYPE.SPP_GET_FILE_VERSION, new byte[] { b }
    
    Parameters:
    	paramInt (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.GET_FILE_VERSION, params)


def set_user_gif(paramInt1: int, paramInt2: int, paramInt3: int, paramInt4: int) -> bytearray:
    """
        public static byte[] x0(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("getSetScrollSandCmdStart ");
        stringBuilder.append(paramInt4);
        k.d("octopus.CmdManager", stringBuilder.toString());
        HotUpdateHandle.o().A();
        org.greenrobot.eventbus.c.c().k(new com.divoom.Divoom.b.r.c());
        byte b1 = (byte)(paramInt1 & 0xFF);
        byte b2 = (byte)(paramInt2 & 0xFF);
        byte b3 = (byte)(paramInt2 >> 8 & 0xFF);
        byte b4 = (byte)(paramInt3 & 0xFF);
        byte b5 = (byte)(paramInt3 >> 8 & 0xFF);
        byte b6 = (byte)paramInt4;
        return r.c(SppProc$CMD_TYPE.SPP_SET_USER_GIF, new byte[] { 0, 3, b1, b2, b3, b4, b5, b6 }
    
    Parameters:
    	paramInt1 (int)
    	paramInt2 (int)
    	paramInt3 (int)
    	paramInt4 (int)
    Returns:
    	bytearray
    """

    params=[
        (paramInt1, 'int'),
        (paramInt2, 'int'),
        (paramInt3, 'int'),
        (paramInt4, 'int')
    ]

    return send_msg(enums.CmdType.SET_USER_GIF, params)


def get_file_version2_list() -> bytearray:
    """
        public static byte[] y() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_FILE_VERSION2_LIST, new byte[] { 0 }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_FILE_VERSION2_LIST, params)


def light_adjust_level(paramArrayOfbyte: bytearray) -> bytearray:
    """
        public static byte[] y0(byte[] paramArrayOfbyte) {
        return r.c(SppProc$CMD_TYPE.SPP_LIGHT_ADJUST_LEVEL, paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    Returns:
    	bytearray
    """

    params=[
        (paramArrayOfbyte, 'bytearray')
    ]

    return send_msg(enums.CmdType.LIGHT_ADJUST_LEVEL, params)


def lieght_set_25dots_pic(paramArrayOfbyte: bytearray, paramInt: int) -> None:
    """
        public static void y1(byte[] paramArrayOfbyte, int paramInt) {
        byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 1];
        arrayOfByte[0] = (byte)(byte)paramInt;
        System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 1, paramArrayOfbyte.length);
        paramArrayOfbyte = r.c(SppProc$CMD_TYPE.SPP_LIEGHT_SET_25DOTS_PIC, arrayOfByte);
        p.s().D(paramArrayOfbyte);
      }
    
    Parameters:
    	paramArrayOfbyte (bytearray)
    	paramInt (int)
    """

    params=[
        (paramArrayOfbyte, 'bytearray'),
        (paramInt, 'int')
    ]

    return send_msg(enums.CmdType.LIEGHT_SET_25DOTS_PIC, params)


def get_file_version2() -> bytearray:
    """
        public static byte[] z() {
        return r.c(SppProc$CMD_TYPE.SPP_GET_FILE_VERSION2, null);
      }
    
    Returns:
    	bytearray
    """

    params=[]

    return send_msg(enums.CmdType.GET_FILE_VERSION2, params)


def set_scene_listen(paramBoolean: bool, paramByte1: byte, paramByte2: byte) -> bytearray:
    """
        public static byte[] z0(boolean paramBoolean, byte paramByte1, byte paramByte2) {
        byte b = (byte)paramBoolean;
        return r.c(SppProc$CMD_TYPE.SPP_SET_SCENE_LISTEN, new byte[] { b, paramByte1, paramByte2 }
    
    Parameters:
    	paramBoolean (bool)
    	paramByte1 (byte)
    	paramByte2 (byte)
    Returns:
    	bytearray
    """

    params=[
        (paramBoolean, 'bool'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte')
    ]

    return send_msg(enums.CmdType.SET_SCENE_LISTEN, params)


def set_box_mode(light_mode: enums.LightMode, paramByte: byte) -> bytearray:
    """
        public static byte[] f2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, paramByte }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


def set_box_mode(light_mode: enums.LightMode, paramByte1: byte, paramByte2: byte, paramByte3: byte, paramByte4: byte, paramByte5: byte, paramByte6: byte, paramByte7: byte) -> bytearray:
    """
        public static byte[] h2(SppProc$LIGHT_MODE paramSppProc$LIGHT_MODE, byte paramByte1, byte paramByte2, byte paramByte3, byte paramByte4, byte paramByte5, byte paramByte6, byte paramByte7) {
        byte b = paramSppProc$LIGHT_MODE.getCmd_data()[0];
        return r.c(SppProc$CMD_TYPE.SPP_SET_BOX_MODE, new byte[] { b, paramByte1, paramByte2, paramByte3, paramByte4, paramByte5, paramByte6, paramByte7 }
    
    Parameters:
    	light_mode (enums.LightMode)
    	paramByte1 (byte)
    	paramByte2 (byte)
    	paramByte3 (byte)
    	paramByte4 (byte)
    	paramByte5 (byte)
    	paramByte6 (byte)
    	paramByte7 (byte)
    Returns:
    	bytearray
    """

    params=[
        (light_mode, 'enums.LightMode'),
        (paramByte1, 'byte'),
        (paramByte2, 'byte'),
        (paramByte3, 'byte'),
        (paramByte4, 'byte'),
        (paramByte5, 'byte'),
        (paramByte6, 'byte'),
        (paramByte7, 'byte')
    ]

    return send_msg(enums.CmdType.SET_BOX_MODE, params)


