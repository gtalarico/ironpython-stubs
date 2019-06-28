# encoding: utf-8
# module Wms.RemotingObjects.Barcodes calls itself Barcodes
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BarcodeStructure:
    """ BarcodeStructure() """
    @staticmethod
    def Parse(match, definition, replacedValues):
        """ Parse(match: Match, definition: BarcodeStructureDefinition) -> (BarcodeStructure, str) """
        pass

    ApplicationIdentifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationIdentifiers(self: BarcodeStructure) -> SerializableDictionary[str, str]

Set: ApplicationIdentifiers(self: BarcodeStructure) = value
"""

    Batch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Batch(self: BarcodeStructure) -> str

Set: Batch(self: BarcodeStructure) = value
"""

    BestBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BestBefore(self: BarcodeStructure) -> DateTime

Set: BestBefore(self: BarcodeStructure) = value
"""

    HasQuantityInBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasQuantityInBarcode(self: BarcodeStructure) -> bool

"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: BarcodeStructure) -> str

Set: ItemCode(self: BarcodeStructure) = value
"""

    ItemInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemInfo(self: BarcodeStructure) -> ItemInfo

Set: ItemInfo(self: BarcodeStructure) = value
"""

    ItemReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemReference(self: BarcodeStructure) -> str

Set: ItemReference(self: BarcodeStructure) = value
"""

    LicensePlate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlate(self: BarcodeStructure) -> str

Set: LicensePlate(self: BarcodeStructure) = value
"""

    LicensePlateInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateInfo(self: BarcodeStructure) -> LicensePlateBarcodeStructureInfo

Set: LicensePlateInfo(self: BarcodeStructure) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: BarcodeStructure) -> str

Set: Location(self: BarcodeStructure) = value
"""

    MatchedWithScanOf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchedWithScanOf(self: BarcodeStructure) -> ExpectScanOfEnum

Set: MatchedWithScanOf(self: BarcodeStructure) = value
"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Order(self: BarcodeStructure) -> str

Set: Order(self: BarcodeStructure) = value
"""

    Product = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Product(self: BarcodeStructure) -> str

Set: Product(self: BarcodeStructure) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: BarcodeStructure) -> Decimal

Set: Quantity(self: BarcodeStructure) = value
"""

    Serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Serial(self: BarcodeStructure) -> BarcodeStructureSerials

Set: Serial(self: BarcodeStructure) = value
"""



class BarcodeStructureDefinition:
    """ BarcodeStructureDefinition() """
    def Clone(self):
        """ Clone(self: BarcodeStructureDefinition) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: BarcodeStructureDefinition) -> bool

Set: Active(self: BarcodeStructureDefinition) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: BarcodeStructureDefinition) -> str

Set: Description(self: BarcodeStructureDefinition) = value
"""

    HasScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasScript(self: BarcodeStructureDefinition) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BarcodeStructureDefinition) -> int

Set: Id(self: BarcodeStructureDefinition) = value
"""

    ParseInstructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParseInstructions(self: BarcodeStructureDefinition) -> str

Set: ParseInstructions(self: BarcodeStructureDefinition) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: BarcodeStructureDefinition) -> int

Set: Priority(self: BarcodeStructureDefinition) = value
"""

    RegularExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegularExpression(self: BarcodeStructureDefinition) -> str

Set: RegularExpression(self: BarcodeStructureDefinition) = value
"""

    ReplaceInstructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplaceInstructions(self: BarcodeStructureDefinition) -> str

Set: ReplaceInstructions(self: BarcodeStructureDefinition) = value
"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Script(self: BarcodeStructureDefinition) -> str

Set: Script(self: BarcodeStructureDefinition) = value
"""

    System = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: System(self: BarcodeStructureDefinition) -> bool

Set: System(self: BarcodeStructureDefinition) = value
"""

    UseScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseScript(self: BarcodeStructureDefinition) -> bool

Set: UseScript(self: BarcodeStructureDefinition) = value
"""



class BarcodeStructureDefinitionFilter:
    """
    BarcodeStructureDefinitionFilter()
    BarcodeStructureDefinitionFilter(id: int)
    BarcodeStructureDefinitionFilter(id: int, searchText: str)
    BarcodeStructureDefinitionFilter(searchText: str)
    BarcodeStructureDefinitionFilter(active: Nullable[bool])
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, id: int)
        __new__(cls: type, id: int, searchText: str)
        __new__(cls: type, searchText: str)
        __new__(cls: type, active: Nullable[bool])
        """
        pass

    Active = None
    Id = None
    SearchText = None


class BarcodeStructureDefinitions:
    """ BarcodeStructureDefinitions() """
    def Clone(self):
        """ Clone(self: BarcodeStructureDefinitions) -> object """
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

    TotalRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRows(self: BarcodeStructureDefinitions) -> Int64

Set: TotalRows(self: BarcodeStructureDefinitions) = value
"""


    DisplayMember = 'Description'
    ValueMember = 'Id'


class BarcodeStructureResultEnum:
    """ enum (flags) BarcodeStructureResultEnum, values: InputRequired (1), NoInputRequired (2), NoMatchFound (4), None (0) """
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

    InputRequired = None
    NoInputRequired = None
    NoMatchFound = None
    None_ =None
    value__ = None


class BarcodeStructureSerials:
    """
    BarcodeStructureSerials()
    BarcodeStructureSerials(list: IList[str])
    """
    def Equals(self, *__args):
        """
        Equals(self: BarcodeStructureSerials, other: BarcodeStructureSerials) -> bool
        Equals(self: BarcodeStructureSerials, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: BarcodeStructureSerials) -> int """
        pass

    def ToItemIdentifications(self):
        """ ToItemIdentifications(self: BarcodeStructureSerials) -> ItemIdentifications """
        pass

    def ToString(self):
        """ ToString(self: BarcodeStructureSerials) -> str """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[str], item: str) -> bool
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, list=None):
        """
        __new__(cls: type)
        __new__(cls: type, list: IList[str])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""



class BarcodeType:
    """ BarcodeType() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: BarcodeType) -> str

Set: Description(self: BarcodeType) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BarcodeType) -> int

Set: Id(self: BarcodeType) = value
"""

    MainGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainGroup(self: BarcodeType) -> str

Set: MainGroup(self: BarcodeType) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BarcodeType) -> str

Set: Name(self: BarcodeType) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: BarcodeType) -> str

Set: Type(self: BarcodeType) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: BarcodeType) -> str

Set: Value(self: BarcodeType) = value
"""



class BarcodeTypes:
    """ BarcodeTypes() """
    def ToString(self):
        """ ToString(self: BarcodeTypes) -> str """
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

    def __str__(self, *args): #cannot find CLR method
        pass


class ExpectScanOfEnum:
    """ enum (flags) ExpectScanOfEnum, values: Batch (4), Colli (128), GS1 (256), LicensePlate (64), Location (16), Order (32), Product (1), Quantity (8), Raw (512), Serial (2) """
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

    Batch = None
    Colli = None
    GS1 = None
    LicensePlate = None
    Location = None
    Order = None
    Product = None
    Quantity = None
    Raw = None
    Serial = None
    value__ = None


class GeneratedBarcode:
    """ GeneratedBarcode(barcode: str) """
    def ToBarcode(self, includeApplicationIdentifier=None):
        """
        ToBarcode(self: GeneratedBarcode) -> str
        ToBarcode(self: GeneratedBarcode, includeApplicationIdentifier: bool) -> str
        """
        pass

    def ToReadableCode(self, includeApplicationIdentifier=None):
        """
        ToReadableCode(self: GeneratedBarcode) -> str
        ToReadableCode(self: GeneratedBarcode, includeApplicationIdentifier: bool) -> str
        """
        pass

    def ToString(self):
        """ ToString(self: GeneratedBarcode) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, barcode):
        """ __new__(cls: type, barcode: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IGeneratedBarcode:
    # no doc
    def ToBarcode(self, includeApplicationIdentifier=None):
        """
        ToBarcode(self: IGeneratedBarcode) -> str
        ToBarcode(self: IGeneratedBarcode, includeApplicationIdentifier: bool) -> str
        """
        pass

    def ToReadableCode(self, includeApplicationIdentifier=None):
        """
        ToReadableCode(self: IGeneratedBarcode) -> str
        ToReadableCode(self: IGeneratedBarcode, includeApplicationIdentifier: bool) -> str
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


# variables with complex values

