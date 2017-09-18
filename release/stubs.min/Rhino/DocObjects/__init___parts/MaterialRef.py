class MaterialRef(object,IDisposable):
 # no doc
 def Dispose(self):
  """ Dispose(self: MaterialRef) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BackFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the Material used to render the back of an object.



Get: BackFaceMaterialId(self: MaterialRef) -> Guid



"""

 BackFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the material used to render the back of an object



Get: BackFaceMaterialIndex(self: MaterialRef) -> int



"""

 FrontFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the Material used to render the front of an object.



Get: FrontFaceMaterialId(self: MaterialRef) -> Guid



"""

 FrontFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the material used to render the front of an object



Get: FrontFaceMaterialIndex(self: MaterialRef) -> int



"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the simple material should come from the object or from

   it's layer.



Get: MaterialSource(self: MaterialRef) -> ObjectMaterialSource



"""

 PlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies a rendering plug-in



Get: PlugInId(self: MaterialRef) -> Guid



"""


