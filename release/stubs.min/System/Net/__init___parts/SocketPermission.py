class SocketPermission(CodeAccessPermission,IPermission,ISecurityEncodable,IStackWalk,IUnrestrictedPermission):
 """
 Controls rights to make or accept connections on a transport address.

 

 SocketPermission(state: PermissionState)

 SocketPermission(access: NetworkAccess,transport: TransportType,hostName: str,portNumber: int)
 """
 def AddPermission(self,access,transport,hostName,portNumber):
  """
  AddPermission(self: SocketPermission,access: NetworkAccess,transport: TransportType,hostName: str,portNumber: int)

   Adds a permission to the set of permissions for a transport address.

  

   access: One of the System.Net.NetworkAccess values.

   transport: One of the System.Net.TransportType values.

   hostName: The host name for the transport address.

   portNumber: The port number for the transport address.
  """
  pass
 def Copy(self):
  """
  Copy(self: SocketPermission) -> IPermission

  

   Creates a copy of a System.Net.SocketPermission instance.

   Returns: A new instance of the System.Net.SocketPermission class that is a copy of the current instance.
  """
  pass
 def FromXml(self,securityElement):
  """
  FromXml(self: SocketPermission,securityElement: SecurityElement)

   Reconstructs a System.Net.SocketPermission instance for an XML encoding.

  

   securityElement: The XML encoding used to reconstruct the System.Net.SocketPermission instance.
  """
  pass
 def Intersect(self,target):
  """
  Intersect(self: SocketPermission,target: IPermission) -> IPermission

  

   Returns the logical intersection between two System.Net.SocketPermission instances.

  

   target: The System.Net.SocketPermission instance to intersect with the current instance.

   Returns: The System.Net.SocketPermission instance that represents the intersection of two 

    System.Net.SocketPermission instances. If the intersection is empty,the method returns null. If 

    the target parameter is a null reference,the method returns null.
  """
  pass
 def IsSubsetOf(self,target):
  """
  IsSubsetOf(self: SocketPermission,target: IPermission) -> bool

  

   Determines if the current permission is a subset of the specified permission.

  

   target: A System.Net.SocketPermission that is to be tested for the subset relationship.

   Returns: If target is null,this method returns true if the current instance defines no permissions; 

    otherwise,false. If target is not null,this method returns true if the current instance 

    defines a subset of target permissions; otherwise,false.
  """
  pass
 def IsUnrestricted(self):
  """
  IsUnrestricted(self: SocketPermission) -> bool

  

   Checks the overall permission state of the object.

   Returns: true if the System.Net.SocketPermission instance is created with the Unrestricted value from 

    System.Security.Permissions.PermissionState; otherwise,false.
  """
  pass
 def ToXml(self):
  """
  ToXml(self: SocketPermission) -> SecurityElement

  

   Creates an XML encoding of a System.Net.SocketPermission instance and its current state.

   Returns: A System.Security.SecurityElement instance that contains an XML-encoded representation of the 

    System.Net.SocketPermission instance,including state information.
  """
  pass
 def Union(self,target):
  """
  Union(self: SocketPermission,target: IPermission) -> IPermission

  

   Returns the logical union between two System.Net.SocketPermission instances.

  

   target: The System.Net.SocketPermission instance to combine with the current instance.

   Returns: The System.Net.SocketPermission instance that represents the union of two 

    System.Net.SocketPermission instances. If target parameter is null,it returns a copy of the 

    current instance.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,state: PermissionState)

  __new__(cls: type,access: NetworkAccess,transport: TransportType,hostName: str,portNumber: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AcceptList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of System.Net.EndpointPermission instances that identifies the endpoints that can be accepted under this permission instance.



Get: AcceptList(self: SocketPermission) -> IEnumerator



"""

 ConnectList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of System.Net.EndpointPermission instances that identifies the endpoints that can be connected to under this permission instance.



Get: ConnectList(self: SocketPermission) -> IEnumerator



"""


 AllPorts=-1

