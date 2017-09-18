class BindingContext(object,ICollection,IEnumerable):
 """
 Manages the collection of System.Windows.Forms.BindingManagerBase objects for any object that inherits from the System.Windows.Forms.Control class.

 

 BindingContext()
 """
 def Add(self,*args):
  """
  Add(self: BindingContext,dataSource: object,listManager: BindingManagerBase)

   Adds the System.Windows.Forms.BindingManagerBase associated with a specific data source to the 

    collection.

  

  

   dataSource: The System.Object associated with the System.Windows.Forms.BindingManagerBase.

   listManager: The System.Windows.Forms.BindingManagerBase to add.
  """
  pass
 def AddCore(self,*args):
  """
  AddCore(self: BindingContext,dataSource: object,listManager: BindingManagerBase)

   Adds the System.Windows.Forms.BindingManagerBase associated with a specific data source to the 

    collection.

  

  

   dataSource: The object associated with the System.Windows.Forms.BindingManagerBase.

   listManager: The System.Windows.Forms.BindingManagerBase to add.
  """
  pass
 def Clear(self,*args):
  """
  Clear(self: BindingContext)

   Clears the collection of any System.Windows.Forms.BindingManagerBase objects.
  """
  pass
 def ClearCore(self,*args):
  """
  ClearCore(self: BindingContext)

   Clears the collection.
  """
  pass
 def Contains(self,dataSource,dataMember=None):
  """
  Contains(self: BindingContext,dataSource: object,dataMember: str) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.BindingContext contains the 

    System.Windows.Forms.BindingManagerBase associated with the specified data source and data 

    member.

  

  

   dataSource: An System.Object that represents the data source.

   dataMember: The information needed to resolve to a specific System.Windows.Forms.BindingManagerBase.

   Returns: true if the System.Windows.Forms.BindingContext contains the specified 

    System.Windows.Forms.BindingManagerBase; otherwise,false.

  

  Contains(self: BindingContext,dataSource: object) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.BindingContext contains the 

    System.Windows.Forms.BindingManagerBase associated with the specified data source.

  

  

   dataSource: An System.Object that represents the data source.

   Returns: true if the System.Windows.Forms.BindingContext contains the specified 

    System.Windows.Forms.BindingManagerBase; otherwise,false.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: BindingContext,ccevent: CollectionChangeEventArgs)

   Raises the System.Windows.Forms.BindingContext.CollectionChanged event.

  

   ccevent: A System.ComponentModel.CollectionChangeEventArgs that contains the event data.
  """
  pass
 def Remove(self,*args):
  """
  Remove(self: BindingContext,dataSource: object)

   Deletes the System.Windows.Forms.BindingManagerBase associated with the specified data source.

  

   dataSource: The data source associated with the System.Windows.Forms.BindingManagerBase to remove.
  """
  pass
 def RemoveCore(self,*args):
  """
  RemoveCore(self: BindingContext,dataSource: object)

   Removes the System.Windows.Forms.BindingManagerBase associated with the specified data source.

  

   dataSource: The data source associated with the System.Windows.Forms.BindingManagerBase to remove.
  """
  pass
 @staticmethod
 def UpdateBinding(newBindingContext,binding):
  """
  UpdateBinding(newBindingContext: BindingContext,binding: Binding)

   Associates a System.Windows.Forms.Binding with a new System.Windows.Forms.BindingContext.

  

   newBindingContext: The new System.Windows.Forms.BindingContext to associate with the System.Windows.Forms.Binding.

   binding: The System.Windows.Forms.Binding to associate with the new System.Windows.Forms.BindingContext.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the collection is read-only.



Get: IsReadOnly(self: BindingContext) -> bool



"""


 CollectionChanged=None

