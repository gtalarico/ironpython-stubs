class CommonAcl(GenericAcl,ICollection,IEnumerable):
 """ Represents an access control list (ACL) and is the base class for the System.Security.AccessControl.DiscretionaryAcl and System.Security.AccessControl.SystemAcl classes. """
 def GetBinaryForm(self,binaryForm,offset):
  """
  GetBinaryForm(self: CommonAcl,binaryForm: Array[Byte],offset: int)

   Marshals the contents of the System.Security.AccessControl.CommonAcl object into the specified 

    byte array beginning at the specified offset.

  

  

   binaryForm: The byte array into which the contents of the System.Security.AccessControl.CommonAcl is 

    marshaled.

  

   offset: The offset at which to start marshaling.
  """
  pass
 def Purge(self,sid):
  """
  Purge(self: CommonAcl,sid: SecurityIdentifier)

   Removes all access control entries (ACEs) contained by this 

    System.Security.AccessControl.CommonAcl object that are associated with the specified 

    System.Security.Principal.SecurityIdentifier object.

  

  

   sid: The System.Security.Principal.SecurityIdentifier object to check for.
  """
  pass
 def RemoveInheritedAces(self):
  """
  RemoveInheritedAces(self: CommonAcl)

   Removes all inherited access control entries (ACEs) from this 

    System.Security.AccessControl.CommonAcl object.
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 BinaryLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length,in bytes,of the binary representation of the current System.Security.AccessControl.CommonAcl object. This length should be used before marshaling the access control list (ACL) into a binary array by using the System.Security.AccessControl.CommonAcl.GetBinaryForm method.



Get: BinaryLength(self: CommonAcl) -> int



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object.



Get: Count(self: CommonAcl) -> int



"""

 IsCanonical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether the access control entries (ACEs) in the current System.Security.AccessControl.CommonAcl object are in canonical order.



Get: IsCanonical(self: CommonAcl) -> bool



"""

 IsContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets whether the System.Security.AccessControl.CommonAcl object is a container.



Get: IsContainer(self: CommonAcl) -> bool



"""

 IsDS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sets whether the current System.Security.AccessControl.CommonAcl object is a directory object access control list (ACL).



Get: IsDS(self: CommonAcl) -> bool



"""

 Revision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the revision level of the System.Security.AccessControl.CommonAcl.



Get: Revision(self: CommonAcl) -> Byte



"""


