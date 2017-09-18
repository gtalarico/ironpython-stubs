class SemaphoreSecurity(NativeObjectSecurity):
 """
 Represents the Windows access control security for a named semaphore. This class cannot be inherited.

 

 SemaphoreSecurity()

 SemaphoreSecurity(name: str,includeSections: AccessControlSections)
 """
 def AccessRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,type):
  """
  AccessRuleFactory(self: SemaphoreSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,type: AccessControlType) -> AccessRule

  

   Creates a new access control rule for the specified user,with the specified access rights,

    access control,and flags.

  

  

   identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 

    applies to.

  

   accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the 

    access rights to allow or deny,cast to an integer.

  

   isInherited: Meaningless for named semaphores,because they have no hierarchy.

   inheritanceFlags: Meaningless for named semaphores,because they have no hierarchy.

   propagationFlags: Meaningless for named semaphores,because they have no hierarchy.

   type: One of the System.Security.AccessControl.AccessControlType values specifying whether the rights 

    are allowed or denied.

  

   Returns: A System.Security.AccessControl.SemaphoreAccessRule object representing the specified rights for 

    the specified user.
  """
  pass
 def AddAccessRule(self,rule):
  """
  AddAccessRule(self: SemaphoreSecurity,rule: SemaphoreAccessRule)

   Searches for a matching rule with which the new rule can be merged. If none are found,adds the 

    new rule.

  

  

   rule: The access control rule to add.
  """
  pass
 def AddAuditRule(self,rule):
  """
  AddAuditRule(self: SemaphoreSecurity,rule: SemaphoreAuditRule)

   Searches for an audit rule with which the new rule can be merged. If none are found,adds the 

    new rule.

  

  

   rule: The audit rule to add. The user specified by this rule determines the search.
  """
  pass
 def AuditRuleFactory(self,identityReference,accessMask,isInherited,inheritanceFlags,propagationFlags,flags):
  """
  AuditRuleFactory(self: SemaphoreSecurity,identityReference: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,flags: AuditFlags) -> AuditRule

  

   Creates a new audit rule,specifying the user the rule applies to,the access rights to audit,

    and the outcome that triggers the audit rule.

  

  

   identityReference: An System.Security.Principal.IdentityReference that identifies the user or group the rule 

    applies to.

  

   accessMask: A bitwise combination of System.Security.AccessControl.SemaphoreRights values specifying the 

    access rights to audit,cast to an integer.

  

   isInherited: Meaningless for named wait handles,because they have no hierarchy.

   inheritanceFlags: Meaningless for named wait handles,because they have no hierarchy.

   propagationFlags: Meaningless for named wait handles,because they have no hierarchy.

   flags: A bitwise combination of System.Security.AccessControl.AuditFlags values that specify whether to 

    audit successful access,failed access,or both.

  

   Returns: A System.Security.AccessControl.SemaphoreAuditRule object representing the specified audit rule 

    for the specified user. The return type of the method is the base class,

    System.Security.AccessControl.AuditRule,but the return value can be cast safely to the derived 

    class.
  """
  pass
 def RemoveAccessRule(self,rule):
  """
  RemoveAccessRule(self: SemaphoreSecurity,rule: SemaphoreAccessRule) -> bool

  

   Searches for an access control rule with the same user and 

    System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule,and with 

    compatible inheritance and propagation flags; if such a rule is found,the rights contained in 

    the specified access rule are removed from it.

  

  

   rule: A System.Security.AccessControl.SemaphoreAccessRule that specifies the user and 

    System.Security.AccessControl.AccessControlType to search for,and a set of inheritance and 

    propagation flags that a matching rule,if found,must be compatible with. Specifies the rights 

    to remove from the compatible rule,if found.

  

   Returns: true if a compatible rule is found; otherwise false.
  """
  pass
 def RemoveAccessRuleAll(self,rule):
  """
  RemoveAccessRuleAll(self: SemaphoreSecurity,rule: SemaphoreAccessRule)

   Searches for all access control rules with the same user and 

    System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule and,if 

    found,removes them.

  

  

   rule: A System.Security.AccessControl.SemaphoreAccessRule that specifies the user and 

    System.Security.AccessControl.AccessControlType to search for. Any rights specified by this rule 

    are ignored.
  """
  pass
 def RemoveAccessRuleSpecific(self,rule):
  """
  RemoveAccessRuleSpecific(self: SemaphoreSecurity,rule: SemaphoreAccessRule)

   Searches for an access control rule that exactly matches the specified rule and,if found,

    removes it.

  

  

   rule: The System.Security.AccessControl.SemaphoreAccessRule to remove.
  """
  pass
 def RemoveAuditRule(self,rule):
  """
  RemoveAuditRule(self: SemaphoreSecurity,rule: SemaphoreAuditRule) -> bool

  

   Searches for an audit control rule with the same user as the specified rule,and with compatible 

    inheritance and propagation flags; if a compatible rule is found,the rights contained in the 

    specified rule are removed from it.

  

  

   rule: A System.Security.AccessControl.SemaphoreAuditRule that specifies the user to search for,and a 

    set of inheritance and propagation flags that a matching rule,if found,must be compatible 

    with. Specifies the rights to remove from the compatible rule,if found.

  

   Returns: true if a compatible rule is found; otherwise,false.
  """
  pass
 def RemoveAuditRuleAll(self,rule):
  """
  RemoveAuditRuleAll(self: SemaphoreSecurity,rule: SemaphoreAuditRule)

   Searches for all audit rules with the same user as the specified rule and,if found,removes 

    them.

  

  

   rule: A System.Security.AccessControl.SemaphoreAuditRule that specifies the user to search for. Any 

    rights specified by this rule are ignored.
  """
  pass
 def RemoveAuditRuleSpecific(self,rule):
  """
  RemoveAuditRuleSpecific(self: SemaphoreSecurity,rule: SemaphoreAuditRule)

   Searches for an audit rule that exactly matches the specified rule and,if found,removes it.

  

   rule: The System.Security.AccessControl.SemaphoreAuditRule to remove.
  """
  pass
 def ResetAccessRule(self,rule):
  """
  ResetAccessRule(self: SemaphoreSecurity,rule: SemaphoreAccessRule)

   Removes all access control rules with the same user as the specified rule,regardless of 

    System.Security.AccessControl.AccessControlType,and then adds the specified rule.

  

  

   rule: The System.Security.AccessControl.SemaphoreAccessRule to add. The user specified by this rule 

    determines the rules to remove before this rule is added.
  """
  pass
 def SetAccessRule(self,rule):
  """
  SetAccessRule(self: SemaphoreSecurity,rule: SemaphoreAccessRule)

   Removes all access control rules with the same user and 

    System.Security.AccessControl.AccessControlType (allow or deny) as the specified rule,and then 

    adds the specified rule.

  

  

   rule: The System.Security.AccessControl.SemaphoreAccessRule to add. The user and 

    System.Security.AccessControl.AccessControlType of this rule determine the rules to remove 

    before this rule is added.
  """
  pass
 def SetAuditRule(self,rule):
  """
  SetAuditRule(self: SemaphoreSecurity,rule: SemaphoreAuditRule)

   Removes all audit rules with the same user as the specified rule,regardless of the 

    System.Security.AccessControl.AuditFlags value,and then adds the specified rule.

  

  

   rule: The System.Security.AccessControl.SemaphoreAuditRule to add. The user specified by this rule 

    determines the rules to remove before this rule is added.
  """
  pass
 @staticmethod
 def __new__(self,name=None,includeSections=None):
  """
  __new__(cls: type)

  __new__(cls: type,name: str,includeSections: AccessControlSections)
  """
  pass
 AccessRightType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the enumeration that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rights.



Get: AccessRightType(self: SemaphoreSecurity) -> Type



"""

 AccessRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AccessRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent access rules.



Get: AccessRuleType(self: SemaphoreSecurity) -> Type



"""

 AuditRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AuditRuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that the System.Security.AccessControl.SemaphoreSecurity class uses to represent audit rules.



Get: AuditRuleType(self: SemaphoreSecurity) -> Type



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


