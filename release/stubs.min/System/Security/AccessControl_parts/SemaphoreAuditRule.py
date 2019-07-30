class SemaphoreAuditRule(AuditRule):
 """
 Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
 
 SemaphoreAuditRule(identity: IdentityReference,eventRights: SemaphoreRights,flags: AuditFlags)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SemaphoreAuditRule()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,identity,eventRights,flags):
  """ __new__(cls: type,identity: IdentityReference,eventRights: SemaphoreRights,flags: AuditFlags) """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.

"""

 SemaphoreRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access rights affected by the audit rule.

Get: SemaphoreRights(self: SemaphoreAuditRule) -> SemaphoreRights

"""


