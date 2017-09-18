class ProgIdAttribute(Attribute,_Attribute):
 """
 Allows the user to specify the ProgID of a class.

 

 ProgIdAttribute(progId: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,progId):
  """ __new__(cls: type,progId: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ProgID of the class.



Get: Value(self: ProgIdAttribute) -> str



"""


