from System import *
# encoding: utf-8
# module Wms.RemotingImplementation.DefaultLocation calls itself DefaultLocation
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DefaultLocationCacheDTO():
    """ DefaultLocationCacheDTO() """
    Instance = DefaultLocationCacheDTO
    """hardcoded/returns an instance of the class"""
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: DefaultLocationCacheDTO) -> str

Set: ItemCode(self: DefaultLocationCacheDTO) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: DefaultLocationCacheDTO) -> str

Set: LocationCode(self: DefaultLocationCacheDTO) = value
"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: DefaultLocationCacheDTO) -> IEnumerable[object]

Set: Objects(self: DefaultLocationCacheDTO) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: DefaultLocationCacheDTO) -> str

Set: WarehouseCode(self: DefaultLocationCacheDTO) = value
"""



class DefaultLocationCacheUpdater():
    """ DefaultLocationCacheUpdater() """
    Instance = DefaultLocationCacheUpdater
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def Update(updateCacheDto):
        """ Update(updateCacheDto: DefaultLocationCacheDTO) """
        pass


class DefaultLocationHelper(MarshalByRefObject):
    """ DefaultLocationHelper() """
    Instance = DefaultLocationHelper
    """hardcoded/returns an instance of the class"""
    def GetDefaultItemLocationsByItemCode(self, itemCode):
        """ GetDefaultItemLocationsByItemCode(self: DefaultLocationHelper, itemCode: str) -> ResultObject[FindableList[WarehouseItemLocation]] """
        pass

    def GetItemLocationsByItemCode(self, itemCode, filter, defaultLocationsOnly):
        """ GetItemLocationsByItemCode(self: DefaultLocationHelper, itemCode: str, filter: str, defaultLocationsOnly: bool) -> ResultObject[FindableList[WarehouseItemLocation]] """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: DefaultLocationHelper) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting 
             boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def TransferFromDefaultItemLocation(self, item):
        """ TransferFromDefaultItemLocation(self: DefaultLocationHelper, item: WarehouseTransferItem) -> bool """
        pass

    def UpdateCache(self, types, itemCode, locationCode, warehouseCode):
        """ UpdateCache(self: DefaultLocationHelper, types: List[Type], itemCode: str, locationCode: str, warehouseCode: str) """
        pass

    def UpdateDefaultItemLocation(self, dfObject):
        """ UpdateDefaultItemLocation(self: DefaultLocationHelper, dfObject: DataFlowObject[UpdateItemDefaultLocationArgs]) -> DataFlowObject[UpdateItemDefaultLocationArgs] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


