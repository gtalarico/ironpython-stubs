# encoding: utf-8
# module Revit.AnalysisDisplay calls itself AnalysisDisplay
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AbstractAnalysisDisplay(object, IDisposable):
    """
    Superclass for all Revit Analysis Display types
                
                Note: We're using the user facing name from Revit (Analysis Display), rather than the same name that the Revit API
                uses (Spatial Field)
    """
    def GetAnalysisResultSchemaIndex(self, *args): #cannot find CLR method
        """
        GetAnalysisResultSchemaIndex(self: AbstractAnalysisDisplay, resultsSchemaName: str, resultsDescription: str, unitType: Type) -> int
        
            Get the AnalysisResultsSchemaIndex for the SpatialFieldManager
        """
        pass

    def GetElementAndPrimitiveIdFromTrace(self, *args): #cannot find CLR method
        """
        GetElementAndPrimitiveIdFromTrace(self: AbstractAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]]
        
            Set the SpatialFieldManager PrimitiveId from Thread Local Storage
        """
        pass

    def GetSpatialFieldManagerFromView(self, *args): #cannot find CLR method
        """
        GetSpatialFieldManagerFromView(view: View, numValuesPerAnalysisPoint: UInt32) -> SpatialFieldManager
        
            Get the SpatialFieldManager for a particular view.  This is a singleton for 
             every view.  Note that the 
                    number of values per analysis point is 
             ignored if the SpatialFieldManager has already been obtained
                    for 
             this view.  This field cannot be mutated once the SpatialFieldManager is set 
             for a partiular 
                    view.
        """
        pass

    def InternalSetSpatialFieldManager(self, *args): #cannot find CLR method
        """
        InternalSetSpatialFieldManager(self: AbstractAnalysisDisplay, manager: SpatialFieldManager)
            Set the SpatialFieldManager
        """
        pass

    def InternalSetSpatialPrimitiveIds(self, *args): #cannot find CLR method
        """ InternalSetSpatialPrimitiveIds(self: AbstractAnalysisDisplay, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdsForTrace(self, *args): #cannot find CLR method
        """
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay)
            Set the current SpatialFieldManager and PrimitiveId in Thread Local Storage
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int])
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A reference to the current document

"""

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SpatialFieldManager governing this SpatialFieldPrimitive

"""



class FaceAnalysisDisplay(AbstractAnalysisDisplay, IDisposable):
    """ A Revit Point Analysis Display """
    @staticmethod
    def ByViewAndFaceAnalysisData(view, data, name, description, unitType):
        """
        ByViewAndFaceAnalysisData(view: View, data: SurfaceData, name: str, description: str, unitType: Type) -> FaceAnalysisDisplay
        
            Show a colored Face Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            data: A collection of SurfaceData objects.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: A FaceAnalysisDisplay object.
        """
        pass

    @staticmethod
    def ByViewFacePointsAndValues(view, surface, sampleLocations, samples, name, description, unitType):
        """
        ByViewFacePointsAndValues(view: View, surface: Surface, sampleLocations: Array[UV], samples: Array[float], name: str, description: str, unitType: Type) -> FaceAnalysisDisplay
        
            Show a colored Face Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            sampleLocations: The locations at which you want to create analysis values.
            samples: The analysis values at the given locations.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: A FaceAnalysisDisplay object.
        """
        pass

    def GetAnalysisResultSchemaIndex(self, *args): #cannot find CLR method
        """
        GetAnalysisResultSchemaIndex(self: AbstractAnalysisDisplay, resultsSchemaName: str, resultsDescription: str, unitType: Type) -> int
        
            Get the AnalysisResultsSchemaIndex for the SpatialFieldManager
        """
        pass

    def GetElementAndPrimitiveIdFromTrace(self, *args): #cannot find CLR method
        """
        GetElementAndPrimitiveIdFromTrace(self: AbstractAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]]
        
            Set the SpatialFieldManager PrimitiveId from Thread Local Storage
        """
        pass

    def InternalSetSpatialFieldManager(self, *args): #cannot find CLR method
        """
        InternalSetSpatialFieldManager(self: AbstractAnalysisDisplay, manager: SpatialFieldManager)
            Set the SpatialFieldManager
        """
        pass

    def InternalSetSpatialPrimitiveIds(self, *args): #cannot find CLR method
        """ InternalSetSpatialPrimitiveIds(self: AbstractAnalysisDisplay, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdsForTrace(self, *args): #cannot find CLR method
        """
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay)
            Set the current SpatialFieldManager and PrimitiveId in Thread Local Storage
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int])
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, view: View, data: ISurfaceData[UV, float], resultsName: str, description: str, unitType: Type) """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SpatialFieldManager governing this SpatialFieldPrimitive

"""



class PointAnalysisDisplay(AbstractAnalysisDisplay, IDisposable):
    """ A Revit Point Analysis Display """
    @staticmethod
    def ByViewAndPointAnalysisData(view, data, name, description, unitType):
        """
        ByViewAndPointAnalysisData(view: View, data: PointData, name: str, description: str, unitType: Type) -> PointAnalysisDisplay
        
            Show a colored Point Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            data: A list of PointData objects.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: An PointAnalysisDisplay object.
        """
        pass

    @staticmethod
    def ByViewPointsAndValues(view, sampleLocations, samples, name, description, unitType):
        """
        ByViewPointsAndValues(view: View, sampleLocations: Array[Point], samples: Array[float], name: str, description: str, unitType: Type) -> PointAnalysisDisplay
        
            Show a colored Point Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            sampleLocations: The locations at which you want to create analysis values.
            samples: The analysis values at the given locations.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: An PointAnalysisDisplay object.
        """
        pass

    def GetAnalysisResultSchemaIndex(self, *args): #cannot find CLR method
        """
        GetAnalysisResultSchemaIndex(self: AbstractAnalysisDisplay, resultsSchemaName: str, resultsDescription: str, unitType: Type) -> int
        
            Get the AnalysisResultsSchemaIndex for the SpatialFieldManager
        """
        pass

    def GetElementAndPrimitiveIdFromTrace(self, *args): #cannot find CLR method
        """
        GetElementAndPrimitiveIdFromTrace(self: AbstractAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]]
        
            Set the SpatialFieldManager PrimitiveId from Thread Local Storage
        """
        pass

    def GetElementAndPrimitiveIdListFromTrace(self, *args): #cannot find CLR method
        """ GetElementAndPrimitiveIdListFromTrace(self: PointAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]] """
        pass

    def InternalSetSpatialFieldManager(self, *args): #cannot find CLR method
        """
        InternalSetSpatialFieldManager(self: AbstractAnalysisDisplay, manager: SpatialFieldManager)
            Set the SpatialFieldManager
        """
        pass

    def InternalSetSpatialPrimitiveIds(self, *args): #cannot find CLR method
        """ InternalSetSpatialPrimitiveIds(self: AbstractAnalysisDisplay, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdListTrace(self, *args): #cannot find CLR method
        """ SetElementAndPrimitiveIdListTrace(self: PointAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdsForTrace(self, *args): #cannot find CLR method
        """
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay)
            Set the current SpatialFieldManager and PrimitiveId in Thread Local Storage
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int])
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

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SpatialFieldManager governing this SpatialFieldPrimitive

"""



class SpmPrimitiveIdListPair(object, ISerializable):
    """
    SpmPrimitiveIdListPair()
    SpmPrimitiveIdListPair(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: SpmPrimitiveIdListPair, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    PrimitiveIDs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimitiveIDs(self: SpmPrimitiveIdListPair) -> List[int]

Set: PrimitiveIDs(self: SpmPrimitiveIdListPair) = value
"""

    SpatialFieldManagerID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialFieldManagerID(self: SpmPrimitiveIdListPair) -> int

Set: SpatialFieldManagerID(self: SpmPrimitiveIdListPair) = value
"""



class SpmPrimitiveIdPair(object, ISerializable):
    """
    Hold a pair of element ID of SpatialFieldManager and primitive ID to
                support serialization.
    
    SpmPrimitiveIdPair()
    SpmPrimitiveIdPair(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: SpmPrimitiveIdPair, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimitiveIds(self: SpmPrimitiveIdPair) -> List[int]

Set: PrimitiveIds(self: SpmPrimitiveIdPair) = value
"""

    SpatialFieldManagerID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialFieldManagerID(self: SpmPrimitiveIdPair) -> int

Set: SpatialFieldManagerID(self: SpmPrimitiveIdPair) = value
"""



class VectorAnalysisDisplay(AbstractAnalysisDisplay, IDisposable):
    """ A Revit Vector Analysis Display """
    @staticmethod
    def ByViewAndVectorAnalysisData(view, data, name, description, unitType):
        """
        ByViewAndVectorAnalysisData(view: View, data: VectorData, name: str, description: str, unitType: Type) -> VectorAnalysisDisplay
        
            Show a Vector Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            data: A list of VectorData objects.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: A VectorAnalysisDisplay object.
        """
        pass

    @staticmethod
    def ByViewPointsAndVectorValues(view, sampleLocations, samples, name, description, unitType):
        """
        ByViewPointsAndVectorValues(view: View, sampleLocations: Array[Point], samples: Array[Vector], name: str, description: str, unitType: Type) -> VectorAnalysisDisplay
        
            Show a Vector Analysis Display in the Revit view.
        
            view: The view into which you want to draw the analysis results.
            samples: The analysis values at the given locations.
            name: An optional analysis results name to show on the results legend.
            description: An optional analysis results description to show on the results legend.
            unitType: An optional Unit type to provide conversions in the analysis results.
            Returns: A VectorAnalysisDisplay object.
        """
        pass

    def GetAnalysisResultSchemaIndex(self, *args): #cannot find CLR method
        """
        GetAnalysisResultSchemaIndex(self: AbstractAnalysisDisplay, resultsSchemaName: str, resultsDescription: str, unitType: Type) -> int
        
            Get the AnalysisResultsSchemaIndex for the SpatialFieldManager
        """
        pass

    def GetElementAndPrimitiveIdFromTrace(self, *args): #cannot find CLR method
        """
        GetElementAndPrimitiveIdFromTrace(self: AbstractAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]]
        
            Set the SpatialFieldManager PrimitiveId from Thread Local Storage
        """
        pass

    def InternalSetSpatialFieldManager(self, *args): #cannot find CLR method
        """
        InternalSetSpatialFieldManager(self: AbstractAnalysisDisplay, manager: SpatialFieldManager)
            Set the SpatialFieldManager
        """
        pass

    def InternalSetSpatialPrimitiveIds(self, *args): #cannot find CLR method
        """ InternalSetSpatialPrimitiveIds(self: AbstractAnalysisDisplay, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdsForTrace(self, *args): #cannot find CLR method
        """
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay)
            Set the current SpatialFieldManager and PrimitiveId in Thread Local Storage
        SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int])
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

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SpatialFieldManager governing this SpatialFieldPrimitive

"""



