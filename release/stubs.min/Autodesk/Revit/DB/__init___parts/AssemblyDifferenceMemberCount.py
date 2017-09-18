class AssemblyDifferenceMemberCount(AssemblyDifference,IDisposable):
 """ The two assemblies being compared have different number of members """
 def Dispose(self):
  """ Dispose(self: AssemblyDifference,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AssemblyDifference,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Count1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of members in the first assembly



Get: Count1(self: AssemblyDifferenceMemberCount) -> int



"""

 Count2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of members in the second assembly



Get: Count2(self: AssemblyDifferenceMemberCount) -> int



"""


