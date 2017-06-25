# encoding: utf-8
# module Autodesk.Revit.DB.Electrical calls itself Electrical
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CableTrayConduitBase(MEPCurve, IDisposable):
    """ The CableTrayConduitBase class is implemented as the base class for cable tray or conduit """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidEndPoints(startPoint, endPoint):
        """
        IsValidEndPoints(startPoint: XYZ, endPoint: XYZ) -> bool
        
            Identifies if two end points are valid.
        
            startPoint: The start point of the location line.
            endPoint: The end point of the location line.
            Returns: True if the two end points are valid, false otherwise.
        """
        pass

    @staticmethod
    def IsValidLevelId(document, levelId):
        """
        IsValidLevelId(document: Document, levelId: ElementId) -> bool
        
            Identifies if a level id is valid.
        
            document: The document.
            levelId: The level id.
            Returns: True if the level id is valid, false otherwise.
        """
        pass

    def IsWithFitting(self):
        """
        IsWithFitting(self: CableTrayConduitBase) -> bool
        
            Return whether its cable tray/conduit type is with fitting
            Returns: return true if its type is with fitting type.
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

    RunId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the run to which this element belongs.

Get: RunId(self: CableTrayConduitBase) -> ElementId

"""



class CableTray(CableTrayConduitBase, IDisposable):
    """ This class represents a cable tray in Autodesk Revit. """
    @staticmethod
    def Create(document, cabletrayType, startPoint, endPoint, levelId):
        """
        Create(document: Document, cabletrayType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> CableTray
        
            Creates a new instance of cable tray.
        
            document: The document.
            cabletrayType: The cable tray type.  This must be a cable tray type accepted by 
             isValidCableTrayType().
           If the input cable tray type is InvalidElementId, 
             the default cable tray type from the document will be used.
        
            startPoint: The start point of the cable tray location line.
            endPoint: The end point of the cable tray location line.
            levelId: The element id of the level which this cable tray based.
           If the input level 
             id is invalidElementId = -1, the nearest level will be used.
        
            Returns: The newly created cable tray.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetShapeType(self):
        """
        GetShapeType(self: CableTray) -> CableTrayShape
        
            Returns the shape type for the cable tray.
            Returns: The shape type.
        """
        pass

    @staticmethod
    def IsValidCableTrayType(document, cabletrayType):
        """
        IsValidCableTrayType(document: Document, cabletrayType: ElementId) -> bool
        
            Identifies if a cable tray type is valid.
        
            document: The document.
            cabletrayType: The cable tray type.
            Returns: True if the cable tray type is valid, false otherwise.
        """
        pass

    def IsValidRungSpace(self, rungSpace):
        """
        IsValidRungSpace(self: CableTray, rungSpace: float) -> bool
        
            Identifies if the input rung space is valid.
        
            rungSpace: The rung space to check.
            Returns: True if the value is acceptable, false otherwise.
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

    CurveNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The up-direction vector of the cable tray.

Get: CurveNormal(self: CableTray) -> XYZ

Set: CurveNormal(self: CableTray) = value
"""

    RungSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance between two rungs for the ladder cable tray.

Get: RungSpace(self: CableTray) -> float

Set: RungSpace(self: CableTray) = value
"""



class CableTrayConduitRunBase(Element, IDisposable):
    """ The base class for a cable tray or conduit run in Autodesk Revit. """
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

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the whole (cable tray or conduit) run
   default 0.0

Get: Length(self: CableTrayConduitRunBase) -> float

"""



class CableTrayRun(CableTrayConduitRunBase, IDisposable):
    """ This class represents a cable tray run in Autodesk Revit. """
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


class CableTraySettings(Element, IDisposable):
    """ The cable tray settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetCableTraySettings(document):
        """
        GetCableTraySettings(document: Document) -> CableTraySettings
        
            Gets the cable tray settings of the project.
        
            document: The document.
            Returns: The cable tray settings of the project.
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

    ConnectorSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray connector separator string.

Get: ConnectorSeparator(self: CableTraySettings) -> str

Set: ConnectorSeparator(self: CableTraySettings) = value
"""

    FittingAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of fitting annotation size.

Get: FittingAnnotationSize(self: CableTraySettings) -> float

Set: FittingAnnotationSize(self: CableTraySettings) = value
"""

    RiseDropAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rise drop annotation size.

Get: RiseDropAnnotationSize(self: CableTraySettings) -> float

Set: RiseDropAnnotationSize(self: CableTraySettings) = value
"""

    SizeSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray size separator string.

Get: SizeSeparator(self: CableTraySettings) -> str

Set: SizeSeparator(self: CableTraySettings) = value
"""

    SizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray size suffix string.

Get: SizeSuffix(self: CableTraySettings) -> str

Set: SizeSuffix(self: CableTraySettings) = value
"""

    UseAnnotationScaleForSingleLineFittings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: CableTraySettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: CableTraySettings) = value
"""



class CableTrayShape(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum of cable tray shape
    
    enum CableTrayShape, values: Channel (1), Invalid (0), Ladder (2)
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

    Channel = None
    Invalid = None
    Ladder = None
    value__ = None


class CableTraySizeIterator(object, IEnumerator[MEPSize], IDisposable, IEnumerator):
    """ An iterator to a set of MEP cable tray sizes from CableTraySizes. """
    def Dispose(self):
        """ Dispose(self: CableTraySizeIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: CableTraySizeIterator) -> MEPSize
        
            Returns the current MEPSize.
            Returns: The current MEPSize.
        """
        pass

    def HasCurrent(self):
        """
        HasCurrent(self: CableTraySizeIterator) -> bool
        
            Identifies if the iterator has a current item.
            Returns: True if there is a current item.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: CableTraySizeIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: CableTraySizeIterator) -> bool
        
            Increments the iterator to the next item.
            Returns: True if there is a next available item in this iterator.
           False if the 
             iterator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CableTraySizeIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: CableTraySizeIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MEPSize](enumerator: IEnumerator[MEPSize], value: MEPSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: CableTraySizeIterator) -> MEPSize

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CableTraySizeIterator) -> bool

"""



class CableTraySizes(Element, IDisposable, IEnumerable[MEPSize], IEnumerable):
    """ Cable tray sizes. """
    def AddSize(self, sizeInfo):
        """
        AddSize(self: CableTraySizes, sizeInfo: MEPSize)
            Inserts a new MEPSize into the cable tray sizes.
           For cable tray, the 
             nominal diameter of MEPSize is used .
        
        
            sizeInfo: The new MEPSize to be added.
        """
        pass

    def ClearAll(self):
        """
        ClearAll(self: CableTraySizes)
            Removes all MEPSizes in the cable tray sizes.
        """
        pass

    def Contains(self, nominalDiameter):
        """
        Contains(self: CableTraySizes, nominalDiameter: float) -> bool
        
            Checks whether a cable tray size with the nominal diameter exists.
        
            nominalDiameter: Nominal diameter.
            Returns: True if a cable tray size with the nominal diameter exists.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetCableTraySizes(aDoc):
        """
        GetCableTraySizes(aDoc: Document) -> CableTraySizes
        
            Gets the cable tray sizes of the project.
        
            aDoc: The document.
            Returns: The cable tray sizes of the project.
        """
        pass

    def GetCableTraySizesIterator(self):
        """
        GetCableTraySizesIterator(self: CableTraySizes) -> CableTraySizeIterator
        
            Returns a CableTraySizeIterator to the MEP cable tray sizes.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CableTraySizes) -> IEnumerator[MEPSize]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetSizeCount(self):
        """
        GetSizeCount(self: CableTraySizes) -> int
        
            Gets the size count of the cable tray size table.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSize(self, sizeInfo):
        """
        RemoveSize(self: CableTraySizes, sizeInfo: MEPSize)
            Erases the existing MEPSize.
           For cable tray, the nominal diameter is used 
             in MEPSize.
        
        
            sizeInfo: The MEPSize to be removed..
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MEPSize](enumerable: IEnumerable[MEPSize], value: MEPSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class CableTrayType(MEPCurveType, IDisposable):
    """ This class represents a cable tray type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsValidBendMultiplier(self, bendMultiplier):
        """
        IsValidBendMultiplier(self: CableTrayType, bendMultiplier: float) -> bool
        
            Identifies if the input bend multiplier is valid.
        
            bendMultiplier: The bend multiplier to check.
            Returns: True if the value is acceptable, false otherwise.
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

    BendMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend multiplier.

Get: BendMultiplier(self: CableTrayType) -> float

Set: BendMultiplier(self: CableTrayType) = value
"""

    IsWithFitting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this cable tray type is with fitting

Get: IsWithFitting(self: CableTrayType) -> bool

"""

    ShapeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shape of this cable tray type.

Get: ShapeType(self: CableTrayType) -> CableTrayShape

"""



class CapitalizationForLoadNames(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing the options for how electrical load names should be capitalized.
    
    enum CapitalizationForLoadNames, values: Initial (1), Sentence (2), SourceParameters (0), Upper (3)
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

    Initial = None
    Sentence = None
    SourceParameters = None
    Upper = None
    value__ = None


class CircuitLoadCalculationMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Methods to calculate circuit loads
    
    enum CircuitLoadCalculationMethod, values: SumApparentLoad (1), SumTrueLoadAndReactiveLoad (0)
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

    SumApparentLoad = None
    SumTrueLoadAndReactiveLoad = None
    value__ = None


class CircuitSequence(Enum, IComparable, IFormattable, IConvertible):
    """
    Options of circuit sequence for assigning circuit to circuits across panel.
    
    enum CircuitSequence, values: GroupByPhase (1), Numerical (0), OddThenEven (2)
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

    GroupByPhase = None
    Numerical = None
    OddThenEven = None
    value__ = None


class CircuitType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible circuit types.
    
    enum CircuitType, values: Circuit (0), Space (2), Spare (1)
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

    Circuit = None
    Space = None
    Spare = None
    value__ = None


class Conduit(CableTrayConduitBase, IDisposable):
    """ This class represents a conduit in Autodesk Revit. """
    @staticmethod
    def Create(document, conduitType, startPoint, endPoint, levelId):
        """
        Create(document: Document, conduitType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> Conduit
        
            Creates a new instance of conduit.
        
            document: The document.
            conduitType: The conduit type.  This must be a conduit type accepted by 
             isValidConduitType().
           If the input conduit type is InvalidElementId, the 
             default conduit type from the document will be used.
        
            startPoint: The start point of the conduit location line.
            endPoint: The end point of the conduit location line.
            levelId: The element id of the level which this conduit based.
           If the input level id 
             is invalidElementId = -1, the nearest level will be used.
        
            Returns: The newly created conduit.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidConduitType(document, conduitType):
        """
        IsValidConduitType(document: Document, conduitType: ElementId) -> bool
        
            Identifies if a conduit type is valid.
        
            document: The document.
            conduitType: The conduit type.
            Returns: True if the conduit type is valid, false otherwise.
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


class ConduitRun(CableTrayConduitRunBase, IDisposable):
    """ This class represents a conduit run in Autodesk Revit. """
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


class ConduitSettings(Element, IDisposable):
    """ The conduit settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetConduitSettings(document):
        """
        GetConduitSettings(document: Document) -> ConduitSettings
        
            Gets the conduit settings of the project.
        
            document: The document.
            Returns: The conduit settings of the project.
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

    ConnectorSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The conduit connector separator string.

Get: ConnectorSeparator(self: ConduitSettings) -> str

Set: ConnectorSeparator(self: ConduitSettings) = value
"""

    FittingAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of fitting annotation size.

Get: FittingAnnotationSize(self: ConduitSettings) -> float

Set: FittingAnnotationSize(self: ConduitSettings) = value
"""

    RiseDropAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rise drop annotation size.

Get: RiseDropAnnotationSize(self: ConduitSettings) -> float

Set: RiseDropAnnotationSize(self: ConduitSettings) = value
"""

    SizePrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The conduit size prefix string.

Get: SizePrefix(self: ConduitSettings) -> str

Set: SizePrefix(self: ConduitSettings) = value
"""

    SizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The conduit size suffix string.

Get: SizeSuffix(self: ConduitSettings) -> str

Set: SizeSuffix(self: ConduitSettings) = value
"""

    UseAnnotationScaleForSingleLineFittings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: ConduitSettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: ConduitSettings) = value
"""



class ConduitSize(object, IDisposable):
    """
    Stores the basic size information for a conduit.
    
    ConduitSize(nominalDiameter: float, innerDiameter: float, outerDiameter: float, bendRadius: float, usedInSizeLists: bool, usedInSizing: bool)
    """
    def Dispose(self):
        """ Dispose(self: ConduitSize) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConduitSize, disposing: bool) """
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
    def __new__(self, nominalDiameter, innerDiameter, outerDiameter, bendRadius, usedInSizeLists, usedInSizing):
        """ __new__(cls: type, nominalDiameter: float, innerDiameter: float, outerDiameter: float, bendRadius: float, usedInSizeLists: bool, usedInSizing: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BendRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum bend radius

Get: BendRadius(self: ConduitSize) -> float

"""

    InnerDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner diameter

Get: InnerDiameter(self: ConduitSize) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSize) -> bool

"""

    NominalDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nominal diameter

Get: NominalDiameter(self: ConduitSize) -> float

"""

    OuterDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Outer diameter

Get: OuterDiameter(self: ConduitSize) -> float

"""

    UsedInSizeLists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether it is used in size lists.

Get: UsedInSizeLists(self: ConduitSize) -> bool

"""

    UsedInSizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether is used in sizing.

Get: UsedInSizing(self: ConduitSize) -> bool

"""



class ConduitSizeIterator(object, IEnumerator[ConduitSize], IDisposable, IEnumerator):
    """ An iterator to a set of conduit sizes from ConduitSizes. """
    def Dispose(self):
        """ Dispose(self: ConduitSizeIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: ConduitSizeIterator) -> ConduitSize
        
            Returns the current ConduitSize.
            Returns: The current ConduitSize.
        """
        pass

    def HasCurrent(self):
        """
        HasCurrent(self: ConduitSizeIterator) -> bool
        
            Identifies if the iterator has a current item.
            Returns: True if there is a current item.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: ConduitSizeIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: ConduitSizeIterator) -> bool
        
            Increments the iterator to the next item.
            Returns: True if there is a next available item in this iterator.
           False if the 
             iterator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConduitSizeIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ConduitSizeIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConduitSize](enumerator: IEnumerator[ConduitSize], value: ConduitSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: ConduitSizeIterator) -> ConduitSize

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSizeIterator) -> bool

"""



class ConduitSizes(object, IEnumerable[ConduitSize], IEnumerable, IDisposable):
    """ Class ConduitSizeSet being used to store the conduit sizes. """
    def Contains(self, nominalDiameter):
        """
        Contains(self: ConduitSizes, nominalDiameter: float) -> bool
        
            Checks whether a conduit size with the nominal diameter exists.
        
            nominalDiameter: Nominal diameter.
            Returns: True if a conduit size with the nominal diameter exists.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ConduitSizes) """
        pass

    def GetConduitSizesIterator(self):
        """
        GetConduitSizesIterator(self: ConduitSizes) -> ConduitSizeIterator
        
            Returns a ConduitSizeIterator to the conduit sizes.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConduitSizes) -> IEnumerator[ConduitSize]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConduitSizes, disposing: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConduitSize](enumerable: IEnumerable[ConduitSize], value: ConduitSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of the items contained in the collection.

Get: Count(self: ConduitSizes) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSizes) -> bool

"""



class ConduitSizeSettingIterator(object, IEnumerator[KeyValuePair[str, ConduitSizes]], IDisposable, IEnumerator):
    """
    An iterator to a set of items from ConduitSizeSettings. Each item is a KeyValuePair(System::String^, ConduitSizes).
       ElementId is the id of the conduit standard type.
    """
    def Dispose(self):
        """ Dispose(self: ConduitSizeSettingIterator) """
        pass

    def HasCurrent(self):
        """
        HasCurrent(self: ConduitSizeSettingIterator) -> bool
        
            Identifies whether the iterator has a current item.
           There is no current 
             item if the iterator has not started yet or has been done.
        
            Returns: True if there is a current item.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: ConduitSizeSettingIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: ConduitSizeSettingIterator) -> bool
        
            Increments the enumerator to the next item.
            Returns: True if there is a next available item in this enumerator.
           False if the 
             enumerator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConduitSizeSettingIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ConduitSizeSettingIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, ConduitSizes]](enumerator: IEnumerator[KeyValuePair[str, ConduitSizes]], value: KeyValuePair[str, ConduitSizes]) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: ConduitSizeSettingIterator) -> KeyValuePair[str, ConduitSizes]

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSizeSettingIterator) -> bool

"""



class ConduitSizeSettings(Element, IDisposable, IEnumerable[KeyValuePair[str, ConduitSizes]], IEnumerable):
    """ Conduit sizes settings """
    def AddSize(self, standardName, sizeInfo):
        """
        AddSize(self: ConduitSizeSettings, standardName: str, sizeInfo: ConduitSize)
            Inserts a new ConduitSize in to the conduit size settings. The conduit standard 
             name determines the location of the new size in the size table.
        
        
            standardName: The conduit standard name.
            sizeInfo: The new ConduitSize to be added.
        """
        pass

    def CreateConduitStandardTypeFromExisingStandardType(self, pADoc, newStandardName, existingStandardName):
        """
        CreateConduitStandardTypeFromExisingStandardType(self: ConduitSizeSettings, pADoc: Document, newStandardName: str, existingStandardName: str) -> bool
        
            Creates one conduit standard type with the new name and assign the conduit 
             sizes to it from the existing standard type.
        
        
            pADoc: The document.
            newStandardName: The new conduit standard name.
            existingStandardName: The existing conduit standard name.
            Returns: True if creating success; otherwise false.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def DoesConduitStandardTypeExist(self, standardName):
        """
        DoesConduitStandardTypeExist(self: ConduitSizeSettings, standardName: str) -> bool
        
            Checks if the specified conduit standard exist.
        
            standardName: The conduit standard name.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetConduitSizeSettings(aDoc):
        """
        GetConduitSizeSettings(aDoc: Document) -> ConduitSizeSettings
        
            Gets the conduit size settings of the project.
        
            aDoc: The document.
            Returns: The conduit size settings of the project.
        """
        pass

    def GetConduitSizeSettingsIterator(self):
        """
        GetConduitSizeSettingsIterator(self: ConduitSizeSettings) -> ConduitSizeSettingIterator
        
            Returns a ConduitSizeSettingIterator to the conduit size settings.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConduitSizeSettings) -> IEnumerator[KeyValuePair[str, ConduitSizes]]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetSizeCount(self, standardName):
        """
        GetSizeCount(self: ConduitSizeSettings, standardName: str) -> int
        
            Gets the size count of the conduit size table. The conduit standard name the 
             location of the size in the size table.
        
        
            standardName: The conduit standard name.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveConduitStandardType(self, pADoc, standardName):
        """
        RemoveConduitStandardType(self: ConduitSizeSettings, pADoc: Document, standardName: str) -> bool
        
            Erases the existing ConduitSizes with this conduit standard name; the consuit 
             standard type can not be removed if it is in use.
        
        
            pADoc: The document.
            standardName: The conduit standard name.
            Returns: True if removing success; otherwise false.
        """
        pass

    def RemoveSize(self, standardName, nominalDiameter):
        """
        RemoveSize(self: ConduitSizeSettings, standardName: str, nominalDiameter: float)
            Erase the existing ConduitSize with this nominal diameter. The conduit standard 
             name determines the location of the size in the size table.
        
        
            standardName: The conduit standard name.
            nominalDiameter: Nominal diameter.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, ConduitSizes]](enumerable: IEnumerable[KeyValuePair[str, ConduitSizes]], value: KeyValuePair[str, ConduitSizes]) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ConduitType(MEPCurveType, IDisposable):
    """ This class represents a conduit type in Autodesk Revit. """
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

    IsWithFitting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this conduit type is with fitting

Get: IsWithFitting(self: ConduitType) -> bool

"""



class CorrectionFactor(APIObject, IDisposable):
    """ Represents electrical correction factor information. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get factor value of wire correction factor.

Get: Factor(self: CorrectionFactor) -> float

"""

    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get temperature which is used for specifying correction factor.

Get: Temperature(self: CorrectionFactor) -> Int64

"""



class CorrectionFactorSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains correction factors.
    
    CorrectionFactorSet()
    """
    def Clear(self):
        """
        Clear(self: CorrectionFactorSet)
            Removes every correction factor from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """ Contains(self: CorrectionFactorSet, item: CorrectionFactor) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CorrectionFactorSet, A_0: bool) """
        pass

    def Erase(self, item):
        """ Erase(self: CorrectionFactorSet, item: CorrectionFactor) -> int """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: CorrectionFactorSet) -> CorrectionFactorSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CorrectionFactorSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """ Insert(self: CorrectionFactorSet, item: CorrectionFactor) -> bool """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CorrectionFactorSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: CorrectionFactorSet) -> CorrectionFactorSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: CorrectionFactorSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of correction factors that are in the set.

Get: Size(self: CorrectionFactorSet) -> int

"""



class CorrectionFactorSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a correction factor set.
    
    CorrectionFactorSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: CorrectionFactorSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: CorrectionFactorSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CorrectionFactorSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: CorrectionFactorSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: CorrectionFactorSetIterator) -> object

"""



class DistributionSysType(ElementType, IDisposable):
    """ Represents a specific type of distribution system. """
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

    ElectricalPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set electrical phase (single, triple or undefined) of distribution system.

Get: ElectricalPhase(self: DistributionSysType) -> ElectricalPhase

Set: ElectricalPhase(self: DistributionSysType) = value
"""

    ElectricalPhaseConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set electrical phase configuration (Y, delta or undefined) of distribution system.

Get: ElectricalPhaseConfiguration(self: DistributionSysType) -> ElectricalPhaseConfiguration

Set: ElectricalPhaseConfiguration(self: DistributionSysType) = value
"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value which indicates whether this distribution system is in service now.

Get: IsInUse(self: DistributionSysType) -> bool

"""

    NumWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set number of wires of distribution system.

Get: NumWires(self: DistributionSysType) -> int

Set: NumWires(self: DistributionSysType) = value
"""

    VoltageLineToGround = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set line to ground voltage of distribution system type.

Get: VoltageLineToGround(self: DistributionSysType) -> VoltageType

Set: VoltageLineToGround(self: DistributionSysType) = value
"""

    VoltageLineToLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set line to line voltage type of distribution system type.

Get: VoltageLineToLine(self: DistributionSysType) -> VoltageType

Set: VoltageLineToLine(self: DistributionSysType) = value
"""



class DistributionSysTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains DistributionSys types.
    
    DistributionSysTypeSet()
    """
    def Clear(self):
        """
        Clear(self: DistributionSysTypeSet)
            Removes every DistributionSys type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: DistributionSysTypeSet, item: DistributionSysType) -> bool
        
            Tests for the existence of a DistributionSys type within the set.
        
            item: The DistributionSys type to be searched for.
            Returns: The Contains method returns True if the DistributionSys type is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DistributionSysTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: DistributionSysTypeSet, item: DistributionSysType) -> int
        
            Removes a specified DistributionSys type from the set.
        
            item: The DistributionSys type to be erased.
            Returns: The number of DistributionSys types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: DistributionSysTypeSet) -> DistributionSysTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DistributionSysTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: DistributionSysTypeSet, item: DistributionSysType) -> bool
        
            Insert the specified DistributionSys type into the set.
        
            item: The DistributionSys type to be inserted into the set.
            Returns: Returns whether the DistributionSys type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DistributionSysTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: DistributionSysTypeSet) -> DistributionSysTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: DistributionSysTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of DistributionSys types that are in the set.

Get: Size(self: DistributionSysTypeSet) -> int

"""



class DistributionSysTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a DistributionSys type set.
    
    DistributionSysTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: DistributionSysTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: DistributionSysTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DistributionSysTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: DistributionSysTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: DistributionSysTypeSetIterator) -> object

"""



class ElectricalDemandFactorDefinition(Element, IDisposable):
    """
    The ElectricalDemandFactorDef class represents a serialized version of an instance of
       demand factor definition.  It has a name, rule type, and values for the rules that are serialized.
    
    ElectricalDemandFactorDefinition()
    """
    def AddValue(self, dfValue):
        """
        AddValue(self: ElectricalDemandFactorDefinition, dfValue: ElectricalDemandFactorValue)
            Adds a value to the value set for this demand factor definition
        
            dfValue: Value to add to the set
        """
        pass

    def ClearValues(self):
        """
        ClearValues(self: ElectricalDemandFactorDefinition)
            Clears all the values stored for this demand factor definition.
        """
        pass

    @staticmethod
    def Create(ADoc, strName):
        """
        Create(ADoc: Document, strName: str) -> ElectricalDemandFactorDefinition
        
            Creates a new instance of a demand factor definition.
        
            ADoc: The document where the element will be created and added.
            strName: The name of the electrical demand factor definition to be created.
            Returns: The newly created demand factor definition element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetApplicableDemandFactor(self, numberOrLoad):
        """
        GetApplicableDemandFactor(self: ElectricalDemandFactorDefinition, numberOrLoad: float) -> float
        
            This method will return the applicable demand factor for the specified number
         
               of devices or load.
        
        
            numberOrLoad: The number of devices or load for which the demand factor should be looked up.
            Returns: The applicable demand factor.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetValues(self):
        """
        GetValues(self: ElectricalDemandFactorDefinition) -> ICollection[ElectricalDemandFactorValue]
        
            Provides access to the value set stored with this demand factor definition
        """
        pass

    def GetValuesCount(self):
        """
        GetValuesCount(self: ElectricalDemandFactorDefinition) -> int
        
            Returns the number of values in the set.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveValue(self, dfValue):
        """
        RemoveValue(self: ElectricalDemandFactorDefinition, dfValue: ElectricalDemandFactorValue)
            Removes a value to the value set for this demand factor definition
        
            dfValue: Value to remove from the set
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetValues(self, values):
        """ SetValues(self: ElectricalDemandFactorDefinition, values: ICollection[ElectricalDemandFactorValue]) """
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

    AdditionalLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional load to be included during demand load calculation.

Get: AdditionalLoad(self: ElectricalDemandFactorDefinition) -> float

Set: AdditionalLoad(self: ElectricalDemandFactorDefinition) = value
"""

    IncludeAdditionalLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should the additional load (if set) be included in demand load calculations.

Get: IncludeAdditionalLoad(self: ElectricalDemandFactorDefinition) -> bool

Set: IncludeAdditionalLoad(self: ElectricalDemandFactorDefinition) = value
"""

    RuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rule type for this demand factor definition.

Get: RuleType(self: ElectricalDemandFactorDefinition) -> ElectricalDemandFactorRule

Set: RuleType(self: ElectricalDemandFactorDefinition) = value
"""



class ElectricalDemandFactorRule(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum describes the different demand factor rule types available to the application.
       Within a demand factor a rule will be referenced and the user will have to enter values
       corresponding to that rule.
    
    enum ElectricalDemandFactorRule, values: Constant (0), LoadTable (2), LoadTablePerPortion (4), QuantityTable (1), QuantityTablePerPortion (3)
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

    Constant = None
    LoadTable = None
    LoadTablePerPortion = None
    QuantityTable = None
    QuantityTablePerPortion = None
    value__ = None


class ElectricalDemandFactorValue(object, IDisposable):
    """
    This class represents values used by a particular demand factor definition.  Each instance
       corresponds to a row in a table of values.  These values are part of the ElectricalDemandFactorDefinition
       class.
    
    ElectricalDemandFactorValue(minRange: float, maxRange: float, factor: float)
    ElectricalDemandFactorValue()
    """
    def Dispose(self):
        """ Dispose(self: ElectricalDemandFactorValue) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElectricalDemandFactorValue, disposing: bool) """
        pass

    def SetMaxRangeToUnlimited(self):
        """
        SetMaxRangeToUnlimited(self: ElectricalDemandFactorValue)
            Sets the max range on the value to unlimited
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
    def __new__(self, minRange=None, maxRange=None, factor=None):
        """
        __new__(cls: type, minRange: float, maxRange: float, factor: float)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The demand factor for this demand factor value.  For example, objects 1 to 3 can have 100% demand factor.
   In the example above, the demand factor will be 1.0.

Get: Factor(self: ElectricalDemandFactorValue) -> float

Set: Factor(self: ElectricalDemandFactorValue) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ElectricalDemandFactorValue) -> bool

"""

    MaxRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum range for this demand factor value.  For example, objects 1 to 3 can have 100% demand factor.
   In the example above, the maximum range will be 3.

Get: MaxRange(self: ElectricalDemandFactorValue) -> float

Set: MaxRange(self: ElectricalDemandFactorValue) = value
"""

    MinRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum range for this demand factor value.  For example, objects 1 to 3 can have 100% demand factor.
   In the example above, the minimum range will be 1.

Get: MinRange(self: ElectricalDemandFactorValue) -> float

Set: MinRange(self: ElectricalDemandFactorValue) = value
"""



class ElectricalEquipment(MEPModel, IDisposable):
    """ Provides access to the Electrical Equipment in Autodesk Revit MEP. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    DistributionSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """get or set the Distribution System for the Electrical Equipment.

Get: DistributionSystem(self: ElectricalEquipment) -> DistributionSysType

Set: DistributionSystem(self: ElectricalEquipment) = value
"""



class ElectricalLoadClassification(Element, IDisposable):
    """
    The ElectricalLoadClassification class represents a serialized version of an instance of
       load classification.
    """
    @staticmethod
    def Create(ADoc, strName):
        """
        Create(ADoc: Document, strName: str) -> ElectricalLoadClassification
        
            Creates a new instance of load classification and adds it to the document.
        
            ADoc: The document where the element will be created and added.
            strName: The name of the electrical load classification to be created.
            Returns: The newly created load classification element.
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

    ActualElectricalLoadLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the actual load parameter on the load classification.

Get: ActualElectricalLoadLabel(self: ElectricalLoadClassification) -> str

Set: ActualElectricalLoadLabel(self: ElectricalLoadClassification) = value
"""

    DemandFactorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The demand factor definition this load classification element uses.

Get: DemandFactorId(self: ElectricalLoadClassification) -> ElementId

Set: DemandFactorId(self: ElectricalLoadClassification) = value
"""

    LoadSummaryDemandFactorLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the demand factor parameter of the load classification.

Get: LoadSummaryDemandFactorLabel(self: ElectricalLoadClassification) -> str

Set: LoadSummaryDemandFactorLabel(self: ElectricalLoadClassification) = value
"""

    Motor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this load classification is to be used for motors.

Get: Motor(self: ElectricalLoadClassification) -> bool

"""

    PanelConnectedCurrentLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the connected current parameter on the load classification.

Get: PanelConnectedCurrentLabel(self: ElectricalLoadClassification) -> str

Set: PanelConnectedCurrentLabel(self: ElectricalLoadClassification) = value
"""

    PanelConnectedLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the connected load parameter of the load classification.

Get: PanelConnectedLabel(self: ElectricalLoadClassification) -> str

Set: PanelConnectedLabel(self: ElectricalLoadClassification) = value
"""

    PanelEstimatedCurrentLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the estimated current parameter on the load classification.

Get: PanelEstimatedCurrentLabel(self: ElectricalLoadClassification) -> str

Set: PanelEstimatedCurrentLabel(self: ElectricalLoadClassification) = value
"""

    PanelEstimatedLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name template for the estimated demand parameter on the load classification.

Get: PanelEstimatedLabel(self: ElectricalLoadClassification) -> str

Set: PanelEstimatedLabel(self: ElectricalLoadClassification) = value
"""

    SpaceLoadClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The electrical load class associated with a space.

Get: SpaceLoadClass(self: ElectricalLoadClassification) -> ElectricalLoadClassificationSpace

Set: SpaceLoadClass(self: ElectricalLoadClassification) = value
"""



class ElectricalLoadClassificationData(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum is used by the ElectricalLoadClassification class as additional data whenever
       data members changed.  It is used as the additional data when the atom corresponding to each
       data member is touched.
    
    enum ElectricalLoadClassificationData, values: ActualElecLoadNameLabel (8), DemandFactor (2), LoadSummaryDemandFactorLabel (3), Name (0), PanelConnectedCurrentLabel (6), PanelConnectedLabel (4), PanelEstimatedCurrentLabel (7), PanelEstimatedLabel (5), SpaceLoadClass (1)
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

    ActualElecLoadNameLabel = None
    DemandFactor = None
    LoadSummaryDemandFactorLabel = None
    Name = None
    PanelConnectedCurrentLabel = None
    PanelConnectedLabel = None
    PanelEstimatedCurrentLabel = None
    PanelEstimatedLabel = None
    SpaceLoadClass = None
    value__ = None


class ElectricalLoadClassificationSpace(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum is used by the ElectricalLoadClassification to specify the load class for use with spaces.
    
    enum ElectricalLoadClassificationSpace, values: Lighting (1), None (0), Power (2)
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

    Lighting = None
    None = None
    Power = None
    value__ = None


class ElectricalPhase(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type to specify whether the electrical system is single phase or three phase.
    
    enum ElectricalPhase, values: SinglePhase (0), ThreePhase (1)
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

    SinglePhase = None
    ThreePhase = None
    value__ = None


class ElectricalPhaseConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type to specify the electrical phase configuration.
    
    enum ElectricalPhaseConfiguration, values: Delta (2), Undefined (0), Wye (1)
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

    Delta = None
    Undefined = None
    value__ = None
    Wye = None


class ElectricalSetting(Element, IDisposable):
    """ The ElectricalSetting class represents an instance of element of electrical settings. """
    def AddDistributionSysType(self, name, phase, phaseConfig, numWire, volLineToLine, volLineToGround):
        """
        AddDistributionSysType(self: ElectricalSetting, name: str, phase: ElectricalPhase, phaseConfig: ElectricalPhaseConfiguration, numWire: int, volLineToLine: VoltageType, volLineToGround: VoltageType) -> DistributionSysType
        
            Add a new distribution system type to project.
        
            name: The name of new added distribution system type
            phase: Single or three phase this type is
            phaseConfig: Configuration property of given phase
            numWire: Wire number of this distribution system
            volLineToLine: Type of line to line voltage in this system
            volLineToGround: Type of line to ground voltage in this system
            Returns: New added distribution system type object.
        """
        pass

    def AddVoltageType(self, name, actualValue, minValue, maxValue):
        """
        AddVoltageType(self: ElectricalSetting, name: str, actualValue: float, minValue: float, maxValue: float) -> VoltageType
        
            Add a new type definition of voltage into project.
        
            name: Specify voltage type name
            actualValue: Specify actual value of voltage type.
            minValue: Specify acceptable minimum value of the voltage type.
            maxValue: Specify acceptable maximum value of the voltage type.
            Returns: New added voltage type object.
        """
        pass

    def AddWireMaterialType(self, name, baseMaterial):
        """
        AddWireMaterialType(self: ElectricalSetting, name: str, baseMaterial: WireMaterialType) -> WireMaterialType
        
            Add a new type of wire material.
        
            name: Name of new material type.
            baseMaterial: Specify an existing material type which New material will be constructed based 
             on.
        
            Returns: New added wire material type object.
        """
        pass

    def AddWireType(self, name, materialType, temperatureRating, insulation, maxSize, neutralMultiplier, neutralRequired, neutralMode, conduit):
        """
        AddWireType(self: ElectricalSetting, name: str, materialType: WireMaterialType, temperatureRating: TemperatureRatingType, insulation: InsulationType, maxSize: WireSize, neutralMultiplier: float, neutralRequired: bool, neutralMode: NeutralMode, conduit: WireConduitType) -> WireType
        
            Add a new wire type to project.
        
            name: Name of the new wire type.
            materialType: Wire material of new wire type.
            temperatureRating: Temperature rating type information of new wire type.
            insulation: Insulation of new wire type.
            maxSize: Max wire size of new wire type.
            neutralMultiplier: Neutral multiplier of new wire type.
            neutralRequired: Specify whether neutral point is required.
            neutralMode: Specify neutral mode.
            conduit: Conduit type of new wire type.
            Returns: New added wire type object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetElectricalSettings(document):
        """
        GetElectricalSettings(document: Document) -> ElectricalSetting
        
            Get the electrical settings of the project.
        
            document: The document.
            Returns: The electrical settings of the project.
        """
        pass

    def GetSpecificFittingAngles(self):
        """
        GetSpecificFittingAngles(self: ElectricalSetting) -> IList[float]
        
            Gets the list of specific fitting angles.
            Returns: Angles (in degrees).
        """
        pass

    def GetSpecificFittingAngleStatus(self, angle):
        """
        GetSpecificFittingAngleStatus(self: ElectricalSetting, angle: float) -> bool
        
            Gets the status of given specific fitting angle.
        
            angle: The specific fitting angle (in degree) that must be one of 90, 60, 45, 30, 22.5 
             or 11.25 degrees.
        """
        pass

    def IsValidSpecificFittingAngle(self, angle):
        """
        IsValidSpecificFittingAngle(self: ElectricalSetting, angle: float) -> bool
        
            Checks that the given value is a valid specific fitting angle. The specific 
             fitting angles are angles of 90, 60, 45, 30, 22.5 or 11.25 degrees.
        
        
            angle: The angle value (in degree).
            Returns: True if the given value is a valid specific fitting angle.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveDistributionSysType(self, distributionSysType):
        """
        RemoveDistributionSysType(self: ElectricalSetting, distributionSysType: DistributionSysType)
            Remove an existing distribution system type from the project.
        """
        pass

    def RemoveVoltageType(self, voltageType):
        """
        RemoveVoltageType(self: ElectricalSetting, voltageType: VoltageType)
            Remove the voltage type from project.
        
            voltageType: Specify the voltage type to be removed.
        """
        pass

    def RemoveWireMaterialType(self, materialType):
        """
        RemoveWireMaterialType(self: ElectricalSetting, materialType: WireMaterialType)
            Remove the wire material type from project.
        
            materialType: The wire material type to be removed.
        """
        pass

    def RemoveWireType(self, wireType):
        """
        RemoveWireType(self: ElectricalSetting, wireType: WireType)
            Remove wire type definition from project.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSpecificFittingAngleStatus(self, angle, bStatus):
        """
        SetSpecificFittingAngleStatus(self: ElectricalSetting, angle: float, bStatus: bool)
            Sets the status of given specific angle.
        
            angle: The specific angle (in degree) that must be 60, 45, 30, 22.5 or 11.25 degrees.
            bStatus: Status, true - using the given angle during the pipe layout.
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

    CircuitLoadCalculationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The method to calculate circuit load

Get: CircuitLoadCalculationMethod(self: ElectricalSetting) -> CircuitLoadCalculationMethod

Set: CircuitLoadCalculationMethod(self: ElectricalSetting) = value
"""

    CircuitNamePhaseA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Circuit Naming by Phase - Phase A Label.

Get: CircuitNamePhaseA(self: ElectricalSetting) -> str

Set: CircuitNamePhaseA(self: ElectricalSetting) = value
"""

    CircuitNamePhaseB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Circuit Naming by Phase - Phase B Label.

Get: CircuitNamePhaseB(self: ElectricalSetting) -> str

Set: CircuitNamePhaseB(self: ElectricalSetting) = value
"""

    CircuitNamePhaseC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Circuit Naming by Phase - Phase C Label.

Get: CircuitNamePhaseC(self: ElectricalSetting) -> str

Set: CircuitNamePhaseC(self: ElectricalSetting) = value
"""

    CircuitRating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default circuit rating for newly created circuit.

Get: CircuitRating(self: ElectricalSetting) -> float

Set: CircuitRating(self: ElectricalSetting) = value
"""

    CircuitSequence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sequence in which power circuits are created.

Get: CircuitSequence(self: ElectricalSetting) -> CircuitSequence

Set: CircuitSequence(self: ElectricalSetting) = value
"""

    DistributionSysTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all distribution system types of the project.

Get: DistributionSysTypes(self: ElectricalSetting) -> DistributionSysTypeSet

"""

    VoltageTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all voltage type definitions information of the project.

Get: VoltageTypes(self: ElectricalSetting) -> VoltageTypeSet

"""

    WireConduitTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get electrical conduit types information of the project.

Get: WireConduitTypes(self: ElectricalSetting) -> WireConduitTypeSet

"""

    WireMaterialTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get electrical wire material types information of the project.

Get: WireMaterialTypes(self: ElectricalSetting) -> WireMaterialTypeSet

"""

    WireTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all wire type definition information of the project.

Get: WireTypes(self: ElectricalSetting) -> WireTypeSet

"""



class ElectricalSystem(MEPSystem, IDisposable):
    """ Provides access to the Electrical System in Autodesk Revit MEP. """
    def AddToCircuit(self, components):
        """
        AddToCircuit(self: ElectricalSystem, components: ElementSet) -> bool
        
            Add a set of exist components to the Electrical System.
        
            components: The components added to the electrical system.
            Returns: If successful, all the components will add to the system. Otherwise ll is 
             returned.
        """
        pass

    def DisconnectPanel(self):
        """
        DisconnectPanel(self: ElectricalSystem)
            Disconnect the panel for the Electrical System.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def getElementsInNetwork(self, *args): #cannot find CLR method
        """ getElementsInNetwork(self: MEPSystem) -> ElementSet """
        pass

    def getFlow(self, *args): #cannot find CLR method
        """ getFlow(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def getStaticPressure(self, *args): #cannot find CLR method
        """ getStaticPressure(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def NewWires(self, view, wiringType):
        """
        NewWires(self: ElectricalSystem, view: View, wiringType: WiringType) -> WireSet
        
            Create a bunch of wires for the electrical system.
        
            view: The view in which the wire is to be visible.
            wiringType: Specify the wiring type (Arc or Chamfer) that is to be applied to all newly 
             created wires.
        
            Returns: New created wires
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveFromCircuit(self, components):
        """
        RemoveFromCircuit(self: ElectricalSystem, components: ElementSet)
            remove a set of exist components from the Electrical System.
        
            components: The components removed from the electrical system.
        """
        pass

    def SelectPanel(self, panel):
        """
        SelectPanel(self: ElectricalSystem, panel: FamilyInstance)
            Set the panel for the Electrical System.
        
            panel: The panel of the electrical system.
        """
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

    ApparentCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentCurrent value of the Electrical System.

Get: ApparentCurrent(self: ElectricalSystem) -> float

"""

    ApparentCurrentPhaseA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentCurrentPhaseA value of the Electrical System.

Get: ApparentCurrentPhaseA(self: ElectricalSystem) -> float

"""

    ApparentCurrentPhaseB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentCurrentPhaseB value of the Electrical System.

Get: ApparentCurrentPhaseB(self: ElectricalSystem) -> float

"""

    ApparentCurrentPhaseC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentCurrentPhaseC value of the Electrical System.

Get: ApparentCurrentPhaseC(self: ElectricalSystem) -> float

"""

    ApparentLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentLoad value of the Electrical System.

Get: ApparentLoad(self: ElectricalSystem) -> float

"""

    ApparentLoadPhaseA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentLoadPhaseA value of the Electrical System.

Get: ApparentLoadPhaseA(self: ElectricalSystem) -> float

"""

    ApparentLoadPhaseB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentLoadPhaseB value of the Electrical System.

Get: ApparentLoadPhaseB(self: ElectricalSystem) -> float

"""

    ApparentLoadPhaseC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the ApparentLoadPhaseC value of the Electrical System.

Get: ApparentLoadPhaseC(self: ElectricalSystem) -> float

"""

    BalancedLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether the BalancedLoad is on or off.

Get: BalancedLoad(self: ElectricalSystem) -> bool

"""

    CircuitNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the CircuitNumber of the Electrical System.

Get: CircuitNumber(self: ElectricalSystem) -> str

"""

    CircuitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the circuit type of the Electrical System.

Get: CircuitType(self: ElectricalSystem) -> CircuitType

"""

    GroundConductorsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the GroundConductors Number of the Electrical System.

Get: GroundConductorsNumber(self: ElectricalSystem) -> int

"""

    HotConductorsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the HotConductors Number of the Electrical System.

Get: HotConductorsNumber(self: ElectricalSystem) -> int

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Length value of the Electrical System.

Get: Length(self: ElectricalSystem) -> float

"""

    LoadClassifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the LoadClassifications used in the Electrical System.

Get: LoadClassifications(self: ElectricalSystem) -> str

"""

    LoadName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/Set the LoadName of the Electrical System.

Get: LoadName(self: ElectricalSystem) -> str

Set: LoadName(self: ElectricalSystem) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Name of the Electrical System.

Get: Name(self: ElectricalSystem) -> str

"""

    NeutralConductorsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the NeutralConductors Number of the Electrical System.

Get: NeutralConductorsNumber(self: ElectricalSystem) -> int

"""

    PanelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Panel name of the Electrical System.

Get: PanelName(self: ElectricalSystem) -> str

"""

    PolesNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Poles Number of the Electrical System.

Get: PolesNumber(self: ElectricalSystem) -> int

"""

    PowerFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the PowerFactor value of the Electrical System.

Get: PowerFactor(self: ElectricalSystem) -> float

"""

    PowerFactorState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the PowerFactorState type of the Electrical System.

Get: PowerFactorState(self: ElectricalSystem) -> PowerFactorStateType

"""

    Rating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/Set the Rating value of the Electrical System.

Get: Rating(self: ElectricalSystem) -> float

Set: Rating(self: ElectricalSystem) = value
"""

    RunsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Runs Number of the Electrical System.

Get: RunsNumber(self: ElectricalSystem) -> int

"""

    StartSlot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/Set the Start Slot where the Electrical System is located in its panel.

Get: StartSlot(self: ElectricalSystem) -> int

"""

    SystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Electrical System Type of the Electrical System.

Get: SystemType(self: ElectricalSystem) -> ElectricalSystemType

"""

    TrueCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueCurrent value of the Electrical System.

Get: TrueCurrent(self: ElectricalSystem) -> float

"""

    TrueCurrentPhaseA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueCurrentPhaseA value of the Electrical System.

Get: TrueCurrentPhaseA(self: ElectricalSystem) -> float

"""

    TrueCurrentPhaseB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueCurrentPhaseB value of the Electrical System.

Get: TrueCurrentPhaseB(self: ElectricalSystem) -> float

"""

    TrueCurrentPhaseC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueCurrentPhaseC value of the Electrical System.

Get: TrueCurrentPhaseC(self: ElectricalSystem) -> float

"""

    TrueLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueLoad value of the Electrical System.

Get: TrueLoad(self: ElectricalSystem) -> float

"""

    TrueLoadPhaseA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueLoadPhaseA value of the Electrical System.

Get: TrueLoadPhaseA(self: ElectricalSystem) -> float

"""

    TrueLoadPhaseB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueLoadPhaseB value of the Electrical System.

Get: TrueLoadPhaseB(self: ElectricalSystem) -> float

"""

    TrueLoadPhaseC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the TrueLoadPhaseC value of the Electrical System.

Get: TrueLoadPhaseC(self: ElectricalSystem) -> float

"""

    Voltage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Voltage value of the Electrical System.

Get: Voltage(self: ElectricalSystem) -> float

"""

    VoltageDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the VoltageDrop value of the Electrical System.

Get: VoltageDrop(self: ElectricalSystem) -> float

"""

    WireSizeString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the WireSize as a String of the Electrical System.

Get: WireSizeString(self: ElectricalSystem) -> str

"""

    WireType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/Set the wire type of the Electrical System.

Get: WireType(self: ElectricalSystem) -> WireType

Set: WireType(self: ElectricalSystem) = value
"""



class ElectricalSystemSet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contain any type of object.
    
    ElectricalSystemSet()
    """
    def Clear(self):
        """
        Clear(self: ElectricalSystemSet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """ Contains(self: ElectricalSystemSet, item: ElectricalSystem) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: ElectricalSystemSet, A_0: bool) """
        pass

    def Erase(self, item):
        """ Erase(self: ElectricalSystemSet, item: ElectricalSystem) -> int """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ElectricalSystemSet) -> ElectricalSystemSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ElectricalSystemSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """ Insert(self: ElectricalSystemSet, item: ElectricalSystem) -> bool """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElectricalSystemSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ElectricalSystemSet) -> ElectricalSystemSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: ElectricalSystemSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the set.

Get: Size(self: ElectricalSystemSet) -> int

"""



class ElectricalSystemSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a set.
    
    ElectricalSystemSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: ElectricalSystemSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: ElectricalSystemSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElectricalSystemSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: ElectricalSystemSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: ElectricalSystemSetIterator) -> object

"""



class ElectricalSystemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible electrical system types for a connector object.
    
    enum ElectricalSystemType, values: Communication (14), Controls (13), Data (5), FireAlarm (11), NurseCall (12), PowerBalanced (30), PowerCircuit (6), PowerUnBalanced (31), Security (10), Telephone (9), UndefinedSystemType (0)
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

    Communication = None
    Controls = None
    Data = None
    FireAlarm = None
    NurseCall = None
    PowerBalanced = None
    PowerCircuit = None
    PowerUnBalanced = None
    Security = None
    Telephone = None
    UndefinedSystemType = None
    value__ = None


class GroundConductorSize(APIObject, IDisposable):
    """ Represents electrical ground conductor size definition information. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Ampacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get ampacity which is used for specifying size, the unit is ampere.

Get: Ampacity(self: GroundConductorSize) -> Int64

"""

    ConductorSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get conductor size corresponding to specific ampacity.

Get: ConductorSize(self: GroundConductorSize) -> str

"""

    MaterialBelongTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the material type which include this ground conductor size information.

Get: MaterialBelongTo(self: GroundConductorSize) -> WireMaterialType

"""



class GroundConductorSizeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains GroundConductorSizes.
    
    GroundConductorSizeSet()
    """
    def Clear(self):
        """
        Clear(self: GroundConductorSizeSet)
            Removes every GroundConductorSize from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: GroundConductorSizeSet, item: GroundConductorSize) -> bool
        
            Tests for the existence of a GroundConductorSize within the set.
        
            item: The GroundConductorSize to be searched for.
            Returns: The Contains method returns True if the GroundConductorSize is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: GroundConductorSizeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: GroundConductorSizeSet, item: GroundConductorSize) -> int
        
            Removes a specified GroundConductorSize from the set.
        
            item: The GroundConductorSize to be erased.
            Returns: The number of GroundConductorSizes that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: GroundConductorSizeSet) -> GroundConductorSizeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GroundConductorSizeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: GroundConductorSizeSet, item: GroundConductorSize) -> bool
        
            Insert the specified GroundConductorSize into the set.
        
            item: The GroundConductorSize to be inserted into the set.
            Returns: Returns whether the GroundConductorSize was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GroundConductorSizeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: GroundConductorSizeSet) -> GroundConductorSizeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: GroundConductorSizeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of GroundConductorSizes that are in the set.

Get: Size(self: GroundConductorSizeSet) -> int

"""



class GroundConductorSizeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a GroundConductorSize set.
    
    GroundConductorSizeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: GroundConductorSizeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: GroundConductorSizeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GroundConductorSizeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: GroundConductorSizeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: GroundConductorSizeSetIterator) -> object

"""



class InsulationType(ElementType, IDisposable):
    """ Represents electrical insulation type definition information. """
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

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the insulation type is in use.

Get: IsInUse(self: InsulationType) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get name of Insulation type.

Set: Name(self: InsulationType) = value
"""



class InsulationTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains insulation types.
    
    InsulationTypeSet()
    """
    def Clear(self):
        """
        Clear(self: InsulationTypeSet)
            Removes every insulation type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: InsulationTypeSet, item: InsulationType) -> bool
        
            Tests for the existence of a insulation type within the set.
        
            item: The insulation type to be searched for.
            Returns: The Contains method returns True if the insulation type is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: InsulationTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: InsulationTypeSet, item: InsulationType) -> int
        
            Removes a specified insulation type from the set.
        
            item: The insulation type to be erased.
            Returns: The number of insulation types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: InsulationTypeSet) -> InsulationTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: InsulationTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: InsulationTypeSet, item: InsulationType) -> bool
        
            Insert the specified insulation type into the set.
        
            item: The insulation type to be inserted into the set.
            Returns: Returns whether the insulation type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InsulationTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: InsulationTypeSet) -> InsulationTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: InsulationTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of insulation types that are in the set.

Get: Size(self: InsulationTypeSet) -> int

"""



class InsulationTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a insulation type set.
    
    InsulationTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: InsulationTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: InsulationTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InsulationTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: InsulationTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: InsulationTypeSetIterator) -> object

"""



class LightingDevice(MEPModel, IDisposable):
    """ Provides access to the Lighting Device in Autodesk Revit MEP. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


class LightingFixture(MEPModel, IDisposable):
    """ Provides access to the Lighting Fixture in Autodesk Revit MEP. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


class LoadClassification(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type to list all demand factor classifications.
    
    enum LoadClassification, values: Hvac (3), Lighting (2), Power (1), Undefined (0)
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

    Hvac = None
    Lighting = None
    Power = None
    Undefined = None
    value__ = None


class LoadClassificationType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible load classification types for a connector object.
    
    enum LoadClassificationType, values: HVAC (3), Lighting (2), Other (0), Power (1)
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

    HVAC = None
    Lighting = None
    Other = None
    Power = None
    value__ = None


class NeutralMode(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type to list the neutral mode for wire type.
    
    enum NeutralMode, values: HotConductorSize (0), UnbalancedCurrent (1)
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

    HotConductorSize = None
    UnbalancedCurrent = None
    value__ = None


class PanelConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum declares the configuration for given panel schedule type.
    
    enum PanelConfiguration, values: OneColumn (0), TwoColumnsCircuitsAcross (1), TwoColumnsCircuitsDown (2)
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

    OneColumn = None
    TwoColumnsCircuitsAcross = None
    TwoColumnsCircuitsDown = None
    value__ = None


class PanelScheduleData(TableData, IDisposable):
    """
    The PanelScheduleData class holds most of the data that describe
       the layout, appearance, and style of the rows, columns, and cells
       of a panel schedule
    """
    def AddLoadClassification(self, loadClassficationId):
        """
        AddLoadClassification(self: PanelScheduleData, loadClassficationId: ElementId) -> bool
        
            Add a Load Classification Id to the array of Load Classifications.
        
            loadClassficationId: The load classification to add
            Returns: True if success; false if the given Id has already existed.
        """
        pass

    def Dispose(self):
        """ Dispose(self: TableData, A_0: bool) """
        pass

    def GetLoadClassifications(self):
        """
        GetLoadClassifications(self: PanelScheduleData) -> IList[ElementId]
        
            Gets an array of the load classifications associated with this panel schedule
            Returns: The array of the load classifications
        """
        pass

    def GetNumberOfCircuitRows(self):
        """
        GetNumberOfCircuitRows(self: PanelScheduleData) -> int
        
            Gets the number of rows in the circuit table
            Returns: The number of rows
        """
        pass

    def IsSymmetric(self):
        """
        IsSymmetric(self: PanelScheduleData) -> bool
        
            Check if this panel schedule is symmetric
            Returns: True if this panel schedule is symmetric, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TableData, disposing: bool) """
        pass

    def RemoveLoadClassification(self, nIndex):
        """
        RemoveLoadClassification(self: PanelScheduleData, nIndex: int)
            Remove a Load Classification Id from the array of Load Classifications
        
            nIndex: The index at which to remove the load classification
        """
        pass

    def SetBorderAroundSchedule(self, borderId):
        """
        SetBorderAroundSchedule(self: PanelScheduleData, borderId: ElementId)
            Adds a border around the schedule
        
            borderId: The border to set around the schedule
        """
        pass

    def SetBorderAroundSections(self, borderId):
        """
        SetBorderAroundSections(self: PanelScheduleData, borderId: ElementId)
            Adds a border around the sections
        
            borderId: The border to set around the sections
        """
        pass

    def SetLoadClassifications(self, loadClassificaions):
        """ SetLoadClassifications(self: PanelScheduleData, loadClassificaions: IList[ElementId]) """
        pass

    def UpdateCircuitTableForInstance(self, pPanel):
        """
        UpdateCircuitTableForInstance(self: PanelScheduleData, pPanel: FamilyInstance)
            Redraw the circuit table for the given panel with the given parameter updates
        
            pPanel: The panel that this circuit table is being drawn for
        """
        pass

    def UpdateCircuitTableForTemplate(self, newType, nNumSlots, bPhasesAsCurrents):
        """
        UpdateCircuitTableForTemplate(self: PanelScheduleData, newType: PanelSchedulePhaseLoadType, nNumSlots: int, bPhasesAsCurrents: bool)
            Redraw the circuit table for a template with the given parameter updates
        
            newType: The new phase load type of the circuit table
            nNumSlots: The number of circuit slots
            bPhasesAsCurrents: True if the phase columns should be currents, false if they should be loads
        """
        pass

    def UpdateIsSectionHidden(self, sectionType, bHide):
        """
        UpdateIsSectionHidden(self: PanelScheduleData, sectionType: SectionType, bHide: bool)
            Update if this section is hidden or not
        
            sectionType: The Section Type
            bHide: Whether to hide this section or not
        """
        pass

    def UpdateLoadSummary(self):
        """
        UpdateLoadSummary(self: PanelScheduleData)
            Update the load summary section
        """
        pass

    def UpdateVerticalHeadersInSection(self, sectionType, bVertical):
        """
        UpdateVerticalHeadersInSection(self: PanelScheduleData, sectionType: SectionType, bVertical: bool)
            Sets if this header should have vertical text
        
            sectionType: The section type
            bVertical: Whether headers are vertical or not
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

    BodyShowsVerticalHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shows text in the Load Summary section's headers vertically instead of horizontally

Get: BodyShowsVerticalHeaders(self: PanelScheduleData) -> bool

"""

    BorderAroundSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Places a border (GraphicStyle element) around the entire schedule, visible only on the instance and sheet

Get: BorderAroundSchedule(self: PanelScheduleData) -> ElementId

"""

    BorderAroundSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Places a border (GraphicStyle element) around each section, visible only on the instance and sheet

Get: BorderAroundSections(self: PanelScheduleData) -> ElementId

"""

    IsFooterSectionHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the user wishes to hide the footer section; setting this value must go through the appropriate update function

Get: IsFooterSectionHidden(self: PanelScheduleData) -> bool

"""

    IsHeaderSectionHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the user wishes to hide the header section; setting this value must go through the appropriate update function

Get: IsHeaderSectionHidden(self: PanelScheduleData) -> bool

"""

    IsPanelSinglePhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the panel is single phase.

Get: IsPanelSinglePhase(self: PanelScheduleData) -> bool

Set: IsPanelSinglePhase(self: PanelScheduleData) = value
"""

    IsSummarySectionHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the user wishes to hide the summary section; setting this value must go through the appropriate update function

Get: IsSummarySectionHidden(self: PanelScheduleData) -> bool

"""

    IsThirdPhaseHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the user wishes to hide the 3rd phase column of a single phase panel

Get: IsThirdPhaseHidden(self: PanelScheduleData) -> bool

Set: IsThirdPhaseHidden(self: PanelScheduleData) = value
"""

    NumberOfSlots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of slots in the panel schedule; setting this value must go through the appropriate update function

Get: NumberOfSlots(self: PanelScheduleData) -> int

"""

    PanelConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The panel configuration of this panel schedule

Get: PanelConfiguration(self: PanelScheduleData) -> PanelConfiguration

"""

    PhaseLoadType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property determines the layout of the phase load columns; setting this value must go through the updateCircuitTable function

Get: PhaseLoadType(self: PanelScheduleData) -> PanelSchedulePhaseLoadType

"""

    PhasesAsCurrents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the phase columns are currents (A), otherwise they are loads (VA); setting this value must go through the appropriate update function

Get: PhasesAsCurrents(self: PanelScheduleData) -> bool

"""

    ScheduleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The panel schedule type of this panel schedule

Get: ScheduleType(self: PanelScheduleData) -> PanelScheduleType

"""

    ShowCircuitNumberOnOneRowForMultiphaseCircuits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shows the circuit number broken up on each row of the multiphase circuit rows if true, all on the first row otherwise

Get: ShowCircuitNumberOnOneRowForMultiphaseCircuits(self: PanelScheduleData) -> bool

Set: ShowCircuitNumberOnOneRowForMultiphaseCircuits(self: PanelScheduleData) = value
"""

    ShowMultipleRowsForMultiphaseCircuits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """shows extra rows below multiphase circuits to indicate how many slots they take up if true, all on a single row otherwise

Get: ShowMultipleRowsForMultiphaseCircuits(self: PanelScheduleData) -> bool

Set: ShowMultipleRowsForMultiphaseCircuits(self: PanelScheduleData) = value
"""

    ShowSlotFromDeviceInsteadOfTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When true, the number of rows in an instance will be the number of poles on the associated device, not a set number

Get: ShowSlotFromDeviceInsteadOfTemplate(self: PanelScheduleData) -> bool

Set: ShowSlotFromDeviceInsteadOfTemplate(self: PanelScheduleData) = value
"""

    SummaryShowsGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Show groups of load classifications in the load summary section

Get: SummaryShowsGroups(self: PanelScheduleData) -> bool

Set: SummaryShowsGroups(self: PanelScheduleData) = value
"""

    SummaryShowsOnlyConnectedLoads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Show only the connected load classifications in the summary section

Get: SummaryShowsOnlyConnectedLoads(self: PanelScheduleData) -> bool

Set: SummaryShowsOnlyConnectedLoads(self: PanelScheduleData) = value
"""

    SummaryShowsVerticalHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shows text in the Load Summary section's headers vertically instead of horizontally

Get: SummaryShowsVerticalHeaders(self: PanelScheduleData) -> bool

"""



class PanelSchedulePhaseLoadType(Enum, IComparable, IFormattable, IConvertible):
    """
    Declares the panel schedule type.  The comments for each enum type show
       a simple example of how the layout would look when applied to a panel schedule
    
    enum PanelSchedulePhaseLoadType, values: LoadsByPhase (4), LoadsByPhaseInSharedColumns (3), LoadsByPhaseInSplitColumns (1), MirroredPhaseColumns (2), NoLoadInformation (0), SeperatePhaseLoadsPerCircuit (6), TotalLoadOnlyPerCircuit (5)
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

    LoadsByPhase = None
    LoadsByPhaseInSharedColumns = None
    LoadsByPhaseInSplitColumns = None
    MirroredPhaseColumns = None
    NoLoadInformation = None
    SeperatePhaseLoadsPerCircuit = None
    TotalLoadOnlyPerCircuit = None
    value__ = None


class PanelScheduleSheetInstance(Element, IDisposable):
    """ The class represents an instance of a panel schedule placed on sheet. """
    @staticmethod
    def Create(ADoc, scheduleId, DBView):
        """
        Create(ADoc: Document, scheduleId: ElementId, DBView: View) -> PanelScheduleSheetInstance
        
            Creates a new instance of panel schedule on sheet and adds it to the document.
            Returns: The newly created panel schedule sheet instance element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetSchedule(self):
        """
        GetSchedule(self: PanelScheduleSheetInstance) -> PanelScheduleView
        
            Gets the panel schedule view.
            Returns: The panel schedule view element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SplitSegment(self, iSeg):
        """
        SplitSegment(self: PanelScheduleSheetInstance, iSeg: int) -> bool
        
            Split the panel schedule into
           Thrown if the index is out of bounds.
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

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet instance offset in drawing sheet coordinates.

Get: Origin(self: PanelScheduleSheetInstance) -> XYZ

Set: Origin(self: PanelScheduleSheetInstance) = value
"""

    ScheduleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The panel schedule id.

Get: ScheduleId(self: PanelScheduleSheetInstance) -> ElementId

Set: ScheduleId(self: PanelScheduleSheetInstance) = value
"""



class PanelScheduleTemplate(Element, IDisposable):
    """
    The PanelScheduleTemplate class represents an instance of panel schedule template
       element. An instance object could be a branch panel, a switchboard or a data panel template.
    """
    def CopyFrom(self, OtherADoc, otherElem):
        """
        CopyFrom(self: PanelScheduleTemplate, OtherADoc: Document, otherElem: PanelScheduleTemplate)
            Copies all values from other element to this object.
        
            OtherADoc: The Document for the otherElem
            otherElem: The element being copied from.
        """
        pass

    @staticmethod
    def Create(document, type, config, strName):
        """
        Create(document: Document, type: PanelScheduleType, config: PanelConfiguration, strName: str) -> PanelScheduleTemplate
        
            Creates a new instance of a panel schedule template.
        
            document: The document where the element will be created and added.
            type: The panel schedule type.
            config: The panel configuration type.
            strName: The name of the panel schedule template to be created.
            Returns: The newly created panel schedule template element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetPanelScheduleType(self):
        """
        GetPanelScheduleType(self: PanelScheduleTemplate) -> PanelScheduleType
        
            Returns the panel schedule type.
        """
        pass

    def GetSectionData(self, sectionType):
        """
        GetSectionData(self: PanelScheduleTemplate, sectionType: SectionType) -> TableSectionData
        
            Gets the writable section data object.
            Returns: The table section data object.
        """
        pass

    def GetTableData(self):
        """
        GetTableData(self: PanelScheduleTemplate) -> PanelScheduleData
        
            Gets the writable table data object.
            Returns: The panel schedule data object.
        """
        pass

    def HasSameType(self, otherTemplate):
        """
        HasSameType(self: PanelScheduleTemplate, otherTemplate: PanelScheduleTemplate) -> bool
        
            Checks if given template has the same panel schedule type with this template.
        
            otherTemplate: The given template to check.
            Returns: True if the given template has the same panel schedule type with this template, 
             false otherwise.
        """
        pass

    @staticmethod
    def IsValidPanelConfiguration(scheduleType, configuration):
        """
        IsValidPanelConfiguration(scheduleType: PanelScheduleType, configuration: PanelConfiguration) -> bool
        
            Checks if given panel configuration is valid for given panel schedule type.
        
            scheduleType: The panel schedule type.
            configuration: The given configuration to check.
            Returns: True if panel schedule template can have a valid configuration assigned, false 
             otherwise.
        """
        pass

    @staticmethod
    def IsValidType(*__args):
        """
        IsValidType(panelScheduleType: PanelScheduleType) -> bool
        
            Checks if given type is valid for this panel schedule template element.
        
            panelScheduleType: The given type to check.
            Returns: True if panel schedule template can have a type assigned and this type is valid 
             for this element, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetTableData(self, Data):
        """
        SetTableData(self: PanelScheduleTemplate, Data: PanelScheduleData)
            Assigns table data to this template
        
            Data: The panel schedule data
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

    IsBranchPanelSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks to see if this object is branch panel schedule template element.

Get: IsBranchPanelSchedule(self: PanelScheduleTemplate) -> bool

"""

    IsDataPanelSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks to see if this object is data panel schedule template element.

Get: IsDataPanelSchedule(self: PanelScheduleTemplate) -> bool

"""

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks to see if this is default template for the given panel schedule type.

Get: IsDefault(self: PanelScheduleTemplate) -> bool

"""

    IsSwitchboardSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks to see if this object is switchboard schedule template element.

Get: IsSwitchboardSchedule(self: PanelScheduleTemplate) -> bool

"""



class PanelScheduleType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum declares the panel schedule type.
    
    enum PanelScheduleType, values: Branch (0), Data (2), Switchboard (1), Unknown (-1)
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

    Branch = None
    Data = None
    Switchboard = None
    Unknown = None
    value__ = None


class PanelScheduleView(TableView, IDisposable):
    """ An instance of a panel schedule view. """
    def CanMoveSlotTo(self, nMovingRow, nMovingCol, nToRow, nToCol):
        """
        CanMoveSlotTo(self: PanelScheduleView, nMovingRow: int, nMovingCol: int, nToRow: int, nToCol: int) -> bool
        
            Verifies if can circuits in the source slot to the specific slot.
        
            nMovingRow: The Row Number of cell to be moved.
            nMovingCol: Start Column Number of cell to be moved.
            nToRow: The Row Number of cell to moved to.
            nToCol: End Column Number of cell to moved to.
            Returns: True if can move circuits in the source slot to the specific slot.
        """
        pass

    @staticmethod
    def CreateInstanceView(ADoc, *__args):
        """
        CreateInstanceView(ADoc: Document, panelId: ElementId) -> PanelScheduleView
        
            Creates a new instance of this view (using default template)
        
            ADoc: The Document
            panelId: Element id of the electrical panel element.
            Returns: The PanelScheduleView
        CreateInstanceView(ADoc: Document, templateId: ElementId, panelId: ElementId) -> PanelScheduleView
        
            Creates a new instance of this view (using specific template)
        
            ADoc: The Document
            templateId: The templateId that this function will use
            panelId: Element id of the electrical panel element.
            Returns: The PanelScheduleView
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GenerateInstanceFromTemplate(self, templateId):
        """
        GenerateInstanceFromTemplate(self: PanelScheduleView, templateId: ElementId)
            Assigns the data from the template to the instance and performs any tasks 
             specific to the instance (3rd phase, borders, etc)
        
        
            templateId: Element id of the template element.
        """
        pass

    def GetApparentPhaseValue(self, circuitId, apparentLoadParam):
        """
        GetApparentPhaseValue(self: PanelScheduleView, circuitId: ElementId, apparentLoadParam: ElementId) -> float
        
            Gets the apparent load for the given phase for the given slotted circuit
        
            circuitId: Circuit id for the apparent phase value
            apparentLoadParam: The requested apparent load phase parameter
            Returns: The value of the apparent phase
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: View, view: View) -> BoundingBoxXYZ """
        pass

    def GetCellsBySlotNumber(self, nSlotNumber, RowArr, ColArr):
        """ GetCellsBySlotNumber(self: PanelScheduleView, nSlotNumber: int) -> (IList[int], IList[int]) """
        pass

    def GetCircuitByCell(self, nRow, nCol):
        """
        GetCircuitByCell(self: PanelScheduleView, nRow: int, nCol: int) -> ElectricalSystem
        
            Gets the circuit element for the given slot number
        
            nRow: Row Number of the Body Section
            nCol: Column Number of the Body Section
            Returns: The circuit found at the given row and column
        """
        pass

    def GetCircuitIdByCell(self, nRow, nCol):
        """
        GetCircuitIdByCell(self: PanelScheduleView, nRow: int, nCol: int) -> ElementId
        
            Gets the circuit id for the given slot number
        
            nRow: Row Number
            nCol: Column Number
            Returns: ElementId of the circuit found at the given row and column
        """
        pass

    def GetCombinedParamValue(self, sectionType, nRow, nCol):
        """
        GetCombinedParamValue(self: PanelScheduleView, sectionType: SectionType, nRow: int, nCol: int) -> str
        
            Returns the combined parameter text for instance view
        
            sectionType: Section type
            nRow: Row Number
            nCol: Column Number
            Returns: The combined parameter text
        """
        pass

    def GetLoadClassificationConnectedCurrent(self, nRow, nCol):
        """
        GetLoadClassificationConnectedCurrent(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the Total Current for given Load Classification
        
            nRow: Row number of Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The Connected Current for the given Load Classification
        """
        pass

    def GetLoadClassificationConnectedLoad(self, nRow, nCol):
        """
        GetLoadClassificationConnectedLoad(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the Total Load for given Load Classification
        
            nRow: Row number of Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The total load for the given Load Classification
        """
        pass

    def GetLoadClassificationDemandCurrent(self, nRow, nCol):
        """
        GetLoadClassificationDemandCurrent(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the Demand Current for given Load Classification
        
            nRow: Row number of Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The Demand Current for the given Load Classification
        """
        pass

    def GetLoadClassificationDemandFactor(self, nRow, nCol):
        """
        GetLoadClassificationDemandFactor(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the Demand Factor for given Load Classification
        
            nRow: Row number of Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The Demand Factor for the given Load Classification
        """
        pass

    def GetLoadClassificationDemandLoad(self, nRow, nCol):
        """
        GetLoadClassificationDemandLoad(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the Demand Load for given Load Classification
        
            nRow: Row number of Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The Demand Load for the Load Classification
        """
        pass

    def GetLoadClassificationId(self, nRow):
        """
        GetLoadClassificationId(self: PanelScheduleView, nRow: int) -> ElementId
        
            Gets the id of the associated Load Classification at the given row
        
            nRow: Row number of Load Summary Section
            Returns: The element id of the Load Classification
        """
        pass

    def GetLoadClassificationName(self, nRow, nCol):
        """
        GetLoadClassificationName(self: PanelScheduleView, nRow: int, nCol: int) -> str
        
            Gets the name of the Load Classification at the given row/column
        
            nRow: Row Number of the Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The name of the Load Classification
        """
        pass

    def GetLoadClassificationParamValue(self, parameterId, nRow, nCol):
        """
        GetLoadClassificationParamValue(self: PanelScheduleView, parameterId: ElementId, nRow: int, nCol: int) -> str
        
            Gets the load classification parameter value.
        
            parameterId: Parameter Id of the Load Classification
            nRow: Row Number of the Load Summary Section
            nCol: Column number of Load Summary Section
            Returns: The value of the Load Classification parameter
        """
        pass

    def GetPanel(self):
        """
        GetPanel(self: PanelScheduleView) -> ElementId
        
            Gets the panel for this view
            Returns: The id of the panel for this view
        """
        pass

    def GetParamValue(self, sectionType, nRow, nCol):
        """
        GetParamValue(self: PanelScheduleView, sectionType: SectionType, nRow: int, nCol: int) -> str
        
            Gets the cell's text based on its type
        
            sectionType: Section of the desired parameter value
            nRow: Row Number of the Section
            nCol: Column Number of the Section
            Returns: The cell's text
        """
        pass

    def GetSectionData(self, sectionType):
        """
        GetSectionData(self: PanelScheduleView, sectionType: SectionType) -> TableSectionData
        
            Gets section data that will be written to
        
            sectionType: The section type
            Returns: The Autodesk.Revit.DB.TableSectionData
        """
        pass

    def GetSlotNumberByCell(self, nRow, nCol):
        """
        GetSlotNumberByCell(self: PanelScheduleView, nRow: int, nCol: int) -> int
        
            Gets the slot number in the circuit table
        
            nRow: Column Number
            Returns: Row Number
        """
        pass

    def GetSpareCurrentValue(self, row, column, idCurrentParameter):
        """
        GetSpareCurrentValue(self: PanelScheduleView, row: int, column: int, idCurrentParameter: ElementId) -> float
        
            Gets the value of the apparent current parameter for a spare
        
            row: A row where the valid spare is
            column: A column where the valid spare is
            idCurrentParameter: One of 4 valid current parameters: RBS_ELEC_APPARENT_CURRENT_PARAM, 
             RBS_ELEC_APPARENT_CURRENT_PHASEA_PARAM, RBS_ELEC_APPARENT_CURRENT_PHASEB_PARAM, 
             RBS_ELEC_APPARENT_CURRENT_PHASEC_PARAM
        
            Returns: The value of the spare's current parameter
        """
        pass

    def GetSpareLoadValue(self, row, column, idLoadParameter):
        """
        GetSpareLoadValue(self: PanelScheduleView, row: int, column: int, idLoadParameter: ElementId) -> float
        
            Gets the value of the apparent load parameter for a spare
        
            row: A row where the valid spare is
            column: A column where the valid spare is
            idLoadParameter: One of 4 valid load parameters: RBS_ELEC_APPARENT_LOAD, 
             RBS_ELEC_APPARENT_LOAD_PHASEA, RBS_ELEC_APPARENT_LOAD_PHASEB, 
             RBS_ELEC_APPARENT_LOAD_PHASEC
        
            Returns: The value of the spare's load parameter
        """
        pass

    def GetTableData(self):
        """
        GetTableData(self: PanelScheduleView) -> PanelScheduleData
        
            Gets table data that can be written to
            Returns: The Autodesk.Revit.DB.Electrical.PanelScheduleData
        """
        pass

    def GetTemplate(self):
        """
        GetTemplate(self: PanelScheduleView) -> ElementId
        
            Gets the template for this view (to set the template, you must go through 
             generateInstanceFromTemplate)
        
            Returns: The template id for this view
        """
        pass

    def IsCellInPhaseLoads(self, nRow, nCol):
        """
        IsCellInPhaseLoads(self: PanelScheduleView, nRow: int, nCol: int) -> bool
        
            Check if this cell in the phase loads
        
            nRow: Row Number
            nCol: Column Number
            Returns: True if this cell in the phase loads, false otherwise
        """
        pass

    def IsColumnInLoadSummary(self, nCol):
        """
        IsColumnInLoadSummary(self: PanelScheduleView, nCol: int) -> bool
        
            Check if this column in the load summary
        
            nCol: Column Number
            Returns: Check if this column in the load summary
        """
        pass

    def IsPanelScheduleTemplate(self):
        """
        IsPanelScheduleTemplate(self: PanelScheduleView) -> bool
        
            Check if this is a panel schedule template.
            Returns: Check if this is a panel schedule template.
        """
        pass

    def IsRowInCircuitTable(self, nRow):
        """
        IsRowInCircuitTable(self: PanelScheduleView, nRow: int) -> bool
        
            Check if this row in the circuit table
        
            nRow: Row Number
            Returns: True if this row in the circuit table, false otherwise.
        """
        pass

    def IsSlotGrouped(self, nRow, nCol):
        """
        IsSlotGrouped(self: PanelScheduleView, nRow: int, nCol: int) -> int
        
            Check if the slot is in a group
        
            nRow: Row Number
            nCol: Column Number
            Returns: It is not in a group if the return value equals to 0. It is in a group if the 
             return value is greater than 0 and the return value is the group number.
        """
        pass

    def IsSlotLocked(self, nRow, nCol):
        """
        IsSlotLocked(self: PanelScheduleView, nRow: int, nCol: int) -> bool
        
            Check if the circuit slot in this cell is locked.
        
            nRow: Row Number
            nCol: Column Number
            Returns: True if the circuit slot in this cell is locked, false otherwise
        """
        pass

    def IsSpace(self, nRow, nCol):
        """
        IsSpace(self: PanelScheduleView, nRow: int, nCol: int) -> bool
        
            Check if the selected cell is a space
        
            nRow: Row Number
            nCol: Column Number
            Returns: True if the selected cell is a space, false otherwise
        """
        pass

    def IsSpare(self, nRow, nCol):
        """
        IsSpare(self: PanelScheduleView, nRow: int, nCol: int) -> bool
        
            Check if the circuit is a spare
        
            nRow: Row Number
            nCol: Column Number
            Returns: True if the circuit is a spare, false otherwise
        """
        pass

    def MoveSlotTo(self, nMovingRow, nMovingCol, nToRow, nToCol):
        """
        MoveSlotTo(self: PanelScheduleView, nMovingRow: int, nMovingCol: int, nToRow: int, nToCol: int)
            Move the circuits in the source slot to the specific slot.
        
            nMovingRow: The Row Number of cell to be moved.
            nMovingCol: Start Column Number of cell to be moved.
            nToRow: The Row Number of cell to moved to.
            nToCol: End Column Number of cell to moved to.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetParamValue(self, sectionType, nRow, nCol, sValue):
        """
        SetParamValue(self: PanelScheduleView, sectionType: SectionType, nRow: int, nCol: int, sValue: str) -> bool
        
            Sets the text for the given cell, returns true if successful, false otherwise
        
            sectionType: The associated section
            nRow: Row Number of the Section
            nCol: Column Number of the Section
            sValue: String value to set the parameter
            Returns: Returns whether the function succeeded
        """
        pass

    def SetSpareCurrentValue(self, row, column, idCurrentParameter, value):
        """
        SetSpareCurrentValue(self: PanelScheduleView, row: int, column: int, idCurrentParameter: ElementId, value: float)
            Sets the value of the apparent current parameter for a spare
        
            row: A row where the valid spare is
            column: A column where the valid spare is
            idCurrentParameter: One of 4 valid current parameters: RBS_ELEC_APPARENT_CURRENT_PARAM, 
             RBS_ELEC_APPARENT_CURRENT_PHASEA_PARAM, RBS_ELEC_APPARENT_CURRENT_PHASEB_PARAM, 
             RBS_ELEC_APPARENT_CURRENT_PHASEC_PARAM
        
            value: The value of the spare's current for the given parameter
        """
        pass

    def SetSpareLoadValue(self, row, column, idLoadParameter, value):
        """
        SetSpareLoadValue(self: PanelScheduleView, row: int, column: int, idLoadParameter: ElementId, value: float)
            Sets the value of the apparent load parameter for a spare
        
            row: A row where the valid spare is
            column: A column where the valid spare is
            idLoadParameter: One of 4 valid load parameters: RBS_ELEC_APPARENT_LOAD, 
             RBS_ELEC_APPARENT_LOAD_PHASEA, RBS_ELEC_APPARENT_LOAD_PHASEB, 
             RBS_ELEC_APPARENT_LOAD_PHASEC
        
            value: The value of the spare's load for the given parameter
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


class PowerFactorStateType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible power factor state types for a connector object.
    
    enum PowerFactorStateType, values: Lagging (1), Leading (0)
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

    Lagging = None
    Leading = None
    value__ = None


class TemperatureRatingType(ElementType, IDisposable):
    """ Represents temperature rating type definition information. """
    def AddCorrectionFactor(self, temperature, factor):
        """
        AddCorrectionFactor(self: TemperatureRatingType, temperature: Int64, factor: float) -> CorrectionFactor
        
            Add a new electrical correction factor type to this temperature rating type.
        
            temperature: Temperature of correction factor to be added.
            factor: Factor of correction factor to be added.
            Returns: New constructed correction factor.
        """
        pass

    def AddInsulationType(self, name):
        """
        AddInsulationType(self: TemperatureRatingType, name: str) -> InsulationType
        
            Add a new kind of insulation type into this temperature rating type.
        
            name: Name of insulation type symbol to be constructed and added.
            Returns: Constructed insulation type instance.
        """
        pass

    def AddWireSize(self, size, ampacity, diameter):
        """
        AddWireSize(self: TemperatureRatingType, size: str, ampacity: Int64, diameter: float) -> WireSize
        
            Add a new kind of wire size type into this temperature rating type.
        
            size: Size of wire size.
            ampacity: Ampacity of wire size to be added.
            diameter: Diameter of wire size to be added.
            Returns: Constructed wire size type.
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

    def RemoveCorrectionFactor(self, correctionFactor):
        """
        RemoveCorrectionFactor(self: TemperatureRatingType, correctionFactor: CorrectionFactor)
            Remove an existing correction factor from this temperature rating type in Revit 
             MEP project.
        
        
            correctionFactor: The correction factor to be removed.
            Returns: New constructed correction factor.
        """
        pass

    def RemoveInsulationType(self, insulationType):
        """
        RemoveInsulationType(self: TemperatureRatingType, insulationType: InsulationType)
            Remove an existing insulation type from this temperature rating type.
        
            insulationType: Insulation type to be removed.
        """
        pass

    def RemoveWireSize(self, wireSize):
        """
        RemoveWireSize(self: TemperatureRatingType, wireSize: WireSize)
            Remove an existing wire size type from this temperature rating type.
        
            wireSize: The wire size type to be removed.
        """
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

    CorrectionFactors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all correction factors defined in this temperature rating type and its corresponding material type.

Get: CorrectionFactors(self: TemperatureRatingType) -> CorrectionFactorSet

"""

    InsulationTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all insulation types defined in this temperature rating type and its corresponding material type.

Get: InsulationTypes(self: TemperatureRatingType) -> InsulationTypeSet

"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the temperature rating type is in use.

Get: IsInUse(self: TemperatureRatingType) -> bool

"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the material type information which this temperature rating type belongs to.

Get: MaterialType(self: TemperatureRatingType) -> WireMaterialType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get name of temperature rating type.

Set: Name(self: TemperatureRatingType) = value
"""

    WireSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all electrical wire sizes defined in this temperature rating type and its corresponding material type.

Get: WireSizes(self: TemperatureRatingType) -> WireSizeSet

"""



class TemperatureRatingTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains TemperatureRating types.
    
    TemperatureRatingTypeSet()
    """
    def Clear(self):
        """
        Clear(self: TemperatureRatingTypeSet)
            Removes every TemperatureRating type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> bool
        
            Tests for the existence of a TemperatureRating type within the set.
        
            item: The TemperatureRating type to be searched for.
            Returns: The Contains method returns True if the TemperatureRating type is within the 
             set, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: TemperatureRatingTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> int
        
            Removes a specified TemperatureRating type from the set.
        
            item: The TemperatureRating type to be erased.
            Returns: The number of TemperatureRating types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: TemperatureRatingTypeSet) -> TemperatureRatingTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TemperatureRatingTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> bool
        
            Insert the specified TemperatureRating type into the set.
        
            item: The TemperatureRating type to be inserted into the set.
            Returns: Returns whether the TemperatureRating type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TemperatureRatingTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: TemperatureRatingTypeSet) -> TemperatureRatingTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: TemperatureRatingTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of TemperatureRating types that are in the set.

Get: Size(self: TemperatureRatingTypeSet) -> int

"""



class TemperatureRatingTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a TemperatureRating type set.
    
    TemperatureRatingTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: TemperatureRatingTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: TemperatureRatingTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TemperatureRatingTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: TemperatureRatingTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: TemperatureRatingTypeSetIterator) -> object

"""



class VoltageType(ElementType, IDisposable):
    """
    Represents electrical voltage type. An electrical voltage type define a range of voltages,
    and circuits can be created between components with rated voltages that do not precisely match the voltage definition value.
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

    def SetVoltageValue(self, actualValue, minValue, maxValue):
        """
        SetVoltageValue(self: VoltageType, actualValue: float, minValue: float, maxValue: float)
            Assign new values to modify voltage type, all of the unit are volt.
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

    ActualValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get actual voltage value of this voltage definition, the unit is volt.

Get: ActualValue(self: VoltageType) -> float

"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this voltage type is in service now, such as by other distribution system.

Get: IsInUse(self: VoltageType) -> bool

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get upper boundary of voltage value of this voltage definition, the unit is volt.

Get: MaxValue(self: VoltageType) -> float

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get lower boundary of voltage value of this voltage definition, the unit is volt.

Get: MinValue(self: VoltageType) -> float

"""



class VoltageTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains voltage types.
    
    VoltageTypeSet()
    """
    def Clear(self):
        """
        Clear(self: VoltageTypeSet)
            Removes every voltage type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: VoltageTypeSet, item: VoltageType) -> bool
        
            Tests for the existence of a voltage type within the set.
        
            item: The voltage type to be searched for.
            Returns: The Contains method returns True if the voltage type is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: VoltageTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: VoltageTypeSet, item: VoltageType) -> int
        
            Removes a specified voltage type from the set.
        
            item: The voltage type to be erased.
            Returns: The number of voltage types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: VoltageTypeSet) -> VoltageTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: VoltageTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: VoltageTypeSet, item: VoltageType) -> bool
        
            Insert the specified voltage type into the set.
        
            item: The voltage type to be inserted into the set.
            Returns: Returns whether the voltage type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VoltageTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: VoltageTypeSet) -> VoltageTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: VoltageTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of voltage types that are in the set.

Get: Size(self: VoltageTypeSet) -> int

"""



class VoltageTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a voltage type set.
    
    VoltageTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: VoltageTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: VoltageTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: VoltageTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: VoltageTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: VoltageTypeSetIterator) -> object

"""



class Wire(MEPCurve, IDisposable):
    """ Electrical wire element. """
    def AppendVertex(self, vertexPoint):
        """
        AppendVertex(self: Wire, vertexPoint: XYZ)
            Appends one vertex to the end of the wire.
        
            vertexPoint: The vertex to be appended.
        """
        pass

    @staticmethod
    def AreVertexPointsValid(vertexPoints, startConnector, endConnector):
        """ AreVertexPointsValid(vertexPoints: IList[XYZ], startConnector: Connector, endConnector: Connector) -> bool """
        pass

    def ConnectTo(self, startConnectorTo, endConnectorTo):
        """
        ConnectTo(self: Wire, startConnectorTo: Connector, endConnectorTo: Connector)
            Connects the wire to other elements.
        
            startConnectorTo: The connector that the start connector of the wire connects to.
            endConnectorTo: The connector that the end connector of the wire connects to.
        """
        pass

    @staticmethod
    def Create(document, wireTypeId, viewId, wiringType, vertexPoints, startConnectorTo, endConnectorTo):
        """ Create(document: Document, wireTypeId: ElementId, viewId: ElementId, wiringType: WiringType, vertexPoints: IList[XYZ], startConnectorTo: Connector, endConnectorTo: Connector) -> Wire """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetMEPSystems(self):
        """
        GetMEPSystems(self: Wire) -> IList[ElementId]
        
            Gets the systems to which the wire belongs.
            Returns: The systems to which the wire belongs.
        """
        pass

    def GetVertex(self, index):
        """
        GetVertex(self: Wire, index: int) -> XYZ
        
            Gets the position of an existing vertex.
        
            index: The index of the existing vertex. Should be between 0 and 
             Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.
        
            Returns: The position of the vertex.
        """
        pass

    def InsertVertex(self, index, vertexPoint):
        """
        InsertVertex(self: Wire, index: int, vertexPoint: XYZ)
            Inserts a new vertex before the specified index.
        
            index: The index of the vertex to come after this new vertex. Should be between 0 and 
             Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.
        
            vertexPoint: The point of the new vertex.
        """
        pass

    def IsVertexPointValid(self, vertexPoint):
        """
        IsVertexPointValid(self: Wire, vertexPoint: XYZ) -> bool
        
            Checks if the given vertex point can be added to this wire.
        
            vertexPoint: The vertex point.
            Returns: True if the vertex point can be added, false if the point cannot be added 
             because there is already a vertex at this position on the view plane (within 
             tolerance).
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveVertex(self, index):
        """
        RemoveVertex(self: Wire, index: int)
            Removes the vertex corresponding to the specified index.
           Can not remove the 
             start or end vertex if it already connects to other element.
        
        
            index: The index which should be in [0, NumberOfVertices).
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetVertex(self, index, vertexPoint):
        """
        SetVertex(self: Wire, index: int, vertexPoint: XYZ)
            Sets the position of a given vertex.
           If the vertex is start or end point, 
             and the wire connects to electrical device, the wire end offset will be set 
             according to the given vertex.
           If the vertex is start or end point, and the 
             wire connects to other wire, user can't set the vertex and exception will be 
             thrown.
           If the vertex is start or end point, and the wire connects to 
             nothing, the vertex will be set as the given vertex.
        
        
            index: The index of the existing vertex. Should be between 0 and 
             Autodesk.Revit.DB.Electrical.Wire.NumberOfVertices.
        
            vertexPoint: The new position for the vertex.
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

    GroundConductorNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ground conductor number. Its default value is zero after created.

Get: GroundConductorNum(self: Wire) -> int

Set: GroundConductorNum(self: Wire) = value
"""

    HotConductorNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hot conductor number. Its default value is zero after created.

Get: HotConductorNum(self: Wire) -> int

Set: HotConductorNum(self: Wire) = value
"""

    NeutralConductorNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The neutral conductor number. Its default value is zero after created.

Get: NeutralConductorNum(self: Wire) -> int

Set: NeutralConductorNum(self: Wire) = value
"""

    NumberOfVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of vertices of the wire, including the start and end point.

Get: NumberOfVertices(self: Wire) -> int

"""

    WiringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wiring type(arc or chamfer) for the wire.

Get: WiringType(self: Wire) -> WiringType

Set: WiringType(self: Wire) = value
"""



class WireConduitType(APIObject, IDisposable):
    """ Represents a specific conduit type of wire type. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: WireConduitType) -> str

"""



class WireConduitTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains conduit types.
    
    WireConduitTypeSet()
    """
    def Clear(self):
        """
        Clear(self: WireConduitTypeSet)
            Removes every conduit type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: WireConduitTypeSet, item: WireConduitType) -> bool
        
            Tests for the existence of a conduit type within the set.
        
            item: The conduit type to be searched for.
            Returns: The Contains method returns True if the conduit type is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: WireConduitTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: WireConduitTypeSet, item: WireConduitType) -> int
        
            Removes a specified conduit type from the set.
        
            item: The conduit type to be erased.
            Returns: The number of conduit types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireConduitTypeSet) -> WireConduitTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireConduitTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: WireConduitTypeSet, item: WireConduitType) -> bool
        
            Insert the specified conduit type into the set.
        
            item: The conduit type to be inserted into the set.
            Returns: Returns whether the conduit type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireConduitTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireConduitTypeSet) -> WireConduitTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireConduitTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of conduit types that are in the set.

Get: Size(self: WireConduitTypeSet) -> int

"""



class WireConduitTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a conduit type set.
    
    WireConduitTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: WireConduitTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: WireConduitTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireConduitTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: WireConduitTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: WireConduitTypeSetIterator) -> object

"""



class WireMaterialType(ElementType, IDisposable):
    """ Represents electrical wire material type definition information of wire type. """
    def AddGroundConductorSize(self, ampacity, size):
        """
        AddGroundConductorSize(self: WireMaterialType, ampacity: Int64, size: str) -> GroundConductorSize
        
            Add new electrical ground conductor size type into this material type.
        
            ampacity: Ampacity of ground conductor size to be added.
            size: Size of ground conductor size to be added.
            Returns: New added ground conductor size.
        """
        pass

    def AddTemperatureRatingType(self, name, baseOn):
        """
        AddTemperatureRatingType(self: WireMaterialType, name: str, baseOn: TemperatureRatingType) -> TemperatureRatingType
        
            Add a new temperature rating type into material type.
        
            name: Name of temperature type to be added.
            baseOn: The new temperature rating will be created base on this existing temperature 
             rating type.
        
            Returns: New constructed temperature rating type.
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

    def RemoveGroundConductorSize(self, grdConductorSize):
        """
        RemoveGroundConductorSize(self: WireMaterialType, grdConductorSize: GroundConductorSize)
            Remove an existing ground conductor size from this material type.
        
            grdConductorSize: The ground size type to be removed.
        """
        pass

    def RemoveTemperatureRatingType(self, temperatureRating):
        """
        RemoveTemperatureRatingType(self: WireMaterialType, temperatureRating: TemperatureRatingType)
            Remove an existing temperature rating type from this material type.
        
            temperatureRating: The temperature rating type to be removed.
        """
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

    GroundConductorSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all ground conductor size types defined in this wire material type.

Get: GroundConductorSizes(self: WireMaterialType) -> GroundConductorSizeSet

"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the wire material type is in use.

Get: IsInUse(self: WireMaterialType) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get name of wire material type.

Set: Name(self: WireMaterialType) = value
"""

    TemperatureRatings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all temperature rating type definitions defined in this wire material type.

Get: TemperatureRatings(self: WireMaterialType) -> TemperatureRatingTypeSet

"""



class WireMaterialTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains wire material types.
    
    WireMaterialTypeSet()
    """
    def Clear(self):
        """
        Clear(self: WireMaterialTypeSet)
            Removes every wire material type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: WireMaterialTypeSet, item: WireMaterialType) -> bool
        
            Tests for the existence of a wire material type within the set.
        
            item: The wire material type to be searched for.
            Returns: The Contains method returns True if the wire material type is within the set, 
             otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: WireMaterialTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: WireMaterialTypeSet, item: WireMaterialType) -> int
        
            Removes a specified wire material type from the set.
        
            item: The wire material type to be erased.
            Returns: The number of wire material types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireMaterialTypeSet) -> WireMaterialTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireMaterialTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: WireMaterialTypeSet, item: WireMaterialType) -> bool
        
            Insert the specified wire material type into the set.
        
            item: The wire material type to be inserted into the set.
            Returns: Returns whether the wire material type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireMaterialTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireMaterialTypeSet) -> WireMaterialTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireMaterialTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of wire material types that are in the set.

Get: Size(self: WireMaterialTypeSet) -> int

"""



class WireMaterialTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a wire material type set.
    
    WireMaterialTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: WireMaterialTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: WireMaterialTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireMaterialTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: WireMaterialTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: WireMaterialTypeSetIterator) -> object

"""



class WireSet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contain any type of object.
    
    WireSet()
    """
    def Clear(self):
        """
        Clear(self: WireSet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """ Contains(self: WireSet, item: Wire) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: WireSet, A_0: bool) """
        pass

    def Erase(self, item):
        """ Erase(self: WireSet, item: Wire) -> int """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireSet) -> WireSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """ Insert(self: WireSet, item: Wire) -> bool """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireSet) -> WireSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the set.

Get: Size(self: WireSet) -> int

"""



class WireSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a set.
    
    WireSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: WireSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: WireSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: WireSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: WireSetIterator) -> object

"""



class WireSize(APIObject, IDisposable):
    """ Represents specific electrical wire size information. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Ampacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get ampacity which be used for specifying size, the unit is ampere.

Get: Ampacity(self: WireSize) -> Int64

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get diameter of wire.

Get: Diameter(self: WireSize) -> float

"""

    InUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set whether the size can be used in sizing.

Get: InUse(self: WireSize) -> bool

Set: InUse(self: WireSize) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get size symbol of wire.

Get: Size(self: WireSize) -> str

"""



class WireSizeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains wire sizes.
    
    WireSizeSet()
    """
    def Clear(self):
        """
        Clear(self: WireSizeSet)
            Removes every wire size from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: WireSizeSet, item: WireSize) -> bool
        
            Tests for the existence of a wire size within the set.
        
            item: The wire size to be searched for.
            Returns: The Contains method returns True if the wire size is within the set, otherwise 
             False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: WireSizeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: WireSizeSet, item: WireSize) -> int
        
            Removes a specified wire size from the set.
        
            item: The wire size to be erased.
            Returns: The number of wire sizes that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireSizeSet) -> WireSizeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireSizeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: WireSizeSet, item: WireSize) -> bool
        
            Insert the specified wire size into the set.
        
            item: The wire size to be inserted into the set.
            Returns: Returns whether the wire size was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireSizeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireSizeSet) -> WireSizeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireSizeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of wire sizes that are in the set.

Get: Size(self: WireSizeSet) -> int

"""



class WireSizeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a wire size set.
    
    WireSizeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: WireSizeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: WireSizeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireSizeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: WireSizeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: WireSizeSetIterator) -> object

"""



class WireType(ElementType, IDisposable):
    """ Represents a specific wire type. """
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

    Conduit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The conduit type of the wire type.

Get: Conduit(self: WireType) -> WireConduitType

Set: Conduit(self: WireType) = value
"""

    Insulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The insulation type.

Get: Insulation(self: WireType) -> InsulationType

Set: Insulation(self: WireType) = value
"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the wire type is in use.

Get: IsInUse(self: WireType) -> bool

"""

    MaxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The max size of the wire type.

Get: MaxSize(self: WireType) -> WireSize

Set: MaxSize(self: WireType) = value
"""

    NeutralMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The neutral multiplier type of the wire type.

Get: NeutralMultiplier(self: WireType) -> float

Set: NeutralMultiplier(self: WireType) = value
"""

    NeutralRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the neutral point is required.

Get: NeutralRequired(self: WireType) -> bool

Set: NeutralRequired(self: WireType) = value
"""

    NeutralSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum neutral size of the wire type.

Get: NeutralSize(self: WireType) -> NeutralMode

Set: NeutralSize(self: WireType) = value
"""

    TemperatureRating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The temperature rating type of the wire type.

Get: TemperatureRating(self: WireType) -> TemperatureRatingType

Set: TemperatureRating(self: WireType) = value
"""

    WireMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The material type of the wire type.

Get: WireMaterial(self: WireType) -> WireMaterialType

Set: WireMaterial(self: WireType) = value
"""



class WireTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains wire types.
    
    WireTypeSet()
    """
    def Clear(self):
        """
        Clear(self: WireTypeSet)
            Removes every wire type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: WireTypeSet, item: WireType) -> bool
        
            Tests for the existence of a wire type within the set.
        
            item: The wire type to be searched for.
            Returns: The Contains method returns True if the wire type is within the set, otherwise 
             False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: WireTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: WireTypeSet, item: WireType) -> int
        
            Removes a specified wire type from the set.
        
            item: The wire type to be erased.
            Returns: The number of wire types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: WireTypeSet) -> WireTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: WireTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: WireTypeSet, item: WireType) -> bool
        
            Insert the specified wire type into the set.
        
            item: The wire type to be inserted into the set.
            Returns: Returns whether the wire type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: WireTypeSet) -> WireTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: WireTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of wire types that are in the set.

Get: Size(self: WireTypeSet) -> int

"""



class WireTypeSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a wire type set.
    
    WireTypeSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: WireTypeSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: WireTypeSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WireTypeSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: WireTypeSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: WireTypeSetIterator) -> object

"""



class WiringType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type to list all wiring types.
    
    enum WiringType, values: Arc (0), Chamfer (1)
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

    Arc = None
    Chamfer = None
    value__ = None


