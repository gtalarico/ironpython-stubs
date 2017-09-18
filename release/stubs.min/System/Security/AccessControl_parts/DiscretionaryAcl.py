class DiscretionaryAcl(CommonAcl,ICollection,IEnumerable):
 """
 Represents a Discretionary Access Control List (DACL).

 

 DiscretionaryAcl(isContainer: bool,isDS: bool,capacity: int)

 DiscretionaryAcl(isContainer: bool,isDS: bool,revision: Byte,capacity: int)

 DiscretionaryAcl(isContainer: bool,isDS: bool,rawAcl: RawAcl)
 """
 def AddAccess(self,accessType,sid,*__args):
  """
  AddAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Adds an Access Control Entry (ACE) with the specified settings to the current 

    System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 

    Access Control Lists (ACLs) when specifying the object type or the inherited object type for the 

    new ACE.

  

  

   accessType: The type of access control (allow or deny) to add.

   sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.

   accessMask: The access rule for the new ACE.

   inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

   propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the new ACE applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.

  AddAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,rule: ObjectAccessRule)AddAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Adds an Access Control Entry (ACE) with the specified settings to the current 

    System.Security.AccessControl.DiscretionaryAcl object.

  

  

   accessType: The type of access control (allow or deny) to add.

   sid: The System.Security.Principal.SecurityIdentifier for which to add an ACE.

   accessMask: The access rule for the new ACE.

   inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

   propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
  """
  pass
 def RemoveAccess(self,accessType,sid,*__args):
  """
  RemoveAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid) -> bool

  

   Removes the specified access control rule from the current 

    System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 

    Access Control Lists (ACLs) when specifying the object type or the inherited object type.

  

  

   accessType: The type of access control (allow or deny) to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.

   accessMask: The access mask for the access control rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the access control rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the access control rule to be 

    removed.

  

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the removed access control rule applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the removed access control rule.

   Returns: true if this method successfully removes the specified access; otherwise,false.

  RemoveAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,rule: ObjectAccessRule) -> bool

  RemoveAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags) -> bool

  

   Removes the specified access control rule from the current 

    System.Security.AccessControl.DiscretionaryAcl object.

  

  

   accessType: The type of access control (allow or deny) to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an access control rule.

   accessMask: The access mask for the rule to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the rule to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the rule to be removed.

   Returns: true if this method successfully removes the specified access; otherwise,false.
  """
  pass
 def RemoveAccessSpecific(self,accessType,sid,*__args):
  """
  RemoveAccessSpecific(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Removes the specified Access Control Entry (ACE) from the current 

    System.Security.AccessControl.DiscretionaryAcl object. Use this method for directory object 

    Access Control Lists (ACLs) when specifying the object type or the inherited object type for the 

    ACE to be removed.

  

  

   accessType: The type of access control (allow or deny) to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.

   accessMask: The access mask for the ACE to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the removed ACE applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the removed ACE.

  RemoveAccessSpecific(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,rule: ObjectAccessRule)RemoveAccessSpecific(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Removes the specified Access Control Entry (ACE) from the current 

    System.Security.AccessControl.DiscretionaryAcl object.

  

  

   accessType: The type of access control (allow or deny) to remove.

   sid: The System.Security.Principal.SecurityIdentifier for which to remove an ACE.

   accessMask: The access mask for the ACE to be removed.

   inheritanceFlags: Flags that specify the inheritance properties of the ACE to be removed.

   propagationFlags: Flags that specify the inheritance propagation properties for the ACE to be removed.
  """
  pass
 def SetAccess(self,accessType,sid,*__args):
  """
  SetAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectFlags: ObjectAceFlags,objectType: Guid,inheritedObjectType: Guid)

   Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier 

    object.

  

  

   accessType: The type of access control (allow or deny) to set.

   sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.

   accessMask: The access rule for the new ACE.

   inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

   propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.

   objectFlags: Flags that specify if the objectType and inheritedObjectType parameters contain non-null values.

   objectType: The identity of the class of objects to which the new ACE applies.

   inheritedObjectType: The identity of the class of child objects which can inherit the new ACE.

  SetAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,rule: ObjectAccessRule)SetAccess(self: DiscretionaryAcl,accessType: AccessControlType,sid: SecurityIdentifier,accessMask: int,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags)

   Sets the specified access control for the specified System.Security.Principal.SecurityIdentifier 

    object.

  

  

   accessType: The type of access control (allow or deny) to set.

   sid: The System.Security.Principal.SecurityIdentifier for which to set an ACE.

   accessMask: The access rule for the new ACE.

   inheritanceFlags: Flags that specify the inheritance properties of the new ACE.

   propagationFlags: Flags that specify the inheritance propagation properties for the new ACE.
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
