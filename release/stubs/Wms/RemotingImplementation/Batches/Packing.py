# encoding: utf-8
# module Wms.RemotingImplementation.Batches.Packing calls itself Packing
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DefaultPackageCreator():
    """ DefaultPackageCreator(manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages, autoPackItems: bool, addNewPackages: bool) """
    def AddPackage(self, *args): #cannot find CLR method
        """ AddPackage(self: DefaultPackageCreator, generateSSCCNumber: bool) -> Guid """
        pass

    def AddTransportItem(self, *args): #cannot find CLR method
        """ AddTransportItem(self: DefaultPackageCreator, line: OutboundOrderLine, packLoc: ItemPackLocation, colloReference: str) -> TransportItem """
        pass

    def Cleanup(self, *args): #cannot find CLR method
        """ Cleanup(self: DefaultPackageCreator) """
        pass

    def Create(self):
        """ Create(self: DefaultPackageCreator) """
        pass

    def GetPackageGuidForPacking(self, *args): #cannot find CLR method
        """ GetPackageGuidForPacking(self: DefaultPackageCreator) -> Guid """
        pass

    def HasItemsLeft(self, *args): #cannot find CLR method
        """ HasItemsLeft(self: DefaultPackageCreator) -> bool """
        pass

    def PrepareItems(self, *args): #cannot find CLR method
        """ PrepareItems(self: DefaultPackageCreator) -> TransportItems """
        pass

    def ShouldAddExtraPackage(self, *args): #cannot find CLR method
        """ ShouldAddExtraPackage(self: DefaultPackageCreator) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, manager, customer, batches, packages, autoPackItems, addNewPackages):
        """ __new__(cls: type, manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages, autoPackItems: bool, addNewPackages: bool) """
        pass

    Customer = None
    Items = None
    TransportPackages = None
    _batches = None

    Instance = DefaultPackageCreator()
    """hardcoded/returns an instance of the class"""

class ColloReferencePacker(DefaultPackageCreator):
    """ ColloReferencePacker(manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages) """
    @staticmethod # known case of __new__
    def __new__(self, manager, customer, batches, packages):
        """ __new__(cls: type, manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages) """
        pass

    Customer = None
    Items = None
    TransportPackages = None
    _batches = None

    Instance = ColloReferencePacker()
    """hardcoded/returns an instance of the class"""

class OrderPackageCreator(DefaultPackageCreator):
    """ OrderPackageCreator(manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages) """
    @staticmethod # known case of __new__
    def __new__(self, manager, customer, batches, packages):
        """ __new__(cls: type, manager: BatchPackManager, customer: PackCustomer, batches: Batches, packages: TransportPackages) """
        pass

    Customer = None
    Items = None
    TransportPackages = None
    _batches = None

    Instance = OrderPackageCreator()
    """hardcoded/returns an instance of the class"""

class PackageCreatorFactory():
    # no doc
    @staticmethod
    def Create(packages, batches, customer):
        """ Create(packages: TransportPackages, batches: Batches, customer: PackCustomer) """
        pass

    __all__ = [
        'Create',
    ]

    Instance = PackageCreatorFactory()
    """hardcoded/returns an instance of the class"""

class TransportPackagesHelper():
    """ TransportPackagesHelper() """
    def AddTransportPackage(self, args):
        """ AddTransportPackage(self: TransportPackagesHelper, args: AddTransportPackageArgs) """
        pass

    def GetNewSSCC(self):
        """ GetNewSSCC(self: TransportPackagesHelper) -> str """
        pass

    NewPackageGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewPackageGuid(self: TransportPackagesHelper) -> Guid

"""

    Packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Packages(self: TransportPackagesHelper) -> TransportPackages

"""


    Instance = TransportPackagesHelper()
    """hardcoded/returns an instance of the class"""

