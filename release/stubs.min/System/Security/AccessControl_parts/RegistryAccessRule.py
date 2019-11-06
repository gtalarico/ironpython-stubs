class RegistryAccessRule(AccessRule):
 """
 Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited.
 
 RegistryAccessRule(identity: IdentityReference,registryRights: RegistryRights,type: AccessControlType)
 RegistryAccessRule(identity: str,registryRights: RegistryRights,type: AccessControlType)
 RegistryAccessRule(identity: IdentityReference,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
 RegistryAccessRule(identity: str,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RegistryAccessRule()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,identity,registryRights,*__args):
  """
  __new__(cls: type,identity: IdentityReference,registryRights: RegistryRights,type: AccessControlType)
  __new__(cls: type,identity: str,registryRights: RegistryRights,type: AccessControlType)
  __new__(cls: type,identity: IdentityReference,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
  __new__(cls: type,identity: str,registryRights: RegistryRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.

"""

 RegistryRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rights allowed or denied by the access rule.

Get: RegistryRights(self: RegistryAccessRule) -> RegistryRights

"""


