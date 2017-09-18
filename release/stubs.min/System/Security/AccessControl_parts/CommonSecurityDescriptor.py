class CommonSecurityDescriptor(GenericSecurityDescriptor):
 """
 Represents a security descriptor. A security descriptor includes an owner,a primary group,a Discretionary Access Control List (DACL),and a System Access Control List (SACL).

 

 CommonSecurityDescriptor(isContainer: bool,isDS: bool,flags: ControlFlags,owner: SecurityIdentifier,group: SecurityIdentifier,systemAcl: SystemAcl,discretionaryAcl: DiscretionaryAcl)

 CommonSecurityDescriptor(isContainer: bool,isDS: bool,rawSecurityDescriptor: RawSecurityDescriptor)

 CommonSecurityDescriptor(isContainer: bool,isDS: bool,sddlForm: str)

 CommonSecurityDescriptor(isContainer: bool,isDS: bool,binaryForm: Array[Byte],offset: int)
 """
 def AddDiscretionaryAcl(self,revision,trusted):
  """ AddDiscretionaryAcl(self: CommonSecurityDescriptor,revision: Byte,trusted: int) """
  pass
 def AddSystemAcl(self,revision,trusted):
  """ AddSystemAcl(self: CommonSecurityDescriptor,revision: Byte,trusted: int) """
  pass
 def PurgeAccessControl(self,sid):
  """
  PurgeAccessControl(self: CommonSecurityDescriptor,sid: SecurityIdentifier)

   Removes all access rules for the specified security identifier from the Discretionary Access 

    Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor 

    object.

  

  

   sid: The security identifier for which to remove access rules.
  """
  pass
 def PurgeAudit(self,sid):
  """
  PurgeAudit(self: CommonSecurityDescriptor,sid: SecurityIdentifier)

   Removes all audit rules for the specified security identifier from the System Access Control 

    List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object.

  

  

   sid: The security identifier for which to remove audit rules.
  """
  pass
 def SetDiscretionaryAclProtection(self,isProtected,preserveInheritance):
  """
  SetDiscretionaryAclProtection(self: CommonSecurityDescriptor,isProtected: bool,preserveInheritance: bool)

   Sets the inheritance protection for the Discretionary Access Control List (DACL) associated with 

    this System.Security.AccessControl.CommonSecurityDescriptor object. DACLs that are protected do 

    not inherit access rules from parent containers.

  

  

   isProtected: true to protect the DACL from inheritance.

   preserveInheritance: true to keep inherited access rules in the DACL; false to remove inherited access rules from the 

    DACL.
  """
  pass
 def SetSystemAclProtection(self,isProtected,preserveInheritance):
  """
  SetSystemAclProtection(self: CommonSecurityDescriptor,isProtected: bool,preserveInheritance: bool)

   Sets the inheritance protection for the System Access Control List (SACL) associated with this 

    System.Security.AccessControl.CommonSecurityDescriptor object. SACLs that are protected do not 

    inherit audit rules from parent containers.

  

  

   isProtected: true to protect the SACL from inheritance.

   preserveInheritance: true to keep inherited audit rules in the SACL; false to remove inherited audit rules from the 

    SACL.
  """
  pass
 @staticmethod
 def __new__(self,isContainer,isDS,*__args):
  """
  __new__(cls: type,isContainer: bool,isDS: bool,flags: ControlFlags,owner: SecurityIdentifier,group: SecurityIdentifier,systemAcl: SystemAcl,discretionaryAcl: DiscretionaryAcl)

  __new__(cls: type,isContainer: bool,isDS: bool,rawSecurityDescriptor: RawSecurityDescriptor)

  __new__(cls: type,isContainer: bool,isDS: bool,sddlForm: str)

  __new__(cls: type,isContainer: bool,isDS: bool,binaryForm: Array[Byte],offset: int)
  """
  pass
 ControlFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values that specify behavior of the System.Security.AccessControl.CommonSecurityDescriptor object.



Get: ControlFlags(self: CommonSecurityDescriptor) -> ControlFlags



"""

 DiscretionaryAcl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the discretionary access control list (DACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The DACL contains access rules.



Get: DiscretionaryAcl(self: CommonSecurityDescriptor) -> DiscretionaryAcl



Set: DiscretionaryAcl(self: CommonSecurityDescriptor)=value

"""

 Group=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the primary group for this System.Security.AccessControl.CommonSecurityDescriptor object.



Get: Group(self: CommonSecurityDescriptor) -> SecurityIdentifier



Set: Group(self: CommonSecurityDescriptor)=value

"""

 IsContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a container object.



Get: IsContainer(self: CommonSecurityDescriptor) -> bool



"""

 IsDiscretionaryAclCanonical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether the Discretionary Access Control List (DACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.



Get: IsDiscretionaryAclCanonical(self: CommonSecurityDescriptor) -> bool



"""

 IsDS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object is a directory object.



Get: IsDS(self: CommonSecurityDescriptor) -> bool



"""

 IsSystemAclCanonical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether the System Access Control List (SACL) associated with this System.Security.AccessControl.CommonSecurityDescriptor object is in canonical order.



Get: IsSystemAclCanonical(self: CommonSecurityDescriptor) -> bool



"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the owner of the object associated with this System.Security.AccessControl.CommonSecurityDescriptor object.



Get: Owner(self: CommonSecurityDescriptor) -> SecurityIdentifier



Set: Owner(self: CommonSecurityDescriptor)=value

"""

 SystemAcl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.CommonSecurityDescriptor object. The SACL contains audit rules.



Get: SystemAcl(self: CommonSecurityDescriptor) -> SystemAcl



Set: SystemAcl(self: CommonSecurityDescriptor)=value

"""


