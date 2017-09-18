class ImportedFromTypeLibAttribute(Attribute,_Attribute):
 """
 Indicates that the types defined within an assembly were originally defined in a type library.

 

 ImportedFromTypeLibAttribute(tlbFile: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,tlbFile):
  """ __new__(cls: type,tlbFile: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the original type library file.



Get: Value(self: ImportedFromTypeLibAttribute) -> str



"""


