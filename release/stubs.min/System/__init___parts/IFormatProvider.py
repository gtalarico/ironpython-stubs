class IFormatProvider:
 """ Provides a mechanism for retrieving an object to control formatting. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IFormatProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetFormat(self,formatType):
  """
  GetFormat(self: IFormatProvider,formatType: Type) -> object
  
   Returns an object that provides formatting services for the specified type.
  
   formatType: An object that specifies the type of format object to return.
   Returns: An instance of the object specified by formatType,if the System.IFormatProvider implementation can supply that type of object; otherwise,null.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
