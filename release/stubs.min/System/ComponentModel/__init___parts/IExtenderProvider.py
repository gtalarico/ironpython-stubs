class IExtenderProvider:
 """ Defines the interface for extending properties to other components in a container. """
 def CanExtend(self,extendee):
  """
  CanExtend(self: IExtenderProvider,extendee: object) -> bool

  

   Specifies whether this object can provide its extender properties to the specified object.

  

   extendee: The System.Object to receive the extender properties.

   Returns: true if this object can provide extender properties to the specified object; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
