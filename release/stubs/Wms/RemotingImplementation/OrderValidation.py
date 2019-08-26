# encoding: utf-8
# module Wms.RemotingImplementation.OrderValidation calls itself OrderValidation
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OrderValidator:
    """
    OrderValidator(orderNumber: str, orderType: OrderTypeEnum)
    OrderValidator(orderNumber: str, orderType: OrderTypeEnum, orderLines: IEnumerable[OutboundOrderLine])
    """
    def Dispose(self):
        """ Dispose(self: OrderValidator) """
        pass

    def IsOrderProcessed(self, orderLinesToValidate):
        """ IsOrderProcessed(self: OrderValidator, orderLinesToValidate: str) """
        pass

    def IsOrderValid(self):
        """ IsOrderValid(self: OrderValidator) -> OrderValidationResult """
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
    def __new__(self, orderNumber, orderType, orderLines=None):
        """
        __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum)
        __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum, orderLines: IEnumerable[OutboundOrderLine])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    OrderNumber = None
    OrderType = None
    Result = None

    Instance = OrderValidator()
    """hardcoded/returns an instance of the class"""

class OrderValidatorFactory():
    """ OrderValidatorFactory(orderNumber: str, orderType: OrderTypeEnum) """
    def Create(self):
        """ Create(self: OrderValidatorFactory) -> OrderValidator """
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderNumber, orderType):
        """ __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum) """
        pass

    Instance = OrderValidatorFactory()
    """hardcoded/returns an instance of the class"""

class PurchasOrderValidator(OrderValidator):
    """ PurchasOrderValidator(orderNumber: str, orderType: OrderTypeEnum) """
    def IsOrderValid(self):
        """ IsOrderValid(self: PurchasOrderValidator) -> OrderValidationResult """
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
    def __new__(self, orderNumber, orderType):
        """ __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum) """
        pass

    OrderNumber = None
    OrderType = None
    Result = None

    Instance = PurchasOrderValidator()
    """hardcoded/returns an instance of the class"""

class ReplenishmentOrderValidator(OrderValidator):
    """ ReplenishmentOrderValidator(orderNumber: str, orderType: OrderTypeEnum) """
    def IsOrderValid(self):
        """ IsOrderValid(self: ReplenishmentOrderValidator) -> OrderValidationResult """
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
    def __new__(self, orderNumber, orderType):
        """ __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum) """
        pass

    OrderNumber = None
    OrderType = None
    Result = None

    Instance = ReplenishmentOrderValidator()
    """hardcoded/returns an instance of the class"""

class RmaOrderValidator(OrderValidator):
    """ RmaOrderValidator(orderNumber: str, orderType: OrderTypeEnum) """
    def IsOrderValid(self):
        """ IsOrderValid(self: RmaOrderValidator) -> OrderValidationResult """
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
    def __new__(self, orderNumber, orderType):
        """ __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum) """
        pass

    OrderNumber = None
    OrderType = None
    Result = None

    Instance = RmaOrderValidator()
    """hardcoded/returns an instance of the class"""

class SalesOrderValidator(OrderValidator):
    """ SalesOrderValidator(orderNumber: str, orderType: OrderTypeEnum) """
    def IsOrderValid(self):
        """ IsOrderValid(self: SalesOrderValidator) -> OrderValidationResult """
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
    def __new__(self, orderNumber, orderType):
        """ __new__(cls: type, orderNumber: str, orderType: OrderTypeEnum) """
        pass

    OrderNumber = None
    OrderType = None
    Result = None

    Instance = SalesOrderValidator()
    """hardcoded/returns an instance of the class"""

