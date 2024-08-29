# pylint:disable=line-too-long
from __future__ import annotations
import logging
from collections import OrderedDict

from ...sim_type import (SimTypeFunction,
    SimTypeShort,
    SimTypeInt,
    SimTypeLong,
    SimTypeLongLong,
    SimTypeDouble,
    SimTypeFloat,
    SimTypePointer,
    SimTypeChar,
    SimStruct,
    SimTypeArray,
    SimTypeBottom,
    SimUnion,
    SimTypeBool,
    SimTypeRef,
)
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.type_collection_names = ["win32"]
lib.set_default_cc("X86", SimCCStdcall)
lib.set_default_cc("AMD64", SimCCMicrosoftAMD64)
lib.set_library_names("cfgmgr32.dll")
prototypes = \
    {
        #
        'CM_Add_Empty_Log_Conf': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="PRIORITY"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "dnDevInst", "Priority", "ulFlags"]),
        #
        'CM_Add_Empty_Log_Conf_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="PRIORITY"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "dnDevInst", "Priority", "ulFlags", "hMachine"]),
        #
        'CM_Add_IDA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszID", "ulFlags"]),
        #
        'CM_Add_IDW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszID", "ulFlags"]),
        #
        'CM_Add_ID_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszID", "ulFlags", "hMachine"]),
        #
        'CM_Add_ID_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszID", "ulFlags", "hMachine"]),
        #
        'CM_Add_Range': SimTypeFunction([SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ullStartValue", "ullEndValue", "rlh", "ulFlags"]),
        #
        'CM_Add_Res_Des': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"]),
        #
        'CM_Add_Res_Des_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"]),
        #
        'CM_Connect_MachineA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["UNCServerName", "phMachine"]),
        #
        'CM_Connect_MachineW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["UNCServerName", "phMachine"]),
        #
        'CM_Create_DevNodeA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "dnParent", "ulFlags"]),
        #
        'CM_Create_DevNodeW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "dnParent", "ulFlags"]),
        #
        'CM_Create_DevNode_ExA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "dnParent", "ulFlags", "hMachine"]),
        #
        'CM_Create_DevNode_ExW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "dnParent", "ulFlags", "hMachine"]),
        #
        'CM_Create_Range_List': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prlh", "ulFlags"]),
        #
        'CM_Delete_Class_Key': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulFlags"]),
        #
        'CM_Delete_Class_Key_Ex': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulFlags", "hMachine"]),
        #
        'CM_Delete_DevNode_Key': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevNode", "ulHardwareProfile", "ulFlags"]),
        #
        'CM_Delete_DevNode_Key_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevNode", "ulHardwareProfile", "ulFlags", "hMachine"]),
        #
        'CM_Delete_Range': SimTypeFunction([SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ullStartValue", "ullEndValue", "rlh", "ulFlags"]),
        #
        'CM_Detect_Resource_Conflict': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags"]),
        #
        'CM_Detect_Resource_Conflict_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags", "hMachine"]),
        #
        'CM_Disable_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Disable_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Disconnect_Machine': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["hMachine"]),
        #
        'CM_Dup_Range_List': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlhOld", "rlhNew", "ulFlags"]),
        #
        'CM_Enable_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Enable_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Enumerate_Classes': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="CM_ENUMERATE_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulClassIndex", "ClassGuid", "ulFlags"]),
        #
        'CM_Enumerate_Classes_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="CM_ENUMERATE_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulClassIndex", "ClassGuid", "ulFlags", "hMachine"]),
        #
        'CM_Enumerate_EnumeratorsA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulEnumIndex", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Enumerate_EnumeratorsW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulEnumIndex", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Enumerate_Enumerators_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulEnumIndex", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Enumerate_Enumerators_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulEnumIndex", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Find_Range': SimTypeFunction([SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="UInt32"), SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pullStart", "ullStart", "ulLength", "ullAlignment", "ullEnd", "rlh", "ulFlags"]),
        #
        'CM_First_Range': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlh", "pullStart", "pullEnd", "preElement", "ulFlags"]),
        #
        'CM_Free_Log_Conf': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["lcLogConfToBeFreed", "ulFlags"]),
        #
        'CM_Free_Log_Conf_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["lcLogConfToBeFreed", "ulFlags", "hMachine"]),
        #
        'CM_Free_Log_Conf_Handle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["lcLogConf"]),
        #
        'CM_Free_Range_List': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlh", "ulFlags"]),
        #
        'CM_Free_Res_Des': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ulFlags"]),
        #
        'CM_Free_Res_Des_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ulFlags", "hMachine"]),
        #
        'CM_Free_Res_Des_Handle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rdResDes"]),
        #
        'CM_Get_Child': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_Child_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_NameA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_Class_NameW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_Class_Name_ExA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Name_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Key_NameA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszKeyName", "pulLength", "ulFlags"]),
        #
        'CM_Get_Class_Key_NameW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszKeyName", "pulLength", "ulFlags"]),
        #
        'CM_Get_Class_Key_Name_ExA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszKeyName", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Key_Name_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszKeyName", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Depth': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulDepth", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_Depth_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulDepth", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_IDA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_IDW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_ID_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_ListA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszFilter", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_ID_ListW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszFilter", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_ID_List_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszFilter", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_List_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszFilter", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_List_SizeA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "pszFilter", "ulFlags"]),
        #
        'CM_Get_Device_ID_List_SizeW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "pszFilter", "ulFlags"]),
        #
        'CM_Get_Device_ID_List_Size_ExA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "pszFilter", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_List_Size_ExW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "pszFilter", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_ID_Size': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_Device_ID_Size_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_PropertyW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Get_DevNode_Property_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Property_Keys': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"]),
        #
        'CM_Get_DevNode_Property_Keys_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Registry_PropertyA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_DevNode_Registry_PropertyW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_DevNode_Registry_Property_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Registry_Property_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Custom_PropertyA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_DevNode_Custom_PropertyW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags"]),
        #
        'CM_Get_DevNode_Custom_Property_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Custom_Property_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_DevNode_Status': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="CM_DEVNODE_STATUS_FLAGS"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="CM_PROB"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_DevNode_Status_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="CM_DEVNODE_STATUS_FLAGS"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="CM_PROB"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_First_Log_Conf': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_LOG_CONF")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_First_Log_Conf_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_LOG_CONF"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_Global_State': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulState", "ulFlags"]),
        #
        'CM_Get_Global_State_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulState", "ulFlags", "hMachine"]),
        #
        'CM_Get_Hardware_Profile_InfoA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("HWPROFILEINFO_A", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulIndex", "pHWProfileInfo", "ulFlags"]),
        #
        'CM_Get_Hardware_Profile_Info_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("HWPROFILEINFO_A", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulIndex", "pHWProfileInfo", "ulFlags", "hMachine"]),
        #
        'CM_Get_Hardware_Profile_InfoW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("HWPROFILEINFO_W", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulIndex", "pHWProfileInfo", "ulFlags"]),
        #
        'CM_Get_Hardware_Profile_Info_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("HWPROFILEINFO_W", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulIndex", "pHWProfileInfo", "ulFlags", "hMachine"]),
        #
        'CM_Get_HW_Prof_FlagsA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags"]),
        #
        'CM_Get_HW_Prof_FlagsW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags"]),
        #
        'CM_Get_HW_Prof_Flags_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags", "hMachine"]),
        #
        'CM_Get_HW_Prof_Flags_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_AliasA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags"]),
        #
        'CM_Get_Device_Interface_AliasW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags"]),
        #
        'CM_Get_Device_Interface_Alias_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_Alias_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_ListA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_Interface_ListW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Device_Interface_List_ExA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_List_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_List_SizeA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags"]),
        #
        'CM_Get_Device_Interface_List_SizeW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags"]),
        #
        'CM_Get_Device_Interface_List_Size_ExA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_List_Size_ExW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="CM_GET_DEVICE_INTERFACE_LIST_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_PropertyW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Get_Device_Interface_Property_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Get_Device_Interface_Property_KeysW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"]),
        #
        'CM_Get_Device_Interface_Property_Keys_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"]),
        #
        'CM_Get_Log_Conf_Priority': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["lcLogConf", "pPriority", "ulFlags"]),
        #
        'CM_Get_Log_Conf_Priority_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["lcLogConf", "pPriority", "ulFlags", "hMachine"]),
        #
        'CM_Get_Next_Log_Conf': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "lcLogConf", "ulFlags"]),
        #
        'CM_Get_Next_Log_Conf_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["plcLogConf", "lcLogConf", "ulFlags", "hMachine"]),
        #
        'CM_Get_Parent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_Parent_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_Res_Des_Data': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rdResDes", "Buffer", "BufferLen", "ulFlags"]),
        #
        'CM_Get_Res_Des_Data_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rdResDes", "Buffer", "BufferLen", "ulFlags", "hMachine"]),
        #
        'CM_Get_Res_Des_Data_Size': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulSize", "rdResDes", "ulFlags"]),
        #
        'CM_Get_Res_Des_Data_Size_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulSize", "rdResDes", "ulFlags", "hMachine"]),
        #
        'CM_Get_Sibling': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags"]),
        #
        'CM_Get_Sibling_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Get_Version': SimTypeFunction([], SimTypeShort(signed=False, label="UInt16")),
        #
        'CM_Get_Version_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeShort(signed=False, label="UInt16"), arg_names=["hMachine"]),
        #
        'CM_Is_Version_Available': SimTypeFunction([SimTypeShort(signed=False, label="UInt16")], SimTypeInt(signed=True, label="Int32"), arg_names=["wVersion"]),
        #
        'CM_Is_Version_Available_Ex': SimTypeFunction([SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["wVersion", "hMachine"]),
        #
        'CM_Intersect_Range_List': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"]),
        #
        'CM_Invert_Range_List': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlhOld", "rlhNew", "ullMaxValue", "ulFlags"]),
        #
        'CM_Locate_DevNodeA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="CM_LOCATE_DEVNODE_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "ulFlags"]),
        #
        'CM_Locate_DevNodeW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="CM_LOCATE_DEVNODE_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "ulFlags"]),
        #
        'CM_Locate_DevNode_ExA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "ulFlags", "hMachine"]),
        #
        'CM_Locate_DevNode_ExW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pdnDevInst", "pDeviceID", "ulFlags", "hMachine"]),
        #
        'CM_Merge_Range_List': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"]),
        #
        'CM_Modify_Res_Des': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"]),
        #
        'CM_Modify_Res_Des_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"]),
        #
        'CM_Move_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnFromDevInst", "dnToDevInst", "ulFlags"]),
        #
        'CM_Move_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnFromDevInst", "dnToDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Next_Range': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["preElement", "pullStart", "pullEnd", "ulFlags"]),
        #
        'CM_Get_Next_Res_Des': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="CM_RESTYPE"), SimTypePointer(SimTypeInt(signed=False, label="CM_RESTYPE"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags"]),
        #
        'CM_Get_Next_Res_Des_Ex': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="CM_RESTYPE"), SimTypePointer(SimTypeInt(signed=False, label="CM_RESTYPE"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags", "hMachine"]),
        #
        'CM_Open_Class_KeyA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags"]),
        #
        'CM_Open_Class_KeyW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags"]),
        #
        'CM_Open_Class_Key_ExA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags", "hMachine"]),
        #
        'CM_Open_Class_Key_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags", "hMachine"]),
        #
        'CM_Open_DevNode_Key': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags"]),
        #
        'CM_Open_DevNode_Key_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags", "hMachine"]),
        #
        'CM_Open_Device_Interface_KeyA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags"]),
        #
        'CM_Open_Device_Interface_KeyW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags"]),
        #
        'CM_Open_Device_Interface_Key_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Open_Device_Interface_Key_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Delete_Device_Interface_KeyA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags"]),
        #
        'CM_Delete_Device_Interface_KeyW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags"]),
        #
        'CM_Delete_Device_Interface_Key_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Delete_Device_Interface_Key_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Query_Arbitrator_Free_Data': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags"]),
        #
        'CM_Query_Arbitrator_Free_Data_Ex': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags", "hMachine"]),
        #
        'CM_Query_Arbitrator_Free_Size': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulSize", "dnDevInst", "ResourceID", "ulFlags"]),
        #
        'CM_Query_Arbitrator_Free_Size_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pulSize", "dnDevInst", "ResourceID", "ulFlags", "hMachine"]),
        #
        'CM_Query_Remove_SubTree': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "ulFlags"]),
        #
        'CM_Query_Remove_SubTree_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "ulFlags", "hMachine"]),
        #
        'CM_Query_And_Remove_SubTreeA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"]),
        #
        'CM_Query_And_Remove_SubTreeW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"]),
        #
        'CM_Query_And_Remove_SubTree_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags", "hMachine"]),
        #
        'CM_Query_And_Remove_SubTree_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags", "hMachine"]),
        #
        'CM_Request_Device_EjectA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"]),
        #
        'CM_Request_Device_Eject_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags", "hMachine"]),
        #
        'CM_Request_Device_EjectW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"]),
        #
        'CM_Request_Device_Eject_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="PNP_VETO_TYPE"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags", "hMachine"]),
        #
        'CM_Reenumerate_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_REENUMERATE_FLAGS")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Reenumerate_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Register_Device_InterfaceA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags"]),
        #
        'CM_Register_Device_InterfaceW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags"]),
        #
        'CM_Register_Device_Interface_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Register_Device_Interface_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Set_DevNode_Problem_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProblem", "ulFlags", "hMachine"]),
        #
        'CM_Set_DevNode_Problem': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProblem", "ulFlags"]),
        #
        'CM_Unregister_Device_InterfaceA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags"]),
        #
        'CM_Unregister_Device_InterfaceW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags"]),
        #
        'CM_Unregister_Device_Interface_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Unregister_Device_Interface_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "ulFlags", "hMachine"]),
        #
        'CM_Register_Device_Driver': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Register_Device_Driver_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Remove_SubTree': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "ulFlags"]),
        #
        'CM_Remove_SubTree_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnAncestor", "ulFlags", "hMachine"]),
        #
        'CM_Set_DevNode_PropertyW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Set_DevNode_Property_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Set_DevNode_Registry_PropertyA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags"]),
        #
        'CM_Set_DevNode_Registry_PropertyW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags"]),
        #
        'CM_Set_DevNode_Registry_Property_ExA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"]),
        #
        'CM_Set_DevNode_Registry_Property_ExW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"]),
        #
        'CM_Set_Device_Interface_PropertyW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Set_Device_Interface_Property_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Is_Dock_Station_Present': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pbPresent"]),
        #
        'CM_Is_Dock_Station_Present_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pbPresent", "hMachine"]),
        #
        'CM_Request_Eject_PC': SimTypeFunction([], SimTypeInt(signed=False, label="CONFIGRET")),
        #
        'CM_Request_Eject_PC_Ex': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["hMachine"]),
        #
        'CM_Set_HW_Prof_FlagsA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulConfig", "ulValue", "ulFlags"]),
        #
        'CM_Set_HW_Prof_FlagsW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulConfig", "ulValue", "ulFlags"]),
        #
        'CM_Set_HW_Prof_Flags_ExA': SimTypeFunction([SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulConfig", "ulValue", "ulFlags", "hMachine"]),
        #
        'CM_Set_HW_Prof_Flags_ExW': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pDeviceID", "ulConfig", "ulValue", "ulFlags", "hMachine"]),
        #
        'CM_Setup_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Setup_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Test_Range_Available': SimTypeFunction([SimTypeLongLong(signed=False, label="UInt64"), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ullStartValue", "ullEndValue", "rlh", "ulFlags"]),
        #
        'CM_Uninstall_DevNode': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags"]),
        #
        'CM_Uninstall_DevNode_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["dnDevInst", "ulFlags", "hMachine"]),
        #
        'CM_Run_Detection': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulFlags"]),
        #
        'CM_Run_Detection_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulFlags", "hMachine"]),
        #
        'CM_Set_HW_Prof': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulHardwareProfile", "ulFlags"]),
        #
        'CM_Set_HW_Prof_Ex': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ulHardwareProfile", "ulFlags", "hMachine"]),
        #
        'CM_Query_Resource_Conflict_List': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="CM_RESTYPE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pclConflictList", "dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"]),
        #
        'CM_Free_Resource_Conflict_Handle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["clConflictList"]),
        #
        'CM_Get_Resource_Conflict_Count': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["clConflictList", "pulCount"]),
        #
        'CM_Get_Resource_Conflict_DetailsA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("CONFLICT_DETAILS_A", SimStruct), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["clConflictList", "ulIndex", "pConflictDetails"]),
        #
        'CM_Get_Resource_Conflict_DetailsW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("CONFLICT_DETAILS_W", SimStruct), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["clConflictList", "ulIndex", "pConflictDetails"]),
        #
        'CM_Get_Class_PropertyW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Get_Class_Property_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=False, label="DEVPROPTYPE"), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Property_Keys': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"]),
        #
        'CM_Get_Class_Property_Keys_Ex': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"]),
        #
        'CM_Set_Class_PropertyW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"]),
        #
        'CM_Set_Class_Property_ExW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeRef("DEVPROPKEY", SimStruct), offset=0), SimTypeInt(signed=False, label="DEVPROPTYPE"), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Registry_PropertyA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Get_Class_Registry_PropertyW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"]),
        #
        'CM_Set_Class_Registry_PropertyA': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"]),
        #
        'CM_Set_Class_Registry_PropertyW': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["ClassGuid", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"]),
        #
        'CMP_WaitNoPendingInstallEvents': SimTypeFunction([SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["dwTimeout"]),
        #
        'CM_Register_Notification': SimTypeFunction([SimTypePointer(SimTypeRef("CM_NOTIFY_FILTER", SimStruct), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=False, label="CM_NOTIFY_ACTION"), SimTypePointer(SimTypeRef("CM_NOTIFY_EVENT_DATA", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["hNotify", "Context", "Action", "EventData", "EventDataSize"]), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["pFilter", "pContext", "pCallback", "pNotifyContext"]),
        #
        'CM_Unregister_Notification': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=False, label="CONFIGRET"), arg_names=["NotifyContext"]),
        #
        'CM_MapCrToWin32Err': SimTypeFunction([SimTypeInt(signed=False, label="CONFIGRET"), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["CmReturnCode", "DefaultErr"]),
        #
        'SwDeviceCreate': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeRef("SW_DEVICE_CREATE_INFO", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPERTY", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeBottom(label="Void"), arg_names=["hSwDevice", "CreateResult", "pContext", "pszDeviceInstanceId"]), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pszEnumeratorName", "pszParentDeviceInstance", "pCreateInfo", "cPropertyCount", "pProperties", "pCallback", "pContext", "phSwDevice"]),
        #
        'SwDeviceClose': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeBottom(label="Void"), arg_names=["hSwDevice"]),
        #
        'SwDeviceSetLifetime': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="SW_DEVICE_LIFETIME")], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "Lifetime"]),
        #
        'SwDeviceGetLifetime': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="SW_DEVICE_LIFETIME"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "pLifetime"]),
        #
        'SwDevicePropertySet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPERTY", SimStruct), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "cPropertyCount", "pProperties"]),
        #
        'SwDeviceInterfaceRegister': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPERTY", SimStruct), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "pInterfaceClassGuid", "pszReferenceString", "cPropertyCount", "pProperties", "fEnabled", "ppszDeviceInterfaceId"]),
        #
        'SwMemFree': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pMem"]),
        #
        'SwDeviceInterfaceSetState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "pszDeviceInterfaceId", "fEnabled"]),
        #
        'SwDeviceInterfacePropertySet': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("DEVPROPERTY", SimStruct), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hSwDevice", "pszDeviceInterfaceId", "cPropertyCount", "pProperties"]),
    }

lib.set_prototypes(prototypes)
