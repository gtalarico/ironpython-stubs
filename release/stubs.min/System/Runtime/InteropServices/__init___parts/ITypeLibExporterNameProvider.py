class ITypeLibExporterNameProvider:
 """ Provides control over the casing of names when exported to a type library. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ITypeLibExporterNameProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetNames(self):
  """
  GetNames(self: ITypeLibExporterNameProvider) -> Array[str]
  
   Returns a list of names to control the casing of.
   Returns: An array of strings,where each element contains the name of a type to control casing for.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
