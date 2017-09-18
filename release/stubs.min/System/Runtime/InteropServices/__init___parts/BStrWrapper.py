class BStrWrapper(object):
 """
 Marshals data of type VT_BSTR from managed to unmanaged code. This class cannot be inherited.

 

 BStrWrapper(value: str)

 BStrWrapper(value: object)
 """
 @staticmethod
 def __new__(self,value):
  """
  __new__(cls: type,value: str)

  __new__(cls: type,value: object)
  """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the wrapped System.String object to marshal as type VT_BSTR.



Get: WrappedObject(self: BStrWrapper) -> str



"""


