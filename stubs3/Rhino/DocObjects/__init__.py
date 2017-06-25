# encoding: utf-8
# module Rhino.DocObjects calls itself DocObjects
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ActiveSpace(Enum):
    """ enum ActiveSpace, values: ModelSpace (1), None (0), PageSpace (2) """
    ModelSpace = None
    None = None
    PageSpace = None
    value__ = None


class BasepointZero(Enum):
    """ enum BasepointZero, values: CenterOfEarth (2), GroundLevel (0), MeanSeaLevel (1) """
    CenterOfEarth = None
    GroundLevel = None
    MeanSeaLevel = None
    value__ = None


class ConstructionPlane(object):
    """ ConstructionPlane() """
    DepthBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthBuffered(self: ConstructionPlane) -> bool

Set: DepthBuffered(self: ConstructionPlane) = value
"""

    GridLineCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridLineCount(self: ConstructionPlane) -> int

Set: GridLineCount(self: ConstructionPlane) = value
"""

    GridSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridSpacing(self: ConstructionPlane) -> float

Set: GridSpacing(self: ConstructionPlane) = value
"""

    GridXColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridXColor(self: ConstructionPlane) -> Color

Set: GridXColor(self: ConstructionPlane) = value
"""

    GridYColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridYColor(self: ConstructionPlane) -> Color

Set: GridYColor(self: ConstructionPlane) = value
"""

    GridZColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridZColor(self: ConstructionPlane) -> Color

Set: GridZColor(self: ConstructionPlane) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConstructionPlane) -> str

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: ConstructionPlane) -> Plane

Set: Plane(self: ConstructionPlane) = value
"""

    ShowAxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowAxes(self: ConstructionPlane) -> bool

Set: ShowAxes(self: ConstructionPlane) = value
"""

    ShowGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowGrid(self: ConstructionPlane) -> bool

Set: ShowGrid(self: ConstructionPlane) = value
"""

    SnapSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SnapSpacing(self: ConstructionPlane) -> float

Set: SnapSpacing(self: ConstructionPlane) = value
"""

    ThickLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThickLineColor(self: ConstructionPlane) -> Color

Set: ThickLineColor(self: ConstructionPlane) = value
"""

    ThickLineFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThickLineFrequency(self: ConstructionPlane) -> int

Set: ThickLineFrequency(self: ConstructionPlane) = value
"""

    ThinLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThinLineColor(self: ConstructionPlane) -> Color

Set: ThinLineColor(self: ConstructionPlane) = value
"""



class CoordinateSystem(Enum):
    """ enum CoordinateSystem, values: Camera (1), Clip (2), Screen (3), World (0) """
    Camera = None
    Clip = None
    Screen = None
    value__ = None
    World = None


class DimensionStyle(CommonObject):
    """ DimensionStyle() """
    def CommitChanges(self):
        """ CommitChanges(self: DimensionStyle) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    AlternateLengthFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlternateLengthFactor(self: DimensionStyle) -> float

Set: AlternateLengthFactor(self: DimensionStyle) = value
"""

    AngleResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleResolution(self: DimensionStyle) -> int

Set: AngleResolution(self: DimensionStyle) = value
"""

    ArrowLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowLength(self: DimensionStyle) -> float

Set: ArrowLength(self: DimensionStyle) = value
"""

    ArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: ArrowType(self: DimensionStyle) = value
"""

    CenterMarkSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterMarkSize(self: DimensionStyle) -> float

Set: CenterMarkSize(self: DimensionStyle) = value
"""

    ExtensionLineExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLineExtension(self: DimensionStyle) -> float

Set: ExtensionLineExtension(self: DimensionStyle) = value
"""

    ExtensionLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLineOffset(self: DimensionStyle) -> float

Set: ExtensionLineOffset(self: DimensionStyle) = value
"""

    FontIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontIndex(self: DimensionStyle) -> int

Set: FontIndex(self: DimensionStyle) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DimensionStyle) -> Guid

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: DimensionStyle) -> int

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReference(self: DimensionStyle) -> bool

"""

    LeaderArrowLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderArrowLength(self: DimensionStyle) -> float

Set: LeaderArrowLength(self: DimensionStyle) = value
"""

    LeaderArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: LeaderArrowType(self: DimensionStyle) = value
"""

    LengthFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFactor(self: DimensionStyle) -> float

Set: LengthFactor(self: DimensionStyle) = value
"""

    LengthFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFormat(self: DimensionStyle) -> DistanceDisplayMode

Set: LengthFormat(self: DimensionStyle) = value
"""

    LengthResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthResolution(self: DimensionStyle) -> int

Set: LengthResolution(self: DimensionStyle) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DimensionStyle) -> str

Set: Name(self: DimensionStyle) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: DimensionStyle) -> str

Set: Prefix(self: DimensionStyle) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: DimensionStyle) -> str

Set: Suffix(self: DimensionStyle) = value
"""

    TextAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextAlignment(self: DimensionStyle) -> TextDisplayAlignment

Set: TextAlignment(self: DimensionStyle) = value
"""

    TextGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextGap(self: DimensionStyle) -> float

Set: TextGap(self: DimensionStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: DimensionStyle) -> float

Set: TextHeight(self: DimensionStyle) = value
"""



class DimensionStyleArrowType(Enum):
    """ enum DimensionStyleArrowType, values: Arrow (4), Dot (1), LongerTriangle (7), LongTriangle (6), Rectangle (5), ShortTriangle (3), SolidTriangle (0), Tick (2) """
    Arrow = None
    Dot = None
    LongerTriangle = None
    LongTriangle = None
    Rectangle = None
    ShortTriangle = None
    SolidTriangle = None
    Tick = None
    value__ = None


class DisplayMode(Enum):
    """ enum DisplayMode, values: Default (0), RenderPreview (3), Shaded (2), Wireframe (1) """
    Default = None
    RenderPreview = None
    Shaded = None
    value__ = None
    Wireframe = None


class DistanceDisplayMode(Enum):
    """ enum DistanceDisplayMode, values: Decimal (0), Feet (1), FeetAndInches (2) """
    Decimal = None
    Feet = None
    FeetAndInches = None
    value__ = None


class EarthAnchorPoint(object):
    """ EarthAnchorPoint() """
    def Dispose(self):
        """ Dispose(self: EarthAnchorPoint) """
        pass

    def GetModelCompass(self):
        """ GetModelCompass(self: EarthAnchorPoint) -> Plane """
        pass

    def GetModelToEarthTransform(self, modelUnitSystem):
        """ GetModelToEarthTransform(self: EarthAnchorPoint, modelUnitSystem: UnitSystem) -> Transform """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: EarthAnchorPoint) -> str

Set: Description(self: EarthAnchorPoint) = value
"""

    EarthBasepointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EarthBasepointElevation(self: EarthAnchorPoint) -> float

Set: EarthBasepointElevation(self: EarthAnchorPoint) = value
"""

    EarthBasepointElevationZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EarthBasepointElevationZero(self: EarthAnchorPoint) -> BasepointZero

Set: EarthBasepointElevationZero(self: EarthAnchorPoint) = value
"""

    EarthBasepointLatitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EarthBasepointLatitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLatitude(self: EarthAnchorPoint) = value
"""

    EarthBasepointLongitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EarthBasepointLongitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLongitude(self: EarthAnchorPoint) = value
"""

    ModelBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelBasePoint(self: EarthAnchorPoint) -> Point3d

Set: ModelBasePoint(self: EarthAnchorPoint) = value
"""

    ModelEast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelEast(self: EarthAnchorPoint) -> Vector3d

Set: ModelEast(self: EarthAnchorPoint) = value
"""

    ModelNorth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelNorth(self: EarthAnchorPoint) -> Vector3d

Set: ModelNorth(self: EarthAnchorPoint) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EarthAnchorPoint) -> str

Set: Name(self: EarthAnchorPoint) = value
"""



class HatchPattern(CommonObject):
    """ HatchPattern() """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: HatchPattern) -> str

Set: Description(self: HatchPattern) = value
"""

    FillType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillType(self: HatchPattern) -> HatchPatternFillType

Set: FillType(self: HatchPattern) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: HatchPattern) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HatchPattern) -> str

Set: Name(self: HatchPattern) = value
"""



class HatchPatternFillType(Enum):
    """ enum HatchPatternFillType, values: Gradient (2), Lines (1), Solid (0) """
    Gradient = None
    Lines = None
    Solid = None
    value__ = None


class InstanceDefinitionArchiveFileStatus(Enum):
    """ enum InstanceDefinitionArchiveFileStatus, values: LinkedFileIsDifferent (3), LinkedFileIsNewer (1), LinkedFileIsOlder (2), LinkedFileIsUpToDate (0), LinkedFileNotFound (-1), LinkedFileNotReadable (-2), NotALinkedInstanceDefinition (-3) """
    LinkedFileIsDifferent = None
    LinkedFileIsNewer = None
    LinkedFileIsOlder = None
    LinkedFileIsUpToDate = None
    LinkedFileNotFound = None
    LinkedFileNotReadable = None
    NotALinkedInstanceDefinition = None
    value__ = None


class InstanceDefinitionLayerStyle(Enum):
    """ enum InstanceDefinitionLayerStyle, values: Active (1), None (0), Reference (2) """
    Active = None
    None = None
    Reference = None
    value__ = None


class InstanceDefinitionUpdateType(Enum):
    """ enum InstanceDefinitionUpdateType, values: Embedded (1), Linked (3), LinkedAndEmbedded (2), Static (0) """
    Embedded = None
    Linked = None
    LinkedAndEmbedded = None
    Static = None
    value__ = None


class Layer(CommonObject):
    """ Layer() """
    def CommitChanges(self):
        """ CommitChanges(self: Layer) -> bool """
        pass

    def Default(self):
        """ Default(self: Layer) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetPersistentLocking(self):
        """ GetPersistentLocking(self: Layer) -> bool """
        pass

    def GetPersistentVisibility(self):
        """ GetPersistentVisibility(self: Layer) -> bool """
        pass

    def GetUserString(self, key):
        """ GetUserString(self: Layer, key: str) -> str """
        pass

    def GetUserStrings(self):
        """ GetUserStrings(self: Layer) -> NameValueCollection """
        pass

    def SetPersistentLocking(self, persistentLocking):
        """ SetPersistentLocking(self: Layer, persistentLocking: bool) """
        pass

    def SetPersistentVisibility(self, persistentVisibility):
        """ SetPersistentVisibility(self: Layer, persistentVisibility: bool) """
        pass

    def SetUserString(self, key, value):
        """ SetUserString(self: Layer, key: str, value: str) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Layer) -> str """
        pass

    def UnsetPersistentLocking(self):
        """ UnsetPersistentLocking(self: Layer) """
        pass

    def UnsetPersistentVisibility(self):
        """ UnsetPersistentVisibility(self: Layer) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Layer) -> Color

Set: Color(self: Layer) = value
"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullPath(self: Layer) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Layer) -> Guid

Set: Id(self: Layer) = value
"""

    IgesLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgesLevel(self: Layer) -> int

Set: IgesLevel(self: Layer) = value
"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeleted(self: Layer) -> bool

"""

    IsExpanded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExpanded(self: Layer) -> bool

Set: IsExpanded(self: Layer) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocked(self: Layer) -> bool

Set: IsLocked(self: Layer) = value
"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReference(self: Layer) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: Layer) -> bool

Set: IsVisible(self: Layer) = value
"""

    LayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerIndex(self: Layer) -> int

Set: LayerIndex(self: Layer) = value
"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeIndex(self: Layer) -> int

Set: LinetypeIndex(self: Layer) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Layer) -> str

Set: Name(self: Layer) = value
"""

    ParentLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentLayerId(self: Layer) -> Guid

Set: ParentLayerId(self: Layer) = value
"""

    PlotColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotColor(self: Layer) -> Color

Set: PlotColor(self: Layer) = value
"""

    PlotWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWeight(self: Layer) -> float

Set: PlotWeight(self: Layer) = value
"""

    RenderMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialIndex(self: Layer) -> int

Set: RenderMaterialIndex(self: Layer) = value
"""

    SortIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortIndex(self: Layer) -> int

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: Layer) -> int

"""



class Linetype(CommonObject):
    """ Linetype() """
    def AppendSegment(self, length, isSolid):
        """ AppendSegment(self: Linetype, length: float, isSolid: bool) -> int """
        pass

    def CommitChanges(self):
        """ CommitChanges(self: Linetype) -> bool """
        pass

    def Default(self):
        """ Default(self: Linetype) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetSegment(self, index, length, isSolid):
        """ GetSegment(self: Linetype, index: int) -> (float, bool) """
        pass

    def RemoveSegment(self, index):
        """ RemoveSegment(self: Linetype, index: int) -> bool """
        pass

    def SetSegment(self, index, length, isSolid):
        """ SetSegment(self: Linetype, index: int, length: float, isSolid: bool) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Linetype) -> Guid

Set: Id(self: Linetype) = value
"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeleted(self: Linetype) -> bool

"""

    IsModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsModified(self: Linetype) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReference(self: Linetype) -> bool

"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeIndex(self: Linetype) -> int

Set: LinetypeIndex(self: Linetype) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Linetype) -> str

Set: Name(self: Linetype) = value
"""

    PatternLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternLength(self: Linetype) -> float

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentCount(self: Linetype) -> int

"""



class Material(CommonObject):
    """ Material() """
    def CommitChanges(self):
        """ CommitChanges(self: Material) -> bool """
        pass

    def Default(self):
        """ Default(self: Material) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetBitmapTexture(self):
        """ GetBitmapTexture(self: Material) -> Texture """
        pass

    def GetBumpTexture(self):
        """ GetBumpTexture(self: Material) -> Texture """
        pass

    def GetEnvironmentTexture(self):
        """ GetEnvironmentTexture(self: Material) -> Texture """
        pass

    def GetTextures(self):
        """ GetTextures(self: Material) -> Array[Texture] """
        pass

    def GetTransparencyTexture(self):
        """ GetTransparencyTexture(self: Material) -> Texture """
        pass

    def GetUserString(self, key):
        """ GetUserString(self: Material, key: str) -> str """
        pass

    def GetUserStrings(self):
        """ GetUserStrings(self: Material) -> NameValueCollection """
        pass

    def SetBitmapTexture(self, *__args):
        """
        SetBitmapTexture(self: Material, texture: Texture) -> bool
        SetBitmapTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetBumpTexture(self, *__args):
        """
        SetBumpTexture(self: Material, texture: Texture) -> bool
        SetBumpTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetEnvironmentTexture(self, *__args):
        """
        SetEnvironmentTexture(self: Material, texture: Texture) -> bool
        SetEnvironmentTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetTransparencyTexture(self, *__args):
        """
        SetTransparencyTexture(self: Material, texture: Texture) -> bool
        SetTransparencyTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetUserString(self, key, value):
        """ SetUserString(self: Material, key: str, value: str) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: Material) -> Color

Set: AmbientColor(self: Material) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: Material) -> Color

Set: DiffuseColor(self: Material) = value
"""

    EmissionColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EmissionColor(self: Material) -> Color

Set: EmissionColor(self: Material) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Material) -> Guid

"""

    IndexOfRefraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndexOfRefraction(self: Material) -> float

Set: IndexOfRefraction(self: Material) = value
"""

    IsDefaultMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultMaterial(self: Material) -> bool

"""

    MaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialIndex(self: Material) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Material) -> str

Set: Name(self: Material) = value
"""

    ReflectionColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectionColor(self: Material) -> Color

Set: ReflectionColor(self: Material) = value
"""

    Reflectivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reflectivity(self: Material) -> float

Set: Reflectivity(self: Material) = value
"""

    RenderPlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderPlugInId(self: Material) -> Guid

Set: RenderPlugInId(self: Material) = value
"""

    Shine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shine(self: Material) -> float

Set: Shine(self: Material) = value
"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: Material) -> Color

Set: SpecularColor(self: Material) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparency(self: Material) -> float

Set: Transparency(self: Material) = value
"""

    TransparentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransparentColor(self: Material) -> Color

Set: TransparentColor(self: Material) = value
"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: Material) -> int

"""


    MaxShine = 255.0


class MaterialRef(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: MaterialRef) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    BackFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackFaceMaterialId(self: MaterialRef) -> Guid

"""

    BackFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackFaceMaterialIndex(self: MaterialRef) -> int

"""

    FrontFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontFaceMaterialId(self: MaterialRef) -> Guid

"""

    FrontFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontFaceMaterialIndex(self: MaterialRef) -> int

"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialSource(self: MaterialRef) -> ObjectMaterialSource

"""

    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlugInId(self: MaterialRef) -> Guid

"""



class MaterialRefCreateParams(object):
    """ MaterialRefCreateParams() """
    BackFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: BackFaceMaterialId(self: MaterialRefCreateParams) = value
"""

    BackFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: BackFaceMaterialIndex(self: MaterialRefCreateParams) = value
"""

    FrontFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: FrontFaceMaterialId(self: MaterialRefCreateParams) = value
"""

    FrontFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: FrontFaceMaterialIndex(self: MaterialRefCreateParams) = value
"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialSource(self: MaterialRefCreateParams) -> ObjectMaterialSource

Set: MaterialSource(self: MaterialRefCreateParams) = value
"""

    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlugInId(self: MaterialRefCreateParams) -> Guid

Set: PlugInId(self: MaterialRefCreateParams) = value
"""



class MaterialRefs(object):
    # no doc
    def Add(self, *__args):
        """ Add(self: MaterialRefs, key: Guid, value: MaterialRef)Add(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef]) """
        pass

    def Clear(self):
        """ Clear(self: MaterialRefs) """
        pass

    def Contains(self, item):
        """ Contains(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef]) -> bool """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: MaterialRefs, key: Guid) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MaterialRefs, array: Array[KeyValuePair[Guid, MaterialRef]], arrayIndex: int) """
        pass

    def Create(self, createParams):
        """ Create(self: MaterialRefs, createParams: MaterialRefCreateParams) -> MaterialRef """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MaterialRefs) -> IEnumerator[KeyValuePair[Guid, MaterialRef]] """
        pass

    def Remove(self, *__args):
        """
        Remove(self: MaterialRefs, key: Guid) -> bool
        Remove(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef]) -> bool
        """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: MaterialRefs, key: Guid) -> (bool, MaterialRef) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Guid, MaterialRef], key: Guid) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MaterialRefs) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MaterialRefs) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: MaterialRefs) -> ICollection[Guid]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: MaterialRefs) -> ICollection[MaterialRef]

"""



class ObjectAttributes(CommonObject):
    """ ObjectAttributes() """
    def AddToGroup(self, groupIndex):
        """ AddToGroup(self: ObjectAttributes, groupIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: ObjectAttributes) -> ObjectAttributes """
        pass

    def GetGroupList(self):
        """ GetGroupList(self: ObjectAttributes) -> Array[int] """
        pass

    def GetUserString(self, key):
        """ GetUserString(self: ObjectAttributes, key: str) -> str """
        pass

    def GetUserStrings(self):
        """ GetUserStrings(self: ObjectAttributes) -> NameValueCollection """
        pass

    def HasDisplayModeOverride(self, viewportId):
        """ HasDisplayModeOverride(self: ObjectAttributes, viewportId: Guid) -> bool """
        pass

    def RemoveDisplayModeOverride(self, rhinoViewportId=None):
        """ RemoveDisplayModeOverride(self: ObjectAttributes, rhinoViewportId: Guid)RemoveDisplayModeOverride(self: ObjectAttributes) """
        pass

    def RemoveFromAllGroups(self):
        """ RemoveFromAllGroups(self: ObjectAttributes) """
        pass

    def RemoveFromGroup(self, groupIndex):
        """ RemoveFromGroup(self: ObjectAttributes, groupIndex: int) """
        pass

    def SetUserString(self, key, value):
        """ SetUserString(self: ObjectAttributes, key: str, value: str) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ColorSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorSource(self: ObjectAttributes) -> ObjectColorSource

Set: ColorSource(self: ObjectAttributes) = value
"""

    GroupCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupCount(self: ObjectAttributes) -> int

"""

    HasMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasMapping(self: ObjectAttributes) -> bool

"""

    IsInstanceDefinitionObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInstanceDefinitionObject(self: ObjectAttributes) -> bool

"""

    LayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerIndex(self: ObjectAttributes) -> int

Set: LayerIndex(self: ObjectAttributes) = value
"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeIndex(self: ObjectAttributes) -> int

Set: LinetypeIndex(self: ObjectAttributes) = value
"""

    LinetypeSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeSource(self: ObjectAttributes) -> ObjectLinetypeSource

Set: LinetypeSource(self: ObjectAttributes) = value
"""

    MaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialIndex(self: ObjectAttributes) -> int

Set: MaterialIndex(self: ObjectAttributes) = value
"""

    MaterialRefs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialRefs(self: ObjectAttributes) -> MaterialRefs

"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialSource(self: ObjectAttributes) -> ObjectMaterialSource

Set: MaterialSource(self: ObjectAttributes) = value
"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mode(self: ObjectAttributes) -> ObjectMode

Set: Mode(self: ObjectAttributes) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ObjectAttributes) -> str

Set: Name(self: ObjectAttributes) = value
"""

    ObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectColor(self: ObjectAttributes) -> Color

Set: ObjectColor(self: ObjectAttributes) = value
"""

    ObjectDecoration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectDecoration(self: ObjectAttributes) -> ObjectDecoration

Set: ObjectDecoration(self: ObjectAttributes) = value
"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: ObjectAttributes) -> Guid

Set: ObjectId(self: ObjectAttributes) = value
"""

    PlotColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotColor(self: ObjectAttributes) -> Color

Set: PlotColor(self: ObjectAttributes) = value
"""

    PlotColorSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotColorSource(self: ObjectAttributes) -> ObjectPlotColorSource

Set: PlotColorSource(self: ObjectAttributes) = value
"""

    PlotWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWeight(self: ObjectAttributes) -> float

Set: PlotWeight(self: ObjectAttributes) = value
"""

    PlotWeightSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWeightSource(self: ObjectAttributes) -> ObjectPlotWeightSource

Set: PlotWeightSource(self: ObjectAttributes) = value
"""

    Space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Space(self: ObjectAttributes) -> ActiveSpace

Set: Space(self: ObjectAttributes) = value
"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: ObjectAttributes) -> int

"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportId(self: ObjectAttributes) -> Guid

Set: ViewportId(self: ObjectAttributes) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: ObjectAttributes) -> bool

Set: Visible(self: ObjectAttributes) = value
"""

    WireDensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WireDensity(self: ObjectAttributes) -> int

Set: WireDensity(self: ObjectAttributes) = value
"""



class ObjectColorSource(Enum):
    """ enum ObjectColorSource, values: ColorFromLayer (0), ColorFromMaterial (2), ColorFromObject (1), ColorFromParent (3) """
    ColorFromLayer = None
    ColorFromMaterial = None
    ColorFromObject = None
    ColorFromParent = None
    value__ = None


class ObjectDecoration(Enum):
    """ enum (flags) ObjectDecoration, values: BothArrowhead (24), EndArrowhead (16), None (0), StartArrowhead (8) """
    BothArrowhead = None
    EndArrowhead = None
    None = None
    StartArrowhead = None
    value__ = None


class ObjectLinetypeSource(Enum):
    """ enum ObjectLinetypeSource, values: LinetypeFromLayer (0), LinetypeFromObject (1), LinetypeFromParent (3) """
    LinetypeFromLayer = None
    LinetypeFromObject = None
    LinetypeFromParent = None
    value__ = None


class ObjectMaterialSource(Enum):
    """ enum ObjectMaterialSource, values: MaterialFromLayer (0), MaterialFromObject (1), MaterialFromParent (3) """
    MaterialFromLayer = None
    MaterialFromObject = None
    MaterialFromParent = None
    value__ = None


class ObjectMode(Enum):
    """ enum ObjectMode, values: Hidden (1), InstanceDefinitionObject (3), Locked (2), Normal (0) """
    Hidden = None
    InstanceDefinitionObject = None
    Locked = None
    Normal = None
    value__ = None


class ObjectPlotColorSource(Enum):
    """ enum ObjectPlotColorSource, values: PlotColorFromDisplay (2), PlotColorFromLayer (0), PlotColorFromObject (1), PlotColorFromParent (3) """
    PlotColorFromDisplay = None
    PlotColorFromLayer = None
    PlotColorFromObject = None
    PlotColorFromParent = None
    value__ = None


class ObjectPlotWeightSource(Enum):
    """ enum ObjectPlotWeightSource, values: PlotWeightFromLayer (0), PlotWeightFromObject (1), PlotWeightFromParent (3) """
    PlotWeightFromLayer = None
    PlotWeightFromObject = None
    PlotWeightFromParent = None
    value__ = None


class ObjectType(Enum):
    """ enum (flags) ObjectType, values: Annotation (512), AnyObject (4294967295), Brep (16), BrepLoop (524288), Cage (134217728), ClipPlane (536870912), Curve (4), Detail (32768), EdgeFilter (4194304), Extrusion (1073741824), Grip (16384), Hatch (65536), InstanceDefinition (2048), InstanceReference (4096), Light (256), Mesh (32), MeshEdge (33554432), MeshFace (67108864), MeshVertex (16777216), MorphControl (131072), None (0), Phantom (268435456), Point (1), PointSet (2), PolyedgeFilter (8388608), PolysrfFilter (2097152), Surface (8), TextDot (8192) """
    Annotation = None
    AnyObject = None
    Brep = None
    BrepLoop = None
    Cage = None
    ClipPlane = None
    Curve = None
    Detail = None
    EdgeFilter = None
    Extrusion = None
    Grip = None
    Hatch = None
    InstanceDefinition = None
    InstanceReference = None
    Light = None
    Mesh = None
    MeshEdge = None
    MeshFace = None
    MeshVertex = None
    MorphControl = None
    None = None
    Phantom = None
    Point = None
    PointSet = None
    PolyedgeFilter = None
    PolysrfFilter = None
    Surface = None
    TextDot = None
    value__ = None


class SelectionMethod(Enum):
    """ enum SelectionMethod, values: CrossingBox (3), MousePick (1), Other (0), WindowBox (2) """
    CrossingBox = None
    MousePick = None
    Other = None
    value__ = None
    WindowBox = None


class TextDisplayAlignment(Enum):
    """ enum TextDisplayAlignment, values: AboveLine (2), Horizontal (1), InLine (3), Normal (0) """
    AboveLine = None
    Horizontal = None
    InLine = None
    Normal = None
    value__ = None


class Texture(CommonObject):
    """ Texture() """
    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetAlphaBlendValues(self, constant, a0, a1, a2, a3):
        """ GetAlphaBlendValues(self: Texture) -> (float, float, float, float, float) """
        pass

    def SetAlphaBlendValues(self, constant, a0, a1, a2, a3):
        """ SetAlphaBlendValues(self: Texture, constant: float, a0: float, a1: float, a2: float, a3: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ApplyUvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyUvwTransform(self: Texture) -> bool

Set: ApplyUvwTransform(self: Texture) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: Texture) -> bool

Set: Enabled(self: Texture) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: Texture) -> str

Set: FileName(self: Texture) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Texture) -> Guid

"""

    MappingChannelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingChannelId(self: Texture) -> int

"""

    TextureCombineMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureCombineMode(self: Texture) -> TextureCombineMode

Set: TextureCombineMode(self: Texture) = value
"""

    TextureType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureType(self: Texture) -> TextureType

Set: TextureType(self: Texture) = value
"""

    UvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UvwTransform(self: Texture) -> Transform

Set: UvwTransform(self: Texture) = value
"""

    WrapU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrapU(self: Texture) -> TextureUvwWrapping

Set: WrapU(self: Texture) = value
"""

    WrapV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrapV(self: Texture) -> TextureUvwWrapping

Set: WrapV(self: Texture) = value
"""

    WrapW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrapW(self: Texture) -> TextureUvwWrapping

Set: WrapW(self: Texture) = value
"""



class TextureCombineMode(Enum):
    """ enum TextureCombineMode, values: Blend (3), Decal (2), Modulate (1), None (0) """
    Blend = None
    Decal = None
    Modulate = None
    None = None
    value__ = None


class TextureType(Enum):
    """ enum TextureType, values: Bitmap (1), Bump (2), None (0), Transparency (3) """
    Bitmap = None
    Bump = None
    None = None
    Transparency = None
    value__ = None


class TextureUvwWrapping(Enum):
    """ enum TextureUvwWrapping, values: Clamp (1), Repeat (0) """
    Clamp = None
    Repeat = None
    value__ = None


class ViewInfo(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: ViewInfo) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ViewInfo) -> str

Set: Name(self: ViewInfo) = value
"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: ViewInfo) -> ViewportInfo

"""



class ViewportInfo(object):
    """
    ViewportInfo()
    ViewportInfo(other: ViewportInfo)
    """
    def ChangeToParallelProjection(self, symmetricFrustum):
        """ ChangeToParallelProjection(self: ViewportInfo, symmetricFrustum: bool) -> bool """
        pass

    def ChangeToPerspectiveProjection(self, targetDistance, symmetricFrustum, lensLength):
        """ ChangeToPerspectiveProjection(self: ViewportInfo, targetDistance: float, symmetricFrustum: bool, lensLength: float) -> bool """
        pass

    def ChangeToSymmetricFrustum(self, isLeftRightSymmetric, isTopBottomSymmetric, targetDistance):
        """ ChangeToSymmetricFrustum(self: ViewportInfo, isLeftRightSymmetric: bool, isTopBottomSymmetric: bool, targetDistance: float) -> bool """
        pass

    def ChangeToTwoPointPerspectiveProjection(self, targetDistance, up, lensLength):
        """ ChangeToTwoPointPerspectiveProjection(self: ViewportInfo, targetDistance: float, up: Vector3d, lensLength: float) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: ViewportInfo) """
        pass

    def DollyCamera(self, dollyVector):
        """ DollyCamera(self: ViewportInfo, dollyVector: Vector3d) -> bool """
        pass

    def DollyExtents(self, *__args):
        """
        DollyExtents(self: ViewportInfo, cameraCoordinateBoundingBox: BoundingBox, border: float) -> bool
        DollyExtents(self: ViewportInfo, geometry: IEnumerable[GeometryBase], border: float) -> bool
        """
        pass

    def DollyFrustum(self, dollyDistance):
        """ DollyFrustum(self: ViewportInfo, dollyDistance: float) -> bool """
        pass

    def Extents(self, halfViewAngleRadians, *__args):
        """
        Extents(self: ViewportInfo, halfViewAngleRadians: float, sphere: Sphere) -> bool
        Extents(self: ViewportInfo, halfViewAngleRadians: float, bbox: BoundingBox) -> bool
        """
        pass

    def FrustumCenterPoint(self, targetDistance):
        """ FrustumCenterPoint(self: ViewportInfo, targetDistance: float) -> Point3d """
        pass

    def GetBoundingBoxDepth(self, bbox, nearDistance, farDistance):
        """ GetBoundingBoxDepth(self: ViewportInfo, bbox: BoundingBox) -> (bool, float, float) """
        pass

    def GetCameraAngles(self, halfDiagonalAngleRadians, halfVerticalAngleRadians, halfHorizontalAngleRadians):
        """ GetCameraAngles(self: ViewportInfo) -> (bool, float, float, float) """
        pass

    def GetCameraFrame(self, location, cameraX, cameraY, cameraZ):
        """ GetCameraFrame(self: ViewportInfo) -> (bool, Point3d, Vector3d, Vector3d, Vector3d) """
        pass

    def GetDollyCameraVector(self, *__args):
        """
        GetDollyCameraVector(self: ViewportInfo, screen0: Point, screen1: Point, projectionPlaneDistance: float) -> Vector3d
        GetDollyCameraVector(self: ViewportInfo, screenX0: int, screenY0: int, screenX1: int, screenY1: int, projectionPlaneDistance: float) -> Vector3d
        """
        pass

    def GetFarPlaneCorners(self):
        """ GetFarPlaneCorners(self: ViewportInfo) -> Array[Point3d] """
        pass

    def GetFrustum(self, left, right, bottom, top, nearDistance, farDistance):
        """ GetFrustum(self: ViewportInfo) -> (bool, float, float, float, float, float, float) """
        pass

    def GetFrustumLine(self, *__args):
        """
        GetFrustumLine(self: ViewportInfo, screenPoint: PointF) -> Line
        GetFrustumLine(self: ViewportInfo, screenPoint: Point) -> Line
        GetFrustumLine(self: ViewportInfo, screenX: float, screenY: float) -> Line
        """
        pass

    def GetNearPlaneCorners(self):
        """ GetNearPlaneCorners(self: ViewportInfo) -> Array[Point3d] """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: ViewportInfo, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetPointDepth(self, point, distance):
        """ GetPointDepth(self: ViewportInfo, point: Point3d) -> (bool, float) """
        pass

    def GetScreenPort(self, near=None, far=None):
        """
        GetScreenPort(self: ViewportInfo) -> Rectangle
        GetScreenPort(self: ViewportInfo) -> (Rectangle, int, int)
        """
        pass

    def GetSphereDepth(self, sphere, nearDistance, farDistance):
        """ GetSphereDepth(self: ViewportInfo, sphere: Sphere) -> (bool, float, float) """
        pass

    def GetWorldToScreenScale(self, pointInFrustum):
        """ GetWorldToScreenScale(self: ViewportInfo, pointInFrustum: Point3d) -> float """
        pass

    def GetXform(self, sourceSystem, destinationSystem):
        """ GetXform(self: ViewportInfo, sourceSystem: CoordinateSystem, destinationSystem: CoordinateSystem) -> Transform """
        pass

    def SetCameraDirection(self, direction):
        """ SetCameraDirection(self: ViewportInfo, direction: Vector3d) -> bool """
        pass

    def SetCameraLocation(self, location):
        """ SetCameraLocation(self: ViewportInfo, location: Point3d) -> bool """
        pass

    def SetCameraUp(self, up):
        """ SetCameraUp(self: ViewportInfo, up: Vector3d) -> bool """
        pass

    def SetFrustum(self, left, right, bottom, top, nearDistance, farDistance):
        """ SetFrustum(self: ViewportInfo, left: float, right: float, bottom: float, top: float, nearDistance: float, farDistance: float) -> bool """
        pass

    def SetFrustumNearFar(self, *__args):
        """
        SetFrustumNearFar(self: ViewportInfo, nearDistance: float, farDistance: float) -> bool
        SetFrustumNearFar(self: ViewportInfo, nearDistance: float, farDistance: float, minNearDistance: float, minNearOverFar: float, targetDistance: float) -> bool
        SetFrustumNearFar(self: ViewportInfo, boundingBox: BoundingBox) -> bool
        SetFrustumNearFar(self: ViewportInfo, center: Point3d, radius: float) -> bool
        """
        pass

    def SetScreenPort(self, *__args):
        """
        SetScreenPort(self: ViewportInfo, windowRectangle: Rectangle) -> bool
        SetScreenPort(self: ViewportInfo, windowRectangle: Rectangle, near: int, far: int) -> bool
        SetScreenPort(self: ViewportInfo, left: int, right: int, bottom: int, top: int, near: int, far: int) -> bool
        """
        pass

    def TargetDistance(self, useFrustumCenterFallback):
        """ TargetDistance(self: ViewportInfo, useFrustumCenterFallback: bool) -> float """
        pass

    def UnlockCamera(self):
        """ UnlockCamera(self: ViewportInfo) """
        pass

    def UnlockFrustumSymmetry(self):
        """ UnlockFrustumSymmetry(self: ViewportInfo) """
        pass

    def ZoomToScreenRect(self, *__args):
        """
        ZoomToScreenRect(self: ViewportInfo, windowRectangle: Rectangle) -> bool
        ZoomToScreenRect(self: ViewportInfo, left: int, top: int, right: int, bottom: int) -> bool
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: ViewportInfo)
        """
        pass

    Camera35mmLensLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Camera35mmLensLength(self: ViewportInfo) -> float

Set: Camera35mmLensLength(self: ViewportInfo) = value
"""

    CameraAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraAngle(self: ViewportInfo) -> float

Set: CameraAngle(self: ViewportInfo) = value
"""

    CameraDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraDirection(self: ViewportInfo) -> Vector3d

"""

    CameraLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraLocation(self: ViewportInfo) -> Point3d

"""

    CameraUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraUp(self: ViewportInfo) -> Vector3d

"""

    CameraX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraX(self: ViewportInfo) -> Vector3d

"""

    CameraY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraY(self: ViewportInfo) -> Vector3d

"""

    CameraZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraZ(self: ViewportInfo) -> Vector3d

"""

    FrustumAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumAspect(self: ViewportInfo) -> float

Set: FrustumAspect(self: ViewportInfo) = value
"""

    FrustumBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumBottom(self: ViewportInfo) -> float

"""

    FrustumBottomPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumBottomPlane(self: ViewportInfo) -> Plane

"""

    FrustumCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumCenter(self: ViewportInfo) -> Point3d

"""

    FrustumFar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumFar(self: ViewportInfo) -> float

"""

    FrustumFarPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumFarPlane(self: ViewportInfo) -> Plane

"""

    FrustumHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumHeight(self: ViewportInfo) -> float

"""

    FrustumLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumLeft(self: ViewportInfo) -> float

"""

    FrustumLeftPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumLeftPlane(self: ViewportInfo) -> Plane

"""

    FrustumMaximumDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumMaximumDiameter(self: ViewportInfo) -> float

"""

    FrustumMinimumDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumMinimumDiameter(self: ViewportInfo) -> float

"""

    FrustumNear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumNear(self: ViewportInfo) -> float

"""

    FrustumNearPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumNearPlane(self: ViewportInfo) -> Plane

"""

    FrustumRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumRight(self: ViewportInfo) -> float

"""

    FrustumRightPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumRightPlane(self: ViewportInfo) -> Plane

"""

    FrustumTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumTop(self: ViewportInfo) -> float

"""

    FrustumTopPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumTopPlane(self: ViewportInfo) -> Plane

"""

    FrustumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrustumWidth(self: ViewportInfo) -> float

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ViewportInfo) -> Guid

"""

    IsCameraDirectionLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCameraDirectionLocked(self: ViewportInfo) -> bool

Set: IsCameraDirectionLocked(self: ViewportInfo) = value
"""

    IsCameraLocationLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCameraLocationLocked(self: ViewportInfo) -> bool

Set: IsCameraLocationLocked(self: ViewportInfo) = value
"""

    IsCameraUpLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCameraUpLocked(self: ViewportInfo) -> bool

Set: IsCameraUpLocked(self: ViewportInfo) = value
"""

    IsFrustumLeftRightSymmetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFrustumLeftRightSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumLeftRightSymmetric(self: ViewportInfo) = value
"""

    IsFrustumTopBottomSymmetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFrustumTopBottomSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumTopBottomSymmetric(self: ViewportInfo) = value
"""

    IsParallelProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParallelProjection(self: ViewportInfo) -> bool

Set: IsParallelProjection(self: ViewportInfo) = value
"""

    IsPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPerspectiveProjection(self: ViewportInfo) -> bool

Set: IsPerspectiveProjection(self: ViewportInfo) = value
"""

    IsTwoPointPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTwoPointPerspectiveProjection(self: ViewportInfo) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: ViewportInfo) -> bool

"""

    IsValidCamera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidCamera(self: ViewportInfo) -> bool

"""

    IsValidFrustum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidFrustum(self: ViewportInfo) -> bool

"""

    ScreenPortAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScreenPortAspect(self: ViewportInfo) -> float

"""

    TargetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetPoint(self: ViewportInfo) -> Point3d

Set: TargetPoint(self: ViewportInfo) = value
"""

    ViewScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewScale(self: ViewportInfo) -> SizeF

Set: ViewScale(self: ViewportInfo) = value
"""



# variables with complex values

