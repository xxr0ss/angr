# pylint:disable=line-too-long
from __future__ import annotations
import logging
from collections import OrderedDict

from angr.sim_type import SimTypeFunction, SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat, SimTypePointer, SimTypeChar, SimStruct, SimTypeArray, SimTypeBottom, SimUnion, SimTypeBool, SimTypeRef
from angr.calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from angr.procedures import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.type_collection_names = ["win32"]
lib.set_default_cc("X86", SimCCStdcall)
lib.set_default_cc("AMD64", SimCCMicrosoftAMD64)
lib.set_library_names("usp10.dll")
prototypes = \
    {
        #
        'ScriptFreeCache': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["psc"]),
        #
        'ScriptItemize': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_CONTROL", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_STATE", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ITEM", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pwcInChars", "cInChars", "cMaxItems", "psControl", "psState", "pItems", "pcItems"]),
        #
        'ScriptLayout': SimTypeFunction([SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["cRuns", "pbLevel", "piVisualToLogical", "piLogicalToVisual"]),
        #
        'ScriptShape': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "pwcChars", "cChars", "cMaxGlyphs", "psa", "pwOutGlyphs", "pwLogClust", "psva", "pcGlyphs"]),
        #
        'ScriptPlace': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("GOFFSET", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeRef("ABC", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "pwGlyphs", "cGlyphs", "psva", "psa", "piAdvance", "pGoffset", "pABC"]),
        #
        'ScriptTextOut': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("RECT", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("GOFFSET", SimStruct), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "x", "y", "fuOptions", "lprc", "psa", "pwcReserved", "iReserved", "pwGlyphs", "cGlyphs", "piAdvance", "piJustify", "pGoffset"]),
        #
        'ScriptJustify': SimTypeFunction([SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["psva", "piAdvance", "cGlyphs", "iDx", "iMinKashida", "piJustify"]),
        #
        'ScriptBreak': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_LOGATTR", SimStruct), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pwcChars", "cChars", "psa", "psla"]),
        #
        'ScriptCPtoX': SimTypeFunction([SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["iCP", "fTrailing", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "piX"]),
        #
        'ScriptXtoCP': SimTypeFunction([SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["iX", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "piCP", "piTrailing"]),
        #
        'ScriptGetLogicalWidths': SimTypeFunction([SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["psa", "cChars", "cGlyphs", "piGlyphWidth", "pwLogClust", "psva", "piDx"]),
        #
        'ScriptApplyLogicalWidth': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_VISATTR", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypePointer(SimTypeRef("ABC", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["piDx", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "pABC", "piJustify"]),
        #
        'ScriptGetCMap': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "pwcInChars", "cChars", "dwFlags", "pwOutGlyphs"]),
        #
        'ScriptGetGlyphABCWidth': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeRef("ABC", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "wGlyph", "pABC"]),
        #
        'ScriptGetProperties': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypePointer(SimTypeRef("SCRIPT_PROPERTIES", SimStruct), offset=0), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ppSp", "piNumScripts"]),
        #
        'ScriptGetFontProperties': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_FONTPROPERTIES", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "sfp"]),
        #
        'ScriptCacheGetHeight': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "tmHeight"]),
        #
        'ScriptStringAnalyse': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_CONTROL", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_STATE", SimStruct), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_TABDEF", SimStruct), offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "pString", "cString", "cGlyphs", "iCharset", "dwFlags", "iReqWidth", "psControl", "psState", "piDx", "pTabdef", "pbInClass", "pssa"]),
        #
        'ScriptStringFree': SimTypeFunction([SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pssa"]),
        #
        'ScriptString_pSize': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypePointer(SimTypeRef("SIZE", SimStruct), offset=0), arg_names=["ssa"]),
        #
        'ScriptString_pcOutChars': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), arg_names=["ssa"]),
        #
        'ScriptString_pLogAttr': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypePointer(SimTypeRef("SCRIPT_LOGATTR", SimStruct), offset=0), arg_names=["ssa"]),
        #
        'ScriptStringGetOrder': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa", "puOrder"]),
        #
        'ScriptStringCPtoX': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa", "icp", "fTrailing", "pX"]),
        #
        'ScriptStringXtoCP': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa", "iX", "piCh", "piTrailing"]),
        #
        'ScriptStringGetLogicalWidths': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa", "piDx"]),
        #
        'ScriptStringValidate': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa"]),
        #
        'ScriptStringOut': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="ETO_OPTIONS"), SimTypePointer(SimTypeRef("RECT", SimStruct), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32")], SimTypeInt(signed=True, label="Int32"), arg_names=["ssa", "iX", "iY", "uOptions", "prc", "iMinSel", "iMaxSel", "fDisabled"]),
        #
        'ScriptIsComplex': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=False, label="SCRIPT_IS_COMPLEX_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["pwcInChars", "cInChars", "dwFlags"]),
        #
        'ScriptRecordDigitSubstitution': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeRef("SCRIPT_DIGITSUBSTITUTE", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Locale", "psds"]),
        #
        'ScriptApplyDigitSubstitution': SimTypeFunction([SimTypePointer(SimTypeRef("SCRIPT_DIGITSUBSTITUTE", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_CONTROL", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_STATE", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["psds", "psc", "pss"]),
        #
        'ScriptShapeOpenType': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypePointer(SimTypeRef("TEXTRANGE_PROPERTIES", SimStruct), offset=0), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_CHARPROP", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_GLYPHPROP", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "rcRangeChars", "rpRangeProperties", "cRanges", "pwcChars", "cChars", "cMaxGlyphs", "pwLogClust", "pCharProps", "pwOutGlyphs", "pOutGlyphProps", "pcGlyphs"]),
        #
        'ScriptPlaceOpenType': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypePointer(SimTypeRef("TEXTRANGE_PROPERTIES", SimStruct), offset=0), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_CHARPROP", SimStruct), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("SCRIPT_GLYPHPROP", SimStruct), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), label="LPArray", offset=0), SimTypePointer(SimTypeRef("GOFFSET", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeRef("ABC", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "rcRangeChars", "rpRangeProperties", "cRanges", "pwcChars", "pwLogClust", "pCharProps", "cChars", "pwGlyphs", "pGlyphProps", "cGlyphs", "piAdvance", "pGoffset", "pABC"]),
        #
        'ScriptItemizeOpenType': SimTypeFunction([SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeRef("SCRIPT_CONTROL", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_STATE", SimStruct), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ITEM", SimStruct), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pwcInChars", "cInChars", "cMaxItems", "psControl", "psState", "pItems", "pScriptTags", "pcItems"]),
        #
        'ScriptGetFontScriptTags': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "cMaxTags", "pScriptTags", "pcTags"]),
        #
        'ScriptGetFontLanguageTags': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "cMaxTags", "pLangsysTags", "pcTags"]),
        #
        'ScriptGetFontFeatureTags': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "cMaxTags", "pFeatureTags", "pcTags"]),
        #
        'ScriptGetFontAlternateGlyphs': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeShort(signed=False, label="UInt16"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "wGlyphId", "cMaxAlternates", "pAlternateGlyphs", "pcAlternates"]),
        #
        'ScriptSubstituteSingleGlyph': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypeShort(signed=False, label="UInt16"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "lParameter", "wGlyphId", "pwOutGlyphId"]),
        #
        'ScriptPositionSingleGlyph': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0), SimTypePointer(SimTypeRef("SCRIPT_ANALYSIS", SimStruct), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypeShort(signed=False, label="UInt16"), SimTypeInt(signed=True, label="Int32"), SimTypeRef("GOFFSET", SimStruct), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypeRef("GOFFSET", SimStruct), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "lParameter", "wGlyphId", "iAdvance", "GOffset", "piOutAdvance", "pOutGoffset"]),
    }

lib.set_prototypes(prototypes)
