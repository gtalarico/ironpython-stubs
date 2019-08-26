# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.GS1.Mapping calls itself Mapping
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintLineToGS1MapperBase:
    # no doc
    def ConvertToBarcode(self, propertyName, value, provider):
        """
        ConvertToBarcode(self: PrintLineToGS1MapperBase, propertyName: str, value: object, provider: IFormatProvider) -> IGeneratedBarcode
        
            provider: (Optional) The culture that should be used to parse the value before converting it to the barcode value
        """
        pass

    def FormatValue(self, propertyName, value):
        """ FormatValue(self: PrintLineToGS1MapperBase, propertyName: str, value: object) -> object """
        pass

    def GetMapping(self, propertyName):
        """ GetMapping(self: PrintLineToGS1MapperBase, propertyName: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = PrintLineToGS1MapperBase()
    """hardcoded/returns an instance of the class"""

class HomogeneousPalletMapper(PrintLineToGS1MapperBase):
    """ HomogeneousPalletMapper() """
    def ConvertToBarcode(self, propertyName, value, provider):
        """
        ConvertToBarcode(self: HomogeneousPalletMapper, propertyName: str, value: object, provider: IFormatProvider) -> IGeneratedBarcode
        
            provider: (Optional) The culture that should be used to parse the value before converting it to the barcode value
        """
        pass

    def FormatValue(self, propertyName, value):
        """ FormatValue(self: HomogeneousPalletMapper, propertyName: str, value: object) -> object """
        pass

    def GetMapping(self, propertyName):
        """ GetMapping(self: HomogeneousPalletMapper, propertyName: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = HomogeneousPalletMapper()
    """hardcoded/returns an instance of the class"""

class IPrintlineToGS1Mapper:
    # no doc
    def ConvertToBarcode(self, propertyName, value, provider):
        """ ConvertToBarcode(self: IPrintlineToGS1Mapper, propertyName: str, value: object, provider: IFormatProvider) -> IGeneratedBarcode """
        pass

    def FormatValue(self, propertyName, value):
        """ FormatValue(self: IPrintlineToGS1Mapper, propertyName: str, value: object) -> object """
        pass

    def GetMapping(self, propertyName):
        """ GetMapping(self: IPrintlineToGS1Mapper, propertyName: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = IPrintlineToGS1Mapper()
    """hardcoded/returns an instance of the class"""

class MixedPalletMapper(PrintLineToGS1MapperBase):
    """ MixedPalletMapper() """
    def GetMapping(self, propertyName):
        """ GetMapping(self: MixedPalletMapper, propertyName: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Instance = MixedPalletMapper()
    """hardcoded/returns an instance of the class"""

class PrintLineToGS1MapperFactory():
    # no doc
    @staticmethod
    def GetMapper(datasetName):
        """ GetMapper(datasetName: str) -> IPrintlineToGS1Mapper """
        pass

    __all__ = [
        'GetMapper',
    ]

    Instance = PrintLineToGS1MapperFactory()
    """hardcoded/returns an instance of the class"""

