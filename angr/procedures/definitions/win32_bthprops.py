# pylint:disable=line-too-long
from __future__ import annotations
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("bthprops.dll")
prototypes = \
    {
        #
        'BluetoothSelectDevices': SimTypeFunction([SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "cNumOfClasses": SimTypeInt(signed=False, label="UInt32"), "prgClassOfDevices": SimTypePointer(SimStruct({"ulCODMask": SimTypeInt(signed=False, label="UInt32"), "pcszDescription": SimTypeBottom(label="PWSTR")}, name="BLUETOOTH_COD_PAIRS", pack=False, align=None), offset=0), "pszInfo": SimTypeBottom(label="PWSTR"), "hwndParent": SimTypeBottom(label="HWND"), "fForceAuthentication": SimTypeBottom(label="BOOL"), "fShowAuthenticated": SimTypeBottom(label="BOOL"), "fShowRemembered": SimTypeBottom(label="BOOL"), "fShowUnknown": SimTypeBottom(label="BOOL"), "fAddNewDeviceWizard": SimTypeBottom(label="BOOL"), "fSkipServicesPage": SimTypeBottom(label="BOOL"), "pfnDeviceCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0)], SimTypeBottom(label="BOOL"), arg_names=["pvParam", "pDevice"]), offset=0), "pvParam": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "cNumDevices": SimTypeInt(signed=False, label="UInt32"), "pDevices": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0)}, name="BLUETOOTH_SELECT_DEVICE_PARAMS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pbtsdp"]),
        #
        'BluetoothSelectDevicesFree': SimTypeFunction([SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "cNumOfClasses": SimTypeInt(signed=False, label="UInt32"), "prgClassOfDevices": SimTypePointer(SimStruct({"ulCODMask": SimTypeInt(signed=False, label="UInt32"), "pcszDescription": SimTypeBottom(label="PWSTR")}, name="BLUETOOTH_COD_PAIRS", pack=False, align=None), offset=0), "pszInfo": SimTypeBottom(label="PWSTR"), "hwndParent": SimTypeBottom(label="HWND"), "fForceAuthentication": SimTypeBottom(label="BOOL"), "fShowAuthenticated": SimTypeBottom(label="BOOL"), "fShowRemembered": SimTypeBottom(label="BOOL"), "fShowUnknown": SimTypeBottom(label="BOOL"), "fAddNewDeviceWizard": SimTypeBottom(label="BOOL"), "fSkipServicesPage": SimTypeBottom(label="BOOL"), "pfnDeviceCallback": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0)], SimTypeBottom(label="BOOL"), arg_names=["pvParam", "pDevice"]), offset=0), "pvParam": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "cNumDevices": SimTypeInt(signed=False, label="UInt32"), "pDevices": SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0)}, name="BLUETOOTH_SELECT_DEVICE_PARAMS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pbtsdp"]),
        #
        'BluetoothDisplayDeviceProperties': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwndParent", "pbtdi"]),
        #
        'BluetoothAuthenticateDevice': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndParent", "hRadio", "pbtbi", "pszPasskey", "ulPasskeyLength"]),
        #
        'BluetoothAuthenticateDeviceEx': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"C": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16), "R": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 16)}, name="BLUETOOTH_OOB_DATA_INFO", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="AUTHENTICATION_REQUIREMENTS")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndParentIn", "hRadioIn", "pbtdiInout", "pbtOobData", "authenticationRequirement"]),
        #
        'BluetoothAuthenticateMultipleDevices': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"dwSize": SimTypeInt(signed=False, label="UInt32"), "Address": SimStruct({"Anonymous": SimUnion({"ullLong": SimTypeLongLong(signed=False, label="UInt64"), "rgBytes": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 6)}, name="<anon>", label="None")}, name="BLUETOOTH_ADDRESS", pack=False, align=None), "ulClassofDevice": SimTypeInt(signed=False, label="UInt32"), "fConnected": SimTypeBottom(label="BOOL"), "fRemembered": SimTypeBottom(label="BOOL"), "fAuthenticated": SimTypeBottom(label="BOOL"), "stLastSeen": SimTypeBottom(label="SYSTEMTIME"), "stLastUsed": SimTypeBottom(label="SYSTEMTIME"), "szName": SimTypeFixedSizeArray(SimTypeChar(label="Char"), 248)}, name="BLUETOOTH_DEVICE_INFO", pack=False, align=None), label="LPArray", offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["hwndParent", "hRadio", "cDevices", "rgbtdi"]),
    }

lib.set_prototypes(prototypes)
