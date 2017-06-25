# encoding: utf-8
# module Autodesk.Revit.DB.Architecture calls itself Architecture
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BuildingPad(CeilingAndFloor, IDisposable):
    """ Represents a BuildingPad element. """
    @staticmethod
    def Create(document, buildingPadTypeId, levelId, curveLoops):
        """ Create(document: Document, buildingPadTypeId: ElementId, levelId: ElementId, curveLoops: IList[CurveLoop]) -> BuildingPad """
        pass

    def Dispose(self):
        """ Dispose(self: CeilingAndFloor, A_0: bool) """
        pass

    def GetBoundary(self):
        """
        GetBoundary(self: BuildingPad) -> IList[CurveLoop]
        
            Gets the boundary of current BuildingPad element.
            Returns: The curve loops that represent the boundary of the BuildingPad.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetBoundary(self, curveLoops):
        """ SetBoundary(self: BuildingPad, curveLoops: IList[CurveLoop]) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AssociatedTopographySurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of a topography surface created by the introduction of this building pad.

Get: AssociatedTopographySurfaceId(self: BuildingPad) -> ElementId

"""

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of the topography surface hosting this BuidlingPad.

Get: HostId(self: BuildingPad) -> ElementId

"""



class ContinuousRail(Element, IDisposable):
    """
    Represents a continuous rail element in Autodesk Revit.
       Type Data
       Misc Data
       Path and Profile Data
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetEndExtensionPath(self):
        """
        GetEndExtensionPath(self: ContinuousRail) -> IList[Curve]
        
            Retrieves the start extension path.
            Returns: The start extension path of the rail.
        """
        pass

    def GetPath(self):
        """
        GetPath(self: ContinuousRail) -> IList[Curve]
        
            Retrieves the rail path.
            Returns: The path of the rail.
        """
        pass

    def GetStartExtensionPath(self):
        """
        GetStartExtensionPath(self: ContinuousRail) -> IList[Curve]
        
            Retrieves the start extension path.
            Returns: The start extension path of the rail.
        """
        pass

    def GetSupports(self):
        """
        GetSupports(self: ContinuousRail) -> IList[ElementId]
        
            Returns all the railing supports attached to the rail.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HostRailingId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the host Railing that contains this rail.

Get: HostRailingId(self: ContinuousRail) -> ElementId

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the rail.

Get: Length(self: ContinuousRail) -> float

"""



class ContinuousRailType(ElementType, IDisposable):
    """ A type element containing the properties of a continuous rail. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultJoinOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default join option between two rails.

Get: DefaultJoinOption(self: ContinuousRailType) -> RailTypeDefaultJoinOption

Set: DefaultJoinOption(self: ContinuousRailType) = value
"""

    EndOrTopExtensionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension length of the rail termination at the end or top.

Get: EndOrTopExtensionLength(self: ContinuousRailType) -> float

Set: EndOrTopExtensionLength(self: ContinuousRailType) = value
"""

    EndOrTopExtensionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension style of the rail termination at the end or top.

Get: EndOrTopExtensionStyle(self: ContinuousRailType) -> RailExtensionStyle

Set: EndOrTopExtensionStyle(self: ContinuousRailType) = value
"""

    EndOrTopTermination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The termination of the rail at the end or top.

Get: EndOrTopTermination(self: ContinuousRailType) -> ElementId

Set: EndOrTopTermination(self: ContinuousRailType) = value
"""

    FilletRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fillet radius of the rail join.

Get: FilletRadius(self: ContinuousRailType) -> float

Set: FilletRadius(self: ContinuousRailType) = value
"""

    HandClearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The horizontal distance between the inner boundary of the rail and the path.

Get: HandClearance(self: ContinuousRailType) -> float

Set: HandClearance(self: ContinuousRailType) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the profile of the rail

Get: ProfileId(self: ContinuousRailType) -> ElementId

Set: ProfileId(self: ContinuousRailType) = value
"""

    Projection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The horizontal distance between the outer boundary of the rail and the path.

Get: Projection(self: ContinuousRailType) -> float

"""

    StartOrBottomExtensionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension length of the rail termination at the beginning or bottom.

Get: StartOrBottomExtensionLength(self: ContinuousRailType) -> float

Set: StartOrBottomExtensionLength(self: ContinuousRailType) = value
"""

    StartOrBottomExtensionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension style of the rail termination at the beginning or bottom.

Get: StartOrBottomExtensionStyle(self: ContinuousRailType) -> RailExtensionStyle

Set: StartOrBottomExtensionStyle(self: ContinuousRailType) = value
"""

    StartOrBottomTermination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The termination of the rail at the beginning or bottom.

Get: StartOrBottomTermination(self: ContinuousRailType) -> ElementId

Set: StartOrBottomTermination(self: ContinuousRailType) = value
"""

    Transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The transition option of the rail.

Get: Transition(self: ContinuousRailType) -> RailTransitionOption

Set: Transition(self: ContinuousRailType) = value
"""



class CutLineType(Enum, IComparable, IFormattable, IConvertible):
    """
    The available line types for a stairs cut line.
    
    enum CutLineType, values: DoubleLine (1), SingleLine (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoubleLine = None
    SingleLine = None
    value__ = None


class CutMarkSymbol(Enum, IComparable, IFormattable, IConvertible):
    """
    The available shapes for the cut mark symbol.
    
    enum CutMarkSymbol, values: Curve (2), None (0), Zigzag (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curve = None
    None = None
    value__ = None
    Zigzag = None


class CutMarkType(ElementType, IDisposable):
    """ An object represents the cut mark type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CutLineAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rotation angle of the cut mark.

Get: CutLineAngle(self: CutMarkType) -> float

Set: CutLineAngle(self: CutMarkType) = value
"""

    CutLineDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance between 2 cut lines.

Get: CutLineDistance(self: CutMarkType) -> float

Set: CutLineDistance(self: CutMarkType) = value
"""

    CutLineExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension distance to the boundary.

Get: CutLineExtension(self: CutMarkType) -> float

Set: CutLineExtension(self: CutMarkType) = value
"""

    CutLineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cut line type of the cut mark.

Get: CutLineType(self: CutMarkType) -> CutLineType

Set: CutLineType(self: CutMarkType) = value
"""

    CutMarkSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The symbol type of the cut mark.

Get: CutMarkSymbol(self: CutMarkType) -> CutMarkSymbol

Set: CutMarkSymbol(self: CutMarkType) = value
"""

    CutMarkSymbolSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the cut mark symbol.

Get: CutMarkSymbolSize(self: CutMarkType) -> float

Set: CutMarkSymbolSize(self: CutMarkType) = value
"""



class Fascia(HostedSweep, IDisposable):
    """ An object that represents a fascia within the Autodesk Revit project. """
    def AddSegment(self, targetRef):
        """
        AddSegment(self: Fascia, targetRef: Reference)
            Add segments to the fascia.
        
            targetRef: Segment's reference on which want to be added.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FasciaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves/set an object that represents the type of the Fascia.

Get: FasciaType(self: Fascia) -> FasciaType

Set: FasciaType(self: Fascia) = value
"""



class FasciaType(HostedSweepType, IDisposable):
    """
    An object that represents the fascia type
    in Autodesk Revit.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Gutter(HostedSweep, IDisposable):
    """ An object that represents a gutter within the Autodesk Revit project. """
    def AddSegment(self, targetRef):
        """
        AddSegment(self: Gutter, targetRef: Reference)
            Add segments to the gutter.
        
            targetRef: Segment's reference on which want to be added.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GutterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves/set an object that represents the type of the Gutter.

Get: GutterType(self: Gutter) -> GutterType

Set: GutterType(self: Gutter) = value
"""



class GutterType(HostedSweepType, IDisposable):
    """
    An object that represents the gutter type
    in Autodesk Revit.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class HandRail(ContinuousRail, IDisposable):
    """ Represents a hand rail element in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class HandRailPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    The position of the hand rail.
    
    enum HandRailPosition, values: Left (1), LeftAndRight (3), None (0), Right (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Left = None
    LeftAndRight = None
    None = None
    Right = None
    value__ = None


class HandRailType(ContinuousRailType, IDisposable):
    """ A rail type object that is used in the generation of hand rail. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the handrail.

Get: Height(self: HandRailType) -> float

Set: Height(self: HandRailType) = value
"""

    SupportJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The support justification method of the handrail.

Get: SupportJustification(self: HandRailType) -> RailSupportJustification

Set: SupportJustification(self: HandRailType) = value
"""

    SupportLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The support layout method of the handrail.

Get: SupportLayout(self: HandRailType) -> RailSupportsLayout

Set: SupportLayout(self: HandRailType) = value
"""

    SupportNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of supports of the handrail.

Get: SupportNumber(self: HandRailType) -> int

Set: SupportNumber(self: HandRailType) = value
"""

    SupportSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The support spacing of the handrail.

Get: SupportSpacing(self: HandRailType) -> float

Set: SupportSpacing(self: HandRailType) = value
"""

    SupportTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The support type of the handrail.

Get: SupportTypeId(self: HandRailType) -> ElementId

Set: SupportTypeId(self: HandRailType) = value
"""



class RailAngledJoinOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The angled joins of the rails.
    
    enum RailAngledJoinOption, values: AddVerticalOrHorizontalSegments (0), NoConnector (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AddVerticalOrHorizontalSegments = None
    NoConnector = None
    value__ = None


class RailConnectionOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The connections between rails.
    
    enum RailConnectionOption, values: Trim (0), Weld (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Trim = None
    value__ = None
    Weld = None


class RailExtensionStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    The extension style of the rail.
    
    enum RailExtensionStyle, values: Floor (2), None (0), Post (3), Wall (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Floor = None
    None = None
    Post = None
    value__ = None
    Wall = None


class RailIndex(Enum, IComparable, IFormattable, IConvertible):
    """
    The continuous rail position index.
    
    enum RailIndex, values: LeftPrimary (1), LeftSecondary (3), RightPrimary (2), RightSecondary (4), Top (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LeftPrimary = None
    LeftSecondary = None
    RightPrimary = None
    RightSecondary = None
    Top = None
    value__ = None


class Railing(Element, IDisposable):
    """ Represents a railing element in Autodesk Revit. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, stairsOrRampId: ElementId, railingTypeId: ElementId, placePosition: RailingPlacementPosition) -> ICollection[ElementId]
        
            Automatically creates new railings with the specified railing type on all sides 
             of a stairs or ramp element.
        
        
            document: The document.
            stairsOrRampId: The stairs or ramp to which the new railing will host.
           The stairs or ramp 
             should have no associated railings yet.
        
            railingTypeId: The railing type of the new railing is to be created.
            placePosition: The placement position of the new railing.
            Returns: The new railing instances successfully created on the stairs.
        Create(document: Document, curveLoop: CurveLoop, railingTypeId: ElementId, baseLevelId: ElementId) -> Railing
        
            Creates a new railing by specifying the railing path in the project document.
        
            document: The document.
            curveLoop: The railing path which the new railing will be created along with.
           The 
             curveLoop should be continuous with curves which are only bounded lines and 
             arcs on the same horizontal plane.
        
            railingTypeId: The railing type of the new railing is to be created.
            baseLevelId: The base level on which the new railing will be created.
            Returns: The new railing instance if creation was successful, otherwise ll.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Flip(self):
        """
        Flip(self: Railing)
            Flips the railing.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHandRails(self):
        """
        GetHandRails(self: Railing) -> IList[ElementId]
        
            Get all the handrails of the railing.
            Returns: All handrails of the railing.
        """
        pass

    def GetPath(self):
        """
        GetPath(self: Railing) -> IList[Curve]
        
            Gets the railing path.
            Returns: The curve array of the railing path.
        """
        pass

    @staticmethod
    def IsValidHostForNewRailing(document, elementId):
        """
        IsValidHostForNewRailing(document: Document, elementId: ElementId) -> bool
        
            Checks whether new railing can be created and placed on the specified host.
        
            document: The document.
            elementId: The element to check.
            Returns: True if new railing can be created and placed on the host, False otherwise.
        """
        pass

    def RailingCanBeHostedByElement(self, hostId):
        """
        RailingCanBeHostedByElement(self: Railing, hostId: ElementId) -> bool
        
            Checks whether the specified element can be used as a host for the railing.
           
             The host can be a stairs, ramp, floor, slab edge, wall or roof.
        
        
            hostId: Element id to check.
            Returns: True if the element can be used as host for the railing.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveHost(self):
        """
        RemoveHost(self: Railing)
            Removes the association between the railing and its host.
        """
        pass

    def Reset(self):
        """
        Reset(self: Railing)
            Resets the railing to the default one that the system generates.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPath(self, curveLoop):
        """
        SetPath(self: Railing, curveLoop: CurveLoop)
            Sets the railing path.
        
            curveLoop: The new curve array for the railing path.
           The curveLoop should be 
             continuous with curves which are only bounded lines and arcs on the same 
             horizontal plane.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanReset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the railing can be reset, False otherwise.

Get: CanReset(self: Railing) -> bool

"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the railing is flipped.

Get: Flipped(self: Railing) -> bool

"""

    HasHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the railing has a host.

Get: HasHost(self: Railing) -> bool

"""

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host of the railing.

Get: HostId(self: Railing) -> ElementId

Set: HostId(self: Railing) = value
"""

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the railing is the default one that system generates.

Get: IsDefault(self: Railing) -> bool

"""

    TopRail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top rail of the railing.

Get: TopRail(self: Railing) -> ElementId

"""



class RailingHeightCorrectionOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Railing height correction option.
    
    enum RailingHeightCorrectionOption, values: ByType (0), Custom (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ByType = None
    Custom = None
    value__ = None


class RailingPathCurveJoinOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The join type of the railing path.
    
    enum RailingPathCurveJoinOption, values: AddVerticalOrHorizontalSegments (2), ByType (0), ExtendRailsToMeet (1), NoConnector (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AddVerticalOrHorizontalSegments = None
    ByType = None
    ExtendRailsToMeet = None
    NoConnector = None
    value__ = None


class RailingPlacementPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Railing placement position.
    
    enum RailingPlacementPosition, values: Stringer (1), Treads (0), Undefined (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Stringer = None
    Treads = None
    Undefined = None
    value__ = None


class RailingSlopeOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The option determines the slope of the railing.
    
    enum RailingSlopeOption, values: ByHost (0), Flat (1), Sloped (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ByHost = None
    Flat = None
    Sloped = None
    value__ = None


class RailingType(ElementType, IDisposable):
    """ A railing type object that is used in the generation of railing. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PrimaryHandrailHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the primary handrail.

Get: PrimaryHandrailHeight(self: RailingType) -> float

"""

    PrimaryHandrailLateralOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lateral offset of the primary handrail.

Get: PrimaryHandrailLateralOffset(self: RailingType) -> float

"""

    PrimaryHandRailPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position of the primary handrail.

Get: PrimaryHandRailPosition(self: RailingType) -> HandRailPosition

Set: PrimaryHandRailPosition(self: RailingType) = value
"""

    PrimaryHandrailType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the primary handrail.

Get: PrimaryHandrailType(self: RailingType) -> ElementId

Set: PrimaryHandrailType(self: RailingType) = value
"""

    SecondaryHandrailHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the secondary handrail.

Get: SecondaryHandrailHeight(self: RailingType) -> float

"""

    SecondaryHandrailLateralOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lateral offset of the secondary handrail.

Get: SecondaryHandrailLateralOffset(self: RailingType) -> float

"""

    SecondaryHandRailPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position of the secondary handrail.

Get: SecondaryHandRailPosition(self: RailingType) -> HandRailPosition

Set: SecondaryHandRailPosition(self: RailingType) = value
"""

    SecondaryHandrailType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the secondary handrail.

Get: SecondaryHandrailType(self: RailingType) -> ElementId

Set: SecondaryHandrailType(self: RailingType) = value
"""

    TopRailHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the top rail in the railing system.

Get: TopRailHeight(self: RailingType) -> float

Set: TopRailHeight(self: RailingType) = value
"""

    TopRailType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the top rail in the railing system.

Get: TopRailType(self: RailingType) -> ElementId

Set: TopRailType(self: RailingType) = value
"""



class RailJoinOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The join type of the system rails.
    
    enum RailJoinOption, values: ByType (-1), Fillet (1), Miter (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ByType = None
    Fillet = None
    Miter = None
    value__ = None


class RailSupportJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    The justification of the rail supports.
    
    enum RailSupportJustification, values: Begin (0), Center (1), End (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Begin = None
    Center = None
    End = None
    value__ = None


class RailSupportsLayout(Enum, IComparable, IFormattable, IConvertible):
    """
    The layout of the rail supports.
    
    enum RailSupportsLayout, values: AlignWithRailingPosts (2), FixedDistance (1), FixedNumber (3), MaxSpacing (4), MinSpacing (5), None (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlignWithRailingPosts = None
    FixedDistance = None
    FixedNumber = None
    MaxSpacing = None
    MinSpacing = None
    None = None
    value__ = None


class RailTagentJoinOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The tangent joins of the rails.
    
    enum RailTagentJoinOption, values: AddVerticalOrHorizontalSegments (0), ExtendRailsToMeet (2), NoConnector (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AddVerticalOrHorizontalSegments = None
    ExtendRailsToMeet = None
    NoConnector = None
    value__ = None


class RailTransitionOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The transition type of the continuous rail.
    
    enum RailTransitionOption, values: Gooseneck (1), None (0), Simple (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Gooseneck = None
    None = None
    Simple = None
    value__ = None


class RailTypeDefaultJoinOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The default join type of the rail.
    
    enum RailTypeDefaultJoinOption, values: Fillet (1), Miter (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Fillet = None
    Miter = None
    value__ = None


class RiserToTreadConnectionOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the connection style of the riser and tread in relation to each other.
    
    enum RiserToTreadConnectionOption, values: JoinAll (2), RiserBehindTread (0), TreadUnderRiser (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    JoinAll = None
    RiserBehindTread = None
    TreadUnderRiser = None
    value__ = None


class Room(SpatialElement, IDisposable):
    """ Provides access to the room topology in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsPointInRoom(self, point):
        """
        IsPointInRoom(self: Room, point: XYZ) -> bool
        
            Determines if a point lies within the volume of the room.
        
            point: Point to be checked.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def Unplace(self):
        """
        Unplace(self: Room)
            Remove the room from its location, but the project still contains the room.
        
             The room can be placed in another location after unplaced.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Base Offset of the Room.

Get: BaseOffset(self: Room) -> float

Set: BaseOffset(self: Room) = value
"""

    ClosedShell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the closedShell of the Room.

Get: ClosedShell(self: Room) -> GeometryElement

"""

    LimitOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Limit Offset of the Room.

Get: LimitOffset(self: Room) -> float

Set: LimitOffset(self: Room) = value
"""

    UnboundedHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Unbounded Height of the Room.

Get: UnboundedHeight(self: Room) -> float

"""

    UpperLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Upper Limit of the Room.

Get: UpperLimit(self: Room) -> Level

Set: UpperLimit(self: Room) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Volume of the Room.

Get: Volume(self: Room) -> float

"""



class RoomFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match rooms.
    
    RoomFilter()
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RoomTag(SpatialElementTag, IDisposable):
    """ Provides access to the room tag in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsInRoom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the tag is lockated in a room.

Get: IsInRoom(self: RoomTag) -> bool

"""

    Room = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The room that the tag is associated with.

Get: Room(self: RoomTag) -> Room

"""

    RoomTagType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tag type.

Get: RoomTagType(self: RoomTag) -> RoomTagType

Set: RoomTagType(self: RoomTag) = value
"""

    TaggedLocalRoomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the tagged room.

Get: TaggedLocalRoomId(self: RoomTag) -> ElementId

"""

    TaggedRoomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The LinkElementId of the tagged room.

Get: TaggedRoomId(self: RoomTag) -> LinkElementId

"""



class RoomTagFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match room tags.
    
    RoomTagFilter()
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RoomTagType(FamilySymbol, IDisposable):
    """ An object that represents a Room Tag type. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SiteSubRegion(object, IDisposable):
    """ Represents a proxy class exposing the interfaces needed to access details of a subregion. """
    @staticmethod
    def Create(document, curveLoops, hostTopoSurfaceId=None):
        """
        Create(document: Document, curveLoops: IList[CurveLoop]) -> SiteSubRegion
        Create(document: Document, curveLoops: IList[CurveLoop], hostTopoSurfaceId: ElementId) -> SiteSubRegion
        """
        pass

    def Dispose(self):
        """ Dispose(self: SiteSubRegion) """
        pass

    def GetBoundary(self):
        """
        GetBoundary(self: SiteSubRegion) -> IList[CurveLoop]
        
            Gets the boundary of current subregion.
            Returns: The curve loops that represent the boundary.
        """
        pass

    @staticmethod
    def IsValidBoundary(curveLoops):
        """ IsValidBoundary(curveLoops: IList[CurveLoop]) -> bool """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SiteSubRegion, disposing: bool) """
        pass

    def SetBoundary(self, curveLoops):
        """ SetBoundary(self: SiteSubRegion, curveLoops: IList[CurveLoop]) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of the topography surface hosting this SiteSubRegion.

Get: HostId(self: SiteSubRegion) -> ElementId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SiteSubRegion) -> bool

"""

    TopographySurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The TopographySurface element which this SiteSubRegion represents.

Get: TopographySurface(self: SiteSubRegion) -> TopographySurface

"""



class SketchedCurveSlopeOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The option determines the slop of the sketched run/landing.
    
    enum SketchedCurveSlopeOption, values: Auto (0), Flat (1), Sloped (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Auto = None
    Flat = None
    Sloped = None
    value__ = None


class Stairs(Element, IDisposable):
    """ Represents a stairs element in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAssociatedRailings(self):
        """
        GetAssociatedRailings(self: Stairs) -> ICollection[ElementId]
        
            Gets a list of the Railing elements which are associated to the boundaries of 
             the stairs.
        
            Returns: The ids of the Railing elements.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetStairsLandings(self):
        """
        GetStairsLandings(self: Stairs) -> ICollection[ElementId]
        
            Returns all the stairs landing components in the stairs.
            Returns: The stairs landing components in the stairs.
        """
        pass

    def GetStairsRuns(self):
        """
        GetStairsRuns(self: Stairs) -> ICollection[ElementId]
        
            Returns all the stairs run components in the stairs.
            Returns: The stairs run components in the stairs.
        """
        pass

    def GetStairsSupports(self):
        """
        GetStairsSupports(self: Stairs) -> ICollection[ElementId]
        
            Returns all the stairs support components in the stairs.
        """
        pass

    @staticmethod
    def IsByComponent(document, stairsId):
        """
        IsByComponent(document: Document, stairsId: ElementId) -> bool
        
            Indicates if the stairs is created by stairs components(runs, landings and 
             supports).
        
        
            document: The document.
            stairsId: The stairs element to check.
            Returns: True if the stairs is created by components, False otherwise.
        """
        pass

    def IsInEditMode(self):
        """
        IsInEditMode(self: Stairs) -> bool
        
            Indicates whether the stairs is in edit mode or not.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualRiserHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual height of the stairs risers in the stairs.

Get: ActualRiserHeight(self: Stairs) -> float

"""

    ActualRisersNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of actually created risers in model.

Get: ActualRisersNumber(self: Stairs) -> int

"""

    ActualTreadDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual depth of the stairs treads in the stairs, actual tread depth is equal to minimum tread depth by default.

Get: ActualTreadDepth(self: Stairs) -> float

Set: ActualTreadDepth(self: Stairs) = value
"""

    ActualTreadsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of treads actually created in the stairs.

Get: ActualTreadsNumber(self: Stairs) -> int

"""

    BaseElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base elevation of the stairs.

Get: BaseElevation(self: Stairs) -> float

"""

    DesiredRisersNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of risers is calculated based on the height between levels.

Get: DesiredRisersNumber(self: Stairs) -> int

Set: DesiredRisersNumber(self: Stairs) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the stair between the base and top levels.

Get: Height(self: Stairs) -> float

Set: Height(self: Stairs) = value
"""

    NumberOfStories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of stories of a multi-story stair, or 1 for a single-story stair.

Get: NumberOfStories(self: Stairs) -> int

"""

    TopElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top elevation of the stairs.

Get: TopElevation(self: Stairs) -> float

"""



class StairsComponentConnection(object, IDisposable):
    """ Represents information about a connection among stairs components(run to landing). """
    def Dispose(self):
        """ Dispose(self: StairsComponentConnection) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StairsComponentConnection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ConnectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connection type of the connected stairs component.

Get: ConnectionType(self: StairsComponentConnection) -> StairsComponentConnectionEndType

"""

    ElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element Id of connected stairs component in the stairs connection.

Get: ElementId(self: StairsComponentConnection) -> ElementId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StairsComponentConnection) -> bool

"""

    PeerConnectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connection type of the peer connected stairs component.

Get: PeerConnectionType(self: StairsComponentConnection) -> StairsComponentConnectionEndType

"""

    PeerElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element Id of peer connected stairs component in the stairs connection.

Get: PeerElementId(self: StairsComponentConnection) -> ElementId

"""



class StairsComponentConnectionEndType(Enum, IComparable, IFormattable, IConvertible):
    """
    The end type identifying the connection type among stairs runs and landings.
    
    enum StairsComponentConnectionEndType, values: ET_Landing (0), ET_RunEnd (2), ET_RunStart (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ET_Landing = None
    ET_RunEnd = None
    ET_RunStart = None
    value__ = None


class StairsConstructionMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the construction method of the stairs.
    
    enum StairsConstructionMethod, values: Assembled (0), CastInPlace (1), Precast (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembled = None
    CastInPlace = None
    Precast = None
    value__ = None


class StairsEndConnectionType(Enum, IComparable, IFormattable, IConvertible):
    """
    The join style between a run and landing.
    
    enum StairsEndConnectionType, values: Notch (1), StraightCut (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Notch = None
    StraightCut = None
    value__ = None


class StairsEndNotchOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The style of notch width for the stairs.
    
    enum StairsEndNotchOption, values: Custom (1), FullRunWidth (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Custom = None
    FullRunWidth = None
    value__ = None


class StairsLanding(Element, IDisposable):
    """ An object that represents a stairs landing in Autodesk Revit. """
    @staticmethod
    def CanCreateAutomaticLanding(document, firstRunId, secondRunId):
        """
        CanCreateAutomaticLanding(document: Document, firstRunId: ElementId, secondRunId: ElementId) -> bool
        
            Checks whether automatic landing(s) can be created between the given two stairs 
             runs and
           logically join(s) with the stairs runs.
        
        
            document: The document that owns the stairs runs.
            firstRunId: The first stairs run.
            secondRunId: The second stairs run.
            Returns: True if automatic landing(s) can be created between the two stairs runs, False 
             otherwise.
        """
        pass

    @staticmethod
    def CreateAutomaticLanding(document, firstRunId, secondRunId):
        """
        CreateAutomaticLanding(document: Document, firstRunId: ElementId, secondRunId: ElementId) -> IList[ElementId]
        
            Creates automatic landing(s) between two stairs runs.
        
            document: The document that owns the stairs runs and new landing(s).
            firstRunId: The first stairs run.
            secondRunId: The second stairs run.
            Returns: The created landing(s) between the two stairs runs.
        """
        pass

    @staticmethod
    def CreateSketchedLanding(document, stairsId, curveLoop, baseElevation):
        """
        CreateSketchedLanding(document: Document, stairsId: ElementId, curveLoop: CurveLoop, baseElevation: float) -> StairsLanding
        
            Creates a customized landing between two runs by providing the closed boundary 
             curves of the landing.
        
        
            document: The document that owns the landing.
            stairsId: The stairs that the new sketched landing belongs to.
            curveLoop: The closed boundary curves of the new landing.
            baseElevation: Base elevation of the new stairs run. The elevation has following restriction:
        
                The base elevation is relative to the base elevation of the stairs.The base 
             elevation will be rounded automatically to a multiple of the riser height. The 
             base elevation should be equal to or greater than half of the riser height.
        
            Returns: The new sketched landing.
        """
        pass

    @staticmethod
    def CreateSketchedLandingWithSlopeData(document, stairsId, curveLoop, baseElevation):
        """ CreateSketchedLandingWithSlopeData(document: Document, stairsId: ElementId, curveLoop: IList[SketchedStairsCurveData], baseElevation: float) -> StairsLanding """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAllSupports(self):
        """
        GetAllSupports(self: StairsLanding) -> IList[ElementId]
        
            Returns all the supports hosting the stairs landing.
            Returns: All the supports hosting the stairs landings.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetConnections(self):
        """
        GetConnections(self: StairsLanding) -> IList[StairsComponentConnection]
        
            Returns information about the connections in which the stairs landing 
             participates.
        
            Returns: The connections in which the stairs landing participates.
        """
        pass

    def GetFootprintBoundary(self):
        """
        GetFootprintBoundary(self: StairsLanding) -> CurveLoop
        
            Returns the landing's boundary curves which are projected on the stairs base 
             level.
        
            Returns: The boundary curves of the landing.
        """
        pass

    def GetStairs(self):
        """
        GetStairs(self: StairsLanding) -> Stairs
        
            Returns the stairs to which the landing belongs.
            Returns: The stairs to which the landing belongs.
        """
        pass

    def GetStairsPath(self):
        """
        GetStairsPath(self: StairsLanding) -> CurveLoop
        
            Returns the stairs path curves on the landing. The curves are projected on the 
             stairs base level.
        
            Returns: The stairs path curves of the landing.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSketchedLandingBoundaryAndPath(self, document, boundaryCurveLoop, pathCurveLoop):
        """
        SetSketchedLandingBoundaryAndPath(self: StairsLanding, document: Document, boundaryCurveLoop: CurveLoop, pathCurveLoop: CurveLoop)
            Sets the boundary and path curves of the sketched landing.
        
            document: The document that owns the landing.
            boundaryCurveLoop: The closed boundary curves of the landing.
            pathCurveLoop: The path curves of the landing, can be an empty CurveLoop.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base elevation of the landing.

Get: BaseElevation(self: StairsLanding) -> float

Set: BaseElevation(self: StairsLanding) = value
"""

    IsAutomaticLanding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the landing is an automatic landing, False otherwise.

Get: IsAutomaticLanding(self: StairsLanding) -> bool

"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The thickness of the landing.

Get: Thickness(self: StairsLanding) -> float

"""



class StairsLandingType(ElementType, IDisposable):
    """ Represents a stairs landing type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsMonolithic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs landing is monolithic, false otherwise.

Get: IsMonolithic(self: StairsLandingType) -> bool

"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thickness of the stairs landing.

Get: Thickness(self: StairsLandingType) -> float

Set: Thickness(self: StairsLandingType) = value
"""



class StairsNumberSystemReferenceOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The reference types permitted for a number system to refer to the geometry of a stairs run.
    
    enum StairsNumberSystemReferenceOption, values: Center (0), Left (1), LeftQuarter (3), Right (2), RightQuarter (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Center = None
    Left = None
    LeftQuarter = None
    Right = None
    RightQuarter = None
    value__ = None


class StairsPath(Element, IDisposable):
    """ An object that represents the stairs path. """
    @staticmethod
    def Create(document, stairsId, typeId, planViewId):
        """
        Create(document: Document, stairsId: LinkElementId, typeId: ElementId, planViewId: ElementId) -> StairsPath
        
            Creates a new stairs path for the specified stairs with the specified stairs 
             path type only in the plan view.
        
        
            document: The document.
            stairsId: The id of the stairs element either in the host document or in a linked 
             document.
        
            typeId: The type of stairs path.
            planViewId: The plan view in which the stairs path will be shown.
            Returns: The new stairs path.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DownText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The stairs down text.

Get: DownText(self: StairsPath) -> str

Set: DownText(self: StairsPath) = value
"""

    DownTextOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of stairs down text.

Get: DownTextOffset(self: StairsPath) -> XYZ

Set: DownTextOffset(self: StairsPath) = value
"""

    ShowDownText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents whether show stairs down text or not.

Get: ShowDownText(self: StairsPath) -> bool

Set: ShowDownText(self: StairsPath) = value
"""

    ShowUpText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents whether show stairs up text or not.

Get: ShowUpText(self: StairsPath) -> bool

Set: ShowUpText(self: StairsPath) = value
"""

    StairsId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host stairs element id.

Get: StairsId(self: StairsPath) -> LinkElementId

"""

    StairsPathOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of stairs path to center line of stairs.

Get: StairsPathOffset(self: StairsPath) -> float

Set: StairsPathOffset(self: StairsPath) = value
"""

    TextOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The orientation of stair up and down text.

Get: TextOrientation(self: StairsPath) -> StairsTextOrientation

Set: TextOrientation(self: StairsPath) = value
"""

    UpText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The stairs up text.

Get: UpText(self: StairsPath) -> str

Set: UpText(self: StairsPath) = value
"""

    UpTextOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of stairs up text.

Get: UpTextOffset(self: StairsPath) -> XYZ

Set: UpTextOffset(self: StairsPath) = value
"""



class StairsPathDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    The direction style of stairs path.
    
    enum StairsPathDirection, values: AlwaysUp (0), AutomaticUpDown (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlwaysUp = None
    AutomaticUpDown = None
    value__ = None


class StairsPathLineShapeAtCorner(Enum, IComparable, IFormattable, IConvertible):
    """
    The options for the line shape of a stairs path at a corner.
    
    enum StairsPathLineShapeAtCorner, values: Curved (1), Straight (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Curved = None
    Straight = None
    value__ = None


class StairsPathType(ElementType, IDisposable):
    """ An object represents the stairs path type. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrowheadTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The arrow head type of the stairs path.

Get: ArrowheadTypeId(self: StairsPathType) -> ElementId

Set: ArrowheadTypeId(self: StairsPathType) = value
"""

    DistanceToCutMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the stairs path arrow to cut mark.

Get: DistanceToCutMark(self: StairsPathType) -> float

Set: DistanceToCutMark(self: StairsPathType) = value
"""

    DrawForEachRun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if stairs paths should be drawn for each run, false if it should be drawn for the whole stairs.

Get: DrawForEachRun(self: StairsPathType) -> bool

Set: DrawForEachRun(self: StairsPathType) = value
"""

    EndAtRiser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents whether the stairs path ends at the riser.

Get: EndAtRiser(self: StairsPathType) -> bool

Set: EndAtRiser(self: StairsPathType) = value
"""

    FullStepArrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the arrow fills the full step width, false if it fills by the specified arrow size.

Get: FullStepArrow(self: StairsPathType) -> bool

Set: FullStepArrow(self: StairsPathType) = value
"""

    LineShapeAtCorner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line shape of stairs path at the corner.

Get: LineShapeAtCorner(self: StairsPathType) -> StairsPathLineShapeAtCorner

Set: LineShapeAtCorner(self: StairsPathType) = value
"""

    ShowArrowheadToCutMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs path arrowhead should be shown to the cutmark, false if the arrow head is not shown.

Get: ShowArrowheadToCutMark(self: StairsPathType) -> bool

Set: ShowArrowheadToCutMark(self: StairsPathType) = value
"""

    StairsPathDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The style of the stairs path.

Get: StairsPathDirection(self: StairsPathType) -> StairsPathDirection

"""

    StartExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start extension length of the stairs path.

Get: StartExtension(self: StairsPathType) -> float

Set: StartExtension(self: StairsPathType) = value
"""

    StartFromRiser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs path starts from the riser, false if it starts from the tread.

Get: StartFromRiser(self: StairsPathType) -> bool

Set: StartFromRiser(self: StairsPathType) = value
"""

    StartSymbolTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start symbol type of stairs path.

Get: StartSymbolTypeId(self: StairsPathType) -> ElementId

Set: StartSymbolTypeId(self: StairsPathType) = value
"""



class StairsRun(Element, IDisposable):
    """ Represents a stairs run element in Autodesk Revit. """
    @staticmethod
    def CreateSketchedRun(document, stairsId, baseElevation, boundaryCurves, riserCurves, stairsPath):
        """ CreateSketchedRun(document: Document, stairsId: ElementId, baseElevation: float, boundaryCurves: IList[Curve], riserCurves: IList[Curve], stairsPath: IList[Curve]) -> StairsRun """
        pass

    @staticmethod
    def CreateSketchedRunWithSlopeData(document, stairsId, baseElevation, boundaryCurves, riserCurves, stairsPath):
        """ CreateSketchedRunWithSlopeData(document: Document, stairsId: ElementId, baseElevation: float, boundaryCurves: IList[SketchedStairsCurveData], riserCurves: IList[Curve], stairsPath: IList[Curve]) -> StairsRun """
        pass

    @staticmethod
    def CreateSpiralRun(document, stairsId, center, radius, startAngle, includedAngle, clockwise, justification):
        """
        CreateSpiralRun(document: Document, stairsId: ElementId, center: XYZ, radius: float, startAngle: float, includedAngle: float, clockwise: bool, justification: StairsRunJustification) -> StairsRun
        
            Creates a spiral run in the project document by providing the center, start 
             angle and included angle.
        
        
            document: The document.
            stairsId: The stairs that the new stairs run will belong to.
            center: The center of the location arc of the spiral run.
           The Z coordinate of the 
             center is the base elevation for the new run (in model coordinates).
           It 
             must be greater than or equal to the stairs base elevation.
        
            radius: The radius of the location arc of the spiral run.
            startAngle: The start angle of the location arc of the spiral run.
           The angle's 
             coordinate system is world coordinate system which always is XYZ.BasisX and 
             XYZ.BasisY.
        
            includedAngle: The total angle covered by the spiral run. Must be a positive value (direction 
             is determined by the clockwise flag).
        
            clockwise: True if the spiral run will be created along clockwise direction, False 
             otherwise.
        
            justification: The location path justification of the new stairs run.
            Returns: The new stairs run.
        """
        pass

    @staticmethod
    def CreateStraightRun(document, stairsId, locationPath, justification):
        """
        CreateStraightRun(document: Document, stairsId: ElementId, locationPath: Line, justification: StairsRunJustification) -> StairsRun
        
            Creates a straight run in the project document.
        
            document: The document.
            stairsId: The stairs that the new stairs run will belong to.
            locationPath: The line for location path of the new stairs run. The line has following 
             restriction:
           The line should be bound line which is parallel to the XY 
             plane.The Z coordinate of the line is the base elevation for the new run (in 
             model coordinates).
           It must be greater than or equal to the stairs base 
             elevation.The number of created risers will be calculated by rounding the 
             length of the
           location path to a multiple of the tread depth.
        
            justification: The location path justification of the new stairs run.
            Returns: The new stairs run.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAllSupports(self):
        """
        GetAllSupports(self: StairsRun) -> IList[ElementId]
        
            Retrieves all supports hosted by the stair's run.
            Returns: All supports hosted by the stair's run.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetConnections(self):
        """
        GetConnections(self: StairsRun) -> IList[StairsComponentConnection]
        
            Returns information about the connections in which the stairs run participates.
             
           The stairs run may have no connection, or have at maximum two connections 
             at the lower and upper ends.
        
            Returns: The connections in which the stairs run participates.
        """
        pass

    def GetFootprintBoundary(self):
        """
        GetFootprintBoundary(self: StairsRun) -> CurveLoop
        
            Returns the run's boundary curves which are projected on the stairs base level.
            Returns: The boundary curves of the stairs run.
        """
        pass

    def GetLeftSupports(self):
        """
        GetLeftSupports(self: StairsRun) -> IList[ElementId]
        
            Retrieves all supports on the left side of run boundaries.
            Returns: The supports on the left side of run boundaries.
        """
        pass

    def GetNumberSystemReference(self, referenceOption):
        """
        GetNumberSystemReference(self: StairsRun, referenceOption: StairsNumberSystemReferenceOption) -> Reference
        
            Gets the number system reference corresponding to the given reference options.
        
            referenceOption: The reference option.
            Returns: The reference.
        """
        pass

    def GetRightSupports(self):
        """
        GetRightSupports(self: StairsRun) -> IList[ElementId]
        
            Retrieves all supports on the right side of run boundaries.
            Returns: The supports on the right side of run boundaries.
        """
        pass

    def GetStairs(self):
        """
        GetStairs(self: StairsRun) -> Stairs
        
            Returns the stairs to which the stairs run belongs.
            Returns: The stairs to which the stairs run belongs.
        """
        pass

    def GetStairsPath(self):
        """
        GetStairsPath(self: StairsRun) -> CurveLoop
        
            Returns the stairs path curves on the run. The curves are projected on base 
             level of the stairs.
        
            Returns: The stairs path curves.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    @staticmethod
    def SetLocationPathForSpiralRun(stairsRun, center, radius, startAngle, includedAngle, clockwise, justification):
        """
        SetLocationPathForSpiralRun(stairsRun: StairsRun, center: XYZ, radius: float, startAngle: float, includedAngle: float, clockwise: bool, justification: StairsRunJustification) -> bool
        
            Set Location path for a spiral run.
        
            stairsRun: The run whose location path will be set.
            center: The center of the location arc of the spiral run.
           The Z coordinate of the 
             center is the base elevation for the new run (in model coordinates).
           It 
             must be greater than or equal to the stairs base elevation.
        
            radius: The radius of the location arc of the spiral run.
            startAngle: The start angle of the location arc of the spiral run.
           The angle's 
             coordinate system is world coordinate system which always is XYZ.BasisX and 
             XYZ.BasisY.
        
            includedAngle: The total angle covered by the spiral run. Must be a positive value (direction 
             is determined by the clockwise flag).
        
            clockwise: True if the spiral run will be created along clockwise direction, False 
             otherwise.
        
            justification: The location path justification of the new stairs run.
            Returns: Indicate if set is success or not.
        """
        pass

    @staticmethod
    def SetLocationPathForStraightRun(stairsRun, locationPath):
        """
        SetLocationPathForStraightRun(stairsRun: StairsRun, locationPath: Line) -> bool
        
            Set location path for a straight run by giving a line.
        
            stairsRun: The run whose location path will be set.
            locationPath: The location path.
            Returns: Indicate if set is success or not.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualRisersNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual number of stairs risers in the stairs run.

Get: ActualRisersNumber(self: StairsRun) -> int

"""

    ActualRunWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the value of the tread width excluding the width of independent side supports.

Get: ActualRunWidth(self: StairsRun) -> float

Set: ActualRunWidth(self: StairsRun) = value
"""

    ActualTreadsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual number of stairs treads in the stairs run.

Get: ActualTreadsNumber(self: StairsRun) -> int

"""

    BaseElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base elevation of the stairs run.

Get: BaseElevation(self: StairsRun) -> float

Set: BaseElevation(self: StairsRun) = value
"""

    BeginsWithRiser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs run begins with a riser, false otherwise.

Get: BeginsWithRiser(self: StairsRun) -> bool

Set: BeginsWithRiser(self: StairsRun) = value
"""

    EndsWithRiser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs run ends with a riser, false otherwise.

Get: EndsWithRiser(self: StairsRun) -> bool

Set: EndsWithRiser(self: StairsRun) = value
"""

    ExtensionBelowRiserBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies a value to extend/trim the run's first step against base elevation of the stairs if the stairs begins with a riser.

Get: ExtensionBelowRiserBase(self: StairsRun) -> float

Set: ExtensionBelowRiserBase(self: StairsRun) = value
"""

    ExtensionBelowTreadBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies a value to extend/trim the run's first step against base elevation of the stairs if the stairs begins with a tread.

Get: ExtensionBelowTreadBase(self: StairsRun) -> float

Set: ExtensionBelowTreadBase(self: StairsRun) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated height of the stairs run.

Get: Height(self: StairsRun) -> float

"""

    LocationLineJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position of the run relative to the Up-direction path used to create the run.

Get: LocationLineJustification(self: StairsRun) -> StairsRunJustification

Set: LocationLineJustification(self: StairsRun) = value
"""

    StairsRunStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The style of the stairs run such as straight, winder, etc.

Get: StairsRunStyle(self: StairsRun) -> StairsRunStyle

"""

    TopElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top elevation of the stairs run.

Get: TopElevation(self: StairsRun) -> float

Set: TopElevation(self: StairsRun) = value
"""



class StairsRunJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    The position of the run relative to the Up-direction path used to create the run.
    
    enum StairsRunJustification, values: Center (1), Left (0), LeftExterior (3), Right (2), RightExterior (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Center = None
    Left = None
    LeftExterior = None
    Right = None
    RightExterior = None
    value__ = None


class StairsRunStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    The shape of a run. Different shape has different ways of manipulation.
    
    enum StairsRunStyle, values: Sketched (2), Spiral (4), Straight (3), Winder (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Sketched = None
    Spiral = None
    Straight = None
    value__ = None
    Winder = None


class StairsRunType(ElementType, IDisposable):
    """ A stairs run type object that is used in the generation of stairs run. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasRisers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs run will include risers on steps, false otherwise.

Get: HasRisers(self: StairsRunType) -> bool

Set: HasRisers(self: StairsRunType) = value
"""

    HasTreads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs run will include treads on steps, false otherwise.

Get: HasTreads(self: StairsRunType) -> bool

Set: HasTreads(self: StairsRunType) = value
"""

    IsMonolithic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs run is monolithic, false otherwise.

Get: IsMonolithic(self: StairsRunType) -> bool

"""

    IsSlanted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if risers will be slanted, false if they will be straight.

Get: IsSlanted(self: StairsRunType) -> bool

Set: IsSlanted(self: StairsRunType) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The material of the stairs run, only available for monolithic stairs run.

Get: MaterialId(self: StairsRunType) -> ElementId

Set: MaterialId(self: StairsRunType) = value
"""

    NosingLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of the tread depth that overhangs the next tread.

Get: NosingLength(self: StairsRunType) -> float

Set: NosingLength(self: StairsRunType) = value
"""

    NosingProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the nosing profile of the treads.

Get: NosingProfile(self: StairsRunType) -> ElementId

Set: NosingProfile(self: StairsRunType) = value
"""

    RiserProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the profile of the risers.

Get: RiserProfile(self: StairsRunType) -> ElementId

Set: RiserProfile(self: StairsRunType) = value
"""

    RiserThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The thickness of the risers.

Get: RiserThickness(self: StairsRunType) -> float

Set: RiserThickness(self: StairsRunType) = value
"""

    RiserToTreadConnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connection of the riser to tread in relation to each other.

Get: RiserToTreadConnect(self: StairsRunType) -> RiserToTreadConnectionOption

Set: RiserToTreadConnect(self: StairsRunType) = value
"""

    StructuralDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The structural depth of the stairs run, only available for monolithic stairs run.

Get: StructuralDepth(self: StairsRunType) -> float

Set: StructuralDepth(self: StairsRunType) = value
"""

    TotalDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total depth of the stairs run, only available for monolithic stairs run.

Get: TotalDepth(self: StairsRunType) -> float

"""

    TreadNosingPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents on which edges of the nosing to apply the nosing profile.

Get: TreadNosingPosition(self: StairsRunType) -> TreadNosingPosition

Set: TreadNosingPosition(self: StairsRunType) = value
"""

    TreadProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the profile of the treads.

Get: TreadProfile(self: StairsRunType) -> ElementId

Set: TreadProfile(self: StairsRunType) = value
"""

    TreadThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The thickness of the treads.

Get: TreadThickness(self: StairsRunType) -> float

Set: TreadThickness(self: StairsRunType) = value
"""

    UndersideSurfaceStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underside surface style of the stairs run, only available for monolithic stairs run.

Get: UndersideSurfaceStyle(self: StairsRunType) -> StairsUndersideSurfaceStyle

Set: UndersideSurfaceStyle(self: StairsRunType) = value
"""



class StairsSupportTopsideSurfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    The style of the topside surface of the support.
    
    enum StairsSupportTopsideSurfaceType, values: Closed (0), Open (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Closed = None
    Open = None
    value__ = None


class StairsTextOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    The options to be used when orienting text annotations relative to stairs.
    
    enum StairsTextOrientation, values: Horizontal (0), Vertical (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Horizontal = None
    value__ = None
    Vertical = None


class StairsType(ElementType, IDisposable):
    """ A type element containing the properties for a component-based stair. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ConstructionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The construction method of the stairs.

Get: ConstructionMethod(self: StairsType) -> StairsConstructionMethod

"""

    EndConnectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The join style between a run and landing.

Get: EndConnectionType(self: StairsType) -> StairsEndConnectionType

Set: EndConnectionType(self: StairsType) = value
"""

    HasMiddleSupports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the stairs type has middle supports, False otherwise.

Get: HasMiddleSupports(self: StairsType) -> bool

Set: HasMiddleSupports(self: StairsType) = value
"""

    LandingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type for all landings in the stair element.

Get: LandingType(self: StairsType) -> ElementId

Set: LandingType(self: StairsType) = value
"""

    LeftLateralOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset for the left support from the edge of the run in a horizontal direction.

Get: LeftLateralOffset(self: StairsType) -> float

Set: LeftLateralOffset(self: StairsType) = value
"""

    LeftSideSupportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of left support used in the stair.

Get: LeftSideSupportType(self: StairsType) -> ElementId

Set: LeftSideSupportType(self: StairsType) = value
"""

    MaxRiserHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum height of each riser on the stair element.

Get: MaxRiserHeight(self: StairsType) -> float

Set: MaxRiserHeight(self: StairsType) = value
"""

    MiddleSupportsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of middle supports used in the stair.

Get: MiddleSupportsNumber(self: StairsType) -> int

Set: MiddleSupportsNumber(self: StairsType) = value
"""

    MiddleSupportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of middle supports used in the stair.

Get: MiddleSupportType(self: StairsType) -> ElementId

Set: MiddleSupportType(self: StairsType) = value
"""

    MinRunWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The initial value for the width of a common run.

Get: MinRunWidth(self: StairsType) -> float

Set: MinRunWidth(self: StairsType) = value
"""

    MinTreadDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum tread width along the center path for all common runs (winder, arc, and straight).

Get: MinTreadDepth(self: StairsType) -> float

Set: MinTreadDepth(self: StairsType) = value
"""

    NotchExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The horizontal length of the notch profile.

Get: NotchExtension(self: StairsType) -> float

Set: NotchExtension(self: StairsType) = value
"""

    NotchHorizontalGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the horizontal gap in the stairs notch.

Get: NotchHorizontalGap(self: StairsType) -> float

Set: NotchHorizontalGap(self: StairsType) = value
"""

    NotchThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertical length of the notch profile from the top.

Get: NotchThickness(self: StairsType) -> float

Set: NotchThickness(self: StairsType) = value
"""

    NotchVerticalGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the vertical gap in the stairs notch.

Get: NotchVerticalGap(self: StairsType) -> float

Set: NotchVerticalGap(self: StairsType) = value
"""

    RightLateralOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset for the right support from the edge of the run in a horizontal direction.

Get: RightLateralOffset(self: StairsType) -> float

Set: RightLateralOffset(self: StairsType) = value
"""

    RightSideSupportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of right support used in the stair.

Get: RightSideSupportType(self: StairsType) -> ElementId

Set: RightSideSupportType(self: StairsType) = value
"""

    RunType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type for all runs in the stair element.

Get: RunType(self: StairsType) -> ElementId

Set: RunType(self: StairsType) = value
"""



class StairsUndersideSurfaceStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    The style of the underside surface of the run.
    
    enum StairsUndersideSurfaceStyle, values: Smooth (1), Stepped (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Smooth = None
    Stepped = None
    value__ = None


class StairsWinderStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    The calculation method for the layout of the winder run steps.
    
    enum StairsWinderStyle, values: Balanced (0), SinglePoint (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Balanced = None
    SinglePoint = None
    value__ = None


class TopographyEditScope(EditScope, IDisposable):
    """
    A TopographyEditScope allows an application to create and maintain an editing session for a TopographySurface.
    
    TopographyEditScope(document: Document, transactionName: str)
    """
    def Dispose(self):
        """ Dispose(self: EditScope, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: EditScope, disposing: bool) """
        pass

    def Start(self, topoSurfaceId):
        """
        Start(self: TopographyEditScope, topoSurfaceId: ElementId) -> ElementId
        
            Starts a topography surface edit mode for an existing TopographySurface element.
        
            topoSurfaceId: The TopographySurface element to be edited.
            Returns: The Id of the topography Surface being eddited.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, document, transactionName):
        """ __new__(cls: type, document: Document, transactionName: str) """
        pass

    IsPermitted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests if the TopographyEditScope is permitted to start.

Get: IsPermitted(self: TopographyEditScope) -> bool

"""



class TopographySurface(Element, IDisposable):
    """ Represents a TopographySurface element. """
    def AddPoints(self, points):
        """ AddPoints(self: TopographySurface, points: IList[XYZ]) """
        pass

    @staticmethod
    def ArePointsDistinct(points):
        """ ArePointsDistinct(points: IList[XYZ]) -> bool """
        pass

    def AsSiteSubRegion(self):
        """
        AsSiteSubRegion(self: TopographySurface) -> SiteSubRegion
        
            Obtains the subregion object represented by this element.
            Returns: The SiteSubRegion element. If this does not represent a SiteSubRegion, this 
             will be ll.
        """
        pass

    def ChangePointElevation(self, point, elevationValue):
        """
        ChangePointElevation(self: TopographySurface, point: XYZ, elevationValue: float)
            Changes the elevation value for a point.
        
            point: The point to be modified.
            elevationValue: The new elevation value.
        """
        pass

    def ChangePointsElevation(self, points, elevationValue):
        """ ChangePointsElevation(self: TopographySurface, points: IList[XYZ], elevationValue: float) """
        pass

    def ContainsPoint(self, point):
        """
        ContainsPoint(self: TopographySurface, point: XYZ) -> bool
        
            Identifies whether the given point exists in the topography surface.
        
            point: The point to be checked.
            Returns: True if the input point exists in the topography surface, otherwise false.
        """
        pass

    @staticmethod
    def Create(document, points):
        """ Create(document: Document, points: IList[XYZ]) -> TopographySurface """
        pass

    def DeletePoints(self, points):
        """ DeletePoints(self: TopographySurface, points: IList[XYZ]) """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def FindPoints(self, boundingBox):
        """
        FindPoints(self: TopographySurface, boundingBox: Outline) -> IList[XYZ]
        
            Filters and returns only the points of the topography surface which lie within 
             the input bounding box.
        
        
            boundingBox: The 3D bounding box.
            Returns: The result points within the 3D bounding box
        """
        pass

    def GetBoundaryPoints(self):
        """
        GetBoundaryPoints(self: TopographySurface) -> IList[XYZ]
        
            Gets the points which are on the boundary of the topography surface.
            Returns: The collection of boundary points.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHostedSubRegionIds(self):
        """
        GetHostedSubRegionIds(self: TopographySurface) -> IList[ElementId]
        
            Gets the ids of all subregion elements hosted on this topography surface.
            Returns: The hosted subregion ids.
        """
        pass

    def GetInteriorPoints(self):
        """
        GetInteriorPoints(self: TopographySurface) -> IList[XYZ]
        
            Gets all of the points that are not boundary points for the topography surface.
            Returns: The collection of interior points.
        """
        pass

    def GetPoints(self):
        """
        GetPoints(self: TopographySurface) -> IList[XYZ]
        
            Gets the points that define this topography surface.
            Returns: The collection of points.
        """
        pass

    def IsBoundaryPoint(self, point):
        """
        IsBoundaryPoint(self: TopographySurface, point: XYZ) -> bool
        
            Identifies whether the given point is an existing boundary point of the current 
             topography surface.
        
        
            point: The point to be checked.
            Returns: Returns true if a given point is an existing boundary point.
           For 
             TopographySurface and SiteSubRegion elements, it returns false if the given 
             point is an existing interior point of current topography surface.
           For the 
             topography surface associated with a BuildingPad element, it always returns 
             true if the point is a part of the element (all points are boundary
           points 
             for the topography surface associated with a BuildingPad element).
        """
        pass

    @staticmethod
    def IsValidRegion(points):
        """ IsValidRegion(points: IList[XYZ]) -> bool """
        pass

    def MovePoint(self, movedPoint, targetPoint):
        """
        MovePoint(self: TopographySurface, movedPoint: XYZ, targetPoint: XYZ)
            Moves a point in a TopographySurface to a new designated location.
        
            movedPoint: The point to be moved.
            targetPoint: The new designated location of this point will move to.
        """
        pass

    def MovePoints(self, movedPoints, moveVector):
        """ MovePoints(self: TopographySurface, movedPoints: IList[XYZ], moveVector: XYZ) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AssociatedBuildingPadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of the building pad which causes this topography surface to be formed.

Get: AssociatedBuildingPadId(self: TopographySurface) -> ElementId

"""

    IsAssociatedWithBuildingPad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if this element represents a topography surface associated with a building pad.

Get: IsAssociatedWithBuildingPad(self: TopographySurface) -> bool

"""

    IsSiteSubRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if this element represents a subregion.

Get: IsSiteSubRegion(self: TopographySurface) -> bool

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the material applied to this element.

Get: MaterialId(self: TopographySurface) -> ElementId

Set: MaterialId(self: TopographySurface) = value
"""



class TopRail(ContinuousRail, IDisposable):
    """ Represents a top rail element in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class TopRailType(ContinuousRailType, IDisposable):
    """ A rail type object that is used in the generation of top rail. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class TreadNosingPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents on which edges of the nosing to apply the nosing profile.
    
    enum TreadNosingPosition, values: FrontAndLeft (1), FrontAndRight (2), FrontLeftAndRight (3), FrontOnly (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FrontAndLeft = None
    FrontAndRight = None
    FrontLeftAndRight = None
    FrontOnly = None
    value__ = None


class WinderPathResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Flag indicates whether curves are valid to use as base lines for winder path.
    
    enum WinderPathResult, values: ColinearOrOverlap (6), InvalidCurveType (8), Noncontinuous (3), NotOpenLoop (4), NotSupported (9), NumberOutOfRange (1), SelfIntersect (7), Success (0), TooShort (5), Unbound (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ColinearOrOverlap = None
    InvalidCurveType = None
    Noncontinuous = None
    NotOpenLoop = None
    NotSupported = None
    NumberOutOfRange = None
    SelfIntersect = None
    Success = None
    TooShort = None
    Unbound = None
    value__ = None


