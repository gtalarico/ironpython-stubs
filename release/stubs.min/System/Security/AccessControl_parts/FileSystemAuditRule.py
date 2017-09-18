class FileSystemAuditRule(AuditRule):
 """
 Represents an abstraction of an access control entry (ACE) that defines an audit rule for a file or directory. This class cannot be inherited.

 

 FileSystemAuditRule(identity: IdentityReference,fileSystemRights: FileSystemRights,flags: AuditFlags)

 FileSystemAuditRule(identity: IdentityReference,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)

 FileSystemAuditRule(identity: str,fileSystemRights: FileSystemRights,flags: AuditFlags)

 FileSystemAuditRule(identity: str,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)
 """
 @staticmethod
 def __new__(self,identity,fileSystemRights,*__args):
  """
  __new__(cls: type,identity: IdentityReference,fileSystemRights: FileSystemRights,flags: AuditFlags)

  __new__(cls: type,identity: IdentityReference,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)

  __new__(cls: type,identity: str,fileSystemRights: FileSystemRights,flags: AuditFlags)

  __new__(cls: type,identity: str,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 FileSystemRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAuditRule object.



Get: FileSystemRights(self: FileSystemAuditRule) -> FileSystemRights



"""


