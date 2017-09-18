class GuidAttribute(Attribute,_Attribute):
 """
 Supplies an explicit System.Guid when an automatic GUID is undesirable.

 

 GuidAttribute(guid: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,guid):
  """ __new__(cls: type,guid: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Guid of the class.



Get: Value(self: GuidAttribute) -> str



"""


