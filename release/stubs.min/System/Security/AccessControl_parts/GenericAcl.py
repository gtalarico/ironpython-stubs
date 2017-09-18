class GenericAcl(object,ICollection,IEnumerable):
 """ Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.CommonAcl,System.Security.AccessControl.DiscretionaryAcl,System.Security.AccessControl.RawAcl,and System.Security.AccessControl.SystemAcl classes. """
 def CopyTo(self,array,index):
  """
  CopyTo(self: GenericAcl,array: Array[GenericAce],index: int)

   Copies each System.Security.AccessControl.GenericAce of the current 

    System.Security.AccessControl.GenericAcl into the specified array.

  

  

   array: The array into which copies of the System.Security.AccessControl.GenericAce objects contained by 

    the current System.Security.AccessControl.GenericAcl are placed.

  

   index: The zero-based index of array where the copying begins.
  """
  pass
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: GenericAcl,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.GenericAcl object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.GenericAcl is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GenericAcl) -> AceEnumerator

  

   Returns a new instance of the System.Security.AccessControl.AceEnumerator class.

   Returns: The Security.AccessControl.AceEnumerator that this method returns.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.GenericAcl object. This length should be used before marshaling the ACL into a binary array with the System.Security.AccessControl.GenericAcl.GetBinaryForm method.



Get: BinaryLength(self: GenericAcl) -> int



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.GenericAcl object.



Get: Count(self: GenericAcl) -> int



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is always set to false. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.



Get: IsSynchronized(self: GenericAcl) -> bool



"""

 Revision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the revision level of the System.Security.AccessControl.GenericAcl.



Get: Revision(self: GenericAcl) -> Byte



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property always returns null. It is implemented only because it is required for the implementation of the System.Collections.ICollection interface.



Get: SyncRoot(self: GenericAcl) -> object



"""


 AclRevision=None
 AclRevisionDS=None
 MaxBinaryLength=65535

