class DispIdAttribute(Attribute,_Attribute):
 """
 Specifies the COM dispatch identifier (DISPID) of a method,field,or property.

 

 DispIdAttribute(dispId: int)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dispId):
  """ __new__(cls: type,dispId: int) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the DISPID for the member.



Get: Value(self: DispIdAttribute) -> int



"""


