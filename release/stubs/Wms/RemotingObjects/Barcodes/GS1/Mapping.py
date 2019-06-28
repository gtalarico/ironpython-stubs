# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.GS1.Mapping calls itself Mapping
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PrintLineToGS1MapperBase:
    # no doc
    def ConvertToBarcode(self, propertyName, value, provider):
        """ ConvertToBarcode(self: PrintLineToGS1MapperBase, propertyName: str, value: object, provider: IFormatProvider) -> IGeneratedBarcode """
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


class HomogeneousPalletMapper:
    """ HomogeneousPalletMapper() """
    def ConvertToBarcode(self, propertyName, value, provider):
        """ ConvertToBarcode(self: HomogeneousPalletMapper, propertyName: str, value: object, provider: IFormatProvider) -> IGeneratedBarcode """
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


class MixedPalletMapper:
    """ MixedPalletMapper() """
    def GetMapping(self, propertyName):
        """ GetMapping(self: MixedPalletMapper, propertyName: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PrintLineToGS1MapperFactory:
    # no doc
    @staticmethod
    def GetMapper(datasetName):
        """ GetMapper(datasetName: str) -> IPrintlineToGS1Mapper """
        pass

    __all__ = [
        'GetMapper',
    ]


