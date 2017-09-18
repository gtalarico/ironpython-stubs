class CommonAce(QualifiedAce):
 """
 Represents an access control entry (ACE).

 

 CommonAce(flags: AceFlags,qualifier: AceQualifier,accessMask: int,sid: SecurityIdentifier,isCallback: bool,opaque: Array[Byte])
 """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: CommonAce,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.CommonAce object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.CommonAce object is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 @staticmethod
 def MaxOpaqueLength(isCallback):
  """
  MaxOpaqueLength(isCallback: bool) -> int

  

   Gets the maximum allowed length of an opaque data BLOB for callback access control entries 

    (ACEs).

  

  

   isCallback: true to specify that the System.Security.AccessControl.CommonAce object is a callback ACE type.

   Returns: The allowed length of an opaque data BLOB.
  """
  pass
 @staticmethod
 def __new__(self,flags,qualifier,accessMask,sid,isCallback,opaque):
  """ __new__(cls: type,flags: AceFlags,qualifier: AceQualifier,accessMask: int,sid: SecurityIdentifier,isCallback: bool,opaque: Array[Byte]) """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.CommonAce object. Use this length with the System.Security.AccessControl.CommonAce.GetBinaryForm(System.Byte[],System.Int32) method before marshaling the ACL into a binary array.



Get: BinaryLength(self: CommonAce) -> int



"""


