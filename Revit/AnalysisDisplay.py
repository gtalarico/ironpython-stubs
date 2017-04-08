# encoding: utf-8
# module Revit.AnalysisDisplay calls itself AnalysisDisplay
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AbstractAnalysisDisplay(object):
    # no doc
    def GetAnalysisResultSchemaIndex(self, *args): #cannot find CLR method
        """ GetAnalysisResultSchemaIndex(self: AbstractAnalysisDisplay, resultsSchemaName: str, resultsDescription: str, unitType: Type) -> int """
        pass

    def GetElementAndPrimitiveIdFromTrace(self, *args): #cannot find CLR method
        """ GetElementAndPrimitiveIdFromTrace(self: AbstractAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]] """
        pass

    def GetSpatialFieldManagerFromView(self, *args): #cannot find CLR method
        """ GetSpatialFieldManagerFromView(view: View, numValuesPerAnalysisPoint: UInt32) -> SpatialFieldManager """
        pass

    def InternalSetSpatialFieldManager(self, *args): #cannot find CLR method
        """ InternalSetSpatialFieldManager(self: AbstractAnalysisDisplay, manager: SpatialFieldManager) """
        pass

    def InternalSetSpatialPrimitiveIds(self, *args): #cannot find CLR method
        """ InternalSetSpatialPrimitiveIds(self: AbstractAnalysisDisplay, primitiveIds: List[int]) """
        pass

    def SetElementAndPrimitiveIdsForTrace(self, *args): #cannot find CLR method
        """ SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay)SetElementAndPrimitiveIdsForTrace(self: AbstractAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int]) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class FaceAnalysisDisplay(AbstractAnalysisDisplay):
    # no doc
    @staticmethod
    def ByViewAndFaceAnalysisData(view, data, name, description, unitType):
        """ ByViewAndFaceAnalysisData(view: View, data: SurfaceData, name: str, description: str, unitType: Type) -> FaceAnalysisDisplay """
        pass

    @staticmethod
    def ByViewFacePointsAndValues(view, surface, sampleLocations, samples, name, description, unitType):
        """ ByViewFacePointsAndValues(view: View, surface: Surface, sampleLocations: Array[UV], samples: Array[float], name: str, description: str, unitType: Type) -> FaceAnalysisDisplay """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, view: View, data: ISurfaceData[UV, float], resultsName: str, description: str, unitType: Type) """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PointAnalysisDisplay(AbstractAnalysisDisplay):
    # no doc
    @staticmethod
    def ByViewAndPointAnalysisData(view, data, name, description, unitType):
        """ ByViewAndPointAnalysisData(view: View, data: PointData, name: str, description: str, unitType: Type) -> PointAnalysisDisplay """
        pass

    @staticmethod
    def ByViewPointsAndValues(view, sampleLocations, samples, name, description, unitType):
        """ ByViewPointsAndValues(view: View, sampleLocations: Array[Point], samples: Array[float], name: str, description: str, unitType: Type) -> PointAnalysisDisplay """
        pass

    def GetElementAndPrimitiveIdListFromTrace(self, *args): #cannot find CLR method
        """ GetElementAndPrimitiveIdListFromTrace(self: PointAnalysisDisplay) -> Tuple[SpatialFieldManager, List[int]] """
        pass

    def SetElementAndPrimitiveIdListTrace(self, *args): #cannot find CLR method
        """ SetElementAndPrimitiveIdListTrace(self: PointAnalysisDisplay, manager: SpatialFieldManager, primitiveIds: List[int]) """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SpmPrimitiveIdListPair(object):
    """
    SpmPrimitiveIdListPair()
    SpmPrimitiveIdListPair(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: SpmPrimitiveIdListPair, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    PrimitiveIDs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimitiveIDs(self: SpmPrimitiveIdListPair) -> List[int]

Set: PrimitiveIDs(self: SpmPrimitiveIdListPair) = value
"""

    SpatialFieldManagerID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialFieldManagerID(self: SpmPrimitiveIdListPair) -> int

Set: SpatialFieldManagerID(self: SpmPrimitiveIdListPair) = value
"""



class SpmPrimitiveIdPair(object):
    """
    SpmPrimitiveIdPair()
    SpmPrimitiveIdPair(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: SpmPrimitiveIdPair, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimitiveIds(self: SpmPrimitiveIdPair) -> List[int]

Set: PrimitiveIds(self: SpmPrimitiveIdPair) = value
"""

    SpatialFieldManagerID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialFieldManagerID(self: SpmPrimitiveIdPair) -> int

Set: SpatialFieldManagerID(self: SpmPrimitiveIdPair) = value
"""



class VectorAnalysisDisplay(AbstractAnalysisDisplay):
    # no doc
    @staticmethod
    def ByViewAndVectorAnalysisData(view, data, name, description, unitType):
        """ ByViewAndVectorAnalysisData(view: View, data: VectorData, name: str, description: str, unitType: Type) -> VectorAnalysisDisplay """
        pass

    @staticmethod
    def ByViewPointsAndVectorValues(view, sampleLocations, samples, name, description, unitType):
        """ ByViewPointsAndVectorValues(view: View, sampleLocations: Array[Point], samples: Array[Vector], name: str, description: str, unitType: Type) -> VectorAnalysisDisplay """
        pass

    PrimitiveIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpatialFieldManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



