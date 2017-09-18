class ViewInfo(object,IDisposable):
 """
 Represents the name and orientation of a View (and named view).

    views can be thought of as cameras.
 """
 def Dispose(self):
  """
  Dispose(self: ViewInfo)

   Actively reclaims unmanaged resources that this instance uses.
  """
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
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the NamedView.



Get: Name(self: ViewInfo) -> str



Set: Name(self: ViewInfo)=value

"""

 Viewport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the viewport,or viewing frustum,associated with this view.



Get: Viewport(self: ViewInfo) -> ViewportInfo



"""


