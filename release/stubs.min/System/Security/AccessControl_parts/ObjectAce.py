class ObjectAce(QualifiedAce):
 """
 Controls access to Directory Services objects. This class represents an Access Control Entry (ACE) associated with a directory object.

 

 ObjectAce(aceFlags: AceFlags,qualifier: AceQualifier,accessMask: int,sid: SecurityIdentifier,flags: ObjectAceFlags,type: Guid,inheritedType: Guid,isCallback: bool,opaque: Array[Byte])
 """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: ObjectAce,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.ObjectAce object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.ObjectAce is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 @staticmethod
 def MaxOpaqueLength(isCallback):
  """
  MaxOpaqueLength(isCallback: bool) -> int

  

   Returns the maximum allowed length,in bytes,of an opaque data BLOB for callback Access Control 

    Entries (ACEs).

  

  

   isCallback: True if the System.Security.AccessControl.ObjectAce is a callback ACE type.

   Returns: The maximum allowed length,in bytes,of an opaque data BLOB for callback Access Control Entries 

    (ACEs).
  """
  pass
 @staticmethod
 def __new__(self,aceFlags,qualifier,accessMask,sid,flags,type,inheritedType,isCallback,opaque):
  """ __new__(cls: type,aceFlags: AceFlags,qualifier: AceQualifier,accessMask: int,sid: SecurityIdentifier,flags: ObjectAceFlags,type: Guid,inheritedType: Guid,isCallback: bool,opaque: Array[Byte]) """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.ObjectAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.ObjectAce.GetBinaryForm method.



Get: BinaryLength(self: ObjectAce) -> int



"""

 InheritedObjectAceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the GUID of the object type that can inherit the Access Control Entry (ACE) that this System.Security.AccessControl.ObjectAce object represents.



Get: InheritedObjectAceType(self: ObjectAce) -> Guid



Set: InheritedObjectAceType(self: ObjectAce)=value

"""

 ObjectAceFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets flags that specify whether the System.Security.AccessControl.ObjectAce.ObjectAceType and System.Security.AccessControl.ObjectAce.InheritedObjectAceType properties contain values that identify valid object types.



Get: ObjectAceFlags(self: ObjectAce) -> ObjectAceFlags



Set: ObjectAceFlags(self: ObjectAce)=value

"""

 ObjectAceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the GUID of the object type associated with this System.Security.AccessControl.ObjectAce object.



Get: ObjectAceType(self: ObjectAce) -> Guid



Set: ObjectAceType(self: ObjectAce)=value

"""


