class DirectoryObjectSecurity(ObjectSecurity):
 """ Provides the ability to control access to directory objects without direct manipulation of Access Control Lists (ACLs). """
 def AccessRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,type,objectType=None,inheritedObjectType=None):
  """
  AccessRuleFactory(self: DirectoryObjectSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType,objectType: Guid,inheritedObjectType: Guid) -> AccessRule

  

   Initializes a new instance of the System.Security.AccessControl.AccessRule class with the 

    specified values.

  

  

   identityReference: The identity to which the access rule applies.  It must be an object that can be cast as a 

    System.Security.Principal.SecurityIdentifier.

  

   accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits,the 

    meaning of which is defined by the individual integrators.

  

   isInherited: true if this rule is inherited from a parent container.

   inheritanceFlags: Specifies the inheritance properties of the access rule.

   propagationFlags: Specifies whether inherited access rules are automatically propagated. The propagation flags are 

    ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

  

   type: Specifies the valid access control type.

   objectType: The identity of the class of objects to which the new access rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new access rule.

   Returns: The System.Security.AccessControl.AccessRule object that this method creates.
  """
  pass
 def AddAccessRule(self,*args):
  """
  AddAccessRule(self: DirectoryObjectSecurity,rule: ObjectAccessRule)

   Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 

    this System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The access rule to add.
  """
  pass
 def AddAuditRule(self,*args):
  """
  AddAuditRule(self: DirectoryObjectSecurity,rule: ObjectAuditRule)

   Adds the specified audit rule to the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The audit rule to add.
  """
  pass
 def AuditRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,flags,objectType=None,inheritedObjectType=None):
  """
  AuditRuleFactory(self: DirectoryObjectSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags,objectType: Guid,inheritedObjectType: Guid) -> AuditRule

  

   Initializes a new instance of the System.Security.AccessControl.AuditRule class with the 

    specified values.

  

  

   identityReference: The identity to which the audit rule applies.  It must be an object that can be cast as a 

    System.Security.Principal.SecurityIdentifier.

  

   accessMask: The access mask of this rule. The access mask is a 32-bit collection of anonymous bits,the 

    meaning of which is defined by the individual integrators.

  

   isInherited: true if this rule is inherited from a parent container.

   inheritanceFlags: Specifies the inheritance properties of the audit rule.

   propagationFlags: Specifies whether inherited audit rules are automatically propagated. The propagation flags are 

    ignored if inheritanceFlags is set to System.Security.AccessControl.InheritanceFlags.None.

  

   flags: Specifies the conditions for which the rule is audited.

   objectType: The identity of the class of objects to which the new audit rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.

   Returns: The System.Security.AccessControl.AuditRule object that this method creates.
  """
  pass
 def GetAccessRules(self,includeExplicit,includeInherited,targetType):
  """
  GetAccessRules(self: DirectoryObjectSecurity,includeExplicit: bool,includeInherited: bool,targetType: Type) -> AuthorizationRuleCollection

  

   Gets a collection of the access rules associated with the specified security identifier.

  

   includeExplicit: true to include access rules explicitly set for the object.

   includeInherited: true to include inherited access rules.

   targetType: The security identifier for which to retrieve access rules. This must be an object that can be 

    cast as a System.Security.Principal.SecurityIdentifier object.

  

   Returns: The collection of access rules associated with the specified 

    System.Security.Principal.SecurityIdentifier object.
  """
  pass
 def GetAuditRules(self,includeExplicit,includeInherited,targetType):
  """
  GetAuditRules(self: DirectoryObjectSecurity,includeExplicit: bool,includeInherited: bool,targetType: Type) -> AuthorizationRuleCollection

  

   Gets a collection of the audit rules associated with the specified security identifier.

  

   includeExplicit: true to include audit rules explicitly set for the object.

   includeInherited: true to include inherited audit rules.

   targetType: The security identifier for which to retrieve audit rules. This must be an object that can be 

    cast as a System.Security.Principal.SecurityIdentifier object.

  

   Returns: The collection of audit rules associated with the specified 

    System.Security.Principal.SecurityIdentifier object.
  """
  pass
 def RemoveAccessRule(self,*args):
  """
  RemoveAccessRule(self: DirectoryObjectSecurity,rule: ObjectAccessRule) -> bool

  

   Removes access rules that contain the same security identifier and access mask as the specified 

    access rule from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The access rule to remove.

   Returns: true if the access rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAccessRuleAll(self,*args):
  """
  RemoveAccessRuleAll(self: DirectoryObjectSecurity,rule: ObjectAccessRule)

   Removes all access rules that have the same security identifier as the specified access rule 

    from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAccessRuleSpecific(self,*args):
  """
  RemoveAccessRuleSpecific(self: DirectoryObjectSecurity,rule: ObjectAccessRule)

   Removes all access rules that exactly match the specified access rule from the Discretionary 

    Access Control List (DACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAuditRule(self,*args):
  """
  RemoveAuditRule(self: DirectoryObjectSecurity,rule: ObjectAuditRule) -> bool

  

   Removes audit rules that contain the same security identifier and access mask as the specified 

    audit rule from the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to remove.

   Returns: true if the audit rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAuditRuleAll(self,*args):
  """
  RemoveAuditRuleAll(self: DirectoryObjectSecurity,rule: ObjectAuditRule)

   Removes all audit rules that have the same security identifier as the specified audit rule from 

    the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def RemoveAuditRuleSpecific(self,*args):
  """
  RemoveAuditRuleSpecific(self: DirectoryObjectSecurity,rule: ObjectAuditRule)

   Removes all audit rules that exactly match the specified audit rule from the System Access 

    Control List (SACL) associated with this System.Security.AccessControl.DirectoryObjectSecurity 

    object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def ResetAccessRule(self,*args):
  """
  ResetAccessRule(self: DirectoryObjectSecurity,rule: ObjectAccessRule)

   Removes all access rules in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to reset.
  """
  pass
 def SetAccessRule(self,*args):
  """
  SetAccessRule(self: DirectoryObjectSecurity,rule: ObjectAccessRule)

   Removes all access rules that contain the same security identifier and qualifier as the 

    specified access rule in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to set.
  """
  pass
 def SetAuditRule(self,*args):
  """
  SetAuditRule(self: DirectoryObjectSecurity,rule: ObjectAuditRule)

   Removes all audit rules that contain the same security identifier and qualifier as the specified 

    audit rule in the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.DirectoryObjectSecurity object and then adds the specified audit 

    rule.

  

  

   rule: The audit rule to set.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,securityDescriptor: CommonSecurityDescriptor)
  """
  pass
 AccessRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AuditRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



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


