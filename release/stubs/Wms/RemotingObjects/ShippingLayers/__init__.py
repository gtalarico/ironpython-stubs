# encoding: utf-8
# module Wms.RemotingObjects.ShippingLayers calls itself ShippingLayers
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Address:
    """ Address() """
    def Clone(self):
        """ Clone(self: Address) -> object """
        pass

    def CopyFrom(self, from_):
        """ CopyFrom(self: Address, from: Address) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Address1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address1(self: Address) -> str

Set: Address1(self: Address) = value
"""

    Address2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address2(self: Address) -> str

Set: Address2(self: Address) = value
"""

    Address3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address3(self: Address) -> str

Set: Address3(self: Address) = value
"""

    City = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: City(self: Address) -> str

Set: City(self: Address) = value
"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: Address) -> str

Set: CountryCode(self: Address) = value
"""

    CountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryName(self: Address) -> str

Set: CountryName(self: Address) = value
"""

    CustomFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomFields(self: Address) -> SerializableDictionary[str, object]

Set: CustomFields(self: Address) = value
"""

    DeliveryBeginDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryBeginDateTime(self: Address) -> DateTime

Set: DeliveryBeginDateTime(self: Address) = value
"""

    DeliveryEndDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryEndDateTime(self: Address) -> DateTime

Set: DeliveryEndDateTime(self: Address) = value
"""

    Email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Email(self: Address) -> str

Set: Email(self: Address) = value
"""

    EoriNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EoriNumber(self: Address) -> str

Set: EoriNumber(self: Address) = value
"""

    FullAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullAddress(self: Address) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Address) -> str

Set: Name(self: Address) = value
"""

    Name2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name2(self: Address) -> str

Set: Name2(self: Address) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: Address) -> str

Set: PhoneNumber(self: Address) = value
"""

    PickupDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickupDateTime(self: Address) -> DateTime

Set: PickupDateTime(self: Address) = value
"""

    StateCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateCode(self: Address) -> str

Set: StateCode(self: Address) = value
"""

    ZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZipCode(self: Address) -> str

Set: ZipCode(self: Address) = value
"""



class AddTransportPackageArgs:
    """ AddTransportPackageArgs() """
    BoxIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoxIds(self: AddTransportPackageArgs) -> List[str]

"""

    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: AddTransportPackageArgs) -> CacheKey

Set: CacheKey(self: AddTransportPackageArgs) = value
"""

    NumberOfPackages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPackages(self: AddTransportPackageArgs) -> int

Set: NumberOfPackages(self: AddTransportPackageArgs) = value
"""

    OuterReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterReference(self: AddTransportPackageArgs) -> str

Set: OuterReference(self: AddTransportPackageArgs) = value
"""

    Preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preset(self: AddTransportPackageArgs) -> ColliPreset

Set: Preset(self: AddTransportPackageArgs) = value
"""

    RegisterBoxIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegisterBoxIds(self: AddTransportPackageArgs) -> bool

Set: RegisterBoxIds(self: AddTransportPackageArgs) = value
"""



class Charge:
    """
    Charge()
    Charge(amount: Decimal, currencyCode: str, description: str)
    Charge(amount: Decimal, salesAmount: Decimal, currencyCode: str, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, amount=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, amount: Decimal, currencyCode: str, description: str)
        __new__(cls: type, amount: Decimal, salesAmount: Decimal, currencyCode: str, description: str)
        """
        pass

    Amount = None
    CurrencyCode = None
    Description = None
    Empty = None
    SalesAmount = None


class Charges:
    """ Charges() """
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

    Empty = None


class ColliPreset:
    """ ColliPreset() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: ColliPreset) -> bool

Set: Active(self: ColliPreset) = value
"""

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ColliPreset) -> str

Set: Barcode(self: ColliPreset) = value
"""

    ColliSpecificationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColliSpecificationCode(self: ColliPreset) -> str

Set: ColliSpecificationCode(self: ColliPreset) = value
"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: ColliPreset) -> str

Set: CreatedBy(self: ColliPreset) = value
"""

    CreatedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOn(self: ColliPreset) -> DateTime

Set: CreatedOn(self: ColliPreset) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: ColliPreset) -> Decimal

Set: Height(self: ColliPreset) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ColliPreset) -> int

Set: Id(self: ColliPreset) = value
"""

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefault(self: ColliPreset) -> bool

Set: IsDefault(self: ColliPreset) = value
"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: ColliPreset) -> Item

Set: Item(self: ColliPreset) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ColliPreset) -> str

Set: ItemCode(self: ColliPreset) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: ColliPreset) -> Decimal

Set: Length(self: ColliPreset) = value
"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: ColliPreset) -> str

Set: ModifiedBy(self: ColliPreset) = value
"""

    ModifiedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedOn(self: ColliPreset) -> DateTime

Set: ModifiedOn(self: ColliPreset) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ColliPreset) -> str

Set: Name(self: ColliPreset) = value
"""

    StockRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockRegistration(self: ColliPreset) -> StockRegistrationForColliEnum

Set: StockRegistration(self: ColliPreset) = value
"""

    StockRegistrationAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockRegistrationAsString(self: ColliPreset) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ColliPreset) -> PackageType

Set: Type(self: ColliPreset) = value
"""

    TypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeAsString(self: ColliPreset) -> str

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: ColliPreset) -> Decimal

Set: Weight(self: ColliPreset) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: ColliPreset) -> Decimal

Set: Width(self: ColliPreset) = value
"""



class ColliPresets:
    """
    ColliPresets()
    ColliPresets(items: Array[ColliPreset])
    """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ColliPreset]) -> ColliPresets """
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

    @staticmethod # known case of __new__
    def __new__(self, items=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: Array[ColliPreset])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Name'
    ValueMember = 'Id'


class Countries:
    """ Countries() """
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

    DisplayMember = 'Name'
    ValueMember = 'Code'


class Country:
    """
    Country()
    Country(code: str, name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, code=None, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, code: str, name: str)
        """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Country) -> str

Set: Code(self: Country) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Country) -> str

Set: Name(self: Country) = value
"""



class DangerousItem:
    """ DangerousItem() """
    def Clone(self):
        """ Clone(self: DangerousItem) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: DangerousItem) -> str

Set: Code(self: DangerousItem) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: DangerousItem) -> str

Set: Description(self: DangerousItem) = value
"""

    FlashPointDegree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlashPointDegree(self: DangerousItem) -> Decimal

Set: FlashPointDegree(self: DangerousItem) = value
"""

    GrossWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossWeight(self: DangerousItem) -> Decimal

Set: GrossWeight(self: DangerousItem) = value
"""

    Instruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Instruction(self: DangerousItem) -> str

Set: Instruction(self: DangerousItem) = value
"""

    LimitedQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitedQuantity(self: DangerousItem) -> str

Set: LimitedQuantity(self: DangerousItem) = value
"""

    LimitedQuantityPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitedQuantityPoints(self: DangerousItem) -> int

Set: LimitedQuantityPoints(self: DangerousItem) = value
"""

    MarkingIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkingIdentifier(self: DangerousItem) -> str

Set: MarkingIdentifier(self: DangerousItem) = value
"""

    Measurements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Measurements(self: DangerousItem) -> Dimensions

Set: Measurements(self: DangerousItem) = value
"""

    NetWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetWeight(self: DangerousItem) -> Decimal

Set: NetWeight(self: DangerousItem) = value
"""

    PackingClassificiation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackingClassificiation(self: DangerousItem) -> str

Set: PackingClassificiation(self: DangerousItem) = value
"""

    PackingGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackingGroup(self: DangerousItem) -> str

Set: PackingGroup(self: DangerousItem) = value
"""

    PackingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackingType(self: DangerousItem) -> str

Set: PackingType(self: DangerousItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: DangerousItem) -> Decimal

Set: Quantity(self: DangerousItem) = value
"""

    TunnelCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TunnelCode(self: DangerousItem) -> str

Set: TunnelCode(self: DangerousItem) = value
"""

    UndgCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndgCode(self: DangerousItem) -> str

Set: UndgCode(self: DangerousItem) = value
"""

    UndgSubCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndgSubCode(self: DangerousItem) -> str

Set: UndgSubCode(self: DangerousItem) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: DangerousItem) -> str

Set: UnitCode(self: DangerousItem) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: DangerousItem) -> Decimal

Set: Volume(self: DangerousItem) = value
"""



class DangerousItems:
    """
    DangerousItems()
    DangerousItems(items: IEnumerable[DangerousItem])
    """
    def Clone(self):
        """ Clone(self: DangerousItems) -> object """
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

    @staticmethod # known case of __new__
    def __new__(self, items=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: IEnumerable[DangerousItem])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class Dimensions:
    """
    Dimensions(length: Decimal, width: Decimal, height: Decimal)
    Dimensions()
    Dimensions(dimensions: str)
    """
    def CompareTo(self, other):
        """ CompareTo(self: Dimensions, other: Dimensions) -> int """
        pass

    def CopyTo(self, destination):
        """ CopyTo(self: Dimensions, destination: Dimensions) """
        pass

    def Equals(self, obj):
        """ Equals(self: Dimensions, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Dimensions) -> int """
        pass

    def IsValid(self):
        """ IsValid(self: Dimensions) -> bool """
        pass

    def ToDimensionObjectWhereLengthIsLongest(self):
        """ ToDimensionObjectWhereLengthIsLongest(self: Dimensions) -> Dimensions """
        pass

    def ToString(self):
        """ ToString(self: Dimensions) -> str """
        pass

    def ToVolume(self):
        """ ToVolume(self: Dimensions) -> Decimal """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, length: Decimal, width: Decimal, height: Decimal)
        __new__(cls: type)
        __new__(cls: type, dimensions: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(dim1: Dimensions, dim2: Dimensions) -> Dimensions """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(dim1: Dimensions, dim2: Dimensions) -> Dimensions """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Dimensions) -> Decimal

Set: Height(self: Dimensions) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Dimensions) -> Decimal

Set: Length(self: Dimensions) = value
"""

    UnitOfMeasurement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitOfMeasurement(self: Dimensions) -> str

Set: UnitOfMeasurement(self: Dimensions) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Dimensions) -> Decimal

Set: Width(self: Dimensions) = value
"""


    Empty = None


class ExportDetails:
    """ ExportDetails() """
    def Clone(self):
        """ Clone(self: ExportDetails) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CountryOfOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryOfOrigin(self: ExportDetails) -> str

Set: CountryOfOrigin(self: ExportDetails) = value
"""

    HsCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HsCode(self: ExportDetails) -> str

Set: HsCode(self: ExportDetails) = value
"""

    HsCodeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HsCodeDescription(self: ExportDetails) -> str

Set: HsCodeDescription(self: ExportDetails) = value
"""

    ReasonOfExport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReasonOfExport(self: ExportDetails) -> str

Set: ReasonOfExport(self: ExportDetails) = value
"""



class HistoryShipment:
    """ HistoryShipment() """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: HistoryShipment) -> str

Set: Address(self: HistoryShipment) = value
"""

    Address2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address2(self: HistoryShipment) -> str

Set: Address2(self: HistoryShipment) = value
"""

    Address3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address3(self: HistoryShipment) -> str

Set: Address3(self: HistoryShipment) = value
"""

    Canceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Canceled(self: HistoryShipment) -> bool

Set: Canceled(self: HistoryShipment) = value
"""

    City = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: City(self: HistoryShipment) -> str

Set: City(self: HistoryShipment) = value
"""

    Colli = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colli(self: HistoryShipment) -> int

Set: Colli(self: HistoryShipment) = value
"""

    CountryAndCity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryAndCity(self: HistoryShipment) -> str

"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: HistoryShipment) -> str

Set: CountryCode(self: HistoryShipment) = value
"""

    CountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryName(self: HistoryShipment) -> str

Set: CountryName(self: HistoryShipment) = value
"""

    DeliveryBeginDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryBeginDateTime(self: HistoryShipment) -> DateTime

Set: DeliveryBeginDateTime(self: HistoryShipment) = value
"""

    DeliveryEndDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryEndDateTime(self: HistoryShipment) -> DateTime

Set: DeliveryEndDateTime(self: HistoryShipment) = value
"""

    Email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Email(self: HistoryShipment) -> str

Set: Email(self: HistoryShipment) = value
"""

    HasAttachments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasAttachments(self: HistoryShipment) -> bool

Set: HasAttachments(self: HistoryShipment) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: HistoryShipment) -> int

Set: Id(self: HistoryShipment) = value
"""

    IsCod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCod(self: HistoryShipment) -> bool

Set: IsCod(self: HistoryShipment) = value
"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: HistoryShipment) -> str

Set: ModifiedBy(self: HistoryShipment) = value
"""

    ModifiedOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedOn(self: HistoryShipment) -> DateTime

Set: ModifiedOn(self: HistoryShipment) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HistoryShipment) -> str

Set: Name(self: HistoryShipment) = value
"""

    Name2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name2(self: HistoryShipment) -> str

Set: Name2(self: HistoryShipment) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: HistoryShipment) -> str

Set: Notes(self: HistoryShipment) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: HistoryShipment) -> str

Set: PhoneNumber(self: HistoryShipment) = value
"""

    PickupDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickupDateTime(self: HistoryShipment) -> DateTime

Set: PickupDateTime(self: HistoryShipment) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: HistoryShipment) -> str

Set: Reference(self: HistoryShipment) = value
"""

    ShipperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperId(self: HistoryShipment) -> str

Set: ShipperId(self: HistoryShipment) = value
"""

    ShipperServiceLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperServiceLevelId(self: HistoryShipment) -> str

Set: ShipperServiceLevelId(self: HistoryShipment) = value
"""

    ShipperServiceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperServiceName(self: HistoryShipment) -> str

Set: ShipperServiceName(self: HistoryShipment) = value
"""

    StateCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateCode(self: HistoryShipment) -> str

Set: StateCode(self: HistoryShipment) = value
"""

    TotalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalWeight(self: HistoryShipment) -> Decimal

Set: TotalWeight(self: HistoryShipment) = value
"""

    ZipCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZipCode(self: HistoryShipment) -> str

Set: ZipCode(self: HistoryShipment) = value
"""



class HistoryShipmentFilter:
    """ HistoryShipmentFilter() """
    SearchString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchString(self: HistoryShipmentFilter) -> str

Set: SearchString(self: HistoryShipmentFilter) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: HistoryShipmentFilter) -> str

Set: YourReference(self: HistoryShipmentFilter) = value
"""



class HistoryShipmentLine:
    """ HistoryShipmentLine() """
    ColliPresetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColliPresetName(self: HistoryShipmentLine) -> str

Set: ColliPresetName(self: HistoryShipmentLine) = value
"""

    CustomerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerReference(self: HistoryShipmentLine) -> str

Set: CustomerReference(self: HistoryShipmentLine) = value
"""

    DateOfDelivery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOfDelivery(self: HistoryShipmentLine) -> DateTime

Set: DateOfDelivery(self: HistoryShipmentLine) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: HistoryShipmentLine) -> str

Set: Description(self: HistoryShipmentLine) = value
"""

    InnerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerReference(self: HistoryShipmentLine) -> str

Set: InnerReference(self: HistoryShipmentLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: HistoryShipmentLine) -> bool

Set: IsBatchNumberItem(self: HistoryShipmentLine) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: HistoryShipmentLine) -> bool

Set: IsSerialNumberItem(self: HistoryShipmentLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: HistoryShipmentLine) -> str

Set: ItemCode(self: HistoryShipmentLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: HistoryShipmentLine) -> str

Set: ItemDescription(self: HistoryShipmentLine) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: HistoryShipmentLine) -> int

Set: LineNumber(self: HistoryShipmentLine) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: HistoryShipmentLine) -> str

Set: OrderNumber(self: HistoryShipmentLine) = value
"""

    OutboundOrdersPk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutboundOrdersPk(self: HistoryShipmentLine) -> int

Set: OutboundOrdersPk(self: HistoryShipmentLine) = value
"""

    PackageDimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageDimensions(self: HistoryShipmentLine) -> str

Set: PackageDimensions(self: HistoryShipmentLine) = value
"""

    PackageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageNumber(self: HistoryShipmentLine) -> str

Set: PackageNumber(self: HistoryShipmentLine) = value
"""

    PackageTrackingNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageTrackingNumber(self: HistoryShipmentLine) -> str

Set: PackageTrackingNumber(self: HistoryShipmentLine) = value
"""

    PackageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageType(self: HistoryShipmentLine) -> str

Set: PackageType(self: HistoryShipmentLine) = value
"""

    PackageVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageVolume(self: HistoryShipmentLine) -> Decimal

Set: PackageVolume(self: HistoryShipmentLine) = value
"""

    PackageWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageWeight(self: HistoryShipmentLine) -> Decimal

Set: PackageWeight(self: HistoryShipmentLine) = value
"""

    QuantityDelivered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityDelivered(self: HistoryShipmentLine) -> Decimal

Set: QuantityDelivered(self: HistoryShipmentLine) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOrdered(self: HistoryShipmentLine) -> Decimal

Set: QuantityOrdered(self: HistoryShipmentLine) = value
"""

    ShipmentPackagePk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentPackagePk(self: HistoryShipmentLine) -> int

Set: ShipmentPackagePk(self: HistoryShipmentLine) = value
"""

    ShipmentPk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentPk(self: HistoryShipmentLine) -> int

Set: ShipmentPk(self: HistoryShipmentLine) = value
"""

    SSCC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSCC(self: HistoryShipmentLine) -> str

Set: SSCC(self: HistoryShipmentLine) = value
"""



class HistoryShipmentLines:
    """
    HistoryShipmentLines()
    HistoryShipmentLines(collection: IEnumerable[HistoryShipmentLine])
    """
    @staticmethod
    def FromIEnumerable(collection):
        """ FromIEnumerable(collection: IEnumerable[HistoryShipmentLine]) -> HistoryShipmentLines """
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

    @staticmethod # known case of __new__
    def __new__(self, collection=None):
        """
        __new__(cls: type)
        __new__(cls: type, collection: IEnumerable[HistoryShipmentLine])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: HistoryShipmentLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: HistoryShipmentLines) -> bool

"""


    DisplayMember = 'ItemDescription'
    ValueMember = 'ItemCode'


class HistoryShipments:
    """ HistoryShipments() """
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

    Total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Total(self: HistoryShipments) -> Int64

Set: Total(self: HistoryShipments) = value
"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: HistoryShipments) -> Int64

Set: TotalRowsMatched(self: HistoryShipments) = value
"""


    DisplayMember = None
    ValueMember = 'Id'


class IService:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IService) -> str

"""

    ExtraCharges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtraCharges(self: IService) -> Charges

Set: ExtraCharges(self: IService) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: IService) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IService) -> str

"""

    TotalCharge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalCharge(self: IService) -> Charge

Set: TotalCharge(self: IService) = value
"""

    TransportationCharge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportationCharge(self: IService) -> Charge

Set: TransportationCharge(self: IService) = value
"""



class IShipper:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ColliSpecificationCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColliSpecificationCodes(self: IShipper) -> Array[str]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IShipper) -> str

"""

    DimensionMandatory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionMandatory(self: IShipper) -> bool

"""

    Logo48 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Logo48(self: IShipper) -> Bitmap

"""

    Logo64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Logo64(self: IShipper) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IShipper) -> str

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: IShipper) -> str

"""



class LogSink:
    """ LogSink() """
    @staticmethod
    def Write(message, type=None):
        """ Write(message: str, type: LogSinkMessageTypes)Write(message: str) """
        pass

    LogSinkMessage = None
    OnLogSinkMessage = None


class LogSinkMessageTypes:
    """ enum LogSinkMessageTypes, values: Debug (2), Error (0), UserInfo (1) """
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

    Debug = None
    Error = None
    UserInfo = None
    value__ = None


class MobileService:
    """
    MobileService()
    MobileService(original: IService)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, original=None):
        """
        __new__(cls: type)
        __new__(cls: type, original: IService)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MobileService) -> str

"""

    DisplayCharge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayCharge(self: MobileService) -> str

"""

    ExtraCharges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtraCharges(self: MobileService) -> Charges

Set: ExtraCharges(self: MobileService) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: MobileService) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MobileService) -> str

"""

    TotalCharge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalCharge(self: MobileService) -> Charge

Set: TotalCharge(self: MobileService) = value
"""

    TransportationCharge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportationCharge(self: MobileService) -> Charge

Set: TransportationCharge(self: MobileService) = value
"""



class MobileShipper:
    """
    MobileShipper(source: IShipper)
    MobileShipper()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None):
        """
        __new__(cls: type, source: IShipper)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColliSpecificationCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColliSpecificationCodes(self: MobileShipper) -> Array[str]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MobileShipper) -> str

"""

    DimensionMandatory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionMandatory(self: MobileShipper) -> bool

"""

    Logo48 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Logo48(self: MobileShipper) -> Bitmap

"""

    Logo64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Logo64(self: MobileShipper) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MobileShipper) -> str

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: MobileShipper) -> str

"""



class OutboundOrderItem:
    """
    OutboundOrderItem()
    OutboundOrderItem(orderNumber: str, boxGuid: Guid, itemCode: str, quantity: Decimal)
    OutboundOrderItem(orderNumber: str, boxGuid: Guid, itemCode: str, itemIdentificationNumber: str, quantity: Decimal)
    """
    def GetHashCode(self):
        """ GetHashCode(self: OutboundOrderItem) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderNumber=None, boxGuid=None, itemCode=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, orderNumber: str, boxGuid: Guid, itemCode: str, quantity: Decimal)
        __new__(cls: type, orderNumber: str, boxGuid: Guid, itemCode: str, itemIdentificationNumber: str, quantity: Decimal)
        """
        pass

    BoxGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoxGuid(self: OutboundOrderItem) -> Guid

Set: BoxGuid(self: OutboundOrderItem) = value
"""

    HistoryIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryIds(self: OutboundOrderItem) -> Dictionary[int, Decimal]

Set: HistoryIds(self: OutboundOrderItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: OutboundOrderItem) -> str

Set: ItemCode(self: OutboundOrderItem) = value
"""

    ItemIdentificationNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentificationNumber(self: OutboundOrderItem) -> str

Set: ItemIdentificationNumber(self: OutboundOrderItem) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: OutboundOrderItem) -> str

Set: OrderNumber(self: OutboundOrderItem) = value
"""

    PackingSlipNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackingSlipNumber(self: OutboundOrderItem) -> str

Set: PackingSlipNumber(self: OutboundOrderItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: OutboundOrderItem) -> Decimal

Set: Quantity(self: OutboundOrderItem) = value
"""

    QuantityOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOriginal(self: OutboundOrderItem) -> Decimal

Set: QuantityOriginal(self: OutboundOrderItem) = value
"""



class OutboundOrderItems:
    """
    OutboundOrderItems()
    OutboundOrderItems(outboundOrderItems: OutboundOrderItems)
    """
    def AddOrUpdate(self, *__args):
        """ AddOrUpdate(self: OutboundOrderItems, outboundOrderItem: OutboundOrderItem)AddOrUpdate(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, quantity: Decimal)AddOrUpdate(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, itemIdentificationNumber: str, quantity: Decimal) """
        pass

    def Clone(self):
        """ Clone(self: OutboundOrderItems) -> object """
        pass

    def Decrease(self, *__args):
        """ Decrease(self: OutboundOrderItems, outboundOrderItem: OutboundOrderItem)Decrease(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, quantity: Decimal)Decrease(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, itemIdentificationNumber: str, quantity: Decimal) """
        pass

    def DecreaseOrRemove(self, *__args):
        """ DecreaseOrRemove(self: OutboundOrderItems, outboundOrderItem: OutboundOrderItem)DecreaseOrRemove(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, quantity: Decimal)DecreaseOrRemove(self: OutboundOrderItems, orderNumber: str, boxGuid: Guid, itemCode: str, itemIdentificationNumber: str, quantity: Decimal) """
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

    @staticmethod # known case of __new__
    def __new__(self, outboundOrderItems=None):
        """
        __new__(cls: type)
        __new__(cls: type, outboundOrderItems: OutboundOrderItems)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class OutboundOrdersFilter:
    """ OutboundOrdersFilter() """
    BoxNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoxNumber(self: OutboundOrdersFilter) -> str

Set: BoxNumber(self: OutboundOrdersFilter) = value
"""

    SearchString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchString(self: OutboundOrdersFilter) -> str

Set: SearchString(self: OutboundOrdersFilter) = value
"""



class Packages:
    """ Packages() """
    def GetTotalWeight(self):
        """ GetTotalWeight(self: Packages) -> Decimal """
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

    Empty = None


class PackageType:
    """ enum PackageType, values: Box (1), Document (0), Pallet (2) """
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

    Box = None
    Document = None
    Pallet = None
    value__ = None


class PackingSlipLine:
    """ PackingSlipLine() """
    def Clone(self):
        """ Clone(self: PackingSlipLine) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AssemblyInstructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyInstructions(self: PackingSlipLine) -> str

Set: AssemblyInstructions(self: PackingSlipLine) = value
"""

    Composition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Composition(self: PackingSlipLine) -> str

Set: Composition(self: PackingSlipLine) = value
"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Currency(self: PackingSlipLine) -> str

Set: Currency(self: PackingSlipLine) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PackingSlipLine) -> str

Set: Description(self: PackingSlipLine) = value
"""

    ExportDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportDetails(self: PackingSlipLine) -> ExportDetails

Set: ExportDetails(self: PackingSlipLine) = value
"""

    GrossWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossWeight(self: PackingSlipLine) -> Decimal

Set: GrossWeight(self: PackingSlipLine) = value
"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GTINCode(self: PackingSlipLine) -> str

Set: GTINCode(self: PackingSlipLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: PackingSlipLine) -> bool

Set: IsBatchNumberItem(self: PackingSlipLine) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: PackingSlipLine) -> bool

Set: IsSerialNumberItem(self: PackingSlipLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: PackingSlipLine) -> str

Set: ItemCode(self: PackingSlipLine) = value
"""

    ItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentifications(self: PackingSlipLine) -> List[ItemIdentificationBase]

Set: ItemIdentifications(self: PackingSlipLine) = value
"""

    NettoWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NettoWeight(self: PackingSlipLine) -> Decimal

Set: NettoWeight(self: PackingSlipLine) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: PackingSlipLine) -> str

Set: Number(self: PackingSlipLine) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: PackingSlipLine) -> str

Set: OrderNumber(self: PackingSlipLine) = value
"""

    Proforma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Proforma(self: PackingSlipLine) -> Proforma

Set: Proforma(self: PackingSlipLine) = value
"""

    Quality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quality(self: PackingSlipLine) -> str

Set: Quality(self: PackingSlipLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: PackingSlipLine) -> Decimal

Set: Quantity(self: PackingSlipLine) = value
"""

    QuantityCubicMeters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityCubicMeters(self: PackingSlipLine) -> Decimal

Set: QuantityCubicMeters(self: PackingSlipLine) = value
"""

    QuantityInBackOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityInBackOrder(self: PackingSlipLine) -> Decimal

Set: QuantityInBackOrder(self: PackingSlipLine) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOrdered(self: PackingSlipLine) -> Decimal

Set: QuantityOrdered(self: PackingSlipLine) = value
"""

    SalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesPrice(self: PackingSlipLine) -> Decimal

Set: SalesPrice(self: PackingSlipLine) = value
"""

    SalesPriceWithVat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesPriceWithVat(self: PackingSlipLine) -> Decimal

Set: SalesPriceWithVat(self: PackingSlipLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: PackingSlipLine) -> str

Set: UnitCode(self: PackingSlipLine) = value
"""

    WeightUom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeightUom(self: PackingSlipLine) -> str

Set: WeightUom(self: PackingSlipLine) = value
"""



class ProcessShipmentArgs:
    """ ProcessShipmentArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ProcessShipmentArgs) -> CacheKey

Set: CacheKey(self: ProcessShipmentArgs) = value
"""

    ShipmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentId(self: ProcessShipmentArgs) -> int

Set: ShipmentId(self: ProcessShipmentArgs) = value
"""



class ProcessShipmentStepsEnum:
    """ enum ProcessShipmentStepsEnum, values: Done (4), LogShipment (1), PrintPackingSlip (3), ProcessInfoToErp (2), ProcessShipment (0) """
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

    Done = None
    LogShipment = None
    PrintPackingSlip = None
    ProcessInfoToErp = None
    ProcessShipment = None
    value__ = None


class Proforma:
    """ Proforma() """
    def Clone(self):
        """ Clone(self: Proforma) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: Proforma) -> DateTime

Set: Date(self: Proforma) = value
"""

    DbKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DbKey(self: Proforma) -> int

Set: DbKey(self: Proforma) = value
"""

    Discounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Discounts(self: Proforma) -> Decimal

Set: Discounts(self: Proforma) = value
"""

    FreightCharges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreightCharges(self: Proforma) -> Decimal

Set: FreightCharges(self: Proforma) = value
"""

    InsuranceCharges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsuranceCharges(self: Proforma) -> Decimal

Set: InsuranceCharges(self: Proforma) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: Proforma) -> int

Set: LineNumber(self: Proforma) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: Proforma) -> int

Set: Number(self: Proforma) = value
"""

    OtherCharges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OtherCharges(self: Proforma) -> Decimal

Set: OtherCharges(self: Proforma) = value
"""



class References:
    """ References() """
    def Clone(self):
        """ Clone(self: References) -> object """
        pass

    def CopyFrom(self, from_):
        """ CopyFrom(self: References, from: References) """
        pass

    @staticmethod
    def JoinReferences(references):
        """ JoinReferences(references: IEnumerable[str]) -> str """
        pass

    @staticmethod
    def SplitReferences(references):
        """ SplitReferences(references: str) -> List[str] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CustomerReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerReferences(self: References) -> List[str]

"""

    CustomerReferencesAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerReferencesAsString(self: References) -> str

Set: CustomerReferencesAsString(self: References) = value
"""

    DebtorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebtorNumber(self: References) -> str

Set: DebtorNumber(self: References) = value
"""

    OrderNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumbers(self: References) -> List[str]

"""

    OrderNumbersAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumbersAsString(self: References) -> str

Set: OrderNumbersAsString(self: References) = value
"""

    PackageSlipNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageSlipNumbers(self: References) -> List[str]

"""

    PackageSlipNumbersAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageSlipNumbersAsString(self: References) -> str

Set: PackageSlipNumbersAsString(self: References) = value
"""



class Services:
    """ Services() """
    def Exists(self, *__args):
        """ Exists(self: Services, serviceId: str) -> bool """
        pass

    def GetById(self, serviceId):
        """ GetById(self: Services, serviceId: str) -> ServiceBase """
        pass

    def IndexOf(self, *__args):
        """ IndexOf(self: Services, serviceId: str) -> int """
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


class ShipmentDayClass:
    """ ShipmentDayClass() """
    ShipmentDay = None


class ShipmentInfo:
    """ ShipmentInfo() """
    ColliCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColliCount(self: ShipmentInfo) -> int

Set: ColliCount(self: ShipmentInfo) = value
"""

    TotalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalWeight(self: ShipmentInfo) -> Decimal

Set: TotalWeight(self: ShipmentInfo) = value
"""

    TrackingUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrackingUrl(self: ShipmentInfo) -> str

Set: TrackingUrl(self: ShipmentInfo) = value
"""



class ShipperInitInfo:
    """ ShipperInitInfo() """
    RootShipperFolder = None


class ShipperServiceLink:
    """
    ShipperServiceLink()
    ShipperServiceLink(erpDeliveryMethodCode: str, erpDeliveryMethodDescription: str, shipperId: str, serviceLevel: str, allowDifferentChoice: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, erpDeliveryMethodCode=None, erpDeliveryMethodDescription=None, shipperId=None, serviceLevel=None, allowDifferentChoice=None):
        """
        __new__(cls: type)
        __new__(cls: type, erpDeliveryMethodCode: str, erpDeliveryMethodDescription: str, shipperId: str, serviceLevel: str, allowDifferentChoice: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AllowDifferentChoice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowDifferentChoice(self: ShipperServiceLink) -> bool

Set: AllowDifferentChoice(self: ShipperServiceLink) = value
"""

    ErpDeliveryMethodCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErpDeliveryMethodCode(self: ShipperServiceLink) -> str

Set: ErpDeliveryMethodCode(self: ShipperServiceLink) = value
"""

    ErpDeliveryMethodDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErpDeliveryMethodDescription(self: ShipperServiceLink) -> str

Set: ErpDeliveryMethodDescription(self: ShipperServiceLink) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ShipperServiceLink) -> int

Set: Id(self: ShipperServiceLink) = value
"""

    ServiceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ServiceLevel(self: ShipperServiceLink) -> str

Set: ServiceLevel(self: ShipperServiceLink) = value
"""

    ShipperId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperId(self: ShipperServiceLink) -> str

Set: ShipperId(self: ShipperServiceLink) = value
"""



class ShipperServiceLinks:
    """
    ShipperServiceLinks()
    ShipperServiceLinks(items: Array[ShipperServiceLink])
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, items=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: Array[ShipperServiceLink])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'ErpDeliveryMethodCode'
    ValueMember = 'Id'


class State:
    """ enum State, values: Packed (2), Picked (0), Processed (1), Shipped (3) """
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

    Packed = None
    Picked = None
    Processed = None
    Shipped = None
    value__ = None


class TransportItem:
    """
    TransportItem()
    TransportItem(line: OutboundOrderLine, boxGuid: Guid, itemIds: ItemIdentifications, innerReference: str)
    TransportItem(line: OutboundOrderLine, boxGuid: Guid, quantity: Decimal, quantityProcessed: Decimal, registerItemIdsDuringPacking: bool, innerReference: str)
    """
    def Clone(self):
        """ Clone(self: TransportItem) -> object """
        pass

    def CloneWithSpecificOutboundOrder(self, orderNumber):
        """ CloneWithSpecificOutboundOrder(self: TransportItem, orderNumber: str) -> object """
        pass

    def CopyTo(self, item, itemIds=None):
        """ CopyTo(self: TransportItem, item: TransportItem)CopyTo(self: TransportItem, item: TransportItem, itemIds: ItemIdentifications) """
        pass

    def ResetQuantity(self):
        """ ResetQuantity(self: TransportItem) """
        pass

    def SetQuantityOriginal(self):
        """ SetQuantityOriginal(self: TransportItem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, line=None, boxGuid=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, line: OutboundOrderLine, boxGuid: Guid, itemIds: ItemIdentifications, innerReference: str)
        __new__(cls: type, line: OutboundOrderLine, boxGuid: Guid, quantity: Decimal, quantityProcessed: Decimal, registerItemIdsDuringPacking: bool, innerReference: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchId(self: TransportItem) -> str

Set: BatchId(self: TransportItem) = value
"""

    BatchIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchIds(self: TransportItem) -> List[str]

Set: BatchIds(self: TransportItem) = value
"""

    Colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colors(self: TransportItem) -> List[str]

Set: Colors(self: TransportItem) = value
"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Currency(self: TransportItem) -> str

Set: Currency(self: TransportItem) = value
"""

    DbKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DbKey(self: TransportItem) -> int

Set: DbKey(self: TransportItem) = value
"""

    DefaultVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorItemCode(self: TransportItem) -> str

Set: DefaultVendorItemCode(self: TransportItem) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: TransportItem) -> str

Set: Description(self: TransportItem) = value
"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GTINCode(self: TransportItem) -> str

Set: GTINCode(self: TransportItem) = value
"""

    InnerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerReference(self: TransportItem) -> str

Set: InnerReference(self: TransportItem) = value
"""

    Instruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Instruction(self: TransportItem) -> str

Set: Instruction(self: TransportItem) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: TransportItem) -> bool

Set: IsBatchNumberItem(self: TransportItem) = value
"""

    IsExtraItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExtraItem(self: TransportItem) -> bool

Set: IsExtraItem(self: TransportItem) = value
"""

    IsFractionAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFractionAllowed(self: TransportItem) -> bool

Set: IsFractionAllowed(self: TransportItem) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: TransportItem) -> bool

Set: IsSerialNumberItem(self: TransportItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: TransportItem) -> str

Set: ItemCode(self: TransportItem) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: TransportItem) -> ItemIdentifications

Set: ItemIds(self: TransportItem) = value
"""

    ItemSalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemSalesPrice(self: TransportItem) -> Decimal

Set: ItemSalesPrice(self: TransportItem) = value
"""

    ItemSalesPriceSingleWithVat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemSalesPriceSingleWithVat(self: TransportItem) -> Decimal

Set: ItemSalesPriceSingleWithVat(self: TransportItem) = value
"""

    ItemWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemWeight(self: TransportItem) -> Decimal

Set: ItemWeight(self: TransportItem) = value
"""

    OutboundOrderItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutboundOrderItems(self: TransportItem) -> OutboundOrderItems

Set: OutboundOrderItems(self: TransportItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: TransportItem) -> Decimal

Set: Quantity(self: TransportItem) = value
"""

    QuantityOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOriginal(self: TransportItem) -> Decimal

Set: QuantityOriginal(self: TransportItem) = value
"""

    QuantityProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityProcessed(self: TransportItem) -> Decimal

Set: QuantityProcessed(self: TransportItem) = value
"""

    RegisterItemIdsDuringPacking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegisterItemIdsDuringPacking(self: TransportItem) -> bool

Set: RegisterItemIdsDuringPacking(self: TransportItem) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: TransportItem) -> State

Set: State(self: TransportItem) = value
"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: TransportItem) -> str

"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: TransportItem) -> str

Set: UnitCode(self: TransportItem) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: TransportItem) -> str

Set: WarehouseCode(self: TransportItem) = value
"""



class TransportItems:
    """
    TransportItems()
    TransportItems(items: IEnumerable[TransportItem])
    """
    def Add(self, item, includingItemIds=None):
        """ Add(self: TransportItems, item: TransportItem)Add(self: TransportItems, item: TransportItem, includingItemIds: bool) """
        pass

    def Clone(self):
        """ Clone(self: TransportItems) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[TransportItem]) -> TransportItems """
        pass

    def GetTotalAmountWithVat(self):
        """ GetTotalAmountWithVat(self: TransportItems) -> Decimal """
        pass

    def Remove(self, *__args):
        """ Remove(self: TransportItems, item: TransportItem, removeWhenNothingLeft: bool, compareItemIdsForOutboundOrder: bool) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, items=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: IEnumerable[TransportItem])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Description'
    ValueMember = 'UniqueId'


class TransportOptions:
    """ TransportOptions() """
    CustomFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomFields(self: TransportOptions) -> SerializableDictionary[str, object]

Set: CustomFields(self: TransportOptions) = value
"""

    DeliveryBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryBegin(self: TransportOptions) -> Nullable[DateTime]

Set: DeliveryBegin(self: TransportOptions) = value
"""

    DeliveryEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryEnd(self: TransportOptions) -> Nullable[DateTime]

Set: DeliveryEnd(self: TransportOptions) = value
"""

    IsShipperServiceLinkSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShipperServiceLinkSet(self: TransportOptions) -> bool

"""

    Pickup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pickup(self: TransportOptions) -> Nullable[DateTime]

Set: Pickup(self: TransportOptions) = value
"""

    Shipper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shipper(self: TransportOptions) -> str

Set: Shipper(self: TransportOptions) = value
"""

    ShipperDisallowDifferentChoice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperDisallowDifferentChoice(self: TransportOptions) -> bool

Set: ShipperDisallowDifferentChoice(self: TransportOptions) = value
"""

    ShipperServiceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipperServiceLevel(self: TransportOptions) -> str

Set: ShipperServiceLevel(self: TransportOptions) = value
"""



class TransportPackage:
    """
    TransportPackage(boxGuid: Guid)
    TransportPackage()
    """
    def Clone(self):
        """ Clone(self: TransportPackage) -> object """
        pass

    def CreateExtraTransportItemOfOrderLine(self, line):
        """ CreateExtraTransportItemOfOrderLine(self: TransportPackage, line: OutboundOrderLine) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, boxGuid=None):
        """
        __new__(cls: type, boxGuid: Guid)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CashAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CashAmount(self: TransportPackage) -> Decimal

Set: CashAmount(self: TransportPackage) = value
"""

    IsMixedCollo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMixedCollo(self: TransportPackage) -> bool

"""

    Shipment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shipment(self: TransportPackage) -> ShipmentBase

"""

    StockRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockRegistration(self: TransportPackage) -> StockRegistrationForColliEnum

Set: StockRegistration(self: TransportPackage) = value
"""

    TransportItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportItems(self: TransportPackage) -> TransportItems

Set: TransportItems(self: TransportPackage) = value
"""



class TransportPackages:
    """
    TransportPackages()
    TransportPackages(batches: Batches)
    """
    def Add(self, *__args):
        """ Add(self: TransportPackages, package: TransportPackage) """
        pass

    def AddNew(self, basedOn=None, boxId=None, outerReference=None):
        """
        AddNew(self: TransportPackages) -> Guid
        AddNew(self: TransportPackages, basedOn: ColliPreset) -> Guid
        AddNew(self: TransportPackages, basedOn: ColliPreset, boxId: str, outerReference: str) -> Guid
        """
        pass

    def AddTransportItemToPackage(self, boxGuid, transItem):
        """ AddTransportItemToPackage(self: TransportPackages, boxGuid: Guid, transItem: TransportItem) """
        pass

    def Clone(self):
        """ Clone(self: TransportPackages) -> object """
        pass

    @staticmethod
    def FromIEnumerable(packages):
        """ FromIEnumerable(packages: IEnumerable[TransportPackage]) -> TransportPackages """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TransportPackages) -> int """
        pass

    def GetTransportItems(self, boxGuid):
        """ GetTransportItems(self: TransportPackages, boxGuid: Guid) -> TransportItems """
        pass

    def MoveTransportItems(self, fromBoxGuid, toBoxGuid, items, includingItemIds):
        """ MoveTransportItems(self: TransportPackages, fromBoxGuid: Guid, toBoxGuid: Guid, items: TransportItems, includingItemIds: bool) -> bool """
        pass

    def Remove(self, *__args):
        """ Remove(self: TransportPackages, boxGuid: Guid) -> bool """
        pass

    def SetReferences(self, boxGuid):
        """ SetReferences(self: TransportPackages, boxGuid: Guid) """
        pass

    def Update(self, *__args):
        """ Update(self: TransportPackages, newPackageData: TransportPackage) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, batches=None):
        """
        __new__(cls: type)
        __new__(cls: type, batches: Batches)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    AreOutboundOrdersProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreOutboundOrdersProcessed(self: TransportPackages) -> bool

Set: AreOutboundOrdersProcessed(self: TransportPackages) = value
"""

    ArePackagesRegistered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArePackagesRegistered(self: TransportPackages) -> bool

Set: ArePackagesRegistered(self: TransportPackages) = value
"""

    Batches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Batches(self: TransportPackages) -> Batches

"""

    Customer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Customer(self: TransportPackages) -> PackCustomer

Set: Customer(self: TransportPackages) = value
"""

    InvoiceAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InvoiceAddress(self: TransportPackages) -> Address

Set: InvoiceAddress(self: TransportPackages) = value
"""

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: TransportPackages) -> bool

"""

    IsHistoricShipment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHistoricShipment(self: TransportPackages) -> bool

"""

    IsModifiedHistoryShipment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsModifiedHistoryShipment(self: TransportPackages) -> bool

Set: IsModifiedHistoryShipment(self: TransportPackages) = value
"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: TransportPackages) -> TransportOptions

Set: Options(self: TransportPackages) = value
"""

    OrderNotes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNotes(self: TransportPackages) -> str

Set: OrderNotes(self: TransportPackages) = value
"""

    OurReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OurReferences(self: TransportPackages) -> List[str]

"""

    PackageSlipNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackageSlipNumbers(self: TransportPackages) -> List[str]

Set: PackageSlipNumbers(self: TransportPackages) = value
"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: TransportPackages) -> bool

"""

    ProcessedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessedBy(self: TransportPackages) -> Session

Set: ProcessedBy(self: TransportPackages) = value
"""

    ProcessState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessState(self: TransportPackages) -> ProcessShipmentStepsEnum

Set: ProcessState(self: TransportPackages) = value
"""

    ReceiveAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveAddress(self: TransportPackages) -> Address

Set: ReceiveAddress(self: TransportPackages) = value
"""

    SendAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SendAddress(self: TransportPackages) -> Address

Set: SendAddress(self: TransportPackages) = value
"""

    SessionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionCount(self: TransportPackages) -> int

Set: SessionCount(self: TransportPackages) = value
"""

    SessionHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionHashCode(self: TransportPackages) -> int

Set: SessionHashCode(self: TransportPackages) = value
"""

    ShipmentKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentKey(self: TransportPackages) -> int

Set: ShipmentKey(self: TransportPackages) = value
"""

    ShipmentNotes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentNotes(self: TransportPackages) -> str

Set: ShipmentNotes(self: TransportPackages) = value
"""

    TotalVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalVolume(self: TransportPackages) -> Decimal

"""



class TypeOfDay:
    """ enum TypeOfDay, values: WeekDays (1), WorkingDays (0) """
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

    value__ = None
    WeekDays = None
    WorkingDays = None


class UpdateTransportPackageArgs:
    """ UpdateTransportPackageArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: UpdateTransportPackageArgs) -> CacheKey

Set: CacheKey(self: UpdateTransportPackageArgs) = value
"""

    ValidateItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidateItem(self: UpdateTransportPackageArgs) -> bool

Set: ValidateItem(self: UpdateTransportPackageArgs) = value
"""



class UpdateTransportPackagesHeaderArgs:
    """ UpdateTransportPackagesHeaderArgs() """
    Customer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Customer(self: UpdateTransportPackagesHeaderArgs) -> PackCustomer

Set: Customer(self: UpdateTransportPackagesHeaderArgs) = value
"""

    InvoiceAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InvoiceAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: InvoiceAddress(self: UpdateTransportPackagesHeaderArgs) = value
"""

    ReceiveAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: ReceiveAddress(self: UpdateTransportPackagesHeaderArgs) = value
"""

    SendAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SendAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: SendAddress(self: UpdateTransportPackagesHeaderArgs) = value
"""

    ShipmentNotes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipmentNotes(self: UpdateTransportPackagesHeaderArgs) -> str

Set: ShipmentNotes(self: UpdateTransportPackagesHeaderArgs) = value
"""

    TransportOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportOptions(self: UpdateTransportPackagesHeaderArgs) -> TransportOptions

Set: TransportOptions(self: UpdateTransportPackagesHeaderArgs) = value
"""



# variables with complex values

