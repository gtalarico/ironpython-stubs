class MarshalByValueComponent(object,IComponent,IDisposable,IServiceProvider):
 """
 Implements System.ComponentModel.IComponent and provides the base implementation for remotable components that are marshaled by value (a copy of the serialized object is passed).

 

 MarshalByValueComponent()
 """
 def Dispose(self):
  """
  Dispose(self: MarshalByValueComponent)

   Releases all resources used by the System.ComponentModel.MarshalByValueComponent.
  """
  pass
 def GetService(self,service):
  """
  GetService(self: MarshalByValueComponent,service: Type) -> object

  

   Gets the implementer of the System.IServiceProvider.

  

   service: A System.Type that represents the type of service you want.

   Returns: An System.Object that represents the implementer of the System.IServiceProvider.
  """
  pass
 def ToString(self):
  """
  ToString(self: MarshalByValueComponent) -> str

  

   Returns a System.String containing the name of the System.ComponentModel.Component,if any. This 

    method should not be overridden.

  

   Returns: A System.String containing the name of the System.ComponentModel.Component,if any.null if the 

    System.ComponentModel.Component is unnamed.
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
 def __str__(self,*args):
  pass
 Container=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the container for the component.



Get: Container(self: MarshalByValueComponent) -> IContainer



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component is currently in design mode.



Get: DesignMode(self: MarshalByValueComponent) -> bool



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this component.



"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the site of the component.



Get: Site(self: MarshalByValueComponent) -> ISite



Set: Site(self: MarshalByValueComponent)=value

"""


 Disposed=None

