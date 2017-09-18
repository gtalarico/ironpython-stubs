class BestFitMappingAttribute(Attribute,_Attribute):
 """
 Controls whether Unicode characters are converted to the closest matching ANSI characters.

 

 BestFitMappingAttribute(BestFitMapping: bool)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,BestFitMapping):
  """ __new__(cls: type,BestFitMapping: bool) """
  pass
 BestFitMapping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the best-fit mapping behavior when converting Unicode characters to ANSI characters.



Get: BestFitMapping(self: BestFitMappingAttribute) -> bool



"""


 ThrowOnUnmappableChar=None

