class RawAcl(GenericAcl,ICollection,IEnumerable):
 """
 Represents an Access Control List (ACL).

 

 RawAcl(revision: Byte,capacity: int)

 RawAcl(binaryForm: Array[Byte],offset: int)
 """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: RawAcl,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.RawAcl object into the specified byte 

    array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.RawAcl is marshaled.

   offset: The offset at which to start marshaling.
  """
  pass
 def InsertAce(self,index,ace):
  """
  InsertAce(self: RawAcl,index: int,ace: GenericAce)

   Inserts the specified Access Control Entry (ACE) at the specified index.

  

   index: The position at which to add the new ACE. Specify the value of the 

    System.Security.AccessControl.RawAcl.Count property to insert an ACE at the end of the 

    System.Security.AccessControl.RawAcl object.

  

   ace: The ACE to insert.
  """
  pass
 def RemoveAce(self,index):
  """
  RemoveAce(self: RawAcl,index: int)

   Removes the Access Control Entry (ACE) at the specified location.

  

   index: The zero-based index of the ACE to remove.
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,revision: Byte,capacity: int)

  __new__(cls: type,binaryForm: Array[Byte],offset: int)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.RawAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.RawAcl.GetBinaryForm method.



Get: BinaryLength(self: RawAcl) -> int



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.RawAcl object.



Get: Count(self: RawAcl) -> int



"""

 Revision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the revision level of the System.Security.AccessControl.RawAcl.



Get: Revision(self: RawAcl) -> Byte



"""


