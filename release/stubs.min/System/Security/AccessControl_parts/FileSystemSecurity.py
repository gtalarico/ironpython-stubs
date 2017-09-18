class FileSystemSecurity(NativeObjectSecurity):
 """ Represents the access control and audit security for a file or directory. """
 def AccessRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,type):
  """
  AccessRuleFactory(self: FileSystemSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType) -> AccessRule

  

   Initializes a new instance of the System.Security.AccessControl.FileSystemAccessRule class that 

    represents a new access control rule for the specified user,with the specified access rights,

    access control,and flags.

  

  

   identityReference: An System.Security.Principal.IdentityReference object that represents a user account.

   accessMask: An integer that specifies an access type.

   isInherited: true if the access rule is inherited; otherwise,false.

   inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate 

    access masks to child objects.

  

   propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate 

    Access Control Entries (ACEs) to child objects.

  

   type: One of the System.Security.AccessControl.AccessControlType values that specifies whether access 

    is allowed or denied.

  

   Returns: A new System.Security.AccessControl.FileSystemAccessRule object that represents a new access 

    control rule for the specified user,with the specified access rights,access control,and 

    flags.
  """
  pass
 def AddAccessRule(self,rule):
  """
  AddAccessRule(self: FileSystemSecurity,rule: FileSystemAccessRule)

   Adds the specified access control list (ACL) permission to the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 

    list (ACL) permission to add to a file or directory.
  """
  pass
 def AddAuditRule(self,rule):
  """
  AddAuditRule(self: FileSystemSecurity,rule: FileSystemAuditRule)

   Adds the specified audit rule to the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to add 

    to a file or directory.
  """
  pass
 def AuditRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,flags):
  """
  AuditRuleFactory(self: FileSystemSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags) -> AuditRule

  

   Initializes a new instance of the System.Security.AccessControl.FileSystemAuditRule class 

    representing the specified audit rule for the specified user.

  

  

   identityReference: An System.Security.Principal.IdentityReference object that represents a user account.

   accessMask: An integer that specifies an access type.

   isInherited: true if the access rule is inherited; otherwise,false.

   inheritanceFlags: One of the System.Security.AccessControl.InheritanceFlags values that specifies how to propagate 

    access masks to child objects.

  

   propagationFlags: One of the System.Security.AccessControl.PropagationFlags values that specifies how to propagate 

    Access Control Entries (ACEs) to child objects.

  

   flags: One of the System.Security.AccessControl.AuditFlags values that specifies the type of auditing 

    to perform.

  

   Returns: A new System.Security.AccessControl.FileSystemAuditRule object representing the specified audit 

    rule for the specified user.
  """
  pass
 def RemoveAccessRule(self,rule):
  """
  RemoveAccessRule(self: FileSystemSecurity,rule: FileSystemAccessRule) -> bool

  

   Removes all matching allow or deny access control list (ACL) permissions from the current file 

    or directory.

  

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 

    list (ACL) permission to remove from a file or directory.

  

   Returns: true if the access rule was removed; otherwise,false.
  """
  pass
 def RemoveAccessRuleAll(self,rule):
  """
  RemoveAccessRuleAll(self: FileSystemSecurity,rule: FileSystemAccessRule)

   Removes all access control list (ACL) permissions for the specified user from the current file 

    or directory.

  

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that specifies a user whose access 

    control list (ACL) permissions should be removed from a file or directory.
  """
  pass
 def RemoveAccessRuleSpecific(self,rule):
  """
  RemoveAccessRuleSpecific(self: FileSystemSecurity,rule: FileSystemAccessRule)

   Removes a single matching allow or deny access control list (ACL) permission from the current 

    file or directory.

  

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that specifies a user whose access 

    control list (ACL) permissions should be removed from a file or directory.
  """
  pass
 def RemoveAuditRule(self,rule):
  """
  RemoveAuditRule(self: FileSystemSecurity,rule: FileSystemAuditRule) -> bool

  

   Removes all matching allow or deny audit rules from the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to 

    remove from a file or directory.

  

   Returns: true if the audit rule was removed; otherwise,false
  """
  pass
 def RemoveAuditRuleAll(self,rule):
  """
  RemoveAuditRuleAll(self: FileSystemSecurity,rule: FileSystemAuditRule)

   Removes all audit rules for the specified user from the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAuditRule object that specifies a user whose audit 

    rules should be removed from a file or directory.
  """
  pass
 def RemoveAuditRuleSpecific(self,rule):
  """
  RemoveAuditRuleSpecific(self: FileSystemSecurity,rule: FileSystemAuditRule)

   Removes a single matching allow or deny audit rule from the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAuditRule  object that represents an audit rule to 

    remove from a file or directory.
  """
  pass
 def ResetAccessRule(self,rule):
  """
  ResetAccessRule(self: FileSystemSecurity,rule: FileSystemAccessRule)

   Adds the specified access control list (ACL) permission to the current file or directory and 

    removes all matching ACL permissions.

  

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 

    list (ACL) permission to add to a file or directory.
  """
  pass
 def SetAccessRule(self,rule):
  """
  SetAccessRule(self: FileSystemSecurity,rule: FileSystemAccessRule)

   Sets the specified access control list (ACL) permission for the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAccessRule object that represents an access control 

    list (ACL) permission to set for a file or directory.
  """
  pass
 def SetAuditRule(self,rule):
  """
  SetAuditRule(self: FileSystemSecurity,rule: FileSystemAuditRule)

   Sets the specified audit rule for the current file or directory.

  

   rule: A System.Security.AccessControl.FileSystemAuditRule object that represents an audit rule to set 

    for a file or directory.
  """
  pass
 AccessRightType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rights.



Get: AccessRightType(self: FileSystemSecurity) -> Type



"""

 AccessRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AccessRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the enumeration that the System.Security.AccessControl.FileSystemSecurity class uses to represent access rules.



Get: AccessRuleType(self: FileSystemSecurity) -> Type



"""

 AuditRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AuditRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that the System.Security.AccessControl.FileSystemSecurity class uses to represent audit rules.



Get: AuditRuleType(self: FileSystemSecurity) -> Type



"""

 GroupModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.



"""

 IsContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.



"""

 IsDS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.



"""

 OwnerModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.



"""


