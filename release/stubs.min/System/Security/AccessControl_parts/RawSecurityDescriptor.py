class RawSecurityDescriptor(GenericSecurityDescriptor):
 """
 Represents a security descriptor. A security descriptor includes an owner,a primary group,a Discretionary Access Control List (DACL),and a System Access Control List (SACL).

 

 RawSecurityDescriptor(flags: ControlFlags,owner: SecurityIdentifier,group: SecurityIdentifier,systemAcl: RawAcl,discretionaryAcl: RawAcl)

 RawSecurityDescriptor(sddlForm: str)

 RawSecurityDescriptor(binaryForm: Array[Byte],offset: int)
 """
 def SetFlags(self,flags):
  """
  SetFlags(self: RawSecurityDescriptor,flags: ControlFlags)

   Sets the System.Security.AccessControl.RawSecurityDescriptor.ControlFlags property of this 

    System.Security.AccessControl.RawSecurityDescriptor object to the specified value.

  

  

   flags: One or more values of the System.Security.AccessControl.ControlFlags enumeration combined with a 

    logical OR operation.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,flags: ControlFlags,owner: SecurityIdentifier,group: SecurityIdentifier,systemAcl: RawAcl,discretionaryAcl: RawAcl)

  __new__(cls: type,sddlForm: str)

  __new__(cls: type,binaryForm: Array[Byte],offset: int)
  """
  pass
 ControlFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values that specify behavior of the System.Security.AccessControl.RawSecurityDescriptor object.



Get: ControlFlags(self: RawSecurityDescriptor) -> ControlFlags



"""

 DiscretionaryAcl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Discretionary Access Control List (DACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The DACL contains access rules.



Get: DiscretionaryAcl(self: RawSecurityDescriptor) -> RawAcl



Set: DiscretionaryAcl(self: RawSecurityDescriptor)=value

"""

 Group=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the primary group for this System.Security.AccessControl.RawSecurityDescriptor object.



Get: Group(self: RawSecurityDescriptor) -> SecurityIdentifier



Set: Group(self: RawSecurityDescriptor)=value

"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the owner of the object associated with this System.Security.AccessControl.RawSecurityDescriptor object.



Get: Owner(self: RawSecurityDescriptor) -> SecurityIdentifier



Set: Owner(self: RawSecurityDescriptor)=value

"""

 ResourceManagerControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a byte value that represents the resource manager control bits associated with this System.Security.AccessControl.RawSecurityDescriptor object.



Get: ResourceManagerControl(self: RawSecurityDescriptor) -> Byte



Set: ResourceManagerControl(self: RawSecurityDescriptor)=value

"""

 SystemAcl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System Access Control List (SACL) for this System.Security.AccessControl.RawSecurityDescriptor object. The SACL contains audit rules.



Get: SystemAcl(self: RawSecurityDescriptor) -> RawAcl



Set: SystemAcl(self: RawSecurityDescriptor)=value

"""


