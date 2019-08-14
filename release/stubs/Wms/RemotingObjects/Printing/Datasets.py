# encoding: utf-8
# module Wms.RemotingObjects.Printing.Datasets calls itself Datasets
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintDatasetBase():
    """  """
    Instance = PrintDatasetBase
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: PrintDatasetBase, userName: str, source: PrintLinesBase) -> DataTable
        
            source: an object that holds the lines to print.
            Returns: a filled dataset with values from source.
        CreateFrom(self: PrintDatasetBase, userName: str, source: PrintLineBase) -> DataTable
        
            source: an object that holds the line to print.
            Returns: a filled dataset with values from source.
        """
        pass

    def CreateItemRowFrom(self, *args): #cannot find CLR method
        """ CreateItemRowFrom(self: PrintDatasetBase, userName: str, line: PrintLineBase) -> DataRow """
        pass

    def CreateRowsFrom(self, *args): #cannot find CLR method
        """ CreateRowsFrom(self: PrintDatasetBase, userName: str, line: PrintLineBase) -> Array[DataRow] """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: PrintDatasetBase, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        
            source: an object that holds the line to print.
            Returns: a filled dataset with values from source.
        CreateWithItems(self: PrintDatasetBase, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        
            source: an object that holds the line to print.
            Returns: a filled dataset with values from source.
        """
        pass

    def Empty(self):
        """
        Empty(self: PrintDatasetBase) -> DataTable
            Returns: An empty dataset, but with all possible columns specfied.
        """
        pass

    def EmptyItems(self):
        """
        EmptyItems(self: PrintDatasetBase) -> DataTable
            Returns: an empty dataset, but with all possible columns specfied.
        """
        pass

    def GetTestData(self):
        """
        GetTestData(self: PrintDatasetBase) -> PrintLinesBase
        
            Return value needs to be cast before usage.
            Returns: An object that can be used to put in the cache, and to print a test page afterwards.
        """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: PrintDatasetBase) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies to which PrintLines object this dataset is applicable.

Get: DesignedForPrintLines(self: PrintDatasetBase) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the dataset has multiple items

Get: HasItems(self: PrintDatasetBase) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the dataset

Get: Name(self: PrintDatasetBase) -> str

"""

    OneLabelPerPrintAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if only 1 label should be printed, overrides given NumberOfCopies

Get: OneLabelPerPrintAction(self: PrintDatasetBase) -> bool

Set: OneLabelPerPrintAction(self: PrintDatasetBase) = value
"""


    Date = 'Date'
    Employee = 'Employee'
    NumberOfCopies = 'NumberOfCopies'
    Quantity = 'Quantity'


class BarcodeDataset(PrintDatasetBase):
    """ BarcodeDataset() """
    Instance = BarcodeDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: BarcodeDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        CreateFrom(self: BarcodeDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: BarcodeDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: BarcodeDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: BarcodeDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: BarcodeDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: BarcodeDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: BarcodeDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: BarcodeDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: BarcodeDataset) -> str

"""



class ItemPrintDataset(PrintDatasetBase):
    """ ItemPrintDataset() """
    Instance = ItemPrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: ItemPrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an ItemPrintLines object!
        CreateFrom(self: ItemPrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an ItemPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: ItemPrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: ItemPrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: ItemPrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: ItemPrintDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: ItemPrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: ItemPrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: ItemPrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ItemPrintDataset) -> str

"""



class ItemWithItemIdPrintDataset(PrintDatasetBase):
    """ ItemWithItemIdPrintDataset() """
    Instance = ItemWithItemIdPrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: ItemWithItemIdPrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an ItemPrintLines object!
        CreateFrom(self: ItemWithItemIdPrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an ItemPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: ItemWithItemIdPrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: ItemWithItemIdPrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: ItemWithItemIdPrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: ItemWithItemIdPrintDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: ItemWithItemIdPrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: ItemWithItemIdPrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: ItemWithItemIdPrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ItemWithItemIdPrintDataset) -> str

"""



class LicensePlatePrintDataset(PrintDatasetBase):
    """ LicensePlatePrintDataset() """
    Instance = LicensePlatePrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: LicensePlatePrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        CreateFrom(self: LicensePlatePrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: LicensePlatePrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: LicensePlatePrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: LicensePlatePrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: LicensePlatePrintDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: LicensePlatePrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: LicensePlatePrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: LicensePlatePrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: LicensePlatePrintDataset) -> str

"""



class PickbatchPrintDataset(PrintDatasetBase):
    """ PickbatchPrintDataset() """
    Instance = PickbatchPrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: PickbatchPrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an PickbatchPrintLines object!
        CreateFrom(self: PickbatchPrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an PickbatchPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: PickbatchPrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: PickbatchPrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: PickbatchPrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: PickbatchPrintDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: PickbatchPrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: PickbatchPrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: PickbatchPrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: PickbatchPrintDataset) -> str

"""



class PurchaseItemIdPrintDataset(PrintDatasetBase):
    """ PurchaseItemIdPrintDataset() """
    Instance = PurchaseItemIdPrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: PurchaseItemIdPrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        CreateFrom(self: PurchaseItemIdPrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: PurchaseItemIdPrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: PurchaseItemIdPrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: PurchaseItemIdPrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """
        GetTestData(self: PurchaseItemIdPrintDataset) -> PrintLinesBase
            Returns: An OrderPrintLine to be able to send to the cache, after which 
                    Broker.Inbound.PrintPurchaseOrderPrintLines can be called.
        """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: PurchaseItemIdPrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: PurchaseItemIdPrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: PurchaseItemIdPrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: PurchaseItemIdPrintDataset) -> str

"""



class PurchasePrintDataset(PrintDatasetBase):
    """ PurchasePrintDataset() """
    Instance = PurchasePrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: PurchasePrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        CreateFrom(self: PurchasePrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: PurchasePrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: PurchasePrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: PurchasePrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """
        GetTestData(self: PurchasePrintDataset) -> PrintLinesBase
            Returns: An OrderPrintLine to be able to send to the cache, after which 
                    Broker.Inbound.PrintPurchaseOrderPrintLines can be called.
        """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: PurchasePrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: PurchasePrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: PurchasePrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: PurchasePrintDataset) -> str

"""



class RmaPrintDataset(PrintDatasetBase):
    """ RmaPrintDataset() """
    Instance = RmaPrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: RmaPrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an RmaOrderPrintLines object!
        CreateFrom(self: RmaPrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an RmaOrderPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: RmaPrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: RmaPrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: RmaPrintDataset) -> DataTable """
        pass

    def GetTestData(self):
        """
        GetTestData(self: RmaPrintDataset) -> PrintLinesBase
            Returns: An RmaOrderPrintLine to be able to send to the cache, after which 
                    Broker.Inbound.PrintRmaOrderPrintLines can be called.
        """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: RmaPrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: RmaPrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: RmaPrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: RmaPrintDataset) -> str

"""



class SSCCHeterogeneousDataSet(PrintDatasetBase):
    """ SSCCHeterogeneousDataSet() """
    Instance = SSCCHeterogeneousDataSet
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: SSCCHeterogeneousDataSet, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        CreateFrom(self: SSCCHeterogeneousDataSet, userName: str, source: PrintLineBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: SSCCHeterogeneousDataSet, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: SSCCHeterogeneousDataSet, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: SSCCHeterogeneousDataSet) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: SSCCHeterogeneousDataSet) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: SSCCHeterogeneousDataSet) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: SSCCHeterogeneousDataSet) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: SSCCHeterogeneousDataSet) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: SSCCHeterogeneousDataSet) -> str

"""



class SSCCHomogeneousDataSet(PrintDatasetBase):
    """ SSCCHomogeneousDataSet() """
    Instance = SSCCHomogeneousDataSet
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: SSCCHomogeneousDataSet, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        CreateFrom(self: SSCCHomogeneousDataSet, userName: str, source: PrintLineBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.BarcodePrintLines
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: SSCCHomogeneousDataSet, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: SSCCHomogeneousDataSet, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: SSCCHomogeneousDataSet) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: SSCCHomogeneousDataSet) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: SSCCHomogeneousDataSet) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: SSCCHomogeneousDataSet) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: SSCCHomogeneousDataSet) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: SSCCHomogeneousDataSet) -> str

"""



class SSCCPregeneratedDataset(PrintDatasetBase):
    """ SSCCPregeneratedDataset() """
    Instance = SSCCPregeneratedDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: SSCCPregeneratedDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.SSCCBasePrintLines
        CreateFrom(self: SSCCPregeneratedDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Wms.RemotingObjects.Printing.SSCCBasePrintLine
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: SSCCPregeneratedDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: SSCCPregeneratedDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        """
        pass

    def Empty(self):
        """ Empty(self: SSCCPregeneratedDataset) -> DataTable """
        pass

    def GetTestData(self):
        """ GetTestData(self: SSCCPregeneratedDataset) -> PrintLinesBase """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: SSCCPregeneratedDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: SSCCPregeneratedDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: SSCCPregeneratedDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: SSCCPregeneratedDataset) -> str

"""



class TransportPackagePrintDataset(PrintDatasetBase):
    """ TransportPackagePrintDataset() """
    Instance = TransportPackagePrintDataset
    """hardcoded/returns an instance of the class"""
    def CreateFrom(self, userName, source):
        """
        CreateFrom(self: TransportPackagePrintDataset, userName: str, source: PrintLinesBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        CreateFrom(self: TransportPackagePrintDataset, userName: str, source: PrintLineBase) -> DataTable
        
            source: Should be an OrderPrintLines object!
        """
        pass

    def CreateWithItems(self, userName, source):
        """
        CreateWithItems(self: TransportPackagePrintDataset, userName: str, source: PrintLinesBase) -> Tuple[DataTable, DataTable]
        CreateWithItems(self: TransportPackagePrintDataset, userName: str, source: PrintLineBase) -> Tuple[DataTable, DataTable]
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

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Columns(self: TransportPackagePrintDataset) -> List[str]

"""

    DesignedForPrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DesignedForPrintLines(self: TransportPackagePrintDataset) -> Type

"""

    HasItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: HasItems(self: TransportPackagePrintDataset) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: TransportPackagePrintDataset) -> str

"""



