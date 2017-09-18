class CommonObjectSecurity(ObjectSecurity):
 """ Controls access to objects without direct manipulation of access control lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.NativeObjectSecurity class. """
 def AddAccessRule(self,*args):
  """
  AddAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 

    this System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to add.
  """
  pass
 def AddAuditRule(self,*args):
  """
  AddAuditRule(self: CommonObjectSecurity,rule: AuditRule)

   Adds the specified audit rule to the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to add.
  """
  pass
 def GetAccessRules(self,includeExplicit,includeInherited,targetType):
  """
  GetAccessRules(self: CommonObjectSecurity,includeExplicit: bool,includeInherited: bool,targetType: Type) -> AuthorizationRuleCollection

  

   Gets a collection of the access rules associated with the specified security identifier.

  

   includeExplicit: true to include access rules explicitly set for the object.

   includeInherited: true to include inherited access rules.

   targetType: Specifies whether the security identifier for which to retrieve access rules is of type 

    T:System.Security.Principal.SecurityIdentifier or type T:System.Security.Principal.NTAccount. 

    The value of this parameter must be a type that can be translated to  the 

    System.Security.Principal.SecurityIdentifier type.

  

   Returns: The collection of access rules associated with the specified 

    System.Security.Principal.SecurityIdentifier object.
  """
  pass
 def GetAuditRules(self,includeExplicit,includeInherited,targetType):
  """
  GetAuditRules(self: CommonObjectSecurity,includeExplicit: bool,includeInherited: bool,targetType: Type) -> AuthorizationRuleCollection

  

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
  RemoveAccessRule(self: CommonObjectSecurity,rule: AccessRule) -> bool

  

   Removes access rules that contain the same security identifier and access mask as the specified 

    access rule from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.

   Returns: true if the access rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAccessRuleAll(self,*args):
  """
  RemoveAccessRuleAll(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that have the same security identifier as the specified access rule 

    from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAccessRuleSpecific(self,*args):
  """
  RemoveAccessRuleSpecific(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that exactly match the specified access rule from the Discretionary 

    Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAuditRule(self,*args):
  """
  RemoveAuditRule(self: CommonObjectSecurity,rule: AuditRule) -> bool

  

   Removes audit rules that contain the same security identifier and access mask as the specified 

    audit rule from the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to remove.

   Returns: true if the audit rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAuditRuleAll(self,*args):
  """
  RemoveAuditRuleAll(self: CommonObjectSecurity,rule: AuditRule)

   Removes all audit rules that have the same security identifier as the specified audit rule from 

    the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def RemoveAuditRuleSpecific(self,*args):
  """
  RemoveAuditRuleSpecific(self: CommonObjectSecurity,rule: AuditRule)

   Removes all audit rules that exactly match the specified audit rule from the System Access 

    Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity 

    object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def ResetAccessRule(self,*args):
  """
  ResetAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to reset.
  """
  pass
 def SetAccessRule(self,*args):
  """
  SetAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that contain the same security identifier and qualifier as the 

    specified access rule in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to set.
  """
  pass
 def SetAuditRule(self,*args):
  """
  SetAuditRule(self: CommonObjectSecurity,rule: AuditRule)

   Removes all audit rules that contain the same security identifier and qualifier as the specified 

    audit rule in the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object and then adds the specified audit 

    rule.

  

  

   rule: The audit rule to set.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,isContainer: bool) """
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


