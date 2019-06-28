# encoding: utf-8
# module Wms.RemotingObjects.BatchPacking calls itself BatchPacking
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ItemPackScanArgs:
 """ ItemPackScanArgs(cacheKey: CacheKey,barcode: str,packageGuid: Guid) """
 @staticmethod
 def __new__(self,cacheKey,barcode,packageGuid):
  """ __new__(cls: type,cacheKey: CacheKey,barcode: str,packageGuid: Guid) """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: ItemPackScanArgs) -> str

"""

 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: ItemPackScanArgs) -> CacheKey

"""

 PackageGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PackageGuid(self: ItemPackScanArgs) -> Guid

"""



class MoveAction:
 """ enum MoveAction,values: Ignore (0),MoveBetweenColli (3),Pack (1),Unpack (2) """
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
 Ignore=None
 MoveBetweenColli=None
 Pack=None
 Unpack=None
 value__=None


class MoveTransportItemsBetweenTransportPackagesArgs:
 """ MoveTransportItemsBetweenTransportPackagesArgs() """
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Action(self: MoveTransportItemsBetweenTransportPackagesArgs) -> MoveAction

Set: Action(self: MoveTransportItemsBetweenTransportPackagesArgs)=value
"""

 ItemsPacked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemsPacked(self: MoveTransportItemsBetweenTransportPackagesArgs) -> TransportPackages

Set: ItemsPacked(self: MoveTransportItemsBetweenTransportPackagesArgs)=value
"""

 ItemsToPack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemsToPack(self: MoveTransportItemsBetweenTransportPackagesArgs) -> TransportItems

Set: ItemsToPack(self: MoveTransportItemsBetweenTransportPackagesArgs)=value
"""

 ItemsToPackArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemsToPackArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) -> GetItemsToPackArgs

Set: ItemsToPackArgs(self: MoveTransportItemsBetweenTransportPackagesArgs)=value
"""

 MoveArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MoveArgs(self: MoveTransportItemsBetweenTransportPackagesArgs) -> MoveTransportPackageItemsArgs

Set: MoveArgs(self: MoveTransportItemsBetweenTransportPackagesArgs)=value
"""



class MoveTransportPackageItemsArgs:
 """ MoveTransportPackageItemsArgs() """
 @staticmethod
 def Validate(args):
  """ Validate(args: MoveTransportPackageItemsArgs) """
  pass
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: MoveTransportPackageItemsArgs) -> CacheKey

Set: CacheKey(self: MoveTransportPackageItemsArgs)=value
"""

 FromBoxGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromBoxGuid(self: MoveTransportPackageItemsArgs) -> Guid

Set: FromBoxGuid(self: MoveTransportPackageItemsArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: MoveTransportPackageItemsArgs) -> str

Set: OrderNumber(self: MoveTransportPackageItemsArgs)=value
"""

 ToBoxGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToBoxGuid(self: MoveTransportPackageItemsArgs) -> Guid

Set: ToBoxGuid(self: MoveTransportPackageItemsArgs)=value
"""

 TransportItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransportItems(self: MoveTransportPackageItemsArgs) -> TransportItems

Set: TransportItems(self: MoveTransportPackageItemsArgs)=value
"""



class ProcessBatchPackingArgs:
 """ ProcessBatchPackingArgs() """
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: ProcessBatchPackingArgs) -> CacheKey

Set: CacheKey(self: ProcessBatchPackingArgs)=value
"""

 ValidateStock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ValidateStock(self: ProcessBatchPackingArgs) -> Nullable[bool]

Set: ValidateStock(self: ProcessBatchPackingArgs)=value
"""



class ScanItemPackArgsResult:
 """ ScanItemPackArgsResult() """
 BarcodeStructure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BarcodeStructure(self: ScanItemPackArgsResult) -> BarcodeStructure

Set: BarcodeStructure(self: ScanItemPackArgsResult)=value
"""

 ResultType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ResultType(self: ScanItemPackArgsResult) -> ScanItemPackResultType

Set: ResultType(self: ScanItemPackArgsResult)=value
"""

 ScanResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ScanResult(self: ScanItemPackArgsResult) -> BarcodeStructureResultEnum

Set: ScanResult(self: ScanItemPackArgsResult)=value
"""



class ScanItemPackResultType:
 """ enum ScanItemPackResultType,values: InnerReference (1),Item (0) """
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
 InnerReference=None
 Item=None
 value__=None


class TransportPackageScanEnum:
 """ enum TransportPackageScanEnum,values: None (0),Serial (2),SSCC (1) """
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
 None_ =None
 Serial=None
 SSCC=None
 value__=None


class TransportPackageScanResult:
 """ TransportPackageScanResult() """
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Barcode(self: TransportPackageScanResult) -> str

Set: Barcode(self: TransportPackageScanResult)=value
"""

 FaultMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FaultMessage(self: TransportPackageScanResult) -> str

Set: FaultMessage(self: TransportPackageScanResult)=value
"""

 MatchedScanOfType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MatchedScanOfType(self: TransportPackageScanResult) -> TransportPackageScanEnum

Set: MatchedScanOfType(self: TransportPackageScanResult)=value
"""



