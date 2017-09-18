class ISite(IServiceProvider):
 """ Provides functionality required by sites. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Component=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the component associated with the System.ComponentModel.ISite when implemented by a class.



Get: Component(self: ISite) -> IComponent



"""

 Container=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.ComponentModel.IContainer associated with the System.ComponentModel.ISite when implemented by a class.



Get: Container(self: ISite) -> IContainer



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether the component is in design mode when implemented by a class.



Get: DesignMode(self: ISite) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the component associated with the System.ComponentModel.ISite when implemented by a class.



Get: Name(self: ISite) -> str



Set: Name(self: ISite)=value

"""


