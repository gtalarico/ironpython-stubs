class RegistryAuditRule(AuditRule):
 """
 Represents a set of access rights to be audited for a user or group. This class cannot be inherited.

 

 RegistryAuditRule(identity: IdentityReference,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)

 RegistryAuditRule(identity: str,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)
 """
 @staticmethod
 def __new__(self,identity,registryRights,inheritanceFlags,propagationFlags,flags):
  """
  __new__(cls: type,identity: IdentityReference,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)

  __new__(cls: type,identity: str,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 RegistryRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access rights affected by the audit rule.



Get: RegistryRights(self: RegistryAuditRule) -> RegistryRights



"""


