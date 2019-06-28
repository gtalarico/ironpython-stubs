# encoding: utf-8
# module Wms.RemotingObjects.Printing.Datasets calls itself Datasets
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintDatasetBase:
 # no doc
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: PrintDatasetBase,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: PrintDatasetBase,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateItemRowFrom(self,*args):
  """ CreateItemRowFrom(self: PrintDatasetBase,userName: str,line: PrintLineBase) -> DataRow """
  pass
 def CreateRowsFrom(self,*args):
  """ CreateRowsFrom(self: PrintDatasetBase,userName: str,line: PrintLineBase) -> Array[DataRow] """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: PrintDatasetBase,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: PrintDatasetBase,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: PrintDatasetBase) -> DataTable """
  pass
 def EmptyItems(self):
  """ EmptyItems(self: PrintDatasetBase) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: PrintDatasetBase) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: PrintDatasetBase) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: PrintDatasetBase) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: PrintDatasetBase) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PrintDatasetBase) -> str

"""

 OneLabelPerPrintAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OneLabelPerPrintAction(self: PrintDatasetBase) -> bool

Set: OneLabelPerPrintAction(self: PrintDatasetBase)=value
"""


 Date='Date'
 Employee='Employee'
 NumberOfCopies='NumberOfCopies'
 Quantity='Quantity'


class BarcodeDataset:
 """ BarcodeDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: BarcodeDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: BarcodeDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: BarcodeDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: BarcodeDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: BarcodeDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: BarcodeDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: BarcodeDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: BarcodeDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: BarcodeDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: BarcodeDataset) -> str

"""



class ItemPrintDataset:
 """ ItemPrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: ItemPrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: ItemPrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: ItemPrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: ItemPrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: ItemPrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: ItemPrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: ItemPrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: ItemPrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: ItemPrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ItemPrintDataset) -> str

"""



class ItemWithItemIdPrintDataset:
 """ ItemWithItemIdPrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: ItemWithItemIdPrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: ItemWithItemIdPrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: ItemWithItemIdPrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: ItemWithItemIdPrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: ItemWithItemIdPrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: ItemWithItemIdPrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: ItemWithItemIdPrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: ItemWithItemIdPrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: ItemWithItemIdPrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: ItemWithItemIdPrintDataset) -> str

"""



class LicensePlatePrintDataset:
 """ LicensePlatePrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: LicensePlatePrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: LicensePlatePrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: LicensePlatePrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: LicensePlatePrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: LicensePlatePrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: LicensePlatePrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: LicensePlatePrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: LicensePlatePrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: LicensePlatePrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: LicensePlatePrintDataset) -> str

"""



class PickbatchPrintDataset:
 """ PickbatchPrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: PickbatchPrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: PickbatchPrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: PickbatchPrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: PickbatchPrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: PickbatchPrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: PickbatchPrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: PickbatchPrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: PickbatchPrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: PickbatchPrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PickbatchPrintDataset) -> str

"""



class PurchaseItemIdPrintDataset:
 """ PurchaseItemIdPrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: PurchaseItemIdPrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: PurchaseItemIdPrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: PurchaseItemIdPrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: PurchaseItemIdPrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: PurchaseItemIdPrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: PurchaseItemIdPrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: PurchaseItemIdPrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: PurchaseItemIdPrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: PurchaseItemIdPrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PurchaseItemIdPrintDataset) -> str

"""



class PurchasePrintDataset:
 """ PurchasePrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: PurchasePrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: PurchasePrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: PurchasePrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: PurchasePrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: PurchasePrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: PurchasePrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: PurchasePrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: PurchasePrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: PurchasePrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: PurchasePrintDataset) -> str

"""



class RmaPrintDataset:
 """ RmaPrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: RmaPrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: RmaPrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: RmaPrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: RmaPrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: RmaPrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: RmaPrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: RmaPrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: RmaPrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: RmaPrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: RmaPrintDataset) -> str

"""



class SSCCHeterogeneousDataSet:
 """ SSCCHeterogeneousDataSet() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: SSCCHeterogeneousDataSet,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: SSCCHeterogeneousDataSet,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: SSCCHeterogeneousDataSet,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: SSCCHeterogeneousDataSet,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: SSCCHeterogeneousDataSet) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: SSCCHeterogeneousDataSet) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: SSCCHeterogeneousDataSet) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: SSCCHeterogeneousDataSet) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: SSCCHeterogeneousDataSet) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: SSCCHeterogeneousDataSet) -> str

"""



class SSCCHomogeneousDataSet:
 """ SSCCHomogeneousDataSet() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: SSCCHomogeneousDataSet,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: SSCCHomogeneousDataSet,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: SSCCHomogeneousDataSet,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: SSCCHomogeneousDataSet,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: SSCCHomogeneousDataSet) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: SSCCHomogeneousDataSet) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: SSCCHomogeneousDataSet) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: SSCCHomogeneousDataSet) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: SSCCHomogeneousDataSet) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: SSCCHomogeneousDataSet) -> str

"""



class SSCCPregeneratedDataset:
 """ SSCCPregeneratedDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: SSCCPregeneratedDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: SSCCPregeneratedDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: SSCCPregeneratedDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: SSCCPregeneratedDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: SSCCPregeneratedDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: SSCCPregeneratedDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: SSCCPregeneratedDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: SSCCPregeneratedDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: SSCCPregeneratedDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: SSCCPregeneratedDataset) -> str

"""



class TransportPackagePrintDataset:
 """ TransportPackagePrintDataset() """
 def CreateFrom(self,userName,source):
  """
  CreateFrom(self: TransportPackagePrintDataset,userName: str,source: PrintLinesBase) -> DataTable
  CreateFrom(self: TransportPackagePrintDataset,userName: str,source: PrintLineBase) -> DataTable
  """
  pass
 def CreateWithItems(self,userName,source):
  """
  CreateWithItems(self: TransportPackagePrintDataset,userName: str,source: PrintLinesBase) -> Tuple[DataTable,DataTable]
  CreateWithItems(self: TransportPackagePrintDataset,userName: str,source: PrintLineBase) -> Tuple[DataTable,DataTable]
  """
  pass
 def Empty(self):
  """ Empty(self: TransportPackagePrintDataset) -> DataTable """
  pass
 def EmptyItems(self):
  """ EmptyItems(self: TransportPackagePrintDataset) -> DataTable """
  pass
 def GetTestData(self):
  """ GetTestData(self: TransportPackagePrintDataset) -> PrintLinesBase """
  pass
 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Columns(self: TransportPackagePrintDataset) -> List[str]

"""

 DesignedForPrintLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DesignedForPrintLines(self: TransportPackagePrintDataset) -> Type

"""

 HasItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasItems(self: TransportPackagePrintDataset) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: TransportPackagePrintDataset) -> str

"""



