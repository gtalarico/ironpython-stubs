class INestedContainer(IContainer,IDisposable):
 """ Provides functionality for nested containers,which logically contain zero or more other components and are owned by a parent component. """
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
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the owning component for the nested container.



Get: Owner(self: INestedContainer) -> IComponent



"""


