class SocketPermissionAttribute(CodeAccessSecurityAttribute,_Attribute):
 """
 Specifies security actions to control System.Net.Sockets.Socket connections. This class cannot be inherited.

 

 SocketPermissionAttribute(action: SecurityAction)
 """
 def CreatePermission(self):
  """
  CreatePermission(self: SocketPermissionAttribute) -> IPermission

  

   Creates and returns a new instance of the System.Net.SocketPermission class.

   Returns: An instance of the System.Net.SocketPermission class that corresponds to the security 

    declaration.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,action):
  """ __new__(cls: type,action: SecurityAction) """
  pass
 def __reduce_ex__(self,*args):
  pass
 Access=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the network access method that is allowed by this System.Net.SocketPermissionAttribute.



Get: Access(self: SocketPermissionAttribute) -> str



Set: Access(self: SocketPermissionAttribute)=value

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the DNS host name or IP address that is specified by this System.Net.SocketPermissionAttribute.



Get: Host(self: SocketPermissionAttribute) -> str



Set: Host(self: SocketPermissionAttribute)=value

"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the port number that is associated with this System.Net.SocketPermissionAttribute.



Get: Port(self: SocketPermissionAttribute) -> str



Set: Port(self: SocketPermissionAttribute)=value

"""

 Transport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Net.TransportType that is specified by this System.Net.SocketPermissionAttribute.



Get: Transport(self: SocketPermissionAttribute) -> str



Set: Transport(self: SocketPermissionAttribute)=value

"""


