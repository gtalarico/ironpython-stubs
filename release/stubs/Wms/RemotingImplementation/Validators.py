# encoding: utf-8
# module Wms.RemotingImplementation.Validators calls itself Validators
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IReallocationValidator:
    # no doc
    def Validate(self, itemCode, warehouseCode, locationCode):
        """ Validate(self: IReallocationValidator, itemCode: str, warehouseCode: str, locationCode: str) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: IReallocationValidator) -> str

Set: ErrorMessage(self: IReallocationValidator) = value
"""


    Instance = IReallocationValidator()
    """hardcoded/returns an instance of the class"""

class ReAllocateValidator:
    """ ReAllocateValidator(stockManager: IStockManager) """
    def Validate(self, itemCode, warehouseCode, locationCode):
        """ Validate(self: ReAllocateValidator, itemCode: str, warehouseCode: str, locationCode: str) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stockManager):
        """ __new__(cls: type, stockManager: IStockManager) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: ReAllocateValidator) -> str

Set: ErrorMessage(self: ReAllocateValidator) = value
"""


    Instance = ReAllocateValidator()
    """hardcoded/returns an instance of the class"""

class TransferWarehouseValidator:
    """ TransferWarehouseValidator() """
    def Validate(self, itemCode, warehouseCode, locationCode):
        """ Validate(self: TransferWarehouseValidator, itemCode: str, warehouseCode: str, locationCode: str) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: TransferWarehouseValidator) -> str

Set: ErrorMessage(self: TransferWarehouseValidator) = value
"""


    Instance = TransferWarehouseValidator()
    """hardcoded/returns an instance of the class"""

