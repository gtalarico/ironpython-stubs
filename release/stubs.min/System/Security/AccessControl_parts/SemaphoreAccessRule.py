class SemaphoreAccessRule(AccessRule):
 """
 Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

 

 SemaphoreAccessRule(identity: IdentityReference,eventRights: SemaphoreRights,type: AccessControlType)

 SemaphoreAccessRule(identity: str,eventRights: SemaphoreRights,type: AccessControlType)
 """
 @staticmethod
 def __new__(self,identity,eventRights,type):
  """
  __new__(cls: type,identity: IdentityReference,eventRights: SemaphoreRights,type: AccessControlType)

  __new__(cls: type,identity: str,eventRights: SemaphoreRights,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 SemaphoreRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rights allowed or denied by the access rule.



Get: SemaphoreRights(self: SemaphoreAccessRule) -> SemaphoreRights



"""


