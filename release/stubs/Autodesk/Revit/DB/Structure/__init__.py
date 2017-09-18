# encoding: utf-8
# module Autodesk.Revit.DB.Structure calls itself Structure
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AnalyticalAlignmentMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how analytical model is being aligned in space
    
    enum AnalyticalAlignmentMethod, values: AutoDetect (0), ManuallyAdjusted (2), Projection (1), Varies (3)
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

    AutoDetect = None
    ManuallyAdjusted = None
    Projection = None
    value__ = None
    Varies = None


class AnalyticalConsistencyChecking(object):
    """ Utilities that allow for detection of incorrect or incomplete analytical consistency. """
    @staticmethod
    def CheckAnalyticalConsistency(document):
        """
        CheckAnalyticalConsistency(document: Document) -> bool
        
            Checks consistency of the Analytical Model.
        
            document: Document in which to perform consistency checks.
            Returns: True if run succeeded, false otherwise.
        """
        pass

    __all__ = [
        'CheckAnalyticalConsistency',
    ]


class AnalyticalCurveSelector(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies which portion of an Analytical Curve is of interest.
    
    enum AnalyticalCurveSelector, values: EndPoint (1), StartPoint (0), WholeCurve (2)
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

    EndPoint = None
    StartPoint = None
    value__ = None
    WholeCurve = None


class AnalyticalCurveType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies what type of Analytical Model curves should be extracted.
    
    enum AnalyticalCurveType, values: ActiveCurves (3), AllRigidLinks (6), ApproximatedCurves (4), BaseCurve (5), RawCurves (0), RigidLinkHead (1), RigidLinkTail (2)
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

    ActiveCurves = None
    AllRigidLinks = None
    ApproximatedCurves = None
    BaseCurve = None
    RawCurves = None
    RigidLinkHead = None
    RigidLinkTail = None
    value__ = None


class AnalyticalDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies a direction for manipulating analytical model.
    
    enum AnalyticalDirection, values: Any (6), Horizontal (3), HorizontalEnd (5), HorizontalStart (4), Vertical (0), VerticalBottom (2), VerticalTop (1), X (7), Y (8), Z (9)
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

    Any = None
    Horizontal = None
    HorizontalEnd = None
    HorizontalStart = None
    value__ = None
    Vertical = None
    VerticalBottom = None
    VerticalTop = None
    X = None
    Y = None
    Z = None


class AnalyticalElementSelector(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies a portion of an Analytical Element or the whole element.
    
    enum AnalyticalElementSelector, values: EndOrTop (1), StartOrBase (0), Whole (2)
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

    EndOrTop = None
    StartOrBase = None
    value__ = None
    Whole = None


class AnalyticalFixityState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the fixity setting of individual degrees of freedom in analytical release conditions.
    
    enum AnalyticalFixityState, values: Fixed (0), Released (1), Spring (2)
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

    Fixed = None
    Released = None
    Spring = None
    value__ = None


class AnalyticalLink(Element, IDisposable):
    """ An analytical link element that is used to create connections between other AnalyticalModel elements. """
    @staticmethod
    def Create(doc, type, startHubId, endHubId):
        """
        Create(doc: Document, type: ElementId, startHubId: ElementId, endHubId: ElementId) -> AnalyticalLink
        
            Creates a new instance of a AnalyticalLink element between two Hubs.
        
            doc: Document to which new AnalyticalLink should be added.
            type: AnalyticalLinkType for the new AnalyticalLink.
            startHubId: Hub at start of AnalyticalLink.
            endHubId: Hub at end of AnalyticalLink.
            Returns: The newly created AnalyticalLink instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsAutoGenerated(self):
        """
        IsAutoGenerated(self: AnalyticalLink) -> bool
        
            Specifies whether or not an AnalyticalLink was created by an AnalyticalModel 
             element.
        
            Returns: True if AnalyticalLink was created by an AnalyticalModel element, false 
             otherwise.
        """
        pass

    @staticmethod
    def IsValidHub(doc, hubId):
        """
        IsValidHub(doc: Document, hubId: ElementId) -> bool
        
            Checks whether input hub is valid for an AnalyticalLink.
        
            doc: Hubs's document.
            hubId: Hub to test for validity.
            Returns: True is returned when provided hubId points hub that is valid for 
             AnalyticalLink, false otherwise.
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

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point at the end of the AnalyticalLink.

Get: End(self: AnalyticalLink) -> XYZ

"""

    EndHubId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hub ID at end of AnalyticalLink.

Get: EndHubId(self: AnalyticalLink) -> ElementId

"""

    OwnerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ElementId of AnalyticalModel element which created the AnalyticalLink (if any)
   invalidElementId if this Analytical Link was created by the User or API

Get: OwnerId(self: AnalyticalLink) -> ElementId

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point at the start of the AnalyticalLink.

Get: Start(self: AnalyticalLink) -> XYZ

"""

    StartHubId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hub ID at start of AnalyticalLink.

Get: StartHubId(self: AnalyticalLink) -> ElementId

"""



class AnalyticalLinkType(ElementType, IDisposable):
    """ An object that specifies the analysis properties for an AnalyticalLink element. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidAnalyticalFixityState(fixityState):
        """
        IsValidAnalyticalFixityState(fixityState: AnalyticalFixityState) -> bool
        
            Returns whether the input fixity state is valid for Analytical Link Type 
             parameters.
        
        
            fixityState: The fixity state value to check.
            Returns: True if valid.
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

    RotationX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around X.

Get: RotationX(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationX(self: AnalyticalLinkType) = value
"""

    RotationY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around Y.

Get: RotationY(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationY(self: AnalyticalLinkType) = value
"""

    RotationZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around Z.

Get: RotationZ(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationZ(self: AnalyticalLinkType) = value
"""

    TranslationX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along X.

Get: TranslationX(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationX(self: AnalyticalLinkType) = value
"""

    TranslationY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along Y.

Get: TranslationY(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationY(self: AnalyticalLinkType) = value
"""

    TranslationZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along Z.

Get: TranslationZ(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationZ(self: AnalyticalLinkType) = value
"""



class AnalyticalLoopType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies kind of analytical model loop.
    
    enum AnalyticalLoopType, values: All (0), External (1), Filled (3), Internal (2), Void (4)
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

    All = None
    External = None
    Filled = None
    Internal = None
    value__ = None
    Void = None


class AnalyticalModel(Element, IDisposable):
    """ AnalyticalModel represents the Analytical Model portion of a given Structural Element. """
    def Approximate(self, enableApproximation):
        """
        Approximate(self: AnalyticalModel, enableApproximation: bool)
            Switches between non-approximated (e.g., Curved) Analytical Models
           and 
             approximated (made up of lines only) Analytical Models
        
        
            enableApproximation: Enable/disable approximated function.
        """
        pass

    def CanApproximate(self):
        """
        CanApproximate(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model can be approximated or not.
            Returns: True if Analytical Model can be approximated; false otherwise.
        """
        pass

    def CanDisableAutoDetect(self, direction):
        """
        CanDisableAutoDetect(self: AnalyticalModel, direction: AnalyticalDirection) -> bool
        
            Indicates if Analytical Auto-detect can be disabled programmatically
        
            direction: Direction in which to test whether Analytical Auto-detect can be disabled
            Returns: True if Analytical Auto-detect can be disabled, false otherwise
        """
        pass

    def CanHaveRigidLinks(self):
        """
        CanHaveRigidLinks(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model supports Rigid Links.
            Returns: True if Analytical Model supports Rigid Links; false otherwise.
        """
        pass

    def CanUseHardPoints(self):
        """
        CanUseHardPoints(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model can use Hard Points.
            Returns: True if Analytical Model can use Hard Points, false otherwise.
        """
        pass

    def CloneAdjustment(self, source, end):
        """
        CloneAdjustment(self: AnalyticalModel, source: AnalyticalModel, end: int)
            The method clones the adjustment of one end of the AM on another AM,
           with 
             respect to the one of the ends.
           One of the Analytical Model ends
        """
        pass

    def Disconnect(self, selector):
        """
        Disconnect(self: AnalyticalModel, selector: AnalyticalElementSelector)
            Unjoin from Hub Element.
        
            selector: End of the analytical model.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Enable(self, enable):
        """
        Enable(self: AnalyticalModel, enable: bool)
            Enables or disables Analytical Model, if the Element allows a one-operation 
             Analytical Model toggle.
        
        
            enable: Enable (true) or disable (false) Analytical Model.
        """
        pass

    def EnableAutoDetect(self, direction, enabled):
        """
        EnableAutoDetect(self: AnalyticalModel, direction: AnalyticalDirection, enabled: bool)
            Enable or disable Analytical Auto-detect.
        
            direction: Direction in which to enable Analytical Auto-detect
            enabled: Turn Analytical Auto-detect on (true) or off (false)
        """
        pass

    def GetAnalyticalModelSketchComponents(self):
        """
        GetAnalyticalModelSketchComponents(self: AnalyticalModel) -> IList[AnalyticalModelSketchComponent]
        
            Retrieves a collection of AnalyticalModelSketchComponent objects, which are 
             useful for those Analytical Models
           that have finer calibration below the 
             Element level.
        
            Returns: If the Analytical Model supports Sketch-based adjustment of the Analytical 
             Model,
           then this will return an array of AnalyticalModelSketchComponents.  
             Otherwise, it will
           return an empty array.
        """
        pass

    def GetAnalyticalModelSupports(self):
        """
        GetAnalyticalModelSupports(self: AnalyticalModel) -> IList[AnalyticalModelSupport]
        
            Retrieves the AnalyticalModelSupport array, which is useful to extract 
             Analytical
           Support Information from Elements.
        
            Returns: Array of AnalyticalModelSupport objects, each one representing a support.
        """
        pass

    def GetAnalyzeAs(self):
        """
        GetAnalyzeAs(self: AnalyticalModel) -> AnalyzeAs
        
            Returns value of Analyze As parameter for Analytical Model.
            Returns: AnalyzeAs enumeration, indicating how Analytical Model is analyzed.
        """
        pass

    def GetApproximationDeviation(self):
        """
        GetApproximationDeviation(self: AnalyticalModel) -> float
        
            Retrieves amount by which approximation is made.
            Returns: Maximum distance from approximated line to curve.
           If approximation does not 
             make sense, then this will be 0.0.
        """
        pass

    def GetAutoDetectMatchedElements(self, direction):
        """
        GetAutoDetectMatchedElements(self: AnalyticalModel, direction: AnalyticalDirection) -> ICollection[ElementId]
        
            Retrieves other Element Ids that this Element is Auto-detecting against.
        
            direction: Direction in which Analytical Auto-detect is being done.
            Returns: A set of Element Ids against which this Element is Auto-detecting.
           The set 
             may be empty if this Element is not Auto-detecting against anything.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurve(self):
        """
        GetCurve(self: AnalyticalModel) -> Curve
        
            Returns the single curve of the Analytical Model, if it is only one curve.
            Returns: Single curve of the Analytical Model.
        """
        pass

    def GetCurves(self, curveType):
        """
        GetCurves(self: AnalyticalModel, curveType: AnalyticalCurveType) -> IList[Curve]
        
            Retrieves all curves for the Analytical Model of a given type.
        
            curveType: Which curve type should be returned.
            Returns: An array of curves representing analytical model.
        """
        pass

    def GetElementId(self):
        """
        GetElementId(self: AnalyticalModel) -> ElementId
        
            Retrieves Element Id of the structural element corresponding to the Analytical 
             Model.
        
            Returns: Element Id for a structural element.
        """
        pass

    def GetLocalCoordinateSystem(self):
        """
        GetLocalCoordinateSystem(self: AnalyticalModel) -> Transform
        
            Gets the local coordinate system (LCS) for an analytical model element.
            Returns: Transformation matrix.
           Returns ll for analytical model elements that do not 
             have local coordinate system.
           Origin returned by transform is point for 
             which local coordinate system was calculated.
        """
        pass

    def GetManualAdjustmentMatchedElements(self):
        """
        GetManualAdjustmentMatchedElements(self: AnalyticalModel) -> ICollection[ElementId]
        
            Retrieves other Element Ids against which the Analytical Model has been 
             adjusted.
        
            Returns: Set of Element Ids, representing those Elements against which the Analytical 
             Model has been adjusted.
           The set may be empty if Analytical Model is not 
             participating in locked Manual Analytical Adjustment.
        """
        pass

    def GetOffset(self, selector):
        """
        GetOffset(self: AnalyticalModel, selector: AnalyticalElementSelector) -> XYZ
        
            Gets the offset of the analytical model at end.
        
            selector: End of the analytical model.
            Returns: Offset of analytical model from base analytical model at the given end.
        """
        pass

    def GetPoint(self):
        """
        GetPoint(self: AnalyticalModel) -> XYZ
        
            Retrieves point of the Analytical Model.
            Returns: Point of the Analytical Model.
        """
        pass

    def GetReference(self, selector):
        """
        GetReference(self: AnalyticalModel, selector: AnalyticalModelSelector) -> Reference
        
            Returns a reference to a given curve within the analytical model.
        
            selector: Specifies where in the analytical model the reference lies.
            Returns: Requested reference.
        """
        pass

    def GetRigidLink(self, selector):
        """
        GetRigidLink(self: AnalyticalModel, selector: AnalyticalModelSelector) -> Curve
        
            Returns rigid link curve corresponding to selector.
        
            selector: Identifies from which end of the analytical model to get the Rigid Link.
            Returns: Rigid link satisfying selector.
        """
        pass

    def HasDeletedLinks(self):
        """
        HasDeletedLinks(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model contains deleted Analytical Links.
            Returns: True if contains, false otherwise.
        """
        pass

    def HasRigidLinksWith(self, neighborId):
        """
        HasRigidLinksWith(self: AnalyticalModel, neighborId: ElementId) -> bool
        
            Indicates if Analytical Model has Rigid Links with specified element.
        
            neighborId: neighboring Element, to which Rigid Links may exist.
            Returns: true if Rigid Links exist, false otherwise.
        """
        pass

    def IsAnalyzeAsValid(self, analyzeAs):
        """
        IsAnalyzeAsValid(self: AnalyticalModel, analyzeAs: AnalyzeAs) -> bool
        
            Determines if the given Analyze As parameter is valid for this Element.
        
            analyzeAs: Indicates how Analytical Model is analyzed.
            Returns: True if valid; false otherwise.
        """
        pass

    def IsApproximated(self):
        """
        IsApproximated(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model is approximated or not.
            Returns: True if the Analytical Model is approximated, false otherwise.
           False if 
             approximation is meaningless for Analytical Model.
        """
        pass

    def IsAutoDetectEnabled(self, direction):
        """
        IsAutoDetectEnabled(self: AnalyticalModel, direction: AnalyticalDirection) -> bool
        
            Reports if Analytical Auto-detect for the given direction is enabled.
        
            direction: Direction in which Auto-detect behavior may be enabled.
            Returns: True if enabled in the given direction, false otherwise.
        """
        pass

    def IsElementFullySupported(self):
        """
        IsElementFullySupported(self: AnalyticalModel) -> bool
        
            Indicates if Analytical Model is fully supported.
            Returns: True if Analytical Model is fully supported, false otherwise.
        """
        pass

    def IsEnabled(self):
        """
        IsEnabled(self: AnalyticalModel) -> bool
        
            Reports whether the Analytical Model is enabled or disabled.
            Returns: True if Analytical Model is enabled, false otherwise.
        """
        pass

    def IsManuallyAdjusted(self):
        """
        IsManuallyAdjusted(self: AnalyticalModel) -> bool
        
            Indicates if the Analytical Model has been manually adjusted by the user.
            Returns: True if user has manually adjusted the Analytical Model; false otherwise.
        """
        pass

    def IsModified(self):
        """
        IsModified(self: AnalyticalModel) -> bool
        
            Checks if AM has been adjusted from auto-detect at any end.
        """
        pass

    def IsSingleCurve(self):
        """
        IsSingleCurve(self: AnalyticalModel) -> bool
        
            Indicates if the Analytical Model can be expressed as a single curve.
            Returns: True if Analytical Model can be expressed as a single curve, false otherwise.
        """
        pass

    def IsSinglePoint(self):
        """
        IsSinglePoint(self: AnalyticalModel) -> bool
        
            Indicates if the Analytical Model can be expressed as a single point.
            Returns: True if Analytical Model can be expressed as a single point, false otherwise.
        """
        pass

    def IsValidDirectionForAutoDetect(self, direction):
        """
        IsValidDirectionForAutoDetect(self: AnalyticalModel, direction: AnalyticalDirection) -> bool
        
            Tests if the supplied direction is valid for Analytical Auto-detect.
        
            direction: Direction in which Auto-detect behavior may be valid.
            Returns: True if direction is valid, false otherwise.
        """
        pass

    def IsValidForManualAdjustment(self, reference):
        """
        IsValidForManualAdjustment(self: AnalyticalModel, reference: Reference) -> bool
        
            Indicates if the identified reference is acceptable for Manual Analytical 
             Adjustment.
        
        
            reference: Reference that will be examined.
            Returns: True if reference can be used, false otherwise.
        """
        pass

    def IsValidManualAdjustmentSource(self, source, adjustmentDirection):
        """
        IsValidManualAdjustmentSource(self: AnalyticalModel, source: Reference, adjustmentDirection: AnalyticalDirection) -> bool
        
            Indicates if the identified reference is acceptable as a source for Manual 
             Analytical Adjustment.
        
        
            source: Reference to be examined.
            adjustmentDirection: Direction in which adjustment will occur.
            Returns: True if reference can be used as source; false otherwise.
        """
        pass

    def IsValidManualAdjustmentTarget(self, target, source, direction):
        """
        IsValidManualAdjustmentTarget(self: AnalyticalModel, target: Reference, source: Reference, direction: AnalyticalDirection) -> bool
        
            Indicates if reference is acceptable as a "Target" for Manual Analytical 
             Adjustment.
        
        
            target: Target reference.
            source: Source reference.  This is necessary to avoid illegal conditions.  For instance 
             if Element A
           is manually adjusted against Element B, Element B cannot in 
             general be adjusted against Element A.
        
            direction: Direction in which source Element can be adjusted against target Element.
            Returns: True if reference can be used, false otherwise.
        """
        pass

    def IsValidRigidLinksOption(self, rigidLinksOption):
        """
        IsValidRigidLinksOption(self: AnalyticalModel, rigidLinksOption: AnalyticalRigidLinksOption) -> bool
        
            Indicates if Rigid Links option is valid for the Analytical Model.
        
            rigidLinksOption: Rigid Links option to validate.
            Returns: True if option is valid, false otherwise.
        """
        pass

    def IsValidSelector(self, selector):
        """
        IsValidSelector(self: AnalyticalModel, selector: AnalyticalModelSelector) -> bool
        
            Indicates if the input selector is valid for the Analytical Model.
        
            selector: Portion of the analytical model geometry.
            Returns: True if selector is valid for this Analytical Model, false otherwise.
        """
        pass

    def ManuallyAdjust(self, source, target):
        """
        ManuallyAdjust(self: AnalyticalModel, source: Reference, target: Reference) -> bool
        
            Perform Manual Analytical Adjustment on analytical model, with respect to 
             another Element
        
        
            source: Which part of Analytical Model needs to change.
            target: Which part of another Analytical Model change should be made against.
            Returns: Indicates the successful completion of the Manual Analytical Adjustment 
             operation.
           True if source Element was adjusted successfully, false 
             otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def ResetLinks(self):
        """
        ResetLinks(self: AnalyticalModel)
            The function is trying to recreate analytical link elements that were deleted 
             by the user.
        """
        pass

    def ResetManualAdjustment(self):
        """
        ResetManualAdjustment(self: AnalyticalModel) -> bool
        
            Resets all manual adjustments performed by the user onto the Analytical Model.
            Returns: Indicates the successful reset of all manual adjustment.
           True if reset 
             succeeds, false otherwise.
        """
        pass

    def SetAnalyzeAs(self, analyzeAs):
        """
        SetAnalyzeAs(self: AnalyticalModel, analyzeAs: AnalyzeAs)
            Sets value of Analyze As parameter for this Element.
        
            analyzeAs: Indicates how Analytical Model is analyzed .
        """
        pass

    def SetApproximationDeviation(self, deviation):
        """
        SetApproximationDeviation(self: AnalyticalModel, deviation: float)
            Adjusts the amount by which approximation is made.
        
            deviation: Maximum distance from line to actual curve
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetOffset(self, selector, offset):
        """
        SetOffset(self: AnalyticalModel, selector: AnalyticalElementSelector, offset: XYZ)
            Sets the offset of the analytical model at end.
        
            selector: End of analytical model to offset.
            offset: New offset for end of analytical model.
        """
        pass

    def SetUsesHardPoints(self, hardPoints):
        """
        SetUsesHardPoints(self: AnalyticalModel, hardPoints: bool)
            Sets Hard Points for the Analytical Model.
        
            hardPoints: Enable/disable Hard Points (true = enable).
        """
        pass

    def SupportsManualAdjustment(self):
        """
        SupportsManualAdjustment(self: AnalyticalModel) -> bool
        
            Indicates if the Element supports Manual Analytical Adjustment.
            Returns: True if Manual Adjustment is possible, false otherwise.
        """
        pass

    def UsesHardPoints(self):
        """
        UsesHardPoints(self: AnalyticalModel) -> bool
        
            Indicates if the Analytical Model is using Hard Points during approximation.
            Returns: True if Hard Points are being used, false otherwise.
           False if Hard Points 
             are meaningless for Analytical Model.
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

    RigidLinksOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if parameters indicate if Rigid Links should be formed.

Get: RigidLinksOption(self: AnalyticalModel) -> AnalyticalRigidLinksOption

Set: RigidLinksOption(self: AnalyticalModel) = value
"""



class AnalyticalModelStick(AnalyticalModel, IDisposable):
    """
    An element that represents a stick in the structural analytical model.
       Could be one of beam, brace or column type.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAlignmentMethod(self, selector):
        """
        GetAlignmentMethod(self: AnalyticalModelStick, selector: AnalyticalElementSelector) -> AnalyticalAlignmentMethod
        
            Gets the alignment method for a given selector.
        
            selector: End of the analytical model.
            Returns: The alignment method at a given end.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetLocalCoordinateSystem(self, *__args):
        """
        GetLocalCoordinateSystem(self: AnalyticalModelStick, point: XYZ) -> Transform
        
            Gets the local coordinate system (LCS) reflects analytical model orientation at 
             the specified point.
        
        
            point: The point on the analytical model stick element.
            Returns: Transformation matrix.
           x - longitudinal axis, y - transversal, section - 
             horizontal, strong axis, z - transversal, section - vertical, weak axis, origin 
             - base point of LCS.
        
        GetLocalCoordinateSystem(self: AnalyticalModelStick, parameter: float) -> Transform
        
            Gets the local coordinate system (LCS) reflects analytical model orientation at 
             the specified parameter value along a curve.
        
        
            parameter: The parameter value along a curve that should be in the range [0, 1], where 0 
             represents start and 1 represents end of the element.
        
            Returns: Transformation matrix.
           x - longitudinal axis, y - transversal, section - 
             horizontal, strong axis, z - transversal, section - vertical, weak axis, origin 
             - base point of LCS.
        """
        pass

    def GetMemberForces(self):
        """
        GetMemberForces(self: AnalyticalModelStick) -> IList[MemberForces]
        
            Gets the member forces associated with this element.
            Returns: Returns a collection of Member Forces associated with this element. Empty 
             collection will be returned if element doesn't have any Member Forces.
           To 
             find out with which end member forces are associated use 
             Autodesk::Revit::DB::Structure::MemberForces::Position
           property to obtain a 
             position of Member Forces on element.
        """
        pass

    def GetProjectionPlaneY(self, selector):
        """
        GetProjectionPlaneY(self: AnalyticalModelStick, selector: AnalyticalElementSelector) -> ElementId
        
            Retrieves analytical model projection information for Y direction.
        
            selector: End of the analytical model.
            Returns: Plane on to which analytical model is projected, or invalidElementId if
           not 
             projected to a Plane.
        """
        pass

    def GetProjectionPlaneZ(self, selector):
        """
        GetProjectionPlaneZ(self: AnalyticalModelStick, selector: AnalyticalElementSelector) -> ElementId
        
            Retrieves analytical model projection information for Z direction.
        
            selector: End of the analytical model.
            Returns: Plane on to which analytical model is projected, or invalidElementId if
           not 
             projected to a Plane.
        """
        pass

    def GetProjectionY(self, selector):
        """
        GetProjectionY(self: AnalyticalModelStick, selector: AnalyticalElementSelector) -> StickElementProjectionY
        
            Retrieves analytical model projection information for Y direction.
        
            selector: End of the analytical model.
            Returns: Indicates if the projection is a preset value, or refers to a Plane.
        """
        pass

    def GetProjectionZ(self, selector):
        """
        GetProjectionZ(self: AnalyticalModelStick, selector: AnalyticalElementSelector) -> StickElementProjectionZ
        
            Retrieves analytical model projection information for Z direction.
        
            selector: End of the analytical model.
            Returns: Indicates if the projection is a preset value, or refers to a Plane.
        """
        pass

    def GetReleases(self, start, fx, fy, fz, mx, my, mz):
        """
        GetReleases(self: AnalyticalModelStick, start: bool) -> (bool, bool, bool, bool, bool, bool)
        
            Gets the releases of element.
        
            start: The position on analytical model stick element. True for start, false for end.
        """
        pass

    def GetReleaseType(self, start):
        """
        GetReleaseType(self: AnalyticalModelStick, start: bool) -> ReleaseType
        
            Gets the release type.
        
            start: The position on analytical model stick element. True for start, false for end.
            Returns: The type of release.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveAllMemberForces(self):
        """
        RemoveAllMemberForces(self: AnalyticalModelStick) -> bool
        
            Removes all member forces associated with element.
            Returns: True if any member forces were removed, false otherwise.
        """
        pass

    def RemoveMemberForces(self, start):
        """
        RemoveMemberForces(self: AnalyticalModelStick, start: bool) -> bool
        
            Removes member forces defined for given position.
        
            start: Member Forces position on analytical model stick element. True for start, false 
             for end.
        
            Returns: True if member forces for provided position were removed, false otherwise.
        """
        pass

    def SetAlignmentMethod(self, selector, method):
        """
        SetAlignmentMethod(self: AnalyticalModelStick, selector: AnalyticalElementSelector, method: AnalyticalAlignmentMethod)
            Sets the alignment method for a given selector.
        
            selector: End of the analytical model.
            method: The alignment method at a given end.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetMemberForces(self, *__args):
        """
        SetMemberForces(self: AnalyticalModelStick, start: bool, force: XYZ, moment: XYZ)
            Adds Member Forces to element.
        
            start: Member Forces position on analytical model stick element. True for start, false 
             for end.
        
            force: The translational forces at specified position of the element.
           The x value 
             of XYZ object represents force along x-axis of the analytical model coordinate 
             system, y along y-axis, z along z-axis respectively.
        
            moment: The rotational forces at specified position of the element.
           The x value of 
             XYZ object represents moment about x-axis of the analytical model coordinate 
             system, y about y-axis, z about z-axis respectively.
        
        SetMemberForces(self: AnalyticalModelStick, memberForces: MemberForces)
            Sets Member Forces to element.
        
            memberForces: End to which member forces will be added is defined by setting 
             Autodesk::Revit::DB::Structure::MemberForces::Position
           property in provided 
             Member Forces object.
        """
        pass

    def SetProjection(self, selector, *__args):
        """
        SetProjection(self: AnalyticalModelStick, selector: AnalyticalElementSelector, planeIdY: ElementId, projectionZ: StickElementProjectionZ)
            Sets the analytical model projection to a preset value.
        
            selector: End of the analytical model.
            planeIdY: Plane on to which analytical model may be projected in Y direction.
           Plane 
             identifies a Level, a Grid, or a Ref Plane.
        
            projectionZ: Preset value for Analytical Model Stick projection Z.
        SetProjection(self: AnalyticalModelStick, selector: AnalyticalElementSelector, projectionY: StickElementProjectionY, projectionZ: StickElementProjectionZ)
            Sets the analytical model projection to a preset value.
        
            selector: End of the analytical model.
            projectionY: Preset value for Analytical Model Stick projection Y.
            projectionZ: Preset value for Analytical Model Stick projection Z.
        SetProjection(self: AnalyticalModelStick, selector: AnalyticalElementSelector, planeIdY: ElementId, planeIdZ: ElementId)
            Sets the analytical model projection to a preset value.
        
            selector: End of the analytical model.
            planeIdY: Plane on to which analytical model may be projected in Y direction.
           Plane 
             identifies a Level, a Grid, or a Ref Plane.
        
            planeIdZ: Plane on to which analytical model may be projected in Z direction.
           Plane 
             identifies a Level, a Grid, or a Ref Plane.
        
        SetProjection(self: AnalyticalModelStick, selector: AnalyticalElementSelector, projectionY: StickElementProjectionY, planeIdZ: ElementId)
            Sets the analytical model projection to a preset value.
        
            selector: End of the analytical model.
            projectionY: Preset value for Analytical Model Stick projection Y.
            planeIdZ: Plane on to which analytical model may be projected in Z direction.
           Plane 
             identifies a Level, a Grid, or a Ref Plane.
        """
        pass

    def SetReleases(self, start, fx, fy, fz, mx, my, mz):
        """
        SetReleases(self: AnalyticalModelStick, start: bool, fx: bool, fy: bool, fz: bool, mx: bool, my: bool, mz: bool)
            Sets the releases of element.
        
            start: The position on analytical model stick element. True for start, false for end.
        """
        pass

    def SetReleaseType(self, start, releaseType):
        """
        SetReleaseType(self: AnalyticalModelStick, start: bool, releaseType: ReleaseType)
            Sets the release type.
        
            start: The position on analytical model stick element. True for start, false for end.
            releaseType: The type of release.
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


class AnalyticalModelColumn(AnalyticalModelStick, IDisposable):
    """ An element that represents the structural analytical model column. """
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

    BaseExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base extension option.

Get: BaseExtension(self: AnalyticalModelColumn) -> StickElementExtension

Set: BaseExtension(self: AnalyticalModelColumn) = value
"""

    BaseExtensionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom extension method option.

Get: BaseExtensionMethod(self: AnalyticalModelColumn) -> AnalyticalAlignmentMethod

Set: BaseExtensionMethod(self: AnalyticalModelColumn) = value
"""

    BaseExtensionPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom extension plane ID option.

Get: BaseExtensionPlaneId(self: AnalyticalModelColumn) -> ElementId

Set: BaseExtensionPlaneId(self: AnalyticalModelColumn) = value
"""

    TopExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension option.

Get: TopExtension(self: AnalyticalModelColumn) -> StickElementExtension

Set: TopExtension(self: AnalyticalModelColumn) = value
"""

    TopExtensionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension method option.

Get: TopExtensionMethod(self: AnalyticalModelColumn) -> AnalyticalAlignmentMethod

Set: TopExtensionMethod(self: AnalyticalModelColumn) = value
"""

    TopExtensionPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension plane ID option.

Get: TopExtensionPlaneId(self: AnalyticalModelColumn) -> ElementId

Set: TopExtensionPlaneId(self: AnalyticalModelColumn) = value
"""



class AnalyticalModelSelector(object, IDisposable):
    """
    Defines a portion of an Analytical Model for an Element.
    
    AnalyticalModelSelector(curve: Curve)
    AnalyticalModelSelector(curve: Curve, inCurveSelector: AnalyticalCurveSelector)
    AnalyticalModelSelector()
    AnalyticalModelSelector(inCurveSelector: AnalyticalCurveSelector)
    """
    def Dispose(self):
        """ Dispose(self: AnalyticalModelSelector) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalyticalModelSelector, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, curve: Curve)
        __new__(cls: type, curve: Curve, inCurveSelector: AnalyticalCurveSelector)
        __new__(cls: type)
        __new__(cls: type, inCurveSelector: AnalyticalCurveSelector)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurveSelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The portion of the curve to be selected.

Get: CurveSelector(self: AnalyticalModelSelector) -> AnalyticalCurveSelector

Set: CurveSelector(self: AnalyticalModelSelector) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalyticalModelSelector) -> bool

"""



class AnalyticalModelSketchComponent(object, IDisposable):
    """ This is one component of an AnalyticalModelSketch, which exists to provide greater granularity over the Analytical Model than at the Element level. """
    def Dispose(self):
        """ Dispose(self: AnalyticalModelSketchComponent) """
        pass

    def EnableAutoDetect(self):
        """
        EnableAutoDetect(self: AnalyticalModelSketchComponent)
            Enables Auto-detect on Sketch Component.
        """
        pass

    def GetAnalyticalAlignmentMethod(self):
        """
        GetAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent) -> AnalyticalAlignmentMethod
        
            Retrieves Analytical Alignment Method preset for Sketch Component.
            Returns: Indicates whether Alignment Method is at Auto-Detect or Projection
        """
        pass

    def GetAnalyticalProjectionDatumPlane(self):
        """
        GetAnalyticalProjectionDatumPlane(self: AnalyticalModelSketchComponent) -> ElementId
        
            Retrieves Datum Plane ElementId for Analytical Projection
            Returns: Represents Datum used for Analytical Projection, if Analytical Projection Type 
             indicates that a
           Datum Plane is to be used.  Otherwise, invalidElementId is 
             returned.
        """
        pass

    def GetAnalyticalProjectionType(self):
        """
        GetAnalyticalProjectionType(self: AnalyticalModelSketchComponent) -> AnalyticalProjectionType
        
            Retrieves Analytical Projection Type preset for Sketch Component.
            Returns: Indicates whether Analytical Projection is at a preset, or refers to a Datum.
        """
        pass

    def GetAutoDetectMatchedElements(self):
        """
        GetAutoDetectMatchedElements(self: AnalyticalModelSketchComponent) -> ICollection[ElementId]
        
            Retrieves ElementIds that Sketch Component is Auto-detecting against.
            Returns: Set of ElementIds that Sketch Component is auto-detecting against.
        """
        pass

    def GetComponentElementId(self):
        """
        GetComponentElementId(self: AnalyticalModelSketchComponent) -> ElementId
        
            Retrieves ElementId of Sketch Component, if such an operation makes sense.
            Returns: ElementId of Sketch Component.
           If the operation does not make sense 
             (perhaps because the Sketch abstraction does not
           translate one-to-one to 
             ElementIds), then this will return invalidElementId.
        """
        pass

    def IsAutoDetectEnabled(self):
        """
        IsAutoDetectEnabled(self: AnalyticalModelSketchComponent) -> bool
        
            Indicates whether Auto-detect is enabled on the given Sketch component.
            Returns: True if Auto-detect is enabled, false otherwise.
        """
        pass

    def IsValidAnalyticalAlignmentMethod(self, alignmentMethod):
        """
        IsValidAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent, alignmentMethod: AnalyticalAlignmentMethod) -> bool
        
            Indicates whether Analytical Alignment Method is valid for Sketch Component.
        
            alignmentMethod: Analytical Alignment Method preset to test for validity.
            Returns: True means alignment method is valid, false otherwise.
        """
        pass

    def IsValidAnalyticalProjectionType(self, projectionType):
        """
        IsValidAnalyticalProjectionType(self: AnalyticalModelSketchComponent, projectionType: AnalyticalProjectionType) -> bool
        
            Indicates whether Analytical Projection Type is valid for Sketch Component.
        
            projectionType: Analytical Projection Type preset to test for validity.
            Returns: True is projection type is valid, false otherwise.
        """
        pass

    def IsValidDatumPlaneForProjection(self, datumPlaneId):
        """
        IsValidDatumPlaneForProjection(self: AnalyticalModelSketchComponent, datumPlaneId: ElementId) -> bool
        
            Indicates whether Datum Plane is valid Analytical Projection of Sketch 
             Component.
        
        
            datumPlaneId: ElementId identifying Datum Plane.
            Returns: True if Datum Plane is valid; false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalyticalModelSketchComponent, disposing: bool) """
        pass

    def SetAnalyticalAlignmentMethod(self, alignmentMethod):
        """
        SetAnalyticalAlignmentMethod(self: AnalyticalModelSketchComponent, alignmentMethod: AnalyticalAlignmentMethod)
            Sets the Alignment Method to the supplied Analytical Alignment Method
        
            alignmentMethod: Analytical Alignment Method which the Analytical Model should use for alignment.
        """
        pass

    def SetAnalyticalProjectionDatumPlane(self, datumPlaneId):
        """
        SetAnalyticalProjectionDatumPlane(self: AnalyticalModelSketchComponent, datumPlaneId: ElementId)
            Sets the Analytical Projection to supplied Datum Plane.
        
            datumPlaneId: Identifies Datum Plane ElementId.
        """
        pass

    def SetAnalyticalProjectionType(self, projectionType):
        """
        SetAnalyticalProjectionType(self: AnalyticalModelSketchComponent, projectionType: AnalyticalProjectionType)
            Sets the Analytical Projection to the supplied Analytical Projection Type.
        
            projectionType: Analytical Projection Type to which the Analytical Model should project.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalyticalModelSketchComponent) -> bool

"""



class AnalyticalModelSupport(object, IDisposable):
    """ Represents one support for an Element, in the realm of the Analytical Model. """
    def Dispose(self):
        """ Dispose(self: AnalyticalModelSupport) """
        pass

    def GetCurve(self):
        """
        GetCurve(self: AnalyticalModelSupport) -> Curve
        
            Retrieves the curve providing support.
            Returns: Represents the curve providing support, if the Support Type is Curve Support.
        """
        pass

    def GetFace(self):
        """
        GetFace(self: AnalyticalModelSupport) -> Face
        
            Retrieves surface providing support,
            Returns: Surface representing the surface providing support, if the Support Type is 
             Surface Support.
        """
        pass

    def GetPoint(self):
        """
        GetPoint(self: AnalyticalModelSupport) -> XYZ
        
            Retrieves the point providing support.
            Returns: Represents the point providing support, if the Support Type is Point Support.
        """
        pass

    def GetPriority(self):
        """
        GetPriority(self: AnalyticalModelSupport) -> AnalyticalSupportPriority
        
            Retrieves the priority of the support provided.
            Returns: Indicates the support priority, as determined by Analytical Support Checking
        """
        pass

    def GetSupportingElement(self):
        """
        GetSupportingElement(self: AnalyticalModelSupport) -> ElementId
        
            Retrieves the actual Element Id providing support.
            Returns: Represents Element that provides support.
        """
        pass

    def GetSupportType(self):
        """
        GetSupportType(self: AnalyticalModelSupport) -> AnalyticalSupportType
        
            Gets the type of support provided.
            Returns: Indicates type of support provided.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AnalyticalModelSupport, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalyticalModelSupport) -> bool

"""



class AnalyticalModelSurface(AnalyticalModel, IDisposable):
    """ An element that represents a surface in the structural analytical model. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHiddenOpenings(self, openingsIds):
        """ GetHiddenOpenings(self: AnalyticalModelSurface) -> ICollection[ElementId] """
        pass

    def GetLocalCoordinateSystem(self, point=None):
        """
        GetLocalCoordinateSystem(self: AnalyticalModelSurface, point: XYZ) -> Transform
        
            Gets the local coordinate system (LCS) reflects analytical model orientation at 
             the specified point.
        
        
            point: The point on the analytical model surface element.
            Returns: Transformation matrix.
           x - longitudinal axis, y - transversal, section - 
             horizontal, strong axis, z - transversal, section - vertical, weak axis, origin 
             - base point of LCS.
        """
        pass

    def GetLoops(self, loopType):
        """
        GetLoops(self: AnalyticalModelSurface, loopType: AnalyticalLoopType) -> IList[CurveLoop]
        
            Retrieves Analytical Model Loops with respect to the loopType.
            Returns: Loops that satisfy loopType criteria are returned.
        """
        pass

    def GetOpeningLoops(self, openingId):
        """
        GetOpeningLoops(self: AnalyticalModelSurface, openingId: ElementId) -> IList[CurveLoop]
        
            Retrieves Array of CurveLoops of Analytical Surface Opening..
           Only valid 
             openings for hide are allowed.
        
        
            openingId: Identifies which Opening creates the CurveLoop in the analytical surface.
            Returns: Array of CurveLoops associated with Opening.
        """
        pass

    def GetOpenings(self, openingsIds):
        """ GetOpenings(self: AnalyticalModelSurface) -> ICollection[ElementId] """
        pass

    def GetPlane(self):
        """
        GetPlane(self: AnalyticalModelSurface) -> Plane
        
            Returns plane on which Analytical Model Surface Element is lying.
           Only 
             planar surface elements are valid for this function.
        
            Returns: Plane object on which Analytical Model is projected.
        """
        pass

    def HasOpenings(self):
        """
        HasOpenings(self: AnalyticalModelSurface) -> bool
        
            Checks if the analytical model surface have any openings.
            Returns: True if Analytical Surface Element contains any openings (included invalid for 
             hide).
        """
        pass

    def HideOpening(self, openingId):
        """
        HideOpening(self: AnalyticalModelSurface, openingId: ElementId) -> bool
        
            Hides set of curves originating from Opening.
        
            openingId: Opening to hide in analytical surface.
            Returns: True if given opening was hidden (operation was successful).
        """
        pass

    def IsOpeningHidden(self, openingId):
        """
        IsOpeningHidden(self: AnalyticalModelSurface, openingId: ElementId) -> bool
        
            Returns true if opening with given Identifier is hidden.
        
            openingId: Identifier of opening to check.
            Returns: True for openings which are hidden, false for all other Identifiers.
        """
        pass

    def IsPlanar(self):
        """
        IsPlanar(self: AnalyticalModelSurface) -> bool
        
            Indicates if the Analytical Model Surface Element is planar.
            Returns: True if Analytical Model Surface Element is planar, false otherwise.
        """
        pass

    def IsValidOpeningForHide(self, openingId):
        """
        IsValidOpeningForHide(self: AnalyticalModelSurface, openingId: ElementId) -> bool
        
            Returns true if opening with given Identifier could be hidden, false for all 
             other Identifiers.
        
        
            openingId: Identifier of opening to check.
            Returns: True for openings which are valid to be hidden, false for all other Identifiers.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetLoops(self, loopType, newLoops):
        """ SetLoops(self: AnalyticalModelSurface, loopType: AnalyticalLoopType, newLoops: IList[CurveLoop]) -> bool """
        pass

    def ShowOpening(self, openingId):
        """
        ShowOpening(self: AnalyticalModelSurface, openingId: ElementId) -> bool
        
            Shows previously hidden set of curves originating from Opening.
        
            openingId: Opening to show in analytical surface.
            Returns: True if given opening was shown (operation was successful).
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

    AlignmentMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The alignment method option.

Get: AlignmentMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod

Set: AlignmentMethod(self: AnalyticalModelSurface) = value
"""

    BottomExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom extension option.

Get: BottomExtension(self: AnalyticalModelSurface) -> SurfaceElementExtension

Set: BottomExtension(self: AnalyticalModelSurface) = value
"""

    BottomExtensionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom extension method option.

Get: BottomExtensionMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod

Set: BottomExtensionMethod(self: AnalyticalModelSurface) = value
"""

    BottomExtensionPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom extension plane ID option.

Get: BottomExtensionPlaneId(self: AnalyticalModelSurface) -> ElementId

Set: BottomExtensionPlaneId(self: AnalyticalModelSurface) = value
"""

    HasExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the element supports an extension option.

Get: HasExtension(self: AnalyticalModelSurface) -> bool

"""

    ProjectionPlaneZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Z projection option.

Get: ProjectionPlaneZ(self: AnalyticalModelSurface) -> ElementId

Set: ProjectionPlaneZ(self: AnalyticalModelSurface) = value
"""

    ProjectionZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Z projection option.

Get: ProjectionZ(self: AnalyticalModelSurface) -> SurfaceElementProjectionZ

Set: ProjectionZ(self: AnalyticalModelSurface) = value
"""

    TopExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension option.

Get: TopExtension(self: AnalyticalModelSurface) -> SurfaceElementExtension

Set: TopExtension(self: AnalyticalModelSurface) = value
"""

    TopExtensionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension method option.

Get: TopExtensionMethod(self: AnalyticalModelSurface) -> AnalyticalAlignmentMethod

Set: TopExtensionMethod(self: AnalyticalModelSurface) = value
"""

    TopExtensionPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The top extension plane ID option.

Get: TopExtensionPlaneId(self: AnalyticalModelSurface) -> ElementId

Set: TopExtensionPlaneId(self: AnalyticalModelSurface) = value
"""



class AnalyticalProjectionType(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Projection.  Combined with AnalyticalDirection, this abstracts
       Analytical Projections for all Structural Elements
    
    enum AnalyticalProjectionType, values: AutoDetect (5), Bottom (2), Center (1), CenterOfCore (11), DatumPlane (8), Default (10), Invalid (6), LocationLine (12), NotApplicable (9), SideOne (3), SideTwo (4), SketchCurve (7), Top (0), Varies (13)
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

    AutoDetect = None
    Bottom = None
    Center = None
    CenterOfCore = None
    DatumPlane = None
    Default = None
    Invalid = None
    LocationLine = None
    NotApplicable = None
    SideOne = None
    SideTwo = None
    SketchCurve = None
    Top = None
    value__ = None
    Varies = None


class AnalyticalRigidLinksOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how Rigid Links will be made for the Analytical Model.
    
    enum AnalyticalRigidLinksOption, values: Disabled (1), Enabled (0), FromColumn (2)
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

    Disabled = None
    Enabled = None
    FromColumn = None
    value__ = None


class AnalyticalSupportChecking(object):
    """ Utilities that allow for detection of incorrect or incomplete analytical supports. """
    @staticmethod
    def CheckMemberSupports(document, progressIndicatorText):
        """
        CheckMemberSupports(document: Document, progressIndicatorText: str) -> bool
        
            Check if the document contains unsupported Structural Elements.
        
            document: Document in which to perform Analytical Support Check.
            progressIndicatorText: Text to display on progress indicator.
            Returns: True if the support check succeeded, false otherwise.
        """
        pass

    __all__ = [
        'CheckMemberSupports',
    ]


class AnalyticalSupportPriority(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines how "highly" another Element is giving support for one Element.
    
    enum AnalyticalSupportPriority, values: FourthHigestPriority (4), HighestPriority (1), SecondHighestPriority (2), ThirdHighestPriority (3), UnknownPriority (0)
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

    FourthHigestPriority = None
    HighestPriority = None
    SecondHighestPriority = None
    ThirdHighestPriority = None
    UnknownPriority = None
    value__ = None


class AnalyticalSupportType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates what kind of support another Element provides -- Point, Surface, or Curve.
    
    enum AnalyticalSupportType, values: CurveSupport (2), PointSupport (1), SurfaceSupport (3), UnknownSupport (0)
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

    CurveSupport = None
    PointSupport = None
    SurfaceSupport = None
    UnknownSupport = None
    value__ = None


class AnalyzeAs(Enum, IComparable, IFormattable, IConvertible):
    """
    Analyze As has various functions within the Analytical Model, and is Element-dependent.
       "Not for Analysis" usually means that there will not be an Analytical Model generated.
       The others indicate how the Analytical Model behavior will treat the Element in question.
       For instance "Hanger" columns have different support expectations than "Gravity" columns.
    
    enum AnalyzeAs, values: Gravity (1), GravityLateral (10), Hanger (0), Lateral (2), Mat (4), NotApplicable (8), NotForAnalysis (7), SlabOneWay (3), SlabOnGrade (5), SlabTwoWay (9)
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

    Gravity = None
    GravityLateral = None
    Hanger = None
    Lateral = None
    Mat = None
    NotApplicable = None
    NotForAnalysis = None
    SlabOneWay = None
    SlabOnGrade = None
    SlabTwoWay = None
    value__ = None


class LoadBase(Element, IDisposable):
    """ The LoadBase object is the base class for all load objects within the Autodesk Revit API. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsOrientToPermitted(self, orientTo):
        """
        IsOrientToPermitted(self: LoadBase, orientTo: LoadOrientTo) -> bool
        
            Indicates if the provided orientation is permitted for this load.
        
            orientTo: Load orientation to check.
            Returns: True if provided orientation type is permitted for this load, false if not.
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

    HostElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element for the load.

Get: HostElement(self: LoadBase) -> AnalyticalModel

"""

    HostElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element ID for the load.

Get: HostElementId(self: LoadBase) -> ElementId

"""

    IsHosted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the Load is hosted or non-hosted.

Get: IsHosted(self: LoadBase) -> bool

"""

    IsReaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load is reaction option.

Get: IsReaction(self: LoadBase) -> bool

Set: IsReaction(self: LoadBase) = value
"""

    LoadCase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load case for the load.

Get: LoadCase(self: LoadBase) -> LoadCase

"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load case ID for the load.

Get: LoadCaseId(self: LoadBase) -> ElementId

Set: LoadCaseId(self: LoadBase) = value
"""

    LoadCaseName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the load case to which this load belongs.

Get: LoadCaseName(self: LoadBase) -> str

"""

    LoadCategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the category to which this load belongs.

Get: LoadCategoryName(self: LoadBase) -> str

"""

    LoadNatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string representing the nature of the load.

Get: LoadNatureName(self: LoadBase) -> str

"""

    OrientTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load orientation option.

Get: OrientTo(self: LoadBase) -> LoadOrientTo

Set: OrientTo(self: LoadBase) = value
"""

    WorkPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the work plane which may determine the orientation of the load.

Get: WorkPlaneId(self: LoadBase) -> ElementId

"""



class AreaLoad(LoadBase, IDisposable):
    """ An object that represents a force applied across an area. """
    @staticmethod
    def Create(aDoc, *__args):
        """
        Create(aDoc: Document, host: AnalyticalModelSurface, forceVector: XYZ, symbol: AreaLoadType) -> AreaLoad
        
            Creates a new hosted area load within the project.
        
            aDoc: Document to which new area load will be added.
            host: The analytical surface host element (Analytical Floor, Analytical Foundation 
             Slab or Analytical Wall) for the area Load.
        
            forceVector: The force vector applied to the 1st reference point of the area load.
            symbol: The symbol of the AreaLoad. Set ll to use default type.
            Returns: If successful, returns an object of the newly created AreaLoad. ll is returned 
             if the operation fails.
        
        Create(aDoc: Document, loops: IList[CurveLoop], forceVector: XYZ, symbol: AreaLoadType) -> AreaLoad
        Create(aDoc: Document, loops: IList[CurveLoop], forceVectors: IList[XYZ], refPointCurveIndexes: IList[int], refPointCurveSelectors: IList[int], symbol: AreaLoadType) -> AreaLoad
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetLoops(self):
        """
        GetLoops(self: AreaLoad) -> IList[CurveLoop]
        
            Returns curve loops that define geometry of the area load.
        """
        pass

    def GetRefPoint(self, index):
        """
        GetRefPoint(self: AreaLoad, index: int) -> XYZ
        
            Returns the physical location of the reference point.
        
            index: The index of the point to return.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetLoops(self, doc, newLoops):
        """ SetLoops(self: AreaLoad, doc: Document, newLoops: IList[CurveLoop]) -> bool """
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns area of the area load.

Get: Area(self: AreaLoad) -> float

"""

    ForceVector1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the 1st reference point of the area load, oriented according to OrientTo setting.

Get: ForceVector1(self: AreaLoad) -> XYZ

Set: ForceVector1(self: AreaLoad) = value
"""

    ForceVector2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the 2nd reference point of the area load, oriented according to OrientTo setting.

Get: ForceVector2(self: AreaLoad) -> XYZ

Set: ForceVector2(self: AreaLoad) = value
"""

    ForceVector3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the 3rd reference point of the area load, oriented according to OrientTo setting.

Get: ForceVector3(self: AreaLoad) -> XYZ

Set: ForceVector3(self: AreaLoad) = value
"""

    IsProjected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load is projected.

Get: IsProjected(self: AreaLoad) -> bool

Set: IsProjected(self: AreaLoad) = value
"""

    NumRefPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the total number of reference points for the area load.

Get: NumRefPoints(self: AreaLoad) -> int

"""



class LoadTypeBase(ElementType, IDisposable):
    """ An object that represents a Load type. """
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


class AreaLoadType(LoadTypeBase, IDisposable):
    """ An object that represents a Load type. """
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


class AreaReinforcement(Element, IDisposable):
    """ An object that represents an Area Reinforcement within the Autodesk Revit project. """
    @staticmethod
    def Create(document, hostElement, *__args):
        """
        Create(document: Document, hostElement: Element, curveArray: IList[Curve], majorDirection: XYZ, areaReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, rebarHookTypeId: ElementId) -> AreaReinforcement
        Create(document: Document, hostElement: Element, majorDirection: XYZ, areaReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, rebarHookTypeId: ElementId) -> AreaReinforcement
        
            Creates a new AreaReinforcement object based on a host boundary.
        
            document: The document.
            hostElement: The element that will host the AreaReinforcement. The host can be a Structural 
             Floor, Structural Wall, Structural Slab, or a Part created from a structural 
             layer belonging to one of those element types.
        
            majorDirection: A vector to define the major direction of the AreaReinforcement.
            areaReinforcementTypeId: The id of the AreaReinforcementType.
            rebarBarTypeId: The id of the RebarBarType.
            rebarHookTypeId: The id of the RebarHookType.
           If this parameter is InvalidElementId, it 
             means to create a rebar with no hooks.
        
            Returns: The newly created AreaReinforcement.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetBoundaryCurveIds(self):
        """
        GetBoundaryCurveIds(self: AreaReinforcement) -> IList[ElementId]
        
            Retrieves the set of curves forming the boundary of the Area Reinforcement.
            Returns: A collection of ElementIds of AreaReinforcementCurve elements.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHostId(self):
        """
        GetHostId(self: AreaReinforcement) -> ElementId
        
            The element that contains the Area Reinforcement.
            Returns: The element that the Area Reinforcement object belongs to, such as a structural
             
           wall, floor or foundation.
        """
        pass

    def GetRebarInSystemIds(self):
        """
        GetRebarInSystemIds(self: AreaReinforcement) -> IList[ElementId]
        
            Returns the ids of the RebarInSystem elements owned by the AreaReinforcement
          
              element.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: AreaReinforcement, view: View3D) -> bool
        
            Checks if this Area Reinforcement is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if Area Reinforcement is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: AreaReinforcement, view: View) -> bool
        
            Checks if Area Reinforcement is shown unobscured in a view.
        
            view: The view element
            Returns: True if Area Reinforcement is shown unobscured, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def RemoveAreaReinforcementSystem(doc, system):
        """
        RemoveAreaReinforcementSystem(doc: Document, system: AreaReinforcement) -> IList[ElementId]
        
            Deletes the specified AreaReinforcement, and converts its RebarInSystem
           
             elements to equivalent Rebar elements.
        
        
            doc: The document.
            system: An AreaReinforcement element in the document.
            Returns: The ids of the newly created Rebar elements.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: AreaReinforcement, view: View3D, solid: bool)
            Sets this Area Reinforcement to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if Area Reinforcement is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: AreaReinforcement, view: View, unobscured: bool)
            Sets Area Reinforcement to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if Area Reinforcement is shown unobscured, false otherwise.
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

    AdditionalBottomCoverOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional offset from the bottom or interior cover reference.

Get: AdditionalBottomCoverOffset(self: AreaReinforcement) -> float

Set: AdditionalBottomCoverOffset(self: AreaReinforcement) = value
"""

    AdditionalTopCoverOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional offset from the top or exterior cover reference.

Get: AdditionalTopCoverOffset(self: AreaReinforcement) -> float

Set: AdditionalTopCoverOffset(self: AreaReinforcement) = value
"""

    AreaReinforcementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the type of the Area Reinforcement.

Get: AreaReinforcementType(self: AreaReinforcement) -> AreaReinforcementType

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the Major Direction of the Area Reinforcement.

Get: Direction(self: AreaReinforcement) -> XYZ

"""



class AreaReinforcementCurve(CurveElement, IDisposable):
    """ An object that specifies the type of a floor in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: AreaReinforcementCurve, A_0: bool) """
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

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the 3D curve forming part of the boundary of an Area Reinforcement element.

Get: Curve(self: AreaReinforcementCurve) -> Curve

"""



class AreaReinforcementType(ElementType, IDisposable):
    """ An object that specifies the type of a Structural Area Reinforcement element in Autodesk Revit. """
    @staticmethod
    def CreateDefaultAreaReinforcementType(aDoc):
        """
        CreateDefaultAreaReinforcementType(aDoc: Document) -> ElementId
        
            Creates a new AreaReinforcementType object with a default name.
        
            aDoc: The document.
            Returns: The newly created type id.
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


class BentFabricBendDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Direction in which FabricSheet is bent.
    
    enum BentFabricBendDirection, values: Major (0), Minor (1)
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

    Major = None
    Minor = None
    value__ = None


class BentFabricStraightWiresLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    Bent Fabric straight wires location.
       The side on wich straight wires will be loacted is determined by the start and end point of the first bent profile segment that specifies the direction of the curve loop on plane.
    
    enum BentFabricStraightWiresLocation, values: Left (1), Right (0)
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
    Right = None
    value__ = None


class BentFabricWiresOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Bent Fabric wires orientation.
    
    enum BentFabricWiresOrientation, values: Down (0), Up (1)
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

    Down = None
    Up = None
    value__ = None


class BoundaryConditions(Element, IDisposable):
    """ An object that represents a force applied across an area. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetBoundaryConditionsType(self):
        """
        GetBoundaryConditionsType(self: BoundaryConditions) -> BoundaryConditionsType
        
            Returns the boundary conditions type.
            Returns: The boundary conditions type.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurve(self):
        """
        GetCurve(self: BoundaryConditions) -> Curve
        
            Returns curve that define geometry of the line boundary conditions.
        """
        pass

    def GetDegreesOfFreedomCoordinateSystem(self):
        """
        GetDegreesOfFreedomCoordinateSystem(self: BoundaryConditions) -> Transform
        
            Gets the origin and rotation of coordinate system that is used by translation 
             and rotation parameters, like X Translation or Z Rotation.
        
            Returns: The coordinate system. Origin contains the position of the start of the 
             boundary conditions. BasisX, BasisY and BasisZ contain the directions of the 
             axes in the global coordinate system.
        """
        pass

    def GetLoops(self):
        """
        GetLoops(self: BoundaryConditions) -> IList[CurveLoop]
        
            Returns curve loops that define geometry of the area boundary conditions.
            Returns: The curve loop collection.
        """
        pass

    def GetOrientTo(self):
        """
        GetOrientTo(self: BoundaryConditions) -> BoundaryConditionsOrientTo
        
            Returns the boundary conditions orientation option.
            Returns: The orientation option.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetOrientTo(self, orientTo):
        """
        SetOrientTo(self: BoundaryConditions, orientTo: BoundaryConditionsOrientTo)
            Sets the boundary condition orientation option.
        
            orientTo: The new orientation option.
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

    AssociatedLoadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the internal load element associated with a boundary conditions.

Get: AssociatedLoadId(self: BoundaryConditions) -> ElementId

Set: AssociatedLoadId(self: BoundaryConditions) = value
"""

    HostElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element for the boundary conditions.

Get: HostElement(self: BoundaryConditions) -> AnalyticalModel

"""

    HostElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element Id for the boundary conditions.

Get: HostElementId(self: BoundaryConditions) -> ElementId

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the position of point boundary conditions.

Get: Point(self: BoundaryConditions) -> XYZ

"""



class BoundaryConditionsOrientTo(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies boundary condition orientation.
    
    enum BoundaryConditionsOrientTo, values: HostLocalCoordinateSystem (1), Project (0)
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

    HostLocalCoordinateSystem = None
    Project = None
    value__ = None


class BoundaryConditionsType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum declares type of BoundaryConditions.
    
    enum BoundaryConditionsType, values: Area (2), Line (1), Point (0)
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

    Area = None
    Line = None
    Point = None
    value__ = None


class BracePlanRepresentation(Enum, IComparable, IFormattable, IConvertible):
    """
    The possible representations for braces in plan views.
    
    enum BracePlanRepresentation, values: LineWithAngle (2), ParallelLine (1)
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

    LineWithAngle = None
    ParallelLine = None
    value__ = None


class CodeCheckingParameterServiceData(object, IDisposable):
    """ The data needed by code checking server to perform code checking. """
    def Dispose(self):
        """ Dispose(self: CodeCheckingParameterServiceData) """
        pass

    def GetCurrentElements(self):
        """
        GetCurrentElements(self: CodeCheckingParameterServiceData) -> IList[ElementId]
        
            Returns the list of Ids of the current elements.
            Returns: Ids of the current elements. Contains the analytical model element to which the 
             code checking parameter belongs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CodeCheckingParameterServiceData, disposing: bool) """
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current document.

Get: Document(self: CodeCheckingParameterServiceData) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CodeCheckingParameterServiceData) -> bool

"""



class DistributionType(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of the distribution
    
    enum DistributionType, values: Uniform (0), VaryingLength (1)
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

    Uniform = None
    value__ = None
    VaryingLength = None


class EndTreatmentType(ElementType, IDisposable):
    """ An end treatment type object that is used to hold information about the end treatment applied to bars that are connected to a coupler. """
    @staticmethod
    def Create(doc, strTreatment=None):
        """
        Create(doc: Document) -> EndTreatmentType
        
            Creates a new EndTreatmentType in a document.
        Create(doc: Document, strTreatment: str) -> EndTreatmentType
        
            Creates a new EndTreatmentType in a document and adds the input string to the 
             endTreatment parameter.
        """
        pass

    @staticmethod
    def CreateDefaultEndTreatmentType(ADoc):
        """
        CreateDefaultEndTreatmentType(ADoc: Document) -> ElementId
        
            Creates a new EndTreatmentType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
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

    EndTreatment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String describing the end treatment

Get: EndTreatment(self: EndTreatmentType) -> str

Set: EndTreatment(self: EndTreatmentType) = value
"""



class FabricArea(Element, IDisposable):
    """ An object that represents an Fabric Area Distribution within the Autodesk Revit project. It is container for Fabric Sheet elements. """
    def CopyCurveLoopsInSketch(self):
        """
        CopyCurveLoopsInSketch(self: FabricArea) -> IList[CurveLoop]
        
            Creates copies of the CurveLoops in the FabricArea sketch.
            Returns: The copy of the curve loops.
        """
        pass

    @staticmethod
    def Create(aDoc, hostElement, *__args):
        """
        Create(aDoc: Document, hostElement: Element, curveLoops: IList[CurveLoop], majorDirection: XYZ, majorDirectionOrigin: XYZ, fabricAreaTypeId: ElementId, fabricSheetTypeId: ElementId) -> FabricArea
        Create(aDoc: Document, hostElement: Element, majorDirection: XYZ, fabricAreaTypeId: ElementId, fabricSheetTypeId: ElementId) -> FabricArea
        
            Creates a FabricArea based on a host boundary.
        
            aDoc: The document.
            hostElement: The element that will host the FabricArea. The host can be a Structural Floor, 
             Structural Wall, Structural Slab, or a Part created from a structural layer 
             belonging to one of those element types.
        
            majorDirection: A vector to define the major direction of the FabricArea.
            fabricAreaTypeId: The id of the FabricAreaType.
            fabricSheetTypeId: The id of the FabricSheetType.
            Returns: The newly created FabricArea.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetBoundaryCurveIds(self):
        """
        GetBoundaryCurveIds(self: FabricArea) -> IList[ElementId]
        
            Retrieves the identifiers of the set of curves forming the boundary of the 
             Fabric Area.
        
            Returns: A collection of ElementIds of FabricAreaCurve elements.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFabricSheetElementIds(self):
        """
        GetFabricSheetElementIds(self: FabricArea) -> IList[ElementId]
        
            Retrieves the identifiers of all the FabricSheet Elements in the FabricArea.
            Returns: A collection of ElementIds of FabricSheet elements.
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: FabricArea) -> FabricRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def GetTotalSheetMass(self):
        """
        GetTotalSheetMass(self: FabricArea) -> float
        
            Calculates the total sheet mass: Volume of Wire * Unit Weight.
            Returns: The total sheet mass.
        """
        pass

    def GetValidViewsForTags(self):
        """
        GetValidViewsForTags(self: FabricArea) -> IList[ElementId]
        
            Gets ids of the views where tags and symbols can be placed for the FabricArea 
             and/or FabricSheets
        
            Returns: The collection of View ElementIds.
        """
        pass

    def IsCoverOffsetValid(self, coverOffset):
        """
        IsCoverOffsetValid(self: FabricArea, coverOffset: float) -> bool
        
            Identifies if the specified value is valid for use as a cover offset.
        
            coverOffset: The cover offset value.
            Returns: True if the value is valid, false if the value is invalid.
        """
        pass

    def IsValidMajorLapSplice(self, majorLapSplice):
        """
        IsValidMajorLapSplice(self: FabricArea, majorLapSplice: float) -> bool
        
            Identifies if the specified value is valid for use as a major lap splice.
        
            majorLapSplice: The major lap splice value.
            Returns: True if the value is valid, false if the value is invalid.
        """
        pass

    def IsValidMinorLapSplice(self, minorLapSplice):
        """
        IsValidMinorLapSplice(self: FabricArea, minorLapSplice: float) -> bool
        
            Identifies if the specified value is valid for use as a minor lap splice.
        
            minorLapSplice: The minor lap splice value.
            Returns: True if the value is valid, false if the value is invalid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def RemoveFabricReinforcementSystem(doc, system):
        """
        RemoveFabricReinforcementSystem(doc: Document, system: FabricArea) -> IList[ElementId]
        
            Deletes the specified FabricArea, and converts its FabricSheet elements
           to 
             equivalent Single Fabric Sheet elements.
        
        
            doc: The document.
            system: An FabricArea Reinforcement element in the document.
            Returns: The ids of the newly created Single Fabric Sheet elements.
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

    CoverOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The additional cover offset of the fabric distribution.

Get: CoverOffset(self: FabricArea) -> float

Set: CoverOffset(self: FabricArea) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Major Direction of the Fabric Area.

Get: Direction(self: FabricArea) -> XYZ

"""

    DirectionOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Origin Point of the Major Direction of the Fabric Area.

Get: DirectionOrigin(self: FabricArea) -> XYZ

"""

    FabricAreaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the Fabric Area.

Get: FabricAreaType(self: FabricArea) -> FabricAreaType

"""

    FabricLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Fabric location in the host.

Get: FabricLocation(self: FabricArea) -> FabricLocation

Set: FabricLocation(self: FabricArea) = value
"""

    FabricSheetTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Fabric Sheet Type for this element.

Get: FabricSheetTypeId(self: FabricArea) -> ElementId

Set: FabricSheetTypeId(self: FabricArea) = value
"""

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Host element for the fabric area.

Get: HostId(self: FabricArea) -> ElementId

"""

    LapSplicePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabric lap splice position in the fabric distribution.

Get: LapSplicePosition(self: FabricArea) -> FabricLapSplicePosition

Set: LapSplicePosition(self: FabricArea) = value
"""

    MajorLapSpliceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabric lap splice length in the fabric distribution in the major direction.

Get: MajorLapSpliceLength(self: FabricArea) -> float

Set: MajorLapSpliceLength(self: FabricArea) = value
"""

    MajorSheetAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabric sheet alignment in the fabric distribution in the major direction.

Get: MajorSheetAlignment(self: FabricArea) -> FabricSheetAlignment

Set: MajorSheetAlignment(self: FabricArea) = value
"""

    MinorLapSpliceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabric lap splice length in the fabric distribution in the minor direction.

Get: MinorLapSpliceLength(self: FabricArea) -> float

Set: MinorLapSpliceLength(self: FabricArea) = value
"""

    MinorSheetAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabric sheet alignment in the fabric distribution in the minor direction.

Get: MinorSheetAlignment(self: FabricArea) -> FabricSheetAlignment

Set: MinorSheetAlignment(self: FabricArea) = value
"""

    SketchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Sketch element for this element.

Get: SketchId(self: FabricArea) -> ElementId

"""

    TagViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element of the view in which to tag new members of this element.

Get: TagViewId(self: FabricArea) -> ElementId

Set: TagViewId(self: FabricArea) = value
"""



class FabricAreaType(ElementType, IDisposable):
    """ A FabricAreaType object is used in FabricArea object generation. """
    @staticmethod
    def CreateDefaultFabricAreaType(aDoc):
        """
        CreateDefaultFabricAreaType(aDoc: Document) -> ElementId
        
            Creates a new FabricAreaType object with a default name.
        
            aDoc: The document.
            Returns: The newly created type id.
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


class FabricHostReference(Enum, IComparable, IFormattable, IConvertible):
    """
    Controls if Single Fabric Sheet should be cut by the Host Cover.
    
    enum FabricHostReference, values: CutByCover (1), NotCutByCover (0)
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

    CutByCover = None
    NotCutByCover = None
    value__ = None


class FabricLapSplicePosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabric lap splice position in the fabric distribution
    
    enum FabricLapSplicePosition, values: Aligned (0), MajorHalfwayStagger (1), MajorPassingStagger (2), MinorHalfwayStagger (3), MinorPassingStagger (4)
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

    Aligned = None
    MajorHalfwayStagger = None
    MajorPassingStagger = None
    MinorHalfwayStagger = None
    MinorPassingStagger = None
    value__ = None


class FabricLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabric location in the host
    
    enum FabricLocation, values: BottomOrInternal (1), TopOrExternal (0)
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

    BottomOrInternal = None
    TopOrExternal = None
    value__ = None


class FabricReinSpanSymbol(IndependentTag, IDisposable):
    """ Represents an instance of a Structural Fabric Reinforcement Symbol in Autodesk Revit. """
    @staticmethod
    def Create(document, viewId, hostId, point, symbolId):
        """
        Create(document: Document, viewId: ElementId, hostId: LinkElementId, point: XYZ, symbolId: ElementId) -> FabricReinSpanSymbol
        
            Places a new instance of the Structural Fabric Reinforcement Symbol into the 
             project relative to a particular FabricSheet and View.
        
        
            document: The document.
            viewId: The id of the view in which the symbol should appear.
            hostId: The ElementId of FabricSheet (either in the document, or linked from another 
             document).
        
            point: The span symbol's head position.
            symbolId: The id of the family symbol of this symbol.
            Returns: A reference to the newly-created symbol.
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


class ReinforcementRoundingManager(object, IDisposable):
    """ A base class providing access to reinforcement rounding overrides for structural elements. """
    def Dispose(self):
        """ Dispose(self: ReinforcementRoundingManager) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementRoundingManager, disposing: bool) """
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

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner of the reinforcement rounding overrides.

Get: Element(self: ReinforcementRoundingManager) -> Element

"""

    IsActiveOnElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines whether reinforcement rounding is activated for the particular element.

Get: IsActiveOnElement(self: ReinforcementRoundingManager) -> bool

Set: IsActiveOnElement(self: ReinforcementRoundingManager) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReinforcementRoundingManager) -> bool

"""

    LengthDisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length units used when displaying the reinforcement rounding values.

Get: LengthDisplayUnit(self: ReinforcementRoundingManager) -> DisplayUnitType

"""



class FabricRoundingManager(ReinforcementRoundingManager, IDisposable):
    """ Provides access to element reinforcement roundings overrides. """
    def Dispose(self):
        """ Dispose(self: ReinforcementRoundingManager, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementRoundingManager, disposing: bool) """
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

    ApplicableReinforcementRoundingSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the source of the rounding settings for this element.

Get: ApplicableReinforcementRoundingSource(self: FabricRoundingManager) -> ReinforcementRoundingSource

"""

    ApplicableSegmentLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding for fabric segments.

Get: ApplicableSegmentLengthRounding(self: FabricRoundingManager) -> float

"""

    ApplicableSegmentLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding method for fabric segments.

Get: ApplicableSegmentLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

"""

    ApplicableTotalLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding for Cut Overall Length and Cut Overall Width parameters.

Get: ApplicableTotalLengthRounding(self: FabricRoundingManager) -> float

"""

    ApplicableTotalLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding method for Cut Overall Length and Cut Overall Width parameters.

Get: ApplicableTotalLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

"""

    SegmentLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rounding for fabric segments.

Get: SegmentLengthRounding(self: FabricRoundingManager) -> float

Set: SegmentLengthRounding(self: FabricRoundingManager) = value
"""

    SegmentLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the segment length rounding method

Get: SegmentLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

Set: SegmentLengthRoundingMethod(self: FabricRoundingManager) = value
"""

    TotalLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rounding for Cut Overall Length and Cut Overall Width parameters.

Get: TotalLengthRounding(self: FabricRoundingManager) -> float

Set: TotalLengthRounding(self: FabricRoundingManager) = value
"""

    TotalLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the total length rounding method

Get: TotalLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

Set: TotalLengthRoundingMethod(self: FabricRoundingManager) = value
"""



class FabricSheet(Element, IDisposable):
    """ An object that represents an Fabric Sheet Element within the Autodesk Revit project. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, hostElement: Element, fabricSheetTypeId: ElementId) -> FabricSheet
        
            Creates a new instance of a single flat Fabric Sheet element within the project.
        
            document: The document in which the fabric sheet is to be created.
            hostElement: The element that will host the FabricSheet. The host can be a Structural Floor, 
             Structural Wall, Structural Slab, or a Part created from a structural layer 
             belonging to one of those element types.
        
            fabricSheetTypeId: The id of the FabricSheetType.
            Returns: The newly created single Fabric Sheet instance.
        Create(document: Document, concreteHostElementId: ElementId, fabricSheetTypeId: ElementId, bendProfile: CurveLoop) -> FabricSheet
        
            Creates a new instance of a single bent Fabric Sheet element within the project.
        
            document: The document in which the fabric sheet is to be created.
            concreteHostElementId: The element that will host the FabricSheet.
           The host can be a Structural 
             Floor, Structural Wall, Structural Slab, Structural Floor Edge, Structural Slab 
             Edge,
           Structural Column, Beam and Brace.
           Also, host can be a 
             Autodesk::Revit::DB::Part created from a structural layer of Structural Floor, 
             Structural Wall or Structural Slab.
        
            fabricSheetTypeId: The id of the FabricSheetType.
            bendProfile: A profile that defines the bending shape of the fabric sheet.
           The profile 
             can be provided without fillets (eg. for L shape, only two lines not two lines 
             and one arc), if so,
           then fillets (in example one arc) will be 
             automatically generated basing on the Bend Diameter parameter defined in the 
             Fabric Wire system family.
           If the provided profile has no corners (has a 
             tangent defined at each point except the ends), no fillets will be generated.
         
               The provided profile defines the center-curve of a wire.
        
            Returns: The instance of the newly created bent fabric sheet.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetBendProfile(self):
        """
        GetBendProfile(self: FabricSheet) -> CurveLoop
        
            Returns the profile (not including generated fillets) that defines the shape of 
             the Fabric Sheet bending.
        
            Returns: The profile that defines the shape of the fabric sheet bending for bent fabric 
             sheet, for flat fabric sheet ll will be returned.
        """
        pass

    def GetBendProfileWithFillets(self):
        """
        GetBendProfileWithFillets(self: FabricSheet) -> CurveLoop
        
            Returns the profile with generated fillets that defines the shape of the Fabric 
             Sheet bending.
        
            Returns: The bend profile with generated fillets that defines the shape of the fabric 
             sheet bending for bent fabric sheet,
           for flat fabric sheet ll will be 
             returned.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: FabricSheet) -> FabricRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def GetSegmentParameterIdsAndLengths(self, rounded):
        """
        GetSegmentParameterIdsAndLengths(self: FabricSheet, rounded: bool) -> IDictionary[ElementId, float]
        
            Returns the array of pairs [parameter ID, length] that correspond to segments 
             of a bent fabric sheet (like A, B, C, D etc.).
        
        
            rounded: Set to true to return rounded values for segments lengths.
            Returns: Array of pairs [parameter ID, length] that correspond to segments of a bent 
             fabric sheet (like A, B, C, D etc.) is returned for bend fabric sheet.
           For 
             flat fabric sheet (not bent) empty array is returned.
        """
        pass

    def GetSheetLocation(self):
        """
        GetSheetLocation(self: FabricSheet) -> Transform
        
            Gets the position and the orientation of the Fabric Sheet instance.
            Returns: The location of the Fabric Sheet instance.
        """
        pass

    def GetWireCenterlines(self, wireDirection=None):
        """
        GetWireCenterlines(self: FabricSheet, wireDirection: WireDistributionDirection) -> IList[Curve]
        
            Gets a list of curves representing the wires centerlines of the Fabric Sheet.
        
            wireDirection: The direction of wire distribution in the Fabric Sheet.
            Returns: The centerline curves.
        GetWireCenterlines(self: FabricSheet) -> IList[Curve]
        
            Gets a list of curves representing the wires centerlines of the Fabric Sheet in 
             the both distribution directions.
        
            Returns: The centerline curves.
        """
        pass

    def IsCoverOffsetValid(self, coverOffset):
        """
        IsCoverOffsetValid(self: FabricSheet, coverOffset: float) -> bool
        
            Identifies if the specified value is valid for use as a cover offset.
        
            coverOffset: The cover offset value.
            Returns: True if the value is valid, false if the value is invalid.
        """
        pass

    def IsSingleFabricSheetWithinHost(self, hostElement, transform):
        """
        IsSingleFabricSheetWithinHost(self: FabricSheet, hostElement: Element, transform: Transform) -> bool
        
            Identifies if the specified single Fabric Sheet position is within the host.
        
            hostElement: A structural element that will host the Fabric Sheet.
            transform: The transform that defines the placement of the instance single Fabric Sheet.
            Returns: True if the single Fabric Sheet instance is within the host, false if the 
             single Fabric Sheet instance is out of host.
        """
        pass

    @staticmethod
    def IsValidHost(*__args):
        """
        IsValidHost(document: Document, concreteHostElementId: ElementId) -> bool
        
            Checks whether an element is a valid host for fabric sheet.
        
            document: The document.
            concreteHostElementId: The elementId to check.
            Returns: True if the element is a valid host for fabric sheet, false otherwise.
        IsValidHost(host: Element) -> bool
        
            Checks whether an element is a valid host for fabric sheet.
        
            host: The element to check.
            Returns: True if the element is a valid host for fabric sheet, false otherwise.
        """
        pass

    def PlaceInHost(self, hostElement, transform):
        """
        PlaceInHost(self: FabricSheet, hostElement: Element, transform: Transform)
            Inserts the single Fabric Sheet instance into the host element.
        
            hostElement: A structural element that will host the Fabric Sheet. The element must support 
             fabric hosting.
        
            transform: The transform that defines the placement of the instance single Fabric Sheet.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetBendProfile(self, bendProfile):
        """
        SetBendProfile(self: FabricSheet, bendProfile: CurveLoop)
            Sets new profile that defines the shape of the Fabric Sheet bending.
        
            bendProfile: A profile that defines the bending shape of the fabric sheet.
           The profile 
             can be provided without fillets (eg. for L shape, only two lines not two lines 
             and one arc), if so,
           then fillets (in example one arc) will be 
             automatically generated basing on the Bend Diameter parameter defined in the 
             Fabric Wire system family.
           If the provided profile has no corners (has a 
             tangent defined at each point except the ends), no fillets will be generated.
         
               The provided profile defines the center-curve of a wire.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSegmentLength(self, segmentParameterId, value):
        """
        SetSegmentLength(self: FabricSheet, segmentParameterId: ElementId, value: float)
            Sets the value of the bent fabric sheet segment(like A, B, C, D etc.)
        
            segmentParameterId: The segment ID of the bent fabric sheet.
            value: The length value to set
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

    BendFinalLoopOrientationVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Direction of local Fabric Sheet Y axis in bending polyline LCS.

Get: BendFinalLoopOrientationVector(self: FabricSheet) -> XYZ

"""

    BentFabricBendDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies which wire direction of the fabric sheet is bent.

Get: BentFabricBendDirection(self: FabricSheet) -> BentFabricBendDirection

Set: BentFabricBendDirection(self: FabricSheet) = value
"""

    BentFabricLongitudinalCutLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the cut length of the fabric sheet perpendicular to the bend edge.

Get: BentFabricLongitudinalCutLength(self: FabricSheet) -> float

Set: BentFabricLongitudinalCutLength(self: FabricSheet) = value
"""

    BentFabricStraightWiresLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the location of straight bars with respect to bent bars in the fabric sheet.

Get: BentFabricStraightWiresLocation(self: FabricSheet) -> BentFabricStraightWiresLocation

Set: BentFabricStraightWiresLocation(self: FabricSheet) = value
"""

    BentFabricWiresOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the location of the straight bars in the fabric sheet.

Get: BentFabricWiresOrientation(self: FabricSheet) -> BentFabricWiresOrientation

Set: BentFabricWiresOrientation(self: FabricSheet) = value
"""

    CoverOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The additional cover offset of the Fabric Sheet.

Get: CoverOffset(self: FabricSheet) -> float

Set: CoverOffset(self: FabricSheet) = value
"""

    CutOverallLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet length after cutting has taken place.

Get: CutOverallLength(self: FabricSheet) -> float

"""

    CutOverallWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet length after cutting has taken place.

Get: CutOverallWidth(self: FabricSheet) -> float

"""

    CutSheetMass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet mass after cutting has taken place.

Get: CutSheetMass(self: FabricSheet) -> float

"""

    FabricAreaOwnerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Fabric Area Id.

Get: FabricAreaOwnerId(self: FabricSheet) -> ElementId

"""

    FabricHostReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls if Single Fabric Sheet should be cut by the Host Cover

Get: FabricHostReference(self: FabricSheet) -> FabricHostReference

Set: FabricHostReference(self: FabricSheet) = value
"""

    FabricLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Fabric Sheet location in the host.

Get: FabricLocation(self: FabricSheet) -> FabricLocation

Set: FabricLocation(self: FabricSheet) = value
"""

    FabricNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the numerical parameter assigned to the fabric sheet and any sheet of the same type, dimension, material, shape, and partition.

Get: FabricNumber(self: FabricSheet) -> str

"""

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The structure element that contains the Fabric Sheet.

Get: HostId(self: FabricSheet) -> ElementId

"""

    IsBent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of fabric sheet. True for bent fabric sheet, false for flat fabric sheet.

Get: IsBent(self: FabricSheet) -> bool

"""

    SketchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Sketch element for this element.

Get: SketchId(self: FabricSheet) -> ElementId

"""



class FabricSheetAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabric Sheet alignment in the fabric distribution
    
    enum FabricSheetAlignment, values: BothEdges (3), EndingEdge (2), Null (0), StartingEdge (1)
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

    BothEdges = None
    EndingEdge = None
    Null = None
    StartingEdge = None
    value__ = None


class FabricSheetLayoutPattern(Enum, IComparable, IFormattable, IConvertible):
    """
    The pattern for how the wires in Fabric Sheet are laid out.
    
    enum FabricSheetLayoutPattern, values: ActualSpacing (0), FixedNumber (1), MaximumSpacing (2), NumberWithSpacing (3), QuantitativeSpacing (4)
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

    ActualSpacing = None
    FixedNumber = None
    MaximumSpacing = None
    NumberWithSpacing = None
    QuantitativeSpacing = None
    value__ = None


class FabricSheetType(ElementType, IDisposable):
    """ Represents a fabric sheet type, used in the generation of fabric wires. """
    @staticmethod
    def CreateDefaultFabricSheetType(ADoc):
        """
        CreateDefaultFabricSheetType(ADoc: Document) -> ElementId
        
            Creates a new FabricSheetType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: FabricSheetType) -> FabricRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def GetWireItem(self, wireIndex, direction):
        """
        GetWireItem(self: FabricSheetType, wireIndex: int, direction: WireDistributionDirection) -> FabricWireItem
        
            Gets the Wire stored in the FabricSheetType at the associated index.
        
            wireIndex: Item index in the Fabric Sheet
            direction: Wire distribution direction of the inquired item
            Returns: Fabric wire Item
        """
        pass

    def IsCustom(self):
        """
        IsCustom(self: FabricSheetType) -> bool
        
            Verifies if the type is Custom Fabric Sheet
            Returns: True if Layout is set on Custom and if the wireArr is not null
        """
        pass

    def IsValidMajorLapSplice(self, majorLapSplice):
        """
        IsValidMajorLapSplice(self: FabricSheetType, majorLapSplice: float) -> bool
        
            Identifies if the input value is valid to be applied as the major lap splice
          
              value for this FabricSheetType.
        """
        pass

    def IsValidMinorLapSplice(self, minorLapSplice):
        """
        IsValidMinorLapSplice(self: FabricSheetType, minorLapSplice: float) -> bool
        
            Identifies if the input value is valid to be applied as the minor lap splice
          
              value for this FabricSheetType.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetLayoutAsCustomPattern(self, minorStartOverhang, minorEndOverhang, majorStartOverhang, majorEndOverhang, minorFabricWireItems, majorFabricWireItems):
        """ SetLayoutAsCustomPattern(self: FabricSheetType, minorStartOverhang: float, minorEndOverhang: float, majorStartOverhang: float, majorEndOverhang: float, minorFabricWireItems: IList[FabricWireItem], majorFabricWireItems: IList[FabricWireItem]) """
        pass

    def SetMajorLayoutAsActualSpacing(self, overallWidth, minorStartOverhang, spacing):
        """
        SetMajorLayoutAsActualSpacing(self: FabricSheetType, overallWidth: float, minorStartOverhang: float, spacing: float)
            Sets the major layout pattern as ActualSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallWidth: The entire width of the wire sheet in the minor direction.
            minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
             direction.
        
            spacing: The distance between the wires in the major direction.
        """
        pass

    def SetMajorLayoutAsFixedNumber(self, overallWidth, minorStartOverhang, minorEndOverhang, numberOfWires):
        """
        SetMajorLayoutAsFixedNumber(self: FabricSheetType, overallWidth: float, minorStartOverhang: float, minorEndOverhang: float, numberOfWires: int)
            Sets the major layout pattern as FixedNumber, while specifying the needed 
             parameters for this pattern.
        
        
            overallWidth: The entire width of the wire sheet in the minor direction.
            minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
             direction.
        
            minorEndOverhang: The distance from the last wire to the edge of the sheet in the minor direction.
            numberOfWires: The number of the wires to set in the major direction.
        """
        pass

    def SetMajorLayoutAsMaximumSpacing(self, overallWidth, minorStartOverhang, minorEndOverhang, spacing):
        """
        SetMajorLayoutAsMaximumSpacing(self: FabricSheetType, overallWidth: float, minorStartOverhang: float, minorEndOverhang: float, spacing: float)
            Sets the major layout pattern as MaximumSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallWidth: The entire width of the wire sheet in the minor direction.
            minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
             direction.
        
            minorEndOverhang: The distance from the last wire to the edge of the sheet in the minor direction.
            spacing: The distance between the wires in the major direction.
        """
        pass

    def SetMajorLayoutAsNumberWithSpacing(self, overallWidth, minorStartOverhang, numberOfWires, spacing):
        """
        SetMajorLayoutAsNumberWithSpacing(self: FabricSheetType, overallWidth: float, minorStartOverhang: float, numberOfWires: int, spacing: float)
            Sets the major layout pattern as NumberWithSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallWidth: The entire width of the wire sheet in the minor direction.
            minorStartOverhang: The distance from the edge of the sheet to the first wire in the minor 
             direction.
        
            numberOfWires: The number of the wires to set in the major direction.
            spacing: The distance between the wires in the major direction.
        """
        pass

    def SetMinorLayoutAsActualSpacing(self, overallLength, majorStartOverhang, spacing):
        """
        SetMinorLayoutAsActualSpacing(self: FabricSheetType, overallLength: float, majorStartOverhang: float, spacing: float)
            Sets the minor layout pattern as ActualSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallLength: The entire length of the wire sheet in the major direction.
            majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
             direction.
        
            spacing: The distance between the wires in the minor direction.
        """
        pass

    def SetMinorLayoutAsFixedNumber(self, overallLength, majorStartOverhang, majorEndOverhang, numberOfWires):
        """
        SetMinorLayoutAsFixedNumber(self: FabricSheetType, overallLength: float, majorStartOverhang: float, majorEndOverhang: float, numberOfWires: int)
            Sets the major layout pattern as FixedNumber, while specifying the needed 
             parameters for this pattern.
        
        
            overallLength: The entire length of the wire sheet in the major direction.
            majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
             direction.
        
            majorEndOverhang: The distance from the last wire to the edge of the sheet in the major direction.
            numberOfWires: The number of the wires to set in the minor direction.
        """
        pass

    def SetMinorLayoutAsMaximumSpacing(self, overallLength, majorStartOverhang, majorEndOverhang, spacing):
        """
        SetMinorLayoutAsMaximumSpacing(self: FabricSheetType, overallLength: float, majorStartOverhang: float, majorEndOverhang: float, spacing: float)
            Sets the major layout pattern as MaximumSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallLength: The entire length of the wire sheet in the major direction.
            majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
             direction.
        
            majorEndOverhang: The distance from the last wire to the edge of the sheet in the major direction.
            spacing: The distance between the wires in the minor direction.
        """
        pass

    def SetMinorLayoutAsNumberWithSpacing(self, overallLength, majorStartOverhang, numberOfWires, spacing):
        """
        SetMinorLayoutAsNumberWithSpacing(self: FabricSheetType, overallLength: float, majorStartOverhang: float, numberOfWires: int, spacing: float)
            Sets the major layout pattern as NumberWithSpacing, while specifying the needed 
             parameters for this pattern.
        
        
            overallLength: The entire length of the wire sheet in the major direction.
            majorStartOverhang: The distance from the edge of the sheet to the first wire in the major 
             direction.
        
            numberOfWires: The number of wires in the minor direction.
            spacing: The distance between the wires in the minor direction.
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

    MajorDirectionWireType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FabricWireType to be used in the major direction.

Get: MajorDirectionWireType(self: FabricSheetType) -> ElementId

Set: MajorDirectionWireType(self: FabricSheetType) = value
"""

    MajorEndOverhang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the edge of the sheet to the last wire (measured in the major direction).

Get: MajorEndOverhang(self: FabricSheetType) -> float

"""

    MajorLapSpliceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lap splice length in the major direction.

Get: MajorLapSpliceLength(self: FabricSheetType) -> float

Set: MajorLapSpliceLength(self: FabricSheetType) = value
"""

    MajorLayoutPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The layout pattern in the major direction.

Get: MajorLayoutPattern(self: FabricSheetType) -> FabricSheetLayoutPattern

"""

    MajorNumberOfWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of wires used in the major direction (includes the first and last wires).

Get: MajorNumberOfWires(self: FabricSheetType) -> int

"""

    MajorReinforcementArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The area of fabric divided by the spacing of the wire in the major direction.

Get: MajorReinforcementArea(self: FabricSheetType) -> float

"""

    MajorSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The spacing between the wires in the major direction (not including the overhangs).

Get: MajorSpacing(self: FabricSheetType) -> float

"""

    MajorStartOverhang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the edge of the sheet to the first wire (measured in the major direction).

Get: MajorStartOverhang(self: FabricSheetType) -> float

"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the material assigned to wires.

Get: Material(self: FabricSheetType) -> ElementId

Set: Material(self: FabricSheetType) = value
"""

    MinorDirectionWireType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FabricWireType to be used in the minor direction.

Get: MinorDirectionWireType(self: FabricSheetType) -> ElementId

Set: MinorDirectionWireType(self: FabricSheetType) = value
"""

    MinorEndOverhang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the edge of the sheet to the last wire (measured in the minor direction).

Get: MinorEndOverhang(self: FabricSheetType) -> float

"""

    MinorLapSpliceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lap splice length in the minor direction.

Get: MinorLapSpliceLength(self: FabricSheetType) -> float

Set: MinorLapSpliceLength(self: FabricSheetType) = value
"""

    MinorLayoutPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The layout pattern in the minor direction.

Get: MinorLayoutPattern(self: FabricSheetType) -> FabricSheetLayoutPattern

"""

    MinorNumberOfWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of wires used in the minor direction (includes the 1st and last wires).

Get: MinorNumberOfWires(self: FabricSheetType) -> int

"""

    MinorReinforcementArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The area of fabric divided by the spacing of the wire in the minor direction.

Get: MinorReinforcementArea(self: FabricSheetType) -> float

"""

    MinorSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The spacing between the wires in the minor direction (not including the overhangs).

Get: MinorSpacing(self: FabricSheetType) -> float

"""

    MinorStartOverhang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the edge of the sheet to the first wire (measured in the minor direction).

Get: MinorStartOverhang(self: FabricSheetType) -> float

"""

    OverallLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the wire sheet (including overhangs) in the major direction.

Get: OverallLength(self: FabricSheetType) -> float

"""

    OverallWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the wire sheet (including overhangs) in the minor direction.

Get: OverallWidth(self: FabricSheetType) -> float

"""

    SheetMass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet mass.

Get: SheetMass(self: FabricSheetType) -> float

Set: SheetMass(self: FabricSheetType) = value
"""

    SheetMassUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet mass per area unit.

Get: SheetMassUnit(self: FabricSheetType) -> float

"""



class FabricTagComponentReference(Enum, IComparable, IFormattable, IConvertible):
    """
    How FabricSheet tag text will be aligned to the FabricSheet symbol.
    
    enum FabricTagComponentReference, values: Diagonal (2), Intersection (3), MajorAxis (0), MinorAxis (1)
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

    Diagonal = None
    Intersection = None
    MajorAxis = None
    MinorAxis = None
    value__ = None


class FabricWireItem(object, IDisposable):
    """ Provides implementation for FabricWires stored in a Custom Fabric Sheet """
    @staticmethod
    def Create(distance, wireLength, wireType):
        """
        Create(distance: float, wireLength: float, wireType: ElementId) -> FabricWireItem
        
            Creates a new instance of a single Fabric wire.
        
            distance: The distance between this wire and the next wire in the Custom Fabric Sheet
            wireLength: Length of this wire
            wireType: The wire type of this wire
            Returns: The newly created Fabric wire instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricWireItem) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricWireItem, disposing: bool) """
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

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance to the next fabric wire item

Get: Distance(self: FabricWireItem) -> float

Set: Distance(self: FabricWireItem) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricWireItem) -> bool

"""

    WireLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wire length for this wire item

Get: WireLength(self: FabricWireItem) -> float

Set: WireLength(self: FabricWireItem) = value
"""

    WireType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wire type of this wire item

Get: WireType(self: FabricWireItem) -> ElementId

Set: WireType(self: FabricWireItem) = value
"""



class FabricWireType(ElementType, IDisposable):
    """ A Fabric Wire Type object that is used in the generation of Fabric Wire. """
    @staticmethod
    def CreateDefaultFabricWireType(ADoc):
        """
        CreateDefaultFabricWireType(ADoc: Document) -> ElementId
        
            Creates a new FabricWireType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
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

    BendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the bending diameter of the wire.

Get: BendDiameter(self: FabricWireType) -> float

Set: BendDiameter(self: FabricWireType) = value
"""

    WireDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the diameter of the wire.

Get: WireDiameter(self: FabricWireType) -> float

Set: WireDiameter(self: FabricWireType) = value
"""



class FamilyStructuralMaterialTypeFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match families that have the given structural material type.
    
    FamilyStructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType, inverted: bool)
    FamilyStructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType)
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

    @staticmethod # known case of __new__
    def __new__(self, structuralMaterialType, inverted=None):
        """
        __new__(cls: type, structuralMaterialType: StructuralMaterialType, inverted: bool)
        __new__(cls: type, structuralMaterialType: StructuralMaterialType)
        """
        pass

    StructuralMaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The family structural material type.

Get: StructuralMaterialType(self: FamilyStructuralMaterialTypeFilter) -> StructuralMaterialType

"""



class Hub(Element, IDisposable):
    """ Represents a connection between two or more Autodesk Revit Elements. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHubConnectorManager(self):
        """
        GetHubConnectorManager(self: Hub) -> ConnectorManager
        
            Retrieves the ConnectorManager of the Hub.
            Returns: The ConnectorManager.
        """
        pass

    def GetOrigin(self):
        """
        GetOrigin(self: Hub) -> XYZ
        
            Retrieves position of a Hub if such position is a 3D point.
            Returns: The origin.
        """
        pass

    def HasOrigin(self):
        """
        HasOrigin(self: Hub) -> bool
        
            Provides information if Hub has a specific location at point in 3D space.
            Returns: True if the Hub has a specific location at point in 3D space.
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


class ICodeCheckingParameterServer(IExternalServer):
    """ Interface for the code checking parameter server to implement. """
    def PerformCodeChecking(self, data):
        """
        PerformCodeChecking(self: ICodeCheckingParameterServer, data: CodeCheckingParameterServiceData) -> bool
        
            The server's method that will be called when Revit User clicks the Code 
             Checking parameter's button from the properties palette.
        
        
            data: The Code Checking data.
            Returns: Indicates whether the code checking parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMemberForcesServer(IExternalServer):
    """ Interface for the Member Forces server to implement. """
    def MemberForcesUpdate(self, data):
        """
        MemberForcesUpdate(self: IMemberForcesServer, data: MemberForcesServiceData) -> bool
        
            The server's method that will be called when Revit User clicks Member Forces 
             button in the MPP.
        
        
            data: The Moment Forces data.
            Returns: Indicates whether themember forces parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStructuralSectionsServer(IExternalServer):
    """ Interface for the section type parameter server to implement. """
    def StructuralSectionsUpdate(self, data):
        """
        StructuralSectionsUpdate(self: IStructuralSectionsServer, data: StructuralSectionsServiceData) -> bool
        
            The server's method that will be called when Revit User clicks the Section Type 
             parameter's button in the family dialog.
        
        
            data: The Section Type data.
            Returns: Indicates whether the section type parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LineLoad(LoadBase, IDisposable):
    """ An object that represents a force/moment applied in a linear manner. """
    @staticmethod
    def Create(aDoc, *__args):
        """
        Create(aDoc: Document, host: AnalyticalModelStick, forceVector1: XYZ, momentVector1: XYZ, symbol: LineLoadType) -> LineLoad
        
            Creates a new hosted line load within the project.
        
            aDoc: Document to which new line load will be added.
            host: The analytical model stick host element for the line Load.
            forceVector1: The applied 3d force vector.
            momentVector1: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        Create(aDoc: Document, host: AnalyticalModelSurface, curveIndex: int, forceVector1: XYZ, momentVector1: XYZ, symbol: LineLoadType) -> LineLoad
        
            Creates a new hosted line load within the project.
        
            aDoc: Document to which new line load will be added.
            host: The analytical model surface host element for the line Load.
            curveIndex: The index of a curve in analytical surface element starting from 0.
           Use 
             Autodesk::Revit::DB::Structure::AnalyticalModelSurface::GetLoops(Autodesk::Revit
             ::DB::Structure::AnalyticalLoopType::All) method to obtain appropriate curve 
             index.
           Curve index has a unique value in analytical surface element even if 
             it contains more than one loop. The index should be obtain by iteration through 
             all curves in all loops.
        
            forceVector1: The applied 3d force vector.
            momentVector1: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        Create(aDoc: Document, startPoint: XYZ, endPoint: XYZ, forceVector: XYZ, momentVector: XYZ, symbol: LineLoadType, plane: SketchPlane) -> LineLoad
        
            Creates a new non-hosted line load within the project using data at point.
        
            aDoc: Document to which new line load will be added.
            startPoint: The start point of line load, measured in decimal feet.
            endPoint: The end point of line load, measured in decimal feet.
            forceVector: The applied 3d force vector.
            momentVector: The applied 3d moment vector.
            symbol: The symbol of the LineLoad. Set ll to use default type.
            plane: The work plane of the LineLoad. Set ll to use default plane.
            Returns: If successful, returns the newly created LineLoad, ll otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurve(self):
        """
        GetCurve(self: LineLoad) -> Curve
        
            Returns curve that define geometry of the line load.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPoints(self, startPoint, endPoint):
        """
        SetPoints(self: LineLoad, startPoint: XYZ, endPoint: XYZ) -> bool
        
            Sets start and end point of the line load.
        
            startPoint: The start point.
            endPoint: The end point.
            Returns: Returns true if successful, false otherwise.
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

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the three dimensional location of the end point for the line load.

Get: EndPoint(self: LineLoad) -> XYZ

"""

    ForceVector1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the start point of the line load, oriented according to OrientTo setting.

Get: ForceVector1(self: LineLoad) -> XYZ

Set: ForceVector1(self: LineLoad) = value
"""

    ForceVector2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the end point of the line load, oriented according to OrientTo setting.

Get: ForceVector2(self: LineLoad) -> XYZ

Set: ForceVector2(self: LineLoad) = value
"""

    IsProjected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load is projected.

Get: IsProjected(self: LineLoad) -> bool

Set: IsProjected(self: LineLoad) = value
"""

    IsUniform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load is uniform.

Get: IsUniform(self: LineLoad) -> bool

"""

    MomentVector1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moment vector applied to the start point of the line load, oriented according to OrientTo setting.

Get: MomentVector1(self: LineLoad) -> XYZ

Set: MomentVector1(self: LineLoad) = value
"""

    MomentVector2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moment vector applied to the end point of the line load, oriented according to OrientTo setting.

Get: MomentVector2(self: LineLoad) -> XYZ

Set: MomentVector2(self: LineLoad) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the three dimensional location of the start point for the line load.

Get: StartPoint(self: LineLoad) -> XYZ

"""



class LineLoadType(LoadTypeBase, IDisposable):
    """ An object that represents a Load type. """
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


class LoadCase(Element, IDisposable):
    """ An object that represents a load usage. """
    @staticmethod
    def Create(document, name, natureId, *__args):
        """
        Create(document: Document, name: str, natureId: ElementId, loadCaseCategory: LoadCaseCategory) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            loadCaseCategory: The predefined load case category.
            Returns: The newly created load case element if successful, ll otherwise.
        Create(document: Document, name: str, natureId: ElementId, subcategoryId: ElementId) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            subcategoryId: The load case subcategory ID. Could be one of predefined or user defined load 
             case category.
           Built-in structural Load Cases 
             (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) subcategories are:
           
             Autodesk.Revit.DB.BuiltInCategory.OST_LoadCasesDeadAutodesk.Revit.DB.BuiltInCate
             gory.OST_LoadCasesLiveAutodesk.Revit.DB.BuiltInCategory.OST_LoadCasesWindAutodes
             k.Revit.DB.BuiltInCategory.OST_LoadCasesSnowAutodesk.Revit.DB.BuiltInCategory.OS
             T_LoadCasesRoofLiveAutodesk.Revit.DB.BuiltInCategory.OST_LoadCasesAccidentalAuto
             desk.Revit.DB.BuiltInCategory.OST_LoadCasesTemperatureAutodesk.Revit.DB.BuiltInC
             ategory.OST_LoadCasesSeismic
        
            Returns: The newly created load case element if successful, ll otherwise.
        Create(document: Document, name: str, natureId: ElementId, natureCategory: LoadNatureCategory) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            natureCategory: The predefined load nature category.
            Returns: The newly created load case element if successful, ll otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsLoadCaseSubcategoryId(self, loadCaseSubcategoryId):
        """
        IsLoadCaseSubcategoryId(self: LoadCase, loadCaseSubcategoryId: ElementId) -> bool
        
            Checks whether provided element ID refer to subcategory of Structural Load 
             Cases (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) category - one of 
             built-in or user defined.
        
        
            loadCaseSubcategoryId: The ID to check.
            Returns: True if the ID refers to load case category element, false otherwise.
        """
        pass

    def IsLoadNatureId(self, natureId):
        """
        IsLoadNatureId(self: LoadCase, natureId: ElementId) -> bool
        
            Checks whether provided element ID refer to LoadNature element.
        
            natureId: The ID to check.
            Returns: True if the ID refers to LoadNature element, false otherwise.
        """
        pass

    @staticmethod
    def IsNumberUnique(document, number):
        """
        IsNumberUnique(document: Document, number: int) -> bool
        
            Checks that a given number is unique among all load cases.
        
            number: The number to check.
            Returns: True if the given number is unique among all load cases, false otherwise.
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

    NatureCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nature category of the load case.

Get: NatureCategory(self: LoadCase) -> LoadNatureCategory

Set: NatureCategory(self: LoadCase) = value
"""

    NatureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nature ID of the load case.

Get: NatureId(self: LoadCase) -> ElementId

Set: NatureId(self: LoadCase) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns unique load case number.

Get: Number(self: LoadCase) -> int

Set: Number(self: LoadCase) = value
"""

    SubcategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Build-in or user defined subcategory of Structural Load Cases (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) category.

Get: SubcategoryId(self: LoadCase) -> ElementId

Set: SubcategoryId(self: LoadCase) = value
"""



class LoadCaseCategory(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies load case category.
    
    enum LoadCaseCategory, values: Accidental (5), Dead (0), Live (1), RoofLive (4), Seismic (7), Snow (3), Temperature (6), Wind (2)
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

    Accidental = None
    Dead = None
    Live = None
    RoofLive = None
    Seismic = None
    Snow = None
    Temperature = None
    value__ = None
    Wind = None


class LoadCombination(Element, IDisposable):
    """ An object that represents a load combination. """
    @staticmethod
    def Create(document, name, type=None, state=None):
        """
        Create(document: Document, name: str) -> LoadCombination
        
            Creates a new default LoadCombination.
        
            document: The Document to which new load combination element will be added.
            name: The name of the load combination.
            Returns: The newly created load combination element if successful, ll otherwise.
        Create(document: Document, name: str, type: LoadCombinationType, state: LoadCombinationState) -> LoadCombination
        
            Creates a new LoadCombination.
        
            document: The Document to which new load combination element will be added.
            name: The name of the load combination.
            type: The type of the load combination.
            state: The state of the load combination.
            Returns: The newly created load combination element if successful, ll otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCaseAndCombinationIds(self):
        """
        GetCaseAndCombinationIds(self: LoadCombination) -> IList[ElementId]
        
            Returns collection of the load combination case and combination IDs.
            Returns: A collection of the load combination case and combination IDs.
        """
        pass

    def GetComponents(self):
        """
        GetComponents(self: LoadCombination) -> IList[LoadComponent]
        
            Returns collection of the load combination components.
            Returns: A collection of the load combination components.
        """
        pass

    def GetUsageIds(self):
        """
        GetUsageIds(self: LoadCombination) -> IList[ElementId]
        
            Returns collection of the load combination usage IDs.
            Returns: A collection of the load combination usage IDs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetComponents(self, components):
        """ SetComponents(self: LoadCombination, components: IList[LoadComponent]) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetUsageIds(self, usageIds):
        """ SetUsageIds(self: LoadCombination, usageIds: IList[ElementId]) """
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

    IsThirdPartyGenerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the load combination was created by API.

Get: IsThirdPartyGenerated(self: LoadCombination) -> bool

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the load combination.

Get: State(self: LoadCombination) -> LoadCombinationState

Set: State(self: LoadCombination) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the load combination.

Get: Type(self: LoadCombination) -> LoadCombinationType

Set: Type(self: LoadCombination) = value
"""



class LoadCombinationState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies load combination state.
    
    enum LoadCombinationState, values: Serviceability (0), Ultimate (1)
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

    Serviceability = None
    Ultimate = None
    value__ = None


class LoadCombinationType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies load combination type.
    
    enum LoadCombinationType, values: Combination (0), Envelope (1)
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

    Combination = None
    Envelope = None
    value__ = None


class LoadComponent(object, IDisposable):
    """
    An object that represents a load combination component.
    
    LoadComponent(loadCaseOrCombinationId: ElementId, factor: float)
    """
    def Dispose(self):
        """ Dispose(self: LoadComponent) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LoadComponent, disposing: bool) """
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
    def __new__(self, loadCaseOrCombinationId, factor):
        """ __new__(cls: type, loadCaseOrCombinationId: ElementId, factor: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load component factor.

Get: Factor(self: LoadComponent) -> float

Set: Factor(self: LoadComponent) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LoadComponent) -> bool

"""

    LoadCaseOrCombinationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load case or combination id.

Get: LoadCaseOrCombinationId(self: LoadComponent) -> ElementId

Set: LoadCaseOrCombinationId(self: LoadComponent) = value
"""



class LoadNature(Element, IDisposable):
    """ An object that represents a load nature. """
    @staticmethod
    def Create(document, name):
        """
        Create(document: Document, name: str) -> LoadNature
        
            Creates a new LoadNature.
        
            document: The Document to which new load nature element will be added.
            name: The name of the load nature.
            Returns: The newly created load nature element if successful, ll otherwise.
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


class LoadNatureCategory(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies load case nature.
    
    enum LoadNatureCategory, values: Accidental (5), Dead (0), Live (1), RoofLive (4), Seismic (7), Snow (3), Temperature (6), Wind (2)
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

    Accidental = None
    Dead = None
    Live = None
    RoofLive = None
    Seismic = None
    Snow = None
    Temperature = None
    value__ = None
    Wind = None


class LoadOrientTo(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies load orientation.
    
    enum LoadOrientTo, values: HostLocalCoordinateSystem (2), Project (0), WorkPlane (1)
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

    HostLocalCoordinateSystem = None
    Project = None
    value__ = None
    WorkPlane = None


class LoadType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum declares types of Loads.
    
    enum LoadType, values: Area (2), Line (1), Point (0)
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

    Area = None
    Line = None
    Point = None
    value__ = None


class LoadUsage(Element, IDisposable):
    """ An object that represents a load usage. """
    @staticmethod
    def Create(document, name):
        """
        Create(document: Document, name: str) -> LoadUsage
        
            Creates a new LoadUsage.
        
            document: The Document to which new load usage element will be added.
            name: The name of the load usage.
            Returns: The newly created load usage element if successful, ll otherwise.
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


class MemberForces(object, IDisposable):
    """
    An object that represents a member forces on analytical model element.
    
    MemberForces(start: bool, force: XYZ, moment: XYZ)
    """
    def Dispose(self):
        """ Dispose(self: MemberForces) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MemberForces, disposing: bool) """
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
    def __new__(self, start, force, moment):
        """ __new__(cls: type, start: bool, force: XYZ, moment: XYZ) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Force = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The translational forces at relative point position of the element.

Get: Force(self: MemberForces) -> XYZ

Set: Force(self: MemberForces) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MemberForces) -> bool

"""

    Moment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rotational forces at relative point position of the element.

Get: Moment(self: MemberForces) -> XYZ

Set: Moment(self: MemberForces) = value
"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Member Forces position on analytical model stick element. True for start, false for end.

Get: Start(self: MemberForces) -> bool

Set: Start(self: MemberForces) = value
"""



class MemberForcesServiceData(object, IDisposable):
    """
    The data needed by member forces server to perform type definition.
    
    MemberForcesServiceData(document: Document, currentElementIds: IList[ElementId])
    """
    def Dispose(self):
        """ Dispose(self: MemberForcesServiceData) """
        pass

    def GetCurrentElements(self):
        """
        GetCurrentElements(self: MemberForcesServiceData) -> IList[ElementId]
        
            Returns the list of Ids of the current elements.
            Returns: Ids of the current elements. Contains the family base element to which the 
             Member Forces parameters belongs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MemberForcesServiceData, disposing: bool) """
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
    def __new__(self, document, currentElementIds):
        """ __new__(cls: type, document: Document, currentElementIds: IList[ElementId]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current document.

Get: Document(self: MemberForcesServiceData) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MemberForcesServiceData) -> bool

"""



class MultiplanarOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Input argument type for Rebar.GetCenterlineCurves method.
       Controls whether all curves of a multi-planar Rebar element are returned by
       GetCenterlineCurves, or only the curves in the primary plane.
    
    enum MultiplanarOption, values: IncludeAllMultiplanarCurves (0), IncludeOnlyPlanarCurves (1)
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

    IncludeAllMultiplanarCurves = None
    IncludeOnlyPlanarCurves = None
    value__ = None


class PathReinforcement(Element, IDisposable):
    """ An object that represents an Path Reinforcement within the Autodesk Revit project. """
    @staticmethod
    def Create(document, hostElement, curveArray, flip, pathReinforcementTypeId, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId, rebarShapeId=None):
        """
        Create(document: Document, hostElement: Element, curveArray: IList[Curve], flip: bool, pathReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId) -> PathReinforcement
        Create(document: Document, hostElement: Element, curveArray: IList[Curve], flip: bool, pathReinforcementTypeId: ElementId, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId, rebarShapeId: ElementId) -> PathReinforcement
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurveElementIds(self):
        """
        GetCurveElementIds(self: PathReinforcement) -> IList[ElementId]
        
            Retrieves the set of ElementIds of curves forming the boundary of the Path 
             Reinforcement.
        
            Returns: A collection of ElementIds of ModelCurve elements.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: PathReinforcement) -> ElementId
        
            The element that contains the Path Reinforcement.
            Returns: The element that the Path Reinforcement object belongs to, such as a structural
             
           wall, floor or foundation.
        """
        pass

    @staticmethod
    def GetOrCreateDefaultRebarShape(document, rebarBarTypeId, startRebarHookTypeId, endRebarHookTypeId):
        """
        GetOrCreateDefaultRebarShape(document: Document, rebarBarTypeId: ElementId, startRebarHookTypeId: ElementId, endRebarHookTypeId: ElementId) -> ElementId
        
            Creates a new RebarShape object with a default name or
           returns existing one 
             which fulfills Path Reinforcement bending data requirements.
        
        
            document: The document.
            rebarBarTypeId: The id of the RebarBarType.
            startRebarHookTypeId: The id of the RebarHookType for the start of the bar.
           If this parameter is 
             InvalidElementId, it means to create a rebar with no start hook.
        
            endRebarHookTypeId: The id of the RebarHookType for the end of the bar.
           If this parameter is 
             InvalidElementId, it means to create a rebar with no end hook.
        
            Returns: Rebar Shape id.
        """
        pass

    def GetRebarInSystemIds(self):
        """
        GetRebarInSystemIds(self: PathReinforcement) -> IList[ElementId]
        
            Returns the ids of the RebarInSystem elements owned by the PathReinforcement
          
              element.
        """
        pass

    def IsAlternatingLayerEnabled(self):
        """
        IsAlternatingLayerEnabled(self: PathReinforcement) -> bool
        
            Checks if alternating bars are present in Path Reinforcement.
            Returns: True if the alternating bars exist in Path Reinforcement instance.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: PathReinforcement, view: View3D) -> bool
        
            Checks if this Path Reinforcement is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if Path Reinforcement is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: PathReinforcement, view: View) -> bool
        
            Checks if Path Reinforcement is shown unobscured in a view.
        
            view: The view element
            Returns: True if Path Reinforcement is shown unobscured, false otherwise.
        """
        pass

    def IsValidAlternatingBarOrientation(self, orientation):
        """
        IsValidAlternatingBarOrientation(self: PathReinforcement, orientation: ReinforcementBarOrientation) -> bool
        
            Checks if orientation for alternating bars is valid.
        
            orientation: An orientation.
            Returns: True if orientation for alternating bars are valid.
        """
        pass

    def IsValidPrimaryBarOrientation(self, orientation):
        """
        IsValidPrimaryBarOrientation(self: PathReinforcement, orientation: ReinforcementBarOrientation) -> bool
        
            Checks if orientation for primary bars is valid.
        
            orientation: An orientation.
            Returns: True if orientation for primary bars are valid.
        """
        pass

    @staticmethod
    def IsValidRebarShapeId(aDoc, elementId):
        """
        IsValidRebarShapeId(aDoc: Document, elementId: ElementId) -> bool
        
            Identifies whether an element id corresponds to a Rebar Shape element which can 
             be used in Path Reinforcement.
        
        
            aDoc: The document.
            elementId: An element id.
            Returns: True if the specified element id corresponds to a Rebar Shape element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def RemovePathReinforcementSystem(doc, system):
        """
        RemovePathReinforcementSystem(doc: Document, system: PathReinforcement) -> IList[ElementId]
        
            Deletes the specified PathReinforcement, and converts its RebarInSystem
           
             elements to equivalent Rebar elements.
        
        
            doc: The document.
            system: A PathReinforcement element in the document.
            Returns: The ids of the newly created Rebar elements.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: PathReinforcement, view: View3D, solid: bool)
            Sets this Path Reinforcement to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if Path Reinforcement is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: PathReinforcement, view: View, unobscured: bool)
            Sets Path Reinforcement to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if Path Reinforcement is shown unobscured, false otherwise.
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

    AdditionalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional offset of rebars in the Path Reinforcement.

Get: AdditionalOffset(self: PathReinforcement) -> float

Set: AdditionalOffset(self: PathReinforcement) = value
"""

    AlternatingBarOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Orientation of alternating bars of Path Reinforcement.

Get: AlternatingBarOrientation(self: PathReinforcement) -> ReinforcementBarOrientation

Set: AlternatingBarOrientation(self: PathReinforcement) = value
"""

    AlternatingBarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the alternating bars of the Path Reinforcement.

Get: AlternatingBarShapeId(self: PathReinforcement) -> ElementId

Set: AlternatingBarShapeId(self: PathReinforcement) = value
"""

    PathReinforcementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the type of the Path Reinforcement.

Get: PathReinforcementType(self: PathReinforcement) -> PathReinforcementType

"""

    PrimaryBarOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Orientation of primary bars of Path Reinforcement.

Get: PrimaryBarOrientation(self: PathReinforcement) -> ReinforcementBarOrientation

Set: PrimaryBarOrientation(self: PathReinforcement) = value
"""

    PrimaryBarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the primary bars of the Path Reinforcement.

Get: PrimaryBarShapeId(self: PathReinforcement) -> ElementId

Set: PrimaryBarShapeId(self: PathReinforcement) = value
"""



class PathReinforcementType(ElementType, IDisposable):
    """ An object that specifies the type of a Structural Path Reinforcement element in Autodesk Revit. """
    @staticmethod
    def CreateDefaultPathReinforcementType(ADoc):
        """
        CreateDefaultPathReinforcementType(ADoc: Document) -> ElementId
        
            Creates a new PathReinforcementType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
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


class PathReinSpanSymbol(IndependentTag, IDisposable):
    """ Represents a Path Reinforcement Span Symbol element in Autodesk Revit. """
    @staticmethod
    def Create(document, viewId, hostId, point, symbolId):
        """
        Create(document: Document, viewId: ElementId, hostId: LinkElementId, point: XYZ, symbolId: ElementId) -> PathReinSpanSymbol
        
            Creates a new instance of PathReinSpanSymbol in the project.
        
            document: The document.
            viewId: The id of the view in which the symbol should appear.
            hostId: The ElementId of PathReinforcement (either in the document, or linked from 
             another document).
        
            point: The span symbol's head position.
            symbolId: The family symbol id of this element.
            Returns: A reference to newly created span symbol.
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


class PointLoad(LoadBase, IDisposable):
    """ An object that represents a force/moment applied to a single point. """
    @staticmethod
    def Create(aDoc, *__args):
        """
        Create(aDoc: Document, host: AnalyticalModelStick, selector: AnalyticalElementSelector, forceVector: XYZ, momentVector: XYZ, symbol: PointLoadType) -> PointLoad
        
            Creates a new hosted point load within the project.
        
            aDoc: Document to which new point load will be added.
            host: The AnalyticalModelStick (Analytical Beam, Analytical Brace, Analytical Column) 
             host element for the point Load.
        
            selector: The start or end point of the Analytical stick element.
            forceVector: The applied 3d force vector.
            momentVector: The applied 3d moment vector.
            symbol: The symbol of the PointLoad. Set ll to use default type.
            Returns: If successful, returns the newly created PointLoad, ll otherwise.
        Create(aDoc: Document, host: AnalyticalModel, forceVector: XYZ, momentVector: XYZ, symbol: PointLoadType) -> PointLoad
        
            Creates a new hosted point load within the project.
        
            aDoc: Document to which new point load will be added.
            host: The Analytical Isolated Foundation type host element for the point Load.
            forceVector: The applied 3d force vector.
            momentVector: The applied 3d moment vector.
            symbol: The symbol of the PointLoad. Set ll to use default type.
            Returns: If successful, returns the newly created PointLoad, ll otherwise.
        Create(aDoc: Document, point: XYZ, forceVector: XYZ, momentVector: XYZ, symbol: PointLoadType, plane: SketchPlane) -> PointLoad
        
            Creates a new non-hosted point load within the project using data at point.
        
            aDoc: Document to which new point load will be added.
            point: The position of point load, measured in decimal feet.
            forceVector: The applied 3d force vector.
            momentVector: The applied 3d moment vector.
            symbol: The symbol of the PointLoad. Set ll to use default type.
            plane: The work plane of the PointLoad. Set ll to use default plane.
            Returns: If successful, returns the newly created PointLoad, ll otherwise.
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

    ForceVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The force vector applied to the point load, oriented according to OrientTo setting.

Get: ForceVector(self: PointLoad) -> XYZ

Set: ForceVector(self: PointLoad) = value
"""

    MomentVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moment vector applied to the point load, oriented according to OrientTo setting.

Get: MomentVector(self: PointLoad) -> XYZ

Set: MomentVector(self: PointLoad) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the position of point load, measured in decimal feet.

Get: Point(self: PointLoad) -> XYZ

Set: Point(self: PointLoad) = value
"""



class PointLoadType(LoadTypeBase, IDisposable):
    """ An object that represents a Load type. """
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


class Rebar(Element, IDisposable):
    """ Represents a rebar element in Autodesk Revit. """
    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: Rebar, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this rebar in the given view.
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if presentation mode can be applied for this view, false otherwise.
        """
        pass

    def CanSuppressFirstOrLastBar(self, dBView, end):
        """
        CanSuppressFirstOrLastBar(self: Rebar, dBView: View, end: int) -> bool
        
            Checks if the first or last bar in rebar set can be hidden in the given view.
        
            dBView: The view in which presentation mode will be applied.
            end: 0 for the first bar in rebar set, 1 for the last bar.
            Returns: True the first or last bar in rebar set can be hidden for this view, false 
             otherwise.
        """
        pass

    def CanUseHookType(self, proposedHookId):
        """
        CanUseHookType(self: Rebar, proposedHookId: ElementId) -> bool
        
            Checks if the specified RebarHookType id is of a valid RebarHookType for the 
             Rebar's RebarBarType
        
        
            proposedHookId: The Id of the RebarHookType
            Returns: Returns true if the id is of a valid RebarHookType for the Rebar element.
        """
        pass

    def ClearPresentationMode(self, dBView):
        """
        ClearPresentationMode(self: Rebar, dBView: View)
            Sets the presentation mode for this rebar set to the default (either for a 
             single view, or for all views).
        
        
            dBView: The view where the presentation mode will be cleared. NULL for all views
        """
        pass

    def ComputeDrivingCurves(self):
        """
        ComputeDrivingCurves(self: Rebar) -> IList[Curve]
        
            Compute the driving curves.
            Returns: Returns an empty array if an error is encountered.
        """
        pass

    def ConstraintsCanBeEdited(self):
        """
        ConstraintsCanBeEdited(self: Rebar) -> bool
        
            Returns true, if the Rebar element's external constraints are available for 
             editing using the
           RebarConstraintsManager class.  Examples of where this 
             method would return false are:
           Rebar in Groups (which do not have 
             constraints), or legacy, sketch-based Rebar elements
           created before the 
             introduction of RebarShape families in version 2009.
        """
        pass

    @staticmethod
    def ContainsValidArcRadiiForStyleAndBarType(curves, style, barType):
        """ ContainsValidArcRadiiForStyleAndBarType(curves: IList[Curve], style: RebarStyle, barType: RebarBarType) -> bool """
        pass

    @staticmethod
    def CreateFromCurves(doc, style, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape):
        """ CreateFromCurves(doc: Document, style: RebarStyle, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, host: Element, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation, useExistingShapeIfPossible: bool, createNewShape: bool) -> Rebar """
        pass

    @staticmethod
    def CreateFromCurvesAndShape(doc, rebarShape, barType, startHook, endHook, host, norm, curves, startHookOrient, endHookOrient):
        """ CreateFromCurvesAndShape(doc: Document, rebarShape: RebarShape, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, host: Element, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> Rebar """
        pass

    @staticmethod
    def CreateFromRebarShape(doc, rebarShape, barType, host, origin, xVec, yVec):
        """
        CreateFromRebarShape(doc: Document, rebarShape: RebarShape, barType: RebarBarType, host: Element, origin: XYZ, xVec: XYZ, yVec: XYZ) -> Rebar
        
            Creates a new Rebar, as an instance of a RebarShape.
           The instance will have 
             the default shape parameters from the RebarShape,
           and its location is based 
             on the bounding box of the shape in the shape definition.
           Hooks are removed 
             from the shape before computing its bounding box.
           If appropriate hooks can 
             be found in the document, they will be assigned arbitrarily.
        
        
            doc: A document.
            rebarShape: A RebarShape element that defines the shape of the rebar.
            barType: A RebarBarType element that defines bar diameter, bend radius and material of 
             the rebar.
        
            host: The element to which the rebar belongs. The element must support rebar hosting;
             
           see Autodesk.Revit.DB.Structure.RebarHostData.
        
            origin: The lower-left corner of the shape's bounding box will be placed at this point 
             in the project.
        
            xVec: The x-axis in the shape definition will be mapped to this direction in the 
             project.
        
            yVec: The y-axis in the shape definition will be mapped to this direction in the 
             project.
        
            Returns: The newly created Rebar instance, or ll if the operation fails.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def DoesBarExistAtPosition(self, barPosition):
        """
        DoesBarExistAtPosition(self: Rebar, barPosition: int) -> bool
        
            Checks whether a bar exists at the specified position.
        
            barPosition: A bar position index between 0 and NumberOfBarPositions-1.
        """
        pass

    def FindMatchingPredefinedPresentationMode(self, dBView):
        """
        FindMatchingPredefinedPresentationMode(self: Rebar, dBView: View) -> RebarPresentationMode
        
            Determines if there is a matching RebarPresentationMode for the current set of 
             selected hidden and unhidden bars assigned to the given view.
        
        
            dBView: The view.
            Returns: The presentation mode that matches the current set of selected hidden and 
             unhidden bars.
           If there is no better match, this returns 
             RebarPresentationMode.Select.
        """
        pass

    def GetBarPositionTransform(self, barPositionIndex):
        """
        GetBarPositionTransform(self: Rebar, barPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of any
           individual bar 
             in the set.
        
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
            Returns: The position of a bar in the set relative to the first position.
        """
        pass

    def GetBendData(self):
        """
        GetBendData(self: Rebar) -> RebarBendData
        
            Gets the RebarBendData, containing bar and hook information, of the instance.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCenterlineCurves(self, adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption=None, barPositionIndex=None):
        """
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool, multiplanarOption: MultiplanarOption) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            multiplanarOption: If the Rebar is a multi-planar shape, this parameter controls whether to 
             generate only
           the curves in the primary plane (IncludeOnlyPlanarCurves), or 
             to generate all curves,
           (IncludeAllMultiplanarCurves) including the 
             out-of-plane connector segments as well as
           multi-planar copies of the 
             primary plane curves.
           This argument is ignored for planar shapes.
        
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        
        GetCenterlineCurves(self: Rebar, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool, multiplanarOption: MultiplanarOption, barPositionIndex: int) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            multiplanarOption: If the Rebar is a multi-planar shape, this parameter controls whether to 
             generate only
           the curves in the primary plane (IncludeOnlyPlanarCurves), or 
             to generate all curves,
           (IncludeAllMultiplanarCurves) including the 
             out-of-plane connector segments as well as
           multi-planar copies of the 
             primary plane curves.
           This argument is ignored for planar shapes.
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
           Use the barPositionIndex 
             to obtain all the curves at a specific index in the distribution.
           You can 
             use GetNumberOfBarPositions() to verify if a specific rebar has more than one 
             bar positions.
           Use GetDistributionType() to probe if the bars in a specific 
             rebar have a varying shape. If so, you can retrieve the centerline curve 
             geometry of that particular bar, by passing the appropriate index.
           When the 
             distribution type of a rebar set is uniform, the form of the bars does not vary 
             from one index to another.
        
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        """
        pass

    def GetCouplerId(self, end):
        """
        GetCouplerId(self: Rebar, end: int) -> ElementId
        
            Get the id of the Rebar Coupler that is applied to the rebar at the specified 
             end.
        
        
            end: 0 for the start Rebar Coupler, 1 for the end Rebar Coupler.
            Returns: The id of a Rebar Coupler, or invalidElementId if the rebar has
           no Rebar 
             Coupler at the specified end.
        """
        pass

    def GetDistributionPath(self):
        """
        GetDistributionPath(self: Rebar) -> Line
        
            The distribution path of a rebar set.
            Returns: A line beginning at (0, 0, 0) and representing the direction and
           length of 
             the set.
        """
        pass

    def GetEndTreatmentTypeId(self, end):
        """
        GetEndTreatmentTypeId(self: Rebar, end: int) -> ElementId
        
            Get the id of the EndTreatmentType to be applied to the rebar.
        
            end: 0 for the start end treatment, 1 for the end end treatment.
            Returns: The id of a EndTreatmentType, or invalidElementId if the rebar has
           no end 
             treatment at the specified end.
        """
        pass

    def GetFullGeometryForView(self, view):
        """
        GetFullGeometryForView(self: Rebar, view: View) -> GeometryElement
        
            Generates full geometry for the Rebar for a specific view.
        
            view: The view in which the geometry is generated.
            Returns: The generated geometry of the Rebar before cutting is applied.
        """
        pass

    def GetHookOrientation(self, iEnd):
        """
        GetHookOrientation(self: Rebar, iEnd: int) -> RebarHookOrientation
        
            Returns the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            Returns: Value = Right: The hook is on your right as you stand at the end of the bar,
          
              with the bar behind you, taking the bar's normal as "up."
           Value = Left: 
             The hook is on your left as you stand at the end of the bar,
           with the bar 
             behind you, taking the bar's normal as "up."
        """
        pass

    def GetHookTypeId(self, end):
        """
        GetHookTypeId(self: Rebar, end: int) -> ElementId
        
            Get the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            Returns: The id of a RebarHookType, or invalidElementId if the rebar has
           no hook at 
             the specified end.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: Rebar) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetParameterValueAtIndex(self, paramId, barPositionIndex):
        """
        GetParameterValueAtIndex(self: Rebar, paramId: ElementId, barPositionIndex: int) -> ParameterValue
        
            Get the parameter value for a bar at the specified index.
           The parameter Id.
             
           The bar index in the rebar distribution. Accepts only values between 0 and 
             NumberOfBarPositions-1.
           The ParameterValue for given parameterId and 
             barPositionIndex.
           Throws exception if barPositionIndex is outside 
             boundaries.
        """
        pass

    def GetPresentationMode(self, dBView):
        """
        GetPresentationMode(self: Rebar, dBView: View) -> RebarPresentationMode
        
            Gets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            Returns: The presentation mode.
        """
        pass

    def GetRebarConstraintsManager(self):
        """
        GetRebarConstraintsManager(self: Rebar) -> RebarConstraintsManager
        
            Returns an object for managing the external constraints on the Rebar element
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: Rebar) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: Rebar, dBView: View) -> bool
        
            Identifies if this Rebar has overridden default presentation settings for the 
             given view.
        
        
            dBView: The view.
            Returns: True if this Rebar has overriden default presentation settings, false otherwise.
        """
        pass

    def HookAngleMatchesRebarShapeDefinition(self, iEnd, proposedHookId):
        """
        HookAngleMatchesRebarShapeDefinition(self: Rebar, iEnd: int, proposedHookId: ElementId) -> bool
        
            Checks that the hook angle of the specified RebarHookType matches the hook 
             angle used in the Rebar's RebarShape at the specified end of the bar.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            proposedHookId: The Id of the RebarHookType
            Returns: Returns true if the hook angle of the RebarHookType matches the angle used in 
             the RebarShape at the specified end of the bar.
        """
        pass

    def IsBarHidden(self, view, barIndex):
        """
        IsBarHidden(self: Rebar, view: View, barIndex: int) -> bool
        
            Identifies if a given bar in this rebar set is hidden in this view.
        
            view: The view.
            barIndex: The index of the bar from this rebar set.
            Returns: True if the bar is hidden in this view, false otherwise.
        """
        pass

    def IsRebarInSection(self, dBView):
        """
        IsRebarInSection(self: Rebar, dBView: View) -> bool
        
            Identifies if this Rebar is shown as a cross-section in the given view.
        
            dBView: The view.
            Returns: True if this Rebar is shown as a cross-section, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: Rebar, view: View3D) -> bool
        
            Checks if this rebar element is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if rebar is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: Rebar, view: View) -> bool
        
            Checks if this rebar element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    @staticmethod
    def RebarShapeMatchesCurvesAndHooks(rebarShape, barType, norm, curves, startHook, endHook, startHookOrient, endHookOrient):
        """ RebarShapeMatchesCurvesAndHooks(rebarShape: RebarShape, barType: RebarBarType, norm: XYZ, curves: IList[Curve], startHook: RebarHookType, endHook: RebarHookType, startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> bool """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def ScaleToBox(self, origin, xVec, yVec):
        """
        ScaleToBox(self: Rebar, origin: XYZ, xVec: XYZ, yVec: XYZ)
            Move and resize the bar to fit within a specified box.
           The arguments are 
             interpreted as an arbitrary
           rectangle in 3D with vertices: origin, 
             origin+xVec,
           origin+xVec+yVec, origin+yVec. The algorithm then
           proceeds 
             as follows. First the bar is given the
           default values of the shape 
             parameters from the shape
           definition. Then, if it is possible to do so 
             without
           violating the shape definition, the parameter values
           are scaled 
             so that the width and height of the shape
           (including bar thickness) match 
             the lengths of xVec and yVec.
           If there is no way to do this within the 
             shape definition
           due to overconstraining, a compromise is attempted, such 
             as
           scaling the whole shape until either the width or the
           height is 
             correct. Finally the shape is rotated to
           match the coordinate system of the 
             box. The algorithm
           is the same one used in one-click placement.
        
        
            origin: One corner of the rectangle.
            xVec: Vector representing the first edge of the rectangle. The length
           must be 
             positive.
        
            yVec: Vector representing the second edge of the rectangle. Must
           be perpendicular 
             to xVec.
        """
        pass

    def ScaleToBoxFor3D(self, origin, xVec, yVec, height):
        """
        ScaleToBoxFor3D(self: Rebar, origin: XYZ, xVec: XYZ, yVec: XYZ, height: float)
            Move and resize a spiral or multiplanar instance to fit within a specified box.
             
           The arguments are interpreted as an arbitrary rectangle in 3D with
           
             vertices: origin, origin+xVec, origin+xVec+yVec, origin+yVec. One end of the
          
              rebar shape is inscribed in this rectangle following the procedure described
         
               for the ScaleToBox method. The other end is placed in the parallel plane at
         
               distance (center-to-center) given by the height argument, in the
           
             direction of (xVec x yVec).
           Note that spiral shapes interpret the input 
             arguments using a different convention
           than multiplanar shapes.  For spiral 
             shapes, the spiral start will be placed in
           the rectangle defined by origin, 
             xVec, yVec, and the end of the spiral will be
           placed in the parallel plane. 
              For multiplanar shapes, the rebar is placed with
           its primary shape 
             definition located in the parallel plane defined by the height
           argument, 
             and its connector segments extending in the direction opposite (xVec x yVec).
         
               This method replaces ScaleToBoxForSpiral() from prior releases.
        
        
            origin: One corner of the rectangle.
            xVec: Vector representing the first edge of the rectangle. The length
           must be 
             positive.
        
            yVec: Vector representing the second edge of the rectangle. Must
           be perpendicular 
             to xVec.
        
            height: New value for the Height or MultiplanarDepth property.
        """
        pass

    def SetBarHiddenStatus(self, view, barIndex, hide):
        """
        SetBarHiddenStatus(self: Rebar, view: View, barIndex: int, hide: bool)
            Sets the bar in this rebar set to be hidden or unhidden in the given view.
        
            view: The view.
            barIndex: The index of the bar from this set.
            hide: True to hide this bar in the view, false to unhide the bar.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetHookOrientation(self, iEnd, hookOrientation):
        """
        SetHookOrientation(self: Rebar, iEnd: int, hookOrientation: RebarHookOrientation)
            Defines the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            hookOrientation: Only two values are permitted:
           Value = Right: The hook is on your right as 
             you stand at the end of the bar,
           with the bar behind you, taking the bar's 
             normal as "up."
           Value = Left: The hook is on your left as you stand at the 
             end of the bar,
           with the bar behind you, taking the bar's normal as "up."
        """
        pass

    def SetHookTypeId(self, end, hookTypeId):
        """
        SetHookTypeId(self: Rebar, end: int, hookTypeId: ElementId)
            Set the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            hookTypeId: The id of a RebarHookType element, or invalidElementId if
           the rebar should 
             have no hook at the specified end.
        """
        pass

    def SetHostId(self, doc, hostId):
        """
        SetHostId(self: Rebar, doc: Document, hostId: ElementId)
            The element that contains the rebar.
        
            doc: The document containing both this element and the host element.
            hostId: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column. The rebar does not need
           to be 
             strictly inside the host, but it must be assigned to one host
           element.
        """
        pass

    def SetLayoutAsFixedNumber(self, numberOfBarPositions, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsFixedNumber(self: Rebar, numberOfBarPositions: int, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to FixedNumber.
        
            numberOfBarPositions: The number of bar positions in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMaximumSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMaximumSpacing(self: Rebar, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MaximumSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMinimumClearSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMinimumClearSpacing(self: Rebar, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MinimumClearSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsNumberWithSpacing(self, numberOfBarPositions, spacing, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsNumberWithSpacing(self: Rebar, numberOfBarPositions: int, spacing: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to NumberWithSpacing
        
            numberOfBarPositions: The number of bar positions in rebar set
            spacing: The maximum spacing between rebar in rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsSingle(self):
        """
        SetLayoutAsSingle(self: Rebar)
            Sets the Layout Rule property of rebar set to Single.
        """
        pass

    def SetPresentationMode(self, dBView, presentationMode):
        """
        SetPresentationMode(self: Rebar, dBView: View, presentationMode: RebarPresentationMode)
            Sets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            presentationMode: The presentation mode.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: Rebar, view: View3D, solid: bool)
            Sets this rebar element to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if rebar is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: Rebar, view: View, unobscured: bool)
            Sets this rebar element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if rebar is shown unobscured, false otherwise.
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

    ArrayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the distribution path length of rebar set.

Get: ArrayLength(self: Rebar) -> float

Set: ArrayLength(self: Rebar) = value
"""

    BarsOnNormalSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.

Get: BarsOnNormalSide(self: Rebar) -> bool

Set: BarsOnNormalSide(self: Rebar) = value
"""

    BaseFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the lower end of the spiral.

Get: BaseFinishingTurns(self: Rebar) -> int

Set: BaseFinishingTurns(self: Rebar) = value
"""

    DistributionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of rebar distribution(also known as Rebar Set Type).

Get: DistributionType(self: Rebar) -> DistributionType

Set: DistributionType(self: Rebar) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the overall height.

Get: Height(self: Rebar) -> float

Set: Height(self: Rebar) = value
"""

    IncludeFirstBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the first bar in rebar set is shown.

Get: IncludeFirstBar(self: Rebar) -> bool

Set: IncludeFirstBar(self: Rebar) = value
"""

    IncludeLastBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the last bar in rebar set is shown.

Get: IncludeLastBar(self: Rebar) -> bool

Set: IncludeLastBar(self: Rebar) = value
"""

    LayoutRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the layout rule of rebar set.

Get: LayoutRule(self: Rebar) -> RebarLayoutRule

"""

    MaxSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the maximum spacing between rebar in rebar set.

Get: MaxSpacing(self: Rebar) -> float

Set: MaxSpacing(self: Rebar) = value
"""

    MultiplanarDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a multiplanar rebar, the depth of the instance.

Get: MultiplanarDepth(self: Rebar) -> float

Set: MultiplanarDepth(self: Rebar) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unit-length vector normal to the plane of the rebar

Get: Normal(self: Rebar) -> XYZ

"""

    NumberOfBarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of potential bars in the set.

Get: NumberOfBarPositions(self: Rebar) -> int

Set: NumberOfBarPositions(self: Rebar) = value
"""

    Pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the pitch, or vertical distance traveled in one rotation.

Get: Pitch(self: Rebar) -> float

Set: Pitch(self: Rebar) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the number of bars in rebar set.

Get: Quantity(self: Rebar) -> int

"""

    RebarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the rebar.

Get: RebarShapeId(self: Rebar) -> ElementId

Set: RebarShapeId(self: Rebar) = value
"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: Rebar) -> str

Set: ScheduleMark(self: Rebar) = value
"""

    TopFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the upper end of the spiral.

Get: TopFinishingTurns(self: Rebar) -> int

Set: TopFinishingTurns(self: Rebar) = value
"""

    TotalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of an individual bar multiplied by Quantity.

Get: TotalLength(self: Rebar) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of an individual bar multiplied by Quantity.

Get: Volume(self: Rebar) -> float

"""



class RebarBarType(ElementType, IDisposable):
    """ A Rebar type object that is used in the generation of Rebar """
    @staticmethod
    def Create(ADoc):
        """
        Create(ADoc: Document) -> RebarBarType
        
            Creates a new RebarBarType object
        """
        pass

    @staticmethod
    def CreateDefaultRebarBarType(ADoc):
        """
        CreateDefaultRebarBarType(ADoc: Document) -> ElementId
        
            Creates a new RebarBarType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAutoCalcHookLengths(self, hookId):
        """
        GetAutoCalcHookLengths(self: RebarBarType, hookId: ElementId) -> bool
        
            Identifies if the hook lengths of a hook type are automatically calculated for 
             this bar type
        
        
            hookId: id of the hook type
            Returns: True if the hook lengths are automatically calculated, otherwise false
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHookLength(self, hookId):
        """
        GetHookLength(self: RebarBarType, hookId: ElementId) -> float
        
            Identifies the hook length for a hook type
        
            hookId: id of the hook type
            Returns: The hook length for a hook type
        """
        pass

    def GetHookOffsetLength(self, hookId):
        """
        GetHookOffsetLength(self: RebarBarType, hookId: ElementId) -> float
        
            Identifies the hook offset length for a hook type
        
            hookId: id of the hook type
            Returns: The hook offset length for a hook type
        """
        pass

    def GetHookPermission(self, hookId):
        """
        GetHookPermission(self: RebarBarType, hookId: ElementId) -> bool
        
            Identifies if a hook type is permitted for this bar type
        
            hookId: id of the hook type
            Returns: True if the hook type is permitted for this bar type, otherwise false
        """
        pass

    def GetHookTangentLength(self, hookId):
        """
        GetHookTangentLength(self: RebarBarType, hookId: ElementId) -> float
        
            Identifies the hook tangent length for a hook type
        
            hookId: id of the hook type
            Returns: The hook tangent length for a hook type
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: RebarBarType) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetAutoCalcHookLengths(self, hookId, autoCalculated):
        """
        SetAutoCalcHookLengths(self: RebarBarType, hookId: ElementId, autoCalculated: bool)
            Identifies if the hook lengths of a hook type are automatically calculated for 
             this bar type
        
        
            hookId: id of the hook type
            autoCalculated: True if the hook lengths should be automatically calculated, otherwise false
          
              When it is false, default hook length and default hook offset length will be 
             reported
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetHookLength(self, hookId, hookLength):
        """
        SetHookLength(self: RebarBarType, hookId: ElementId, hookLength: float)
            Identifies the hook length for a hook type
        
            hookId: id of the hook type
            hookLength: The hook length for a hook type
        """
        pass

    def SetHookOffsetLength(self, hookId, newLength):
        """
        SetHookOffsetLength(self: RebarBarType, hookId: ElementId, newLength: float)
            Identifies the hook offset length for a hook type
        
            hookId: id of the hook type
            newLength: The hook offset length for a hook type
        """
        pass

    def SetHookPermission(self, hookId, permission):
        """
        SetHookPermission(self: RebarBarType, hookId: ElementId, permission: bool)
            Identifies if a hook type is permitted for this bar type
        
            hookId: id of the hook type
            permission: True if the hook type should be permitted for this bar type, otherwise false
        """
        pass

    def SetHookTangentLength(self, hookId, newLength):
        """
        SetHookTangentLength(self: RebarBarType, hookId: ElementId, newLength: float)
            Identifies the hook tangent length for a hook type
        
            hookId: id of the hook type
            newLength: The hook tangent length for a hook type
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

    BarDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines bar diameter of rebar

Get: BarDiameter(self: RebarBarType) -> float

Set: BarDiameter(self: RebarBarType) = value
"""

    DeformationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines bar deformation type.

Get: DeformationType(self: RebarBarType) -> RebarDeformationType

Set: DeformationType(self: RebarBarType) = value
"""

    MaximumBendRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines maximum bend radius of rebar

Get: MaximumBendRadius(self: RebarBarType) -> float

Set: MaximumBendRadius(self: RebarBarType) = value
"""

    StandardBendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines bar bend diameter for rebar whose style is standard

Get: StandardBendDiameter(self: RebarBarType) -> float

Set: StandardBendDiameter(self: RebarBarType) = value
"""

    StandardHookBendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines hook bend diameter for rebar whose style is standard

Get: StandardHookBendDiameter(self: RebarBarType) -> float

Set: StandardHookBendDiameter(self: RebarBarType) = value
"""

    StirrupTieBendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines bar and hook bend diameter for rebar whose style is stirrup/tie

Get: StirrupTieBendDiameter(self: RebarBarType) -> float

Set: StirrupTieBendDiameter(self: RebarBarType) = value
"""



class RebarBendData(object, IDisposable):
    """
    The values in this class provide a summary of information taken from the RebarBarType, RebarHookType, and RebarStyle.
    
    RebarBendData(barType: RebarBarType, hookType0: RebarHookType, hookType1: RebarHookType, style: RebarStyle, hookOrient0: RebarHookOrientation, hookOrient1: RebarHookOrientation)
    RebarBendData()
    """
    def Dispose(self):
        """ Dispose(self: RebarBendData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarBendData, disposing: bool) """
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
    def __new__(self, barType=None, hookType0=None, hookType1=None, style=None, hookOrient0=None, hookOrient1=None):
        """
        __new__(cls: type, barType: RebarBarType, hookType0: RebarHookType, hookType1: RebarHookType, style: RebarStyle, hookOrient0: RebarHookOrientation, hookOrient1: RebarHookOrientation)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BarDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The diameter of the bar.

Get: BarDiameter(self: RebarBendData) -> float

Set: BarDiameter(self: RebarBendData) = value
"""

    BendRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of all fillets, except hook fillets, in the Rebar shape.

Get: BendRadius(self: RebarBendData) -> float

Set: BendRadius(self: RebarBendData) = value
"""

    HookAngle0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle of the hook at the start.

Get: HookAngle0(self: RebarBendData) -> int

Set: HookAngle0(self: RebarBendData) = value
"""

    HookAngle1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle of the hook at the end.

Get: HookAngle1(self: RebarBendData) -> int

Set: HookAngle1(self: RebarBendData) = value
"""

    HookBendRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the hook fillets in the Rebar shape.

Get: HookBendRadius(self: RebarBendData) -> float

Set: HookBendRadius(self: RebarBendData) = value
"""

    HookLength0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension length of the hook at the start.

Get: HookLength0(self: RebarBendData) -> float

Set: HookLength0(self: RebarBendData) = value
"""

    HookLength1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The extension length of the hook at the end.

Get: HookLength1(self: RebarBendData) -> float

Set: HookLength1(self: RebarBendData) = value
"""

    HookOrient0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The orientation of the hook at the start.

Get: HookOrient0(self: RebarBendData) -> RebarHookOrientation

Set: HookOrient0(self: RebarBendData) = value
"""

    HookOrient1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The orientation of the hook at the end.

Get: HookOrient1(self: RebarBendData) -> RebarHookOrientation

Set: HookOrient1(self: RebarBendData) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarBendData) -> bool

"""



class RebarConstrainedHandle(object, IDisposable):
    """
    A class representing a handle on a Rebar that can be joined to a reference, such
       as a host Element's surface or cover, or another Rebar's handle.
    """
    def Dispose(self):
        """ Dispose(self: RebarConstrainedHandle) """
        pass

    def GetEdgeNumber(self):
        """
        GetEdgeNumber(self: RebarConstrainedHandle) -> int
        
            If the RebarConstrainedHandle's RebarHandleType is 'Edge,'
           then this 
             function will return the number of the edge that is
           driven by the handle.
        """
        pass

    def GetHandleType(self):
        """
        GetHandleType(self: RebarConstrainedHandle) -> RebarHandleType
        
            Returns the RebarHandleType of a RebarConstrainedHandle.
            Returns: The RebarHandleType of the specified RebarConstrainedHandle.
        """
        pass

    def IsEdgeHandle(self):
        """
        IsEdgeHandle(self: RebarConstrainedHandle) -> bool
        
            Returns true if the RebarHandleType of the RebarConstrainedHandle is 'Edge.'
        """
        pass

    def IsValid(self):
        """
        IsValid(self: RebarConstrainedHandle) -> bool
        
            Checks that the RebarConstrainedHandle still has access to valid Rebar handle 
             data
           and that its RebarConstraintsManager is still valid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarConstrainedHandle, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarConstrainedHandle) -> bool

"""



class RebarConstraint(object, IDisposable):
    """ A class representing a constraint on a handle of a rebar element. """
    def Dispose(self):
        """ Dispose(self: RebarConstraint) """
        pass

    def GetConstraintType(self):
        """
        GetConstraintType(self: RebarConstraint) -> RebarConstraintType
        
            Returns the RebarConstraintType of a RebarConstraint.
            Returns: The RebarConstraintType of the specified RebarConstraint.
        """
        pass

    def GetDistanceToTargetCover(self):
        """
        GetDistanceToTargetCover(self: RebarConstraint) -> float
        
            Returns the distance from the RebarConstrainedHandle to the target Host Cover 
             Element surface.
           The RebarConstraintType of the RebarConstraint must be 
             'ToCover.'
        """
        pass

    def GetDistanceToTargetHostFace(self):
        """
        GetDistanceToTargetHostFace(self: RebarConstraint) -> float
        
            Returns the distance from the RebarConstrainedHandle to the target Host Element 
             surface.
           The RebarConstraintType of the RebarConstraint must be 
             'FixedDistanceToHostFace.'
        """
        pass

    def GetRebarConstraintTargetHostFaceType(self):
        """
        GetRebarConstraintTargetHostFaceType(self: RebarConstraint) -> RebarConstraintTargetHostFaceType
        
            Returns the RebarConstraintTargetHostFaceType of the host Element face to which
             
           the RebarConstraint is attached.  The RebarConstraintType of the 
             RebarConstraint
           must be 'FixedDistanceToHostFace' or 'ToCover.'
        """
        pass

    def GetTargetElement(self):
        """
        GetTargetElement(self: RebarConstraint) -> Element
        
            Returns the Element object (either Host or Rebar) which provides the constraint.
        """
        pass

    def GetTargetHostFaceReference(self):
        """
        GetTargetHostFaceReference(self: RebarConstraint) -> Reference
        
            Returns a reference to the host Element face to which the RebarConstraint is 
             attached.
           The RebarConstraintType of the RebarConstraint must be 
             'FixedDistanceToHostFace' or 'ToCover.'
        
            Returns: Requested reference.
        """
        pass

    def GetTargetRebarAngleOnBarOrHookBend(self):
        """
        GetTargetRebarAngleOnBarOrHookBend(self: RebarConstraint) -> int
        
            Returns the angular increment along a bar or hook bend to which the 
             RebarConstraint is attached.
        
            Returns: The angular increment relative to the reference bar edge.
        """
        pass

    def GetTargetRebarBendNumber(self):
        """
        GetTargetRebarBendNumber(self: RebarConstraint) -> int
        
            Returns the number of the bend on the other Rebar Element to which this 
             RebarConstraint is attached.
           The RebarConstraint must be of 
             RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
           must 
             be 'BarBend.'
        """
        pass

    def GetTargetRebarConstraintType(self):
        """
        GetTargetRebarConstraintType(self: RebarConstraint) -> TargetRebarConstraintType
        
            Returns the TargetRebarConstraintType of the handle on the other Rebar Element
        
                to which this RebarConstraint is attached. The RebarConstraintType of the
          
              RebarConstraint must be 'ToOtherRebar.'
        """
        pass

    def GetTargetRebarEdgeNumber(self):
        """
        GetTargetRebarEdgeNumber(self: RebarConstraint) -> int
        
            Returns the number of the edge on the other Rebar Element to which this 
             RebarConstraint is attached.
           The RebarConstraint must be of 
             RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
           must 
             be 'Edge.'
        """
        pass

    def GetTargetRebarHookBarEnd(self):
        """
        GetTargetRebarHookBarEnd(self: RebarConstraint) -> int
        
            Returns 0 or 1 to indicate which end hook on the other Rebar Element to which 
             this RebarConstraint is attached.
           The RebarConstraint must be of 
             RebarConstraintType 'ToOtherRebar,' and the TargetRebarConstraintType
           must 
             be 'HookBend.'
        """
        pass

    def HasAnEdgeNumber(self):
        """
        HasAnEdgeNumber(self: RebarConstraint) -> bool
        
            Checks if the getTargetRebarEdgeNumber method can be called for the 
             RebarConstraint.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: RebarConstraint, other: RebarConstraint) -> bool
        
            Returns true if the specified RebarConstraint is the same as 'this.'  The 
             method
           can be used to determine which of the RebarConstraint candidates 
             offered by the
           RebarConstraintsManager is currently active.
        """
        pass

    def IsFixedDistanceToHostFace(self):
        """
        IsFixedDistanceToHostFace(self: RebarConstraint) -> bool
        
            Returns true if the RebarConstraintType of the RebarConstraint is 
             'FixedDistanceToHostFace.'
        """
        pass

    def IsToCover(self):
        """
        IsToCover(self: RebarConstraint) -> bool
        
            Returns true if the RebarConstraintType of the RebarConstraint is 'ToCover.'
        """
        pass

    def IsToHostFaceOrCover(self):
        """
        IsToHostFaceOrCover(self: RebarConstraint) -> bool
        
            Returns true if the RebarConstraintType of the RebarConstraint is either 
             'FixedDistanceToHostFace' or 'ToCover.'
        """
        pass

    def IsToOtherRebar(self):
        """
        IsToOtherRebar(self: RebarConstraint) -> bool
        
            Returns true if the RebarConstraintType of the RebarConstraint is 
             'ToOtherRebar.'
        """
        pass

    def IsValid(self):
        """
        IsValid(self: RebarConstraint) -> bool
        
            Checks that the RebarConstraint still has access to valid Rebar constraint data
             
           and that its RebarConstraintsManager is still valid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarConstraint, disposing: bool) """
        pass

    def SetDistanceToTargetCover(self, distanceToTargetCover):
        """
        SetDistanceToTargetCover(self: RebarConstraint, distanceToTargetCover: float)
            Sets the distance from the RebarConstrainedHandle to the target Host Cover 
             Element surface.
           The RebarConstraintType of the RebarConstraint must be 
             'ToCover.'
        
        
            distanceToTargetCover: The distance is given as an offset value, the sign of which depends on Host 
             Cover direction.
        """
        pass

    def SetDistanceToTargetHostFace(self, offset):
        """
        SetDistanceToTargetHostFace(self: RebarConstraint, offset: float)
            Sets the distance from the RebarConstrainedHandle to the target Host Element 
             surface.
           The RebarConstraintType of the RebarConstraint must be 
             'FixedDistanceToHostFace.'
        
        
            offset: The distance is given as an offset value, the sign of which depends on Host 
             Face direction.
        """
        pass

    def TargetIsBarBend(self):
        """
        TargetIsBarBend(self: RebarConstraint) -> bool
        
            Returns true if the RebarTargetConstraintType of the RebarConstraint is 
             'BarBend'
        """
        pass

    def TargetIsHookBend(self):
        """
        TargetIsHookBend(self: RebarConstraint) -> bool
        
            Returns true if the RebarTargetConstraintType of the RebarConstraint is 
             'HookBend'
        """
        pass

    def TargetRebarConstraintTypeIsEdge(self):
        """
        TargetRebarConstraintTypeIsEdge(self: RebarConstraint) -> bool
        
            Returns true if the RebarConstraintType of the RebarConstraint is 
             'ToOtherRebar,'
           and the RebarConstraint is attached to an edge of the other 
             Rebar Element.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarConstraint) -> bool

"""



class RebarConstraintsManager(object, IDisposable):
    """
    A class used to obtain information about the constraints (RebarConstraints) acting
       on the shape handles (RebarConstrainedHandles) of a Rebar element, and to replace
       default constraints with user-preferred choices.
    """
    def ClearHandleConstraintPairHighlighting(self, aDoc):
        """
        ClearHandleConstraintPairHighlighting(self: RebarConstraintsManager, aDoc: Document)
            Clears all highlighting in all views.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarConstraintsManager) """
        pass

    def GetAllConstrainedHandles(self):
        """
        GetAllConstrainedHandles(self: RebarConstraintsManager) -> IList[RebarConstrainedHandle]
        
            Retrieves all handles on the Rebar that are constrained to external references.
            Returns: A collection of RebarConstrainedHandles
        """
        pass

    def GetConstraintCandidatesForHandle(self, handle):
        """
        GetConstraintCandidatesForHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> IList[RebarConstraint]
        
            Returns all possible RebarConstraints that could be used for a specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which constraint candidates are sought.
            Returns: A collection of RebarConstraints
        """
        pass

    def GetCurrentConstraintOnHandle(self, handle):
        """
        GetCurrentConstraintOnHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> RebarConstraint
        
            Retrieves the RebarConstraint that acts on the specified RebarConstraintHandle.
        """
        pass

    def GetPreferredConstraintOnHandle(self, handle):
        """
        GetPreferredConstraintOnHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> RebarConstraint
        
            Returns the RebarConstraint that has been set as preferred for the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which the user RebarConstraint is to be returned.
            Returns: The user prefered RebarConstraint applied to the RebarConstrainedHandle.
        """
        pass

    def HasValidRebar(self):
        """
        HasValidRebar(self: RebarConstraintsManager) -> bool
        
            Checks whether the Manager's Rebar is still valid.
        """
        pass

    def HighlightHandleConstraintPairInAllViews(self, aDoc, handle, constraint):
        """
        HighlightHandleConstraintPairInAllViews(self: RebarConstraintsManager, aDoc: Document, handle: RebarConstrainedHandle, constraint: RebarConstraint)
            Highlights the specified RebarConstrainedHandle and RebarConstraint in all 
             views.
        
        
            handle: The RebarConstrainedHandle to be highlighted in all views.
            constraint: The RebarConstraint to be highlighted in all views.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarConstraintsManager, disposing: bool) """
        pass

    def RemovePreferredConstraintFromHandle(self, handle):
        """
        RemovePreferredConstraintFromHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle)
            Clears the user-preferred RebarConstraint from the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which the user RebarConstraint is to be deleted.
        """
        pass

    def SetPreferredConstraintForHandle(self, handle, constraint):
        """
        SetPreferredConstraintForHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle, constraint: RebarConstraint)
            Sets the RebarConstraint as preferred constraint target for the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle to which the new RebarConstraint is to be applied.
            constraint: The new RebarConstraint to be applied to the RebarConstrainedHandle.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarConstraintsManager) -> bool

"""


    IsRebarConstrainedPlacementEnabled = False


class RebarConstraintTargetHostFaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    A type to help identify the individual face on a host element to which a Rebar handle
       is constrained.
    
    enum RebarConstraintTargetHostFaceType, values: Bottom (2), End0 (3), End1 (4), FaceWithTagId (0), Side0 (5), Side1 (6), Top (1)
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

    Bottom = None
    End0 = None
    End1 = None
    FaceWithTagId = None
    Side0 = None
    Side1 = None
    Top = None
    value__ = None


class RebarConstraintType(Enum, IComparable, IFormattable, IConvertible):
    """
    The various types of constraints that can be applied to a RebarConstrainedHandle.
    
    enum RebarConstraintType, values: FixedDistanceToHostFace (0), ToCover (1), ToOtherRebar (2)
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

    FixedDistanceToHostFace = None
    ToCover = None
    ToOtherRebar = None
    value__ = None


class RebarContainer(Element, IDisposable, IEnumerable[RebarContainerItem], IEnumerable):
    """ An object that represents an Rebar Container Element within the Autodesk Revit project. """
    def AppendItemFromCurves(self, style, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape):
        """ AppendItemFromCurves(self: RebarContainer, style: RebarStyle, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, normal: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation, useExistingShapeIfPossible: bool, createNewShape: bool) -> RebarContainerItem """
        pass

    def AppendItemFromCurvesAndShape(self, rebarShape, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient):
        """ AppendItemFromCurvesAndShape(self: RebarContainer, rebarShape: RebarShape, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, normal: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> RebarContainerItem """
        pass

    def AppendItemFromRebar(self, rebar):
        """
        AppendItemFromRebar(self: RebarContainer, rebar: Rebar) -> RebarContainerItem
        
            Appends an Item to the RebarContainer. Fills its data on base of the Rebar.
        
            rebar: The Rebar.
            Returns: The Rebar Container Item.
        """
        pass

    def AppendItemFromRebarShape(self, rebarShape, barType, origin, xVector, yVector):
        """
        AppendItemFromRebarShape(self: RebarContainer, rebarShape: RebarShape, barType: RebarBarType, origin: XYZ, xVector: XYZ, yVector: XYZ) -> RebarContainerItem
        
            Appends an Item to the RebarContainer. Fills its data on base of the Rebar.
        
            rebarShape: A RebarShape element that defines the shape of the rebar.
            barType: A RebarBarType element that defines bar diameter, bend radius and material of 
             the rebar.
        
            origin: The lower-left corner of the shape's bounding box will be placed at this point 
             in the project.
        
            xVector: The x-axis in the shape definition will be mapped to this direction in the 
             project.
        
            yVector: The y-axis in the shape definition will be mapped to this direction in the 
             project.
        
            Returns: The Rebar Container Item.
        """
        pass

    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: RebarContainer, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this RebarContainer in the 
             given view.
        
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if presentation mode can be applied for this view, false otherwise.
        """
        pass

    def ClearItems(self):
        """
        ClearItems(self: RebarContainer)
            Clears all the Items stored in this Rebar Container element.
        """
        pass

    def Contains(self, pItem):
        """
        Contains(self: RebarContainer, pItem: RebarContainerItem) -> bool
        
            Checks if the RebarContainer has this item as one of its members.
        
            pItem: The item to be checked if RebarContainer has it as one of its members
            Returns: True if RebarContainer has this item as one of its members, false otherwise.
        """
        pass

    @staticmethod
    def Create(aDoc, hostElement, rebarContainerTypeId):
        """
        Create(aDoc: Document, hostElement: Element, rebarContainerTypeId: ElementId) -> RebarContainer
        
            Creates a new instance of a Rebar Container element within the project.
        
            aDoc: A document.
            hostElement: The element that will host the RebarContainer.
            rebarContainerTypeId: The id of the RebarContainerType.
            Returns: The newly created Rebar Container instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: RebarContainer) -> IEnumerator[RebarContainerItem]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: RebarContainer) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetItem(self, itemIndex):
        """
        GetItem(self: RebarContainer, itemIndex: int) -> RebarContainerItem
        
            Gets the item stored in the RebarContainer at the associated index.
        
            itemIndex: Item index in the Rebar Container
            Returns: Rebar Container Item
        """
        pass

    def GetParametersManager(self):
        """
        GetParametersManager(self: RebarContainer) -> RebarContainerParameterManager
        
            Returns an object used to manage parameters of the Rebar Container.
            Returns: The parameters manager.
        """
        pass

    def GetRebarContainerIterator(self):
        """
        GetRebarContainerIterator(self: RebarContainer) -> RebarContainerIterator
        
            Returns a Rebar Container Iterator that iterates through the Rebar Container 
             Items.
        
            Returns: A Rebar Container Iterator object that can be used to iterate through Rebar 
             Container Items in the collection.
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: RebarContainer) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: RebarContainer, dBView: View) -> bool
        
            Identifies if any RebarContainerItem of this RebarContainer has overridden 
             default presentation settings for the given view.
        
        
            dBView: The view.
            Returns: True if if any RebarContainerItem of this RebarContainer has overridden default 
             presentation settings, false otherwise.
        """
        pass

    def IsItemHidden(self, view, itemIndex):
        """
        IsItemHidden(self: RebarContainer, view: View, itemIndex: int) -> bool
        
            Identifies if a given RebarContainerItem is hidden in this view.
        
            view: The view.
            itemIndex: Item index in the Rebar Container.
            Returns: True if the RebarContainerItem is hidden in this view, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: RebarContainer, view: View3D) -> bool
        
            Checks if this RebarContainer element is shown as solid in the given 3D view.
        
            view: The 3D view element
            Returns: True this RebarContainer element is shown as solid in the given 3D view, false 
             otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: RebarContainer, view: View) -> bool
        
            Checks if this rebar container element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveItem(self, pItem):
        """
        RemoveItem(self: RebarContainer, pItem: RebarContainerItem)
            Removes Item from the Rebar Container.
        
            pItem: Item to be removed from this Rebar Container
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetHostId(self, doc, hostId):
        """
        SetHostId(self: RebarContainer, doc: Document, hostId: ElementId)
            The element that contains the rebar.
        
            doc: The document containing both this element and the host element.
            hostId: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column. The rebar does not need
           to be 
             strictly inside the host, but it must be assigned to one host
           element.
        """
        pass

    def SetItemHiddenStatus(self, view, itemIndex, hide):
        """
        SetItemHiddenStatus(self: RebarContainer, view: View, itemIndex: int, hide: bool)
            Sets the RebarContainerItem to be hidden or unhidden in the given view.
        
            view: The view.
            itemIndex: Item index in the Rebar Container.
            hide: True to hide this RebarContainerItem in the view, false to unhide the item.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: RebarContainer, view: View3D, solid: bool)
            Sets this RebarContainer element is shown as solid in the given 3D view.
        
            view: The 3D view element
            solid: True if this RebarContainer element is shown as solid in the given 3D view, 
             false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: RebarContainer, view: View, unobscured: bool)
            Sets this rebar container element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RebarContainerItem](enumerable: IEnumerable[RebarContainerItem], value: RebarContainerItem) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    ItemsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The count of Items in this Rebar Container.

Get: ItemsCount(self: RebarContainer) -> int

"""

    PresentItemsAsSubelements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if Items should be presented in schedules and tags as separate subelements.

Get: PresentItemsAsSubelements(self: RebarContainer) -> bool

Set: PresentItemsAsSubelements(self: RebarContainer) = value
"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: RebarContainer) -> str

Set: ScheduleMark(self: RebarContainer) = value
"""



class RebarContainerItem(object, IDisposable):
    """ Provides implementation for Rebar stored in RebarContainer. """
    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: RebarContainerItem, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this rebar in the given view.
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if presentation mode can be applied for this view, false otherwise.
        """
        pass

    def CanUseHookType(self, proposedHookId):
        """
        CanUseHookType(self: RebarContainerItem, proposedHookId: ElementId) -> bool
        
            Checks if the specified RebarHookType id is of a valid RebarHookType for the 
             Rebar's RebarBarType
        
        
            proposedHookId: The Id of the RebarHookType
            Returns: Returns true if the id is of a valid RebarHookType for the Rebar element.
        """
        pass

    def ClearPresentationMode(self, dBView):
        """
        ClearPresentationMode(self: RebarContainerItem, dBView: View)
            Sets the presentation mode for this rebar set to the default (either for a 
             single view, or for all views).
        
        
            dBView: The view where the presentation mode will be cleared. NULL for all views
        """
        pass

    def ComputeDrivingCurves(self):
        """
        ComputeDrivingCurves(self: RebarContainerItem) -> IList[Curve]
        
            Compute the driving curves.
            Returns: Returns an empty array if an error is encountered.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarContainerItem) """
        pass

    def DoesBarExistAtPosition(self, barPosition):
        """
        DoesBarExistAtPosition(self: RebarContainerItem, barPosition: int) -> bool
        
            Checks whether a bar exists at the specified position.
        
            barPosition: A bar position index between 0 and NumberOfBarPositions-1.
        """
        pass

    def FindMatchingPredefinedPresentationMode(self, dBView):
        """
        FindMatchingPredefinedPresentationMode(self: RebarContainerItem, dBView: View) -> RebarPresentationMode
        
            Determines if there is a matching RebarPresentationMode for the current set of 
             selected hidden and unhidden bars assigned to the given view.
        
        
            dBView: The view.
            Returns: The presentation mode that matches the current set of selected hidden and 
             unhidden bars.
           If there is no better match, this returns 
             RebarPresentationMode.Select.
        """
        pass

    def GetBarPositionTransform(self, barPositionIndex):
        """
        GetBarPositionTransform(self: RebarContainerItem, barPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of any
           individual bar 
             in the set.
        
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
            Returns: The position of a bar in the set relative to the first position.
        """
        pass

    def GetBendData(self):
        """
        GetBendData(self: RebarContainerItem) -> RebarBendData
        
            Gets the RebarBendData, containing bar and hook information, of the instance.
        """
        pass

    def GetCenterlineCurves(self, adjustForSelfIntersection, suppressHooks, suppressBendRadius, multiplanarOption=None):
        """
        GetCenterlineCurves(self: RebarContainerItem, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        
        GetCenterlineCurves(self: RebarContainerItem, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool, multiplanarOption: MultiplanarOption) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            multiplanarOption: If the Rebar is a multi-planar shape, this parameter controls whether to 
             generate only
           the curves in the primary plane (IncludeOnlyPlanarCurves), or 
             to generate all curves,
           (IncludeAllMultiplanarCurves) including the 
             out-of-plane connector segments as well as
           multi-planar copies of the 
             primary plane curves.
           This argument is ignored for planar shapes.
        
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        """
        pass

    def GetDistributionPath(self):
        """
        GetDistributionPath(self: RebarContainerItem) -> Line
        
            The distribution path of a rebar set.
            Returns: A line beginning at (0, 0, 0) and representing the direction and
           length of 
             the set.
        """
        pass

    def GetHookOrientation(self, iEnd):
        """
        GetHookOrientation(self: RebarContainerItem, iEnd: int) -> RebarHookOrientation
        
            Returns the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            Returns: Value = Right: The hook is on your right as you stand at the end of the bar,
          
              with the bar behind you, taking the bar's normal as "up."
           Value = Left: 
             The hook is on your left as you stand at the end of the bar,
           with the bar 
             behind you, taking the bar's normal as "up."
        """
        pass

    def GetHookTypeId(self, end):
        """
        GetHookTypeId(self: RebarContainerItem, end: int) -> ElementId
        
            Get the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            Returns: The id of a RebarHookType, or invalidElementId if the rebar has
           no hook at 
             the specified end.
        """
        pass

    def GetPresentationMode(self, dBView):
        """
        GetPresentationMode(self: RebarContainerItem, dBView: View) -> RebarPresentationMode
        
            Gets the presentaion mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            Returns: The presentation mode.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: RebarContainerItem, dBView: View) -> bool
        
            Identifies if this rebar set has overridden default presentation settings for 
             the given view.
        
        
            dBView: The view.
            Returns: True if this rebar set has overriden default presentation settings, false 
             otherwise.
        """
        pass

    def IsBarHidden(self, view, barIndex):
        """
        IsBarHidden(self: RebarContainerItem, view: View, barIndex: int) -> bool
        
            Identifies if a given bar in this rebar set is hidden in this view.
        
            view: The view.
            barIndex: The index of the bar from this rebar set.
            Returns: True if the bar is hidden in this view, false otherwise.
        """
        pass

    def IsRebarInSection(self, dBView):
        """
        IsRebarInSection(self: RebarContainerItem, dBView: View) -> bool
        
            Identifies if this rebar set is shown as a cross-section in the given view.
        
            dBView: The view.
            Returns: True if this rebar set is shown as a cross-section, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarContainerItem, disposing: bool) """
        pass

    def SetBarHiddenStatus(self, view, barIndex, hide):
        """
        SetBarHiddenStatus(self: RebarContainerItem, view: View, barIndex: int, hide: bool)
            Sets the bar in this rebar set to be hidden or unhidden in the given view.
        
            view: The view.
            barIndex: The index of the bar from this set.
            hide: True to hide this bar in the view, false to unhide the bar.
        """
        pass

    def SetFromCurves(self, style, barType, startHook, endHook, norm, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape):
        """ SetFromCurves(self: RebarContainerItem, style: RebarStyle, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation, useExistingShapeIfPossible: bool, createNewShape: bool) """
        pass

    def SetFromCurvesAndShape(self, rebarShape, barType, startHook, endHook, norm, curves, startHookOrient, endHookOrient):
        """ SetFromCurvesAndShape(self: RebarContainerItem, rebarShape: RebarShape, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, norm: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) """
        pass

    def SetFromRebar(self, rebar):
        """
        SetFromRebar(self: RebarContainerItem, rebar: Rebar)
            Set an instance of a RebarContainerItem element according to a Rebar parameters.
        
            rebar: The Rebar.
        """
        pass

    def SetFromRebarShape(self, rebarShape, barType, origin, xVec, yVec):
        """
        SetFromRebarShape(self: RebarContainerItem, rebarShape: RebarShape, barType: RebarBarType, origin: XYZ, xVec: XYZ, yVec: XYZ)
            Set an instance of a RebarContainerItem element, as an instance of a 
             RebarShape.
           The instance will have the default shape parameters from the 
             RebarShape,
           and its location is based on the bounding box of the shape in 
             the shape definition.
           Hooks are removed from the shape before computing its 
             bounding box.
           If appropriate hooks can be found in the document, they will 
             be assigned arbitrarily.
        
        
            rebarShape: A RebarShape element that defines the shape of the rebar.
            barType: A RebarBarType element that defines bar diameter, bend radius and material of 
             the rebar.
        
            origin: The lower-left corner of the shape's bounding box will be placed at this point 
             in the project.
        
            xVec: The x-axis in the shape definition will be mapped to this direction in the 
             project.
        
            yVec: The y-axis in the shape definition will be mapped to this direction in the 
             project.
        """
        pass

    def SetHookOrientation(self, iEnd, hookOrientation):
        """
        SetHookOrientation(self: RebarContainerItem, iEnd: int, hookOrientation: RebarHookOrientation)
            Defines the orientation of the hook plane at the start or at the end of the 
             rebar with respect to the orientation of the first or the last curve and the 
             plane normal.
        
        
            iEnd: 0 for the start hook, 1 for the end hook.
            hookOrientation: Only two values are permitted:
           Value = Right: The hook is on your right as 
             you stand at the end of the bar,
           with the bar behind you, taking the bar's 
             normal as "up."
           Value = Left: The hook is on your left as you stand at the 
             end of the bar,
           with the bar behind you, taking the bar's normal as "up."
        """
        pass

    def SetHookTypeId(self, end, hookTypeId):
        """
        SetHookTypeId(self: RebarContainerItem, end: int, hookTypeId: ElementId)
            Set the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            hookTypeId: The id of a RebarHookType element, or invalidElementId if
           the rebar should 
             have no hook at the specified end.
        """
        pass

    def SetLayoutAsFixedNumber(self, numberOfBarPositions, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsFixedNumber(self: RebarContainerItem, numberOfBarPositions: int, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to FixedNumber.
        
            numberOfBarPositions: The number of bar positions in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMaximumSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMaximumSpacing(self: RebarContainerItem, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MaximumSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsMinimumClearSpacing(self, spacing, arrayLength, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsMinimumClearSpacing(self: RebarContainerItem, spacing: float, arrayLength: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to MinimumClearSpacing
        
            spacing: The maximum spacing between rebar in rebar set
            arrayLength: The distribution length of rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsNumberWithSpacing(self, numberOfBarPositions, spacing, barsOnNormalSide, includeFirstBar, includeLastBar):
        """
        SetLayoutAsNumberWithSpacing(self: RebarContainerItem, numberOfBarPositions: int, spacing: float, barsOnNormalSide: bool, includeFirstBar: bool, includeLastBar: bool)
            Sets the Layout Rule property of rebar set to NumberWithSpacing
        
            numberOfBarPositions: The number of bar positions in rebar set
            spacing: The maximum spacing between rebar in rebar set
            barsOnNormalSide: Identifies if the bars of the rebar set are on the same side of the rebar plane 
             indicated by the normal
        
            includeFirstBar: Identifies if the first bar in rebar set is shown
            includeLastBar: Identifies if the last bar in rebar set is shown
        """
        pass

    def SetLayoutAsSingle(self):
        """
        SetLayoutAsSingle(self: RebarContainerItem)
            Sets the Layout Rule property of rebar set to Single.
        """
        pass

    def SetPresentationMode(self, dBView, presentationMode):
        """
        SetPresentationMode(self: RebarContainerItem, dBView: View, presentationMode: RebarPresentationMode)
            Sets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            presentationMode: The presentation mode.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ArrayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the distribution path length of rebar set.

Get: ArrayLength(self: RebarContainerItem) -> float

Set: ArrayLength(self: RebarContainerItem) = value
"""

    BarsOnNormalSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.

Get: BarsOnNormalSide(self: RebarContainerItem) -> bool

Set: BarsOnNormalSide(self: RebarContainerItem) = value
"""

    BarTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier of the rebar bar type.

Get: BarTypeId(self: RebarContainerItem) -> ElementId

"""

    BaseFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the lower end of the spiral.

Get: BaseFinishingTurns(self: RebarContainerItem) -> int

Set: BaseFinishingTurns(self: RebarContainerItem) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the overall height.

Get: Height(self: RebarContainerItem) -> float

Set: Height(self: RebarContainerItem) = value
"""

    IncludeFirstBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the first bar in rebar set is shown.

Get: IncludeFirstBar(self: RebarContainerItem) -> bool

Set: IncludeFirstBar(self: RebarContainerItem) = value
"""

    IncludeLastBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the last bar in rebar set is shown.

Get: IncludeLastBar(self: RebarContainerItem) -> bool

Set: IncludeLastBar(self: RebarContainerItem) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarContainerItem) -> bool

"""

    ItemIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of this item in its associated RebarContainer.

Get: ItemIndex(self: RebarContainerItem) -> int

"""

    LayoutRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the layout rule of rebar set.

Get: LayoutRule(self: RebarContainerItem) -> RebarLayoutRule

"""

    MaxSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the maximum spacing between rebar in rebar set.

Get: MaxSpacing(self: RebarContainerItem) -> float

Set: MaxSpacing(self: RebarContainerItem) = value
"""

    MultiplanarDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a multiplanar rebar, the depth of the instance.

Get: MultiplanarDepth(self: RebarContainerItem) -> float

Set: MultiplanarDepth(self: RebarContainerItem) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unit-length vector normal to the plane of the rebar

Get: Normal(self: RebarContainerItem) -> XYZ

"""

    NumberOfBarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of potential bars in the set.

Get: NumberOfBarPositions(self: RebarContainerItem) -> int

Set: NumberOfBarPositions(self: RebarContainerItem) = value
"""

    Pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the pitch, or vertical distance traveled in one rotation.

Get: Pitch(self: RebarContainerItem) -> float

Set: Pitch(self: RebarContainerItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the number of bars in rebar set.

Get: Quantity(self: RebarContainerItem) -> int

"""

    RebarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the rebar.

Get: RebarShapeId(self: RebarContainerItem) -> ElementId

Set: RebarShapeId(self: RebarContainerItem) = value
"""

    TopFinishingTurns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a spiral, the number of finishing turns at the upper end of the spiral.

Get: TopFinishingTurns(self: RebarContainerItem) -> int

Set: TopFinishingTurns(self: RebarContainerItem) = value
"""

    TotalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of an individual bar multiplied by Quantity.

Get: TotalLength(self: RebarContainerItem) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of an individual bar multiplied by Quantity.

Get: Volume(self: RebarContainerItem) -> float

"""



class RebarContainerIterator(object, IEnumerator[RebarContainerItem], IDisposable, IEnumerator):
    """ An iterator to a Rebar Container. """
    def Dispose(self):
        """ Dispose(self: RebarContainerIterator) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: RebarContainerIterator) -> bool
        
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
        """ ReleaseUnmanagedResources(self: RebarContainerIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: RebarContainerIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RebarContainerItem](enumerator: IEnumerator[RebarContainerItem], value: RebarContainerItem) -> bool """
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

Get: Current(self: RebarContainerIterator) -> RebarContainerItem

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarContainerIterator) -> bool

"""



class RebarContainerParameterManager(object, IDisposable):
    """ Provides implementation of RebarContainer parameters overrides. """
    def AddOverride(self, paramId, value):
        """
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: int)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: float)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: ElementId)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: str)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        """
        pass

    def AddSharedParameterAsOverride(self, paramId):
        """
        AddSharedParameterAsOverride(self: RebarContainerParameterManager, paramId: ElementId)
            Adds a shared parameter as one of the parameter overrides stored by this Rebar 
             Container element.
        
        
            paramId: The id of the shared parameter element
        """
        pass

    def ClearOverrides(self):
        """
        ClearOverrides(self: RebarContainerParameterManager)
            Clears any overridden values from all parameters of the associated 
             RebarContainer element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarContainerParameterManager) """
        pass

    def IsOverriddenParameterModifiable(self, paramId):
        """
        IsOverriddenParameterModifiable(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if overridden parameter is modifiable.
        
            paramId: Overridden parameter id
            Returns: True if the parameter is modifiable, false if the parameter is readonly.
        """
        pass

    def IsParameterOverridden(self, paramId):
        """
        IsParameterOverridden(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if the parameter has an override
        
            paramId: The id of the parameter element
            Returns: True if the parameter has an override
        """
        pass

    def IsRebarContainerParameter(self, paramId):
        """
        IsRebarContainerParameter(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if the parameter is a Rebar Container parameter
        
            paramId: The id of the parameter element
            Returns: True if the parameter is  a Rebar Container parameter
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarContainerParameterManager, disposing: bool) """
        pass

    def RemoveOverride(self, paramId):
        """
        RemoveOverride(self: RebarContainerParameterManager, paramId: ElementId)
            Removes an overridden value from the given parameter.
        
            paramId: The id of the parameter
        """
        pass

    def SetOverriddenParameterModifiable(self, paramId):
        """
        SetOverriddenParameterModifiable(self: RebarContainerParameterManager, paramId: ElementId)
            Sets this overridden parameter to be modifiable.
        
            paramId: Overridden parameter id
        """
        pass

    def SetOverriddenParameterReadonly(self, paramId):
        """
        SetOverriddenParameterReadonly(self: RebarContainerParameterManager, paramId: ElementId)
            Sets this overridden parameter to be readonly.
        
            paramId: Overridden parameter id
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarContainerParameterManager) -> bool

"""



class RebarContainerType(ElementType, IDisposable):
    """ Represents a Rebar Container Type, used in the generation of Rebar Container. """
    @staticmethod
    def CreateDefaultRebarContainerType(aDoc):
        """
        CreateDefaultRebarContainerType(aDoc: Document) -> ElementId
        
            Creates a new RebarContainerType object with a default name.
        
            aDoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetOrCreateRebarContainerType(aDoc, name):
        """
        GetOrCreateRebarContainerType(aDoc: Document, name: str) -> ElementId
        
            Creates or returns a RebarContainerType object with a given name.
        
            aDoc: The document.
            name: Name of the type.
            Returns: The type id.
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


class RebarCoupler(Element, IDisposable):
    """ Represents a rebar coupler element in Autodesk Revit. """
    def CouplerLinkTwoBars(self):
        """
        CouplerLinkTwoBars(self: RebarCoupler) -> bool
        
            returns true if the coupler sits on two rebar and false otherwise
        """
        pass

    @staticmethod
    def Create(doc, typeId, pFirstData, pSecondData, error):
        """
        Create(doc: Document, typeId: ElementId, pFirstData: ReinforcementData, pSecondData: ReinforcementData) -> (RebarCoupler, RebarCouplerError)
        
            Creates a new instance of a Rebar Coupler element within the project.
        
            doc: A document.
            typeId: type id for coupler
            pFirstData: information about the first reinforcement to be coupled
            pSecondData: information about the second reinforcement to be coupled; for the default 
             value, coupler is placed on one reinforcement
        
            Returns: The newly created Rebar Coupler instance, or ll if the operation fails.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCoupledReinforcementData(self):
        """
        GetCoupledReinforcementData(self: RebarCoupler) -> IList[ReinforcementData]
        
            gets the reinforcement data. If coupler stays on one bar the list will have 
             size = 1. If coupler connects two bars the size will be 2.
        """
        pass

    def GetCouplerPositionTransform(self, couplerPositionIndex):
        """
        GetCouplerPositionTransform(self: RebarCoupler, couplerPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of the coupler at index 
             couplerPositionIndex in the set.
        
        
            couplerPositionIndex: An index between 0 and (CouplerQuantity-1).
            Returns: The position of a coupler in the set relative (0,0,0).
        """
        pass

    def GetCouplerQuantity(self):
        """
        GetCouplerQuantity(self: RebarCoupler) -> int
        
            Identifies the number of couplers in a set.
            Returns: Returns the number of couplers in a set.
        """
        pass

    def GetPointsForPlacement(self):
        """
        GetPointsForPlacement(self: RebarCoupler) -> IList[XYZ]
        
            gets the point (or points in case of rebar set) where the coupler is placed
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

    CouplerMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """gets and sets the coupler mark

Get: CouplerMark(self: RebarCoupler) -> str

Set: CouplerMark(self: RebarCoupler) = value
"""



class RebarCouplerError(Enum, IComparable, IFormattable, IConvertible):
    """
    Error states for the Rebar Coupler
    
    enum RebarCouplerError, values: BarSegementsAreNotParallel (6), BarSegmentsAreNotOnSameLine (7), BarSegmentSmallerThanEngagement (13), BarsNotTouching (3), CurvesOtherThanLine (12), DifferentLayout (2), InconsistentShape (8), IncorrectEndTreatmentCoupler (5), IncorrectEndTreatmentHook (4), IncorrectInputData (1), InvalidDiameter (9), ValidationSuccessfuly (0), VaryingDistanceBetweenDistributionsBars (14)
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

    BarSegementsAreNotParallel = None
    BarSegmentsAreNotOnSameLine = None
    BarSegmentSmallerThanEngagement = None
    BarsNotTouching = None
    CurvesOtherThanLine = None
    DifferentLayout = None
    InconsistentShape = None
    IncorrectEndTreatmentCoupler = None
    IncorrectEndTreatmentHook = None
    IncorrectInputData = None
    InvalidDiameter = None
    ValidationSuccessfuly = None
    value__ = None
    VaryingDistanceBetweenDistributionsBars = None


class RebarCoverType(ElementType, IDisposable):
    """ A named value for a clear cover distance. """
    @staticmethod
    def Create(doc, name, coverDistance):
        """
        Create(doc: Document, name: str, coverDistance: float) -> RebarCoverType
        
            Creates a new CoverType in the document.
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

    CoverDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A distance that can be used as a concrete cover value in a document.

Get: CoverDistance(self: RebarCoverType) -> float

Set: CoverDistance(self: RebarCoverType) = value
"""



class RebarDeformationType(Enum, IComparable, IFormattable, IConvertible):
    """
    Bar deformation type
    
    enum RebarDeformationType, values: Deformed (0), Plain (1)
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

    Deformed = None
    Plain = None
    value__ = None


class RebarHandleType(Enum, IComparable, IFormattable, IConvertible):
    """
    The various types of handles on a Rebar instance that can be joined to References
    
    enum RebarHandleType, values: Edge (3), EndOfBar (2), OutOfPlaneExtent (4), RebarPlane (0), StartOfBar (1)
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

    Edge = None
    EndOfBar = None
    OutOfPlaneExtent = None
    RebarPlane = None
    StartOfBar = None
    value__ = None


class RebarHookOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Orientation of a rebar hook relative to the path of the Rebar Shape.
    
    enum RebarHookOrientation, values: Left (1), Right (-1)
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
    Right = None
    value__ = None


class RebarHookType(ElementType, IDisposable):
    """ A Rebar Hook type object that is used in the generation of Rebar. """
    @staticmethod
    def Create(doc, angle, multiplier):
        """
        Create(doc: Document, angle: float, multiplier: float) -> RebarHookType
        
            Creates a new RebarHookType in a document.
        
            angle: Determine the hook angle of new RebarHookType.
            multiplier: Determine the straight line multiplier of new RebarHookType.
        """
        pass

    @staticmethod
    def CreateDefaultRebarHookType(ADoc):
        """
        CreateDefaultRebarHookType(ADoc: Document) -> ElementId
        
            Creates a new RebarHookType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetDefaultHookExtension(self, barDiameter):
        """
        GetDefaultHookExtension(self: RebarHookType, barDiameter: float) -> float
        
            Computes the default hook length, which is equal to barDiameter * multiplier.
        """
        pass

    def GetHookExtensionLength(self, barType):
        """
        GetHookExtensionLength(self: RebarHookType, barType: RebarBarType) -> float
        
            Computes the hook extension length based on current hook length
        """
        pass

    def IsOffsetLengthRequired(self):
        """
        IsOffsetLengthRequired(self: RebarHookType) -> bool
        
            Check whether hook offset length is required.
           remarks: If hook angle is no 
             more than 90 degree, hook offset length is not meaningful.
           returns: True if 
             hook offset length is required, otherwise false.
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

    HookAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hook angle, measured in radians. Must be greater than 0 and no more than pi.

Get: HookAngle(self: RebarHookType) -> float

Set: HookAngle(self: RebarHookType) = value
"""

    StraightLineMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multiplier of bar diameter. Used to compute a default hook length.
   The default hook length can be overridden by the RebarBarType class.

Get: StraightLineMultiplier(self: RebarHookType) -> float

Set: StraightLineMultiplier(self: RebarHookType) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hook may only be applied to shapes of the specified style.

Get: Style(self: RebarHookType) -> RebarStyle

Set: Style(self: RebarHookType) = value
"""



class RebarHostCategory(Enum, IComparable, IFormattable, IConvertible):
    """
    Rebar host category
    
    enum RebarHostCategory, values: Floor (5), Other (0), Part (1), SlabEdge (8), Stairs (7), StructuralColumn (2), StructuralFoundation (6), StructuralFraming (3), Wall (4)
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
    Other = None
    Part = None
    SlabEdge = None
    Stairs = None
    StructuralColumn = None
    StructuralFoundation = None
    StructuralFraming = None
    value__ = None
    Wall = None


class RebarHostData(object, IDisposable):
    """ Interface to rebar-specific data stored in each valid rebar host element. """
    def Dispose(self):
        """ Dispose(self: RebarHostData) """
        pass

    def GetAreaReinforcementsInHost(self):
        """
        GetAreaReinforcementsInHost(self: RebarHostData) -> IList[AreaReinforcement]
        
            Returns all AreaReinforcement elements hosted by the referenced element.
        """
        pass

    def GetCommonCoverType(self):
        """
        GetCommonCoverType(self: RebarHostData) -> RebarCoverType
        
            If all exposed faces of the host have the same associated CoverType,
           return 
             that CoverType; otherwise, return ll.
        
            Returns: The common CoverType for all exposed faces, or ll
           if there are multiple 
             CoverTypes.
        """
        pass

    def GetCoverType(self, face):
        """
        GetCoverType(self: RebarHostData, face: Reference) -> RebarCoverType
        
            Gets the CoverType associated with a face of the element.
            Returns: The cover associated with the face, if it is an exposed face.
           If the face 
             is concealed, returns ll.
        """
        pass

    def GetExposedFaces(self):
        """
        GetExposedFaces(self: RebarHostData) -> IList[Reference]
        
            Returns all the exposed faces, that is, those that have an associated CoverType.
        """
        pass

    def GetFabricAreasInHost(self):
        """
        GetFabricAreasInHost(self: RebarHostData) -> IList[FabricArea]
        
            Returns all FabricArea elements hosted by the referenced element.
        """
        pass

    def GetFabricSheetsInHost(self):
        """
        GetFabricSheetsInHost(self: RebarHostData) -> IList[FabricSheet]
        
            Returns all FabricSheet elements hosted by the referenced element.
        """
        pass

    def GetPathReinforcementsInHost(self):
        """
        GetPathReinforcementsInHost(self: RebarHostData) -> IList[PathReinforcement]
        
            Returns all PathReinforcement elements hosted by the referenced element.
        """
        pass

    def GetRebarContainersInHost(self):
        """
        GetRebarContainersInHost(self: RebarHostData) -> IList[RebarContainer]
        
            Returns all RebarContainer elements hosted by the referenced element.
        """
        pass

    @staticmethod
    def GetRebarHostData(host):
        """
        GetRebarHostData(host: Element) -> RebarHostData
        
            Gets a RebarHostData object referring to the specified
           rebar host element.
        
            host: An element to host rebar.
            Returns: A RebarHostData object, or ll.
        """
        pass

    def GetRebarsInHost(self):
        """
        GetRebarsInHost(self: RebarHostData) -> IList[Rebar]
        
            Returns all Rebar elements hosted by the referenced element.
        """
        pass

    def IsFaceExposed(self, face):
        """
        IsFaceExposed(self: RebarHostData, face: Reference) -> bool
        
            Checks whether the specified face is considered exposed, and
           therefore has 
             an associated CoverType.
        
            Returns: True if %face% is exposed, false otherwise.
        """
        pass

    @staticmethod
    def IsValidHost(element=None):
        """
        IsValidHost(self: RebarHostData) -> bool
        
            Reports whether the element is a valid rebar host.
            Returns: True if the referenced Element can currently host Rebar elements,
           false 
             otherwise.
        
        IsValidHost(element: Element) -> bool
        
            Identifies whether a given element can host reinforcement.
        
            element: The element to check.
            Returns: True if the input Element can host reinforcement elements,
           false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarHostData, disposing: bool) """
        pass

    def SetCommonCoverType(self, coverType):
        """
        SetCommonCoverType(self: RebarHostData, coverType: RebarCoverType)
            Associate a single CoverType with all exposed faces of the host element.
        
            coverType: A CoverType object to be applied to all faces.
        """
        pass

    def SetCoverType(self, face, coverType):
        """
        SetCoverType(self: RebarHostData, face: Reference, coverType: RebarCoverType)
            Associates the specified CoverType with the specified face of the element.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarHostData) -> bool

"""



class RebarInSystem(Element, IDisposable):
    """ Represents a rebar element that is part of a system. """
    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: RebarInSystem, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this rebar in the given view.
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if a presentation mode can be applied for the given view, false otherwise.
        """
        pass

    def ClearPresentationMode(self, dBView):
        """
        ClearPresentationMode(self: RebarInSystem, dBView: View)
            Sets the presentation mode for this rebar set to the default (either for a 
             single view, or for all views).
        
        
            dBView: The view where the presentation mode will be cleared. NULL for all views
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def DoesBarExistAtPosition(self, barPosition):
        """
        DoesBarExistAtPosition(self: RebarInSystem, barPosition: int) -> bool
        
            Checks whether a bar exists at the specified position.
        
            barPosition: A bar position index between 0 and NumberOfBarPositions-1.
            Returns: Always returns true, since it is not possible to de-activate the first or last 
             bars
           in a Rebar set that is part of Area or Path Reinforcement.
           (see 
             includeFirstBar and includeLastBar methods for Rebar)
        """
        pass

    def FindMatchingPredefinedPresentationMode(self, dBView):
        """
        FindMatchingPredefinedPresentationMode(self: RebarInSystem, dBView: View) -> RebarPresentationMode
        
            Determines if there is a matching RebarPresentationMode for the current set of 
             selected hidden and unhidden bars assigned to the given view.
        
        
            dBView: The view.
            Returns: The presentation mode that matches the current set of selected hidden and 
             unhidden bars.
           If there is no better match, this returns 
             RebarPresentationMode.Select.
        """
        pass

    def GetBarPositionTransform(self, barPositionIndex):
        """
        GetBarPositionTransform(self: RebarInSystem, barPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of any
           individual bar 
             in the set.
        
        
            barPositionIndex: An index between 0 and (NumberOfBarPositions-1).
            Returns: The position of a bar in the set relative to the first position.
        """
        pass

    def GetBendData(self):
        """
        GetBendData(self: RebarInSystem) -> RebarBendData
        
            Gets the RebarBendData, containing bar and hook information, of the instance.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCenterlineCurves(self, adjustForSelfIntersection, suppressHooks, suppressBendRadius):
        """
        GetCenterlineCurves(self: RebarInSystem, adjustForSelfIntersection: bool, suppressHooks: bool, suppressBendRadius: bool) -> IList[Curve]
        
            A chain of curves representing the centerline of the rebar.
        
            adjustForSelfIntersection: If the curves overlap, as in a planar stirrup, this parameter controls
           
             whether they should be adjusted to avoid intersection (as in fine views),
           
             or kept in a single plane for simplicity (as in coarse views).
        
            suppressHooks: Identifies if the chain will include hooks curves.
            suppressBendRadius: Identifies if the connected chain will include unfilleted curves.
            Returns: The centerline curves or empty array if the curves cannot be computed because
         
               the parameters values are inconsistent
           with the constraints of the 
             RebarShape definition.
        """
        pass

    def GetDistributionPath(self):
        """
        GetDistributionPath(self: RebarInSystem) -> Line
        
            The distribution path of a rebar set.
            Returns: A line beginning at (0, 0, 0) and representing the direction and
           length of 
             the set.
        """
        pass

    def GetHookTypeId(self, end):
        """
        GetHookTypeId(self: RebarInSystem, end: int) -> ElementId
        
            Get the id of the RebarHookType to be applied to the rebar.
        
            end: 0 for the start hook, 1 for the end hook.
            Returns: The id of a RebarHookType, or invalidElementId if the rebar has
           no hook at 
             the specified end.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: RebarInSystem) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetPresentationMode(self, dBView):
        """
        GetPresentationMode(self: RebarInSystem, dBView: View) -> RebarPresentationMode
        
            Gets the presentaion mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            Returns: The presentation mode.
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: RebarInSystem) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: RebarInSystem, dBView: View) -> bool
        
            Identifies if this RebarInSystem has overridden default presentation settings 
             for the given view.
        
        
            dBView: The view.
            Returns: True if this RebarInSystem has overriden default presentation settings, false 
             otherwise.
        """
        pass

    def IsBarHidden(self, view, barIndex):
        """
        IsBarHidden(self: RebarInSystem, view: View, barIndex: int) -> bool
        
            Identifies if a given bar in this rebar set is hidden in this view.
        
            view: The view.
            barIndex: The index of the bar from this rebar set.
            Returns: True if the bar is hidden in this view, false otherwise.
        """
        pass

    def IsRebarInSection(self, dBView):
        """
        IsRebarInSection(self: RebarInSystem, dBView: View) -> bool
        
            Identifies if this RebarInSystem is shown as a cross-section in the given view.
        
            dBView: The view.
            Returns: True if this RebarInSystem is shown as a cross-section, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: RebarInSystem, view: View3D) -> bool
        
            Checks if this rebar element is shown solidly in a 3D view.
        
            view: The 3D view element
            Returns: True if rebar is shown solidly, false otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: RebarInSystem, view: View) -> bool
        
            Checks if this rebar element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetBarHiddenStatus(self, view, barIndex, hide):
        """
        SetBarHiddenStatus(self: RebarInSystem, view: View, barIndex: int, hide: bool)
            Sets the bar in this rebar set to be hidden or unhidden in the given view.
        
            view: The view.
            barIndex: The index of the bar from this set.
            hide: True to hide this bar in the view, false to unhide the bar.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPresentationMode(self, dBView, presentationMode):
        """
        SetPresentationMode(self: RebarInSystem, dBView: View, presentationMode: RebarPresentationMode)
            Sets the presentation mode for this rebar set when displayed in the given view.
        
            dBView: The view.
            presentationMode: The presentation mode.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: RebarInSystem, view: View3D, solid: bool)
            Sets this rebar element to be shown solidly in a 3D view.
        
            view: The 3D view element
            solid: True if rebar element is shown solidly, false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: RebarInSystem, view: View, unobscured: bool)
            Sets  RebarInSystem element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if  RebarInSystem element is shown unobscured, false otherwise.
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

    ArrayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the distribution path length of rebar set.

Get: ArrayLength(self: RebarInSystem) -> float

"""

    BarsOnNormalSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the bars of the rebar set are on the same side of the rebar plane indicated by the normal.
   For the current implementation of RebarInSystem, this property will always return true,
   but it is included in the RebarInSystem interface for consistency with the Rebar class.

Get: BarsOnNormalSide(self: RebarInSystem) -> bool

"""

    LayoutRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the layout rule of rebar set.

Get: LayoutRule(self: RebarInSystem) -> RebarLayoutRule

"""

    MaxSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the maximum spacing between rebar in rebar set.

Get: MaxSpacing(self: RebarInSystem) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unit-length vector normal to the plane of the rebar

Get: Normal(self: RebarInSystem) -> XYZ

"""

    NumberOfBarPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bar positions available in the rebar.

Get: NumberOfBarPositions(self: RebarInSystem) -> int

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the number of bars in rebar set.
   For the current implementation of RebarInSystem, this property will always return the same number as NumberOfBarPositions,
   since the first and last bars of a RebarInSystem set cannot be suppressed.
   However, it is included in the RebarInSystem interface for consistency with the Rebar class.

Get: Quantity(self: RebarInSystem) -> int

"""

    RebarShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RebarShape element that defines the shape of the rebar.

Get: RebarShapeId(self: RebarInSystem) -> ElementId

"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: RebarInSystem) -> str

Set: ScheduleMark(self: RebarInSystem) = value
"""

    SystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of an AreaReinforcement or PathReinforcement element that owns
   this element.

Get: SystemId(self: RebarInSystem) -> ElementId

"""

    TotalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of an individual bar multiplied by Quantity.

Get: TotalLength(self: RebarInSystem) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of an individual bar multiplied by Quantity.

Get: Volume(self: RebarInSystem) -> float

"""



class RebarLayoutRule(Enum, IComparable, IFormattable, IConvertible):
    """
    The rule for how the rebars in rebar set are laid out
    
    enum RebarLayoutRule, values: FixedNumber (1), MaximumSpacing (2), MinimumClearSpacing (4), NumberWithSpacing (3), Single (0)
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

    FixedNumber = None
    MaximumSpacing = None
    MinimumClearSpacing = None
    NumberWithSpacing = None
    Single = None
    value__ = None


class RebarPresentationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Bar presentation mode
    
    enum RebarPresentationMode, values: All (0), FirstLast (1), Middle (2), Select (3)
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

    All = None
    FirstLast = None
    Middle = None
    Select = None
    value__ = None


class ReinforcementData(object, IDisposable):
    """ Abstract class for various reinforcement data """
    def Dispose(self):
        """ Dispose(self: ReinforcementData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementData, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReinforcementData) -> bool

"""



class RebarReinforcementData(ReinforcementData, IDisposable):
    """ class containing the id and the end of rebar on which the coupler stays """
    @staticmethod
    def Create(rebarId, iEnd):
        """
        Create(rebarId: ElementId, iEnd: int) -> RebarReinforcementData
        
            Creates a new instance of RebarReinforcementData, or ll if the operation fails.
        
            rebarId: the Id of the rebar
            iEnd: The end of rebar where the coupler stays. This should be 0 or 1
            Returns: Creates a new instance of RebarReinforcementData
        """
        pass

    def Dispose(self):
        """ Dispose(self: ReinforcementData, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementData, disposing: bool) """
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

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end of the rebar. The end should be 0 or 1.

Get: End(self: RebarReinforcementData) -> int

Set: End(self: RebarReinforcementData) = value
"""

    RebarId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Rebar

Get: RebarId(self: RebarReinforcementData) -> ElementId

Set: RebarId(self: RebarReinforcementData) = value
"""



class RebarRoundingManager(ReinforcementRoundingManager, IDisposable):
    """ Provides access to element reinforcement roundings overrides. """
    def Dispose(self):
        """ Dispose(self: ReinforcementRoundingManager, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementRoundingManager, disposing: bool) """
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

    ApplicableReinforcementRoundingSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the source of the rounding settings for this element.

Get: ApplicableReinforcementRoundingSource(self: RebarRoundingManager) -> ReinforcementRoundingSource

"""

    ApplicableSegmentLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding for shared parameters used by rebar.

Get: ApplicableSegmentLengthRounding(self: RebarRoundingManager) -> float

"""

    ApplicableSegmentLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding method for shared parameters used by rebar.

Get: ApplicableSegmentLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod

"""

    ApplicableTotalLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding for Bar Length and Total Bar Length parameters.

Get: ApplicableTotalLengthRounding(self: RebarRoundingManager) -> float

"""

    ApplicableTotalLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The applicable rounding method for Bar Length and Total Bar Length parameters.

Get: ApplicableTotalLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod

"""

    SegmentLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rounding for shared parameters used by rebar.

Get: SegmentLengthRounding(self: RebarRoundingManager) -> float

Set: SegmentLengthRounding(self: RebarRoundingManager) = value
"""

    SegmentLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the segment length rounding method

Get: SegmentLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod

Set: SegmentLengthRoundingMethod(self: RebarRoundingManager) = value
"""

    TotalLengthRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rounding for Bar Length and Total Bar Length parameters.

Get: TotalLengthRounding(self: RebarRoundingManager) -> float

Set: TotalLengthRounding(self: RebarRoundingManager) = value
"""

    TotalLengthRoundingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the total length rounding method

Get: TotalLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod

Set: TotalLengthRoundingMethod(self: RebarRoundingManager) = value
"""



class RebarShape(ElementType, IDisposable):
    """ RebarShape specifies the shape type for a Rebar instance. """
    @staticmethod
    def Create(doc, definition, multiplanarDefinition, style, attachmentType, startHookAngle, startHookOrientation, endHookAngle, endHookOrientation, higherEnd):
        """
        Create(doc: Document, definition: RebarShapeDefinition, multiplanarDefinition: RebarShapeMultiplanarDefinition, style: RebarStyle, attachmentType: StirrupTieAttachmentType, startHookAngle: int, startHookOrientation: RebarHookOrientation, endHookAngle: int, endHookOrientation: RebarHookOrientation, higherEnd: int) -> RebarShape
        
            Create a new instance of a Rebar Shape, which defines the shape of a rebar.
        
            doc: A document to contain the RebarShape.
            definition: The definition of the rebar shape, as a set of curves in a plane
           driven by 
             parameters.
        
            multiplanarDefinition: If not null, the created RebarShape will be a 3D shape. The shape
           is built 
             out of the planar RebarShapeDefinition, with additional
           out-of-plane 
             segments defined by the RebarShapeMultiplanarDefinition
           object. Not 
             supported in conjunction with RebarShapeDefinitionByArc
           of type Spiral or 
             LappedCircle.
        
            style: Whether the shape is to be used as a standard bar or a stirrup/tie.
            attachmentType: When the style is stirrup/tie, specify whether it will attach to the
           
             interior of cover (cover is measured to the stirrups), or to the
           exterior 
             of cover (cover is measured to the standard bars).
           Ignored when the style 
             is Standard.
        
            startHookAngle: The start hook angle, expressed as an integral number of degrees.
           If 0, the 
             shape will have no start hook. Common values are 0, 90, 135, and 180.
        
            startHookOrientation: The orientation of the start hook.
           Ignored when startHookAngle is 0.
            endHookAngle: The end hook angle, expressed as an integral number of degrees.
           If 0, the 
             shape will have no end hook. Common values are 0, 90, 135, and 180.
        
            endHookOrientation: The orientation of the end hook.
           Ignored when endHookAngle is 0.
            higherEnd: When the rebar crosses itself, one end will be "lifted" to avoid 
             self-intersection.
           Specify which end should be lifted: 0 for start, 1 for 
             end.
        
            Returns: A new RebarShape instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAllowed(self, barType):
        """
        GetAllowed(self: RebarShape, barType: RebarBarType) -> bool
        
            Check whether a bar type can be used with this RebarShape. Bar types are 
             allowed by default.
        
        
            barType: A bar type in the same document as this shape.
            Returns: True if this shape may be combined with this barType.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCurvesForBrowser(self):
        """
        GetCurvesForBrowser(self: RebarShape) -> IList[Curve]
        
            Generate curves for the shape, as used in the shape browser.
            Returns: An array of curves representing the shape with its default parameters.
        """
        pass

    def GetDefaultHookAngle(self, index):
        """
        GetDefaultHookAngle(self: RebarShape, index: int) -> int
        
            Get the hook angle, expressed as an integral number of degrees (common values 
             are 0, 90, 135, and 180).
        
        
            index: 0 for the starting hook, 1 for the ending hook.
        """
        pass

    def GetDefaultHookOrientation(self, index):
        """
        GetDefaultHookOrientation(self: RebarShape, index: int) -> RebarHookOrientation
        
            Get the hook orientation.
        
            index: 0 for the starting hook, 1 for the ending hook.
        """
        pass

    def GetEndTreatmentTypeId(self, iEnd):
        """
        GetEndTreatmentTypeId(self: RebarShape, iEnd: int) -> ElementId
        
            get the id of the end treatment for the designated shape end
        """
        pass

    def GetMultiplanarDefinition(self):
        """
        GetMultiplanarDefinition(self: RebarShape) -> RebarShapeMultiplanarDefinition
        
            The optional 3D structure of the shape.
            Returns: A copy of the multiplanar definition. Changes will not affect the RebarShape.
        """
        pass

    def GetRebarShapeDefinition(self):
        """
        GetRebarShapeDefinition(self: RebarShape) -> RebarShapeDefinition
        
            Return the definition of the RebarShape.
            Returns: A copy of the definition. Changes will not affect the RebarShape.
        """
        pass

    def HasEndTreatment(self):
        """
        HasEndTreatment(self: RebarShape) -> bool
        
            returns true if the shape has end treatment for at least one end.
        """
        pass

    def IsSameShapeIgnoringHooks(self, otherShape):
        """
        IsSameShapeIgnoringHooks(self: RebarShape, otherShape: RebarShape) -> bool
        
            Test whether two shapes have equivalent definitions by comparing
           the 
             RebarShapeDefinition and MultiplanarDefinition properties.
        
        
            otherShape: Another shape to be compared to this one.
            Returns: True if the shape definitions match, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetAllowed(self, barType, allowed):
        """
        SetAllowed(self: RebarShape, barType: RebarBarType, allowed: bool)
            Specify which bar types can be used with this RebarShape. Bar types are allowed 
             by default.
        
        
            barType: A bar type in the same document as this shape.
            allowed: Whether this shape may be combined with barType.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetEndTreatmentTypeId(self, treatmenetId, iEnd):
        """
        SetEndTreatmentTypeId(self: RebarShape, treatmenetId: ElementId, iEnd: int)
            set the end treatment type id for the designated shape end
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

    HigherEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the higher end of rebar shape.

Get: HigherEnd(self: RebarShape) -> int

"""

    RebarStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the shape represents a standard bar or a stirrup.

Get: RebarStyle(self: RebarShape) -> RebarStyle

"""

    ShapeFamilyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get and return the rebar shape family id.

Get: ShapeFamilyId(self: RebarShape) -> ElementId

"""

    SimpleArc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check whether this shape consists of a single arc, possibly with hooks.

Get: SimpleArc(self: RebarShape) -> bool

"""

    SimpleLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check whether this shape consists of a single straight segment, possibly with hooks.

Get: SimpleLine(self: RebarShape) -> bool

"""

    StirrupTieAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The attachment type of stirrup ties and rebars.

Get: StirrupTieAttachment(self: RebarShape) -> StirrupTieAttachmentType

"""



class RebarShapeArcReferenceType(Enum, IComparable, IFormattable, IConvertible):
    """
    A Rebar Shape Definition constraint that is
       measured to a bend must take the bar diameter into
       account by specifying whether it measures to
       the exterior, centerline, or interior of the bend.
    
    enum RebarShapeArcReferenceType, values: Centerline (0), External (1), Internal (-1)
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

    Centerline = None
    External = None
    Internal = None
    value__ = None


class RebarShapeBendAngle(Enum, IComparable, IFormattable, IConvertible):
    """
    A bend in a rebar shape has an angular range
       specified by one of these values. The angles refer to
       the angle swept out by one segment as it is bent
       relative to another. That is, an "Obtuse" bend results
       in two segments that meet at an angle that is less
       than 90 degrees when measured internally. Put another
       way, to create an equilateral triangle, you would need
       two "Obtuse" bends.
    
    enum RebarShapeBendAngle, values: Acute (1), Obtuse (3), Right (2)
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

    Acute = None
    Obtuse = None
    Right = None
    value__ = None


class RebarShapeConstraint(object, IDisposable):
    """ A dimension or other constraint that takes part in a RebarShapeDefinition. """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint) """
        pass

    def GetParamId(self):
        """
        GetParamId(self: RebarShapeConstraint) -> ElementId
        
            Return the Id of the parameter associated with this constraint.
            Returns: The Id of the parameter, or InvalidElementId if the constraint
           does not 
             have one.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeConstraint) -> bool

"""



class RebarShapeConstraint180DegreeBendArcLength(RebarShapeConstraint, IDisposable):
    """
    A constraint which can be applied to a RebarShapeSegment, and causes the segment
       to be replaced with a 180-degree arc. The associated parameter drives
       the arc length.
    
    RebarShapeConstraint180DegreeBendArcLength(paramId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId):
        """ __new__(cls: type, paramId: ElementId) """
        pass


class RebarShapeConstraint180DegreeBendRadius(RebarShapeConstraint, IDisposable):
    """
    A constraint which can be applied to a RebarShapeSegment, and causes the segment
       to be replaced with a 180-degree arc. The associated parameter drives
       the radius of the arc.
    
    RebarShapeConstraint180DegreeBendRadius(paramId: ElementId, refType: RebarShapeArcReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType):
        """ __new__(cls: type, paramId: ElementId, refType: RebarShapeArcReferenceType) """
        pass

    ArcReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A choice of rule for measuring the radius.

Get: ArcReferenceType(self: RebarShapeConstraint180DegreeBendRadius) -> RebarShapeArcReferenceType

"""



class RebarShapeConstraint180DegreeDefaultBend(RebarShapeConstraint, IDisposable):
    """
    A constraint which can be applied to a RebarShapeSegment, and causes the segment
       to be replaced with a 180-degree arc. The arc's radius is not specified
       by the shape; instead it is a "default bend radius," taken from
       the RebarBarType associated with the Rebar instance.
    
    RebarShapeConstraint180DegreeDefaultBend()
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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


class RebarShapeConstraintAngleFromFixedDir(RebarShapeConstraint, IDisposable):
    """
    A constraint which can be applied to a RebarShapeSegment and drives the angle
       of the segment relative to a fixed direction in UV-space.
    
    RebarShapeConstraintAngleFromFixedDir(paramId: ElementId, sign: int, direction: UV)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, sign, direction):
        """ __new__(cls: type, paramId: ElementId, sign: int, direction: UV) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A fixed direction in UV-space. The parameter will drive
   the segment's angle relative to this direction.

Get: Direction(self: RebarShapeConstraintAngleFromFixedDir) -> UV

Set: Direction(self: RebarShapeConstraintAngleFromFixedDir) = value
"""

    Sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When the sign is 1, the Direction is rotated clockwise by the angle's value.
   When -1, the Direction is rotated counter-clockwise.

Get: Sign(self: RebarShapeConstraintAngleFromFixedDir) -> int

Set: Sign(self: RebarShapeConstraintAngleFromFixedDir) = value
"""



class RebarShapeConstraintArcLength(RebarShapeConstraint, IDisposable):
    """
    An arc-length constraint associated with an arc in a RebarShapeDefinition.
    
    RebarShapeConstraintArcLength(paramId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId):
        """ __new__(cls: type, paramId: ElementId) """
        pass


class RebarShapeConstraintChordLength(RebarShapeConstraint, IDisposable):
    """
    A constraint that can be applied to a RebarShapeDefinitionByArc
       and drives the straight distance between the arc endpoints.
    
    RebarShapeConstraintChordLength(paramId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId):
        """ __new__(cls: type, paramId: ElementId) """
        pass


class RebarShapeConstraintCircumference(RebarShapeConstraint, IDisposable):
    """
    A circumference constraint associated with an arc in a RebarShapeDefinition.
    
    RebarShapeConstraintCircumference(paramId: ElementId, refType: RebarShapeArcReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType):
        """ __new__(cls: type, paramId: ElementId, refType: RebarShapeArcReferenceType) """
        pass

    ArcReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The choice of rule for measuring the diameter.

Get: ArcReferenceType(self: RebarShapeConstraintCircumference) -> RebarShapeArcReferenceType

"""



class RebarShapeConstraintDiameter(RebarShapeConstraint, IDisposable):
    """
    A diameter constraint associated with an arc in a RebarShapeDefinition.
    
    RebarShapeConstraintDiameter(paramId: ElementId, refType: RebarShapeArcReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType):
        """ __new__(cls: type, paramId: ElementId, refType: RebarShapeArcReferenceType) """
        pass

    ArcReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The choice of rule for measuring the diameter.

Get: ArcReferenceType(self: RebarShapeConstraintDiameter) -> RebarShapeArcReferenceType

"""



class RebarShapeConstraintFixedSegmentDir(RebarShapeConstraint, IDisposable):
    """
    A constraint that can be applied to a RebarShapeSegment and fixes the
       direction of the segment in UV-space.
    
    RebarShapeConstraintFixedSegmentDir(dir: UV)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, dir):
        """ __new__(cls: type, dir: UV) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the RebarShapeSegment in UV-space.

Get: Direction(self: RebarShapeConstraintFixedSegmentDir) -> UV

Set: Direction(self: RebarShapeConstraintFixedSegmentDir) = value
"""



class RebarShapeConstraintProjectedSegmentLength(RebarShapeConstraint, IDisposable):
    """
    A constraint that measures the length of a segment as measured by projecting onto a direction
       that is not parallel to the segment.
    
    RebarShapeConstraintProjectedSegmentLength(paramId: ElementId, direction: UV, tripleProductSign: int, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def GetSegmentEndReferenceType(self, index):
        """
        GetSegmentEndReferenceType(self: RebarShapeConstraintProjectedSegmentLength, index: int) -> RebarShapeSegmentEndReferenceType
        
            Choice of two possibilities for the start and end references of the length 
             constraint.
        
        
            index: Which reference on the constraint. Either 0 or 1.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, direction, tripleProductSign, refType0, refType1):
        """ __new__(cls: type, paramId: ElementId, direction: UV, tripleProductSign: int, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A vector specifying the direction of the constraint. The direction is fixed,
   and the shape is always constructed so that the segment
   direction has a positive dot product with this vector.

Get: Direction(self: RebarShapeConstraintProjectedSegmentLength) -> UV

"""

    TripleProductSign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sign of the z-coordinate of the cross
   product of the Direction property with the segment vector.
   TripleProductSign is 1 if the segment direction is to be on the left of
   the constraint direction,
   or -1 if the segment direction is to be on the right.

Get: TripleProductSign(self: RebarShapeConstraintProjectedSegmentLength) -> int

"""



class RebarShapeConstraintRadius(RebarShapeConstraint, IDisposable):
    """
    A radius constraint associated with an arc in a RebarShapeDefinition.
    
    RebarShapeConstraintRadius(paramId: ElementId, refType: RebarShapeArcReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType):
        """ __new__(cls: type, paramId: ElementId, refType: RebarShapeArcReferenceType) """
        pass

    ArcReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The choice of rule for measuring the radius.

Get: ArcReferenceType(self: RebarShapeConstraintRadius) -> RebarShapeArcReferenceType

"""



class RebarShapeConstraintSagittaLength(RebarShapeConstraint, IDisposable):
    """
    A constraint that can be applied to a RebarShapeDefinitionByArc
       and drives the height of the arc.
    
    RebarShapeConstraintSagittaLength(paramId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId):
        """ __new__(cls: type, paramId: ElementId) """
        pass


class RebarShapeConstraintSegmentLength(RebarShapeConstraint, IDisposable):
    """
    A constraint that controls the length of a segment.
    
    RebarShapeConstraintSegmentLength(paramId: ElementId, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def GetSegmentEndReferenceType(self, index):
        """
        GetSegmentEndReferenceType(self: RebarShapeConstraintSegmentLength, index: int) -> RebarShapeSegmentEndReferenceType
        
            Choice of two possibilities for the start and end references of the length 
             constraint.
        
        
            index: Which reference on the constraint. Either 0 or 1.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType0, refType1):
        """ __new__(cls: type, paramId: ElementId, refType0: RebarShapeSegmentEndReferenceType, refType1: RebarShapeSegmentEndReferenceType) """
        pass


class RebarShapeDefinition(object, IDisposable):
    """
    A class to assist in defining rebar shapes.
       A RebarShape element needs exactly one RebarShapeDefinition.
    """
    def AddFormulaParameter(self, paramId, formula):
        """
        AddFormulaParameter(self: RebarShapeDefinition, paramId: ElementId, formula: str)
            Add a formula-driven parameter to the shape definition.
        
            paramId: The parameter. To obtain the id of a shared parameter,
           call 
             RebarShapeParameters.GetElementIdForExternalDefinition.
        
            formula: The formula expressed as a string. The string is exactly what a user would
           
             type into the Family Types dialog, e.g. "Total Length*3.14159*(Bar 
             Diameter/2)*(Bar Diameter/2)"
        """
        pass

    def AddParameter(self, paramId, defaultValue):
        """
        AddParameter(self: RebarShapeDefinition, paramId: ElementId, defaultValue: float)
            Add a parameter to the shape definition.
        
            paramId: The parameter. To obtain the id of a shared parameter,
           call 
             RebarShapeParameters.GetElementIdForExternalDefinition.
        
            defaultValue: A default value for this parameter in shapes. The default values
           should be 
             chosen carefully, because they are required to be consistent as a set of 
             constraints.
        """
        pass

    def CheckDefaultParameterValues(self, bendRadius, barDiameter):
        """
        CheckDefaultParameterValues(self: RebarShapeDefinition, bendRadius: float, barDiameter: float) -> bool
        
            Check that the shape can be solved with the default parameter values.
        
            bendRadius: A value for the Bend Radius parameter. Zero is allowed.
            barDiameter: A value for the Bar Diameter parameter. Zero is allowed.
            Returns: True if the rebar can be solved with the
           default parameter values and the 
             given bend radius and
           bar diameter; false if it cannot.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarShapeDefinition) """
        pass

    def GetParameterDefaultValue(self, paramId):
        """
        GetParameterDefaultValue(self: RebarShapeDefinition, paramId: ElementId) -> float
        
            Return the parameter's default value as stored in the definition.
        
            paramId: Id of a parameter in the definition.
            Returns: The parameter value.
        """
        pass

    def GetParameterFormula(self, paramId):
        """
        GetParameterFormula(self: RebarShapeDefinition, paramId: ElementId) -> str
        
            Return the parameter's formula, if one is associated with it.
        
            paramId: Id of a parameter in the definition.
            Returns: The formula, or an empty string if there is no formula for the parameter.
        """
        pass

    def GetParameters(self):
        """
        GetParameters(self: RebarShapeDefinition) -> IList[ElementId]
        
            Return the Ids of the shared parameters in the Definition.
            Returns: List of parameters as ElementIds.
        """
        pass

    def HasParameter(self, paramId):
        """
        HasParameter(self: RebarShapeDefinition, paramId: ElementId) -> bool
        
            Whether the definition stores the parameter.
        
            paramId: Id of a parameter.
            Returns: True if the definition stores the parameter, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeDefinition, disposing: bool) """
        pass

    def RemoveParameter(self, paramId):
        """
        RemoveParameter(self: RebarShapeDefinition, paramId: ElementId)
            Remove the parameter from the definition.
        
            paramId: Id of a parameter in the definition.
        """
        pass

    def SetParameterDefaultValue(self, paramId, value):
        """
        SetParameterDefaultValue(self: RebarShapeDefinition, paramId: ElementId, value: float)
            Change the parameter's value as stored in the definition.
        
            paramId: Id of a parameter in the definition.
            value: New value for the parameter.
        """
        pass

    def SetParameterFormula(self, paramId, formula):
        """
        SetParameterFormula(self: RebarShapeDefinition, paramId: ElementId, formula: str)
            Associate a formula with the parameter.
        
            paramId: Id of a parameter in the definition.
            formula: The formula expressed as a string. The string is exactly what a user would
           
             type into the Family Types dialog, e.g. "Total Length*3.14159*(Bar 
             Diameter/2)*(Bar Diameter/2)"
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Complete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Report whether the shape definition is fully
   constrained.

Get: Complete(self: RebarShapeDefinition) -> bool

"""

    IsPlanar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether the shape definition lies within a plane: false if a spiral,
   true in all other cases.

Get: IsPlanar(self: RebarShapeDefinition) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeDefinition) -> bool

"""



class RebarShapeDefinitionByArc(RebarShapeDefinition, IDisposable):
    """
    Definition of a shape whose size and position can determined by a single arc.
    
    RebarShapeDefinitionByArc(doc: Document, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
    RebarShapeDefinitionByArc(doc: Document, type: RebarShapeDefinitionByArcType)
    """
    def AddConstraintArcLength(self, paramId):
        """
        AddConstraintArcLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the arc length of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def AddConstraintChordLength(self, paramId):
        """
        AddConstraintChordLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the chord length (the straight-line distance 
             between the endpoints of the arc).
        
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def AddConstraintCircumference(self, paramId, arcRefType):
        """
        AddConstraintCircumference(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the circumference of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify along which circle the circumference is measured--to the interior
           
             of the bar, the centerline, or the exterior.
        """
        pass

    def AddConstraintDiameter(self, paramId, arcRefType):
        """
        AddConstraintDiameter(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the diameter of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify how the diameter should be measured--to the interior of the bend, the 
             centerline of the bar, or the exterior.
        """
        pass

    def AddConstraintRadius(self, paramId, arcRefType):
        """
        AddConstraintRadius(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the radius of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify how the radius should be measured--to the interior of the bend, the 
             centerline of the bar, or the exterior.
        """
        pass

    def AddConstraintSagittaLength(self, paramId):
        """
        AddConstraintSagittaLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the sagittal
           length (the height of the 
             circular segment, measured
           perpendicular to the chord).
        
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarShapeDefinition, A_0: bool) """
        pass

    def GetConstraints(self):
        """
        GetConstraints(self: RebarShapeDefinitionByArc) -> IList[RebarShapeConstraint]
        
            Retrieve the list of constraints associated with this definition.
            Returns: The list of constraints.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeDefinition, disposing: bool) """
        pass

    def SetArcTypeSpiral(self, height, pitch, baseFinishingTurns, topFinishingTurns):
        """
        SetArcTypeSpiral(self: RebarShapeDefinitionByArc, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
            Set the RebarShapeDefinitionByArc.Type property to Spiral.
        
            height: The height of the spiral (assuming the spiral is vertical).
            pitch: The pitch, or vertical distance traveled in one rotation.
            baseFinishingTurns: The number of finishing turns at the lower end of the spiral.
            topFinishingTurns: The number of finishing turns at the upper end of the spiral.
        """
        pass

    def SetConstraints(self, constraints):
        """ SetConstraints(self: RebarShapeDefinitionByArc, constraints: IList[RebarShapeConstraint]) """
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
    def __new__(self, doc, *__args):
        """
        __new__(cls: type, doc: Document, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
        __new__(cls: type, doc: Document, type: RebarShapeDefinitionByArcType)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Among those rebar shapes defined by an arc, specify which kind.

Get: Type(self: RebarShapeDefinitionByArc) -> RebarShapeDefinitionByArcType

Set: Type(self: RebarShapeDefinitionByArc) = value
"""



class RebarShapeDefinitionByArcType(Enum, IComparable, IFormattable, IConvertible):
    """
    A RebarShapeDefinitionByArc takes one of three forms.
    
    enum RebarShapeDefinitionByArcType, values: Arc (0), LappedCircle (1), Spiral (2)
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
    LappedCircle = None
    Spiral = None
    value__ = None


class RebarShapeDefinitionBySegments(RebarShapeDefinition, IDisposable):
    """
    Definition of a shape in terms of one or more straight segments of rebar,
       with arc bends between the segments.
    
    RebarShapeDefinitionBySegments(doc: Document, numberOfSegments: int)
    """
    def AddBendDefaultRadius(self, vertexIndex, turn, angle):
        """
        AddBendDefaultRadius(self: RebarShapeDefinitionBySegments, vertexIndex: int, turn: RebarShapeVertexTurn, angle: RebarShapeBendAngle)
            Specify a default-radius bend.
        
            vertexIndex: Index of the vertex (1 to NumberOfVertices - 2).
            turn: Specify turn direction (RebarShapeVertexTurn::Left or 
             RebarShapeVertexTurn::Right).
        
            angle: Specify whether the bend is acute, obtuse, etc.
        """
        pass

    def AddBendVariableRadius(self, vertexIndex, turn, angle, paramId, measureIncludingBarThickness):
        """
        AddBendVariableRadius(self: RebarShapeDefinitionBySegments, vertexIndex: int, turn: RebarShapeVertexTurn, angle: RebarShapeBendAngle, paramId: ElementId, measureIncludingBarThickness: bool)
            Specify a variable-radius bend.
        
            vertexIndex: Index of the vertex (1 to NumberOfVertices - 2).
            turn: Specify turn direction (RebarShapeVertexTurn::Left or 
             RebarShapeVertexTurn::Right).
        
            angle: Specify whether the bend is acute, obtuse, etc.
            paramId: Id of a parameter driving the radius.
            measureIncludingBarThickness: If true, the radius is measured to the outside of the
           bend; if false, it is 
             measured to the inside.
        """
        pass

    def AddConstraintParallelToSegment(self, iSegment, paramId, measureToOutsideOfBend0, measureToOutsideOfBend1):
        """
        AddConstraintParallelToSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, measureToOutsideOfBend0: bool, measureToOutsideOfBend1: bool)
            Constrain the length of a segment by parameterizing its length.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the constraint. To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            measureToOutsideOfBend0: Choose between two possibilities for the first reference of the length 
             dimension. If false, the reference is at the point where the bend begins; 
             equivalently, at the projection of the bend centerpoint onto the segment. If 
             true, the reference is moved outward by a distance equal to the bend radius 
             plus the bar diameter; if the bend is a right angle or greater, this is 
             equivalent to putting the reference at the outer face of the bend.
        
            measureToOutsideOfBend1: Choose between two possibilities for the second reference of the length 
             dimension.
        """
        pass

    def AddConstraintToSegment(self, iSegment, paramId, constraintDirCoordX, constraintDirCoordY, signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, measureToOutsideOfBend0, measureToOutsideOfBend1):
        """
        AddConstraintToSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, signOfZCoordOfCrossProductOfConstraintDirBySegmentDir: int, measureToOutsideOfBend0: bool, measureToOutsideOfBend1: bool)
            Add a constraint that helps determine the length of a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            signOfZCoordOfCrossProductOfConstraintDirBySegmentDir: Legal values are 1 and -1. For a fixed-direction segment, this value is 
             ignored. For a variable-direction segment, this value is combined with the 
             constraint length (the nonnegative value associated with 'param') to determine 
             the direction of the segment. For example, a segment whose direction vector 
             lies in the upper-right quadrant of the plane, and whose x-axis projected 
             length is A and whose y-axis projected length is B, could be created by 
             calling: AddConstraintToSegment(iSegment, paramA, 1.0, 0.0, 1, ...) 
             AddConstraintToSegment(iSegment, paramB, 0.0, 1.0, -1, ...)
        
            measureToOutsideOfBend0: Choose between two possibilities for the first reference of the length 
             dimension. If false, the reference is at the point where the bend begins; 
             equivalently, at the projection of the bend centerpoint onto the segment. If 
             true, the reference is moved outward by a distance equal to the bend radius 
             plus the bar diameter; if the bend is a right angle or greater, this is 
             equivalent to putting the reference at the outer face of the bend.
        
            measureToOutsideOfBend1: Choose between two possibilities for the second reference of the length 
             dimension.
        """
        pass

    def AddListeningDimensionBendToBend(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iEnd0, iSegment1, iEnd1):
        """
        AddListeningDimensionBendToBend(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iEnd0: int, iSegment1: int, iEnd1: int)
            Specify a dimension between two bends, measured by a read-only parameter.
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iEnd0: End (0 or 1) of the first segment.
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
            iEnd1: End (0 or 1) of the second segment.
        """
        pass

    def AddListeningDimensionSegmentToBend(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1, iEnd1):
        """
        AddListeningDimensionSegmentToBend(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iSegment1: int, iEnd1: int)
            Specify a dimension perpendicular to one fixed-direction segment,
           referring 
             to that segment and some other bend in the shape,
           measured by a read-only 
             parameter.
        
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
            iEnd1: End (0 or 1) of the second segment.
        """
        pass

    def AddListeningDimensionSegmentToSegment(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1):
        """
        AddListeningDimensionSegmentToSegment(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iSegment1: int)
            Specify a dimension perpendicular to two fixed-direction segments, measured by 
             a read-only parameter.
        
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarShapeDefinition, A_0: bool) """
        pass

    def GetSegment(self, segmentIndex):
        """
        GetSegment(self: RebarShapeDefinitionBySegments, segmentIndex: int) -> RebarShapeSegment
        
            Return a reference to one of the segments in the definition.
        
            segmentIndex: Index of the segment (0 to NumberOfSegments - 1).
            Returns: The requested segment.
        """
        pass

    def GetVertex(self, vertexIndex):
        """
        GetVertex(self: RebarShapeDefinitionBySegments, vertexIndex: int) -> RebarShapeVertex
        
            Return a reference to one of the vertices in the definition.
        
            vertexIndex: Index of the vertex (0 to NumberOfVertices - 1).
            Returns: The requested vertex.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeDefinition, disposing: bool) """
        pass

    def RemoveParameterFromSegment(self, iSegment, paramId):
        """
        RemoveParameterFromSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId)
            Remove constraints from a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter driving one or more constraints.
        """
        pass

    def SetSegmentAs180DegreeBend(self, iSegment, paramId=None, measureToOutsideOfBend=None):
        """
        SetSegmentAs180DegreeBend(self: RebarShapeDefinitionBySegments, iSegment: int)
            Indicates that a segment is a "virtual" segment introduced to describe a 
             180-degree bend. The radius of the bend will be taken from the Bar Type.
        
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
        SetSegmentAs180DegreeBend(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, measureToOutsideOfBend: bool)
            Indicate that a segment is a "virtual" segment introduced to describe a 
             180-degree bend. The radius of the bend will be driven by radiusParam.
        
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the radius.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            measureToOutsideOfBend: Choose between two possibilities for the references of the radius dimension.
          
              If true, measure to the exterior face of the bar. If false, measure to the 
             interior face.
        """
        pass

    def SetSegmentFixedDirection(self, iSegment, vecCoordX, vecCoordY):
        """
        SetSegmentFixedDirection(self: RebarShapeDefinitionBySegments, iSegment: int, vecCoordX: float, vecCoordY: float)
            Fix the direction of a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            vecCoordX: The x-coordinate of a 2D vector specifying the segment direction.
            vecCoordY: The y-coordinate of a 2D vector specifying the segment direction.
        """
        pass

    def SetSegmentVariableDirection(self, iSegment):
        """
        SetSegmentVariableDirection(self: RebarShapeDefinitionBySegments, iSegment: int)
            Remove the fixed direction from a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
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
    def __new__(self, doc, numberOfSegments):
        """ __new__(cls: type, doc: Document, numberOfSegments: int) """
        pass

    MajorSegmentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of a segment that can be considered the most important. Revit
   attempts to preserve the orientation of this segment when a Rebar instance
   changes its RebarShape to one with a different number of segments.

Get: MajorSegmentIndex(self: RebarShapeDefinitionBySegments) -> int

Set: MajorSegmentIndex(self: RebarShapeDefinitionBySegments) = value
"""

    NumberOfSegments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of straight segments in this shape.

Get: NumberOfSegments(self: RebarShapeDefinitionBySegments) -> int

"""

    NumberOfVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of vertices in this shape, always equal to NumberOfSegments + 1.

Get: NumberOfVertices(self: RebarShapeDefinitionBySegments) -> int

"""



class RebarShapeMultiplanarDefinition(object, IDisposable):
    """
    A specification for a simple 3D rebar shape.
    
    RebarShapeMultiplanarDefinition(outOfPlaneBendDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeMultiplanarDefinition) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeMultiplanarDefinition, disposing: bool) """
        pass

    def SetPresenceOfSegments(self, isDuplicateShapePresent, isStartConnectorPresent, isEndConnectorPresent):
        """
        SetPresenceOfSegments(self: RebarShapeMultiplanarDefinition, isDuplicateShapePresent: bool, isStartConnectorPresent: bool, isEndConnectorPresent: bool)
            Simultaneously set the presence of all 3D segments.
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
    def __new__(self, outOfPlaneBendDiameter):
        """ __new__(cls: type, outOfPlaneBendDiameter: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DepthParamId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the parameter driving the multiplanar depth.
   The depth is measured center-to-center of the bar.
   A valid shape parameter must be assigned to DepthParamId before
   the MultiplanarDefinition can be used in RebarShape creation.

Get: DepthParamId(self: RebarShapeMultiplanarDefinition) -> ElementId

Set: DepthParamId(self: RebarShapeMultiplanarDefinition) = value
"""

    IsDuplicateShapePresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the shape definition includes an offset
   copy of the 2D shape.

Get: IsDuplicateShapePresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsEndConnectorPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether a perpendicular segment is constructed
   from the end of the 2D shape.

Get: IsEndConnectorPresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsStartConnectorPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether a perpendicular segment is constructed
   from the start of the 2D shape.

Get: IsStartConnectorPresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeMultiplanarDefinition) -> bool

"""

    OutOfPlaneBendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend diameter to be applied to the connector segments.

Get: OutOfPlaneBendDiameter(self: RebarShapeMultiplanarDefinition) -> float

Set: OutOfPlaneBendDiameter(self: RebarShapeMultiplanarDefinition) = value
"""



class RebarShapeParameters(object, IDisposable):
    """ Class containing functions that create and retrieve shared parameters for RebarShapes. """
    def Dispose(self):
        """ Dispose(self: RebarShapeParameters) """
        pass

    @staticmethod
    def GetAllRebarShapeParameters(doc):
        """
        GetAllRebarShapeParameters(doc: Document) -> IList[ElementId]
        
            List all shape parameters used by all the existing RebarShapes in the specified 
             document.
        
        
            doc: The document.
            Returns: ElementIds corresponding to the external parameters.
        """
        pass

    @staticmethod
    def GetElementIdForExternalDefinition(doc, externalDefinition):
        """
        GetElementIdForExternalDefinition(doc: Document, externalDefinition: ExternalDefinition) -> ElementId
        
            Retrieve the ElementId corresponding to an external rebar shape parameter
           
             in the document, if it exists; otherwise, return InvalidElementId.
        
        
            doc: A document.
            externalDefinition: A shared parameter.
            Returns: An ElementId representing the shared parameter stored in the document,
           or 
             InvalidElementId if the parameter is not stored in the document.
        """
        pass

    @staticmethod
    def GetExternalDefinitionForElementId(doc, paramId, definitionFile):
        """
        GetExternalDefinitionForElementId(doc: Document, paramId: ElementId, definitionFile: DefinitionFile) -> ExternalDefinition
        
            Seach a DefinitionFile for the ExternalDefinition corresponding to a parameter
        
             in a document.
        
        
            doc: A document.
            paramId: The id of a shared parameter in the document.
            definitionFile: A database of shared parameters.
            Returns: The external parameter corresponding to the parameter's ElementId,
           or null 
             if the Id does not correspond to an external parameter,
           or the parameter is 
             not in the definition file.
        """
        pass

    @staticmethod
    def GetOrCreateElementIdForExternalDefinition(doc, externalDefinition):
        """
        GetOrCreateElementIdForExternalDefinition(doc: Document, externalDefinition: ExternalDefinition) -> ElementId
        
            Retrieve the ElementId corresponding to an external rebar shape parameter
           
             in the document, if it exists; otherwise, add the parameter to the document
           
             and generate a new ElementId.
        
        
            doc: A document.
            externalDefinition: A shared parameter.
            Returns: An ElementId representing the shared parameter stored in the document.
        """
        pass

    @staticmethod
    def IsValidExternalDefinition(param):
        """
        IsValidExternalDefinition(param: ExternalDefinition) -> bool
        
            Checks that an ExternalDefinition (shared parameter) may be used as a Rebar 
             Shape parameter.
        
        
            param: Definition of a shared parameter.
            Returns: True if the definition is of type Length, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeParameters, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeParameters) -> bool

"""



class RebarShapeSegment(object, IDisposable):
    """
    Part of a RebarShapeDefinitionBySegments, representing one segment
       of a shape definition.
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeSegment) """
        pass

    def GetConstraints(self):
        """
        GetConstraints(self: RebarShapeSegment) -> IList[RebarShapeConstraint]
        
            Retrieve the list of constraints associated with this segment.
            Returns: The list of constraints.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeSegment, disposing: bool) """
        pass

    def SetConstraints(self, constraints):
        """ SetConstraints(self: RebarShapeSegment, constraints: IList[RebarShapeConstraint]) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeSegment) -> bool

"""



class RebarShapeSegmentEndReferenceType(Enum, IComparable, IFormattable, IConvertible):
    """
    A choice of two reference points for one end of a constraint driving the length of
       a RebarShapeSegment.
    
    enum RebarShapeSegmentEndReferenceType, values: Exterior (1), Straight (0)
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

    Exterior = None
    Straight = None
    value__ = None


class RebarShapeVertex(object, IDisposable):
    """ A bend between segments of a rebar shape definition. """
    def Dispose(self):
        """ Dispose(self: RebarShapeVertex) """
        pass

    def GetConstraints(self):
        """
        GetConstraints(self: RebarShapeVertex) -> IList[RebarShapeConstraint]
        
            Retrieve the list of constraints associated with this vertex.
            Returns: The list of constraints.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeVertex, disposing: bool) """
        pass

    def SetConstraints(self, constraints):
        """ SetConstraints(self: RebarShapeVertex, constraints: IList[RebarShapeConstraint]) """
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

    BendAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The range of permissible angles at this bend.

Get: BendAngle(self: RebarShapeVertex) -> RebarShapeBendAngle

Set: BendAngle(self: RebarShapeVertex) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeVertex) -> bool

"""

    Turn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sense of the turn. The Turn property must be set to Left or Right on each internal vertex
   before the RebarShapeDefinitionBySegments is used.
   Default is permissible for the first and last vertex, since they do not correspond to bends.

Get: Turn(self: RebarShapeVertex) -> RebarShapeVertexTurn

Set: Turn(self: RebarShapeVertex) = value
"""



class RebarShapeVertexTurn(Enum, IComparable, IFormattable, IConvertible):
    """
    Specify whether a bend at a RebarShapeVertex represents a left or right turn.
    
    enum RebarShapeVertexTurn, values: Default (0), Left (1), Right (-1)
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

    Default = None
    Left = None
    Right = None
    value__ = None


class RebarStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the usage style of a RebarShape.
       The style affects the bend radius and the set of allowable hooks.
       It also affects Rebar instance auto-constraining behavior.
    
    enum RebarStyle, values: Standard (0), StirrupTie (1)
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

    Standard = None
    StirrupTie = None
    value__ = None


class RebarSystemSpanSymbol(IndependentTag, IDisposable):
    """ Represents a Rebar System Span Symbol element in Autodesk Revit. """
    @staticmethod
    def Create(document, viewId, hostId, point, symbolId):
        """
        Create(document: Document, viewId: ElementId, hostId: LinkElementId, point: XYZ, symbolId: ElementId) -> RebarSystemSpanSymbol
        
            Creates a new instance of RebarSystemSpanSymbol in the project.
        
            document: The document.
            viewId: The id of the view in which the symbol should appear.
            hostId: The ElementId of AreaReinforcement (either in the document, or linked from 
             another document).
        
            point: The span symbol's head position.
            symbolId: The id of the family symbol of this symbol.
            Returns: A reference to newly created span symbol.
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


class ReinforcementAbbreviationObjectType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the type of desired reinforcement object for abbreviation tags.
    
    enum ReinforcementAbbreviationObjectType, values: Area (0), Path (1)
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

    Area = None
    Path = None
    value__ = None


class ReinforcementAbbreviationTag(object, IDisposable):
    """
    This class is used to access the Area or Path Reinforcement abbreviation tag data.
       It stores abbreviation tag value and abbreviation type.
    
    ReinforcementAbbreviationTag(typeTag: ReinforcementAbbreviationTagType, abbreviationTag: str)
    """
    def Dispose(self):
        """ Dispose(self: ReinforcementAbbreviationTag) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementAbbreviationTag, disposing: bool) """
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
    def __new__(self, typeTag, abbreviationTag):
        """ __new__(cls: type, typeTag: ReinforcementAbbreviationTagType, abbreviationTag: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AbbreviationTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation tag value.

Get: AbbreviationTag(self: ReinforcementAbbreviationTag) -> str

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReinforcementAbbreviationTag) -> bool

"""

    TypeTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation tag type.

Get: TypeTag(self: ReinforcementAbbreviationTag) -> ReinforcementAbbreviationTagType

"""



class ReinforcementAbbreviationTagType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines all types of abbreviation tags for Area and Path Reinforcement objects.
    
    enum ReinforcementAbbreviationTagType, values: AreaReinforcementBottomMajor (2), AreaReinforcementBottomMinor (3), AreaReinforcementExteriorMajor (6), AreaReinforcementExteriorMinor (7), AreaReinforcementInteriorMajor (4), AreaReinforcementInteriorMinor (5), AreaReinforcementLayerEachFace (9), AreaReinforcementLayerEachWay (8), AreaReinforcementTopMajor (0), AreaReinforcementTopMinor (1), PathReinforcementAlternating (14), PathReinforcementAlternatingBarOffset (15), PathReinforcementBottom (11), PathReinforcementExterior (13), PathReinforcementInterior (12), PathReinforcementTop (10)
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

    AreaReinforcementBottomMajor = None
    AreaReinforcementBottomMinor = None
    AreaReinforcementExteriorMajor = None
    AreaReinforcementExteriorMinor = None
    AreaReinforcementInteriorMajor = None
    AreaReinforcementInteriorMinor = None
    AreaReinforcementLayerEachFace = None
    AreaReinforcementLayerEachWay = None
    AreaReinforcementTopMajor = None
    AreaReinforcementTopMinor = None
    PathReinforcementAlternating = None
    PathReinforcementAlternatingBarOffset = None
    PathReinforcementBottom = None
    PathReinforcementExterior = None
    PathReinforcementInterior = None
    PathReinforcementTop = None
    value__ = None


class ReinforcementBarOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the bar orientation at Path Reinforcement.
    
    enum ReinforcementBarOrientation, values: BottomOrInterior (2), FarSide (3), NearSide (1), TopOrExterior (0)
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

    BottomOrInterior = None
    FarSide = None
    NearSide = None
    TopOrExterior = None
    value__ = None


class ReinforcementRoundingSource(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing the possible sources for reinforcement rounding overrides.
    
    enum ReinforcementRoundingSource, values: Element (3), None (0), ReinforcementSettings (1), Type (2)
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

    Element = None
    None = None
    ReinforcementSettings = None
    Type = None
    value__ = None


class ReinforcementSettings(Element, IDisposable):
    """ Provides access to project-wide reinforcement settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFabricRoundingManager(self):
        """
        GetFabricRoundingManager(self: ReinforcementSettings) -> FabricRoundingManager
        
            Returns an object for managing reinforcement rounding override settings used by 
             FabricSheetType and FabricSheet elements.
        
            Returns: The rounding manager.
        """
        pass

    def GetRebarRoundingManager(self):
        """
        GetRebarRoundingManager(self: ReinforcementSettings) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings used by 
             RebarBarTypes, Rebar and RebarInSystem elements.
        
            Returns: The rounding manager.
        """
        pass

    def GetReinforcementAbbreviationTag(self, tagType):
        """
        GetReinforcementAbbreviationTag(self: ReinforcementSettings, tagType: ReinforcementAbbreviationTagType) -> str
        
            Gets one abbreviation tag for desired ReinforcementAbbreviationTagType.
        
            tagType: Defines the type of abbreviation tag.
            Returns: Abbreviation tag value
        """
        pass

    def GetReinforcementAbbreviationTags(self, objectType):
        """
        GetReinforcementAbbreviationTags(self: ReinforcementSettings, objectType: ReinforcementAbbreviationObjectType) -> IList[ReinforcementAbbreviationTag]
        
            Gets a list of abbreviation tags for desired reinforcement object type.
        
            objectType: Defines the type of desired reinforcement object for abbreviation tags.
            Returns: An array of ReinforcementAbbreviationTag that will define all abbreviations for 
             given reinforcement object.
        """
        pass

    @staticmethod
    def GetReinforcementSettings(cda):
        """
        GetReinforcementSettings(cda: Document) -> ReinforcementSettings
        
            Obtains the ReinforcementSettings object for the specified project document.
        
            cda: A project document.
            Returns: The ReinforcementSettings object.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: ReinforcementSettings, other: ReinforcementSettings) -> bool
        
            Checks if Reinforcement Settings is equal to other
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetReinforcementAbbreviationTag(self, tagType, abbreviationTag):
        """
        SetReinforcementAbbreviationTag(self: ReinforcementSettings, tagType: ReinforcementAbbreviationTagType, abbreviationTag: str)
            Sets one abbreviation tag for desired ReinforcementAbbreviationTagType.
        
            tagType: Defines the type of abbreviation tag.
            abbreviationTag: Abbreviation tag value to set.
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

    HostStructuralRebar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Host Structural Rebar within Area and Path Reinforcement with touching AtomHostStructuralRebar.

Get: HostStructuralRebar(self: ReinforcementSettings) -> bool

Set: HostStructuralRebar(self: ReinforcementSettings) = value
"""

    NumberVaryingLengthRebarsIndividually = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this option to modify the way varying length bars are numbered (individually or as a whole).

Get: NumberVaryingLengthRebarsIndividually(self: ReinforcementSettings) -> bool

Set: NumberVaryingLengthRebarsIndividually(self: ReinforcementSettings) = value
"""

    RebarPresentationInSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default presentation mode for rebar sets, when:
   The view direction is perpendicular to the rebar normal and the rebar set is cut.The view direction is not perpendicular to the rebar normal and the view direction is not parallel to the rebar normal.

Get: RebarPresentationInSection(self: ReinforcementSettings) -> RebarPresentationMode

Set: RebarPresentationInSection(self: ReinforcementSettings) = value
"""

    RebarPresentationInView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default presentation mode for rebar sets, when the view direction is perpendicular to the rebar normal and the rebar set is not cut.

Get: RebarPresentationInView(self: ReinforcementSettings) -> RebarPresentationMode

Set: RebarPresentationInView(self: ReinforcementSettings) = value
"""

    RebarShapeDefinesEndTreatments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End Treatments are defined by Rebar Shape of Rebar element. Can be changed if document contains no rebars, area reinforcements and path reinforcements.

Get: RebarShapeDefinesEndTreatments(self: ReinforcementSettings) -> bool

Set: RebarShapeDefinesEndTreatments(self: ReinforcementSettings) = value
"""

    RebarShapeDefinesHooks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hooks are defined by Rebar Shape of Rebar element. Can be changed if document contains no rebars, area reinforcements and path reinforcements.

Get: RebarShapeDefinesHooks(self: ReinforcementSettings) -> bool

Set: RebarShapeDefinesHooks(self: ReinforcementSettings) = value
"""

    RebarVaryingLengthNumberSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unique identifier used for a bar within a variable length rebar set.

Get: RebarVaryingLengthNumberSuffix(self: ReinforcementSettings) -> str

Set: RebarVaryingLengthNumberSuffix(self: ReinforcementSettings) = value
"""



class ReleaseType(Enum, IComparable, IFormattable, IConvertible):
    """
    The release type.
    
    enum ReleaseType, values: BendingMoment (2), Fixed (0), Pinned (1), UserDefined (3)
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

    BendingMoment = None
    Fixed = None
    Pinned = None
    UserDefined = None
    value__ = None


class StickElementExtension(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Extension.
    
    enum StickElementExtension, values: BottomOrTop (0), Plane (2), ReferenceLevel (1), Varies (3)
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

    BottomOrTop = None
    Plane = None
    ReferenceLevel = None
    value__ = None
    Varies = None


class StickElementProjectionY(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Projection.
    
    enum StickElementProjectionY, values: Center (2), Left (1), LocationLine (0), Plane (4), Right (3), Varies (5)
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
    LocationLine = None
    Plane = None
    Right = None
    value__ = None
    Varies = None


class StickElementProjectionZ(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Projection.
    
    enum StickElementProjectionZ, values: Bottom (3), Center (2), LocationLine (0), Plane (4), Top (1), Varies (5)
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

    Bottom = None
    Center = None
    LocationLine = None
    Plane = None
    Top = None
    value__ = None
    Varies = None


class StirrupTieAttachmentType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated tye that represents how the Stirrup/Tie rebar is attached to the cover reference.
    
    enum StirrupTieAttachmentType, values: ExteriorFace (1), InteriorFace (0)
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

    ExteriorFace = None
    InteriorFace = None
    value__ = None


class StructuralConnectionApplyTo(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type that represents the type of structural locations to which a connection annotation may be applied.
    
    enum StructuralConnectionApplyTo, values: BeamsAndBraces (0), ColumnBase (2), ColumnTop (1), Connection (3)
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

    BeamsAndBraces = None
    ColumnBase = None
    ColumnTop = None
    Connection = None
    value__ = None


class StructuralConnectionApprovalType(ElementType, IDisposable):
    """ A type element that represents a connection approval type. """
    @staticmethod
    def Create(doc, name):
        """
        Create(doc: Document, name: str) -> StructuralConnectionApprovalType
        
            Creates a new StructuralConnectionApprovalType.
        
            name: A name for the new approval type. It must be unique within the document.
            Returns: Created connection approval type.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllStructuralConnectionApprovalTypes(cda, ids):
        """ GetAllStructuralConnectionApprovalTypes(cda: Document) -> ICollection[ElementId] """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidApprovalTypeName(doc, name):
        """
        IsValidApprovalTypeName(doc: Document, name: str) -> bool
        
            Verifies if the provided approval name is unique in the document.
            Returns: True if approval type name is unique.
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


class StructuralConnectionCodeCheckingStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all code checking status of the structural connection element.
    
    enum StructuralConnectionCodeCheckingStatus, values: CheckingFailed (2), NotCalculated (0), OkChecked (1)
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

    CheckingFailed = None
    NotCalculated = None
    OkChecked = None
    value__ = None


class StructuralConnectionHandler(Element, IDisposable):
    """ An object of Structural Connection Handler. """
    def AddElementIds(self, elemIds):
        """ AddElementIds(self: StructuralConnectionHandler, elemIds: IList[ElementId]) """
        pass

    @staticmethod
    def Create(document, idsToConnect, typeId=None):
        """
        Create(document: Document, idsToConnect: IList[ElementId]) -> StructuralConnectionHandler
        Create(document: Document, idsToConnect: IList[ElementId], typeId: ElementId) -> StructuralConnectionHandler
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetConnectedElementIds(self):
        """
        GetConnectedElementIds(self: StructuralConnectionHandler) -> IList[ElementId]
        
            Retrieves list of element ids of connected elements.
            Returns: Returns connected element ids.
        """
        pass

    def GetOrigin(self):
        """
        GetOrigin(self: StructuralConnectionHandler) -> XYZ
        
            Retrieves origin point of Structural Connection Handler element.
            Returns: The origin point of element.
        """
        pass

    def IsDetailed(self):
        """
        IsDetailed(self: StructuralConnectionHandler) -> bool
        
            Checks if Structural Connection Handler has the detailed connection style.
            Returns: True if Structural Connection Handler has the detailed connection style.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveElementIds(self, elemIds):
        """ RemoveElementIds(self: StructuralConnectionHandler, elemIds: IList[ElementId]) """
        pass

    def SetDefaultPrimaryElement(self):
        """
        SetDefaultPrimaryElement(self: StructuralConnectionHandler)
            Sets primary element in connection according to structural categories, element 
             materials and geometries.
           The steel element is set rather than an element 
             of other material.
           The priorities of the elements are set according 
             structural categories in following order: columns, framings, walls, 
             foundations, floors.
           In case of several Structural Framing elements order 
             is determined by cutting - the cutting element is set as the primary one rather 
             than element being cut.
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

    ApprovalTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves or changes approval type of the Structural Connection Handler.

Get: ApprovalTypeId(self: StructuralConnectionHandler) -> ElementId

Set: ApprovalTypeId(self: StructuralConnectionHandler) = value
"""

    CodeCheckingStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Code checking status of the structural connection.

Get: CodeCheckingStatus(self: StructuralConnectionHandler) -> StructuralConnectionCodeCheckingStatus

Set: CodeCheckingStatus(self: StructuralConnectionHandler) = value
"""

    SingleElementEndIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element end index for single element connections (0: start, 1: end).

Get: SingleElementEndIndex(self: StructuralConnectionHandler) -> int

Set: SingleElementEndIndex(self: StructuralConnectionHandler) = value
"""



class StructuralConnectionHandlerType(ElementType, IDisposable):
    """ A StructuralConnectionHandlerType is used in StructuralConnectionHandler element generation. """
    @staticmethod
    def Create(pADoc, name, guid, familyName):
        """
        Create(pADoc: Document, name: str, guid: Guid, familyName: str) -> StructuralConnectionHandlerType
        
            Creates a new StructuralConnectionHandlerType object.
        
            pADoc: The document.
            name: The type name.
            guid: Connection GUID.
            familyName: Name of system family which created type will belong to.
            Returns: The newly created instance.
        """
        pass

    @staticmethod
    def CreateDefaultStructuralConnectionHandlerType(pADoc):
        """
        CreateDefaultStructuralConnectionHandlerType(pADoc: Document) -> ElementId
        
            Creates a new StructuralConnectionHandlerType object with a default name.
        
            pADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetDefaultConnectionHandlerType(pADoc):
        """
        GetDefaultConnectionHandlerType(pADoc: Document) -> ElementId
        
            Gets a default type id for Structural Connection.
        
            pADoc: The document.
            Returns: The type id.
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

    ConnectionGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID to use for identifying connection geometry generation algorithm.

Get: ConnectionGuid(self: StructuralConnectionHandlerType) -> Guid

"""



class StructuralConnectionSettings(Element, IDisposable):
    """ Provides access to project-wide structural connections settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetStructuralConnectionSettings(document):
        """
        GetStructuralConnectionSettings(document: Document) -> StructuralConnectionSettings
        
            Obtains the StructuralConnectionSettings object for the specified project 
             document.
        
        
            document: A project document.
            Returns: The StructuralConnectionSettings object.
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

    IncludeWarningControls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property controls how Structural Connection Element is generated.
   If set to true and warnings are reported for given Element, additional yellow triangle is displayed.

Get: IncludeWarningControls(self: StructuralConnectionSettings) -> bool

Set: IncludeWarningControls(self: StructuralConnectionSettings) = value
"""



class StructuralConnectionType(ElementType, IDisposable):
    """ A type element that represents a connection symbol applied to structural members. """
    @staticmethod
    def Create(doc, applyTo, name, familySymbolId):
        """
        Create(doc: Document, applyTo: StructuralConnectionApplyTo, name: str, familySymbolId: ElementId) -> StructuralConnectionType
        
            Create a new StructuralConnectionType, allowing the specified
           annotation 
             FamilySymbol to be applied to structural members.
        
        
            applyTo: Specify which type of member this connection type can be applied to.
            name: A name for the connection type. It must be unique within the document.
            familySymbolId: The id of an annotation FamilySymbol. InvalidElementId is
           allowed. 
             Otherwise, the FamilySymbol must
           be in the category "Connection Symbols"
          
              (OST_StructConnectionSymbols) and have its "Apply
           To" parameter set to 
             match the applyTo argument.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllStructuralConnectionTypeIds(cda, ids):
        """ GetAllStructuralConnectionTypeIds(cda: Document) -> ICollection[ElementId] """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFamilySymbolId(self):
        """
        GetFamilySymbolId(self: StructuralConnectionType) -> ElementId
        
            FamilySymbol of the annotation to use for this connection type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetFamilySymbolId(self, familySymbolId):
        """
        SetFamilySymbolId(self: StructuralConnectionType, familySymbolId: ElementId)
            FamilySymbol of the annotation to use for this connection type.
        """
        pass

    @staticmethod
    def ValidFamilySymbolId(doc, applyTo, familySymbolId):
        """
        ValidFamilySymbolId(doc: Document, applyTo: StructuralConnectionApplyTo, familySymbolId: ElementId) -> bool
        
            Checks whether the family symbol id is allowed for
           
             StructuralConnectionTypes with the given value for the applyTo
           property.
        
            Returns: True if %familySymbolId% is invalidElementId; or if it is
           the id of a 
             FamilySymbol of category "Connection
           Symbols" (OST_StructConnectionSymbols) 
             with its "Apply
           To" parameter set to match the applyTo property.
           
             Returns false otherwise.
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

    ApplyTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Choose whether this connection type applies to beams and
   braces, to tops of columns, or to bases of columns.

Get: ApplyTo(self: StructuralConnectionType) -> StructuralConnectionApplyTo

"""



class StructuralFramingUtils(object):
    """ A collection of Structural Framing Utilities. """
    @staticmethod
    def AllowJoinAtEnd(familyInstance, end):
        """
        AllowJoinAtEnd(familyInstance: FamilyInstance, end: int)
            Sets the indicated end of the framing element to be allowed to join to others.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category.
            end: The index of the end (0 for the start, 1 for the end).
        """
        pass

    @staticmethod
    def CanFlipEnds(familyInstance):
        """
        CanFlipEnds(familyInstance: FamilyInstance) -> bool
        
            Determines if the ends of the given framing element can be flipped.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete.
        
            Returns: True for non-concrete line, arc or ellipse framing element, false otherwise.
        """
        pass

    @staticmethod
    def CanSetEndReference(familyInstance, end):
        """
        CanSetEndReference(familyInstance: FamilyInstance, end: int) -> bool
        
            Determines if a reference can be set for the given end of the framing element.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete and joined at the given end.
        
            end: The index of the end (0 for the start, 1 for the end).
            Returns: True if reference can be set for the given end of the framing element.
        """
        pass

    @staticmethod
    def DisallowJoinAtEnd(familyInstance, end):
        """
        DisallowJoinAtEnd(familyInstance: FamilyInstance, end: int)
            Sets the indicated end of the framing element to not be allowed to join to 
             others.
        
        
            familyInstance: The FamilyInstance, which must be of a structural framing category.
            end: The index of the end (0 for the start, 1 for the end).
        """
        pass

    @staticmethod
    def FlipEnds(familyInstance):
        """
        FlipEnds(familyInstance: FamilyInstance)
            Flips the ends of the structural framing element.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete.
        """
        pass

    @staticmethod
    def GetEndReference(familyInstance, end):
        """
        GetEndReference(familyInstance: FamilyInstance, end: int) -> Reference
        
            Returns a reference to the end of a framing element according to the setback 
             settings.
        
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete and joined.
        
            end: The index of the end (0 for the start, 1 for the end).
            Returns: The end reference.
        """
        pass

    @staticmethod
    def IsEndReferenceValid(familyInstance, end, pick):
        """
        IsEndReferenceValid(familyInstance: FamilyInstance, end: int, pick: Reference) -> bool
        
            Determines if the given reference can be set for the given end of the framing 
             element.
        
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete and joined at the given end.
        
            end: The index of the end (0 for the start, 1 for the end).
            pick: The reference to be checked against the given end of the framing element.
            Returns: True if the given reference can be set for the given end of the framing element.
        """
        pass

    @staticmethod
    def IsJoinAllowedAtEnd(familyInstance, end):
        """
        IsJoinAllowedAtEnd(familyInstance: FamilyInstance, end: int) -> bool
        
            Identifies if the indicated end of the framing element is allowed to join to 
             others.
        
        
            familyInstance: The FamilyInstance, which must be of a structural framing category.
            end: The index of the end (0 for the start, 1 for the end).
            Returns: True if it is allowed to join. False if it is disallowed.
        """
        pass

    @staticmethod
    def RemoveEndReference(familyInstance, end):
        """
        RemoveEndReference(familyInstance: FamilyInstance, end: int)
            Resets the end reference of the structural framing element.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete and joined.
        
            end: The index of the end (0 for the start, 1 for the end).
        """
        pass

    @staticmethod
    def SetEndReference(familyInstance, end, pick):
        """
        SetEndReference(familyInstance: FamilyInstance, end: int, pick: Reference)
            Sets the end reference of a framing element.
        
            familyInstance: The FamilyInstance, which must be of a structural framing category, 
             non-concrete and joined.
        
            end: The index of the end (0 for the start, 1 for the end).
            pick: The reference to set to the given end.
        """
        pass

    __all__ = [
        'AllowJoinAtEnd',
        'CanFlipEnds',
        'CanSetEndReference',
        'DisallowJoinAtEnd',
        'FlipEnds',
        'GetEndReference',
        'IsEndReferenceValid',
        'IsJoinAllowedAtEnd',
        'RemoveEndReference',
        'SetEndReference',
    ]


class StructuralInstanceUsage(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the structural usage of a family instance.
    
    enum StructuralInstanceUsage, values: Automatic (10), Brace (7), Column (2), Girder (3), HorizontalBracing (8), Joist (4), KickerBracing (9), Other (6), Purlin (5), TrussChord (11), TrussWeb (12), Undefined (0), Wall (1)
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

    Automatic = None
    Brace = None
    Column = None
    Girder = None
    HorizontalBracing = None
    Joist = None
    KickerBracing = None
    Other = None
    Purlin = None
    TrussChord = None
    TrussWeb = None
    Undefined = None
    value__ = None
    Wall = None


class StructuralInstanceUsageFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to find elements that are structural family instances (typically columns, beams or braces) of the given structural usage.
    
    StructuralInstanceUsageFilter(structuralUsage: StructuralInstanceUsage, inverted: bool)
    StructuralInstanceUsageFilter(structuralUsage: StructuralInstanceUsage)
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

    @staticmethod # known case of __new__
    def __new__(self, structuralUsage, inverted=None):
        """
        __new__(cls: type, structuralUsage: StructuralInstanceUsage, inverted: bool)
        __new__(cls: type, structuralUsage: StructuralInstanceUsage)
        """
        pass

    StructuralUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The family instance structural usage.

Get: StructuralUsage(self: StructuralInstanceUsageFilter) -> StructuralInstanceUsage

"""



class StructuralMaterialType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the structural material type.  This enum value is returned by Autodesk::Revit::DB::FamilyInstance::StructuralMaterialType.
    
    enum StructuralMaterialType, values: Aluminum (7), Concrete (2), Generic (6), Other (4), PrecastConcrete (5), Steel (1), Undefined (0), Wood (3)
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

    Aluminum = None
    Concrete = None
    Generic = None
    Other = None
    PrecastConcrete = None
    Steel = None
    Undefined = None
    value__ = None
    Wood = None


class StructuralMaterialTypeFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match family instances that have the given structural material type.
    
    StructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType, inverted: bool)
    StructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType)
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

    @staticmethod # known case of __new__
    def __new__(self, structuralMaterialType, inverted=None):
        """
        __new__(cls: type, structuralMaterialType: StructuralMaterialType, inverted: bool)
        __new__(cls: type, structuralMaterialType: StructuralMaterialType)
        """
        pass

    StructuralMaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The structural material type.

Get: StructuralMaterialType(self: StructuralMaterialTypeFilter) -> StructuralMaterialType

"""



class StructuralSectionsServiceData(object, IDisposable):
    """
    The data needed by section type server to perform type definition.
    
    StructuralSectionsServiceData(document: Document, currentElementIds: IList[ElementId])
    """
    def Dispose(self):
        """ Dispose(self: StructuralSectionsServiceData) """
        pass

    def GetCurrentElements(self):
        """
        GetCurrentElements(self: StructuralSectionsServiceData) -> IList[ElementId]
        
            Returns the list of Ids of the current elements.
            Returns: Ids of the current elements. Contains the family base element to which the 
             section shape type parameter belongs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSectionsServiceData, disposing: bool) """
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
    def __new__(self, document, currentElementIds):
        """ __new__(cls: type, document: Document, currentElementIds: IList[ElementId]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current document.

Get: Document(self: StructuralSectionsServiceData) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralSectionsServiceData) -> bool

"""



class StructuralSettings(Element, IDisposable):
    """ Provides access to project-wide structural settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetStructuralSettings(doc):
        """
        GetStructuralSettings(doc: Document) -> StructuralSettings
        
            Obtains the StructuralSettings object for the specified project document.
        
            doc: A project document.
            Returns: The StructuralSettings object.
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

    AnalyticalLinkAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for the analytical link distance.

Get: AnalyticalLinkAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalLinkAutofixTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelAutoCheckConsistency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check automatically for consistency between the analytical
   and physical models.

Get: AnalyticalModelAutoCheckConsistency(self: StructuralSettings) -> bool

Set: AnalyticalModelAutoCheckConsistency(self: StructuralSettings) = value
"""

    AnalyticalModelAutoCheckMemberSupports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check automatically for member supports.

Get: AnalyticalModelAutoCheckMemberSupports(self: StructuralSettings) -> bool

Set: AnalyticalModelAutoCheckMemberSupports(self: StructuralSettings) = value
"""

    AnalyticalModelCheckAdjustment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for analytical model distance from default location is
   larger than the tolerance defined by the property
   AnalyticalModelAdjustmentTolerance.

Get: AnalyticalModelCheckAdjustment(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckAdjustment(self: StructuralSettings) = value
"""

    AnalyticalModelCheckBeamSlabDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check the analytical model distance between beam and slab for a level.

Get: AnalyticalModelCheckBeamSlabDistance(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckBeamSlabDistance(self: StructuralSettings) = value
"""

    AnalyticalModelCheckCircularReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check member supports for circular references.

Get: AnalyticalModelCheckCircularReferences(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckCircularReferences(self: StructuralSettings) = value
"""

    AnalyticalModelCheckDiscrepancy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for distance between analytical and physical models
   greater than a tolerance defined by
   AnalyticalModelDiscrepancyTolerance.

Get: AnalyticalModelCheckDiscrepancy(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckDiscrepancy(self: StructuralSettings) = value
"""

    AnalyticalModelCheckInstability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for possible instability based on release conditions.

Get: AnalyticalModelCheckInstability(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckInstability(self: StructuralSettings) = value
"""

    AnalyticalModelCheckSupportDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check that joins in the physical model are consistent
   with proximity in the analytical model.

Get: AnalyticalModelCheckSupportDistance(self: StructuralSettings) -> bool

Set: AnalyticalModelCheckSupportDistance(self: StructuralSettings) = value
"""

    AnalyticalModelDiscrepancyTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for the analytical-to-physical model distance.

Get: AnalyticalModelDiscrepancyTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelDiscrepancyTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelHorizontalAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for horizontal auto-detect for the analytical model.

Get: AnalyticalModelHorizontalAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelHorizontalAutofixTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelSupportDistanceTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum distance between two structural elements,
   where analytical model support rules still apply.

Get: AnalyticalModelSupportDistanceTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelSupportDistanceTolerance(self: StructuralSettings) = value
"""

    AnalyticalModelVerticalAutofixTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tolerance for vertical auto-detect for the analytical model.

Get: AnalyticalModelVerticalAutofixTolerance(self: StructuralSettings) -> float

Set: AnalyticalModelVerticalAutofixTolerance(self: StructuralSettings) = value
"""

    BoundaryConditionAreaAndLineSymbolSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol spacing for boundary conditions.

Get: BoundaryConditionAreaAndLineSymbolSpacing(self: StructuralSettings) -> float

Set: BoundaryConditionAreaAndLineSymbolSpacing(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolFixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a fixed boundary condition.

Get: BoundaryConditionFamilySymbolFixed(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolFixed(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a pinned boundary condition.

Get: BoundaryConditionFamilySymbolPinned(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolPinned(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolRoller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a roller boundary condition.

Get: BoundaryConditionFamilySymbolRoller(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolRoller(self: StructuralSettings) = value
"""

    BoundaryConditionFamilySymbolUserDefined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FamilySymbol to represent a user-defined boundary condition.

Get: BoundaryConditionFamilySymbolUserDefined(self: StructuralSettings) -> ElementId

Set: BoundaryConditionFamilySymbolUserDefined(self: StructuralSettings) = value
"""

    BraceAboveSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a brace above a beam in plan view.

Get: BraceAboveSymbol(self: StructuralSettings) -> ElementId

Set: BraceAboveSymbol(self: StructuralSettings) = value
"""

    BraceBelowSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a brace below a beam in plan view.

Get: BraceBelowSymbol(self: StructuralSettings) -> ElementId

Set: BraceBelowSymbol(self: StructuralSettings) = value
"""

    BraceParallelLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance by which brace symbols in plan
   views will be offset.

Get: BraceParallelLineOffset(self: StructuralSettings) -> float

Set: BraceParallelLineOffset(self: StructuralSettings) = value
"""

    CheckAnalyticalModelAsset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to check for valid Asset within the Material of associated Physical Element.

Get: CheckAnalyticalModelAsset(self: StructuralSettings) -> bool

Set: CheckAnalyticalModelAsset(self: StructuralSettings) = value
"""

    DifferentiateAnalyticalEnds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to use a subcategory for the ends of a linear analytical model, rather than
   the main category.

Get: DifferentiateAnalyticalEnds(self: StructuralSettings) -> bool

Set: DifferentiateAnalyticalEnds(self: StructuralSettings) = value
"""

    KickerBraceSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to represent a kicker brace.

Get: KickerBraceSymbol(self: StructuralSettings) -> ElementId

Set: KickerBraceSymbol(self: StructuralSettings) = value
"""

    ShowBraceAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to show brace symbols above beams in plan views.

Get: ShowBraceAbove(self: StructuralSettings) -> bool

Set: ShowBraceAbove(self: StructuralSettings) = value
"""

    ShowBraceBelow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to show brace symbols below beams in plan views.

Get: ShowBraceBelow(self: StructuralSettings) -> bool

Set: ShowBraceBelow(self: StructuralSettings) = value
"""

    SymbolicCutbackForBeamAndTruss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all beams and trusses.

Get: SymbolicCutbackForBeamAndTruss(self: StructuralSettings) -> float

Set: SymbolicCutbackForBeamAndTruss(self: StructuralSettings) = value
"""

    SymbolicCutbackForBrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all braces.

Get: SymbolicCutbackForBrace(self: StructuralSettings) -> float

Set: SymbolicCutbackForBrace(self: StructuralSettings) = value
"""

    SymbolicCutbackForColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbolic cutback distance to be applied to all columns.

Get: SymbolicCutbackForColumn(self: StructuralSettings) -> float

Set: SymbolicCutbackForColumn(self: StructuralSettings) = value
"""



class StructuralType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the structural type of a family instance.
    
    enum StructuralType, values: Beam (1), Brace (2), Column (3), Footing (4), NonStructural (0), UnknownFraming (5)
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

    Beam = None
    Brace = None
    Column = None
    Footing = None
    NonStructural = None
    UnknownFraming = None
    value__ = None


class StructuralWallUsage(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the structural usage of a wall.
    
    enum StructuralWallUsage, values: Bearing (1), Combined (3), NonBearing (0), Shear (2)
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

    Bearing = None
    Combined = None
    NonBearing = None
    Shear = None
    value__ = None


class StructuralWallUsageFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match walls that have the given structural wall usage.
    
    StructuralWallUsageFilter(structuralWallUsage: StructuralWallUsage, inverted: bool)
    StructuralWallUsageFilter(structuralWallUsage: StructuralWallUsage)
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

    @staticmethod # known case of __new__
    def __new__(self, structuralWallUsage, inverted=None):
        """
        __new__(cls: type, structuralWallUsage: StructuralWallUsage, inverted: bool)
        __new__(cls: type, structuralWallUsage: StructuralWallUsage)
        """
        pass

    StructuralWallUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wall structural usage.

Get: StructuralWallUsage(self: StructuralWallUsageFilter) -> StructuralWallUsage

"""



class SurfaceElementExtension(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Extension.
    
    enum SurfaceElementExtension, values: BottomOrTop (0), Plane (1)
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

    BottomOrTop = None
    Plane = None
    value__ = None


class SurfaceElementProjectionZ(Enum, IComparable, IFormattable, IConvertible):
    """
    Presets for given Analytical Projection Z.
    
    enum SurfaceElementProjectionZ, values: BottomOrExterior (2), CenterOfCore (3), CenterOfElement (1), Plane (4), TopOrInterior (0)
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

    BottomOrExterior = None
    CenterOfCore = None
    CenterOfElement = None
    Plane = None
    TopOrInterior = None
    value__ = None


class TargetRebarConstraintType(Enum, IComparable, IFormattable, IConvertible):
    """
    A type used to identify the particular part of a Stirrup style rebar to which
       a Standard style rebar's handle is constrained.
    
    enum TargetRebarConstraintType, values: BarBend (5), Edge (3), EndOfBar (2), HookBend (6), OutOfPlaneExtent (4), RebarPlane (0), StartOfBar (1)
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

    BarBend = None
    Edge = None
    EndOfBar = None
    HookBend = None
    OutOfPlaneExtent = None
    RebarPlane = None
    StartOfBar = None
    value__ = None


class TranslationRotationValue(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of condition applied to the translation or rotation parameter.
    
    enum TranslationRotationValue, values: Fixed (0), Release (1), Spring (2)
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

    Fixed = None
    Release = None
    Spring = None
    value__ = None


class Truss(Element, IDisposable):
    """ Represents all kinds of Trusses. """
    def AttachChord(self, attachToElement, location, forceRemoveSketch):
        """
        AttachChord(self: Truss, attachToElement: Element, location: TrussChordLocation, forceRemoveSketch: bool)
            Attach a truss's specific chord to a specified element, the element should be a 
             roof or floor.
        
        
            attachToElement: The element to which the truss's chord will attach. The element should be a 
             roof or floor.
        
            location: The chord need to be attached.
            forceRemoveSketch: Whether to detach the original sketch if there is one.
        """
        pass

    @staticmethod
    def Create(document, trussTypeId, sketchPlaneId, curve):
        """
        Create(document: Document, trussTypeId: ElementId, sketchPlaneId: ElementId, curve: Curve) -> Truss
        
            Creates a new Truss.
        
            document: The document in which the new Truss is created.
            trussTypeId: Element id of the truss type.
            sketchPlaneId: Element id of a SketchPlane.
            curve: The curve of the truss element.
           It must be a line, must not be a vertical 
             line, and must be within the sketch plane.
        """
        pass

    def DetachChord(self, location):
        """
        DetachChord(self: Truss, location: TrussChordLocation)
            Detach a truss's specific chord from the element to which it is attached.
        
            location: The chord.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def DropTruss(truss):
        """
        DropTruss(truss: Truss)
            Drop truss Family, it will disassociate all members from the truss and delete 
             the truss.
        
        
            truss: The truss to be dropped.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetTrussMemberInfo(self, elemId):
        """
        GetTrussMemberInfo(self: Truss, elemId: ElementId) -> TrussMemberInfo
        
            Query if a given element is a member of a truss, its lock status and its usage, 
             etc.
        
        
            elemId: The querying element.
            Returns: A struct TrussMemberInfo that contains the querying element's host truss, 
             whether to lock to the truss, usage type, etc.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveProfile(self):
        """
        RemoveProfile(self: Truss)
            Remove the profile of a truss.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetProfile(self, topChords, bottomChords):
        """
        SetProfile(self: Truss, topChords: CurveArray, bottomChords: CurveArray)
            Add or modify the profile of a truss.
        
            topChords: The curves serving as top chords of the truss.
            bottomChords: The curves serving as bottom chords of the truss.
        """
        pass

    def TogglePinMember(self, elemId):
        """
        TogglePinMember(self: Truss, elemId: ElementId)
            Pin/Unpin a truss member.
        
            elemId: The member element is going to pin/unpin.
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

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all the truss curves.

Get: Curves(self: Truss) -> CurveArray

"""

    Members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all the members of truss.

Get: Members(self: Truss) -> ICollection[ElementId]

"""

    TrussType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve/set an object that represents the type of the truss.

Get: TrussType(self: Truss) -> TrussType

Set: TrussType(self: Truss) = value
"""



class TrussChordLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumerated type represents the options for the Truss Chord Location.
    
    enum TrussChordLocation, values: Bottom (0), Top (1)
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

    Bottom = None
    Top = None
    value__ = None


class TrussCurveType(Enum, IComparable, IFormattable, IConvertible):
    """
    Types of curves created in truss families.
    
    enum TrussCurveType, values: BottomChord (2), NonTrussCurve (0), TopChord (1), Web (3)
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

    BottomChord = None
    NonTrussCurve = None
    TopChord = None
    value__ = None
    Web = None


class TrussMemberInfo(object):
    """
    Provides access to the information of a truss member in Autodesk Revit.
    
    TrussMemberInfo()
    """
    hostTrussId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host truss' ElementId of the member.

Get: hostTrussId(self: TrussMemberInfo) -> ElementId

Set: hostTrussId(self: TrussMemberInfo) = value
"""

    lockedToTruss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the member is locked to the host truss.

Get: lockedToTruss(self: TrussMemberInfo) -> bool

Set: lockedToTruss(self: TrussMemberInfo) = value
"""

    memberTypeKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Kind of the member in the truss.

Get: memberTypeKey(self: TrussMemberInfo) -> TrussMemberType

Set: memberTypeKey(self: TrussMemberInfo) = value
"""



class TrussMemberType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the "kind" of a truss member.
    
    enum TrussMemberType, values: ETK_TrussBottomChord (2), ETK_TrussDiagWeb (4), ETK_TrussTopChord (1), ETK_TrussVertWeb (3), ETK_Unknown (0)
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

    ETK_TrussBottomChord = None
    ETK_TrussDiagWeb = None
    ETK_TrussTopChord = None
    ETK_TrussVertWeb = None
    ETK_Unknown = None
    value__ = None


class TrussType(FamilySymbol, IDisposable):
    """ Represents a specific type of truss. """
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


class WireDistributionDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the direction of the distribution of wires in a Fabric Sheet.
    
    enum WireDistributionDirection, values: Major (0), Minor (1)
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

    Major = None
    Minor = None
    value__ = None


class YJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    The justification of the framing element in Y.
    
    enum YJustification, values: Center (1), Left (0), Origin (2), Right (3)
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
    Origin = None
    Right = None
    value__ = None


class YZJustificationOption(Enum, IComparable, IFormattable, IConvertible):
    """
    The option for whether a framing element has independent or uniform justification on its ends.
    
    enum YZJustificationOption, values: Independent (1), Uniform (0)
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

    Independent = None
    Uniform = None
    value__ = None


class ZJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    The justification of the framing element in Z.
    
    enum ZJustification, values: Bottom (3), Center (1), Origin (2), Top (0)
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

    Bottom = None
    Center = None
    Origin = None
    Top = None
    value__ = None


# variables with complex values

