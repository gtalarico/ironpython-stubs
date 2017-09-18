class IComponent(IDisposable):
 """ Provides functionality required by all components. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.ComponentModel.ISite associated with the System.ComponentModel.IComponent.



Get: Site(self: IComponent) -> ISite



Set: Site(self: IComponent)=value

"""


 Disposed=None

