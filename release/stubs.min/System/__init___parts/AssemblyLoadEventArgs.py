class AssemblyLoadEventArgs(EventArgs):
 """
 Provides data for the System.AppDomain.AssemblyLoad event.
 
 AssemblyLoadEventArgs(loadedAssembly: Assembly)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AssemblyLoadEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,loadedAssembly):
  """ __new__(cls: type,loadedAssembly: Assembly) """
  pass
 LoadedAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Reflection.Assembly that represents the currently loaded assembly.

Get: LoadedAssembly(self: AssemblyLoadEventArgs) -> Assembly

"""


