from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.OrderValidation calls itself OrderValidation
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Detail():
    """ Detail() """
    def AddColumn(self, header, description):
        """ AddColumn(self: Detail, header: str, description: str) """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: Detail) -> List[DetailColumn]

Set: Columns(self: Detail) = value
"""


    Instance = Detail()
    """hardcoded/returns an instance of the class"""

class DetailColumn():
    """ DetailColumn() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: DetailColumn) -> str

Set: Description(self: DetailColumn) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Header(self: DetailColumn) -> str

Set: Header(self: DetailColumn) = value
"""


    Instance = DetailColumn()
    """hardcoded/returns an instance of the class"""

class Details():
    """ Details() """
    def ToString(self):
        """ ToString(self: Details) -> str """
        pass

    AdditionalDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AdditionalDetails(self: Details) -> List[Detail]

Set: AdditionalDetails(self: Details) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: Details) -> str

Set: Description(self: Details) = value
"""


    Instance = Details()
    """hardcoded/returns an instance of the class"""

class OrderValidationArgs():
    """ OrderValidationArgs() """
    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Order(self: OrderValidationArgs) -> OutboundOrder

Set: Order(self: OrderValidationArgs) = value
"""

    OrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderLines(self: OrderValidationArgs) -> IEnumerable[OutboundOrderLine]

Set: OrderLines(self: OrderValidationArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderNumber(self: OrderValidationArgs) -> str

Set: OrderNumber(self: OrderValidationArgs) = value
"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: OrderType(self: OrderValidationArgs) -> OrderTypeEnum

Set: OrderType(self: OrderValidationArgs) = value
"""

    ReturnFirstErrorOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ReturnFirstErrorOnly(self: OrderValidationArgs) -> bool

Set: ReturnFirstErrorOnly(self: OrderValidationArgs) = value
"""


    Instance = OrderValidationArgs()
    """hardcoded/returns an instance of the class"""

class OrderValidationCheck():
    """ OrderValidationCheck() """
    def ToString(self, includeDetails=None):
        """
        ToString(self: OrderValidationCheck) -> str
        ToString(self: OrderValidationCheck, includeDetails: bool) -> str
        """
        pass

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Group(self: OrderValidationCheck) -> str

Set: Group(self: OrderValidationCheck) = value
"""

    HasMessageDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasMessageDetails(self: OrderValidationCheck) -> bool

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Message(self: OrderValidationCheck) -> str

Set: Message(self: OrderValidationCheck) = value
"""

    MessageDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MessageDetails(self: OrderValidationCheck) -> Details

Set: MessageDetails(self: OrderValidationCheck) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: OrderValidationCheck) -> str

Set: Name(self: OrderValidationCheck) = value
"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Success(self: OrderValidationCheck) -> bool

Set: Success(self: OrderValidationCheck) = value
"""


    Instance = OrderValidationCheck()
    """hardcoded/returns an instance of the class"""

class OrderValidationResult(FindableList):
    """ OrderValidationResult() """
    def AddResult(self, name, message, *__args):
        """ AddResult(self: OrderValidationResult, name: str, message: str, success: bool, group: str)AddResult(self: OrderValidationResult, name: str, message: str, messageDetails: str, success: bool, group: str) """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ChecksAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ChecksAsString(self: OrderValidationResult) -> str

"""

    ErpName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ErpName(self: OrderValidationResult) -> str

Set: ErpName(self: OrderValidationResult) = value
"""

    ErrorsAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ErrorsAsString(self: OrderValidationResult) -> str

"""

    HasErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasErrors(self: OrderValidationResult) -> bool

"""

    IsOrderValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsOrderValid(self: OrderValidationResult) -> bool

Set: IsOrderValid(self: OrderValidationResult) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Message(self: OrderValidationResult) -> str

Set: Message(self: OrderValidationResult) = value
"""

    MessageDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MessageDetails(self: OrderValidationResult) -> str

Set: MessageDetails(self: OrderValidationResult) = value
"""


    Instance = OrderValidationResult()
    """hardcoded/returns an instance of the class"""

