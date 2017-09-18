class FileSystemAccessRule(AccessRule):
 """
 Represents an abstraction of an access control entry (ACE) that defines an access rule for a file or directory. This class cannot be inherited.

 

 FileSystemAccessRule(identity: IdentityReference,fileSystemRights: FileSystemRights,type: AccessControlType)

 FileSystemAccessRule(identity: str,fileSystemRights: FileSystemRights,type: AccessControlType)

 FileSystemAccessRule(identity: IdentityReference,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)

 FileSystemAccessRule(identity: str,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
 """
 @staticmethod
 def __new__(self,identity,fileSystemRights,*__args):
  """
  __new__(cls: type,identity: IdentityReference,fileSystemRights: FileSystemRights,type: AccessControlType)

  __new__(cls: type,identity: str,fileSystemRights: FileSystemRights,type: AccessControlType)

  __new__(cls: type,identity: IdentityReference,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)

  __new__(cls: type,identity: str,fileSystemRights: FileSystemRights,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 FileSystemRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Security.AccessControl.FileSystemRights flags associated with the current System.Security.AccessControl.FileSystemAccessRule object.



Get: FileSystemRights(self: FileSystemAccessRule) -> FileSystemRights



"""


