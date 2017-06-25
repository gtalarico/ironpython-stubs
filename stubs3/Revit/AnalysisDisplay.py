# encoding: utf-8
# module Revit.AnalysisDisplay calls itself AnalysisDisplay
# from RevitNodes, Version=1.3.0.875, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AbstractAnalysisDisplay(object):
    # no doc

class FaceAnalysisDisplay(AbstractAnalysisDisplay):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


class PointAnalysisDisplay(AbstractAnalysisDisplay):
    # no doc
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


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
# Error generating skeleton for function __init__: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.


