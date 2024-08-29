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
lib.set_library_names("drttransport.dll")
prototypes = \
    {
        #
        'DrtCreateIpv6UdpTransport': SimTypeFunction([SimTypeInt(signed=False, label="DRT_SCOPE"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["scope", "dwScopeId", "dwLocalityThreshold", "pwPort", "phTransport"]),
        #
        'DrtDeleteIpv6UdpTransport': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hTransport"]),
    }

lib.set_prototypes(prototypes)
