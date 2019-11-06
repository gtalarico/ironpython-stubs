from Wms.RemotingObjects import FindableList
# encoding: utf-8
# module Wms.RemotingObjects.WarehouseLayout calls itself WarehouseLayout
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class WarehouseLayout():
    """ WarehouseLayout() """
    Aisle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Aisle(self: WarehouseLayout) -> str

Set: Aisle(self: WarehouseLayout) = value
"""

    Block = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Block(self: WarehouseLayout) -> str

Set: Block(self: WarehouseLayout) = value
"""

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Column(self: WarehouseLayout) -> str

Set: Column(self: WarehouseLayout) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Location(self: WarehouseLayout) -> Location

Set: Location(self: WarehouseLayout) = value
"""

    OriginalValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OriginalValue(self: WarehouseLayout) -> str

Set: OriginalValue(self: WarehouseLayout) = value
"""

    Shelve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Shelve(self: WarehouseLayout) -> str

Set: Shelve(self: WarehouseLayout) = value
"""


    Instance = WarehouseLayout()
    """hardcoded/returns an instance of the class"""

class WarehouseLayouts(FindableList):
    """ WarehouseLayouts() """
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

    Instance = WarehouseLayouts()
    """hardcoded/returns an instance of the class"""

class WarehouseLayoutSettingFilter():
    """
    WarehouseLayoutSettingFilter()
    WarehouseLayoutSettingFilter(id: int)
    WarehouseLayoutSettingFilter(id: int, searchText: str)
    WarehouseLayoutSettingFilter(searchText: str)
    """
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

    Instance = WarehouseLayoutSettingFilter()
    """hardcoded/returns an instance of the class"""

class WarehouseLayoutSettings(FindableList):
    """ WarehouseLayoutSettings() """
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

    DisplayMember = 'WarehouseCode'
    ValueMember = 'Id'

    Instance = WarehouseLayoutSettings()
    """hardcoded/returns an instance of the class"""

# variables with complex values

