# encoding: utf-8
# module Wms.RemotingImplementation.FlatFileGeneration.FixedLength.Models calls itself Models
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BosDepartment():
    """ BosDepartment() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: BosDepartment) -> str

Set: Code(self: BosDepartment) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: BosDepartment) -> str

Set: Description(self: BosDepartment) = value
"""


    Instance = BosDepartment()
    """hardcoded/returns an instance of the class"""

class BosKanbanBarcode():
    """ BosKanbanBarcode() """
    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: BosKanbanBarcode) -> str

Set: Barcode(self: BosKanbanBarcode) = value
"""

    PositionProduct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionProduct(self: BosKanbanBarcode) -> int

Set: PositionProduct(self: BosKanbanBarcode) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: BosKanbanBarcode) -> int

Set: Quantity(self: BosKanbanBarcode) = value
"""


    Instance = BosKanbanBarcode()
    """hardcoded/returns an instance of the class"""

class BosProduct():
    """ BosProduct() """
    def CreateAlternativeIndex(self, code):
        """ CreateAlternativeIndex(self: BosProduct, code: str) -> BosProduct """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: BosProduct) -> str

Set: Code(self: BosProduct) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: BosProduct) -> str

Set: Description(self: BosProduct) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: BosProduct) -> int

Set: Index(self: BosProduct) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: BosProduct) -> str

Set: UnitCode(self: BosProduct) = value
"""


    Instance = BosProduct()
    """hardcoded/returns an instance of the class"""

class BosKanbanProduct(BosProduct):
    """ BosKanbanProduct() """
    Instance = BosKanbanProduct()
    """hardcoded/returns an instance of the class"""

class BosKanbanReplenishmentLine():
    """ BosKanbanReplenishmentLine() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: BosKanbanReplenishmentLine) -> str

Set: Code(self: BosKanbanReplenishmentLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: BosKanbanReplenishmentLine) -> int

Set: Quantity(self: BosKanbanReplenishmentLine) = value
"""

    TimestampUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimestampUtc(self: BosKanbanReplenishmentLine) -> str

Set: TimestampUtc(self: BosKanbanReplenishmentLine) = value
"""

    UserCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserCode(self: BosKanbanReplenishmentLine) -> str

Set: UserCode(self: BosKanbanReplenishmentLine) = value
"""


    Instance = BosKanbanReplenishmentLine()
    """hardcoded/returns an instance of the class"""

class BosMeta():
    """ BosMeta() """
    AppVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppVersion(self: BosMeta) -> str

Set: AppVersion(self: BosMeta) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: BosMeta) -> str

"""


    Instance = BosMeta()
    """hardcoded/returns an instance of the class"""

class BosProductIndex(BosProduct):
    """ BosProductIndex() """
    Instance = BosProductIndex()
    """hardcoded/returns an instance of the class"""

class BosProductReplenishmentLine():
    """ BosProductReplenishmentLine() """
    DepartmentCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepartmentCode(self: BosProductReplenishmentLine) -> str

Set: DepartmentCode(self: BosProductReplenishmentLine) = value
"""

    ProductCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProductCode(self: BosProductReplenishmentLine) -> str

Set: ProductCode(self: BosProductReplenishmentLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: BosProductReplenishmentLine) -> int

Set: Quantity(self: BosProductReplenishmentLine) = value
"""

    TimestampUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimestampUtc(self: BosProductReplenishmentLine) -> str

Set: TimestampUtc(self: BosProductReplenishmentLine) = value
"""

    UserCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserCode(self: BosProductReplenishmentLine) -> str

Set: UserCode(self: BosProductReplenishmentLine) = value
"""


    Instance = BosProductReplenishmentLine()
    """hardcoded/returns an instance of the class"""

