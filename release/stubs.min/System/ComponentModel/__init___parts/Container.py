class Container(object,IContainer,IDisposable):
 """
 Encapsulates zero or more components.

 

 Container()
 """
 def Add(self,component,name=None):
  """
  Add(self: Container,component: IComponent,name: str)

   Adds the specified System.ComponentModel.Component to the System.ComponentModel.Container and 

    assigns it a name.

  

  

   component: The component to add.

   name: The unique,case-insensitive name to assign to the component.-or- null,which leaves the 

    component unnamed.

  

  Add(self: Container,component: IComponent)

   Adds the specified System.ComponentModel.Component to the System.ComponentModel.Container. The 

    component is unnamed.

  

  

   component: The component to add.
  """
  pass
 def CreateSite(self,*args):
  """
  CreateSite(self: Container,component: IComponent,name: str) -> ISite

  

   Creates a site System.ComponentModel.ISite for the given System.ComponentModel.IComponent and 

    assigns the given name to the site.

  

  

   component: The System.ComponentModel.IComponent to create a site for.

   name: The name to assign to component,or null to skip the name assignment.

   Returns: The newly created site.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Container)

   Releases all resources used by the System.ComponentModel.Container.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Container,service: Type) -> object

  

   Gets the service object of the specified type,if it is available.

  

   service: The System.Type of the service to retrieve.

   Returns: An System.Object implementing the requested service,or null if the service cannot be resolved.
  """
  pass
 def Remove(self,component):
  """
  Remove(self: Container,component: IComponent)

   Removes a component from the System.ComponentModel.Container.

  

   component: The component to remove.
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
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 Components=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all the components in the System.ComponentModel.Container.



Get: Components(self: Container) -> ComponentCollection



"""


