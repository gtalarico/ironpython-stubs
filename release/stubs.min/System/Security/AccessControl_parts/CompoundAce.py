class CompoundAce(KnownAce):
 """
 Represents a compound Access Control Entry (ACE).

 

 CompoundAce(flags: AceFlags,accessMask: int,compoundAceType: CompoundAceType,sid: SecurityIdentifier)
 """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: CompoundAce,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.CompoundAce object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.CompoundAce is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 @staticmethod
 def __new__(self,flags,accessMask,compoundAceType,sid):
  """ __new__(cls: type,flags: AceFlags,accessMask: int,compoundAceType: CompoundAceType,sid: SecurityIdentifier) """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.CompoundAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.CompoundAce.GetBinaryForm method.



Get: BinaryLength(self: CompoundAce) -> int



"""

 CompoundAceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of this System.Security.AccessControl.CompoundAce object.



Get: CompoundAceType(self: CompoundAce) -> CompoundAceType



Set: CompoundAceType(self: CompoundAce)=value

"""


