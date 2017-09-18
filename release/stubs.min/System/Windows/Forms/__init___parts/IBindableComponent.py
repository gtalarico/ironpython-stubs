class IBindableComponent(IComponent,IDisposable):
 """ Enables a non-control component to emulate the data-binding behavior of a Windows Forms control. """
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
 BindingContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of currency managers for the System.Windows.Forms.IBindableComponent.



Get: BindingContext(self: IBindableComponent) -> BindingContext



Set: BindingContext(self: IBindableComponent)=value

"""

 DataBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of data-binding objects for this System.Windows.Forms.IBindableComponent.



Get: DataBindings(self: IBindableComponent) -> ControlBindingsCollection



"""


