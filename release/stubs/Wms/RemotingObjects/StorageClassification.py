from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.StorageClassification calls itself StorageClassification
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class LocationClassification(DbObject):
    """ LocationClassification() """
    Instance = LocationClassification
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AisleFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AisleFrom(self: LocationClassification) -> str

Set: AisleFrom(self: LocationClassification) = value
"""

    AisleTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AisleTo(self: LocationClassification) -> str

Set: AisleTo(self: LocationClassification) = value
"""

    BlockFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BlockFrom(self: LocationClassification) -> str

Set: BlockFrom(self: LocationClassification) = value
"""

    BlockTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: BlockTo(self: LocationClassification) -> str

Set: BlockTo(self: LocationClassification) = value
"""

    ColumnFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ColumnFrom(self: LocationClassification) -> str

Set: ColumnFrom(self: LocationClassification) = value
"""

    ColumnTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ColumnTo(self: LocationClassification) -> str

Set: ColumnTo(self: LocationClassification) = value
"""

    HasScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasScript(self: LocationClassification) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: LocationClassification) -> int

Set: Id(self: LocationClassification) = value
"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Script(self: LocationClassification) -> str

Set: Script(self: LocationClassification) = value
"""

    ShelveFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShelveFrom(self: LocationClassification) -> str

Set: ShelveFrom(self: LocationClassification) = value
"""

    ShelveTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShelveTo(self: LocationClassification) -> str

Set: ShelveTo(self: LocationClassification) = value
"""

    StorageAssignmentClassificationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StorageAssignmentClassificationId(self: LocationClassification) -> int

Set: StorageAssignmentClassificationId(self: LocationClassification) = value
"""

    UseScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: UseScript(self: LocationClassification) -> bool

Set: UseScript(self: LocationClassification) = value
"""

    WarehouseLayoutSettingsId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: WarehouseLayoutSettingsId(self: LocationClassification) -> int

Set: WarehouseLayoutSettingsId(self: LocationClassification) = value
"""



class LocationClassifications(FindableList):
    """ LocationClassifications() """
    Instance = LocationClassifications
    """hardcoded/returns an instance of the class"""
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = None
    ValueMember = None


class LocationClassificationsFilter():
    """
    LocationClassificationsFilter()
    LocationClassificationsFilter(storageAssignmentClassificationId: int)
    """
    Instance = LocationClassificationsFilter
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, storageAssignmentClassificationId=None):
        """
        __new__(cls: type)
        __new__(cls: type, storageAssignmentClassificationId: int)
        """
        pass

    StorageAssignmentClassificationId = None


class StorageAssignmentClassification(DbObject):
    """ StorageAssignmentClassification() """
    Instance = StorageAssignmentClassification
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Code(self: StorageAssignmentClassification) -> str

Set: Code(self: StorageAssignmentClassification) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: StorageAssignmentClassification) -> int

Set: Id(self: StorageAssignmentClassification) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: StorageAssignmentClassification) -> str

Set: Name(self: StorageAssignmentClassification) = value
"""

    SortOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SortOrder(self: StorageAssignmentClassification) -> int

Set: SortOrder(self: StorageAssignmentClassification) = value
"""



class StorageAssignmentClassifications(FindableList):
    """ StorageAssignmentClassifications() """
    Instance = StorageAssignmentClassifications
    """hardcoded/returns an instance of the class"""
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = None
    ValueMember = None


class StorageAssignmentClassificationsFilter():
    """
    StorageAssignmentClassificationsFilter()
    StorageAssignmentClassificationsFilter(id: int)
    StorageAssignmentClassificationsFilter(id: int, searchText: str)
    StorageAssignmentClassificationsFilter(searchText: str)
    """
    Instance = StorageAssignmentClassificationsFilter
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, id: int)
        __new__(cls: type, id: int, searchText: str)
        __new__(cls: type, searchText: str)
        """
        pass

    Id = None
    SearchText = None


