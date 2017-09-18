class APIObject(object,IDisposable):
 """ Supports all objects in the Autodesk Revit API hierarchy. """
 def Dispose(self):
  """
  Dispose(self: APIObject)

   Causes the object to release immediately any resources it may be utilizing.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the object is read-only or modifiable.



Get: IsReadOnly(self: APIObject) -> bool



"""


