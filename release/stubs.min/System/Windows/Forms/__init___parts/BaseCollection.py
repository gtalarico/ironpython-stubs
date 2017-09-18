class BaseCollection(MarshalByRefObject,ICollection,IEnumerable):
 """
 Provides the base functionality for creating data-related collections in the System.Windows.Forms namespace.

 

 BaseCollection()
 """
 def CopyTo(self,ar,index):
  """
  CopyTo(self: BaseCollection,ar: Array,index: int)

   Copies all the elements of the current one-dimensional System.Array to the specified 

    one-dimensional System.Array starting at the specified destination System.Array index.

  

  

   ar: The one-dimensional System.Array that is the destination of the elements copied from the current 

    Array.

  

   index: The zero-based relative index in ar at which copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: BaseCollection) -> IEnumerator

  

   Gets the object that enables iterating through the members of the collection.

   Returns: An object that implements the System.Collections.IEnumerator interface.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
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
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of elements in the collection.



Get: Count(self: BaseCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the collection is read-only.



Get: IsReadOnly(self: BaseCollection) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether access to the System.Collections.ICollection is synchronized.



Get: IsSynchronized(self: BaseCollection) -> bool



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Windows.Forms.BaseCollection instance.



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the System.Windows.Forms.BaseCollection.



Get: SyncRoot(self: BaseCollection) -> object



"""


