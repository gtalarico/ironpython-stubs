class CustomAce(GenericAce):
 """
 Represents an Access Control Entry (ACE) that is not defined by one of the members of the System.Security.AccessControl.AceType enumeration.

 

 CustomAce(type: AceType,flags: AceFlags,opaque: Array[Byte])
 """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: CustomAce,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.CustomAce object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.CustomAce is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 def GetOpaque(self):
  """
  GetOpaque(self: CustomAce) -> Array[Byte]

  

   Returns the opaque data associated with this System.Security.AccessControl.CustomAce object.

   Returns: An array of byte values that represents the opaque data associated with this 

    System.Security.AccessControl.CustomAce object.
  """
  pass
 def SetOpaque(self,opaque):
  """
  SetOpaque(self: CustomAce,opaque: Array[Byte])

   Sets the opaque callback data associated with this System.Security.AccessControl.CustomAce 

    object.

  

  

   opaque: An array of byte values that represents the opaque callback data for this 

    System.Security.AccessControl.CustomAce object.
  """
  pass
 @staticmethod
 def __new__(self,type,flags,opaque):
  """ __new__(cls: type,type: AceType,flags: AceFlags,opaque: Array[Byte]) """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.CustomAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CustomAce.GetBinaryForm method.



Get: BinaryLength(self: CustomAce) -> int



"""

 OpaqueLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the opaque data associated with this System.Security.AccessControl.CustomAce object.



Get: OpaqueLength(self: CustomAce) -> int



"""


 MaxOpaqueLength=65531

