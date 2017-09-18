class NestedContainer(Container,IContainer,IDisposable,INestedContainer):
 """
 Provides the base implementation for the System.ComponentModel.INestedContainer interface,which enables containers to have an owning component.

 

 NestedContainer(owner: IComponent)
 """
 def CreateSite(self,*args):
  """
  CreateSite(self: NestedContainer,component: IComponent,name: str) -> ISite

  

   Creates a site for the component within the container.

  

   component: The System.ComponentModel.IComponent to create a site for.

   name: The name to assign to component,or null to skip the name assignment.

   Returns: The newly created System.ComponentModel.ISite.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: NestedContainer,disposing: bool)

   Releases the resources used by the nested container.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: NestedContainer,service: Type) -> object

  

   Gets the service object of the specified type,if it is available.

  

   service: The System.Type of the service to retrieve.

   Returns: An System.Object that implements the requested service,or null if the service cannot be 

    resolved.
  """
  pass
 def RemoveWithoutUnsiting(self,*args):
  """
  RemoveWithoutUnsiting(self: Container,component: IComponent)

   Removes a component from the System.ComponentModel.Container without setting 

    System.ComponentModel.IComponent.Site to null.

  

  

   component: The component to remove.
  """
  pass
 def ValidateName(self,*args):
  """
  ValidateName(self: Container,component: IComponent,name: str)

   Determines whether the component name is unique for this container.

  

   component: The named component.

   name: The component name to validate.
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
 @staticmethod
 def __new__(self,owner):
  """ __new__(cls: type,owner: IComponent) """
  pass
 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the owning component for this nested container.



Get: Owner(self: NestedContainer) -> IComponent



"""

 OwnerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the owning component.



"""


