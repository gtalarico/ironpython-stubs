# encoding: utf-8
# module Rhino.DocObjects calls itself DocObjects
# from Rhino3dmIO,Version=5.1.30000.14,Culture=neutral,PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ActiveSpace(Enum,IComparable,IFormattable,IConvertible):
 """ enum ActiveSpace,values: ModelSpace (1),None (0),PageSpace (2) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ModelSpace=None
 None=None
 PageSpace=None
 value__=None


class BasepointZero(Enum,IComparable,IFormattable,IConvertible):
 """ enum BasepointZero,values: CenterOfEarth (2),GroundLevel (0),MeanSeaLevel (1) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 CenterOfEarth=None
 GroundLevel=None
 MeanSeaLevel=None
 value__=None


class ConstructionPlane(object):
 """ ConstructionPlane() """
 DepthBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DepthBuffered(self: ConstructionPlane) -> bool

Set: DepthBuffered(self: ConstructionPlane)=value
"""

 GridLineCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GridLineCount(self: ConstructionPlane) -> int

Set: GridLineCount(self: ConstructionPlane)=value
"""

 GridSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GridSpacing(self: ConstructionPlane) -> float

Set: GridSpacing(self: ConstructionPlane)=value
"""

 GridXColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GridXColor(self: ConstructionPlane) -> Color

Set: GridXColor(self: ConstructionPlane)=value
"""

 GridYColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GridYColor(self: ConstructionPlane) -> Color

Set: GridYColor(self: ConstructionPlane)=value
"""

 GridZColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GridZColor(self: ConstructionPlane) -> Color

Set: GridZColor(self: ConstructionPlane)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ConstructionPlane) -> str

"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Plane(self: ConstructionPlane) -> Plane

Set: Plane(self: ConstructionPlane)=value
"""

 ShowAxes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShowAxes(self: ConstructionPlane) -> bool

Set: ShowAxes(self: ConstructionPlane)=value
"""

 ShowGrid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShowGrid(self: ConstructionPlane) -> bool

Set: ShowGrid(self: ConstructionPlane)=value
"""

 SnapSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SnapSpacing(self: ConstructionPlane) -> float

Set: SnapSpacing(self: ConstructionPlane)=value
"""

 ThickLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ThickLineColor(self: ConstructionPlane) -> Color

Set: ThickLineColor(self: ConstructionPlane)=value
"""

 ThickLineFrequency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ThickLineFrequency(self: ConstructionPlane) -> int

Set: ThickLineFrequency(self: ConstructionPlane)=value
"""

 ThinLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ThinLineColor(self: ConstructionPlane) -> Color

Set: ThinLineColor(self: ConstructionPlane)=value
"""



class CoordinateSystem(Enum,IComparable,IFormattable,IConvertible):
 """ enum CoordinateSystem,values: Camera (1),Clip (2),Screen (3),World (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Camera=None
 Clip=None
 Screen=None
 value__=None
 World=None


class DimensionStyle(CommonObject,IDisposable,ISerializable):
 """ DimensionStyle() """
 def CommitChanges(self):
  """ CommitChanges(self: DimensionStyle) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AlternateLengthFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AlternateLengthFactor(self: DimensionStyle) -> float

Set: AlternateLengthFactor(self: DimensionStyle)=value
"""

 AngleResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleResolution(self: DimensionStyle) -> int

Set: AngleResolution(self: DimensionStyle)=value
"""

 ArrowLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArrowLength(self: DimensionStyle) -> float

Set: ArrowLength(self: DimensionStyle)=value
"""

 ArrowType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: ArrowType(self: DimensionStyle)=value
"""

 CenterMarkSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CenterMarkSize(self: DimensionStyle) -> float

Set: CenterMarkSize(self: DimensionStyle)=value
"""

 ExtensionLineExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLineExtension(self: DimensionStyle) -> float

Set: ExtensionLineExtension(self: DimensionStyle)=value
"""

 ExtensionLineOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLineOffset(self: DimensionStyle) -> float

Set: ExtensionLineOffset(self: DimensionStyle)=value
"""

 FontIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FontIndex(self: DimensionStyle) -> int

Set: FontIndex(self: DimensionStyle)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: DimensionStyle) -> Guid

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Index(self: DimensionStyle) -> int

"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReference(self: DimensionStyle) -> bool

"""

 LeaderArrowLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LeaderArrowLength(self: DimensionStyle) -> float

Set: LeaderArrowLength(self: DimensionStyle)=value
"""

 LeaderArrowType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LeaderArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: LeaderArrowType(self: DimensionStyle)=value
"""

 LengthFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LengthFactor(self: DimensionStyle) -> float

Set: LengthFactor(self: DimensionStyle)=value
"""

 LengthFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LengthFormat(self: DimensionStyle) -> DistanceDisplayMode

Set: LengthFormat(self: DimensionStyle)=value
"""

 LengthResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LengthResolution(self: DimensionStyle) -> int

Set: LengthResolution(self: DimensionStyle)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: DimensionStyle) -> str

Set: Name(self: DimensionStyle)=value
"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Prefix(self: DimensionStyle) -> str

Set: Prefix(self: DimensionStyle)=value
"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Suffix(self: DimensionStyle) -> str

Set: Suffix(self: DimensionStyle)=value
"""

 TextAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextAlignment(self: DimensionStyle) -> TextDisplayAlignment

Set: TextAlignment(self: DimensionStyle)=value
"""

 TextGap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextGap(self: DimensionStyle) -> float

Set: TextGap(self: DimensionStyle)=value
"""

 TextHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextHeight(self: DimensionStyle) -> float

Set: TextHeight(self: DimensionStyle)=value
"""



class DimensionStyleArrowType(Enum,IComparable,IFormattable,IConvertible):
 """ enum DimensionStyleArrowType,values: Arrow (4),Dot (1),LongerTriangle (7),LongTriangle (6),Rectangle (5),ShortTriangle (3),SolidTriangle (0),Tick (2) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Arrow=None
 Dot=None
 LongerTriangle=None
 LongTriangle=None
 Rectangle=None
 ShortTriangle=None
 SolidTriangle=None
 Tick=None
 value__=None


class DisplayMode(Enum,IComparable,IFormattable,IConvertible):
 """ enum DisplayMode,values: Default (0),RenderPreview (3),Shaded (2),Wireframe (1) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Default=None
 RenderPreview=None
 Shaded=None
 value__=None
 Wireframe=None


class DistanceDisplayMode(Enum,IComparable,IFormattable,IConvertible):
 """ enum DistanceDisplayMode,values: Decimal (0),Feet (1),FeetAndInches (2) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Decimal=None
 Feet=None
 FeetAndInches=None
 value__=None


class EarthAnchorPoint(object,IDisposable):
 """ EarthAnchorPoint() """
 def Dispose(self):
  """ Dispose(self: EarthAnchorPoint) """
  pass
 def GetModelCompass(self):
  """ GetModelCompass(self: EarthAnchorPoint) -> Plane """
  pass
 def GetModelToEarthTransform(self,modelUnitSystem):
  """ GetModelToEarthTransform(self: EarthAnchorPoint,modelUnitSystem: UnitSystem) -> Transform """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: EarthAnchorPoint) -> str

Set: Description(self: EarthAnchorPoint)=value
"""

 EarthBasepointElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EarthBasepointElevation(self: EarthAnchorPoint) -> float

Set: EarthBasepointElevation(self: EarthAnchorPoint)=value
"""

 EarthBasepointElevationZero=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EarthBasepointElevationZero(self: EarthAnchorPoint) -> BasepointZero

Set: EarthBasepointElevationZero(self: EarthAnchorPoint)=value
"""

 EarthBasepointLatitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EarthBasepointLatitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLatitude(self: EarthAnchorPoint)=value
"""

 EarthBasepointLongitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EarthBasepointLongitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLongitude(self: EarthAnchorPoint)=value
"""

 ModelBasePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModelBasePoint(self: EarthAnchorPoint) -> Point3d

Set: ModelBasePoint(self: EarthAnchorPoint)=value
"""

 ModelEast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModelEast(self: EarthAnchorPoint) -> Vector3d

Set: ModelEast(self: EarthAnchorPoint)=value
"""

 ModelNorth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ModelNorth(self: EarthAnchorPoint) -> Vector3d

Set: ModelNorth(self: EarthAnchorPoint)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: EarthAnchorPoint) -> str

Set: Name(self: EarthAnchorPoint)=value
"""



class HatchPattern(CommonObject,IDisposable,ISerializable):
 """ HatchPattern() """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: HatchPattern) -> str

Set: Description(self: HatchPattern)=value
"""

 FillType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FillType(self: HatchPattern) -> HatchPatternFillType

Set: FillType(self: HatchPattern)=value
"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Index(self: HatchPattern) -> int

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: HatchPattern) -> str

Set: Name(self: HatchPattern)=value
"""



class HatchPatternFillType(Enum,IComparable,IFormattable,IConvertible):
 """ enum HatchPatternFillType,values: Gradient (2),Lines (1),Solid (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Gradient=None
 Lines=None
 Solid=None
 value__=None


class InstanceDefinitionArchiveFileStatus(Enum,IComparable,IFormattable,IConvertible):
 """ enum InstanceDefinitionArchiveFileStatus,values: LinkedFileIsDifferent (3),LinkedFileIsNewer (1),LinkedFileIsOlder (2),LinkedFileIsUpToDate (0),LinkedFileNotFound (-1),LinkedFileNotReadable (-2),NotALinkedInstanceDefinition (-3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 LinkedFileIsDifferent=None
 LinkedFileIsNewer=None
 LinkedFileIsOlder=None
 LinkedFileIsUpToDate=None
 LinkedFileNotFound=None
 LinkedFileNotReadable=None
 NotALinkedInstanceDefinition=None
 value__=None


class InstanceDefinitionLayerStyle(Enum,IComparable,IFormattable,IConvertible):
 """ enum InstanceDefinitionLayerStyle,values: Active (1),None (0),Reference (2) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Active=None
 None=None
 Reference=None
 value__=None


class InstanceDefinitionUpdateType(Enum,IComparable,IFormattable,IConvertible):
 """ enum InstanceDefinitionUpdateType,values: Embedded (1),Linked (3),LinkedAndEmbedded (2),Static (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Embedded=None
 Linked=None
 LinkedAndEmbedded=None
 Static=None
 value__=None


class Layer(CommonObject,IDisposable,ISerializable):
 """ Layer() """
 def CommitChanges(self):
  """ CommitChanges(self: Layer) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Default(self):
  """ Default(self: Layer) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetPersistentLocking(self):
  """ GetPersistentLocking(self: Layer) -> bool """
  pass
 def GetPersistentVisibility(self):
  """ GetPersistentVisibility(self: Layer) -> bool """
  pass
 def GetUserString(self,key):
  """ GetUserString(self: Layer,key: str) -> str """
  pass
 def GetUserStrings(self):
  """ GetUserStrings(self: Layer) -> NameValueCollection """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def SetPersistentLocking(self,persistentLocking):
  """ SetPersistentLocking(self: Layer,persistentLocking: bool) """
  pass
 def SetPersistentVisibility(self,persistentVisibility):
  """ SetPersistentVisibility(self: Layer,persistentVisibility: bool) """
  pass
 def SetUserString(self,key,value):
  """ SetUserString(self: Layer,key: str,value: str) -> bool """
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
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Color(self: Layer) -> Color

Set: Color(self: Layer)=value
"""

 FullPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FullPath(self: Layer) -> str

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: Layer) -> Guid

Set: Id(self: Layer)=value
"""

 IgesLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IgesLevel(self: Layer) -> int

Set: IgesLevel(self: Layer)=value
"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDeleted(self: Layer) -> bool

"""

 IsExpanded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsExpanded(self: Layer) -> bool

Set: IsExpanded(self: Layer)=value
"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLocked(self: Layer) -> bool

Set: IsLocked(self: Layer)=value
"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReference(self: Layer) -> bool

"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsVisible(self: Layer) -> bool

Set: IsVisible(self: Layer)=value
"""

 LayerIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LayerIndex(self: Layer) -> int

Set: LayerIndex(self: Layer)=value
"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LinetypeIndex(self: Layer) -> int

Set: LinetypeIndex(self: Layer)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Layer) -> str

Set: Name(self: Layer)=value
"""

 ParentLayerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ParentLayerId(self: Layer) -> Guid

Set: ParentLayerId(self: Layer)=value
"""

 PlotColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotColor(self: Layer) -> Color

Set: PlotColor(self: Layer)=value
"""

 PlotWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotWeight(self: Layer) -> float

Set: PlotWeight(self: Layer)=value
"""

 RenderMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RenderMaterialIndex(self: Layer) -> int

Set: RenderMaterialIndex(self: Layer)=value
"""

 SortIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SortIndex(self: Layer) -> int

"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: Layer) -> int

"""



class Linetype(CommonObject,IDisposable,ISerializable):
 """ Linetype() """
 def AppendSegment(self,length,isSolid):
  """ AppendSegment(self: Linetype,length: float,isSolid: bool) -> int """
  pass
 def CommitChanges(self):
  """ CommitChanges(self: Linetype) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Default(self):
  """ Default(self: Linetype) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetSegment(self,index,length,isSolid):
  """ GetSegment(self: Linetype,index: int) -> (float,bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def RemoveSegment(self,index):
  """ RemoveSegment(self: Linetype,index: int) -> bool """
  pass
 def SetSegment(self,index,length,isSolid):
  """ SetSegment(self: Linetype,index: int,length: float,isSolid: bool) -> bool """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: Linetype) -> Guid

Set: Id(self: Linetype)=value
"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDeleted(self: Linetype) -> bool

"""

 IsModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsModified(self: Linetype) -> bool

"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReference(self: Linetype) -> bool

"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LinetypeIndex(self: Linetype) -> int

Set: LinetypeIndex(self: Linetype)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Linetype) -> str

Set: Name(self: Linetype)=value
"""

 PatternLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PatternLength(self: Linetype) -> float

"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SegmentCount(self: Linetype) -> int

"""



class Material(CommonObject,IDisposable,ISerializable):
 """ Material() """
 def CommitChanges(self):
  """ CommitChanges(self: Material) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Default(self):
  """ Default(self: Material) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
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
 def GetUserString(self,key):
  """ GetUserString(self: Material,key: str) -> str """
  pass
 def GetUserStrings(self):
  """ GetUserStrings(self: Material) -> NameValueCollection """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: Material) """
  pass
 def SetBitmapTexture(self,*__args):
  """
  SetBitmapTexture(self: Material,texture: Texture) -> bool
  SetBitmapTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetBumpTexture(self,*__args):
  """
  SetBumpTexture(self: Material,texture: Texture) -> bool
  SetBumpTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetEnvironmentTexture(self,*__args):
  """
  SetEnvironmentTexture(self: Material,texture: Texture) -> bool
  SetEnvironmentTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetTransparencyTexture(self,*__args):
  """
  SetTransparencyTexture(self: Material,texture: Texture) -> bool
  SetTransparencyTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetUserString(self,key,value):
  """ SetUserString(self: Material,key: str,value: str) -> bool """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AmbientColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AmbientColor(self: Material) -> Color

Set: AmbientColor(self: Material)=value
"""

 DiffuseColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DiffuseColor(self: Material) -> Color

Set: DiffuseColor(self: Material)=value
"""

 EmissionColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EmissionColor(self: Material) -> Color

Set: EmissionColor(self: Material)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: Material) -> Guid

"""

 IndexOfRefraction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IndexOfRefraction(self: Material) -> float

Set: IndexOfRefraction(self: Material)=value
"""

 IsDefaultMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDefaultMaterial(self: Material) -> bool

"""

 MaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialIndex(self: Material) -> int

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Material) -> str

Set: Name(self: Material)=value
"""

 ReflectionColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReflectionColor(self: Material) -> Color

Set: ReflectionColor(self: Material)=value
"""

 Reflectivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Reflectivity(self: Material) -> float

Set: Reflectivity(self: Material)=value
"""

 RenderPlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RenderPlugInId(self: Material) -> Guid

Set: RenderPlugInId(self: Material)=value
"""

 Shine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Shine(self: Material) -> float

Set: Shine(self: Material)=value
"""

 SpecularColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SpecularColor(self: Material) -> Color

Set: SpecularColor(self: Material)=value
"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Transparency(self: Material) -> float

Set: Transparency(self: Material)=value
"""

 TransparentColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransparentColor(self: Material) -> Color

Set: TransparentColor(self: Material)=value
"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: Material) -> int

"""


 MaxShine=255.0


class MaterialRef(object,IDisposable):
 # no doc
 def Dispose(self):
  """ Dispose(self: MaterialRef) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BackFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackFaceMaterialId(self: MaterialRef) -> Guid

"""

 BackFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackFaceMaterialIndex(self: MaterialRef) -> int

"""

 FrontFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrontFaceMaterialId(self: MaterialRef) -> Guid

"""

 FrontFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrontFaceMaterialIndex(self: MaterialRef) -> int

"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialSource(self: MaterialRef) -> ObjectMaterialSource

"""

 PlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlugInId(self: MaterialRef) -> Guid

"""



class MaterialRefCreateParams(object):
 """ MaterialRefCreateParams() """
 BackFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: BackFaceMaterialId(self: MaterialRefCreateParams)=value
"""

 BackFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: BackFaceMaterialIndex(self: MaterialRefCreateParams)=value
"""

 FrontFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrontFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: FrontFaceMaterialId(self: MaterialRefCreateParams)=value
"""

 FrontFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrontFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: FrontFaceMaterialIndex(self: MaterialRefCreateParams)=value
"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialSource(self: MaterialRefCreateParams) -> ObjectMaterialSource

Set: MaterialSource(self: MaterialRefCreateParams)=value
"""

 PlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlugInId(self: MaterialRefCreateParams) -> Guid

Set: PlugInId(self: MaterialRefCreateParams)=value
"""



class MaterialRefs(object,IDictionary[Guid,MaterialRef],ICollection[KeyValuePair[Guid,MaterialRef]],IEnumerable[KeyValuePair[Guid,MaterialRef]],IEnumerable):
 # no doc
 def Add(self,*__args):
  """ Add(self: MaterialRefs,key: Guid,value: MaterialRef)Add(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef]) """
  pass
 def Clear(self):
  """ Clear(self: MaterialRefs) """
  pass
 def Contains(self,item):
  """ Contains(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef]) -> bool """
  pass
 def ContainsKey(self,key):
  """ ContainsKey(self: MaterialRefs,key: Guid) -> bool """
  pass
 def CopyTo(self,array,arrayIndex):
  """ CopyTo(self: MaterialRefs,array: Array[KeyValuePair[Guid,MaterialRef]],arrayIndex: int) """
  pass
 def Create(self,createParams):
  """ Create(self: MaterialRefs,createParams: MaterialRefCreateParams) -> MaterialRef """
  pass
 def GetEnumerator(self):
  """ GetEnumerator(self: MaterialRefs) -> IEnumerator[KeyValuePair[Guid,MaterialRef]] """
  pass
 def Remove(self,*__args):
  """
  Remove(self: MaterialRefs,key: Guid) -> bool
  Remove(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef]) -> bool
  """
  pass
 def TryGetValue(self,key,value):
  """ TryGetValue(self: MaterialRefs,key: Guid) -> (bool,MaterialRef) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__(self: IDictionary[Guid,MaterialRef],key: Guid) -> bool """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Count(self: MaterialRefs) -> int

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReadOnly(self: MaterialRefs) -> bool

"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Keys(self: MaterialRefs) -> ICollection[Guid]

"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Values(self: MaterialRefs) -> ICollection[MaterialRef]

"""



class ObjectAttributes(CommonObject,IDisposable,ISerializable):
 """ ObjectAttributes() """
 def AddToGroup(self,groupIndex):
  """ AddToGroup(self: ObjectAttributes,groupIndex: int) """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def Duplicate(self):
  """ Duplicate(self: ObjectAttributes) -> ObjectAttributes """
  pass
 def GetGroupList(self):
  """ GetGroupList(self: ObjectAttributes) -> Array[int] """
  pass
 def GetUserString(self,key):
  """ GetUserString(self: ObjectAttributes,key: str) -> str """
  pass
 def GetUserStrings(self):
  """ GetUserStrings(self: ObjectAttributes) -> NameValueCollection """
  pass
 def HasDisplayModeOverride(self,viewportId):
  """ HasDisplayModeOverride(self: ObjectAttributes,viewportId: Guid) -> bool """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def RemoveDisplayModeOverride(self,rhinoViewportId=None):
  """ RemoveDisplayModeOverride(self: ObjectAttributes,rhinoViewportId: Guid)RemoveDisplayModeOverride(self: ObjectAttributes) """
  pass
 def RemoveFromAllGroups(self):
  """ RemoveFromAllGroups(self: ObjectAttributes) """
  pass
 def RemoveFromGroup(self,groupIndex):
  """ RemoveFromGroup(self: ObjectAttributes,groupIndex: int) """
  pass
 def SetUserString(self,key,value):
  """ SetUserString(self: ObjectAttributes,key: str,value: str) -> bool """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 ColorSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ColorSource(self: ObjectAttributes) -> ObjectColorSource

Set: ColorSource(self: ObjectAttributes)=value
"""

 GroupCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GroupCount(self: ObjectAttributes) -> int

"""

 HasMapping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasMapping(self: ObjectAttributes) -> bool

"""

 IsInstanceDefinitionObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsInstanceDefinitionObject(self: ObjectAttributes) -> bool

"""

 LayerIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LayerIndex(self: ObjectAttributes) -> int

Set: LayerIndex(self: ObjectAttributes)=value
"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LinetypeIndex(self: ObjectAttributes) -> int

Set: LinetypeIndex(self: ObjectAttributes)=value
"""

 LinetypeSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LinetypeSource(self: ObjectAttributes) -> ObjectLinetypeSource

Set: LinetypeSource(self: ObjectAttributes)=value
"""

 MaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialIndex(self: ObjectAttributes) -> int

Set: MaterialIndex(self: ObjectAttributes)=value
"""

 MaterialRefs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialRefs(self: ObjectAttributes) -> MaterialRefs

"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaterialSource(self: ObjectAttributes) -> ObjectMaterialSource

Set: MaterialSource(self: ObjectAttributes)=value
"""

 Mode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Mode(self: ObjectAttributes) -> ObjectMode

Set: Mode(self: ObjectAttributes)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ObjectAttributes) -> str

Set: Name(self: ObjectAttributes)=value
"""

 ObjectColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectColor(self: ObjectAttributes) -> Color

Set: ObjectColor(self: ObjectAttributes)=value
"""

 ObjectDecoration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectDecoration(self: ObjectAttributes) -> ObjectDecoration

Set: ObjectDecoration(self: ObjectAttributes)=value
"""

 ObjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectId(self: ObjectAttributes) -> Guid

Set: ObjectId(self: ObjectAttributes)=value
"""

 PlotColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotColor(self: ObjectAttributes) -> Color

Set: PlotColor(self: ObjectAttributes)=value
"""

 PlotColorSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotColorSource(self: ObjectAttributes) -> ObjectPlotColorSource

Set: PlotColorSource(self: ObjectAttributes)=value
"""

 PlotWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotWeight(self: ObjectAttributes) -> float

Set: PlotWeight(self: ObjectAttributes)=value
"""

 PlotWeightSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotWeightSource(self: ObjectAttributes) -> ObjectPlotWeightSource

Set: PlotWeightSource(self: ObjectAttributes)=value
"""

 Space=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Space(self: ObjectAttributes) -> ActiveSpace

Set: Space(self: ObjectAttributes)=value
"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: ObjectAttributes) -> int

"""

 ViewportId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ViewportId(self: ObjectAttributes) -> Guid

Set: ViewportId(self: ObjectAttributes)=value
"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Visible(self: ObjectAttributes) -> bool

Set: Visible(self: ObjectAttributes)=value
"""

 WireDensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WireDensity(self: ObjectAttributes) -> int

Set: WireDensity(self: ObjectAttributes)=value
"""



class ObjectColorSource(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectColorSource,values: ColorFromLayer (0),ColorFromMaterial (2),ColorFromObject (1),ColorFromParent (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ColorFromLayer=None
 ColorFromMaterial=None
 ColorFromObject=None
 ColorFromParent=None
 value__=None


class ObjectDecoration(Enum,IComparable,IFormattable,IConvertible):
 """ enum (flags) ObjectDecoration,values: BothArrowhead (24),EndArrowhead (16),None (0),StartArrowhead (8) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 BothArrowhead=None
 EndArrowhead=None
 None=None
 StartArrowhead=None
 value__=None


class ObjectLinetypeSource(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectLinetypeSource,values: LinetypeFromLayer (0),LinetypeFromObject (1),LinetypeFromParent (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 LinetypeFromLayer=None
 LinetypeFromObject=None
 LinetypeFromParent=None
 value__=None


class ObjectMaterialSource(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectMaterialSource,values: MaterialFromLayer (0),MaterialFromObject (1),MaterialFromParent (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 MaterialFromLayer=None
 MaterialFromObject=None
 MaterialFromParent=None
 value__=None


class ObjectMode(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectMode,values: Hidden (1),InstanceDefinitionObject (3),Locked (2),Normal (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Hidden=None
 InstanceDefinitionObject=None
 Locked=None
 Normal=None
 value__=None


class ObjectPlotColorSource(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectPlotColorSource,values: PlotColorFromDisplay (2),PlotColorFromLayer (0),PlotColorFromObject (1),PlotColorFromParent (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 PlotColorFromDisplay=None
 PlotColorFromLayer=None
 PlotColorFromObject=None
 PlotColorFromParent=None
 value__=None


class ObjectPlotWeightSource(Enum,IComparable,IFormattable,IConvertible):
 """ enum ObjectPlotWeightSource,values: PlotWeightFromLayer (0),PlotWeightFromObject (1),PlotWeightFromParent (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 PlotWeightFromLayer=None
 PlotWeightFromObject=None
 PlotWeightFromParent=None
 value__=None


class ObjectType(Enum,IComparable,IFormattable,IConvertible):
 """ enum (flags) ObjectType,values: Annotation (512),AnyObject (4294967295),Brep (16),BrepLoop (524288),Cage (134217728),ClipPlane (536870912),Curve (4),Detail (32768),EdgeFilter (4194304),Extrusion (1073741824),Grip (16384),Hatch (65536),InstanceDefinition (2048),InstanceReference (4096),Light (256),Mesh (32),MeshEdge (33554432),MeshFace (67108864),MeshVertex (16777216),MorphControl (131072),None (0),Phantom (268435456),Point (1),PointSet (2),PolyedgeFilter (8388608),PolysrfFilter (2097152),Surface (8),TextDot (8192) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Annotation=None
 AnyObject=None
 Brep=None
 BrepLoop=None
 Cage=None
 ClipPlane=None
 Curve=None
 Detail=None
 EdgeFilter=None
 Extrusion=None
 Grip=None
 Hatch=None
 InstanceDefinition=None
 InstanceReference=None
 Light=None
 Mesh=None
 MeshEdge=None
 MeshFace=None
 MeshVertex=None
 MorphControl=None
 None=None
 Phantom=None
 Point=None
 PointSet=None
 PolyedgeFilter=None
 PolysrfFilter=None
 Surface=None
 TextDot=None
 value__=None


class SelectionMethod(Enum,IComparable,IFormattable,IConvertible):
 """ enum SelectionMethod,values: CrossingBox (3),MousePick (1),Other (0),WindowBox (2) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 CrossingBox=None
 MousePick=None
 Other=None
 value__=None
 WindowBox=None


class TextDisplayAlignment(Enum,IComparable,IFormattable,IConvertible):
 """ enum TextDisplayAlignment,values: AboveLine (2),Horizontal (1),InLine (3),Normal (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AboveLine=None
 Horizontal=None
 InLine=None
 Normal=None
 value__=None


class Texture(CommonObject,IDisposable,ISerializable):
 """ Texture() """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def GetAlphaBlendValues(self,constant,a0,a1,a2,a3):
  """ GetAlphaBlendValues(self: Texture) -> (float,float,float,float,float) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: CommonObject) """
  pass
 def SetAlphaBlendValues(self,constant,a0,a1,a2,a3):
  """ SetAlphaBlendValues(self: Texture,constant: float,a0: float,a1: float,a2: float,a3: float) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 ApplyUvwTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ApplyUvwTransform(self: Texture) -> bool

Set: ApplyUvwTransform(self: Texture)=value
"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Enabled(self: Texture) -> bool

Set: Enabled(self: Texture)=value
"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FileName(self: Texture) -> str

Set: FileName(self: Texture)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: Texture) -> Guid

"""

 MappingChannelId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MappingChannelId(self: Texture) -> int

"""

 TextureCombineMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextureCombineMode(self: Texture) -> TextureCombineMode

Set: TextureCombineMode(self: Texture)=value
"""

 TextureType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextureType(self: Texture) -> TextureType

Set: TextureType(self: Texture)=value
"""

 UvwTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UvwTransform(self: Texture) -> Transform

Set: UvwTransform(self: Texture)=value
"""

 WrapU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WrapU(self: Texture) -> TextureUvwWrapping

Set: WrapU(self: Texture)=value
"""

 WrapV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WrapV(self: Texture) -> TextureUvwWrapping

Set: WrapV(self: Texture)=value
"""

 WrapW=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WrapW(self: Texture) -> TextureUvwWrapping

Set: WrapW(self: Texture)=value
"""



class TextureCombineMode(Enum,IComparable,IFormattable,IConvertible):
 """ enum TextureCombineMode,values: Blend (3),Decal (2),Modulate (1),None (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Blend=None
 Decal=None
 Modulate=None
 None=None
 value__=None


class TextureType(Enum,IComparable,IFormattable,IConvertible):
 """ enum TextureType,values: Bitmap (1),Bump (2),None (0),Transparency (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Bitmap=None
 Bump=None
 None=None
 Transparency=None
 value__=None


class TextureUvwWrapping(Enum,IComparable,IFormattable,IConvertible):
 """ enum TextureUvwWrapping,values: Clamp (1),Repeat (0) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Clamp=None
 Repeat=None
 value__=None


class ViewInfo(object,IDisposable):
 # no doc
 def Dispose(self):
  """ Dispose(self: ViewInfo) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ViewInfo) -> str

Set: Name(self: ViewInfo)=value
"""

 Viewport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Viewport(self: ViewInfo) -> ViewportInfo

"""



class ViewportInfo(object,IDisposable,ISerializable):
 """
 ViewportInfo()
 ViewportInfo(other: ViewportInfo)
 """
 def ChangeToParallelProjection(self,symmetricFrustum):
  """ ChangeToParallelProjection(self: ViewportInfo,symmetricFrustum: bool) -> bool """
  pass
 def ChangeToPerspectiveProjection(self,targetDistance,symmetricFrustum,lensLength):
  """ ChangeToPerspectiveProjection(self: ViewportInfo,targetDistance: float,symmetricFrustum: bool,lensLength: float) -> bool """
  pass
 def ChangeToSymmetricFrustum(self,isLeftRightSymmetric,isTopBottomSymmetric,targetDistance):
  """ ChangeToSymmetricFrustum(self: ViewportInfo,isLeftRightSymmetric: bool,isTopBottomSymmetric: bool,targetDistance: float) -> bool """
  pass
 def ChangeToTwoPointPerspectiveProjection(self,targetDistance,up,lensLength):
  """ ChangeToTwoPointPerspectiveProjection(self: ViewportInfo,targetDistance: float,up: Vector3d,lensLength: float) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: ViewportInfo) """
  pass
 def DollyCamera(self,dollyVector):
  """ DollyCamera(self: ViewportInfo,dollyVector: Vector3d) -> bool """
  pass
 def DollyExtents(self,*__args):
  """
  DollyExtents(self: ViewportInfo,cameraCoordinateBoundingBox: BoundingBox,border: float) -> bool
  DollyExtents(self: ViewportInfo,geometry: IEnumerable[GeometryBase],border: float) -> bool
  """
  pass
 def DollyFrustum(self,dollyDistance):
  """ DollyFrustum(self: ViewportInfo,dollyDistance: float) -> bool """
  pass
 def Extents(self,halfViewAngleRadians,*__args):
  """
  Extents(self: ViewportInfo,halfViewAngleRadians: float,sphere: Sphere) -> bool
  Extents(self: ViewportInfo,halfViewAngleRadians: float,bbox: BoundingBox) -> bool
  """
  pass
 def FrustumCenterPoint(self,targetDistance):
  """ FrustumCenterPoint(self: ViewportInfo,targetDistance: float) -> Point3d """
  pass
 def GetBoundingBoxDepth(self,bbox,nearDistance,farDistance):
  """ GetBoundingBoxDepth(self: ViewportInfo,bbox: BoundingBox) -> (bool,float,float) """
  pass
 def GetCameraAngles(self,halfDiagonalAngleRadians,halfVerticalAngleRadians,halfHorizontalAngleRadians):
  """ GetCameraAngles(self: ViewportInfo) -> (bool,float,float,float) """
  pass
 def GetCameraFrame(self,location,cameraX,cameraY,cameraZ):
  """ GetCameraFrame(self: ViewportInfo) -> (bool,Point3d,Vector3d,Vector3d,Vector3d) """
  pass
 def GetDollyCameraVector(self,*__args):
  """
  GetDollyCameraVector(self: ViewportInfo,screen0: Point,screen1: Point,projectionPlaneDistance: float) -> Vector3d
  GetDollyCameraVector(self: ViewportInfo,screenX0: int,screenY0: int,screenX1: int,screenY1: int,projectionPlaneDistance: float) -> Vector3d
  """
  pass
 def GetFarPlaneCorners(self):
  """ GetFarPlaneCorners(self: ViewportInfo) -> Array[Point3d] """
  pass
 def GetFrustum(self,left,right,bottom,top,nearDistance,farDistance):
  """ GetFrustum(self: ViewportInfo) -> (bool,float,float,float,float,float,float) """
  pass
 def GetFrustumLine(self,*__args):
  """
  GetFrustumLine(self: ViewportInfo,screenPoint: PointF) -> Line
  GetFrustumLine(self: ViewportInfo,screenPoint: Point) -> Line
  GetFrustumLine(self: ViewportInfo,screenX: float,screenY: float) -> Line
  """
  pass
 def GetNearPlaneCorners(self):
  """ GetNearPlaneCorners(self: ViewportInfo) -> Array[Point3d] """
  pass
 def GetObjectData(self,info,context):
  """ GetObjectData(self: ViewportInfo,info: SerializationInfo,context: StreamingContext) """
  pass
 def GetPointDepth(self,point,distance):
  """ GetPointDepth(self: ViewportInfo,point: Point3d) -> (bool,float) """
  pass
 def GetScreenPort(self,near=None,far=None):
  """
  GetScreenPort(self: ViewportInfo) -> Rectangle
  GetScreenPort(self: ViewportInfo) -> (Rectangle,int,int)
  """
  pass
 def GetSphereDepth(self,sphere,nearDistance,farDistance):
  """ GetSphereDepth(self: ViewportInfo,sphere: Sphere) -> (bool,float,float) """
  pass
 def GetWorldToScreenScale(self,pointInFrustum):
  """ GetWorldToScreenScale(self: ViewportInfo,pointInFrustum: Point3d) -> float """
  pass
 def GetXform(self,sourceSystem,destinationSystem):
  """ GetXform(self: ViewportInfo,sourceSystem: CoordinateSystem,destinationSystem: CoordinateSystem) -> Transform """
  pass
 def SetCameraDirection(self,direction):
  """ SetCameraDirection(self: ViewportInfo,direction: Vector3d) -> bool """
  pass
 def SetCameraLocation(self,location):
  """ SetCameraLocation(self: ViewportInfo,location: Point3d) -> bool """
  pass
 def SetCameraUp(self,up):
  """ SetCameraUp(self: ViewportInfo,up: Vector3d) -> bool """
  pass
 def SetFrustum(self,left,right,bottom,top,nearDistance,farDistance):
  """ SetFrustum(self: ViewportInfo,left: float,right: float,bottom: float,top: float,nearDistance: float,farDistance: float) -> bool """
  pass
 def SetFrustumNearFar(self,*__args):
  """
  SetFrustumNearFar(self: ViewportInfo,nearDistance: float,farDistance: float) -> bool
  SetFrustumNearFar(self: ViewportInfo,nearDistance: float,farDistance: float,minNearDistance: float,minNearOverFar: float,targetDistance: float) -> bool
  SetFrustumNearFar(self: ViewportInfo,boundingBox: BoundingBox) -> bool
  SetFrustumNearFar(self: ViewportInfo,center: Point3d,radius: float) -> bool
  """
  pass
 def SetScreenPort(self,*__args):
  """
  SetScreenPort(self: ViewportInfo,windowRectangle: Rectangle) -> bool
  SetScreenPort(self: ViewportInfo,windowRectangle: Rectangle,near: int,far: int) -> bool
  SetScreenPort(self: ViewportInfo,left: int,right: int,bottom: int,top: int,near: int,far: int) -> bool
  """
  pass
 def TargetDistance(self,useFrustumCenterFallback):
  """ TargetDistance(self: ViewportInfo,useFrustumCenterFallback: bool) -> float """
  pass
 def UnlockCamera(self):
  """ UnlockCamera(self: ViewportInfo) """
  pass
 def UnlockFrustumSymmetry(self):
  """ UnlockFrustumSymmetry(self: ViewportInfo) """
  pass
 def ZoomToScreenRect(self,*__args):
  """
  ZoomToScreenRect(self: ViewportInfo,windowRectangle: Rectangle) -> bool
  ZoomToScreenRect(self: ViewportInfo,left: int,top: int,right: int,bottom: int) -> bool
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,other=None):
  """
  __new__(cls: type)
  __new__(cls: type,other: ViewportInfo)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Camera35mmLensLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Camera35mmLensLength(self: ViewportInfo) -> float

Set: Camera35mmLensLength(self: ViewportInfo)=value
"""

 CameraAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraAngle(self: ViewportInfo) -> float

Set: CameraAngle(self: ViewportInfo)=value
"""

 CameraDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraDirection(self: ViewportInfo) -> Vector3d

"""

 CameraLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraLocation(self: ViewportInfo) -> Point3d

"""

 CameraUp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraUp(self: ViewportInfo) -> Vector3d

"""

 CameraX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraX(self: ViewportInfo) -> Vector3d

"""

 CameraY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraY(self: ViewportInfo) -> Vector3d

"""

 CameraZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CameraZ(self: ViewportInfo) -> Vector3d

"""

 FrustumAspect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumAspect(self: ViewportInfo) -> float

Set: FrustumAspect(self: ViewportInfo)=value
"""

 FrustumBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumBottom(self: ViewportInfo) -> float

"""

 FrustumBottomPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumBottomPlane(self: ViewportInfo) -> Plane

"""

 FrustumCenter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumCenter(self: ViewportInfo) -> Point3d

"""

 FrustumFar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumFar(self: ViewportInfo) -> float

"""

 FrustumFarPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumFarPlane(self: ViewportInfo) -> Plane

"""

 FrustumHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumHeight(self: ViewportInfo) -> float

"""

 FrustumLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumLeft(self: ViewportInfo) -> float

"""

 FrustumLeftPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumLeftPlane(self: ViewportInfo) -> Plane

"""

 FrustumMaximumDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumMaximumDiameter(self: ViewportInfo) -> float

"""

 FrustumMinimumDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumMinimumDiameter(self: ViewportInfo) -> float

"""

 FrustumNear=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumNear(self: ViewportInfo) -> float

"""

 FrustumNearPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumNearPlane(self: ViewportInfo) -> Plane

"""

 FrustumRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumRight(self: ViewportInfo) -> float

"""

 FrustumRightPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumRightPlane(self: ViewportInfo) -> Plane

"""

 FrustumTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumTop(self: ViewportInfo) -> float

"""

 FrustumTopPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumTopPlane(self: ViewportInfo) -> Plane

"""

 FrustumWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FrustumWidth(self: ViewportInfo) -> float

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: ViewportInfo) -> Guid

"""

 IsCameraDirectionLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCameraDirectionLocked(self: ViewportInfo) -> bool

Set: IsCameraDirectionLocked(self: ViewportInfo)=value
"""

 IsCameraLocationLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCameraLocationLocked(self: ViewportInfo) -> bool

Set: IsCameraLocationLocked(self: ViewportInfo)=value
"""

 IsCameraUpLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCameraUpLocked(self: ViewportInfo) -> bool

Set: IsCameraUpLocked(self: ViewportInfo)=value
"""

 IsFrustumLeftRightSymmetric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsFrustumLeftRightSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumLeftRightSymmetric(self: ViewportInfo)=value
"""

 IsFrustumTopBottomSymmetric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsFrustumTopBottomSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumTopBottomSymmetric(self: ViewportInfo)=value
"""

 IsParallelProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsParallelProjection(self: ViewportInfo) -> bool

Set: IsParallelProjection(self: ViewportInfo)=value
"""

 IsPerspectiveProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsPerspectiveProjection(self: ViewportInfo) -> bool

Set: IsPerspectiveProjection(self: ViewportInfo)=value
"""

 IsTwoPointPerspectiveProjection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsTwoPointPerspectiveProjection(self: ViewportInfo) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: ViewportInfo) -> bool

"""

 IsValidCamera=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValidCamera(self: ViewportInfo) -> bool

"""

 IsValidFrustum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValidFrustum(self: ViewportInfo) -> bool

"""

 ScreenPortAspect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ScreenPortAspect(self: ViewportInfo) -> float

"""

 TargetPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TargetPoint(self: ViewportInfo) -> Point3d

Set: TargetPoint(self: ViewportInfo)=value
"""

 ViewScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ViewScale(self: ViewportInfo) -> SizeF

Set: ViewScale(self: ViewportInfo)=value
"""



# variables with complex values

