class IContainer(IDisposable):
 """ Provides functionality for containers. Containers are objects that logically contain zero or more components. """
 def Add(self,component,name=None):
  """
  Add(self: IContainer,component: IComponent,name: str)

   Adds the specified System.ComponentModel.IComponent to the System.ComponentModel.IContainer at 

    the end of the list,and assigns a name to the component.

  

  

   component: The System.ComponentModel.IComponent to add.

   name: The unique,case-insensitive name to assign to the component.-or- null that leaves the component 

    unnamed.

  

  Add(self: IContainer,component: IComponent)

   Adds the specified System.ComponentModel.IComponent to the System.ComponentModel.IContainer at 

    the end of the list.

  

  

   component: The System.ComponentModel.IComponent to add.
  """
  pass
 def Remove(self,component):
  """
  Remove(self: IContainer,component: IComponent)

   Removes a component from the System.ComponentModel.IContainer.

  

   component: The System.ComponentModel.IComponent to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Components=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all the components in the System.ComponentModel.IContainer.



Get: Components(self: IContainer) -> ComponentCollection



"""


