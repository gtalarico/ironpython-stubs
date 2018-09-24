# encoding: utf-8
# module Tekla.Structures.Model calls itself Model
# from Tekla.Structures.Model, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Object(object):
    # no doc
    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: Object) -> Identifier

Set: Identifier(self: Object) = value
"""



class ModelObject(Object):
    # no doc
    def CompareTo(self, obj):
        """ CompareTo(self: ModelObject, obj: object) -> int """
        pass

    def Delete(self):
        """ Delete(self: ModelObject) -> bool """
        pass

    def DeleteInstance(self, *args): #cannot find CLR method
        """ DeleteInstance(self: ModelObject) -> bool """
        pass

    def Equals(self, *__args):
        """ Equals(self: ModelObject, other: ModelObject) -> bool """
        pass

    def GetAllReportProperties(self, stringNames, doubleNames, integerNames, values):
        """ GetAllReportProperties(self: ModelObject, stringNames: ArrayList, doubleNames: ArrayList, integerNames: ArrayList, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetAllUserProperties(self, values):
        """ GetAllUserProperties(self: ModelObject, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetChildren(self):
        """ GetChildren(self: ModelObject) -> ModelObjectEnumerator """
        pass

    def GetCoordinateSystem(self):
        """ GetCoordinateSystem(self: ModelObject) -> CoordinateSystem """
        pass

    def GetDoubleReportProperties(self, names, values):
        """ GetDoubleReportProperties(self: ModelObject, names: ArrayList, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetDoubleUserProperties(self, values):
        """ GetDoubleUserProperties(self: ModelObject, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetDynamicStringProperty(self, name, value):
        """ GetDynamicStringProperty(self: ModelObject, name: str, value: str) -> (bool, str) """
        pass

    def GetFatherComponent(self):
        """ GetFatherComponent(self: ModelObject) -> BaseComponent """
        pass

    def GetHierarchicObjects(self):
        """ GetHierarchicObjects(self: ModelObject) -> ModelObjectEnumerator """
        pass

    def GetIntegerReportProperties(self, names, values):
        """ GetIntegerReportProperties(self: ModelObject, names: ArrayList, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetIntegerUserProperties(self, values):
        """ GetIntegerUserProperties(self: ModelObject, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetPhase(self, phase):
        """ GetPhase(self: ModelObject) -> (bool, Phase) """
        pass

    def GetReportProperty(self, name, value):
        """
        GetReportProperty(self: ModelObject, name: str, value: int) -> (bool, int)
        GetReportProperty(self: ModelObject, name: str, value: float) -> (bool, float)
        GetReportProperty(self: ModelObject, name: str, value: str) -> (bool, str)
        """
        pass

    def GetStringReportProperties(self, names, values):
        """ GetStringReportProperties(self: ModelObject, names: ArrayList, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetStringUserProperties(self, values):
        """ GetStringUserProperties(self: ModelObject, values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetUserProperty(self, name, value):
        """
        GetUserProperty(self: ModelObject, name: str, value: int) -> (bool, int)
        GetUserProperty(self: ModelObject, name: str, value: float) -> (bool, float)
        GetUserProperty(self: ModelObject, name: str, value: str) -> (bool, str)
        """
        pass

    def Insert(self):
        """ Insert(self: ModelObject) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ModelObject) -> bool """
        pass

    def Select(self):
        """ Select(self: ModelObject) -> bool """
        pass

    def SetDynamicStringProperty(self, name, value):
        """ SetDynamicStringProperty(self: ModelObject, name: str, value: str) -> bool """
        pass

    def SetLabel(self, label):
        """ SetLabel(self: ModelObject, label: str) -> bool """
        pass

    def SetPhase(self, phase):
        """ SetPhase(self: ModelObject, phase: Phase) -> bool """
        pass

    def SetUserProperty(self, name, value):
        """
        SetUserProperty(self: ModelObject, name: str, value: int) -> bool
        SetUserProperty(self: ModelObject, name: str, value: float) -> bool
        SetUserProperty(self: ModelObject, name: str, value: str) -> bool
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsUpToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUpToDate(self: ModelObject) -> bool

"""

    ModificationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModificationTime(self: ModelObject) -> Nullable[DateTime]

"""


    ModelObjectEnum = None


class Assembly(ModelObject):
    """ Assembly() """
    def Add(self, *__args):
        """
        Add(self: Assembly, Assembly: Assembly) -> bool
        Add(self: Assembly, Assemblables: ArrayList) -> bool
        Add(self: Assembly, Object: IAssemblable) -> bool
        """
        pass

    def CompareTo(self, *__args):
        """ CompareTo(self: Assembly, AssemblyToCompare: Assembly) -> bool """
        pass

    def Delete(self):
        """ Delete(self: Assembly) -> bool """
        pass

    def GetAssembly(self):
        """ GetAssembly(self: Assembly) -> Assembly """
        pass

    def GetAssemblyType(self):
        """ GetAssemblyType(self: Assembly) -> AssemblyTypeEnum """
        pass

    def GetFatherPour(self):
        """ GetFatherPour(self: Assembly) -> PourObject """
        pass

    def GetMainPart(self):
        """ GetMainPart(self: Assembly) -> ModelObject """
        pass

    def GetSecondaries(self):
        """ GetSecondaries(self: Assembly) -> ArrayList """
        pass

    def GetSubAssemblies(self):
        """ GetSubAssemblies(self: Assembly) -> ArrayList """
        pass

    def Insert(self):
        """ Insert(self: Assembly) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Assembly) -> bool """
        pass

    def Remove(self, Object):
        """ Remove(self: Assembly, Object: ModelObject) -> bool """
        pass

    def Select(self):
        """ Select(self: Assembly) -> bool """
        pass

    def SetMainPart(self, Part):
        """ SetMainPart(self: Assembly, Part: Part) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    AssemblyNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyNumber(self: Assembly) -> NumberingSeries

Set: AssemblyNumber(self: Assembly) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Assembly) -> str

Set: Name(self: Assembly) = value
"""


    AssemblyTypeEnum = None


class BaseComponent(ModelObject):
    """ BaseComponent() """
    def AddAttributesToStack(self, *args): #cannot find CLR method
        """ AddAttributesToStack(self: BaseComponent) -> bool """
        pass

    def GetAttribute(self, AttrName, *__args):
        """
        GetAttribute(self: BaseComponent, AttrName: str, DValue: float) -> (bool, float)
        GetAttribute(self: BaseComponent, AttrName: str, Value: int) -> (bool, int)
        GetAttribute(self: BaseComponent, AttrName: str, StrValue: str) -> (bool, str)
        """
        pass

    def LoadAttributesFromFile(self, Filename):
        """ LoadAttributesFromFile(self: BaseComponent, Filename: str) -> bool """
        pass

    def LoadComponentAttributes(self, *args): #cannot find CLR method
        """ LoadComponentAttributes(self: BaseComponent) -> bool """
        pass

    def SetAttribute(self, AttrName, *__args):
        """ SetAttribute(self: BaseComponent, AttrName: str, DValue: float)SetAttribute(self: BaseComponent, AttrName: str, Value: int)SetAttribute(self: BaseComponent, AttrName: str, StrValue: str) """
        pass

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BaseComponent) -> str

Set: Name(self: BaseComponent) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: BaseComponent) -> int

Set: Number(self: BaseComponent) = value
"""

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ClassFromAttributeFile = -100
    ConnectionCodeFromAttributeFile = 'CodeFromAttrFile'
    CUSTOM_OBJECT_NUMBER = -1
    PLUGIN_OBJECT_NUMBER = -100000


class Reinforcement(ModelObject):
    # no doc
    def GetFatherPour(self):
        """ GetFatherPour(self: Reinforcement) -> PourObject """
        pass

    def GetNumberOfRebars(self):
        """ GetNumberOfRebars(self: Reinforcement) -> int """
        pass

    def GetRebarGeometries(self, withHooks):
        """ GetRebarGeometries(self: Reinforcement, withHooks: bool) -> ArrayList """
        pass

    def GetRebarGeometriesWithoutClashes(self, withHooks):
        """ GetRebarGeometriesWithoutClashes(self: Reinforcement, withHooks: bool) -> ArrayList """
        pass

    def GetSingleRebar(self, index, withHooks):
        """ GetSingleRebar(self: Reinforcement, index: int, withHooks: bool) -> RebarGeometry """
        pass

    def GetSingleRebarWithoutClash(self, index, withHooks):
        """ GetSingleRebarWithoutClash(self: Reinforcement, index: int, withHooks: bool) -> RebarGeometry """
        pass

    def GetSolid(self):
        """ GetSolid(self: Reinforcement) -> Solid """
        pass

    def IsGeometryValid(self):
        """ IsGeometryValid(self: Reinforcement) -> bool """
        pass

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: Reinforcement) -> int

Set: Class(self: Reinforcement) = value
"""

    EndPointOffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffsetType(self: Reinforcement) -> RebarOffsetTypeEnum

Set: EndPointOffsetType(self: Reinforcement) = value
"""

    EndPointOffsetValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffsetValue(self: Reinforcement) -> float

Set: EndPointOffsetValue(self: Reinforcement) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: Reinforcement) -> ModelObject

Set: Father(self: Reinforcement) = value
"""

    FromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromPlaneOffset(self: Reinforcement) -> float

Set: FromPlaneOffset(self: Reinforcement) = value
"""

    Grade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade(self: Reinforcement) -> str

Set: Grade(self: Reinforcement) = value
"""

    InputPointDeformingState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputPointDeformingState(self: Reinforcement) -> DeformingType

Set: InputPointDeformingState(self: Reinforcement) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Reinforcement) -> str

Set: Name(self: Reinforcement) = value
"""

    NumberingSeries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingSeries(self: Reinforcement) -> NumberingSeries

Set: NumberingSeries(self: Reinforcement) = value
"""

    OnPlaneOffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnPlaneOffsets(self: Reinforcement) -> ArrayList

Set: OnPlaneOffsets(self: Reinforcement) = value
"""

    RadiusValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusValues(self: Reinforcement) -> ArrayList

Set: RadiusValues(self: Reinforcement) = value
"""

    StartPointOffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffsetType(self: Reinforcement) -> RebarOffsetTypeEnum

Set: StartPointOffsetType(self: Reinforcement) = value
"""

    StartPointOffsetValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffsetValue(self: Reinforcement) -> float

Set: StartPointOffsetValue(self: Reinforcement) = value
"""


    RebarOffsetTypeEnum = None


class BaseRebarGroup(Reinforcement):
    # no doc
    EndFromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFromPlaneOffset(self: BaseRebarGroup) -> float

Set: EndFromPlaneOffset(self: BaseRebarGroup) = value
"""

    EndHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndHook(self: BaseRebarGroup) -> RebarHookData

Set: EndHook(self: BaseRebarGroup) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: BaseRebarGroup) -> Point

Set: EndPoint(self: BaseRebarGroup) = value
"""

    ExcludeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeType(self: BaseRebarGroup) -> ExcludeTypeEnum

Set: ExcludeType(self: BaseRebarGroup) = value
"""

    FromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromPlaneOffset(self: BaseRebarGroup) -> float

Set: FromPlaneOffset(self: BaseRebarGroup) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: BaseRebarGroup) -> str

Set: Size(self: BaseRebarGroup) = value
"""

    Spacings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacings(self: BaseRebarGroup) -> ArrayList

Set: Spacings(self: BaseRebarGroup) = value
"""

    SpacingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpacingType(self: BaseRebarGroup) -> RebarGroupSpacingTypeEnum

Set: SpacingType(self: BaseRebarGroup) = value
"""

    StartFromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartFromPlaneOffset(self: BaseRebarGroup) -> float

Set: StartFromPlaneOffset(self: BaseRebarGroup) = value
"""

    StartHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartHook(self: BaseRebarGroup) -> RebarHookData

Set: StartHook(self: BaseRebarGroup) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: BaseRebarGroup) -> Point

Set: StartPoint(self: BaseRebarGroup) = value
"""


    ExcludeTypeEnum = None
    RebarGroupSpacingTypeEnum = None


class BaseRebarModifier(ModelObject):
    # no doc
    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: BaseRebarModifier) -> bool """
        pass

    def Delete(self):
        """ Delete(self: BaseRebarModifier) -> bool """
        pass

    def FromStruct(self, *args): #cannot find CLR method
        """ FromStruct(self: BaseRebarModifier, dotStrip: dotRebarStrip_t) -> dotRebarStrip_t """
        pass

    def Insert(self):
        """ Insert(self: BaseRebarModifier) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BaseRebarModifier) -> bool """
        pass

    def ModifyInstance(self, *args): #cannot find CLR method
        """ ModifyInstance(self: BaseRebarModifier) -> bool """
        pass

    def Select(self):
        """ Select(self: BaseRebarModifier) -> bool """
        pass

    def SelectInstance(self, *args): #cannot find CLR method
        """ SelectInstance(self: BaseRebarModifier) -> bool """
        pass

    def ToStruct(self, *args): #cannot find CLR method
        """ ToStruct(self: BaseRebarModifier, dotStrip: dotRebarStrip_t) -> dotRebarStrip_t """
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: BaseRebarModifier) -> Contour

Set: Curve(self: BaseRebarModifier) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: BaseRebarModifier) -> RebarSet

Set: Father(self: BaseRebarModifier) = value
"""



class BaseWeld(ModelObject):
    # no doc
    def GetSolid(self):
        """ GetSolid(self: BaseWeld) -> Solid """
        pass

    def GetWeldGeometries(self):
        """ GetWeldGeometries(self: BaseWeld) -> ArrayList """
        pass

    AngleAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleAbove(self: BaseWeld) -> float

Set: AngleAbove(self: BaseWeld) = value
"""

    AngleBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBelow(self: BaseWeld) -> float

Set: AngleBelow(self: BaseWeld) = value
"""

    AroundWeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AroundWeld(self: BaseWeld) -> bool

Set: AroundWeld(self: BaseWeld) = value
"""

    ConnectAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectAssemblies(self: BaseWeld) -> bool

Set: ConnectAssemblies(self: BaseWeld) = value
"""

    ContourAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourAbove(self: BaseWeld) -> WeldContourEnum

Set: ContourAbove(self: BaseWeld) = value
"""

    ContourBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourBelow(self: BaseWeld) -> WeldContourEnum

Set: ContourBelow(self: BaseWeld) = value
"""

    EffectiveThroatAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveThroatAbove(self: BaseWeld) -> float

Set: EffectiveThroatAbove(self: BaseWeld) = value
"""

    EffectiveThroatBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveThroatBelow(self: BaseWeld) -> float

Set: EffectiveThroatBelow(self: BaseWeld) = value
"""

    ElectrodeClassification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElectrodeClassification(self: BaseWeld) -> WeldElectrodeClassificationEnum

Set: ElectrodeClassification(self: BaseWeld) = value
"""

    ElectrodeCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElectrodeCoefficient(self: BaseWeld) -> float

Set: ElectrodeCoefficient(self: BaseWeld) = value
"""

    ElectrodeStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElectrodeStrength(self: BaseWeld) -> float

Set: ElectrodeStrength(self: BaseWeld) = value
"""

    FinishAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinishAbove(self: BaseWeld) -> WeldFinishEnum

Set: FinishAbove(self: BaseWeld) = value
"""

    FinishBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinishBelow(self: BaseWeld) -> WeldFinishEnum

Set: FinishBelow(self: BaseWeld) = value
"""

    IncrementAmountAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementAmountAbove(self: BaseWeld) -> int

Set: IncrementAmountAbove(self: BaseWeld) = value
"""

    IncrementAmountBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementAmountBelow(self: BaseWeld) -> int

Set: IncrementAmountBelow(self: BaseWeld) = value
"""

    IntermittentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntermittentType(self: BaseWeld) -> WeldIntermittentTypeEnum

Set: IntermittentType(self: BaseWeld) = value
"""

    LengthAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthAbove(self: BaseWeld) -> float

Set: LengthAbove(self: BaseWeld) = value
"""

    LengthBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthBelow(self: BaseWeld) -> float

Set: LengthBelow(self: BaseWeld) = value
"""

    MainObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainObject(self: BaseWeld) -> ModelObject

Set: MainObject(self: BaseWeld) = value
"""

    NDTInspection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NDTInspection(self: BaseWeld) -> WeldNDTInspectionEnum

Set: NDTInspection(self: BaseWeld) = value
"""

    PitchAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PitchAbove(self: BaseWeld) -> float

Set: PitchAbove(self: BaseWeld) = value
"""

    PitchBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PitchBelow(self: BaseWeld) -> float

Set: PitchBelow(self: BaseWeld) = value
"""

    Placement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Placement(self: BaseWeld) -> WeldPlacementTypeEnum

Set: Placement(self: BaseWeld) = value
"""

    PrefixAboveLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrefixAboveLine(self: BaseWeld) -> str

Set: PrefixAboveLine(self: BaseWeld) = value
"""

    PrefixBelowLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrefixBelowLine(self: BaseWeld) -> str

Set: PrefixBelowLine(self: BaseWeld) = value
"""

    Preparation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preparation(self: BaseWeld) -> WeldPreparationTypeEnum

Set: Preparation(self: BaseWeld) = value
"""

    ProcessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessType(self: BaseWeld) -> WeldProcessTypeEnum

Set: ProcessType(self: BaseWeld) = value
"""

    ReferenceText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceText(self: BaseWeld) -> str

Set: ReferenceText(self: BaseWeld) = value
"""

    RootFaceAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootFaceAbove(self: BaseWeld) -> float

Set: RootFaceAbove(self: BaseWeld) = value
"""

    RootFaceBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootFaceBelow(self: BaseWeld) -> float

Set: RootFaceBelow(self: BaseWeld) = value
"""

    RootOpeningAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootOpeningAbove(self: BaseWeld) -> float

Set: RootOpeningAbove(self: BaseWeld) = value
"""

    RootOpeningBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootOpeningBelow(self: BaseWeld) -> float

Set: RootOpeningBelow(self: BaseWeld) = value
"""

    SecondaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryObject(self: BaseWeld) -> ModelObject

Set: SecondaryObject(self: BaseWeld) = value
"""

    ShopWeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShopWeld(self: BaseWeld) -> bool

Set: ShopWeld(self: BaseWeld) = value
"""

    SizeAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeAbove(self: BaseWeld) -> float

Set: SizeAbove(self: BaseWeld) = value
"""

    SizeBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeBelow(self: BaseWeld) -> float

Set: SizeBelow(self: BaseWeld) = value
"""

    Standard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Standard(self: BaseWeld) -> str

Set: Standard(self: BaseWeld) = value
"""

    StitchWeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StitchWeld(self: BaseWeld) -> bool

Set: StitchWeld(self: BaseWeld) = value
"""

    TypeAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeAbove(self: BaseWeld) -> WeldTypeEnum

Set: TypeAbove(self: BaseWeld) = value
"""

    TypeBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeBelow(self: BaseWeld) -> WeldTypeEnum

Set: TypeBelow(self: BaseWeld) = value
"""

    WeldNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldNumber(self: BaseWeld) -> int

"""

    WeldNumberPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldNumberPrefix(self: BaseWeld) -> str

Set: WeldNumberPrefix(self: BaseWeld) = value
"""


    WeldContourEnum = None
    WeldElectrodeClassificationEnum = None
    WeldFinishEnum = None
    WeldIntermittentTypeEnum = None
    WeldNDTInspectionEnum = None
    WeldPlacementTypeEnum = None
    WeldPreparationTypeEnum = None
    WeldProcessTypeEnum = None
    WeldTypeEnum = None


class Part(ModelObject):
    """ Part() """
    def CompareTo(self, *__args):
        """ CompareTo(self: Part, partToCompare: Part) -> bool """
        pass

    def GetAssembly(self):
        """ GetAssembly(self: Part) -> Assembly """
        pass

    def GetBolts(self):
        """ GetBolts(self: Part) -> ModelObjectEnumerator """
        pass

    def GetBooleans(self):
        """ GetBooleans(self: Part) -> ModelObjectEnumerator """
        pass

    def GetCenterLine(self, withCutsFittings):
        """ GetCenterLine(self: Part, withCutsFittings: bool) -> ArrayList """
        pass

    def GetComponents(self):
        """ GetComponents(self: Part) -> ModelObjectEnumerator """
        pass

    def GetDSTVCoordinateSystem(self):
        """ GetDSTVCoordinateSystem(self: Part) -> CoordinateSystem """
        pass

    def GetPartMark(self):
        """ GetPartMark(self: Part) -> str """
        pass

    def GetPours(self):
        """ GetPours(self: Part) -> ModelObjectEnumerator """
        pass

    def GetReferenceLine(self, withCutsFittings):
        """ GetReferenceLine(self: Part, withCutsFittings: bool) -> ArrayList """
        pass

    def GetReinforcements(self):
        """ GetReinforcements(self: Part) -> ModelObjectEnumerator """
        pass

    def GetSolid(self, *__args):
        """
        GetSolid(self: Part, formingStates: FormingStates) -> Solid
        GetSolid(self: Part, solidCreationType: SolidCreationTypeEnum) -> Solid
        GetSolid(self: Part) -> Solid
        """
        pass

    def GetSurfaceObjects(self):
        """ GetSurfaceObjects(self: Part) -> ModelObjectEnumerator """
        pass

    def GetSurfaceTreatments(self):
        """ GetSurfaceTreatments(self: Part) -> ModelObjectEnumerator """
        pass

    def GetWelds(self):
        """ GetWelds(self: Part) -> ModelObjectEnumerator """
        pass

    AssemblyNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyNumber(self: Part) -> NumberingSeries

Set: AssemblyNumber(self: Part) = value
"""

    CastUnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CastUnitType(self: Part) -> CastUnitTypeEnum

Set: CastUnitType(self: Part) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: Part) -> str

Set: Class(self: Part) = value
"""

    DeformingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeformingData(self: Part) -> DeformingData

Set: DeformingData(self: Part) = value
"""

    Finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Finish(self: Part) -> str

Set: Finish(self: Part) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Part) -> Material

Set: Material(self: Part) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Part) -> str

Set: Name(self: Part) = value
"""

    PartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartNumber(self: Part) -> NumberingSeries

Set: PartNumber(self: Part) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Part) -> Position

Set: Position(self: Part) = value
"""

    PourPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PourPhase(self: Part) -> int

Set: PourPhase(self: Part) = value
"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile(self: Part) -> Profile

Set: Profile(self: Part) = value
"""


    CastUnitTypeEnum = None


class Beam(Part):
    """
    Beam()
    Beam(beamType: BeamTypeEnum)
    Beam(startPoint: Point, endPoint: Point)
    """
    def Delete(self):
        """ Delete(self: Beam) -> bool """
        pass

    def Insert(self):
        """ Insert(self: Beam) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Beam) -> bool """
        pass

    def Select(self):
        """ Select(self: Beam) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, beamType: BeamTypeEnum)
        __new__(cls: type, startPoint: Point, endPoint: Point)
        """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Beam) -> Point

Set: EndPoint(self: Beam) = value
"""

    EndPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffset(self: Beam) -> Offset

Set: EndPointOffset(self: Beam) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Beam) -> Point

Set: StartPoint(self: Beam) = value
"""

    StartPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffset(self: Beam) -> Offset

Set: StartPointOffset(self: Beam) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Beam) -> BeamTypeEnum

"""


    BeamTypeEnum = None


class BentPlate(Part):
    """ BentPlate() """
    def Delete(self):
        """ Delete(self: BentPlate) -> bool """
        pass

    def Insert(self):
        """ Insert(self: BentPlate) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BentPlate) -> bool """
        pass

    def Select(self):
        """ Select(self: BentPlate) -> bool """
        pass

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: BentPlate) -> ConnectiveGeometry

Set: Geometry(self: BentPlate) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: BentPlate) -> float

"""



class BentPlateGeometrySolver(object):
    """ BentPlateGeometrySolver() """
    def AddLeg(self, geometry, *__args):
        """
        AddLeg(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, segment1: LineSegment, polygon: Contour, segment2: LineSegment) -> ConnectiveGeometry
        AddLeg(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, segment1: LineSegment, polygon: Contour, segment2: LineSegment, radius: float) -> ConnectiveGeometry
        AddLeg(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, polygon: Contour) -> ConnectiveGeometry
        AddLeg(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, polygon: Contour, radius: float) -> ConnectiveGeometry
        """
        pass

    def ModifyCylindricalSurface(self, geometry, cylindricalSection, surface):
        """ ModifyCylindricalSurface(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, cylindricalSection: GeometrySection, surface: CylindricalSurface) -> ConnectiveGeometry """
        pass

    def ModifyPolygon(self, geometry, polygonSection, points):
        """ ModifyPolygon(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, polygonSection: GeometrySection, points: Contour) -> ConnectiveGeometry """
        pass

    def ModifyRadius(self, geometry, cylindricalSection, radius):
        """ ModifyRadius(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, cylindricalSection: GeometrySection, radius: float) -> ConnectiveGeometry """
        pass

    def RemoveLeg(self, geometry, legSection):
        """ RemoveLeg(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, legSection: GeometrySection) -> ConnectiveGeometry """
        pass

    def Split(self, geometry, geometrySection):
        """ Split(self: BentPlateGeometrySolver, geometry: ConnectiveGeometry, geometrySection: GeometrySection) -> IList[ConnectiveGeometry] """
        pass

    OperationStatus = None


class BoltGroup(ModelObject):
    """ BoltGroup() """
    def AddOtherPartToBolt(self, M):
        """ AddOtherPartToBolt(self: BoltGroup, M: Part) -> bool """
        pass

    def GetFatherPour(self):
        """ GetFatherPour(self: BoltGroup) -> PourObject """
        pass

    def GetOtherPartsToBolt(self):
        """ GetOtherPartsToBolt(self: BoltGroup) -> ArrayList """
        pass

    def GetSolid(self, withHighAccuracy=None):
        """
        GetSolid(self: BoltGroup, withHighAccuracy: bool) -> Solid
        GetSolid(self: BoltGroup) -> Solid
        """
        pass

    def RemoveOtherPartToBolt(self, M):
        """ RemoveOtherPartToBolt(self: BoltGroup, M: Part) -> bool """
        pass

    Bolt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt(self: BoltGroup) -> bool

Set: Bolt(self: BoltGroup) = value
"""

    BoltPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltPositions(self: BoltGroup) -> ArrayList

"""

    BoltSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltSize(self: BoltGroup) -> float

Set: BoltSize(self: BoltGroup) = value
"""

    BoltStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltStandard(self: BoltGroup) -> str

Set: BoltStandard(self: BoltGroup) = value
"""

    BoltType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltType(self: BoltGroup) -> BoltTypeEnum

Set: BoltType(self: BoltGroup) = value
"""

    ConnectAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectAssemblies(self: BoltGroup) -> bool

Set: ConnectAssemblies(self: BoltGroup) = value
"""

    CutLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutLength(self: BoltGroup) -> float

Set: CutLength(self: BoltGroup) = value
"""

    EndPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffset(self: BoltGroup) -> Offset

Set: EndPointOffset(self: BoltGroup) = value
"""

    ExtraLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtraLength(self: BoltGroup) -> float

Set: ExtraLength(self: BoltGroup) = value
"""

    FirstPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstPosition(self: BoltGroup) -> Point

Set: FirstPosition(self: BoltGroup) = value
"""

    Hole1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hole1(self: BoltGroup) -> bool

Set: Hole1(self: BoltGroup) = value
"""

    Hole2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hole2(self: BoltGroup) -> bool

Set: Hole2(self: BoltGroup) = value
"""

    Hole3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hole3(self: BoltGroup) -> bool

Set: Hole3(self: BoltGroup) = value
"""

    Hole4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hole4(self: BoltGroup) -> bool

Set: Hole4(self: BoltGroup) = value
"""

    Hole5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hole5(self: BoltGroup) -> bool

Set: Hole5(self: BoltGroup) = value
"""

    HoleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HoleType(self: BoltGroup) -> BoltHoleTypeEnum

Set: HoleType(self: BoltGroup) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: BoltGroup) -> float

Set: Length(self: BoltGroup) = value
"""

    Nut1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nut1(self: BoltGroup) -> bool

Set: Nut1(self: BoltGroup) = value
"""

    Nut2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nut2(self: BoltGroup) -> bool

Set: Nut2(self: BoltGroup) = value
"""

    OtherPartsToBolt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OtherPartsToBolt(self: BoltGroup) -> ArrayList

"""

    PartToBeBolted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartToBeBolted(self: BoltGroup) -> Part

Set: PartToBeBolted(self: BoltGroup) = value
"""

    PartToBoltTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartToBoltTo(self: BoltGroup) -> Part

Set: PartToBoltTo(self: BoltGroup) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: BoltGroup) -> Position

Set: Position(self: BoltGroup) = value
"""

    RotateSlots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotateSlots(self: BoltGroup) -> BoltRotateSlotsEnum

Set: RotateSlots(self: BoltGroup) = value
"""

    SecondPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondPosition(self: BoltGroup) -> Point

Set: SecondPosition(self: BoltGroup) = value
"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SlottedHoleX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlottedHoleX(self: BoltGroup) -> float

Set: SlottedHoleX(self: BoltGroup) = value
"""

    SlottedHoleY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlottedHoleY(self: BoltGroup) -> float

Set: SlottedHoleY(self: BoltGroup) = value
"""

    StartPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffset(self: BoltGroup) -> Offset

Set: StartPointOffset(self: BoltGroup) = value
"""

    ThreadInMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadInMaterial(self: BoltGroup) -> BoltThreadInMaterialEnum

Set: ThreadInMaterial(self: BoltGroup) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: BoltGroup) -> float

Set: Tolerance(self: BoltGroup) = value
"""

    Washer1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Washer1(self: BoltGroup) -> bool

Set: Washer1(self: BoltGroup) = value
"""

    Washer2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Washer2(self: BoltGroup) -> bool

Set: Washer2(self: BoltGroup) = value
"""

    Washer3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Washer3(self: BoltGroup) -> bool

Set: Washer3(self: BoltGroup) = value
"""


    BoltHoleTypeEnum = None
    BoltRotateSlotsEnum = None
    BoltShapeEnum = None
    BoltThreadInMaterialEnum = None
    BoltTypeEnum = None


class BoltArray(BoltGroup):
    """ BoltArray() """
    def AddBoltDistX(self, DistX):
        """ AddBoltDistX(self: BoltArray, DistX: float) -> bool """
        pass

    def AddBoltDistY(self, DistY):
        """ AddBoltDistY(self: BoltArray, DistY: float) -> bool """
        pass

    def Delete(self):
        """ Delete(self: BoltArray) -> bool """
        pass

    def GetBoltDistX(self, Index):
        """ GetBoltDistX(self: BoltArray, Index: int) -> float """
        pass

    def GetBoltDistXCount(self):
        """ GetBoltDistXCount(self: BoltArray) -> int """
        pass

    def GetBoltDistY(self, Index):
        """ GetBoltDistY(self: BoltArray, Index: int) -> float """
        pass

    def GetBoltDistYCount(self):
        """ GetBoltDistYCount(self: BoltArray) -> int """
        pass

    def Insert(self):
        """ Insert(self: BoltArray) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BoltArray) -> bool """
        pass

    def RemoveBoltDistX(self, Index):
        """ RemoveBoltDistX(self: BoltArray, Index: int) -> bool """
        pass

    def RemoveBoltDistY(self, Index):
        """ RemoveBoltDistY(self: BoltArray, Index: int) -> bool """
        pass

    def Select(self):
        """ Select(self: BoltArray) -> bool """
        pass

    def SetBoltDistX(self, Index, DistX):
        """ SetBoltDistX(self: BoltArray, Index: int, DistX: float) -> bool """
        pass

    def SetBoltDistY(self, Index, DistY):
        """ SetBoltDistY(self: BoltArray, Index: int, DistY: float) -> bool """
        pass

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BoltCircle(BoltGroup):
    """ BoltCircle() """
    def Delete(self):
        """ Delete(self: BoltCircle) -> bool """
        pass

    def Insert(self):
        """ Insert(self: BoltCircle) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BoltCircle) -> bool """
        pass

    def Select(self):
        """ Select(self: BoltCircle) -> bool """
        pass

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: BoltCircle) -> float

Set: Diameter(self: BoltCircle) = value
"""

    NumberOfBolts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfBolts(self: BoltCircle) -> float

Set: NumberOfBolts(self: BoltCircle) = value
"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BoltXYList(BoltGroup):
    """ BoltXYList() """
    def AddBoltDistX(self, DistX):
        """ AddBoltDistX(self: BoltXYList, DistX: float) -> bool """
        pass

    def AddBoltDistY(self, DistY):
        """ AddBoltDistY(self: BoltXYList, DistY: float) -> bool """
        pass

    def Delete(self):
        """ Delete(self: BoltXYList) -> bool """
        pass

    def GetBoltDistX(self, Index):
        """ GetBoltDistX(self: BoltXYList, Index: int) -> float """
        pass

    def GetBoltDistXCount(self):
        """ GetBoltDistXCount(self: BoltXYList) -> int """
        pass

    def GetBoltDistY(self, Index):
        """ GetBoltDistY(self: BoltXYList, Index: int) -> float """
        pass

    def GetBoltDistYCount(self):
        """ GetBoltDistYCount(self: BoltXYList) -> int """
        pass

    def Insert(self):
        """ Insert(self: BoltXYList) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BoltXYList) -> bool """
        pass

    def Select(self):
        """ Select(self: BoltXYList) -> bool """
        pass

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Boolean(ModelObject):
    """ Boolean() """
    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: Boolean) -> ModelObject

Set: Father(self: Boolean) = value
"""



class BooleanPart(Boolean):
    """ BooleanPart() """
    def Delete(self):
        """ Delete(self: BooleanPart) -> bool """
        pass

    def Insert(self):
        """ Insert(self: BooleanPart) -> bool """
        pass

    def Modify(self):
        """ Modify(self: BooleanPart) -> bool """
        pass

    def Select(self):
        """ Select(self: BooleanPart) -> bool """
        pass

    def SetOperativePart(self, Part):
        """ SetOperativePart(self: BooleanPart, Part: Part) -> bool """
        pass

    OperativePart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OperativePart(self: BooleanPart) -> Part

Set: OperativePart(self: BooleanPart) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: BooleanPart) -> BooleanTypeEnum

Set: Type(self: BooleanPart) = value
"""


    BooleanOperativeClassName = 'BlOpCl'
    BooleanTypeEnum = None


class Brep(Part):
    """
    Brep()
    Brep(startPoint: Point, endPoint: Point)
    """
    def Delete(self):
        """ Delete(self: Brep) -> bool """
        pass

    def Insert(self):
        """ Insert(self: Brep) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Brep) -> bool """
        pass

    def Select(self):
        """ Select(self: Brep) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, startPoint=None, endPoint=None):
        """
        __new__(cls: type)
        __new__(cls: type, startPoint: Point, endPoint: Point)
        """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Brep) -> Point

Set: EndPoint(self: Brep) = value
"""

    EndPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffset(self: Brep) -> Offset

Set: EndPointOffset(self: Brep) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Brep) -> Point

Set: StartPoint(self: Brep) = value
"""

    StartPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffset(self: Brep) -> Offset

Set: StartPointOffset(self: Brep) = value
"""



class Chamfer(object):
    """
    Chamfer()
    Chamfer(X: float, Y: float, Type: ChamferTypeEnum)
    """
    @staticmethod # known case of __new__
    def __new__(self, X=None, Y=None, Type=None):
        """
        __new__(cls: type)
        __new__(cls: type, X: float, Y: float, Type: ChamferTypeEnum)
        """
        pass

    DZ1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DZ1(self: Chamfer) -> float

Set: DZ1(self: Chamfer) = value
"""

    DZ2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DZ2(self: Chamfer) -> float

Set: DZ2(self: Chamfer) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Chamfer) -> ChamferTypeEnum

Set: Type(self: Chamfer) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Chamfer) -> float

Set: X(self: Chamfer) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Chamfer) -> float

Set: Y(self: Chamfer) = value
"""


    ChamferTypeEnum = None


class ChangeData(object):
    # no doc
    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ChangeData) -> ModelObject

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ChangeData) -> ChangeTypeEnum

"""


    ChangeTypeEnum = None


class CircleRebarGroup(BaseRebarGroup):
    """ CircleRebarGroup() """
    def Delete(self):
        """ Delete(self: CircleRebarGroup) -> bool """
        pass

    def Insert(self):
        """ Insert(self: CircleRebarGroup) -> bool """
        pass

    def Modify(self):
        """ Modify(self: CircleRebarGroup) -> bool """
        pass

    def Select(self):
        """ Select(self: CircleRebarGroup) -> bool """
        pass

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: CircleRebarGroup) -> Polygon

Set: Polygon(self: CircleRebarGroup) = value
"""

    StirrupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StirrupType(self: CircleRebarGroup) -> CircleRebarGroupStirrupTypeEnum

Set: StirrupType(self: CircleRebarGroup) = value
"""


    CircleRebarGroupStirrupTypeEnum = None


class ClashCheckData(object):
    """ ClashCheckData() """
    Object1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object1(self: ClashCheckData) -> ModelObject

"""

    Object2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object2(self: ClashCheckData) -> ModelObject

"""

    Overlap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overlap(self: ClashCheckData) -> float

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ClashCheckData) -> ClashTypeEnum

"""


    ClashTypeEnum = None


class ClashCheckHandler(object):
    # no doc
    def GetIntersectionBoundingBoxes(self, ID1, ID2):
        """ GetIntersectionBoundingBoxes(self: ClashCheckHandler, ID1: Identifier, ID2: Identifier) -> ArrayList """
        pass

    def RunClashCheck(self):
        """ RunClashCheck(self: ClashCheckHandler) -> bool """
        pass

    def StopClashCheck(self):
        """ StopClashCheck(self: ClashCheckHandler) -> bool """
        pass


class Component(BaseComponent):
    """
    Component()
    Component(I: ComponentInput)
    """
    def Delete(self):
        """ Delete(self: Component) -> bool """
        pass

    def GetAssembly(self):
        """ GetAssembly(self: Component) -> Assembly """
        pass

    def GetComponentInput(self):
        """ GetComponentInput(self: Component) -> ComponentInput """
        pass

    def GetComponents(self):
        """ GetComponents(self: Component) -> ModelObjectEnumerator """
        pass

    def Insert(self):
        """ Insert(self: Component) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Component) -> bool """
        pass

    def Select(self):
        """ Select(self: Component) -> bool """
        pass

    def SetComponentInput(self, I):
        """ SetComponentInput(self: Component, I: ComponentInput) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, I=None):
        """
        __new__(cls: type)
        __new__(cls: type, I: ComponentInput)
        """
        pass

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ComponentInput(object):
    """ ComponentInput() """
    def AddInputObject(self, M):
        """ AddInputObject(self: ComponentInput, M: ModelObject) -> bool """
        pass

    def AddInputObjects(self, Objects):
        """ AddInputObjects(self: ComponentInput, Objects: ArrayList) -> bool """
        pass

    def AddInputPolygon(self, P):
        """ AddInputPolygon(self: ComponentInput, P: Polygon) -> bool """
        pass

    def AddOneInputPosition(self, P):
        """ AddOneInputPosition(self: ComponentInput, P: Point) -> bool """
        pass

    def AddTwoInputPositions(self, Position1, Position2):
        """ AddTwoInputPositions(self: ComponentInput, Position1: Point, Position2: Point) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: ComponentInput, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ComponentInput) -> IEnumerator """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ComponentInput) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: ComponentInput) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: ComponentInput) -> object

"""



class Connection(BaseComponent):
    """ Connection() """
    def Delete(self):
        """ Delete(self: Connection) -> bool """
        pass

    def GetPrimaryObject(self):
        """ GetPrimaryObject(self: Connection) -> ModelObject """
        pass

    def GetSecondaryObjects(self):
        """ GetSecondaryObjects(self: Connection) -> ArrayList """
        pass

    def Insert(self):
        """ Insert(self: Connection) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Connection) -> bool """
        pass

    def Select(self):
        """ Select(self: Connection) -> bool """
        pass

    def SetPrimaryObject(self, M):
        """ SetPrimaryObject(self: Connection, M: ModelObject) -> bool """
        pass

    def SetSecondaryObject(self, M):
        """ SetSecondaryObject(self: Connection, M: ModelObject) -> bool """
        pass

    def SetSecondaryObjects(self, Secondaries):
        """ SetSecondaryObjects(self: Connection, Secondaries: ArrayList) -> bool """
        pass

    AutoDirectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoDirectionType(self: Connection) -> AutoDirectionTypeEnum

Set: AutoDirectionType(self: Connection) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: Connection) -> int

Set: Class(self: Connection) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Connection) -> str

Set: Code(self: Connection) = value
"""

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionType(self: Connection) -> PositionTypeEnum

Set: PositionType(self: Connection) = value
"""

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: Connection) -> ConnectionStatusEnum

"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: Connection) -> Vector

Set: UpVector(self: Connection) = value
"""



class ConnectiveGeometry(object):
    """ ConnectiveGeometry(contour: Contour) """
    def GetConnection(self, geometrySection1, geometrySection2):
        """ GetConnection(self: ConnectiveGeometry, geometrySection1: GeometrySection, geometrySection2: GeometrySection) -> IList[LineSegment] """
        pass

    def GetGeometryEnumerator(self):
        """ GetGeometryEnumerator(self: ConnectiveGeometry) -> GeometrySectionEnumerator """
        pass

    def GetGeometryLegSections(self):
        """ GetGeometryLegSections(self: ConnectiveGeometry) -> IList[GeometrySection] """
        pass

    def GetNeighborSections(self, geometrySection):
        """ GetNeighborSections(self: ConnectiveGeometry, geometrySection: GeometrySection) -> IList[GeometrySection] """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: ConnectiveGeometry) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, contour):
        """ __new__(cls: type, contour: Contour) """
        pass

    InvalidGeometrySectionIndex = -1


class ConnectiveGeometryException(Exception):
    """
    ConnectiveGeometryException()
    ConnectiveGeometryException(status: OperationStatus, errorMessage: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, status=None, errorMessage=None):
        """
        __new__(cls: type)
        __new__(cls: type, status: OperationStatus, errorMessage: str)
        """
        pass

    OperationStatus = None


class Contour(object):
    """ Contour() """
    def AddContourPoint(self, Point):
        """ AddContourPoint(self: Contour, Point: ContourPoint) """
        pass

    def CalculatePolygon(self, polygon):
        """ CalculatePolygon(self: Contour) -> (bool, Polygon) """
        pass

    ContourPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourPoints(self: Contour) -> ArrayList

Set: ContourPoints(self: Contour) = value
"""



class ContourPlate(Part):
    """ ContourPlate() """
    def AddContourPoint(self, contourPoint):
        """ AddContourPoint(self: ContourPlate, contourPoint: ContourPoint) -> bool """
        pass

    def Delete(self):
        """ Delete(self: ContourPlate) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ContourPlate) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ContourPlate) -> bool """
        pass

    def Select(self):
        """ Select(self: ContourPlate) -> bool """
        pass

    Contour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contour(self: ContourPlate) -> Contour

Set: Contour(self: ContourPlate) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ContourPlate) -> ContourPlateTypeEnum

"""


    ContourPlateTypeEnum = None


class ContourPoint(Point):
    """
    ContourPoint()
    ContourPoint(P: Point, C: Chamfer)
    """
    def SetPoint(self, P):
        """ SetPoint(self: ContourPoint, P: Point) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, P=None, C=None):
        """
        __new__(cls: type)
        __new__(cls: type, P: Point, C: Chamfer)
        """
        pass

    Chamfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chamfer(self: ContourPoint) -> Chamfer

Set: Chamfer(self: ContourPoint) = value
"""



class ControlCircle(ModelObject):
    """
    ControlCircle()
    ControlCircle(point1: Point, point2: Point, point3: Point)
    """
    def Delete(self):
        """ Delete(self: ControlCircle) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ControlCircle) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ControlCircle) -> bool """
        pass

    def Select(self):
        """ Select(self: ControlCircle) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, point1=None, point2=None, point3=None):
        """
        __new__(cls: type)
        __new__(cls: type, point1: Point, point2: Point, point3: Point)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: ControlCircle) -> ControlCircleColorEnum

Set: Color(self: ControlCircle) = value
"""

    Extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extension(self: ControlCircle) -> float

Set: Extension(self: ControlCircle) = value
"""

    Point1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point1(self: ControlCircle) -> Point

Set: Point1(self: ControlCircle) = value
"""

    Point2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point2(self: ControlCircle) -> Point

Set: Point2(self: ControlCircle) = value
"""

    Point3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point3(self: ControlCircle) -> Point

Set: Point3(self: ControlCircle) = value
"""


    ControlCircleColorEnum = None


class ControlLine(ModelObject):
    """
    ControlLine()
    ControlLine(Line: LineSegment, IsMagnetic: bool)
    """
    def Delete(self):
        """ Delete(self: ControlLine) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ControlLine) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ControlLine) -> bool """
        pass

    def Select(self):
        """ Select(self: ControlLine) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Line=None, IsMagnetic=None):
        """
        __new__(cls: type)
        __new__(cls: type, Line: LineSegment, IsMagnetic: bool)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: ControlLine) -> ControlLineColorEnum

Set: Color(self: ControlLine) = value
"""

    Extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extension(self: ControlLine) -> float

Set: Extension(self: ControlLine) = value
"""

    IsMagnetic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMagnetic(self: ControlLine) -> bool

Set: IsMagnetic(self: ControlLine) = value
"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Line(self: ControlLine) -> LineSegment

Set: Line(self: ControlLine) = value
"""


    ControlLineColorEnum = None


class ControlPlane(ModelObject):
    """
    ControlPlane()
    ControlPlane(P: Plane, IsMagnetic: bool)
    """
    def Delete(self):
        """ Delete(self: ControlPlane) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ControlPlane) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ControlPlane) -> bool """
        pass

    def Select(self):
        """ Select(self: ControlPlane) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, P=None, IsMagnetic=None):
        """
        __new__(cls: type)
        __new__(cls: type, P: Plane, IsMagnetic: bool)
        """
        pass

    IsMagnetic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMagnetic(self: ControlPlane) -> bool

Set: IsMagnetic(self: ControlPlane) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ControlPlane) -> str

Set: Name(self: ControlPlane) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: ControlPlane) -> Plane

Set: Plane(self: ControlPlane) = value
"""



class ControlPoint(ModelObject):
    """
    ControlPoint()
    ControlPoint(existPoint: Point)
    """
    def Delete(self):
        """ Delete(self: ControlPoint) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ControlPoint) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ControlPoint) -> bool """
        pass

    def Select(self):
        """ Select(self: ControlPoint) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, existPoint=None):
        """
        __new__(cls: type)
        __new__(cls: type, existPoint: Point)
        """
        pass

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ControlPoint) -> Point

Set: Point(self: ControlPoint) = value
"""



class CurvedRebarGroup(BaseRebarGroup):
    """ CurvedRebarGroup() """
    def Delete(self):
        """ Delete(self: CurvedRebarGroup) -> bool """
        pass

    def Insert(self):
        """ Insert(self: CurvedRebarGroup) -> bool """
        pass

    def Modify(self):
        """ Modify(self: CurvedRebarGroup) -> bool """
        pass

    def Select(self):
        """ Select(self: CurvedRebarGroup) -> bool """
        pass

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: CurvedRebarGroup) -> Polygon

Set: Polygon(self: CurvedRebarGroup) = value
"""



class CustomPart(BaseComponent):
    """
    CustomPart()
    CustomPart(StartPoint: Point, EndPoint: Point)
    """
    def Delete(self):
        """ Delete(self: CustomPart) -> bool """
        pass

    def GetAssembly(self):
        """ GetAssembly(self: CustomPart) -> Assembly """
        pass

    def GetComponents(self):
        """ GetComponents(self: CustomPart) -> ModelObjectEnumerator """
        pass

    def GetStartAndEndPositions(self, StartPoint, EndPoint):
        """ GetStartAndEndPositions(self: CustomPart, StartPoint: Point, EndPoint: Point) -> (bool, Point, Point) """
        pass

    def Insert(self):
        """ Insert(self: CustomPart) -> bool """
        pass

    def Modify(self):
        """ Modify(self: CustomPart) -> bool """
        pass

    def Select(self):
        """ Select(self: CustomPart) -> bool """
        pass

    def SetInputPositions(self, StartPoint, EndPoint):
        """ SetInputPositions(self: CustomPart, StartPoint: Point, EndPoint: Point) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, StartPoint=None, EndPoint=None):
        """
        __new__(cls: type)
        __new__(cls: type, StartPoint: Point, EndPoint: Point)
        """
        pass

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: CustomPart) -> Position

Set: Position(self: CustomPart) = value
"""

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CutPlane(Boolean):
    """ CutPlane() """
    def Delete(self):
        """ Delete(self: CutPlane) -> bool """
        pass

    def Insert(self):
        """ Insert(self: CutPlane) -> bool """
        pass

    def Modify(self):
        """ Modify(self: CutPlane) -> bool """
        pass

    def Select(self):
        """ Select(self: CutPlane) -> bool """
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: CutPlane) -> Plane

Set: Plane(self: CutPlane) = value
"""



class CylindricalSurface(object):
    """ CylindricalSurface(endFaceNormal1: Vector, endFaceNormal2: Vector, sideBoundary1: LineSegment, sideBoundary2: LineSegment) """
    @staticmethod # known case of __new__
    def __new__(self, endFaceNormal1, endFaceNormal2, sideBoundary1, sideBoundary2):
        """ __new__(cls: type, endFaceNormal1: Vector, endFaceNormal2: Vector, sideBoundary1: LineSegment, sideBoundary2: LineSegment) """
        pass

    EndFaceNormal1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFaceNormal1(self: CylindricalSurface) -> Vector

"""

    EndFaceNormal2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFaceNormal2(self: CylindricalSurface) -> Vector

"""

    IntersectionLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionLine(self: CylindricalSurface) -> Line

"""

    InwardCurved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InwardCurved(self: CylindricalSurface) -> bool

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: CylindricalSurface) -> float

"""

    SideBoundary1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SideBoundary1(self: CylindricalSurface) -> LineSegment

Set: SideBoundary1(self: CylindricalSurface) = value
"""

    SideBoundary2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SideBoundary2(self: CylindricalSurface) -> LineSegment

Set: SideBoundary2(self: CylindricalSurface) = value
"""



class CylindricalSurfaceNode(object):
    """ CylindricalSurfaceNode(surface: CylindricalSurface) """
    def AcceptVisitor(self, visitor):
        """ AcceptVisitor(self: CylindricalSurfaceNode, visitor: IGeometryNodeVisitor) """
        pass

    def Clone(self):
        """ Clone(self: CylindricalSurfaceNode) -> IGeometryNode """
        pass

    @staticmethod # known case of __new__
    def __new__(self, surface):
        """ __new__(cls: type, surface: CylindricalSurface) """
        pass

    IsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutomatic(self: CylindricalSurfaceNode) -> bool

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: CylindricalSurfaceNode) -> CylindricalSurface

"""



class DeformingData(object):
    """ DeformingData() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: DeformingData) -> float

Set: Angle(self: DeformingData) = value
"""

    Angle2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle2(self: DeformingData) -> float

Set: Angle2(self: DeformingData) = value
"""

    Cambering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cambering(self: DeformingData) -> float

Set: Cambering(self: DeformingData) = value
"""

    Shortening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shortening(self: DeformingData) -> float

Set: Shortening(self: DeformingData) = value
"""



class Detail(BaseComponent):
    """ Detail() """
    def Delete(self):
        """ Delete(self: Detail) -> bool """
        pass

    def GetPrimaryObject(self):
        """ GetPrimaryObject(self: Detail) -> ModelObject """
        pass

    def GetReferencePoint(self):
        """ GetReferencePoint(self: Detail) -> Point """
        pass

    def Insert(self):
        """ Insert(self: Detail) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Detail) -> bool """
        pass

    def Select(self):
        """ Select(self: Detail) -> bool """
        pass

    def SetPrimaryObject(self, M):
        """ SetPrimaryObject(self: Detail, M: ModelObject) -> bool """
        pass

    def SetReferencePoint(self, ReferencePoint):
        """ SetReferencePoint(self: Detail, ReferencePoint: Point) -> bool """
        pass

    AutoDirectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoDirectionType(self: Detail) -> AutoDirectionTypeEnum

Set: AutoDirectionType(self: Detail) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: Detail) -> int

Set: Class(self: Detail) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Detail) -> str

Set: Code(self: Detail) = value
"""

    DetailType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetailType(self: Detail) -> DetailTypeEnum

Set: DetailType(self: Detail) = value
"""

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionType(self: Detail) -> PositionTypeEnum

Set: PositionType(self: Detail) = value
"""

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: Detail) -> ConnectionStatusEnum

"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: Detail) -> Vector

Set: UpVector(self: Detail) = value
"""



class EdgeChamfer(Boolean):
    """
    EdgeChamfer()
    EdgeChamfer(FirstEnd: Point, SecondEnd: Point)
    """
    def Delete(self):
        """ Delete(self: EdgeChamfer) -> bool """
        pass

    def Insert(self):
        """ Insert(self: EdgeChamfer) -> bool """
        pass

    def Modify(self):
        """ Modify(self: EdgeChamfer) -> bool """
        pass

    def Select(self):
        """ Select(self: EdgeChamfer) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, FirstEnd=None, SecondEnd=None):
        """
        __new__(cls: type)
        __new__(cls: type, FirstEnd: Point, SecondEnd: Point)
        """
        pass

    Chamfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chamfer(self: EdgeChamfer) -> Chamfer

Set: Chamfer(self: EdgeChamfer) = value
"""

    FirstBevelDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstBevelDimension(self: EdgeChamfer) -> float

Set: FirstBevelDimension(self: EdgeChamfer) = value
"""

    FirstChamferEndType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstChamferEndType(self: EdgeChamfer) -> ChamferEndTypeEnum

Set: FirstChamferEndType(self: EdgeChamfer) = value
"""

    FirstEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstEnd(self: EdgeChamfer) -> Point

Set: FirstEnd(self: EdgeChamfer) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EdgeChamfer) -> str

Set: Name(self: EdgeChamfer) = value
"""

    SecondBevelDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondBevelDimension(self: EdgeChamfer) -> float

Set: SecondBevelDimension(self: EdgeChamfer) = value
"""

    SecondChamferEndType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondChamferEndType(self: EdgeChamfer) -> ChamferEndTypeEnum

Set: SecondChamferEndType(self: EdgeChamfer) = value
"""

    SecondEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondEnd(self: EdgeChamfer) -> Point

Set: SecondEnd(self: EdgeChamfer) = value
"""


    ChamferEndTypeEnum = None


class Events(MarshalByRefObject):
    """ Events() """
    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Events) -> object """
        pass

    def OnClashCheckDone(self, eventName, parameters):
        """ OnClashCheckDone(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnClashDetected(self, eventName, parameters):
        """ OnClashDetected(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnCommandStatusChange(self, eventName, parameters):
        """ OnCommandStatusChange(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnDbCommit(self, eventName, parameters):
        """ OnDbCommit(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnModelLoad(self, eventName, parameters):
        """ OnModelLoad(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnModelObjectChanged(self, eventName, parameters):
        """ OnModelObjectChanged(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnModelObjectNumbered(self, eventName, parameters):
        """ OnModelObjectNumbered(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnModelSave(self, eventName, parameters):
        """ OnModelSave(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnModelSaveAs(self, eventName, parameters):
        """ OnModelSaveAs(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnNumbering(self, eventName, parameters):
        """ OnNumbering(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnSelectionChange(self, eventName, parameters):
        """ OnSelectionChange(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnTeklaStructuresExit(self, eventName, parameters):
        """ OnTeklaStructuresExit(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def OnTrackEvent(self, eventName, parameters):
        """ OnTrackEvent(self: Events, eventName: str, *parameters: Array[object]) """
        pass

    def Register(self):
        """ Register(self: Events) """
        pass

    def UnRegister(self):
        """ UnRegister(self: Events) """
        pass

    ClashCheckDone = None
    ClashCheckDoneDelegate = None
    ClashDetected = None
    ClashDetectedDelegate = None
    CommandStatusChange = None
    CommandStatusChangeDelegate = None
    ModelChanged = None
    ModelChangedDelegate = None
    ModelLoad = None
    ModelLoadDelegate = None
    ModelObjectChanged = None
    ModelObjectChangedDelegate = None
    ModelObjectNumbered = None
    ModelObjectNumberedDelegate = None
    ModelSave = None
    ModelSaveAs = None
    ModelSaveAsDelegate = None
    ModelSaveDelegate = None
    Numbering = None
    NumberingDelegate = None
    SelectionChange = None
    SelectionChangeDelegate = None
    TeklaStructuresExit = None
    TeklaStructuresExitDelegate = None
    TrackEvent = None
    TrackEventDelegate = None


class ExtensionIntersectsWithPlateException(ConnectiveGeometryException):
    """ ExtensionIntersectsWithPlateException() """

class FacePerpendicularToIntersectionLineException(ConnectiveGeometryException):
    """ FacePerpendicularToIntersectionLineException() """

class FacesAtAnObtuseAngleException(ConnectiveGeometryException):
    """ FacesAtAnObtuseAngleException() """

class FacesTooNearEachOtherException(ConnectiveGeometryException):
    """ FacesTooNearEachOtherException() """

class Fitting(Boolean):
    """ Fitting() """
    def Delete(self):
        """ Delete(self: Fitting) -> bool """
        pass

    def Insert(self):
        """ Insert(self: Fitting) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Fitting) -> bool """
        pass

    def Select(self):
        """ Select(self: Fitting) -> bool """
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Fitting) -> Plane

Set: Plane(self: Fitting) = value
"""



class GeneralConnectiveGeometryException(ConnectiveGeometryException):
    """ GeneralConnectiveGeometryException() """

class GeometrySection(object):
    # no doc
    GeometryNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryNode(self: GeometrySection) -> IGeometryNode

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: GeometrySection) -> int

"""



class GeometrySectionEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: GeometrySectionEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: GeometrySectionEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: GeometrySectionEnumerator) -> GeometrySection

"""



class Grid(ModelObject):
    """ Grid() """
    def Delete(self):
        """ Delete(self: Grid) -> bool """
        pass

    def Insert(self):
        """ Insert(self: Grid) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Grid) -> bool """
        pass

    def Select(self):
        """ Select(self: Grid) -> bool """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Grid) -> int

Set: Color(self: Grid) = value
"""

    CoordinateX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateX(self: Grid) -> str

Set: CoordinateX(self: Grid) = value
"""

    CoordinateY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateY(self: Grid) -> str

Set: CoordinateY(self: Grid) = value
"""

    CoordinateZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateZ(self: Grid) -> str

Set: CoordinateZ(self: Grid) = value
"""

    ExtensionForMagneticArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionForMagneticArea(self: Grid) -> float

Set: ExtensionForMagneticArea(self: Grid) = value
"""

    ExtensionLeftX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLeftX(self: Grid) -> float

Set: ExtensionLeftX(self: Grid) = value
"""

    ExtensionLeftY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLeftY(self: Grid) -> float

Set: ExtensionLeftY(self: Grid) = value
"""

    ExtensionLeftZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLeftZ(self: Grid) -> float

Set: ExtensionLeftZ(self: Grid) = value
"""

    ExtensionRightX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionRightX(self: Grid) -> float

Set: ExtensionRightX(self: Grid) = value
"""

    ExtensionRightY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionRightY(self: Grid) -> float

Set: ExtensionRightY(self: Grid) = value
"""

    ExtensionRightZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionRightZ(self: Grid) -> float

Set: ExtensionRightZ(self: Grid) = value
"""

    IsMagnetic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMagnetic(self: Grid) -> bool

Set: IsMagnetic(self: Grid) = value
"""

    LabelX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelX(self: Grid) -> str

Set: LabelX(self: Grid) = value
"""

    LabelY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelY(self: Grid) -> str

Set: LabelY(self: Grid) = value
"""

    LabelZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelZ(self: Grid) -> str

Set: LabelZ(self: Grid) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Grid) -> str

Set: Name(self: Grid) = value
"""



class GridPlane(ModelObject):
    """
    GridPlane()
    GridPlane(Plane: Plane, Label: str)
    """
    def Delete(self):
        """ Delete(self: GridPlane) -> bool """
        pass

    def Insert(self):
        """ Insert(self: GridPlane) -> bool """
        pass

    def Modify(self):
        """ Modify(self: GridPlane) -> bool """
        pass

    def Select(self):
        """ Select(self: GridPlane) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Plane=None, Label=None):
        """
        __new__(cls: type)
        __new__(cls: type, Plane: Plane, Label: str)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: GridPlane) -> int

Set: Color(self: GridPlane) = value
"""

    DrawingVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawingVisibility(self: GridPlane) -> bool

Set: DrawingVisibility(self: GridPlane) = value
"""

    ExtensionAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionAbove(self: GridPlane) -> float

Set: ExtensionAbove(self: GridPlane) = value
"""

    ExtensionBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionBelow(self: GridPlane) -> float

Set: ExtensionBelow(self: GridPlane) = value
"""

    ExtensionForMagneticArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionForMagneticArea(self: GridPlane) -> float

Set: ExtensionForMagneticArea(self: GridPlane) = value
"""

    ExtensionLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLeft(self: GridPlane) -> float

Set: ExtensionLeft(self: GridPlane) = value
"""

    ExtensionRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionRight(self: GridPlane) -> float

Set: ExtensionRight(self: GridPlane) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: GridPlane) -> Grid

Set: Father(self: GridPlane) = value
"""

    IsMagnetic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMagnetic(self: GridPlane) -> bool

Set: IsMagnetic(self: GridPlane) = value
"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: GridPlane) -> str

Set: Label(self: GridPlane) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: GridPlane) -> Plane

Set: Plane(self: GridPlane) = value
"""



class HierarchicDefinition(ModelObject):
    """
    HierarchicDefinition()
    HierarchicDefinition(ID: Identifier)
    """
    def AddObjects(self, Objects):
        """ AddObjects(self: HierarchicDefinition, Objects: ArrayList) -> bool """
        pass

    def Delete(self):
        """ Delete(self: HierarchicDefinition) -> bool """
        pass

    def Insert(self):
        """ Insert(self: HierarchicDefinition) -> bool """
        pass

    def Modify(self):
        """ Modify(self: HierarchicDefinition) -> bool """
        pass

    def RemoveObjects(self, Objects):
        """ RemoveObjects(self: HierarchicDefinition, Objects: ArrayList) -> bool """
        pass

    def Select(self):
        """ Select(self: HierarchicDefinition) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ID=None):
        """
        __new__(cls: type)
        __new__(cls: type, ID: Identifier)
        """
        pass

    CustomType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomType(self: HierarchicDefinition) -> str

Set: CustomType(self: HierarchicDefinition) = value
"""

    Drawable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Drawable(self: HierarchicDefinition) -> bool

Set: Drawable(self: HierarchicDefinition) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: HierarchicDefinition) -> HierarchicDefinition

Set: Father(self: HierarchicDefinition) = value
"""

    HierarchicChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HierarchicChildren(self: HierarchicDefinition) -> ArrayList

Set: HierarchicChildren(self: HierarchicDefinition) = value
"""

    HierarchyIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HierarchyIdentifier(self: HierarchicDefinition) -> str

Set: HierarchyIdentifier(self: HierarchicDefinition) = value
"""

    HierarchyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HierarchyType(self: HierarchicDefinition) -> HierarchicDefinitionTypeEnum

Set: HierarchyType(self: HierarchicDefinition) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HierarchicDefinition) -> str

Set: Name(self: HierarchicDefinition) = value
"""



class HierarchicDefinitionTypeEnum(Enum):
    """ enum HierarchicDefinitionTypeEnum, values: DOT_HIERARCHIC_CUSTOM_TYPE (0), DOT_HIERARCHIC_LOGICAL_BUILDING_AREA (1), DOT_HIERARCHIC_OBJECT_TYPE (2), DOT_HIERARCHIC_TASK_SCENARIO (4), DOT_HIERARCHIC_TASK_WORK_TYPE (3) """
    DOT_HIERARCHIC_CUSTOM_TYPE = None
    DOT_HIERARCHIC_LOGICAL_BUILDING_AREA = None
    DOT_HIERARCHIC_OBJECT_TYPE = None
    DOT_HIERARCHIC_TASK_SCENARIO = None
    DOT_HIERARCHIC_TASK_WORK_TYPE = None
    value__ = None


class HierarchicObject(ModelObject):
    """
    HierarchicObject()
    HierarchicObject(ID: Identifier)
    """
    def AddObjects(self, Objects):
        """ AddObjects(self: HierarchicObject, Objects: ArrayList) -> bool """
        pass

    def Delete(self):
        """ Delete(self: HierarchicObject) -> bool """
        pass

    def Insert(self):
        """ Insert(self: HierarchicObject) -> bool """
        pass

    def Modify(self):
        """ Modify(self: HierarchicObject) -> bool """
        pass

    def RemoveObjects(self, Objects):
        """ RemoveObjects(self: HierarchicObject, Objects: ArrayList) -> bool """
        pass

    def Select(self):
        """ Select(self: HierarchicObject) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ID=None):
        """
        __new__(cls: type)
        __new__(cls: type, ID: Identifier)
        """
        pass

    Definition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Definition(self: HierarchicObject) -> HierarchicDefinition

Set: Definition(self: HierarchicObject) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: HierarchicObject) -> HierarchicObject

Set: Father(self: HierarchicObject) = value
"""

    HierarchicChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HierarchicChildren(self: HierarchicObject) -> ArrayList

Set: HierarchicChildren(self: HierarchicObject) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HierarchicObject) -> str

Set: Name(self: HierarchicObject) = value
"""



class IAssemblable:
    # no doc
    def GetAssembly(self):
        """ GetAssembly(self: IAssemblable) -> Assembly """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGeometryNode:
    # no doc
    def AcceptVisitor(self, visitor):
        """ AcceptVisitor(self: IGeometryNode, visitor: IGeometryNodeVisitor) """
        pass

    def Clone(self):
        """ Clone(self: IGeometryNode) -> IGeometryNode """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutomatic(self: IGeometryNode) -> bool

"""



class IGeometryNodeVisitor:
    # no doc
    def Visit(self, node):
        """ Visit(self: IGeometryNodeVisitor, node: CylindricalSurfaceNode)Visit(self: IGeometryNodeVisitor, node: PolygonNode) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InputItem(object):
    # no doc
    def GetData(self):
        """ GetData(self: InputItem) -> object """
        pass

    def GetInputType(self):
        """ GetInputType(self: InputItem) -> InputTypeEnum """
        pass

    InputTypeEnum = None


class InvalidFacePointsException(ConnectiveGeometryException):
    """ InvalidFacePointsException() """

class InvalidRadiusException(ConnectiveGeometryException):
    """ InvalidRadiusException() """

class Load(ModelObject):
    """ Load() """
    AutomaticPrimaryAxisWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticPrimaryAxisWeight(self: Load) -> bool

Set: AutomaticPrimaryAxisWeight(self: Load) = value
"""

    BoundingBoxDx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBoxDx(self: Load) -> float

Set: BoundingBoxDx(self: Load) = value
"""

    BoundingBoxDy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBoxDy(self: Load) -> float

Set: BoundingBoxDy(self: Load) = value
"""

    BoundingBoxDz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBoxDz(self: Load) -> float

Set: BoundingBoxDz(self: Load) = value
"""

    CreateFixedSupportConditionsAutomatically = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateFixedSupportConditionsAutomatically(self: Load) -> bool

Set: CreateFixedSupportConditionsAutomatically(self: Load) = value
"""

    FatherId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FatherId(self: Load) -> Identifier

Set: FatherId(self: Load) = value
"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: Load) -> LoadGroup

Set: Group(self: Load) = value
"""

    LoadAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadAttachment(self: Load) -> LoadAttachmentEnum

Set: LoadAttachment(self: Load) = value
"""

    LoadDispersionAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadDispersionAngle(self: Load) -> float

Set: LoadDispersionAngle(self: Load) = value
"""

    PartFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartFilter(self: Load) -> str

Set: PartFilter(self: Load) = value
"""

    PartNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartNames(self: Load) -> LoadPartNamesEnum

Set: PartNames(self: Load) = value
"""

    PrimaryAxisDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryAxisDirection(self: Load) -> Vector

Set: PrimaryAxisDirection(self: Load) = value
"""

    Spanning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spanning(self: Load) -> LoadSpanningEnum

Set: Spanning(self: Load) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: Load) -> float

Set: Weight(self: Load) = value
"""


    LoadAttachmentEnum = None
    LoadPartNamesEnum = None
    LoadSpanningEnum = None


class LoadArea(Load):
    """ LoadArea() """
    def Delete(self):
        """ Delete(self: LoadArea) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadArea) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadArea) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadArea) -> bool """
        pass

    DistanceA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceA(self: LoadArea) -> float

Set: DistanceA(self: LoadArea) = value
"""

    LoadForm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadForm(self: LoadArea) -> AreaLoadFormEnum

Set: LoadForm(self: LoadArea) = value
"""

    P1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P1(self: LoadArea) -> Vector

Set: P1(self: LoadArea) = value
"""

    P2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P2(self: LoadArea) -> Vector

Set: P2(self: LoadArea) = value
"""

    P3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P3(self: LoadArea) -> Vector

Set: P3(self: LoadArea) = value
"""

    P4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P4(self: LoadArea) -> Vector

Set: P4(self: LoadArea) = value
"""

    Position1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position1(self: LoadArea) -> Point

Set: Position1(self: LoadArea) = value
"""

    Position2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position2(self: LoadArea) -> Point

Set: Position2(self: LoadArea) = value
"""

    Position3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position3(self: LoadArea) -> Point

Set: Position3(self: LoadArea) = value
"""


    AreaLoadFormEnum = None


class LoadGroup(ModelObject):
    """ LoadGroup() """
    def Delete(self):
        """ Delete(self: LoadGroup) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadGroup) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadGroup) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadGroup) -> bool """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: LoadGroup) -> Colors

Set: Color(self: LoadGroup) = value
"""

    Compatible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Compatible(self: LoadGroup) -> int

Set: Compatible(self: LoadGroup) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LoadGroup) -> LoadGroupDirection

Set: Direction(self: LoadGroup) = value
"""

    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupName(self: LoadGroup) -> str

Set: GroupName(self: LoadGroup) = value
"""

    GroupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupType(self: LoadGroup) -> LoadGroupType

Set: GroupType(self: LoadGroup) = value
"""

    Incompatible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Incompatible(self: LoadGroup) -> int

Set: Incompatible(self: LoadGroup) = value
"""


    Colors = None
    LoadGroupDirection = None
    LoadGroupType = None


class LoadLine(Load):
    """ LoadLine() """
    def Delete(self):
        """ Delete(self: LoadLine) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadLine) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadLine) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadLine) -> bool """
        pass

    DistanceA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceA(self: LoadLine) -> float

Set: DistanceA(self: LoadLine) = value
"""

    DistanceB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceB(self: LoadLine) -> float

Set: DistanceB(self: LoadLine) = value
"""

    LoadForm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadForm(self: LoadLine) -> LineLoadFormEnum

Set: LoadForm(self: LoadLine) = value
"""

    P1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P1(self: LoadLine) -> Vector

Set: P1(self: LoadLine) = value
"""

    P2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P2(self: LoadLine) -> Vector

Set: P2(self: LoadLine) = value
"""

    Position1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position1(self: LoadLine) -> Point

Set: Position1(self: LoadLine) = value
"""

    Position2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position2(self: LoadLine) -> Point

Set: Position2(self: LoadLine) = value
"""

    Torsion1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Torsion1(self: LoadLine) -> float

Set: Torsion1(self: LoadLine) = value
"""

    Torsion2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Torsion2(self: LoadLine) -> float

Set: Torsion2(self: LoadLine) = value
"""


    LineLoadFormEnum = None


class LoadPoint(Load):
    """ LoadPoint() """
    def Delete(self):
        """ Delete(self: LoadPoint) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadPoint) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadPoint) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadPoint) -> bool """
        pass

    Moment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Moment(self: LoadPoint) -> Vector

Set: Moment(self: LoadPoint) = value
"""

    P = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P(self: LoadPoint) -> Vector

Set: P(self: LoadPoint) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: LoadPoint) -> Point

Set: Position(self: LoadPoint) = value
"""



class LoadTemperature(Load):
    """ LoadTemperature() """
    def Delete(self):
        """ Delete(self: LoadTemperature) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadTemperature) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadTemperature) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadTemperature) -> bool """
        pass

    AutomaticPrimaryAxisWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticPrimaryAxisWeight(self: LoadTemperature) -> bool

Set: AutomaticPrimaryAxisWeight(self: LoadTemperature) = value
"""

    CreateFixedSupportConditionsAutomatically = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateFixedSupportConditionsAutomatically(self: LoadTemperature) -> bool

Set: CreateFixedSupportConditionsAutomatically(self: LoadTemperature) = value
"""

    InitialAxialElongation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialAxialElongation(self: LoadTemperature) -> float

Set: InitialAxialElongation(self: LoadTemperature) = value
"""

    LoadDispersionAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadDispersionAngle(self: LoadTemperature) -> float

Set: LoadDispersionAngle(self: LoadTemperature) = value
"""

    Position1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position1(self: LoadTemperature) -> Point

Set: Position1(self: LoadTemperature) = value
"""

    Position2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position2(self: LoadTemperature) -> Point

Set: Position2(self: LoadTemperature) = value
"""

    PrimaryAxisDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryAxisDirection(self: LoadTemperature) -> Vector

Set: PrimaryAxisDirection(self: LoadTemperature) = value
"""

    Spanning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spanning(self: LoadTemperature) -> LoadSpanningEnum

Set: Spanning(self: LoadTemperature) = value
"""

    TemperatureChangeForAxialElongation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureChangeForAxialElongation(self: LoadTemperature) -> float

Set: TemperatureChangeForAxialElongation(self: LoadTemperature) = value
"""

    TemperatureDifferentialSideToSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureDifferentialSideToSide(self: LoadTemperature) -> float

Set: TemperatureDifferentialSideToSide(self: LoadTemperature) = value
"""

    TemperatureDifferentialTopToBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureDifferentialTopToBottom(self: LoadTemperature) -> float

Set: TemperatureDifferentialTopToBottom(self: LoadTemperature) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: LoadTemperature) -> float

Set: Weight(self: LoadTemperature) = value
"""



class LoadUniform(Load):
    """ LoadUniform() """
    def Delete(self):
        """ Delete(self: LoadUniform) -> bool """
        pass

    def Insert(self):
        """ Insert(self: LoadUniform) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LoadUniform) -> bool """
        pass

    def Select(self):
        """ Select(self: LoadUniform) -> bool """
        pass

    DistanceA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceA(self: LoadUniform) -> float

Set: DistanceA(self: LoadUniform) = value
"""

    P1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P1(self: LoadUniform) -> Vector

Set: P1(self: LoadUniform) = value
"""

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: LoadUniform) -> Polygon

Set: Polygon(self: LoadUniform) = value
"""



class LogicalWeld(BaseWeld):
    """ LogicalWeld(MainWeld: BaseWeld) """
    def AddWeld(self, Weld):
        """ AddWeld(self: LogicalWeld, Weld: BaseWeld) -> bool """
        pass

    def Delete(self):
        """ Delete(self: LogicalWeld) -> bool """
        pass

    def Explode(self):
        """ Explode(self: LogicalWeld) -> bool """
        pass

    def GetMainWeld(self):
        """ GetMainWeld(self: LogicalWeld) -> BaseWeld """
        pass

    def Insert(self):
        """ Insert(self: LogicalWeld) -> bool """
        pass

    def Modify(self):
        """ Modify(self: LogicalWeld) -> bool """
        pass

    def RemoveWeld(self, Weld):
        """ RemoveWeld(self: LogicalWeld, Weld: BaseWeld) -> bool """
        pass

    def Select(self, ChildWeld=None):
        """
        Select(self: LogicalWeld, ChildWeld: BaseWeld) -> bool
        Select(self: LogicalWeld) -> bool
        """
        pass

    def SetMainWeld(self, Weld):
        """ SetMainWeld(self: LogicalWeld, Weld: BaseWeld) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, MainWeld):
        """ __new__(cls: type, MainWeld: BaseWeld) """
        pass


class Material(object):
    """ Material() """
    MaterialString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialString(self: Material) -> str

Set: MaterialString(self: Material) = value
"""



class Model(object):
    """ Model() """
    def CommitChanges(self, Message=None):
        """
        CommitChanges(self: Model, Message: str) -> bool
        CommitChanges(self: Model) -> bool
        """
        pass

    def GetClashCheckHandler(self):
        """ GetClashCheckHandler(self: Model) -> ClashCheckHandler """
        pass

    def GetConnectionStatus(self):
        """ GetConnectionStatus(self: Model) -> bool """
        pass

    def GetGUIDByIdentifier(self, identifier):
        """ GetGUIDByIdentifier(self: Model, identifier: Identifier) -> str """
        pass

    def GetIdentifierByGUID(self, guid):
        """ GetIdentifierByGUID(self: Model, guid: str) -> Identifier """
        pass

    def GetInfo(self):
        """ GetInfo(self: Model) -> ModelInfo """
        pass

    def GetModelObjectSelector(self):
        """ GetModelObjectSelector(self: Model) -> ModelObjectSelector """
        pass

    def GetPhases(self):
        """ GetPhases(self: Model) -> PhaseCollection """
        pass

    def GetProjectInfo(self):
        """ GetProjectInfo(self: Model) -> ProjectInfo """
        pass

    def GetWorkPlaneHandler(self):
        """ GetWorkPlaneHandler(self: Model) -> WorkPlaneHandler """
        pass

    def SelectModelObject(self, ID):
        """ SelectModelObject(self: Model, ID: Identifier) -> ModelObject """
        pass


class ModelHandler(object):
    """ ModelHandler() """
    def Close(self):
        """ Close(self: ModelHandler) """
        pass

    def CreateNewMultiUserModel(self, ModelName, ModelFolder, ServerName):
        """ CreateNewMultiUserModel(self: ModelHandler, ModelName: str, ModelFolder: str, ServerName: str) -> bool """
        pass

    def CreateNewSingleUserModel(self, ModelName, ModelFolder, Template):
        """ CreateNewSingleUserModel(self: ModelHandler, ModelName: str, ModelFolder: str, Template: str) -> bool """
        pass

    def IsModelAutoSaved(self, ModelFolder):
        """ IsModelAutoSaved(self: ModelHandler, ModelFolder: str) -> bool """
        pass

    def IsModelSaved(self):
        """ IsModelSaved(self: ModelHandler) -> bool """
        pass

    def Open(self, ModelFolder, OpenAutoSaved):
        """ Open(self: ModelHandler, ModelFolder: str, OpenAutoSaved: bool) -> bool """
        pass

    def Save(self, Comment, User):
        """ Save(self: ModelHandler, Comment: str, User: str) -> bool """
        pass


class ModelInfo(object):
    # no doc
    CurrentPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPhase(self: ModelInfo) -> int

Set: CurrentPhase(self: ModelInfo) = value
"""

    ModelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelName(self: ModelInfo) -> str

Set: ModelName(self: ModelInfo) = value
"""

    ModelPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelPath(self: ModelInfo) -> str

Set: ModelPath(self: ModelInfo) = value
"""

    NorthDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NorthDirection(self: ModelInfo) -> float

Set: NorthDirection(self: ModelInfo) = value
"""

    SharedModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SharedModel(self: ModelInfo) -> bool

"""

    SingleUserModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleUserModel(self: ModelInfo) -> bool

"""



class ModelObjectEnumerator(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ModelObjectEnumerator) -> IEnumerator """
        pass

    def GetSize(self):
        """ GetSize(self: ModelObjectEnumerator) -> int """
        pass

    def MoveNext(self):
        """ MoveNext(self: ModelObjectEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: ModelObjectEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ModelObjectEnumerator) -> ModelObject

"""

    SelectInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectInstances(self: ModelObjectEnumerator) -> bool

Set: SelectInstances(self: ModelObjectEnumerator) = value
"""


    AutoFetch = False
    EnumeratorTypeEnum = None


class ModelObjectSelector(object):
    # no doc
    def GetAllObjects(self):
        """ GetAllObjects(self: ModelObjectSelector) -> ModelObjectEnumerator """
        pass

    def GetAllObjectsWithType(self, *__args):
        """
        GetAllObjectsWithType(self: ModelObjectSelector, TypeFilter: Array[Type]) -> ModelObjectEnumerator
        GetAllObjectsWithType(self: ModelObjectSelector, Enum: ModelObjectEnum) -> ModelObjectEnumerator
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ModelObjectSelector) -> ModelObjectEnumerator """
        pass

    def GetFilteredObjectsWithType(self, Enum, FilterName):
        """ GetFilteredObjectsWithType(self: ModelObjectSelector, Enum: ModelObjectEnum, FilterName: str) -> ModelObjectEnumerator """
        pass

    def GetObjectsByBoundingBox(self, MinPoint, MaxPoint):
        """ GetObjectsByBoundingBox(self: ModelObjectSelector, MinPoint: Point, MaxPoint: Point) -> ModelObjectEnumerator """
        pass

    def GetObjectsByFilter(self, FilterExpression):
        """ GetObjectsByFilter(self: ModelObjectSelector, FilterExpression: FilterExpression) -> ModelObjectEnumerator """
        pass

    def GetObjectsByFilterName(self, FilterName):
        """ GetObjectsByFilterName(self: ModelObjectSelector, FilterName: str) -> ModelObjectEnumerator """
        pass


class NumberingSeries(object):
    """
    NumberingSeries()
    NumberingSeries(Prefix: str, Number: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Prefix=None, Number=None):
        """
        __new__(cls: type)
        __new__(cls: type, Prefix: str, Number: int)
        """
        pass

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: NumberingSeries) -> str

Set: Prefix(self: NumberingSeries) = value
"""

    StartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartNumber(self: NumberingSeries) -> int

Set: StartNumber(self: NumberingSeries) = value
"""



class NumberingSeriesNullable(object):
    """
    NumberingSeriesNullable()
    NumberingSeriesNullable(prefix: str, number: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, prefix=None, number=None):
        """
        __new__(cls: type)
        __new__(cls: type, prefix: str, number: int)
        """
        pass

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: NumberingSeriesNullable) -> str

Set: Prefix(self: NumberingSeriesNullable) = value
"""

    StartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartNumber(self: NumberingSeriesNullable) -> Nullable[int]

Set: StartNumber(self: NumberingSeriesNullable) = value
"""



class Offset(object):
    """ Offset() """
    Dx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dx(self: Offset) -> float

Set: Dx(self: Offset) = value
"""

    Dy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dy(self: Offset) -> float

Set: Dy(self: Offset) = value
"""

    Dz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dz(self: Offset) -> float

Set: Dz(self: Offset) = value
"""



class Phase(object):
    """
    Phase()
    Phase(PhaseNumber: int)
    Phase(PhaseNumber: int, PhaseName: str, PhaseComment: str, IsCurrentPhase: int)
    """
    def Delete(self):
        """ Delete(self: Phase) -> bool """
        pass

    def GetUserProperty(self, Name, Value):
        """
        GetUserProperty(self: Phase, Name: str, Value: int) -> (bool, int)
        GetUserProperty(self: Phase, Name: str, Value: float) -> (bool, float)
        GetUserProperty(self: Phase, Name: str, Value: str) -> (bool, str)
        """
        pass

    def Insert(self):
        """ Insert(self: Phase) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Phase) -> bool """
        pass

    def Select(self):
        """ Select(self: Phase) -> bool """
        pass

    def SetUserProperty(self, Name, Value):
        """
        SetUserProperty(self: Phase, Name: str, Value: int) -> bool
        SetUserProperty(self: Phase, Name: str, Value: float) -> bool
        SetUserProperty(self: Phase, Name: str, Value: str) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, PhaseNumber=None, PhaseName=None, PhaseComment=None, IsCurrentPhase=None):
        """
        __new__(cls: type)
        __new__(cls: type, PhaseNumber: int)
        __new__(cls: type, PhaseNumber: int, PhaseName: str, PhaseComment: str, IsCurrentPhase: int)
        """
        pass

    IsCurrentPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCurrentPhase(self: Phase) -> int

Set: IsCurrentPhase(self: Phase) = value
"""

    PhaseComment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseComment(self: Phase) -> str

Set: PhaseComment(self: Phase) = value
"""

    PhaseName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseName(self: Phase) -> str

Set: PhaseName(self: Phase) = value
"""

    PhaseNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseNumber(self: Phase) -> int

Set: PhaseNumber(self: Phase) = value
"""



class PhaseCollection(object):
    # no doc
    def CopyTo(self, Array, Index):
        """ CopyTo(self: PhaseCollection, Array: Array, Index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PhaseCollection) -> IEnumerator """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PhaseCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: PhaseCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: PhaseCollection) -> object

"""



class Plane(object):
    """ Plane() """
    AxisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisX(self: Plane) -> Vector

Set: AxisX(self: Plane) = value
"""

    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: Plane) -> Vector

Set: AxisY(self: Plane) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Plane) -> Point

Set: Origin(self: Plane) = value
"""



class PlateIntersectsWithIntersectionLineException(ConnectiveGeometryException):
    """ PlateIntersectsWithIntersectionLineException() """

class PolyBeam(Part):
    """
    PolyBeam()
    PolyBeam(polyBeamType: PolyBeamTypeEnum)
    """
    def AddContourPoint(self, contourPoint):
        """ AddContourPoint(self: PolyBeam, contourPoint: ContourPoint) -> bool """
        pass

    def Delete(self):
        """ Delete(self: PolyBeam) -> bool """
        pass

    def GetPolybeamCoordinateSystems(self):
        """ GetPolybeamCoordinateSystems(self: PolyBeam) -> ArrayList """
        pass

    def Insert(self):
        """ Insert(self: PolyBeam) -> bool """
        pass

    def Modify(self):
        """ Modify(self: PolyBeam) -> bool """
        pass

    def Select(self):
        """ Select(self: PolyBeam) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, polyBeamType=None):
        """
        __new__(cls: type)
        __new__(cls: type, polyBeamType: PolyBeamTypeEnum)
        """
        pass

    Contour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contour(self: PolyBeam) -> Contour

Set: Contour(self: PolyBeam) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: PolyBeam) -> PolyBeamTypeEnum

"""


    PolyBeamTypeEnum = None


class Polygon(object):
    """ Polygon() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Polygon) -> ArrayList

Set: Points(self: Polygon) = value
"""


    MAX_POLYGON_POINTS = 99
    MIN_POLYGON_POINTS = 3


class PolygonNode(object):
    """ PolygonNode(contour: Contour, isAutomaticNode: bool) """
    def AcceptVisitor(self, visitor):
        """ AcceptVisitor(self: PolygonNode, visitor: IGeometryNodeVisitor) """
        pass

    def Clone(self):
        """ Clone(self: PolygonNode) -> IGeometryNode """
        pass

    @staticmethod # known case of __new__
    def __new__(self, contour, isAutomaticNode):
        """ __new__(cls: type, contour: Contour, isAutomaticNode: bool) """
        pass

    Contour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contour(self: PolygonNode) -> Contour

"""

    IsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutomatic(self: PolygonNode) -> bool

"""



class PolygonWeld(BaseWeld):
    """ PolygonWeld() """
    def Delete(self):
        """ Delete(self: PolygonWeld) -> bool """
        pass

    def GetLogicalWeld(self, LogicalWeld):
        """ GetLogicalWeld(self: PolygonWeld, LogicalWeld: LogicalWeld) -> (bool, LogicalWeld) """
        pass

    def Insert(self):
        """ Insert(self: PolygonWeld) -> bool """
        pass

    def Modify(self):
        """ Modify(self: PolygonWeld) -> bool """
        pass

    def Select(self):
        """ Select(self: PolygonWeld) -> bool """
        pass

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: PolygonWeld) -> Polygon

Set: Polygon(self: PolygonWeld) = value
"""



class Polymesh(object):
    """ Polymesh() """
    @staticmethod
    def CompareFingerprints(fingerprint1, fingerprint2):
        """ CompareFingerprints(fingerprint1: str, fingerprint2: str) -> bool """
        pass

    @staticmethod
    def Convert(input):
        """ Convert(input: dotPolymesh_t) -> (List[FacetedBrep], dotPolymesh_t) """
        pass

    @staticmethod
    def ConvertInvalidInfoFromStruct(input):
        """ ConvertInvalidInfoFromStruct(input: dotPolymeshValidateInvalidInfo_t) -> (List[KeyValuePair[int, PolymeshHealthCheckEnum]], dotPolymeshValidateInvalidInfo_t) """
        pass

    @staticmethod
    def ConvertToStruct(brep, output):
        """ ConvertToStruct(brep: FacetedBrep, output: dotPolymesh_t) -> dotPolymesh_t """
        pass

    @staticmethod
    def Fingerprint(brep):
        """ Fingerprint(brep: FacetedBrep) -> str """
        pass

    def FromStruct(self, input):
        """ FromStruct(self: Polymesh, input: dotPolymesh_t) -> dotPolymesh_t """
        pass

    @staticmethod
    def GetSolidBrep(inBrep, outBrep):
        """ GetSolidBrep(inBrep: FacetedBrep) -> (bool, FacetedBrep) """
        pass

    def ToStruct(self, output):
        """ ToStruct(self: Polymesh, output: dotPolymesh_t) -> dotPolymesh_t """
        pass

    @staticmethod
    def Validate(brep, checkCriteria, invalidInfo):
        """ Validate(brep: FacetedBrep, checkCriteria: PolymeshCheckerFlags, invalidInfo: List[KeyValuePair[int, PolymeshHealthCheckEnum]]) -> (bool, List[KeyValuePair[int, PolymeshHealthCheckEnum]]) """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: Polymesh) -> FacetedBrep

Set: Brep(self: Polymesh) = value
"""


    PolymeshCheckerFlags = None
    PolymeshHealthCheckEnum = None


class PolymeshEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: PolymeshEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: PolymeshEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: PolymeshEnumerator) -> object

"""



class Position(object):
    """ Position() """
    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: Position) -> DepthEnum

Set: Depth(self: Position) = value
"""

    DepthOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthOffset(self: Position) -> float

Set: DepthOffset(self: Position) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Position) -> PlaneEnum

Set: Plane(self: Position) = value
"""

    PlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneOffset(self: Position) -> float

Set: PlaneOffset(self: Position) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: Position) -> RotationEnum

Set: Rotation(self: Position) = value
"""

    RotationOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationOffset(self: Position) -> float

Set: RotationOffset(self: Position) = value
"""


    DepthEnum = None
    PlaneEnum = None
    RotationEnum = None


class PourBreak(ModelObject):
    """ PourBreak() """
    def CreateInstanceDelegate(self, *args): #cannot find CLR method
        """ CreateInstanceDelegate(self: PourBreak, pourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def Delete(self):
        """ Delete(self: PourBreak) -> bool """
        pass

    def Insert(self):
        """ Insert(self: PourBreak) -> bool """
        pass

    def Modify(self):
        """ Modify(self: PourBreak) -> bool """
        pass

    def ModifyInstanceDelegate(self, *args): #cannot find CLR method
        """ ModifyInstanceDelegate(self: PourBreak, pourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def Select(self):
        """ Select(self: PourBreak) -> bool """
        pass

    def SelectInstanceDelegate(self, *args): #cannot find CLR method
        """ SelectInstanceDelegate(self: PourBreak, pourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    ModelObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Polymesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polymesh(self: PourBreak) -> FacetedBrep

Set: Polymesh(self: PourBreak) = value
"""



class PourObject(ModelObject):
    """ PourObject() """
    def Delete(self):
        """ Delete(self: PourObject) -> bool """
        pass

    def GetAssembly(self):
        """ GetAssembly(self: PourObject) -> Assembly """
        pass

    def GetObjects(self):
        """ GetObjects(self: PourObject) -> ModelObjectEnumerator """
        pass

    def GetParts(self):
        """ GetParts(self: PourObject) -> ModelObjectEnumerator """
        pass

    def GetPourPolymeshes(self):
        """ GetPourPolymeshes(self: PourObject) -> PolymeshEnumerator """
        pass

    def GetSolid(self):
        """ GetSolid(self: PourObject) -> Solid """
        pass

    def GetSurfaceObjects(self):
        """ GetSurfaceObjects(self: PourObject) -> ModelObjectEnumerator """
        pass

    def Insert(self):
        """ Insert(self: PourObject) -> bool """
        pass

    def Modify(self):
        """ Modify(self: PourObject) -> bool """
        pass

    def Select(self):
        """ Select(self: PourObject) -> bool """
        pass

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: PourObject) -> int

Set: Class(self: PourObject) = value
"""

    ConcreteMixture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteMixture(self: PourObject) -> str

Set: ConcreteMixture(self: PourObject) = value
"""

    PourNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PourNumber(self: PourObject) -> str

Set: PourNumber(self: PourObject) = value
"""

    PourType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PourType(self: PourObject) -> str

Set: PourType(self: PourObject) = value
"""



class Profile(object):
    """ Profile() """
    @staticmethod
    def FormatProfileString(profileString):
        """ FormatProfileString(profileString: str) -> str """
        pass

    @staticmethod
    def ParseProfileString(profileString):
        """ ParseProfileString(profileString: str) -> str """
        pass

    ProfileString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileString(self: Profile) -> str

Set: ProfileString(self: Profile) = value
"""



class ProjectInfo(object):
    # no doc
    def GetDoubleUserProperties(self, Values):
        """ GetDoubleUserProperties(self: ProjectInfo, Values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetIntegerUserProperties(self, Values):
        """ GetIntegerUserProperties(self: ProjectInfo, Values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetStringUserProperties(self, Values):
        """ GetStringUserProperties(self: ProjectInfo, Values: Hashtable) -> (bool, Hashtable) """
        pass

    def GetUserProperty(self, Name, Value):
        """
        GetUserProperty(self: ProjectInfo, Name: str, Value: float) -> (bool, float)
        GetUserProperty(self: ProjectInfo, Name: str, Value: int) -> (bool, int)
        GetUserProperty(self: ProjectInfo, Name: str, Value: str) -> (bool, str)
        """
        pass

    def Modify(self):
        """ Modify(self: ProjectInfo) -> bool """
        pass

    def SetUserProperty(self, Name, Value):
        """
        SetUserProperty(self: ProjectInfo, Name: str, Value: int) -> bool
        SetUserProperty(self: ProjectInfo, Name: str, Value: float) -> bool
        SetUserProperty(self: ProjectInfo, Name: str, Value: str) -> bool
        """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ProjectInfo) -> str

Set: Address(self: ProjectInfo) = value
"""

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ProjectInfo) -> str

Set: Builder(self: ProjectInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ProjectInfo) -> str

Set: Description(self: ProjectInfo) = value
"""

    Designer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Designer(self: ProjectInfo) -> str

Set: Designer(self: ProjectInfo) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: ProjectInfo) -> str

Set: EndDate(self: ProjectInfo) = value
"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: ProjectInfo) -> str

Set: GUID(self: ProjectInfo) = value
"""

    Info1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Info1(self: ProjectInfo) -> str

Set: Info1(self: ProjectInfo) = value
"""

    Info2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Info2(self: ProjectInfo) -> str

Set: Info2(self: ProjectInfo) = value
"""

    ModelSharingLocalPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSharingLocalPath(self: ProjectInfo) -> DirectoryInfo

Set: ModelSharingLocalPath(self: ProjectInfo) = value
"""

    ModelSharingServerPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSharingServerPath(self: ProjectInfo) -> Uri

Set: ModelSharingServerPath(self: ProjectInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ProjectInfo) -> str

Set: Name(self: ProjectInfo) = value
"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ProjectInfo) -> str

Set: Object(self: ProjectInfo) = value
"""

    ProjectNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectNumber(self: ProjectInfo) -> str

Set: ProjectNumber(self: ProjectInfo) = value
"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDate(self: ProjectInfo) -> str

Set: StartDate(self: ProjectInfo) = value
"""



class RebarEndDetailModifier(BaseRebarModifier):
    """ RebarEndDetailModifier() """
    RebarHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarHook(self: RebarEndDetailModifier) -> RebarHookDataNullable

Set: RebarHook(self: RebarEndDetailModifier) = value
"""

    RebarThreading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarThreading(self: RebarEndDetailModifier) -> RebarThreadingDataNullable

Set: RebarThreading(self: RebarEndDetailModifier) = value
"""



class RebarGeometry(object):
    # no doc
    BendingRadiuses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BendingRadiuses(self: RebarGeometry) -> ArrayList

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: RebarGeometry) -> float

"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shape(self: RebarGeometry) -> PolyLine

"""



class RebarGroup(BaseRebarGroup):
    """ RebarGroup() """
    def Delete(self):
        """ Delete(self: RebarGroup) -> bool """
        pass

    def Insert(self):
        """ Insert(self: RebarGroup) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarGroup) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarGroup) -> bool """
        pass

    Polygons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygons(self: RebarGroup) -> ArrayList

Set: Polygons(self: RebarGroup) = value
"""

    StirrupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StirrupType(self: RebarGroup) -> RebarGroupStirrupTypeEnum

Set: StirrupType(self: RebarGroup) = value
"""


    RebarGroupStirrupTypeEnum = None


class RebarGuideline(object):
    """ RebarGuideline() """
    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: RebarGuideline) -> Contour

Set: Curve(self: RebarGuideline) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: RebarGuideline) -> int

Set: Id(self: RebarGuideline) = value
"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacing(self: RebarGuideline) -> RebarSpacing

Set: Spacing(self: RebarGuideline) = value
"""



class RebarHookData(object):
    """ RebarHookData() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: RebarHookData) -> float

Set: Angle(self: RebarHookData) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarHookData) -> float

Set: Length(self: RebarHookData) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: RebarHookData) -> float

Set: Radius(self: RebarHookData) = value
"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shape(self: RebarHookData) -> RebarHookShapeEnum

Set: Shape(self: RebarHookData) = value
"""


    RebarHookShapeEnum = None


class RebarHookDataNullable(object):
    """ RebarHookDataNullable() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: RebarHookDataNullable) -> Nullable[float]

Set: Angle(self: RebarHookDataNullable) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarHookDataNullable) -> Nullable[float]

Set: Length(self: RebarHookDataNullable) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: RebarHookDataNullable) -> Nullable[float]

Set: Radius(self: RebarHookDataNullable) = value
"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shape(self: RebarHookDataNullable) -> Nullable[RebarHookShapeEnum]

Set: Shape(self: RebarHookDataNullable) = value
"""



class RebarLegFace(object):
    """
    RebarLegFace()
    RebarLegFace(contour: Contour)
    """
    @staticmethod # known case of __new__
    def __new__(self, contour=None):
        """
        __new__(cls: type)
        __new__(cls: type, contour: Contour)
        """
        pass

    AdditonalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditonalOffset(self: RebarLegFace) -> float

Set: AdditonalOffset(self: RebarLegFace) = value
"""

    Contour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contour(self: RebarLegFace) -> Contour

Set: Contour(self: RebarLegFace) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: RebarLegFace) -> int

Set: Id(self: RebarLegFace) = value
"""

    LayerOrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerOrderNumber(self: RebarLegFace) -> int

Set: LayerOrderNumber(self: RebarLegFace) = value
"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: RebarLegFace) -> bool

Set: Reversed(self: RebarLegFace) = value
"""



class RebarMesh(Reinforcement):
    """ RebarMesh() """
    def Delete(self):
        """ Delete(self: RebarMesh) -> bool """
        pass

    def Insert(self):
        """ Insert(self: RebarMesh) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarMesh) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarMesh) -> bool """
        pass

    CatalogName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CatalogName(self: RebarMesh) -> str

Set: CatalogName(self: RebarMesh) = value
"""

    CrossBarLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossBarLocation(self: RebarMesh) -> RebarMeshCrossBarLocationEnum

Set: CrossBarLocation(self: RebarMesh) = value
"""

    CrossDistances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossDistances(self: RebarMesh) -> ArrayList

Set: CrossDistances(self: RebarMesh) = value
"""

    CrossSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSize(self: RebarMesh) -> str

Set: CrossSize(self: RebarMesh) = value
"""

    CutByFatherPartCuts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutByFatherPartCuts(self: RebarMesh) -> bool

Set: CutByFatherPartCuts(self: RebarMesh) = value
"""

    EndFromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFromPlaneOffset(self: RebarMesh) -> float

Set: EndFromPlaneOffset(self: RebarMesh) = value
"""

    EndHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndHook(self: RebarMesh) -> RebarHookData

Set: EndHook(self: RebarMesh) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: RebarMesh) -> Point

Set: EndPoint(self: RebarMesh) = value
"""

    FromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromPlaneOffset(self: RebarMesh) -> float

Set: FromPlaneOffset(self: RebarMesh) = value
"""

    LeftOverhangCross = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOverhangCross(self: RebarMesh) -> float

Set: LeftOverhangCross(self: RebarMesh) = value
"""

    LeftOverhangLongitudinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOverhangLongitudinal(self: RebarMesh) -> float

Set: LeftOverhangLongitudinal(self: RebarMesh) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarMesh) -> float

Set: Length(self: RebarMesh) = value
"""

    LongitudinalDistances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongitudinalDistances(self: RebarMesh) -> ArrayList

Set: LongitudinalDistances(self: RebarMesh) = value
"""

    LongitudinalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongitudinalSize(self: RebarMesh) -> str

Set: LongitudinalSize(self: RebarMesh) = value
"""

    LongitudinalSpacingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongitudinalSpacingMethod(self: RebarMesh) -> RebarMeshSpacingMethodEnum

Set: LongitudinalSpacingMethod(self: RebarMesh) = value
"""

    MeshType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshType(self: RebarMesh) -> RebarMeshTypeEnum

Set: MeshType(self: RebarMesh) = value
"""

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: RebarMesh) -> Polygon

Set: Polygon(self: RebarMesh) = value
"""

    RightOverhangCross = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOverhangCross(self: RebarMesh) -> float

Set: RightOverhangCross(self: RebarMesh) = value
"""

    RightOverhangLongitudinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOverhangLongitudinal(self: RebarMesh) -> float

Set: RightOverhangLongitudinal(self: RebarMesh) = value
"""

    StartFromPlaneOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartFromPlaneOffset(self: RebarMesh) -> float

Set: StartFromPlaneOffset(self: RebarMesh) = value
"""

    StartHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartHook(self: RebarMesh) -> RebarHookData

Set: StartHook(self: RebarMesh) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: RebarMesh) -> Point

Set: StartPoint(self: RebarMesh) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: RebarMesh) -> float

Set: Width(self: RebarMesh) = value
"""


    RebarMeshCrossBarLocationEnum = None
    RebarMeshSpacingMethodEnum = None
    RebarMeshTypeEnum = None


class RebarProperties(object):
    """ RebarProperties() """
    BendingRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BendingRadius(self: RebarProperties) -> float

Set: BendingRadius(self: RebarProperties) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: RebarProperties) -> int

Set: Class(self: RebarProperties) = value
"""

    Grade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade(self: RebarProperties) -> str

Set: Grade(self: RebarProperties) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: RebarProperties) -> str

Set: Name(self: RebarProperties) = value
"""

    NumberingSeries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingSeries(self: RebarProperties) -> NumberingSeries

Set: NumberingSeries(self: RebarProperties) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: RebarProperties) -> str

Set: Size(self: RebarProperties) = value
"""



class RebarPropertiesNullable(object):
    """ RebarPropertiesNullable() """
    BendingRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BendingRadius(self: RebarPropertiesNullable) -> Nullable[float]

Set: BendingRadius(self: RebarPropertiesNullable) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: RebarPropertiesNullable) -> Nullable[int]

Set: Class(self: RebarPropertiesNullable) = value
"""

    Grade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade(self: RebarPropertiesNullable) -> str

Set: Grade(self: RebarPropertiesNullable) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: RebarPropertiesNullable) -> str

Set: Name(self: RebarPropertiesNullable) = value
"""

    NumberingSeries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingSeries(self: RebarPropertiesNullable) -> NumberingSeriesNullable

Set: NumberingSeries(self: RebarPropertiesNullable) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: RebarPropertiesNullable) -> str

Set: Size(self: RebarPropertiesNullable) = value
"""



class RebarPropertyModifier(BaseRebarModifier):
    """ RebarPropertyModifier() """
    RebarProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarProperties(self: RebarPropertyModifier) -> RebarPropertiesNullable

Set: RebarProperties(self: RebarPropertyModifier) = value
"""



class RebarSet(ModelObject):
    """ RebarSet() """
    def Delete(self):
        """ Delete(self: RebarSet) -> bool """
        pass

    def GetRebarModifiers(self):
        """ GetRebarModifiers(self: RebarSet) -> ModelObjectEnumerator """
        pass

    def GetRebarSetAdditions(self):
        """ GetRebarSetAdditions(self: RebarSet) -> ModelObjectEnumerator """
        pass

    def GetReinforcements(self):
        """ GetReinforcements(self: RebarSet) -> ModelObjectEnumerator """
        pass

    def Insert(self):
        """ Insert(self: RebarSet) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarSet) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarSet) -> bool """
        pass

    Guidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guidelines(self: RebarSet) -> List[RebarGuideline]

Set: Guidelines(self: RebarSet) = value
"""

    LayerOrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerOrderNumber(self: RebarSet) -> int

Set: LayerOrderNumber(self: RebarSet) = value
"""

    LegFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegFaces(self: RebarSet) -> List[RebarLegFace]

Set: LegFaces(self: RebarSet) = value
"""

    RebarProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarProperties(self: RebarSet) -> RebarProperties

Set: RebarProperties(self: RebarSet) = value
"""



class RebarSetAddition(ModelObject):
    """ RebarSetAddition() """
    def Delete(self):
        """ Delete(self: RebarSetAddition) -> bool """
        pass

    def Insert(self):
        """ Insert(self: RebarSetAddition) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarSetAddition) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarSetAddition) -> bool """
        pass

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: RebarSetAddition) -> RebarSet

Set: Father(self: RebarSetAddition) = value
"""

    LegFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegFaces(self: RebarSetAddition) -> List[RebarLegFace]

Set: LegFaces(self: RebarSetAddition) = value
"""



class RebarSpacing(object):
    """ RebarSpacing() """
    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: RebarSpacing) -> float

Set: EndOffset(self: RebarSpacing) = value
"""

    EndOffsetIsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffsetIsAutomatic(self: RebarSpacing) -> bool

Set: EndOffsetIsAutomatic(self: RebarSpacing) = value
"""

    EndOffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffsetType(self: RebarSpacing) -> OffsetEnum

Set: EndOffsetType(self: RebarSpacing) = value
"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: RebarSpacing) -> float

Set: StartOffset(self: RebarSpacing) = value
"""

    StartOffsetIsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffsetIsAutomatic(self: RebarSpacing) -> bool

Set: StartOffsetIsAutomatic(self: RebarSpacing) = value
"""

    StartOffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffsetType(self: RebarSpacing) -> OffsetEnum

Set: StartOffsetType(self: RebarSpacing) = value
"""

    Zones = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zones(self: RebarSpacing) -> List[RebarSpacingZone]

Set: Zones(self: RebarSpacing) = value
"""


    OffsetEnum = None


class RebarSpacingZone(object):
    """ RebarSpacingZone() """
    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarSpacingZone) -> float

Set: Length(self: RebarSpacingZone) = value
"""

    LengthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthType(self: RebarSpacingZone) -> LengthEnum

Set: LengthType(self: RebarSpacingZone) = value
"""

    NumberOfSpaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSpaces(self: RebarSpacingZone) -> int

Set: NumberOfSpaces(self: RebarSpacingZone) = value
"""

    NumberOfSpacesType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSpacesType(self: RebarSpacingZone) -> SpacingEnum

Set: NumberOfSpacesType(self: RebarSpacingZone) = value
"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacing(self: RebarSpacingZone) -> float

Set: Spacing(self: RebarSpacingZone) = value
"""

    SpacingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpacingType(self: RebarSpacingZone) -> SpacingEnum

Set: SpacingType(self: RebarSpacingZone) = value
"""


    LengthEnum = None
    SpacingEnum = None


class RebarSplice(ModelObject):
    """
    RebarSplice(InputRebar1: RebarGroup, InputRebar2: RebarGroup)
    RebarSplice()
    """
    def Delete(self):
        """ Delete(self: RebarSplice) -> bool """
        pass

    def Insert(self):
        """ Insert(self: RebarSplice) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarSplice) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarSplice) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, InputRebar1=None, InputRebar2=None):
        """
        __new__(cls: type, InputRebar1: RebarGroup, InputRebar2: RebarGroup)
        __new__(cls: type)
        """
        pass

    BarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarPositions(self: RebarSplice) -> RebarSpliceBarPositionsEnum

Set: BarPositions(self: RebarSplice) = value
"""

    Clearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Clearance(self: RebarSplice) -> float

Set: Clearance(self: RebarSplice) = value
"""

    LapLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LapLength(self: RebarSplice) -> float

Set: LapLength(self: RebarSplice) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: RebarSplice) -> float

Set: Offset(self: RebarSplice) = value
"""

    RebarGroup1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarGroup1(self: RebarSplice) -> Reinforcement

Set: RebarGroup1(self: RebarSplice) = value
"""

    RebarGroup2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarGroup2(self: RebarSplice) -> Reinforcement

Set: RebarGroup2(self: RebarSplice) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RebarSplice) -> RebarSpliceTypeEnum

Set: Type(self: RebarSplice) = value
"""


    RebarSpliceBarPositionsEnum = None
    RebarSpliceTypeEnum = None


class RebarSplitter(BaseRebarModifier):
    """ RebarSplitter() """
    BarsToSplit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarsToSplit(self: RebarSplitter) -> BarsToSplitEnum

Set: BarsToSplit(self: RebarSplitter) = value
"""

    LapLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LapLength(self: RebarSplitter) -> float

Set: LapLength(self: RebarSplitter) = value
"""

    LapPlacement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LapPlacement(self: RebarSplitter) -> LapPlacementEnum

Set: LapPlacement(self: RebarSplitter) = value
"""

    LapSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LapSide(self: RebarSplitter) -> LapSideEnum

Set: LapSide(self: RebarSplitter) = value
"""

    LapType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LapType(self: RebarSplitter) -> LapTypeEnum

Set: LapType(self: RebarSplitter) = value
"""

    SplitOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitOffset(self: RebarSplitter) -> float

Set: SplitOffset(self: RebarSplitter) = value
"""

    StaggerOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerOffset(self: RebarSplitter) -> float

Set: StaggerOffset(self: RebarSplitter) = value
"""

    StaggerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerType(self: RebarSplitter) -> StaggerTypeEnum

Set: StaggerType(self: RebarSplitter) = value
"""


    BarsToSplitEnum = None
    LapPlacementEnum = None
    LapSideEnum = None
    LapTypeEnum = None
    StaggerTypeEnum = None


class RebarStrand(Reinforcement):
    """ RebarStrand() """
    def Delete(self):
        """ Delete(self: RebarStrand) -> bool """
        pass

    def Insert(self):
        """ Insert(self: RebarStrand) -> bool """
        pass

    def Modify(self):
        """ Modify(self: RebarStrand) -> bool """
        pass

    def Select(self):
        """ Select(self: RebarStrand) -> bool """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: RebarStrand) -> Point

Set: EndPoint(self: RebarStrand) = value
"""

    OnPlaneOffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnPlaneOffsets(self: RebarStrand) -> ArrayList

"""

    Patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Patterns(self: RebarStrand) -> ArrayList

Set: Patterns(self: RebarStrand) = value
"""

    PullPerStrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PullPerStrand(self: RebarStrand) -> float

Set: PullPerStrand(self: RebarStrand) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: RebarStrand) -> str

Set: Size(self: RebarStrand) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: RebarStrand) -> Point

Set: StartPoint(self: RebarStrand) = value
"""

    Unbondings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unbondings(self: RebarStrand) -> ArrayList

Set: Unbondings(self: RebarStrand) = value
"""



class RebarThreadingDataNullable(object):
    """ RebarThreadingDataNullable() """
    ExtraFabricationLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtraFabricationLength(self: RebarThreadingDataNullable) -> Nullable[float]

Set: ExtraFabricationLength(self: RebarThreadingDataNullable) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarThreadingDataNullable) -> Nullable[float]

Set: Length(self: RebarThreadingDataNullable) = value
"""

    ThreadingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadingType(self: RebarThreadingDataNullable) -> str

Set: ThreadingType(self: RebarThreadingDataNullable) = value
"""



class ReferenceModel(ModelObject):
    """
    ReferenceModel()
    ReferenceModel(filename: str, position: Point, scale: float)
    """
    def Delete(self):
        """ Delete(self: ReferenceModel) -> bool """
        pass

    def GetChildren(self):
        """ GetChildren(self: ReferenceModel) -> ModelObjectEnumerator """
        pass

    def GetConvertedObjects(self):
        """ GetConvertedObjects(self: ReferenceModel) -> ModelObjectEnumerator """
        pass

    def GetCurrentRevision(self):
        """ GetCurrentRevision(self: ReferenceModel) -> Revision """
        pass

    def GetReferenceModelObjectByExternalGuid(self, externalGuid):
        """ GetReferenceModelObjectByExternalGuid(self: ReferenceModel, externalGuid: str) -> ReferenceModelObject """
        pass

    def GetRevisions(self):
        """ GetRevisions(self: ReferenceModel) -> List[Revision] """
        pass

    def Insert(self):
        """ Insert(self: ReferenceModel) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ReferenceModel) -> bool """
        pass

    def RefreshFile(self):
        """ RefreshFile(self: ReferenceModel) -> bool """
        pass

    def Select(self):
        """ Select(self: ReferenceModel) -> bool """
        pass

    def SetAsCurrentRevision(self, *__args):
        """
        SetAsCurrentRevision(self: ReferenceModel, modelId: int, revisionId: int) -> bool
        SetAsCurrentRevision(self: ReferenceModel, revision: Revision) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filename=None, position=None, scale=None):
        """
        __new__(cls: type)
        __new__(cls: type, filename: str, position: Point, scale: float)
        """
        pass

    ActiveFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveFilePath(self: ReferenceModel) -> str

"""

    BasePointGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePointGuid(self: ReferenceModel) -> Guid

Set: BasePointGuid(self: ReferenceModel) = value
"""

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: ReferenceModel) -> str

Set: Filename(self: ReferenceModel) = value
"""

    ModelGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelGUID(self: ReferenceModel) -> Guid

Set: ModelGUID(self: ReferenceModel) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ReferenceModel) -> Point

Set: Position(self: ReferenceModel) = value
"""

    ProjectGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectGUID(self: ReferenceModel) -> Guid

Set: ProjectGUID(self: ReferenceModel) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: ReferenceModel) -> float

Set: Rotation(self: ReferenceModel) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: ReferenceModel) -> float

Set: Scale(self: ReferenceModel) = value
"""

    VersionGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VersionGUID(self: ReferenceModel) -> Guid

Set: VersionGUID(self: ReferenceModel) = value
"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility(self: ReferenceModel) -> VisibilityEnum

Set: Visibility(self: ReferenceModel) = value
"""


    Revision = None
    VisibilityEnum = None


class ReferenceModelObject(ModelObject):
    """
    ReferenceModelObject(ReferenceModelId: int, ID: Identifier)
    ReferenceModelObject()
    """
    def Delete(self):
        """ Delete(self: ReferenceModelObject) -> bool """
        pass

    def GetFather(self):
        """ GetFather(self: ReferenceModelObject) -> ReferenceModelObject """
        pass

    def GetReferenceModel(self):
        """ GetReferenceModel(self: ReferenceModelObject) -> ReferenceModel """
        pass

    def Insert(self):
        """ Insert(self: ReferenceModelObject) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ReferenceModelObject) -> bool """
        pass

    def Select(self):
        """ Select(self: ReferenceModelObject) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ReferenceModelId=None, ID=None):
        """
        __new__(cls: type, ReferenceModelId: int, ID: Identifier)
        __new__(cls: type)
        """
        pass


class Seam(BaseComponent):
    """ Seam() """
    def Delete(self):
        """ Delete(self: Seam) -> bool """
        pass

    def GetInputPolygon(self):
        """ GetInputPolygon(self: Seam) -> Polygon """
        pass

    def GetPrimaryObject(self):
        """ GetPrimaryObject(self: Seam) -> ModelObject """
        pass

    def GetSecondaryObjects(self):
        """ GetSecondaryObjects(self: Seam) -> ArrayList """
        pass

    def GetStartAndEndPositions(self, StartPoint, EndPoint):
        """ GetStartAndEndPositions(self: Seam, StartPoint: Point, EndPoint: Point) -> (bool, Point, Point) """
        pass

    def Insert(self):
        """ Insert(self: Seam) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Seam) -> bool """
        pass

    def Select(self):
        """ Select(self: Seam) -> bool """
        pass

    def SetInputPolygon(self, InputPolygon):
        """ SetInputPolygon(self: Seam, InputPolygon: Polygon) -> bool """
        pass

    def SetInputPositions(self, StartPoint, EndPoint):
        """ SetInputPositions(self: Seam, StartPoint: Point, EndPoint: Point) -> bool """
        pass

    def SetPrimaryObject(self, M):
        """ SetPrimaryObject(self: Seam, M: ModelObject) -> bool """
        pass

    def SetSecondaryObject(self, M):
        """ SetSecondaryObject(self: Seam, M: ModelObject) -> bool """
        pass

    def SetSecondaryObjects(self, Secondaries):
        """ SetSecondaryObjects(self: Seam, Secondaries: ArrayList) -> bool """
        pass

    AutoDirectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoDirectionType(self: Seam) -> AutoDirectionTypeEnum

Set: AutoDirectionType(self: Seam) = value
"""

    AutoPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoPosition(self: Seam) -> bool

Set: AutoPosition(self: Seam) = value
"""

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: Seam) -> int

Set: Class(self: Seam) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Seam) -> str

Set: Code(self: Seam) = value
"""

    InputPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PrimaryObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SecondaryObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: Seam) -> ConnectionStatusEnum

"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: Seam) -> Vector

Set: UpVector(self: Seam) = value
"""



class SingleRebar(Reinforcement):
    """ SingleRebar() """
    def Delete(self):
        """ Delete(self: SingleRebar) -> bool """
        pass

    def GetRebarSet(self):
        """ GetRebarSet(self: SingleRebar) -> RebarSet """
        pass

    def Insert(self):
        """ Insert(self: SingleRebar) -> bool """
        pass

    def Modify(self):
        """ Modify(self: SingleRebar) -> bool """
        pass

    def Select(self):
        """ Select(self: SingleRebar) -> bool """
        pass

    EndHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndHook(self: SingleRebar) -> RebarHookData

Set: EndHook(self: SingleRebar) = value
"""

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: SingleRebar) -> Polygon

Set: Polygon(self: SingleRebar) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: SingleRebar) -> str

Set: Size(self: SingleRebar) = value
"""

    StartHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartHook(self: SingleRebar) -> RebarHookData

Set: StartHook(self: SingleRebar) = value
"""



class Solid(object):
    # no doc
    def GetAllIntersectionPoints(self, point1, point2, point3):
        """ GetAllIntersectionPoints(self: Solid, point1: Point, point2: Point, point3: Point) -> IEnumerator """
        pass

    def GetCutPart(self, CuttingPart):
        """ GetCutPart(self: Solid, CuttingPart: Solid) -> ShellEnumerator """
        pass

    def GetEdgeEnumerator(self):
        """ GetEdgeEnumerator(self: Solid) -> EdgeEnumerator """
        pass

    def GetFaceEnumerator(self):
        """ GetFaceEnumerator(self: Solid) -> FaceEnumerator """
        pass

    def Intersect(self, *__args):
        """
        Intersect(self: Solid, point1: Point, point2: Point, point3: Point) -> ArrayList
        Intersect(self: Solid, point1: Point, point2: Point) -> ArrayList
        Intersect(self: Solid, line: LineSegment) -> ArrayList
        """
        pass

    def IntersectAllFaces(self, point1, point2, point3):
        """ IntersectAllFaces(self: Solid, point1: Point, point2: Point, point3: Point) -> IEnumerator """
        pass

    MaximumPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumPoint(self: Solid) -> Point

"""

    MinimumPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumPoint(self: Solid) -> Point

"""


    SolidCreationTypeEnum = None


class StrandUnbondingData(object):
    """ StrandUnbondingData() """
    FromEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromEnd(self: StrandUnbondingData) -> float

Set: FromEnd(self: StrandUnbondingData) = value
"""

    FromStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromStart(self: StrandUnbondingData) -> float

Set: FromStart(self: StrandUnbondingData) = value
"""

    MiddleToEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleToEnd(self: StrandUnbondingData) -> float

Set: MiddleToEnd(self: StrandUnbondingData) = value
"""

    MiddleToStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleToStart(self: StrandUnbondingData) -> float

Set: MiddleToStart(self: StrandUnbondingData) = value
"""

    StrandIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StrandIndex(self: StrandUnbondingData) -> int

Set: StrandIndex(self: StrandUnbondingData) = value
"""



class SurfaceObject(ModelObject):
    """ SurfaceObject() """
    def CreateInstanceDelegate(self, *args): #cannot find CLR method
        """ CreateInstanceDelegate(self: SurfaceObject, surface: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def Delete(self):
        """ Delete(self: SurfaceObject) -> bool """
        pass

    def Insert(self):
        """ Insert(self: SurfaceObject) -> bool """
        pass

    def Modify(self):
        """ Modify(self: SurfaceObject) -> bool """
        pass

    def ModifyInstanceDelegate(self, *args): #cannot find CLR method
        """ ModifyInstanceDelegate(self: SurfaceObject, surface: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def Select(self):
        """ Select(self: SurfaceObject) -> bool """
        pass

    def SelectInstanceDelegate(self, *args): #cannot find CLR method
        """ SelectInstanceDelegate(self: SurfaceObject, surface: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: SurfaceObject) -> str

Set: Class(self: SurfaceObject) = value
"""

    CreateHoles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateHoles(self: SurfaceObject) -> bool

Set: CreateHoles(self: SurfaceObject) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: SurfaceObject) -> ModelObject

Set: Father(self: SurfaceObject) = value
"""

    ModelObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SurfaceObject) -> str

Set: Name(self: SurfaceObject) = value
"""

    Polymesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polymesh(self: SurfaceObject) -> FacetedBrep

Set: Polymesh(self: SurfaceObject) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SurfaceObject) -> str

Set: Type(self: SurfaceObject) = value
"""



class SurfaceTreatment(ModelObject):
    """ SurfaceTreatment() """
    def Delete(self):
        """ Delete(self: SurfaceTreatment) -> bool """
        pass

    def Insert(self):
        """ Insert(self: SurfaceTreatment) -> bool """
        pass

    def Modify(self):
        """ Modify(self: SurfaceTreatment) -> bool """
        pass

    def Select(self):
        """ Select(self: SurfaceTreatment) -> bool """
        pass

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: SurfaceTreatment) -> str

Set: Class(self: SurfaceTreatment) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: SurfaceTreatment) -> SurfaceColorEnum

Set: Color(self: SurfaceTreatment) = value
"""

    CutByFatherBooleans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutByFatherBooleans(self: SurfaceTreatment) -> bool

Set: CutByFatherBooleans(self: SurfaceTreatment) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: SurfaceTreatment) -> Point

Set: EndPoint(self: SurfaceTreatment) = value
"""

    Father = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Father(self: SurfaceTreatment) -> Part

Set: Father(self: SurfaceTreatment) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: SurfaceTreatment) -> Material

Set: Material(self: SurfaceTreatment) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SurfaceTreatment) -> str

Set: Name(self: SurfaceTreatment) = value
"""

    Polygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygon(self: SurfaceTreatment) -> Contour

Set: Polygon(self: SurfaceTreatment) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: SurfaceTreatment) -> Position

Set: Position(self: SurfaceTreatment) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: SurfaceTreatment) -> Point

Set: StartPoint(self: SurfaceTreatment) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: SurfaceTreatment) -> float

Set: Thickness(self: SurfaceTreatment) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SurfaceTreatment) -> SurfaceTypeEnum

Set: Type(self: SurfaceTreatment) = value
"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: SurfaceTreatment) -> str

Set: TypeName(self: SurfaceTreatment) = value
"""


    SurfaceColorEnum = None
    SurfaceTypeEnum = None


class Task(ModelObject):
    """
    Task()
    Task(ID: Identifier)
    """
    def AddObjectsToTask(self, ModelObjects):
        """ AddObjectsToTask(self: Task, ModelObjects: ArrayList) -> bool """
        pass

    def Delete(self):
        """ Delete(self: Task) -> bool """
        pass

    @staticmethod
    def GetAllTasksOfSelectedObjects():
        """ GetAllTasksOfSelectedObjects() -> ModelObjectEnumerator """
        pass

    def GetDependencies(self):
        """ GetDependencies(self: Task) -> ModelObjectEnumerator """
        pass

    def GetFathers(self):
        """ GetFathers(self: Task) -> ModelObjectEnumerator """
        pass

    def Insert(self):
        """ Insert(self: Task) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Task) -> bool """
        pass

    def RemoveObjectsFromTask(self, ModelObjects):
        """ RemoveObjectsFromTask(self: Task, ModelObjects: ArrayList) -> bool """
        pass

    def Select(self):
        """ Select(self: Task) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ID=None):
        """
        __new__(cls: type)
        __new__(cls: type, ID: Identifier)
        """
        pass

    ActualEndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualEndDate(self: Task) -> DateTime

Set: ActualEndDate(self: Task) = value
"""

    ActualStartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualStartDate(self: Task) -> DateTime

Set: ActualStartDate(self: Task) = value
"""

    ActualWorkAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualWorkAmount(self: Task) -> float

Set: ActualWorkAmount(self: Task) = value
"""

    Completeness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Completeness(self: Task) -> int

Set: Completeness(self: Task) = value
"""

    Critical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Critical(self: Task) -> bool

Set: Critical(self: Task) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Task) -> str

Set: Description(self: Task) = value
"""

    Local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Local(self: Task) -> bool

Set: Local(self: Task) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Task) -> str

Set: Name(self: Task) = value
"""

    PlannedEndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlannedEndDate(self: Task) -> DateTime

Set: PlannedEndDate(self: Task) = value
"""

    PlannedStartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlannedStartDate(self: Task) -> DateTime

Set: PlannedStartDate(self: Task) = value
"""

    PlannedWorkAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlannedWorkAmount(self: Task) -> float

Set: PlannedWorkAmount(self: Task) = value
"""

    Scenario = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scenario(self: Task) -> HierarchicObject

Set: Scenario(self: Task) = value
"""

    Url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Url(self: Task) -> str

Set: Url(self: Task) = value
"""



class TaskDependency(ModelObject):
    """
    TaskDependency()
    TaskDependency(primary: Task, secondary: Task)
    """
    def Delete(self):
        """ Delete(self: TaskDependency) -> bool """
        pass

    def Insert(self):
        """ Insert(self: TaskDependency) -> bool """
        pass

    def Modify(self):
        """ Modify(self: TaskDependency) -> bool """
        pass

    def Select(self):
        """ Select(self: TaskDependency) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, primary=None, secondary=None):
        """
        __new__(cls: type)
        __new__(cls: type, primary: Task, secondary: Task)
        """
        pass

    DependencyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DependencyType(self: TaskDependency) -> DependencyTypeEnum

Set: DependencyType(self: TaskDependency) = value
"""

    Lag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lag(self: TaskDependency) -> int

Set: Lag(self: TaskDependency) = value
"""

    Local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Local(self: TaskDependency) -> bool

Set: Local(self: TaskDependency) = value
"""

    Primary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Primary(self: TaskDependency) -> Task

Set: Primary(self: TaskDependency) = value
"""

    Secondary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Secondary(self: TaskDependency) -> Task

Set: Secondary(self: TaskDependency) = value
"""


    DependencyTypeEnum = None


class TaskWorktype(ModelObject):
    """ TaskWorktype() """
    def Delete(self):
        """ Delete(self: TaskWorktype) -> bool """
        pass

    def Insert(self):
        """ Insert(self: TaskWorktype) -> bool """
        pass

    def Modify(self):
        """ Modify(self: TaskWorktype) -> bool """
        pass

    def Select(self):
        """ Select(self: TaskWorktype) -> bool """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: TaskWorktype) -> str

Set: Name(self: TaskWorktype) = value
"""



class TransformationPlane(object):
    """
    TransformationPlane()
    TransformationPlane(CoordinateSystem: CoordinateSystem)
    TransformationPlane(Origo: Point, Xvector: Vector, Yvector: Vector)
    """
    def ToString(self):
        """ ToString(self: TransformationPlane) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, CoordinateSystem: CoordinateSystem)
        __new__(cls: type, Origo: Point, Xvector: Vector, Yvector: Vector)
        """
        pass

    TransformationMatrixToGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformationMatrixToGlobal(self: TransformationPlane) -> Matrix

"""

    TransformationMatrixToLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformationMatrixToLocal(self: TransformationPlane) -> Matrix

"""



class UndefinedCurveDirectionException(ConnectiveGeometryException):
    """ UndefinedCurveDirectionException() """

class UnsupportedChamferException(ConnectiveGeometryException):
    """ UnsupportedChamferException() """

class Weld(BaseWeld):
    """ Weld() """
    def Delete(self):
        """ Delete(self: Weld) -> bool """
        pass

    def GetLogicalWeld(self, LogicalWeld):
        """ GetLogicalWeld(self: Weld, LogicalWeld: LogicalWeld) -> (bool, LogicalWeld) """
        pass

    def Insert(self):
        """ Insert(self: Weld) -> bool """
        pass

    def Modify(self):
        """ Modify(self: Weld) -> bool """
        pass

    def Select(self):
        """ Select(self: Weld) -> bool """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Weld) -> Vector

Set: Direction(self: Weld) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Weld) -> WeldPositionEnum

Set: Position(self: Weld) = value
"""


    WeldPositionEnum = None


class WorkPlaneHandler(object):
    # no doc
    def GetCurrentTransformationPlane(self):
        """ GetCurrentTransformationPlane(self: WorkPlaneHandler) -> TransformationPlane """
        pass

    def SetCurrentTransformationPlane(self, TransformationPlane):
        """ SetCurrentTransformationPlane(self: WorkPlaneHandler, TransformationPlane: TransformationPlane) -> bool """
        pass


# variables with complex values

