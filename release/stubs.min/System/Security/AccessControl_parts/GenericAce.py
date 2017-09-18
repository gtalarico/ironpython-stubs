class GenericAce(object):
 """ Represents an Access Control Entry (ACE),and is the base class for all other ACE classes. """
 def Copy(self):
  """
  Copy(self: GenericAce) -> GenericAce

  

   Creates a deep copy of this Access Control Entry (ACE).

   Returns: The System.Security.AccessControl.GenericAce object that this method creates.
  """
  pass
 @staticmethod
 def CreateFromBinaryForm(binaryForm,offset):
  """
  CreateFromBinaryForm(binaryForm: Array[Byte],offset: int) -> GenericAce

  

   Creates a System.Security.AccessControl.GenericAce object from the specified binary data.

  

   binaryForm: The binary data from which to create the new System.Security.AccessControl.GenericAce object.

   offset: The offset at which to begin unmarshaling.

   Returns: The System.Security.AccessControl.GenericAce object this method creates.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: GenericAce,o: object) -> bool

  

   Determines whether the specified System.Security.AccessControl.GenericAce object is equal to the 

    current System.Security.AccessControl.GenericAce object.

  

  

   o: The System.Security.AccessControl.GenericAce object to compare to the current 

    System.Security.AccessControl.GenericAce object.

  

   Returns: true if the specified System.Security.AccessControl.GenericAce object is equal to the current 

    System.Security.AccessControl.GenericAce object; otherwise,false.
  """
  pass
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: GenericAce,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.GenericAce object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAce is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GenericAce) -> int

  

   Serves as a hash function for the System.Security.AccessControl.GenericAce class. The  

    System.Security.AccessControl.GenericAce.GetHashCode method is suitable for use in hashing 

    algorithms and data structures like a hash table.

  

   Returns: A hash code for the current System.Security.AccessControl.GenericAce object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 AceFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Security.AccessControl.AceFlags associated with this System.Security.AccessControl.GenericAce object.



Get: AceFlags(self: GenericAce) -> AceFlags



Set: AceFlags(self: GenericAce)=value

"""

 AceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of this Access Control Entry (ACE).



Get: AceType(self: GenericAce) -> AceType



"""

 AuditFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the audit information associated with this Access Control Entry (ACE).



Get: AuditFlags(self: GenericAce) -> AuditFlags



"""

 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.GenericAce object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAce.GetBinaryForm method.



Get: BinaryLength(self: GenericAce) -> int



"""

 InheritanceFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets flags that specify the inheritance properties of this Access Control Entry (ACE).



Get: InheritanceFlags(self: GenericAce) -> InheritanceFlags



"""

 IsInherited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether this Access Control Entry (ACE) is inherited or is set explicitly.



Get: IsInherited(self: GenericAce) -> bool



"""

 PropagationFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets flags that specify the inheritance propagation properties of this Access Control Entry (ACE).



Get: PropagationFlags(self: GenericAce) -> PropagationFlags



"""


