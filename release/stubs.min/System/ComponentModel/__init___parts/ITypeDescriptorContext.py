class ITypeDescriptorContext(IServiceProvider):
 """ Provides contextual information about a component,such as its container and property descriptor. """
 def OnComponentChanged(self):
  """
  OnComponentChanged(self: ITypeDescriptorContext)

   Raises the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event.
  """
  pass
 def OnComponentChanging(self):
  """
  OnComponentChanging(self: ITypeDescriptorContext) -> bool

  

   Raises the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event.

   Returns: true if this object can be changed; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Container=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the container representing this System.ComponentModel.TypeDescriptor request.



Get: Container(self: ITypeDescriptorContext) -> IContainer



"""

 Instance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object that is connected with this type descriptor request.



Get: Instance(self: ITypeDescriptorContext) -> object



"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.ComponentModel.PropertyDescriptor that is associated with the given context item.



Get: PropertyDescriptor(self: ITypeDescriptorContext) -> PropertyDescriptor



"""


