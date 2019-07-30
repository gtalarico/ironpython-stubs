# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.GS1.Mapping calls itself Mapping
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class PrintLineToGS1MapperBase(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintLineToGS1MapperBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ConvertToBarcode(self,propertyName,value,provider):
  """
  ConvertToBarcode(self: PrintLineToGS1MapperBase,propertyName: str,value: object,provider: IFormatProvider) -> IGeneratedBarcode
  
   provider: (Optional) The culture that should be used to parse the value before converting it to the barcode value
  """
  pass
 def FormatValue(self,propertyName,value):
  """ FormatValue(self: PrintLineToGS1MapperBase,propertyName: str,value: object) -> object """
  pass
 def GetMapping(self,propertyName):
  """ GetMapping(self: PrintLineToGS1MapperBase,propertyName: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class HomogeneousPalletMapper(PrintLineToGS1MapperBase):
 """ HomogeneousPalletMapper() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HomogeneousPalletMapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ConvertToBarcode(self,propertyName,value,provider):
  """
  ConvertToBarcode(self: HomogeneousPalletMapper,propertyName: str,value: object,provider: IFormatProvider) -> IGeneratedBarcode
  
   provider: (Optional) The culture that should be used to parse the value before converting it to the barcode value
  """
  pass
 def FormatValue(self,propertyName,value):
  """ FormatValue(self: HomogeneousPalletMapper,propertyName: str,value: object) -> object """
  pass
 def GetMapping(self,propertyName):
  """ GetMapping(self: HomogeneousPalletMapper,propertyName: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class IPrintlineToGS1Mapper:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IPrintlineToGS1Mapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ConvertToBarcode(self,propertyName,value,provider):
  """ ConvertToBarcode(self: IPrintlineToGS1Mapper,propertyName: str,value: object,provider: IFormatProvider) -> IGeneratedBarcode """
  pass
 def FormatValue(self,propertyName,value):
  """ FormatValue(self: IPrintlineToGS1Mapper,propertyName: str,value: object) -> object """
  pass
 def GetMapping(self,propertyName):
  """ GetMapping(self: IPrintlineToGS1Mapper,propertyName: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class MixedPalletMapper(PrintLineToGS1MapperBase):
 """ MixedPalletMapper() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MixedPalletMapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetMapping(self,propertyName):
  """ GetMapping(self: MixedPalletMapper,propertyName: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class PrintLineToGS1MapperFactory(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PrintLineToGS1MapperFactory()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetMapper(datasetName):
  """ GetMapper(datasetName: str) -> IPrintlineToGS1Mapper """
  pass
 __all__=[
  'GetMapper',
 ]


