# encoding: utf-8
# module Wms.RemotingObjects.ShippingLayers calls itself ShippingLayers
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class Address(object):
 """ Address() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Address()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: Address) -> object """
  pass
 def CopyFrom(self,from_):
  """ CopyFrom(self: Address,from: Address) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Address1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address1(self: Address) -> str

Set: Address1(self: Address)=value
"""

 Address2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address2(self: Address) -> str

Set: Address2(self: Address)=value
"""

 Address3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address3(self: Address) -> str

Set: Address3(self: Address)=value
"""

 City=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: City(self: Address) -> str

Set: City(self: Address)=value
"""

 CountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountryCode(self: Address) -> str

Set: CountryCode(self: Address)=value
"""

 CountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountryName(self: Address) -> str

Set: CountryName(self: Address)=value
"""

 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomFields(self: Address) -> SerializableDictionary[str,object]

Set: CustomFields(self: Address)=value
"""

 DeliveryBeginDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryBeginDateTime(self: Address) -> DateTime

Set: DeliveryBeginDateTime(self: Address)=value
"""

 DeliveryEndDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryEndDateTime(self: Address) -> DateTime

Set: DeliveryEndDateTime(self: Address)=value
"""

 Email=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Email(self: Address) -> str

Set: Email(self: Address)=value
"""

 EoriNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EoriNumber(self: Address) -> str

Set: EoriNumber(self: Address)=value
"""

 FullAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FullAddress(self: Address) -> str

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: Address) -> str

Set: Name(self: Address)=value
"""

 Name2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name2(self: Address) -> str

Set: Name2(self: Address)=value
"""

 PhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PhoneNumber(self: Address) -> str

Set: PhoneNumber(self: Address)=value
"""

 PickupDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PickupDateTime(self: Address) -> DateTime

Set: PickupDateTime(self: Address)=value
"""

 StateCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StateCode(self: Address) -> str

Set: StateCode(self: Address)=value
"""

 ZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ZipCode(self: Address) -> str

Set: ZipCode(self: Address)=value
"""



class AddTransportPackageArgs(object):
 """ AddTransportPackageArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AddTransportPackageArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 BoxIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Optional. The id's for the new Wms.RemotingObjects.ShippingLayers.TransportPackage.

Get: BoxIds(self: AddTransportPackageArgs) -> List[str]

"""

 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: AddTransportPackageArgs) -> CacheKey

Set: CacheKey(self: AddTransportPackageArgs)=value
"""

 NumberOfPackages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: NumberOfPackages(self: AddTransportPackageArgs) -> int

Set: NumberOfPackages(self: AddTransportPackageArgs)=value
"""

 OuterReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The outer reference (SSCC) to be used when adding a new package

Get: OuterReference(self: AddTransportPackageArgs) -> str

Set: OuterReference(self: AddTransportPackageArgs)=value
"""

 Preset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Preset(self: AddTransportPackageArgs) -> ColliPreset

Set: Preset(self: AddTransportPackageArgs)=value
"""

 RegisterBoxIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RegisterBoxIds(self: AddTransportPackageArgs) -> bool

Set: RegisterBoxIds(self: AddTransportPackageArgs)=value
"""



class Charge(object):
 """
 Charge()
 Charge(amount: Decimal,currencyCode: str,description: str)
 Charge(amount: Decimal,salesAmount: Decimal,currencyCode: str,description: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Charge()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,amount=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,amount: Decimal,currencyCode: str,description: str)
  __new__(cls: type,amount: Decimal,salesAmount: Decimal,currencyCode: str,description: str)
  """
  pass
 Amount=None
 CurrencyCode=None
 Description=None
 Empty=None
 SalesAmount=None


class Charges(List):
 """ Charges() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Charges()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Empty=None


class ColliPreset(object):
 """ ColliPreset() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ColliPreset()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Active(self: ColliPreset) -> bool

Set: Active(self: ColliPreset)=value
"""

 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Barcode(self: ColliPreset) -> str

Set: Barcode(self: ColliPreset)=value
"""

 ColliSpecificationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ColliSpecificationCode(self: ColliPreset) -> str

Set: ColliSpecificationCode(self: ColliPreset)=value
"""

 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedBy(self: ColliPreset) -> str

Set: CreatedBy(self: ColliPreset)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedOn(self: ColliPreset) -> DateTime

Set: CreatedOn(self: ColliPreset)=value
"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Height(self: ColliPreset) -> Decimal

Set: Height(self: ColliPreset)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: ColliPreset) -> int

Set: Id(self: ColliPreset)=value
"""

 IsDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsDefault(self: ColliPreset) -> bool

Set: IsDefault(self: ColliPreset)=value
"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Item(self: ColliPreset) -> Item

Set: Item(self: ColliPreset)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: ColliPreset) -> str

Set: ItemCode(self: ColliPreset)=value
"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Length(self: ColliPreset) -> Decimal

Set: Length(self: ColliPreset)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedBy(self: ColliPreset) -> str

Set: ModifiedBy(self: ColliPreset)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedOn(self: ColliPreset) -> DateTime

Set: ModifiedOn(self: ColliPreset)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: ColliPreset) -> str

Set: Name(self: ColliPreset)=value
"""

 StockRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StockRegistration(self: ColliPreset) -> StockRegistrationForColliEnum

Set: StockRegistration(self: ColliPreset)=value
"""

 StockRegistrationAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StockRegistrationAsString(self: ColliPreset) -> str

"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: ColliPreset) -> PackageType

Set: Type(self: ColliPreset)=value
"""

 TypeAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TypeAsString(self: ColliPreset) -> str

"""

 Weight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Weight(self: ColliPreset) -> Decimal

Set: Weight(self: ColliPreset)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Width(self: ColliPreset) -> Decimal

Set: Width(self: ColliPreset)=value
"""



class ColliPresets(FindableList):
 """
 ColliPresets()
 ColliPresets(items: Array[ColliPreset])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ColliPresets()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[ColliPreset]) -> ColliPresets """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,items=None):
  """
  __new__(cls: type)
  __new__(cls: type,items: Array[ColliPreset])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='Id'


class Countries(FindableList):
 """ Countries() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Countries()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='Code'


class Country(object):
 """
 Country()
 Country(code: str,name: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Country()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,code=None,name=None):
  """
  __new__(cls: type)
  __new__(cls: type,code: str,name: str)
  """
  pass
 Code=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Code(self: Country) -> str

Set: Code(self: Country)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Country) -> str

Set: Name(self: Country)=value
"""



class DangerousItem(object):
 """ DangerousItem() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DangerousItem()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: DangerousItem) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Code=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Code(self: DangerousItem) -> str

Set: Code(self: DangerousItem)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: DangerousItem) -> str

Set: Description(self: DangerousItem)=value
"""

 FlashPointDegree=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FlashPointDegree(self: DangerousItem) -> Decimal

Set: FlashPointDegree(self: DangerousItem)=value
"""

 GrossWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: GrossWeight(self: DangerousItem) -> Decimal

Set: GrossWeight(self: DangerousItem)=value
"""

 Instruction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Instruction(self: DangerousItem) -> str

Set: Instruction(self: DangerousItem)=value
"""

 LimitedQuantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LimitedQuantity(self: DangerousItem) -> str

Set: LimitedQuantity(self: DangerousItem)=value
"""

 LimitedQuantityPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: LimitedQuantityPoints(self: DangerousItem) -> int

Set: LimitedQuantityPoints(self: DangerousItem)=value
"""

 MarkingIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MarkingIdentifier(self: DangerousItem) -> str

Set: MarkingIdentifier(self: DangerousItem)=value
"""

 Measurements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Measurements(self: DangerousItem) -> Dimensions

Set: Measurements(self: DangerousItem)=value
"""

 NetWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: NetWeight(self: DangerousItem) -> Decimal

Set: NetWeight(self: DangerousItem)=value
"""

 PackingClassificiation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PackingClassificiation(self: DangerousItem) -> str

Set: PackingClassificiation(self: DangerousItem)=value
"""

 PackingGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PackingGroup(self: DangerousItem) -> str

Set: PackingGroup(self: DangerousItem)=value
"""

 PackingType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PackingType(self: DangerousItem) -> str

Set: PackingType(self: DangerousItem)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Quantity(self: DangerousItem) -> Decimal

Set: Quantity(self: DangerousItem)=value
"""

 TunnelCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TunnelCode(self: DangerousItem) -> str

Set: TunnelCode(self: DangerousItem)=value
"""

 UndgCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UndgCode(self: DangerousItem) -> str

Set: UndgCode(self: DangerousItem)=value
"""

 UndgSubCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UndgSubCode(self: DangerousItem) -> str

Set: UndgSubCode(self: DangerousItem)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: DangerousItem) -> str

Set: UnitCode(self: DangerousItem)=value
"""

 Volume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Volume(self: DangerousItem) -> Decimal

Set: Volume(self: DangerousItem)=value
"""



class DangerousItems(List):
 """
 DangerousItems()
 DangerousItems(items: IEnumerable[DangerousItem])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DangerousItems()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: DangerousItems) -> object """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,items=None):
  """
  __new__(cls: type)
  __new__(cls: type,items: IEnumerable[DangerousItem])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class Dimensions(object):
 """
 Dimensions(length: Decimal,width: Decimal,height: Decimal)
 Dimensions()
 Dimensions(dimensions: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Dimensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CompareTo(self,other):
  """ CompareTo(self: Dimensions,other: Dimensions) -> int """
  pass
 def CopyTo(self,destination):
  """ CopyTo(self: Dimensions,destination: Dimensions) """
  pass
 def Equals(self,obj):
  """ Equals(self: Dimensions,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Dimensions) -> int """
  pass
 def IsValid(self):
  """
  IsValid(self: Dimensions) -> bool
  
   Returns true if all dimensions are greater than zero
  """
  pass
 def ToDimensionObjectWhereLengthIsLongest(self):
  """
  ToDimensionObjectWhereLengthIsLongest(self: Dimensions) -> Dimensions
  
   Swaps dimensions so that length is always the longest
  """
  pass
 def ToString(self):
  """ ToString(self: Dimensions) -> str """
  pass
 def ToVolume(self):
  """ ToVolume(self: Dimensions) -> Decimal """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __lt__(self,*args):
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,length: Decimal,width: Decimal,height: Decimal)
  __new__(cls: type)
  __new__(cls: type,dimensions: str)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """ __radd__(dim1: Dimensions,dim2: Dimensions) -> Dimensions """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """ __rsub__(dim1: Dimensions,dim2: Dimensions) -> Dimensions """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Height(self: Dimensions) -> Decimal

Set: Height(self: Dimensions)=value
"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Length(self: Dimensions) -> Decimal

Set: Length(self: Dimensions)=value
"""

 UnitOfMeasurement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitOfMeasurement(self: Dimensions) -> str

Set: UnitOfMeasurement(self: Dimensions)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Width(self: Dimensions) -> Decimal

Set: Width(self: Dimensions)=value
"""


 Empty=None


class ExportDetails(object):
 """ ExportDetails() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExportDetails()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: ExportDetails) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CountryOfOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Country of origin of a product

Get: CountryOfOrigin(self: ExportDetails) -> str

Set: CountryOfOrigin(self: ExportDetails)=value
"""

 HsCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Harmonized System Code. A unique code of an internationally 
   standard system of names and numbers to classify traded products.

Get: HsCode(self: ExportDetails) -> str

Set: HsCode(self: ExportDetails)=value
"""

 HsCodeDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The descroption of the Wms.RemotingObjects.ShippingLayers.ExportDetails.HsCode

Get: HsCodeDescription(self: ExportDetails) -> str

Set: HsCodeDescription(self: ExportDetails)=value
"""

 ReasonOfExport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A description with the reason of the export

Get: ReasonOfExport(self: ExportDetails) -> str

Set: ReasonOfExport(self: ExportDetails)=value
"""



class HistoryShipment(object):
 """ HistoryShipment() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryShipment()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address(self: HistoryShipment) -> str

Set: Address(self: HistoryShipment)=value
"""

 Address2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address2(self: HistoryShipment) -> str

Set: Address2(self: HistoryShipment)=value
"""

 Address3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Address3(self: HistoryShipment) -> str

Set: Address3(self: HistoryShipment)=value
"""

 Canceled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Canceled(self: HistoryShipment) -> bool

Set: Canceled(self: HistoryShipment)=value
"""

 City=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: City(self: HistoryShipment) -> str

Set: City(self: HistoryShipment)=value
"""

 Colli=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Colli(self: HistoryShipment) -> int

Set: Colli(self: HistoryShipment)=value
"""

 CountryAndCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountryAndCity(self: HistoryShipment) -> str

"""

 CountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CountryCode(self: HistoryShipment) -> str

Set: CountryCode(self: HistoryShipment)=value
"""

 CountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountryName(self: HistoryShipment) -> str

Set: CountryName(self: HistoryShipment)=value
"""

 DeliveryBeginDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryBeginDateTime(self: HistoryShipment) -> DateTime

Set: DeliveryBeginDateTime(self: HistoryShipment)=value
"""

 DeliveryEndDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryEndDateTime(self: HistoryShipment) -> DateTime

Set: DeliveryEndDateTime(self: HistoryShipment)=value
"""

 Email=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Email(self: HistoryShipment) -> str

Set: Email(self: HistoryShipment)=value
"""

 HasAttachments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the shipments has any attachments (documents). This doesn't include labels!

Get: HasAttachments(self: HistoryShipment) -> bool

Set: HasAttachments(self: HistoryShipment)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: HistoryShipment) -> int

Set: Id(self: HistoryShipment)=value
"""

 IsCod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsCod(self: HistoryShipment) -> bool

Set: IsCod(self: HistoryShipment)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedBy(self: HistoryShipment) -> str

Set: ModifiedBy(self: HistoryShipment)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedOn(self: HistoryShipment) -> DateTime

Set: ModifiedOn(self: HistoryShipment)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: HistoryShipment) -> str

Set: Name(self: HistoryShipment)=value
"""

 Name2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name2(self: HistoryShipment) -> str

Set: Name2(self: HistoryShipment)=value
"""

 Notes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Notes(self: HistoryShipment) -> str

Set: Notes(self: HistoryShipment)=value
"""

 PhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PhoneNumber(self: HistoryShipment) -> str

Set: PhoneNumber(self: HistoryShipment)=value
"""

 PickupDateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PickupDateTime(self: HistoryShipment) -> DateTime

Set: PickupDateTime(self: HistoryShipment)=value
"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Reference(self: HistoryShipment) -> str

Set: Reference(self: HistoryShipment)=value
"""

 ShipperId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperId(self: HistoryShipment) -> str

Set: ShipperId(self: HistoryShipment)=value
"""

 ShipperServiceLevelId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperServiceLevelId(self: HistoryShipment) -> str

Set: ShipperServiceLevelId(self: HistoryShipment)=value
"""

 ShipperServiceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperServiceName(self: HistoryShipment) -> str

Set: ShipperServiceName(self: HistoryShipment)=value
"""

 StateCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StateCode(self: HistoryShipment) -> str

Set: StateCode(self: HistoryShipment)=value
"""

 TotalWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalWeight(self: HistoryShipment) -> Decimal

Set: TotalWeight(self: HistoryShipment)=value
"""

 ZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ZipCode(self: HistoryShipment) -> str

Set: ZipCode(self: HistoryShipment)=value
"""



class HistoryShipmentFilter(HistoryFilterBase):
 """ HistoryShipmentFilter() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryShipmentFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 SearchString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SearchString(self: HistoryShipmentFilter) -> str

Set: SearchString(self: HistoryShipmentFilter)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: YourReference(self: HistoryShipmentFilter) -> str

Set: YourReference(self: HistoryShipmentFilter)=value
"""



class HistoryShipmentLine(object):
 """ HistoryShipmentLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryShipmentLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ColliPresetName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ColliPresetName(self: HistoryShipmentLine) -> str

Set: ColliPresetName(self: HistoryShipmentLine)=value
"""

 CustomerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerReference(self: HistoryShipmentLine) -> str

Set: CustomerReference(self: HistoryShipmentLine)=value
"""

 DateOfDelivery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateOfDelivery(self: HistoryShipmentLine) -> DateTime

Set: DateOfDelivery(self: HistoryShipmentLine)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: HistoryShipmentLine) -> str

Set: Description(self: HistoryShipmentLine)=value
"""

 InnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InnerReference(self: HistoryShipmentLine) -> str

Set: InnerReference(self: HistoryShipmentLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsBatchNumberItem(self: HistoryShipmentLine) -> bool

Set: IsBatchNumberItem(self: HistoryShipmentLine)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSerialNumberItem(self: HistoryShipmentLine) -> bool

Set: IsSerialNumberItem(self: HistoryShipmentLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: HistoryShipmentLine) -> str

Set: ItemCode(self: HistoryShipmentLine)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: HistoryShipmentLine) -> str

Set: ItemDescription(self: HistoryShipmentLine)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineNumber(self: HistoryShipmentLine) -> int

Set: LineNumber(self: HistoryShipmentLine)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: HistoryShipmentLine) -> str

Set: OrderNumber(self: HistoryShipmentLine)=value
"""

 OutboundOrdersPk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OutboundOrdersPk(self: HistoryShipmentLine) -> int

Set: OutboundOrdersPk(self: HistoryShipmentLine)=value
"""

 PackageDimensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageDimensions(self: HistoryShipmentLine) -> str

Set: PackageDimensions(self: HistoryShipmentLine)=value
"""

 PackageNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageNumber(self: HistoryShipmentLine) -> str

Set: PackageNumber(self: HistoryShipmentLine)=value
"""

 PackageTrackingNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageTrackingNumber(self: HistoryShipmentLine) -> str

Set: PackageTrackingNumber(self: HistoryShipmentLine)=value
"""

 PackageType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageType(self: HistoryShipmentLine) -> str

Set: PackageType(self: HistoryShipmentLine)=value
"""

 PackageVolume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageVolume(self: HistoryShipmentLine) -> Decimal

Set: PackageVolume(self: HistoryShipmentLine)=value
"""

 PackageWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageWeight(self: HistoryShipmentLine) -> Decimal

Set: PackageWeight(self: HistoryShipmentLine)=value
"""

 QuantityDelivered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityDelivered(self: HistoryShipmentLine) -> Decimal

Set: QuantityDelivered(self: HistoryShipmentLine)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: QuantityOrdered(self: HistoryShipmentLine) -> Decimal

Set: QuantityOrdered(self: HistoryShipmentLine)=value
"""

 ShipmentPackagePk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentPackagePk(self: HistoryShipmentLine) -> int

Set: ShipmentPackagePk(self: HistoryShipmentLine)=value
"""

 ShipmentPk=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentPk(self: HistoryShipmentLine) -> int

Set: ShipmentPk(self: HistoryShipmentLine)=value
"""

 SSCC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SSCC(self: HistoryShipmentLine) -> str

Set: SSCC(self: HistoryShipmentLine)=value
"""



class HistoryShipmentLines(PagedList):
 """
 HistoryShipmentLines()
 HistoryShipmentLines(collection: IEnumerable[HistoryShipmentLine])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryShipmentLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(collection):
  """ FromIEnumerable(collection: IEnumerable[HistoryShipmentLine]) -> HistoryShipmentLines """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[HistoryShipmentLine])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsDisposable(self: HistoryShipmentLines) -> bool

"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreserveState(self: HistoryShipmentLines) -> bool

"""


 DisplayMember='ItemDescription'
 ValueMember='ItemCode'


class HistoryShipments(FindableList):
 """ HistoryShipments() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryShipments()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Total=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Total(self: HistoryShipments) -> Int64

Set: Total(self: HistoryShipments)=value
"""

 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Same as Total property needed to implement Wms.RemotingObjects.IPagedList.

Get: TotalRowsMatched(self: HistoryShipments) -> Int64

Set: TotalRowsMatched(self: HistoryShipments)=value
"""


 DisplayMember=None
 ValueMember='Id'


class IService:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IService()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: IService) -> str

"""

 ExtraCharges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtraCharges(self: IService) -> Charges

Set: ExtraCharges(self: IService)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: IService) -> str

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: IService) -> str

"""

 TotalCharge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalCharge(self: IService) -> Charge

Set: TotalCharge(self: IService)=value
"""

 TransportationCharge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransportationCharge(self: IService) -> Charge

Set: TransportationCharge(self: IService)=value
"""



class IShipper:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IShipper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ColliSpecificationCodes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ColliSpecificationCodes(self: IShipper) -> Array[str]

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: IShipper) -> str

"""

 DimensionMandatory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DimensionMandatory(self: IShipper) -> bool

"""

 Logo48=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Logo48(self: IShipper) -> Bitmap

"""

 Logo64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Logo64(self: IShipper) -> Bitmap

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: IShipper) -> str

"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UniqueId(self: IShipper) -> str

"""



class LogSink(object):
 """ LogSink() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LogSink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def Write(message,type=None):
  """ Write(message: str,type: LogSinkMessageTypes)Write(message: str) """
  pass
 LogSinkMessage=None
 OnLogSinkMessage=None


class LogSinkMessageTypes:
 """ enum LogSinkMessageTypes,values: Debug (2),Error (0),UserInfo (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LogSinkMessageTypes()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Debug=None
 Error=None
 UserInfo=None
 value__=None


class MobileService(object):
 """
 MobileService()
 MobileService(original: IService)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MobileService()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,original=None):
  """
  __new__(cls: type)
  __new__(cls: type,original: IService)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: MobileService) -> str

"""

 DisplayCharge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisplayCharge(self: MobileService) -> str

"""

 ExtraCharges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtraCharges(self: MobileService) -> Charges

Set: ExtraCharges(self: MobileService)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: MobileService) -> str

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: MobileService) -> str

"""

 TotalCharge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalCharge(self: MobileService) -> Charge

Set: TotalCharge(self: MobileService)=value
"""

 TransportationCharge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransportationCharge(self: MobileService) -> Charge

Set: TransportationCharge(self: MobileService)=value
"""



class MobileShipper(object):
 """
 MobileShipper(source: IShipper)
 MobileShipper()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MobileShipper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,source=None):
  """
  __new__(cls: type,source: IShipper)
  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ColliSpecificationCodes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ColliSpecificationCodes(self: MobileShipper) -> Array[str]

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: MobileShipper) -> str

"""

 DimensionMandatory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DimensionMandatory(self: MobileShipper) -> bool

"""

 Logo48=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Logo48(self: MobileShipper) -> Bitmap

"""

 Logo64=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Logo64(self: MobileShipper) -> Bitmap

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: MobileShipper) -> str

"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UniqueId(self: MobileShipper) -> str

"""



class OutboundOrderItem(object):
 """
 OutboundOrderItem()
 OutboundOrderItem(orderNumber: str,boxGuid: Guid,itemCode: str,quantity: Decimal)
 OutboundOrderItem(orderNumber: str,boxGuid: Guid,itemCode: str,itemIdentificationNumber: str,quantity: Decimal)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderItem()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetHashCode(self):
  """ GetHashCode(self: OutboundOrderItem) -> int """
  pass
 @staticmethod
 def __new__(self,orderNumber=None,boxGuid=None,itemCode=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,orderNumber: str,boxGuid: Guid,itemCode: str,quantity: Decimal)
  __new__(cls: type,orderNumber: str,boxGuid: Guid,itemCode: str,itemIdentificationNumber: str,quantity: Decimal)
  """
  pass
 BoxGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BoxGuid(self: OutboundOrderItem) -> Guid

Set: BoxGuid(self: OutboundOrderItem)=value
"""

 HistoryIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ID's of the database record in the BOXwise Pro database table OutboundOrders

Get: HistoryIds(self: OutboundOrderItem) -> Dictionary[int,Decimal]

Set: HistoryIds(self: OutboundOrderItem)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: OutboundOrderItem) -> str

Set: ItemCode(self: OutboundOrderItem)=value
"""

 ItemIdentificationNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIdentificationNumber(self: OutboundOrderItem) -> str

Set: ItemIdentificationNumber(self: OutboundOrderItem)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: OutboundOrderItem) -> str

Set: OrderNumber(self: OutboundOrderItem)=value
"""

 PackingSlipNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The packing slip number of this item. It will be assigned when it has been processed to the ERP.

Get: PackingSlipNumber(self: OutboundOrderItem) -> str

Set: PackingSlipNumber(self: OutboundOrderItem)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Quantity(self: OutboundOrderItem) -> Decimal

Set: Quantity(self: OutboundOrderItem)=value
"""

 QuantityOriginal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityOriginal(self: OutboundOrderItem) -> Decimal

Set: QuantityOriginal(self: OutboundOrderItem)=value
"""



class OutboundOrderItems(List):
 """
 OutboundOrderItems()
 OutboundOrderItems(outboundOrderItems: OutboundOrderItems)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrderItems()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddOrUpdate(self,*__args):
  """ AddOrUpdate(self: OutboundOrderItems,outboundOrderItem: OutboundOrderItem)AddOrUpdate(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,quantity: Decimal)AddOrUpdate(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,itemIdentificationNumber: str,quantity: Decimal) """
  pass
 def Clone(self):
  """ Clone(self: OutboundOrderItems) -> object """
  pass
 def Decrease(self,*__args):
  """ Decrease(self: OutboundOrderItems,outboundOrderItem: OutboundOrderItem)Decrease(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,quantity: Decimal)Decrease(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,itemIdentificationNumber: str,quantity: Decimal) """
  pass
 def DecreaseOrRemove(self,*__args):
  """ DecreaseOrRemove(self: OutboundOrderItems,outboundOrderItem: OutboundOrderItem)DecreaseOrRemove(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,quantity: Decimal)DecreaseOrRemove(self: OutboundOrderItems,orderNumber: str,boxGuid: Guid,itemCode: str,itemIdentificationNumber: str,quantity: Decimal) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,outboundOrderItems=None):
  """
  __new__(cls: type)
  __new__(cls: type,outboundOrderItems: OutboundOrderItems)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class OutboundOrdersFilter(object):
 """ OutboundOrdersFilter() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OutboundOrdersFilter()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 BoxNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BoxNumber(self: OutboundOrdersFilter) -> str

Set: BoxNumber(self: OutboundOrdersFilter)=value
"""

 SearchString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SearchString(self: OutboundOrdersFilter) -> str

Set: SearchString(self: OutboundOrdersFilter)=value
"""



class Packages(List):
 """ Packages() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Packages()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetTotalWeight(self):
  """ GetTotalWeight(self: Packages) -> Decimal """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Empty=None


class PackageType:
 """ enum PackageType,values: Box (1),Document (0),Pallet (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PackageType()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Box=None
 Document=None
 Pallet=None
 value__=None


class PackingSlipLine(object):
 """ PackingSlipLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PackingSlipLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: PackingSlipLine) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AssemblyInstructions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AssemblyInstructions(self: PackingSlipLine) -> str

Set: AssemblyInstructions(self: PackingSlipLine)=value
"""

 Composition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Composition(self: PackingSlipLine) -> str

Set: Composition(self: PackingSlipLine)=value
"""

 Currency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The currencty that's used for the sales price

Get: Currency(self: PackingSlipLine) -> str

Set: Currency(self: PackingSlipLine)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of an item

Get: Description(self: PackingSlipLine) -> str

Set: Description(self: PackingSlipLine)=value
"""

 ExportDetails=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wms.RemotingObjects.ShippingLayers.ExportDetails with additional data for export

Get: ExportDetails(self: PackingSlipLine) -> ExportDetails

Set: ExportDetails(self: PackingSlipLine)=value
"""

 GrossWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gross weight

Get: GrossWeight(self: PackingSlipLine) -> Decimal

Set: GrossWeight(self: PackingSlipLine)=value
"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The EAN code

Get: GTINCode(self: PackingSlipLine) -> str

Set: GTINCode(self: PackingSlipLine)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this item is a batch number item. Used in combination with Wms.RemotingObjects.ShippingLayers.PackingSlipLine.ItemIdentifications.

Get: IsBatchNumberItem(self: PackingSlipLine) -> bool

Set: IsBatchNumberItem(self: PackingSlipLine)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this item is a serial number item. Used in combination with Wms.RemotingObjects.ShippingLayers.PackingSlipLine.ItemIdentifications.

Get: IsSerialNumberItem(self: PackingSlipLine) -> bool

Set: IsSerialNumberItem(self: PackingSlipLine)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique code of an item

Get: ItemCode(self: PackingSlipLine) -> str

Set: ItemCode(self: PackingSlipLine)=value
"""

 ItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A System.Collections.Generic.List with the serial or batch numbers

Get: ItemIdentifications(self: PackingSlipLine) -> List[ItemIdentificationBase]

Set: ItemIdentifications(self: PackingSlipLine)=value
"""

 NettoWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Netto weight

Get: NettoWeight(self: PackingSlipLine) -> Decimal

Set: NettoWeight(self: PackingSlipLine)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of the package slip

Get: Number(self: PackingSlipLine) -> str

Set: Number(self: PackingSlipLine)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The order number

Get: OrderNumber(self: PackingSlipLine) -> str

Set: OrderNumber(self: PackingSlipLine)=value
"""

 Proforma=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wms.RemotingObjects.ShippingLayers.Proforma with information of the proforma

Get: Proforma(self: PackingSlipLine) -> Proforma

Set: Proforma(self: PackingSlipLine)=value
"""

 Quality=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Quality(self: PackingSlipLine) -> str

Set: Quality(self: PackingSlipLine)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Quantity of this item

Get: Quantity(self: PackingSlipLine) -> Decimal

Set: Quantity(self: PackingSlipLine)=value
"""

 QuantityCubicMeters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityCubicMeters(self: PackingSlipLine) -> Decimal

Set: QuantityCubicMeters(self: PackingSlipLine)=value
"""

 QuantityInBackOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The quantity in back order

Get: QuantityInBackOrder(self: PackingSlipLine) -> Decimal

Set: QuantityInBackOrder(self: PackingSlipLine)=value
"""

 QuantityOrdered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The total quantity that has been ordered

Get: QuantityOrdered(self: PackingSlipLine) -> Decimal

Set: QuantityOrdered(self: PackingSlipLine)=value
"""

 SalesPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sales price exluding VAT

Get: SalesPrice(self: PackingSlipLine) -> Decimal

Set: SalesPrice(self: PackingSlipLine)=value
"""

 SalesPriceWithVat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sales price including VAT

Get: SalesPriceWithVat(self: PackingSlipLine) -> Decimal

Set: SalesPriceWithVat(self: PackingSlipLine)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: PackingSlipLine) -> str

Set: UnitCode(self: PackingSlipLine)=value
"""

 WeightUom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit of measurement of the weights

Get: WeightUom(self: PackingSlipLine) -> str

Set: WeightUom(self: PackingSlipLine)=value
"""



class ProcessShipmentArgs(object):
 """ ProcessShipmentArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessShipmentArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: ProcessShipmentArgs) -> CacheKey

Set: CacheKey(self: ProcessShipmentArgs)=value
"""

 ShipmentId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipmentId(self: ProcessShipmentArgs) -> int

Set: ShipmentId(self: ProcessShipmentArgs)=value
"""



class ProcessShipmentStepsEnum:
 """ enum ProcessShipmentStepsEnum,values: Done (4),LogShipment (1),PrintPackingSlip (3),ProcessInfoToErp (2),ProcessShipment (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessShipmentStepsEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Done=None
 LogShipment=None
 PrintPackingSlip=None
 ProcessInfoToErp=None
 ProcessShipment=None
 value__=None


class Proforma(object):
 """ Proforma() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Proforma()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: Proforma) -> object """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Date=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Date(self: Proforma) -> DateTime

Set: Date(self: Proforma)=value
"""

 DbKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DbKey(self: Proforma) -> int

Set: DbKey(self: Proforma)=value
"""

 Discounts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Discounts(self: Proforma) -> Decimal

Set: Discounts(self: Proforma)=value
"""

 FreightCharges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FreightCharges(self: Proforma) -> Decimal

Set: FreightCharges(self: Proforma)=value
"""

 InsuranceCharges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InsuranceCharges(self: Proforma) -> Decimal

Set: InsuranceCharges(self: Proforma)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineNumber(self: Proforma) -> int

Set: LineNumber(self: Proforma)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Number(self: Proforma) -> int

Set: Number(self: Proforma)=value
"""

 OtherCharges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OtherCharges(self: Proforma) -> Decimal

Set: OtherCharges(self: Proforma)=value
"""



class References(object):
 """ References() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return References()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: References) -> object """
  pass
 def CopyFrom(self,from_):
  """ CopyFrom(self: References,from: References) """
  pass
 @staticmethod
 def JoinReferences(references):
  """ JoinReferences(references: IEnumerable[str]) -> str """
  pass
 @staticmethod
 def SplitReferences(references):
  """ SplitReferences(references: str) -> List[str] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CustomerReferences=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerReferences(self: References) -> List[str]

"""

 CustomerReferencesAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerReferencesAsString(self: References) -> str

Set: CustomerReferencesAsString(self: References)=value
"""

 DebtorNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DebtorNumber(self: References) -> str

Set: DebtorNumber(self: References)=value
"""

 OrderNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumbers(self: References) -> List[str]

"""

 OrderNumbersAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumbersAsString(self: References) -> str

Set: OrderNumbersAsString(self: References)=value
"""

 PackageSlipNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PackageSlipNumbers(self: References) -> List[str]

"""

 PackageSlipNumbersAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PackageSlipNumbersAsString(self: References) -> str

Set: PackageSlipNumbersAsString(self: References)=value
"""



class Services(FindableList):
 """ Services() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Services()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Exists(self,*__args):
  """ Exists(self: Services,serviceId: str) -> bool """
  pass
 def GetById(self,serviceId):
  """ GetById(self: Services,serviceId: str) -> ServiceBase """
  pass
 def IndexOf(self,*__args):
  """ IndexOf(self: Services,serviceId: str) -> int """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class ShipmentDayClass(object):
 """ ShipmentDayClass() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipmentDayClass()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ShipmentDay=None


class ShipmentInfo(object):
 """ ShipmentInfo() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipmentInfo()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ColliCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ColliCount(self: ShipmentInfo) -> int

Set: ColliCount(self: ShipmentInfo)=value
"""

 TotalWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalWeight(self: ShipmentInfo) -> Decimal

Set: TotalWeight(self: ShipmentInfo)=value
"""

 TrackingUrl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TrackingUrl(self: ShipmentInfo) -> str

Set: TrackingUrl(self: ShipmentInfo)=value
"""



class ShipperInitInfo(object):
 """ ShipperInitInfo() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipperInitInfo()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 RootShipperFolder=None


class ShipperServiceLink(DbObject):
 """
 ShipperServiceLink()
 ShipperServiceLink(erpDeliveryMethodCode: str,erpDeliveryMethodDescription: str,shipperId: str,serviceLevel: str,allowDifferentChoice: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipperServiceLink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,erpDeliveryMethodCode=None,erpDeliveryMethodDescription=None,shipperId=None,serviceLevel=None,allowDifferentChoice=None):
  """
  __new__(cls: type)
  __new__(cls: type,erpDeliveryMethodCode: str,erpDeliveryMethodDescription: str,shipperId: str,serviceLevel: str,allowDifferentChoice: bool)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AllowDifferentChoice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowDifferentChoice(self: ShipperServiceLink) -> bool

Set: AllowDifferentChoice(self: ShipperServiceLink)=value
"""

 ErpDeliveryMethodCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ErpDeliveryMethodCode(self: ShipperServiceLink) -> str

Set: ErpDeliveryMethodCode(self: ShipperServiceLink)=value
"""

 ErpDeliveryMethodDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ErpDeliveryMethodDescription(self: ShipperServiceLink) -> str

Set: ErpDeliveryMethodDescription(self: ShipperServiceLink)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: ShipperServiceLink) -> int

Set: Id(self: ShipperServiceLink)=value
"""

 ServiceLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ServiceLevel(self: ShipperServiceLink) -> str

Set: ServiceLevel(self: ShipperServiceLink)=value
"""

 ShipperId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperId(self: ShipperServiceLink) -> str

Set: ShipperId(self: ShipperServiceLink)=value
"""



class ShipperServiceLinks(FindableList):
 """
 ShipperServiceLinks()
 ShipperServiceLinks(items: Array[ShipperServiceLink])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipperServiceLinks()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,items=None):
  """
  __new__(cls: type)
  __new__(cls: type,items: Array[ShipperServiceLink])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='ErpDeliveryMethodCode'
 ValueMember='Id'


class State:
 """
 Current state of the Wms.RemotingObjects.ShippingLayers.TransportItem.
    In a normal process a TransportItems goes through all the states.
 
 enum State,values: Packed (2),Picked (0),Processed (1),Shipped (3)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return State()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Packed=None
 Picked=None
 Processed=None
 Shipped=None
 value__=None


class TransportItem(object):
 """
 TransportItem()
 TransportItem(line: OutboundOrderLine,boxGuid: Guid,itemIds: ItemIdentifications,innerReference: str)
 TransportItem(line: OutboundOrderLine,boxGuid: Guid,quantity: Decimal,quantityProcessed: Decimal,registerItemIdsDuringPacking: bool,innerReference: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransportItem()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """
  Clone(self: TransportItem) -> object
  
   Creates shallow clone.
  """
  pass
 def CloneWithSpecificOutboundOrder(self,orderNumber):
  """ CloneWithSpecificOutboundOrder(self: TransportItem,orderNumber: str) -> object """
  pass
 def CopyTo(self,item,itemIds=None):
  """
  CopyTo(self: TransportItem,item: TransportItem)CopyTo(self: TransportItem,item: TransportItem,itemIds: ItemIdentifications)
   Copies the contents of this item to the given item with only the itemidentifications given in the
     second parameter
  
   item: The item to wich the contents of this item have to be copied.
   itemIds: The itemidentifications to copy to the new item.
  """
  pass
 def ResetQuantity(self):
  """ ResetQuantity(self: TransportItem) """
  pass
 def SetQuantityOriginal(self):
  """ SetQuantityOriginal(self: TransportItem) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,line=None,boxGuid=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,line: OutboundOrderLine,boxGuid: Guid,itemIds: ItemIdentifications,innerReference: str)
  __new__(cls: type,line: OutboundOrderLine,boxGuid: Guid,quantity: Decimal,quantityProcessed: Decimal,registerItemIdsDuringPacking: bool,innerReference: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BatchId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BatchId(self: TransportItem) -> str

Set: BatchId(self: TransportItem)=value
"""

 BatchIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: BatchIds(self: TransportItem) -> List[str]

Set: BatchIds(self: TransportItem)=value
"""

 Colors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Colors(self: TransportItem) -> List[str]

Set: Colors(self: TransportItem)=value
"""

 Currency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The currency of the item sales price

Get: Currency(self: TransportItem) -> str

Set: Currency(self: TransportItem)=value
"""

 DbKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DbKey(self: TransportItem) -> int

Set: DbKey(self: TransportItem)=value
"""

 DefaultVendorItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DefaultVendorItemCode(self: TransportItem) -> str

Set: DefaultVendorItemCode(self: TransportItem)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Comes from: Wms.RemotingObjects.Outbound.OutboundOrderLine.LineDescription

Get: Description(self: TransportItem) -> str

Set: Description(self: TransportItem)=value
"""

 GTINCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The GTIN of this item

Get: GTINCode(self: TransportItem) -> str

Set: GTINCode(self: TransportItem)=value
"""

 InnerReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: InnerReference(self: TransportItem) -> str

Set: InnerReference(self: TransportItem)=value
"""

 Instruction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Instruction(self: TransportItem) -> str

Set: Instruction(self: TransportItem)=value
"""

 IsBatchNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsBatchNumberItem(self: TransportItem) -> bool

Set: IsBatchNumberItem(self: TransportItem)=value
"""

 IsExtraItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsExtraItem(self: TransportItem) -> bool

Set: IsExtraItem(self: TransportItem)=value
"""

 IsFractionAllowed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsFractionAllowed(self: TransportItem) -> bool

Set: IsFractionAllowed(self: TransportItem)=value
"""

 IsSerialNumberItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsSerialNumberItem(self: TransportItem) -> bool

Set: IsSerialNumberItem(self: TransportItem)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: TransportItem) -> str

Set: ItemCode(self: TransportItem)=value
"""

 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemIds(self: TransportItem) -> ItemIdentifications

Set: ItemIds(self: TransportItem)=value
"""

 ItemSalesPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The item sales price excluding VAT

Get: ItemSalesPrice(self: TransportItem) -> Decimal

Set: ItemSalesPrice(self: TransportItem)=value
"""

 ItemSalesPriceSingleWithVat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemSalesPriceSingleWithVat(self: TransportItem) -> Decimal

Set: ItemSalesPriceSingleWithVat(self: TransportItem)=value
"""

 ItemWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemWeight(self: TransportItem) -> Decimal

Set: ItemWeight(self: TransportItem)=value
"""

 OutboundOrderItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OutboundOrderItems(self: TransportItem) -> OutboundOrderItems

Set: OutboundOrderItems(self: TransportItem)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Amount of products in  this item.
   Either sum of quantities of item-ids or Quantity itself.

Get: Quantity(self: TransportItem) -> Decimal

Set: Quantity(self: TransportItem)=value
"""

 QuantityOriginal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityOriginal(self: TransportItem) -> Decimal

Set: QuantityOriginal(self: TransportItem)=value
"""

 QuantityProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityProcessed(self: TransportItem) -> Decimal

Set: QuantityProcessed(self: TransportItem)=value
"""

 RegisterItemIdsDuringPacking=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RegisterItemIdsDuringPacking(self: TransportItem) -> bool

Set: RegisterItemIdsDuringPacking(self: TransportItem)=value
"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: State(self: TransportItem) -> State

Set: State(self: TransportItem)=value
"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique id of this Wms.RemotingObjects.ShippingLayers.TransportItem

Get: UniqueId(self: TransportItem) -> str

"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: TransportItem) -> str

Set: UnitCode(self: TransportItem)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: TransportItem) -> str

Set: WarehouseCode(self: TransportItem)=value
"""



class TransportItems(FindableList):
 """
 TransportItems()
 TransportItems(items: IEnumerable[TransportItem])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransportItems()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,item,includingItemIds=None):
  """ Add(self: TransportItems,item: TransportItem)Add(self: TransportItems,item: TransportItem,includingItemIds: bool) """
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
 def Remove(self,*__args):
  """ Remove(self: TransportItems,item: TransportItem,removeWhenNothingLeft: bool,compareItemIdsForOutboundOrder: bool) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,items=None):
  """
  __new__(cls: type)
  __new__(cls: type,items: IEnumerable[TransportItem])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Description'
 ValueMember='UniqueId'


class TransportOptions(object):
 """ TransportOptions() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransportOptions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomFields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomFields(self: TransportOptions) -> SerializableDictionary[str,object]

Set: CustomFields(self: TransportOptions)=value
"""

 DeliveryBegin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryBegin(self: TransportOptions) -> Nullable[DateTime]

Set: DeliveryBegin(self: TransportOptions)=value
"""

 DeliveryEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeliveryEnd(self: TransportOptions) -> Nullable[DateTime]

Set: DeliveryEnd(self: TransportOptions)=value
"""

 IsShipperServiceLinkSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsShipperServiceLinkSet(self: TransportOptions) -> bool

"""

 Pickup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Pickup(self: TransportOptions) -> Nullable[DateTime]

Set: Pickup(self: TransportOptions)=value
"""

 Shipper=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Shipper(self: TransportOptions) -> str

Set: Shipper(self: TransportOptions)=value
"""

 ShipperDisallowDifferentChoice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperDisallowDifferentChoice(self: TransportOptions) -> bool

Set: ShipperDisallowDifferentChoice(self: TransportOptions)=value
"""

 ShipperServiceLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipperServiceLevel(self: TransportOptions) -> str

Set: ShipperServiceLevel(self: TransportOptions)=value
"""



class TransportPackage(PackageBase):
 """
 TransportPackage(boxGuid: Guid)
 TransportPackage()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransportPackage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: TransportPackage) -> object """
  pass
 def CreateExtraTransportItemOfOrderLine(self,line):
  """ CreateExtraTransportItemOfOrderLine(self: TransportPackage,line: OutboundOrderLine) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,boxGuid=None):
  """
  __new__(cls: type,boxGuid: Guid)
  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 CashAmount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CashAmount(self: TransportPackage) -> Decimal

Set: CashAmount(self: TransportPackage)=value
"""

 IsMixedCollo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this Wms.RemotingObjects.ShippingLayers.TransportPackage is a mixed collo (it has multiple items). If not,then
   it's a homogeneous pallet.

Get: IsMixedCollo(self: TransportPackage) -> bool

"""

 Shipment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Shipment(self: TransportPackage) -> ShipmentBase

"""

 StockRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StockRegistration(self: TransportPackage) -> StockRegistrationForColliEnum

Set: StockRegistration(self: TransportPackage)=value
"""

 TransportItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TransportItems(self: TransportPackage) -> TransportItems

Set: TransportItems(self: TransportPackage)=value
"""



class TransportPackages(FindableList):
 """
 TransportPackages()
 TransportPackages(batches: Batches)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransportPackages()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddNew(self,basedOn=None,boxId=None,outerReference=None):
  """
  AddNew(self: TransportPackages) -> Guid
  AddNew(self: TransportPackages,basedOn: ColliPreset) -> Guid
  AddNew(self: TransportPackages,basedOn: ColliPreset,boxId: str,outerReference: str) -> Guid
  """
  pass
 def AddTransportItemToPackage(self,boxGuid,transItem):
  """ AddTransportItemToPackage(self: TransportPackages,boxGuid: Guid,transItem: TransportItem) """
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
 def GetTransportItems(self,boxGuid):
  """ GetTransportItems(self: TransportPackages,boxGuid: Guid) -> TransportItems """
  pass
 def MoveTransportItems(self,fromBoxGuid,toBoxGuid,items,includingItemIds):
  """ MoveTransportItems(self: TransportPackages,fromBoxGuid: Guid,toBoxGuid: Guid,items: TransportItems,includingItemIds: bool) -> bool """
  pass
 def Remove(self,*__args):
  """
  Remove(self: TransportPackages,boxGuid: Guid) -> bool
  
   Returns the package needs to be empty before removal.
     Boxnumbers are renumbered if a package is removed in the middle
  
   boxGuid: BoxNr
  """
  pass
 def SetReferences(self,boxGuid):
  """
  SetReferences(self: TransportPackages,boxGuid: Guid)
   Sets the order and customer references using the order data in this object.
  """
  pass
 def Update(self,*__args):
  """ Update(self: TransportPackages,newPackageData: TransportPackage) -> bool """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,batches=None):
  """
  __new__(cls: type)
  __new__(cls: type,batches: Batches)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 AreOutboundOrdersProcessed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if all orders are processed,otherwise false.

Get: AreOutboundOrdersProcessed(self: TransportPackages) -> bool

Set: AreOutboundOrdersProcessed(self: TransportPackages)=value
"""

 ArePackagesRegistered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArePackagesRegistered(self: TransportPackages) -> bool

Set: ArePackagesRegistered(self: TransportPackages)=value
"""

 Batches=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Batches(self: TransportPackages) -> Batches

"""

 Customer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Contains the Wms.RemotingObjects.ShippingLayers.TransportPackages.Customer object with the pending salesorders. This will be used during 
   processing so the orderlines in the batches are matched to the correct customer and order.

Get: Customer(self: TransportPackages) -> PackCustomer

Set: Customer(self: TransportPackages)=value
"""

 InvoiceAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: InvoiceAddress(self: TransportPackages) -> Address

Set: InvoiceAddress(self: TransportPackages)=value
"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDisposable(self: TransportPackages) -> bool

"""

 IsHistoricShipment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if these Wms.RemotingObjects.ShippingLayers.TransportPackages belong to a historic shipment.

Get: IsHistoricShipment(self: TransportPackages) -> bool

"""

 IsModifiedHistoryShipment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsModifiedHistoryShipment(self: TransportPackages) -> bool

Set: IsModifiedHistoryShipment(self: TransportPackages)=value
"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Options(self: TransportPackages) -> TransportOptions

Set: Options(self: TransportPackages)=value
"""

 OrderNotes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNotes(self: TransportPackages) -> str

Set: OrderNotes(self: TransportPackages)=value
"""

 OurReferences=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The order numbers

Get: OurReferences(self: TransportPackages) -> List[str]

"""

 PackageSlipNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageSlipNumbers(self: TransportPackages) -> List[str]

Set: PackageSlipNumbers(self: TransportPackages)=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreserveState(self: TransportPackages) -> bool

"""

 ProcessedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessedBy(self: TransportPackages) -> Session

Set: ProcessedBy(self: TransportPackages)=value
"""

 ProcessState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessState(self: TransportPackages) -> ProcessShipmentStepsEnum

Set: ProcessState(self: TransportPackages)=value
"""

 ReceiveAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReceiveAddress(self: TransportPackages) -> Address

Set: ReceiveAddress(self: TransportPackages)=value
"""

 SendAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SendAddress(self: TransportPackages) -> Address

Set: SendAddress(self: TransportPackages)=value
"""

 SessionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SessionCount(self: TransportPackages) -> int

Set: SessionCount(self: TransportPackages)=value
"""

 SessionHashCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SessionHashCode(self: TransportPackages) -> int

Set: SessionHashCode(self: TransportPackages)=value
"""

 ShipmentKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentKey(self: TransportPackages) -> int

Set: ShipmentKey(self: TransportPackages)=value
"""

 ShipmentNotes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ShipmentNotes(self: TransportPackages) -> str

Set: ShipmentNotes(self: TransportPackages)=value
"""

 TotalVolume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cubic meters of all packages

Get: TotalVolume(self: TransportPackages) -> Decimal

"""



class TypeOfDay:
 """ enum TypeOfDay,values: WeekDays (1),WorkingDays (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TypeOfDay()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 value__=None
 WeekDays=None
 WorkingDays=None


class UpdateTransportPackageArgs(object):
 """ UpdateTransportPackageArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UpdateTransportPackageArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CacheKey(self: UpdateTransportPackageArgs) -> CacheKey

Set: CacheKey(self: UpdateTransportPackageArgs)=value
"""

 ValidateItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ValidateItem(self: UpdateTransportPackageArgs) -> bool

Set: ValidateItem(self: UpdateTransportPackageArgs)=value
"""



class UpdateTransportPackagesHeaderArgs(object):
 """ UpdateTransportPackagesHeaderArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UpdateTransportPackagesHeaderArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Customer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Customer(self: UpdateTransportPackagesHeaderArgs) -> PackCustomer

Set: Customer(self: UpdateTransportPackagesHeaderArgs)=value
"""

 InvoiceAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: InvoiceAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: InvoiceAddress(self: UpdateTransportPackagesHeaderArgs)=value
"""

 ReceiveAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: ReceiveAddress(self: UpdateTransportPackagesHeaderArgs)=value
"""

 SendAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SendAddress(self: UpdateTransportPackagesHeaderArgs) -> Address

Set: SendAddress(self: UpdateTransportPackagesHeaderArgs)=value
"""

 ShipmentNotes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShipmentNotes(self: UpdateTransportPackagesHeaderArgs) -> str

Set: ShipmentNotes(self: UpdateTransportPackagesHeaderArgs)=value
"""

 TransportOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TransportOptions(self: UpdateTransportPackagesHeaderArgs) -> TransportOptions

Set: TransportOptions(self: UpdateTransportPackagesHeaderArgs)=value
"""



# variables with complex values

