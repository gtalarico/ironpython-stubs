class TreeNodeCollection(object,IList,ICollection,IEnumerable):
 """ Represents a collection of System.Windows.Forms.TreeNode objects. """
 def Add(self,*__args):
  """
  Add(self: TreeNodeCollection,key: str,text: str,imageIndex: int,selectedImageIndex: int) -> TreeNode

  

   Creates a tree node with the specified key,text,and images,and adds it to the collection.

  

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageIndex: The index of the image to display in the tree node.

   selectedImageIndex: The index of the image to be displayed in the tree node when it is in a selected state.

   Returns: The tree node that was added to the collection.

  Add(self: TreeNodeCollection,key: str,text: str,imageKey: str,selectedImageKey: str) -> TreeNode

  

   Creates a tree node with the specified key,text,and images,and adds it to the collection.

  

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageKey: The key of the image to display in the tree node.

   selectedImageKey: The key of the image to display when the node is in a selected state.

   Returns: The System.Windows.Forms.TreeNode that was added to the collection.

  Add(self: TreeNodeCollection,node: TreeNode) -> int

  

   Adds a previously created tree node to the end of the tree node collection.

  

   node: The System.Windows.Forms.TreeNode to add to the collection.

   Returns: The zero-based index value of the System.Windows.Forms.TreeNode added to the tree node 

    collection.

  

  Add(self: TreeNodeCollection,key: str,text: str,imageKey: str) -> TreeNode

  

   Creates a tree node with the specified key,text,and image,and adds it to the collection.

  

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageKey: The image to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was added to the collection.

  Add(self: TreeNodeCollection,text: str) -> TreeNode

  

   Adds a new tree node with the specified label text to the end of the current tree node 

    collection.

  

  

   text: The label text displayed by the System.Windows.Forms.TreeNode.

   Returns: A System.Windows.Forms.TreeNode that represents the tree node being added to the collection.

  Add(self: TreeNodeCollection,key: str,text: str) -> TreeNode

  

   Creates a new tree node with the specified key and text,and adds it to the collection.

  

   key: The name of the tree node.

   text: The text to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was added to the collection.

  Add(self: TreeNodeCollection,key: str,text: str,imageIndex: int) -> TreeNode

  

   Creates a tree node with the specified key,text,and image,and adds it to the collection.

  

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageIndex: The index of the image to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was added to the collection.
  """
  pass
 def AddRange(self,nodes):
  """
  AddRange(self: TreeNodeCollection,nodes: Array[TreeNode])

   Adds an array of previously created tree nodes to the collection.

  

   nodes: An array of System.Windows.Forms.TreeNode objects representing the tree nodes to add to the 

    collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: TreeNodeCollection)

   Removes all tree nodes from the collection.
  """
  pass
 def Contains(self,node):
  """
  Contains(self: TreeNodeCollection,node: TreeNode) -> bool

  

   Determines whether the specified tree node is a member of the collection.

  

   node: The System.Windows.Forms.TreeNode to locate in the collection.

   Returns: true if the System.Windows.Forms.TreeNode is a member of the collection; otherwise,false.
  """
  pass
 def ContainsKey(self,key):
  """
  ContainsKey(self: TreeNodeCollection,key: str) -> bool

  

   Determines whether the collection contains a tree node with the specified key.

  

   key: The name of the System.Windows.Forms.TreeNode to search for.

   Returns: true to indicate the collection contains a System.Windows.Forms.TreeNode with the specified key; 

    otherwise,false.
  """
  pass
 def CopyTo(self,dest,index):
  """
  CopyTo(self: TreeNodeCollection,dest: Array,index: int)

   Copies the entire collection into an existing array at a specified location within the array.

  

   dest: The destination array.

   index: The index in the destination array at which storing begins.
  """
  pass
 def Find(self,key,searchAllChildren):
  """
  Find(self: TreeNodeCollection,key: str,searchAllChildren: bool) -> Array[TreeNode]

  

   Finds the tree nodes with specified key,optionally searching subnodes.

  

   key: The name of the tree node to search for.

   searchAllChildren: true to search child nodes of tree nodes; otherwise,false.

   Returns: An array of System.Windows.Forms.TreeNode objects whose System.Windows.Forms.TreeNode.Name 

    property matches the specified key.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TreeNodeCollection) -> IEnumerator

  

   Returns an enumerator that can be used to iterate through the tree node collection.

   Returns: An System.Collections.IEnumerator that represents the tree node collection.
  """
  pass
 def IndexOf(self,node):
  """
  IndexOf(self: TreeNodeCollection,node: TreeNode) -> int

  

   Returns the index of the specified tree node in the collection.

  

   node: The System.Windows.Forms.TreeNode to locate in the collection.

   Returns: The zero-based index of the item found in the tree node collection; otherwise,-1.
  """
  pass
 def IndexOfKey(self,key):
  """
  IndexOfKey(self: TreeNodeCollection,key: str) -> int

  

   Returns the index of the first occurrence of a tree node with the specified key.

  

   key: The name of the tree node to search for.

   Returns: The zero-based index of the first occurrence of a tree node with the specified key,if found; 

    otherwise,-1.
  """
  pass
 def Insert(self,index,*__args):
  """
  Insert(self: TreeNodeCollection,index: int,key: str,text: str,imageKey: str) -> TreeNode

  

   Creates a tree node with the specified key,text,and image,and inserts it into the collection 

    at the specified index.

  

  

   index: The location within the collection to insert the node.

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageKey: The key of the image to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.

  Insert(self: TreeNodeCollection,index: int,key: str,text: str,imageIndex: int,selectedImageIndex: int) -> TreeNode

  

   Creates a tree node with the specified key,text,and images,and inserts it into the collection 

    at the specified index.

  

  

   index: The location within the collection to insert the node.

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageIndex: The index of the image to display in the tree node.

   selectedImageIndex: The index of the image to display in the tree node when it is in a selected state.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.

  Insert(self: TreeNodeCollection,index: int,key: str,text: str,imageKey: str,selectedImageKey: str) -> TreeNode

  

   Creates a tree node with the specified key,text,and images,and inserts it into the collection 

    at the specified index.

  

  

   index: The location within the collection to insert the node.

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageKey: The key of the image to display in the tree node.

   selectedImageKey: The key of the image to display in the tree node when it is in a selected state.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.

  Insert(self: TreeNodeCollection,index: int,key: str,text: str,imageIndex: int) -> TreeNode

  

   Creates a tree node with the specified key,text,and image,and inserts it into the collection 

    at the specified index.

  

  

   index: The location within the collection to insert the node.

   key: The name of the tree node.

   text: The text to display in the tree node.

   imageIndex: The index of the image to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.

  Insert(self: TreeNodeCollection,index: int,node: TreeNode)

   Inserts an existing tree node into the tree node collection at the specified location.

  

   index: The indexed location within the collection to insert the tree node.

   node: The System.Windows.Forms.TreeNode to insert into the collection.

  Insert(self: TreeNodeCollection,index: int,text: str) -> TreeNode

  

   Creates a tree node with the specified text and inserts it at the specified index.

  

   index: The location within the collection to insert the node.

   text: The text to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.

  Insert(self: TreeNodeCollection,index: int,key: str,text: str) -> TreeNode

  

   Creates a tree node with the specified text and key,and inserts it into the collection.

  

   index: The location within the collection to insert the node.

   key: The name of the tree node.

   text: The text to display in the tree node.

   Returns: The System.Windows.Forms.TreeNode that was inserted in the collection.
  """
  pass
 def Remove(self,node):
  """
  Remove(self: TreeNodeCollection,node: TreeNode)

   Removes the specified tree node from the tree node collection.

  

   node: The System.Windows.Forms.TreeNode to remove.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: TreeNodeCollection,index: int)

   Removes a tree node from the tree node collection at a specified index.

  

   index: The index of the System.Windows.Forms.TreeNode to remove.
  """
  pass
 def RemoveByKey(self,key):
  """
  RemoveByKey(self: TreeNodeCollection,key: str)

   Removes the tree node with the specified key from the collection.

  

   key: The name of the tree node to remove from the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of System.Windows.Forms.TreeNode objects in the collection.



Get: Count(self: TreeNodeCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the collection is read-only.



Get: IsReadOnly(self: TreeNodeCollection) -> bool



"""


