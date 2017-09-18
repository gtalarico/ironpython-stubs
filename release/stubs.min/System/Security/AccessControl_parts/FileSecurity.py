class FileSecurity(FileSystemSecurity):
 """
 Represents the access control and audit security for a file. This class cannot be inherited.

 

 FileSecurity(fileName: str,includeSections: AccessControlSections)

 FileSecurity()
 """
 def AddAccessRule(self,rule):
  """
  AddAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Adds the specified access rule to the Discretionary Access Control List (DACL) associated with 

    this System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to add.
  """
  pass
 def AddAuditRule(self,rule):
  """
  AddAuditRule(self: CommonObjectSecurity,rule: AuditRule)

   Adds the specified audit rule to the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to add.
  """
  pass
 def RemoveAccessRule(self,rule):
  """
  RemoveAccessRule(self: CommonObjectSecurity,rule: AccessRule) -> bool

  

   Removes access rules that contain the same security identifier and access mask as the specified 

    access rule from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.

   Returns: true if the access rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAccessRuleAll(self,rule):
  """
  RemoveAccessRuleAll(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that have the same security identifier as the specified access rule 

    from the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAccessRuleSpecific(self,rule):
  """
  RemoveAccessRuleSpecific(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that exactly match the specified access rule from the Discretionary 

    Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The access rule to remove.
  """
  pass
 def RemoveAuditRule(self,rule):
  """
  RemoveAuditRule(self: CommonObjectSecurity,rule: AuditRule) -> bool

  

   Removes audit rules that contain the same security identifier and access mask as the specified 

    audit rule from the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to remove.

   Returns: true if the audit rule was successfully removed; otherwise,false.
  """
  pass
 def RemoveAuditRuleAll(self,rule):
  """
  RemoveAuditRuleAll(self: CommonObjectSecurity,rule: AuditRule)

   Removes all audit rules that have the same security identifier as the specified audit rule from 

    the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def RemoveAuditRuleSpecific(self,rule):
  """
  RemoveAuditRuleSpecific(self: CommonObjectSecurity,rule: AuditRule)

   Removes all audit rules that exactly match the specified audit rule from the System Access 

    Control List (SACL) associated with this System.Security.AccessControl.CommonObjectSecurity 

    object.

  

  

   rule: The audit rule to remove.
  """
  pass
 def ResetAccessRule(self,rule):
  """
  ResetAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to reset.
  """
  pass
 def SetAccessRule(self,rule):
  """
  SetAccessRule(self: CommonObjectSecurity,rule: AccessRule)

   Removes all access rules that contain the same security identifier and qualifier as the 

    specified access rule in the Discretionary Access Control List (DACL) associated with this 

    System.Security.AccessControl.CommonObjectSecurity object and then adds the specified access 

    rule.

  

  

   rule: The access rule to set.
  """
  pass
 def SetAuditRule(self,rule):
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
 def __new__(self,fileName=None,includeSections=None):
  """
  __new__(cls: type)

  __new__(cls: type,fileName: str,includeSections: AccessControlSections)
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


