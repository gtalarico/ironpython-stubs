class BindingsCollection(BaseCollection,ICollection,IEnumerable):
 """ Represents a collection of System.Windows.Forms.Binding objects for a control. """
 def Add(self,*args):
  """
  Add(self: BindingsCollection,binding: Binding)

   Adds the specified binding to the collection.

  

   binding: The System.Windows.Forms.Binding to add to the collection.
  """
  pass
 def AddCore(self,*args):
  """
  AddCore(self: BindingsCollection,dataBinding: Binding)

   Adds a System.Windows.Forms.Binding to the collection.

  

   dataBinding: The System.Windows.Forms.Binding to add to the collection.
  """
  pass
 def Clear(self,*args):
  """
  Clear(self: BindingsCollection)

   Clears the collection of binding objects.
  """
  pass
 def ClearCore(self,*args):
  """
  ClearCore(self: BindingsCollection)

   Clears the collection of any members.
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
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: BindingsCollection,ccevent: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.BindingsCollection.CollectionChanged event.

  

   ccevent: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def OnCollectionChanging(self,*args):
  """
  OnCollectionChanging(self: BindingsCollection,e: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.BindingsCollection.CollectionChanging event.

  

   e: A System.ComponentModel.CollectionChangeEventArgs that contains event data.
  """
  pass
 def Remove(self,*args):
  """
  Remove(self: BindingsCollection,binding: Binding)

   Deletes the specified binding from the collection.

  

   binding: The Binding to remove from the collection.
  """
  pass
 def RemoveAt(self,*args):
  """
  RemoveAt(self: BindingsCollection,index: int)

   Deletes the binding from the collection at the specified index.

  

   index: The index of the System.Windows.Forms.Binding to remove.
  """
  pass
 def RemoveCore(self,*args):
  """
  RemoveCore(self: BindingsCollection,dataBinding: Binding)

   Removes the specified System.Windows.Forms.Binding from the collection.

  

   dataBinding: The System.Windows.Forms.Binding to remove.
  """
  pass
 def ShouldSerializeMyAll(self,*args):
  """
  ShouldSerializeMyAll(self: BindingsCollection) -> bool

  

   Gets a value that indicates whether the collection should be serialized.

   Returns: true if the collection count is greater than zero; otherwise,false.
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
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of bindings in the collection.



Get: Count(self: BindingsCollection) -> int



"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bindings in the collection as an object.



"""


 CollectionChanged=None
 CollectionChanging=None

