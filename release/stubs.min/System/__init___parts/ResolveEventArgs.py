class ResolveEventArgs(EventArgs):
 """
 Provides data for loader resolution events,such as the System.AppDomain.TypeResolve,System.AppDomain.ResourceResolve,System.AppDomain.ReflectionOnlyAssemblyResolve,and System.AppDomain.AssemblyResolve events.
 
 ResolveEventArgs(name: str)
 ResolveEventArgs(name: str,requestingAssembly: Assembly)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ResolveEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,name,requestingAssembly=None):
  """
  __new__(cls: type,name: str)
  __new__(cls: type,name: str,requestingAssembly: Assembly)
  """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the item to resolve.

Get: Name(self: ResolveEventArgs) -> str

"""

 RequestingAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the assembly whose dependency is being resolved.

Get: RequestingAssembly(self: ResolveEventArgs) -> Assembly

"""


