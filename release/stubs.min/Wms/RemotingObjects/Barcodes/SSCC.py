# encoding: utf-8
# module Wms.RemotingObjects.Barcodes.SSCC calls itself SSCC
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GS1Prefixes:
 # no doc
 Prefixes=None
 __all__=[]


class SSCC:
 """
 SSCC(barcode: str)
 SSCC(extensionDigit: int,companyPrefix: str,serial: int)
 """
 def Equals(self,*__args):
  """
  Equals(self: SSCC,other: SSCC) -> bool
  Equals(self: SSCC,obj: object) -> bool
  """
  pass
 @staticmethod
 def Get(barcode):
  """ Get(barcode: str) -> IGeneratedBarcode """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: SSCC) -> int """
  pass
 def HasValidCompanyPrefix(self):
  """ HasValidCompanyPrefix(self: SSCC) -> bool """
  pass
 @staticmethod
 def IsValid(barcode):
  """ IsValid(barcode: str) -> bool """
  pass
 def ToBarcode(self,includeApplicationIdentifier=None):
  """
  ToBarcode(self: SSCC) -> str
  ToBarcode(self: SSCC,includeApplicationIdentifier: bool) -> str
  """
  pass
 def ToReadableCode(self,includeApplicationIdentifier=None):
  """
  ToReadableCode(self: SSCC) -> str
  ToReadableCode(self: SSCC,includeApplicationIdentifier: bool) -> str
  """
  pass
 def ToString(self,format=None,provider=None):
  """
  ToString(self: SSCC) -> str
  ToString(self: SSCC,format: str) -> str
  ToString(self: SSCC,format: str,provider: IFormatProvider) -> str
  """
  pass
 @staticmethod
 def TryParse(input,sscc):
  """ TryParse(input: str) -> (bool,SSCC) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[SSCC]() -> SSCC
  
  __new__(cls: type,barcode: str)
  __new__(cls: type,extensionDigit: int,companyPrefix: str,serial: int)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 CheckDigit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CheckDigit(self: SSCC) -> int

"""

 CompanyNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CompanyNumber(self: SSCC) -> Int64

"""

 CompanyPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CompanyPrefix(self: SSCC) -> str

"""

 ExtensionDigit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionDigit(self: SSCC) -> int

"""

 Serial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Serial(self: SSCC) -> int

"""

 SerialFromBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SerialFromBarcode(self: SSCC) -> str

"""



