class GenericSecurityDescriptor(object):
 """ Represents a security descriptor. A security descriptor includes an owner,a primary group,a Discretionary Access Control List (DACL),and a System Access Control List (SACL). """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: GenericSecurityDescriptor,binaryForm: Array[Byte],offset: int)

   Returns an array of byte values that represents the information contained in this 

    System.Security.AccessControl.GenericSecurityDescriptor object.

  

  

   binaryForm: The byte array into which the contents of the 

    System.Security.AccessControl.GenericSecurityDescriptor is marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 def GetSddlForm(self,includeSections):
  """
  GetSddlForm(self: GenericSecurityDescriptor,includeSections: AccessControlSections) -> str

  

   Returns the Security Descriptor Definition Language (SDDL) representation of the specified 

    sections of the security descriptor that this 

    System.Security.AccessControl.GenericSecurityDescriptor object represents.

  

  

   includeSections: Specifies which sections (access rules,audit rules,primary group,owner) of the security 

    descriptor to get.

  

   Returns: The SDDL representation of the specified sections of the security descriptor associated with 

    this System.Security.AccessControl.GenericSecurityDescriptor object.
  """
  pass
 @staticmethod
 def IsSddlConversionSupported():
  """
  IsSddlConversionSupported() -> bool

  

   Returns a boolean value that specifies whether the security descriptor associated with this  

    System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security 

    Descriptor Definition Language (SDDL) format.

  

   Returns: true if the security descriptor associated with this  

    System.Security.AccessControl.GenericSecurityDescriptor object can be converted to the Security 

    Descriptor Definition Language (SDDL) format; otherwise,false.
  """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.GenericSecurityDescriptor object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericSecurityDescriptor.GetBinaryForm method.



Get: BinaryLength(self: GenericSecurityDescriptor) -> int



"""

 ControlFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values that specify behavior of the System.Security.AccessControl.GenericSecurityDescriptor object.



Get: ControlFlags(self: GenericSecurityDescriptor) -> ControlFlags



"""

 Group=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the primary group for this System.Security.AccessControl.GenericSecurityDescriptor object.



Get: Group(self: GenericSecurityDescriptor) -> SecurityIdentifier



Set: Group(self: GenericSecurityDescriptor)=value

"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the owner of the object associated with this System.Security.AccessControl.GenericSecurityDescriptor object.



Get: Owner(self: GenericSecurityDescriptor) -> SecurityIdentifier



Set: Owner(self: GenericSecurityDescriptor)=value

"""


 Revision=None

