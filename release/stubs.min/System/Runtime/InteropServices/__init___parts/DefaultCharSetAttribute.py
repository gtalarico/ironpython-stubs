class DefaultCharSetAttribute(Attribute,_Attribute):
 """
 Specifies the value of the System.Runtime.InteropServices.CharSet enumeration. This class cannot be inherited.

 

 DefaultCharSetAttribute(charSet: CharSet)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,charSet):
  """ __new__(cls: type,charSet: CharSet) """
  pass
 CharSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default value of System.Runtime.InteropServices.CharSet for any call to System.Runtime.InteropServices.DllImportAttribute.



Get: CharSet(self: DefaultCharSetAttribute) -> CharSet



"""


