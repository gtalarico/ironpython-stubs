class MutexAccessRule(AccessRule):
 """
 Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

 

 MutexAccessRule(identity: IdentityReference,eventRights: MutexRights,type: AccessControlType)

 MutexAccessRule(identity: str,eventRights: MutexRights,type: AccessControlType)
 """
 @staticmethod
 def __new__(self,identity,eventRights,type):
  """
  __new__(cls: type,identity: IdentityReference,eventRights: MutexRights,type: AccessControlType)

  __new__(cls: type,identity: str,eventRights: MutexRights,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 MutexRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rights allowed or denied by the access rule.



Get: MutexRights(self: MutexAccessRule) -> MutexRights



"""


