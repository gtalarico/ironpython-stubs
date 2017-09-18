class CryptoKeySecurity(NativeObjectSecurity):
 """
 Provides the ability to control access to a cryptographic key object without direct manipulation of  an Access Control List (ACL).

 

 CryptoKeySecurity()

 CryptoKeySecurity(securityDescriptor: CommonSecurityDescriptor)
 """
 def AccessRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,type):
  """
  AccessRuleFactory(self: CryptoKeySecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType) -> AccessRule

  

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

   Returns: The System.Security.AccessControl.AccessRule object that this method creates.
  """
  pass
 def AddAccessRule(self,rule):
  """
  AddAccessRule(self: CryptoKeySecurity,rule: CryptoKeyAccessRule)

   Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 

    this System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The access rule to add.
  """
  pass
 def AddAuditRule(self,rule):
  """
  AddAuditRule(self: CryptoKeySecurity,rule: CryptoKeyAuditRule)

   Adds the specified audit rule to the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The audit rule to add.
  """
  pass
 def AuditRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,flags):
  """
  AuditRuleFactory(self: CryptoKeySecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags) -> AuditRule

  

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

   Returns: The System.Security.AccessControl.AuditRule object that this method creates.
  """
  pass
 def RemoveAccessRule(self,rule):
  """
  RemoveAccessRule(self: CryptoKeySecurity,rule: CryptoKeyAccessRule) -> bool

  

   Removes access rules that contain the same security identifier and access mask as the specified 

    access rule from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The access rule to remove.

   Returns: true if the access rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAccessRuleAll(self,rule):
  """
  RemoveAccessRuleAll(self: CryptoKeySecurity,rule: CryptoKeyAccessRule)

   Removes all access rules that have the same security identifier as the specified access rule 

    from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAccessRuleSpecific(self,rule):
  """
  RemoveAccessRuleSpecific(self: CryptoKeySecurity,rule: CryptoKeyAccessRule)

   Removes all access rules that exactly match the specified access rule from the Discretionary 

    Access Control List (DACL) associated with this System.Security.AccessControl.CryptoKeySecurity 

    object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAuditRule(self,rule):
  """
  RemoveAuditRule(self: CryptoKeySecurity,rule: CryptoKeyAuditRule) -> bool

  

   Removes audit rules that contain the same security identifier and access mask as the specified 

    audit rule from the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The audit rule to remove.

   Returns: true if the audit rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAuditRuleAll(self,rule):
  """
  RemoveAuditRuleAll(self: CryptoKeySecurity,rule: CryptoKeyAuditRule)

   Removes all audit rules that have the same security identifier as the specified audit rule from 

    the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def RemoveAuditRuleSpecific(self,rule):
  """
  RemoveAuditRuleSpecific(self: CryptoKeySecurity,rule: CryptoKeyAuditRule)

   Removes all audit rules that exactly match the specified audit rule from the System Access 

    Control List (SACL) associated with this System.Security.AccessControl.CryptoKeySecurity object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def ResetAccessRule(self,rule):
  """
  ResetAccessRule(self: CryptoKeySecurity,rule: CryptoKeyAccessRule)

   Removes all access rules in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object and then adds the specified access rule.

  

  

   rule: The access rule to reset.
  """
  pass
 def SetAccessRule(self,rule):
  """
  SetAccessRule(self: CryptoKeySecurity,rule: CryptoKeyAccessRule)

   Removes all access rules that contain the same security identifier and qualifier as the 

    specified access rule in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object and then adds the specified access rule.

  

  

   rule: The access rule to set.
  """
  pass
 def SetAuditRule(self,rule):
  """
  SetAuditRule(self: CryptoKeySecurity,rule: CryptoKeyAuditRule)

   Removes all audit rules that contain the same security identifier and qualifier as the specified 

    audit rule in the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CryptoKeySecurity object and then adds the specified audit rule.

  

  

   rule: The audit rule to set.
  """
  pass
 @staticmethod
 def __new__(self,securityDescriptor=None):
  """
  __new__(cls: type)

  __new__(cls: type,securityDescriptor: CommonSecurityDescriptor)
  """
  pass
 AccessRightType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Type of the securable object associated with this System.Security.AccessControl.CryptoKeySecurity object.



Get: AccessRightType(self: CryptoKeySecurity) -> Type



"""

 AccessRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AccessRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Type of the object associated with the access rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.



Get: AccessRuleType(self: CryptoKeySecurity) -> Type



"""

 AuditRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AuditRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Type object associated with the audit rules of this System.Security.AccessControl.CryptoKeySecurity object. The System.Type object must be an object that can be cast as a System.Security.Principal.SecurityIdentifier object.



Get: AuditRuleType(self: CryptoKeySecurity) -> Type



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


