class TriangulatedSolidOrShell(object,IDisposable):
 """ This class represents a triangulated solid or shell. """
 def Dispose(self):
  """ Dispose(self: TriangulatedSolidOrShell) """
  pass
 def GetShellComponent(self,componentIndex):
  """
  GetShellComponent(self: TriangulatedSolidOrShell,componentIndex: int) -> TriangulatedShellComponent

  

   Returns the specified shell component of a solid or shell. Input componentIndex 

    must lie

     between 0 and ShellComponentCount-1,inclusive. The returned 

    TriangulatedShellComponent

     should not be modified by the caller.

  

  

     Returns: The component.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TriangulatedSolidOrShell,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TriangulatedSolidOrShell) -> bool



"""

 ShellComponentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of TriangulatedShellComponents that this TriangulatedSolidOrShell contains.



Get: ShellComponentCount(self: TriangulatedSolidOrShell) -> int



"""


