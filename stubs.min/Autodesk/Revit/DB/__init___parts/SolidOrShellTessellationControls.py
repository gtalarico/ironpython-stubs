class SolidOrShellTessellationControls(object,IDisposable):
 """
 Controls various aspects of the triangulation produced by SolutUtils::tessellateSolidOrShell.
 
 SolidOrShellTessellationControls()
 """
 def DisableLevelOfDetail(self):
  """
  DisableLevelOfDetail(self: SolidOrShellTessellationControls)
   Disables the use of levelOfDetail. The use of levelOfDetail is enabled by 
    calling setLevelOfDetail (with a valid input).
  """
  pass
 def Dispose(self):
  """ Dispose(self: SolidOrShellTessellationControls) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SolidOrShellTessellationControls,disposing: bool) """
  pass
 def UseLevelOfDetail(self):
  """
  UseLevelOfDetail(self: SolidOrShellTessellationControls) -> bool
  
   Returns true if the use of levelOfDetail is enabled,false if not. The use of 
    levelOfDetail is enabled
     by calling setLevelOfDetail (with a valid input).
  """
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
 Accuracy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A positive real number specifying how accurately a triangulation should approximate a solid or shell.

Get: Accuracy(self: SolidOrShellTessellationControls) -> float

Set: Accuracy(self: SolidOrShellTessellationControls)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SolidOrShellTessellationControls) -> bool

"""

 LevelOfDetail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An number between 0 and 1 (inclusive) specifying the level of detail for the triangulation of a solid or shell.

Get: LevelOfDetail(self: SolidOrShellTessellationControls) -> float

Set: LevelOfDetail(self: SolidOrShellTessellationControls)=value
"""

 MinAngleInTriangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A non-negative real number specifying the minimum allowed angle for any triangle in the triangulation,in radians.

Get: MinAngleInTriangle(self: SolidOrShellTessellationControls) -> float

Set: MinAngleInTriangle(self: SolidOrShellTessellationControls)=value
"""

 MinExternalAngleBetweenTriangles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A positive real number specifying the minimum allowed value for the external angle between two adjacent triangles,in radians.

Get: MinExternalAngleBetweenTriangles(self: SolidOrShellTessellationControls) -> float

Set: MinExternalAngleBetweenTriangles(self: SolidOrShellTessellationControls)=value
"""


