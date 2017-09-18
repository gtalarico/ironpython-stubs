class SystemAcl(CommonAcl,ICollection,IEnumerable):
 """
 Represents a System Access Control List (SACL).

 

 SystemAcl(isContainer: bool,isDS: bool,capacity: int)

 SystemAcl(isContainer: bool,isDS: bool,revision: Byte,capacity: int)

 SystemAcl(isContainer: bool,isDS: bool,rawAcl: RawAcl)
 """
 def AddAudit(self,*__args):
  """
  AddAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Adds an audit rule with the specified settings to the current 

    System.Security.AccessControl.SystemAcl object. Use this method for directory object Access 

    Control Lists (ACLs) when specifying the object type or the inherited object type for the new 

    audit rule.

  

  

   auditFlags: The type of audit rule to add.

   sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.

   accessMask: The access mask for the new audit rule.

   inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

   propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the new audit rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.

  AddAudit(self: SystemAcl,sid: SecurityIdentifier,rule: ObjectAuditRule)AddAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Adds an audit rule to the current System.Security.AccessControl.SystemAcl object.

  

   auditFlags: The type of audit rule to add.

   sid: The System.Security.Principal.SecurityIdentifier for which to add an audit rule.

   accessMask: The access mask for the new audit rule.

   inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

   propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
  """
  pass
 def RemoveAudit(self,*__args):
  """
  RemoveAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid) -> bool

  

   Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl 

    object. Use this method for directory object Access Control Lists (ACLs) when specifying the 

    object type or the inherited object type.

  

  

   auditFlags: The type of audit rule to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

   accessMask: The access mask for the rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the removed audit control rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.

   Returns: true if this method successfully removes the specified audit rule; otherwise,false.

  RemoveAudit(self: SystemAcl,sid: SecurityIdentifier,rule: ObjectAuditRule) -> bool

  RemoveAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags) -> bool

  

   Removes the specified audit rule from the current System.Security.AccessControl.SystemAcl object.

  

   auditFlags: The type of audit rule to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

   accessMask: The access mask for the rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

   Returns: true if this method successfully removes the specified audit rule; otherwise,false.
  """
  pass
 def RemoveAuditSpecific(self,*__args):
  """
  RemoveAuditSpecific(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl 

    object. Use this method for directory object Access Control Lists (ACLs) when specifying the 

    object type or the inherited object type.

  

  

   auditFlags: The type of audit rule to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

   accessMask: The access mask for the rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the removed audit control rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the removed audit rule.

  RemoveAuditSpecific(self: SystemAcl,sid: SecurityIdentifier,rule: ObjectAuditRule)RemoveAuditSpecific(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Removes the specified audit rule from the current System.Security.AccessControl.DiscretionaryAcl 

    object.

  

  

   auditFlags: The type of audit rule to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an audit rule.

   accessMask: The access mask for the rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.
  """
  pass
 def SetAudit(self,*__args):
  """
  SetAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier 

    object. Use this method for directory object Access Control Lists (ACLs) when specifying the 

    object type or the inherited object type.

  

  

   auditFlags: The audit condition to set.

   sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.

   accessMask: The access mask for the new audit rule.

   inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

   propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the new audit rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new audit rule.

  SetAudit(self: SystemAcl,sid: SecurityIdentifier,rule: ObjectAuditRule)SetAudit(self: SystemAcl,auditFlags: AuditFlags,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Sets the specified audit rule for the specified System.Security.Principal.SecurityIdentifier 

    object.

  

  

   auditFlags: The audit condition to set.

   sid: The System.Security.Principal.SecurityIdentifier for which to set an audit rule.

   accessMask: The access mask for the new audit rule.

   inheritanceFlags: Flags that specify the inheritance properties of the new audit rule.

   propagationFlags: Flags that specify the inheritance propagation properties for the new audit rule.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,isContainer,isDS,*__args):
  """
  __new__(cls: type,isContainer: bool,isDS: bool,capacity: int)

  __new__(cls: type,isContainer: bool,isDS: bool,revision: Byte,capacity: int)

  __new__(cls: type,isContainer: bool,isDS: bool,rawAcl: RawAcl)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

