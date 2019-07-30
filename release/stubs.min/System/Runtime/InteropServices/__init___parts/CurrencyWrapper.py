class CurrencyWrapper(object):
 """
 Wraps objects the marshaler should marshal as a VT_CY.
 
 CurrencyWrapper(obj: Decimal)
 CurrencyWrapper(obj: object)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CurrencyWrapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,obj):
  """
  __new__(cls: type,obj: Decimal)
  __new__(cls: type,obj: object)
  """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the wrapped object to be marshaled as type VT_CY.

Get: WrappedObject(self: CurrencyWrapper) -> Decimal

"""


