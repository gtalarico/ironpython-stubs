class AssemblyDifferenceMemberDifference(AssemblyDifference,IDisposable):
 """ The two assemblies being compared have different members """
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
 MemberDifference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Difference between the assembly members

Get: MemberDifference(self: AssemblyDifferenceMemberDifference) -> AssemblyMemberDifference

"""

 MemberId1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the member in the first assembly

Get: MemberId1(self: AssemblyDifferenceMemberDifference) -> ElementId

"""

 MemberId2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the member in the second assembly

Get: MemberId2(self: AssemblyDifferenceMemberDifference) -> ElementId

"""


