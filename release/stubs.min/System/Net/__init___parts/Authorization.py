class Authorization(object):
 """
 Contains an authentication message for an Internet server.

 

 Authorization(token: str)

 Authorization(token: str,finished: bool)

 Authorization(token: str,finished: bool,connectionGroupId: str)
 """
 @staticmethod
 def __new__(self,token,finished=None,connectionGroupId=None):
  """
  __new__(cls: type,token: str)

  __new__(cls: type,token: str,finished: bool)

  __new__(cls: type,token: str,finished: bool,connectionGroupId: str)
  """
  pass
 Complete=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the completion status of the authorization.



Get: Complete(self: Authorization) -> bool



"""

 ConnectionGroupId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique identifier for user-specific connections.



Get: ConnectionGroupId(self: Authorization) -> str



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the message returned to the server in response to an authentication challenge.



Get: Message(self: Authorization) -> str



"""

 MutuallyAuthenticated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that indicates whether mutual authentication occurred.



Get: MutuallyAuthenticated(self: Authorization) -> bool



Set: MutuallyAuthenticated(self: Authorization)=value

"""

 ProtectionRealm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the prefix for Uniform Resource Identifiers (URIs) that can be authenticated with the System.Net.Authorization.Message property.



Get: ProtectionRealm(self: Authorization) -> Array[str]



Set: ProtectionRealm(self: Authorization)=value

"""


