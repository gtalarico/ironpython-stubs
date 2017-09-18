class IServiceProvider:
 """ Defines a mechanism for retrieving a service object; that is,an object that provides custom support to other objects. """
 def GetService(self,serviceType):
  """
  GetService(self: IServiceProvider,serviceType: Type) -> object

  

   Gets the service object of the specified type.

  

   serviceType: An object that specifies the type of service object to get.

   Returns: A service object of type serviceType.-or- null if there is no service object of type serviceType.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
