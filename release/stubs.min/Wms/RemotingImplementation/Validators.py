# encoding: utf-8
# module Wms.RemotingImplementation.Validators calls itself Validators
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class IReallocationValidator:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IReallocationValidator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Validate(self,itemCode,warehouseCode,locationCode):
  """ Validate(self: IReallocationValidator,itemCode: str,warehouseCode: str,locationCode: str) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ErrorMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErrorMessage(self: IReallocationValidator) -> str

Set: ErrorMessage(self: IReallocationValidator)=value
"""



class ReAllocateValidator(object):
 """ ReAllocateValidator(stockManager: IStockManager) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReAllocateValidator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Validate(self,itemCode,warehouseCode,locationCode):
  """ Validate(self: ReAllocateValidator,itemCode: str,warehouseCode: str,locationCode: str) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,stockManager):
  """ __new__(cls: type,stockManager: IStockManager) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ErrorMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErrorMessage(self: ReAllocateValidator) -> str

Set: ErrorMessage(self: ReAllocateValidator)=value
"""



class TransferWarehouseValidator(object):
 """ TransferWarehouseValidator() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TransferWarehouseValidator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Validate(self,itemCode,warehouseCode,locationCode):
  """ Validate(self: TransferWarehouseValidator,itemCode: str,warehouseCode: str,locationCode: str) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ErrorMessage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErrorMessage(self: TransferWarehouseValidator) -> str

Set: ErrorMessage(self: TransferWarehouseValidator)=value
"""



