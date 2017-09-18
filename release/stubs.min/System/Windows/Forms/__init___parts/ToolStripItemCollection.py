class ToolStripItemCollection(ArrangedElementCollection,IList,ICollection,IEnumerable):
 """
 Represents a collection of System.Windows.Forms.ToolStripItem objects.

 

 ToolStripItemCollection(owner: ToolStrip,value: Array[ToolStripItem])
 """
 def Add(self,*__args):
  """
  Add(self: ToolStripItemCollection,text: str,image: Image,onClick: EventHandler) -> ToolStripItem

  

   Adds a System.Windows.Forms.ToolStripItem that displays the specified image and text to the 

    collection and that raises the System.Windows.Forms.ToolStripItem.Click event.

  

  

   text: The text to be displayed on the System.Windows.Forms.ToolStripItem.

   image: The System.Drawing.Image to be displayed on the System.Windows.Forms.ToolStripItem.

   onClick: Raises the System.Windows.Forms.ToolStripItem.Click event.

   Returns: The new System.Windows.Forms.ToolStripItem.

  Add(self: ToolStripItemCollection,value: ToolStripItem) -> int

  

   Adds the specified item to the end of the collection.

  

   value: The System.Windows.Forms.ToolStripItem to add to the end of the collection.

   Returns: An System.Int32 representing the zero-based index of the new item in the collection.

  Add(self: ToolStripItemCollection,text: str,image: Image) -> ToolStripItem

  

   Adds a System.Windows.Forms.ToolStripItem that displays the specified image and text to the 

    collection.

  

  

   text: The text to be displayed on the System.Windows.Forms.ToolStripItem.

   image: The System.Drawing.Image to be displayed on the System.Windows.Forms.ToolStripItem.

   Returns: The new System.Windows.Forms.ToolStripItem.

  Add(self: ToolStripItemCollection,text: str) -> ToolStripItem

  

   Adds a System.Windows.Forms.ToolStripItem that displays the specified text to the collection.

  

   text: The text to be displayed on the System.Windows.Forms.ToolStripItem.

   Returns: The new System.Windows.Forms.ToolStripItem.

  Add(self: ToolStripItemCollection,image: Image) -> ToolStripItem

  

   Adds a System.Windows.Forms.ToolStripItem that displays the specified image to the collection.

  

   image: The System.Drawing.Image to be displayed on the System.Windows.Forms.ToolStripItem.

   Returns: The new System.Windows.Forms.ToolStripItem.
  """
  pass
 def AddRange(self,toolStripItems):
  """
  AddRange(self: ToolStripItemCollection,toolStripItems: ToolStripItemCollection)

   Adds a System.Windows.Forms.ToolStripItemCollection to the current collection.

  

   toolStripItems: The System.Windows.Forms.ToolStripItemCollection to be added to the current collection.

  AddRange(self: ToolStripItemCollection,toolStripItems: Array[ToolStripItem])

   Adds an array of System.Windows.Forms.ToolStripItem controls to the collection.

  

   toolStripItems: An array of System.Windows.Forms.ToolStripItem controls.
  """
  pass
 def Clear(self):
  """
  Clear(self: ToolStripItemCollection)

   Removes all items from the collection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: ToolStripItemCollection,value: ToolStripItem) -> bool

  

   Determines whether the specified item is a member of the collection.

  

   value: The System.Windows.Forms.ToolStripItem to search for in the 

    System.Windows.Forms.ToolStripItemCollection.

  

   Returns: true if the System.Windows.Forms.ToolStripItem is a member of the current 

    System.Windows.Forms.ToolStripItemCollection; otherwise,false.
  """
  pass
 def ContainsKey(self,key):
  """
  ContainsKey(self: ToolStripItemCollection,key: str) -> bool

  

   Determines whether the collection contains an item with the specified key.

  

   key: The key to locate in the System.Windows.Forms.ToolStripItemCollection.

   Returns: true if the System.Windows.Forms.ToolStripItemCollection contains a 

    System.Windows.Forms.ToolStripItem with the specified key; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ToolStripItemCollection,array: Array[ToolStripItem],index: int)

   Copies the collection into the specified position of the specified 

    System.Windows.Forms.ToolStripItem array.

  

  

   array: The array of type System.Windows.Forms.ToolStripItem to which to copy the collection.

   index: The position in the System.Windows.Forms.ToolStripItem array at which to paste the collection.
  """
  pass
 def Find(self,key,searchAllChildren):
  """
  Find(self: ToolStripItemCollection,key: str,searchAllChildren: bool) -> Array[ToolStripItem]

  

   Searches for items by their name and returns an array of all matching controls.

  

   key: The item name to search the System.Windows.Forms.ToolStripItemCollection for.

   searchAllChildren: true to search child items of the System.Windows.Forms.ToolStripItem specified by the key 

    parameter; otherwise,false.

  

   Returns: A System.Windows.Forms.ToolStripItem array of the search results.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: ToolStripItemCollection,value: ToolStripItem) -> int

  

   Retrieves the index of the specified item in the collection.

  

   value: The System.Windows.Forms.ToolStripItem to locate in the 

    System.Windows.Forms.ToolStripItemCollection.

  

   Returns: A zero-based index value that represents the position of the specified 

    System.Windows.Forms.ToolStripItem in the System.Windows.Forms.ToolStripItemCollection,if 

    found; otherwise,-1.
  """
  pass
 def IndexOfKey(self,key):
  """
  IndexOfKey(self: ToolStripItemCollection,key: str) -> int

  

   Retrieves the index of the first occurrence of the specified item within the collection.

  

   key: The name of the System.Windows.Forms.ToolStripItem to search for.

   Returns: A zero-based index value that represents the position of the first occurrence of the 

    System.Windows.Forms.ToolStripItem specified by the key parameter,if found; otherwise,-1.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: ToolStripItemCollection,index: int,value: ToolStripItem)

   Inserts the specified item into the collection at the specified index.

  

   index: The location in the System.Windows.Forms.ToolStripItemCollection at which to insert the 

    System.Windows.Forms.ToolStripItem.

  

   value: The System.Windows.Forms.ToolStripItem to insert.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: ToolStripItemCollection,value: ToolStripItem)

   Removes the specified item from the collection.

  

   value: The System.Windows.Forms.ToolStripItem to remove from the 

    System.Windows.Forms.ToolStripItemCollection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: ToolStripItemCollection,index: int)

   Removes an item from the specified index in the collection.

  

   index: The index value of the System.Windows.Forms.ToolStripItem to remove.
  """
  pass
 def RemoveByKey(self,key):
  """
  RemoveByKey(self: ToolStripItemCollection,key: str)

   Removes the item that has the specified key.

  

   key: The key of the System.Windows.Forms.ToolStripItem to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,owner,value):
  """ __new__(cls: type,owner: ToolStrip,value: Array[ToolStripItem]) """
  pass
 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.ToolStripItemCollection is read-only.



Get: IsReadOnly(self: ToolStripItemCollection) -> bool



"""


