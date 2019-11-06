from System import Object
from Wms.RemotingObjects import DbObject
# encoding: utf-8
# module Wms.RemotingObjects.ErpLocking calls itself ErpLocking
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ErpLock(DbObject):
    """ ErpLock() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CurrentState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CurrentState(self: ErpLock) -> ErpLockState

Set: CurrentState(self: ErpLock) = value
"""

    CurrentStateAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: CurrentStateAsString(self: ErpLock) -> str

"""

    EntityKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EntityKey(self: ErpLock) -> str

Set: EntityKey(self: ErpLock) = value
"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EntityType(self: ErpLock) -> ErpLockEntityType

Set: EntityType(self: ErpLock) = value
"""

    EntityTypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EntityTypeAsString(self: ErpLock) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: ErpLock) -> int

Set: Id(self: ErpLock) = value
"""

    MigrateToState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MigrateToState(self: ErpLock) -> ErpLockState

Set: MigrateToState(self: ErpLock) = value
"""

    MigrateToStateAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MigrateToStateAsString(self: ErpLock) -> str

"""


    Instance = ErpLock()
    """hardcoded/returns an instance of the class"""

class ErpLockEntityType(Object):
    """ enum ErpLockEntityType, values: PurchaseOrder (1), SalesOrder (0) """
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

    PurchaseOrder = None
    SalesOrder = None
    value__ = None

    Instance = ErpLockEntityType()
    """hardcoded/returns an instance of the class"""

class ErpLockState(Object):
    """ enum ErpLockState, values: Locked (1), Unkown (0), Unlocked (2) """
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

    Locked = None
    Unkown = None
    Unlocked = None
    value__ = None

    Instance = ErpLockState()
    """hardcoded/returns an instance of the class"""

