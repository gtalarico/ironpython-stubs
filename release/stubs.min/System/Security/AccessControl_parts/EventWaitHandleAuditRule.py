class EventWaitHandleAuditRule(AuditRule):
 """
 Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

 

 EventWaitHandleAuditRule(identity: IdentityReference,eventRights: EventWaitHandleRights,flags: AuditFlags)
 """
 @staticmethod
 def __new__(self,identity,eventRights,flags):
  """ __new__(cls: type,identity: IdentityReference,eventRights: EventWaitHandleRights,flags: AuditFlags) """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 EventWaitHandleRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access rights affected by the audit rule.



Get: EventWaitHandleRights(self: EventWaitHandleAuditRule) -> EventWaitHandleRights



"""


