class ReferenceWithContext(object,IDisposable):
 """ An object including a reference to a geometric object and related context,as instance transform etc. """
 def Dispose(self):
  """ Dispose(self: ReferenceWithContext) """
  pass
 def GetInstanceTransform(self):
  """
  GetInstanceTransform(self: ReferenceWithContext) -> Transform

  

   Gets the transform of the instance.

   Returns: The transform of an instance when the reference is returned by 

    FindReferencesWithContextByDirection(XYZ,XYZ,View3D) or 

    ReferenceIntersector.Find(XYZ,XYZ).
  """
  pass
 def GetReference(self):
  """
  GetReference(self: ReferenceWithContext) -> Reference

  

   Gets the reference of the geometric object.

   Returns: The reference of a geometric object when it is returned by 

    FindReferencesWithContextByDirection(XYZ,XYZ,View3D) or 

    ReferenceIntersector.Find(XYZ,XYZ).
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ReferenceWithContext,disposing: bool) """
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



Get: IsValidObject(self: ReferenceWithContext) -> bool



"""

 Proximity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The proximity value to the ray's origin when the reference is returned by FindReferencesWithContextByDirection(XYZ,XYZ,View3D) or ReferenceIntersector.Find(XYZ,XYZ).



Get: Proximity(self: ReferenceWithContext) -> float



"""


