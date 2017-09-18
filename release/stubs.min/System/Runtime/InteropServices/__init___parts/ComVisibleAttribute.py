class ComVisibleAttribute(Attribute,_Attribute):
 """
 Controls accessibility of an individual managed type or member,or of all types within an assembly,to COM.

 

 ComVisibleAttribute(visibility: bool)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,visibility):
  """ __new__(cls: type,visibility: bool) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the COM type is visible.



Get: Value(self: ComVisibleAttribute) -> bool



"""


