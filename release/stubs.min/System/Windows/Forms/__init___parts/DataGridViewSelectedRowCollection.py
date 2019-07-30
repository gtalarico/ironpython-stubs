class DataGridViewSelectedRowCollection(BaseCollection,ICollection,IEnumerable,IList):
 """ Represents a collection of System.Windows.Forms.DataGridViewRow objects that are selected in a System.Windows.Forms.DataGridView. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewSelectedRowCollection()

 def Clear(self):
  """
  Clear(self: DataGridViewSelectedRowCollection)
   Clears the collection.
  """
  pass
 def Contains(self,dataGridViewRow):
  """
  Contains(self: DataGridViewSelectedRowCollection,dataGridViewRow: DataGridViewRow) -> bool
  
   Determines whether the specified row is contained in the collection.
  
   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to locate in the System.Windows.Forms.DataGridViewSelectedRowCollection.
   Returns: true if dataGridViewRow is in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,*__args):
  """
  CopyTo(self: DataGridViewSelectedRowCollection,array: Array[DataGridViewRow],index: int)
   Copies the elements of the collection to the specified array,starting at the specified index.
  
   array: The one-dimensional array that is the destination of the elements copied from the collection. The array must have zero-based indexing.
   index: The zero-based index in the array at which copying begins.
  """
  pass
 def Insert(self,index,dataGridViewRow):
  """
  Insert(self: DataGridViewSelectedRowCollection,index: int,dataGridViewRow: DataGridViewRow)
   Inserts a row into the collection at the specified position.
  
   index: The zero-based index at which dataGridViewRow should be inserted.
   dataGridViewRow: The System.Windows.Forms.DataGridViewRow to insert into the System.Windows.Forms.DataGridViewSelectedRowCollection.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls to be routed to the remote server object.
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
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
 List=property(lambda self: object(),lambda self,v: None,lambda self: None)


