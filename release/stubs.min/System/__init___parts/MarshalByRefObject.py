class MarshalByRefObject(object):
 """ Enables access to objects across application domain boundaries in applications that support remoting. """
 def CreateObjRef(self,requestedType):
  """
  CreateObjRef(self: MarshalByRefObject,requestedType: Type) -> ObjRef

  

   Creates an object that contains all the relevant information required to generate a proxy used 

    to communicate with a remote object.

  

  

   requestedType: The System.Type of the object that the new System.Runtime.Remoting.ObjRef will reference.

   Returns: Information required to generate a proxy.
  """
  pass
 def GetLifetimeService(self):
  """
  GetLifetimeService(self: MarshalByRefObject) -> object

  

   Retrieves the current lifetime service object that controls the lifetime policy for this 

    instance.

  

   Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy 

    for this instance.
  """
  pass
 def InitializeLifetimeService(self):
  """
  InitializeLifetimeService(self: MarshalByRefObject) -> object

  

   Obtains a lifetime service object to control the lifetime policy for this instance.

   Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy 

    for this instance. This is the current lifetime service object for this instance if one exists; 

    otherwise,a new lifetime service object initialized to the value of the 

    System.Runtime.Remoting.Lifetime.LifetimeServices.LeaseManagerPollTime property.
  """
  pass
