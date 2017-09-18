class EventWaitHandleAccessRule(AccessRule):
 """
 Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.

 

 EventWaitHandleAccessRule(identity: IdentityReference,eventRights: EventWaitHandleRights,type: AccessControlType)

 EventWaitHandleAccessRule(identity: str,eventRights: EventWaitHandleRights,type: AccessControlType)
 """
 @staticmethod
 def __new__(self,identity,eventRights,type):
  """
  __new__(cls: type,identity: IdentityReference,eventRights: EventWaitHandleRights,type: AccessControlType)

  __new__(cls: type,identity: str,eventRights: EventWaitHandleRights,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 EventWaitHandleRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rights allowed or denied by the access rule.



Get: EventWaitHandleRights(self: EventWaitHandleAccessRule) -> EventWaitHandleRights



"""


