class AutomationProxyAttribute(Attribute,_Attribute):
 """
 Specifies whether the type should be marshaled using the Automation marshaler or a custom proxy and stub.

 

 AutomationProxyAttribute(val: bool)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,val):
  """ __new__(cls: type,val: bool) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the type of marshaler to use.



Get: Value(self: AutomationProxyAttribute) -> bool



"""


