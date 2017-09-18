class TreeNode(MarshalByRefObject,ICloneable,ISerializable):
 """
 Represents a node of a System.Windows.Forms.TreeView.

 

 TreeNode()

 TreeNode(text: str)

 TreeNode(text: str,children: Array[TreeNode])

 TreeNode(text: str,imageIndex: int,selectedImageIndex: int)

 TreeNode(text: str,imageIndex: int,selectedImageIndex: int,children: Array[TreeNode])
 """
 def BeginEdit(self):
  """
  BeginEdit(self: TreeNode)

   Initiates the editing of the tree node label.
  """
  pass
 def Clone(self):
  """
  Clone(self: TreeNode) -> object

  

   Copies the tree node and the entire subtree rooted at this tree node.

   Returns: The System.Object that represents the cloned System.Windows.Forms.TreeNode.
  """
  pass
 def Collapse(self,ignoreChildren=None):
  """
  Collapse(self: TreeNode)

   Collapses the tree node.

  Collapse(self: TreeNode,ignoreChildren: bool)

   Collapses the System.Windows.Forms.TreeNode and optionally collapses its children.

  

   ignoreChildren: true to leave the child nodes in their current state; false to collapse the child nodes.
  """
  pass
 def Deserialize(self,*args):
  """
  Deserialize(self: TreeNode,serializationInfo: SerializationInfo,context: StreamingContext)

   Loads the state of the System.Windows.Forms.TreeNode from the specified 

    System.Runtime.Serialization.SerializationInfo.

  

  

   serializationInfo: The System.Runtime.Serialization.SerializationInfo that describes the 

    System.Windows.Forms.TreeNode.

  

   context: The System.Runtime.Serialization.StreamingContext that indicates the state of the stream during 

    deserialization.
  """
  pass
 def EndEdit(self,cancel):
  """
  EndEdit(self: TreeNode,cancel: bool)

   Ends the editing of the tree node label.

  

   cancel: true if the editing of the tree node label text was canceled without being saved; otherwise,

    false.
  """
  pass
 def EnsureVisible(self):
  """
  EnsureVisible(self: TreeNode)

   Ensures that the tree node is visible,expanding tree nodes and scrolling the tree view control 

    as necessary.
  """
  pass
 def Expand(self):
  """
  Expand(self: TreeNode)

   Expands the tree node.
  """
  pass
 def ExpandAll(self):
  """
  ExpandAll(self: TreeNode)

   Expands all the child tree nodes.
  """
  pass
 @staticmethod
 def FromHandle(tree,handle):
  """
  FromHandle(tree: TreeView,handle: IntPtr) -> TreeNode

  

   Returns the tree node with the specified handle and assigned to the specified tree view control.

  

   tree: The System.Windows.Forms.TreeView that contains the tree node.

   handle: The handle of the tree node.

   Returns: A System.Windows.Forms.TreeNode that represents the tree node assigned to the specified 

    System.Windows.Forms.TreeView control with the specified handle.
  """
  pass
 def GetNodeCount(self,includeSubTrees):
  """
  GetNodeCount(self: TreeNode,includeSubTrees: bool) -> int

  

   Returns the number of child tree nodes.

  

   includeSubTrees: true if the resulting count includes all tree nodes indirectly rooted at this tree node; 

    otherwise,false.

  

   Returns: The number of child tree nodes assigned to the System.Windows.Forms.TreeNode.Nodes collection.
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
 def Remove(self):
  """
  Remove(self: TreeNode)

   Removes the current tree node from the tree view control.
  """
  pass
 def Serialize(self,*args):
  """
  Serialize(self: TreeNode,si: SerializationInfo,context: StreamingContext)

   Saves the state of the System.Windows.Forms.TreeNode to the specified 

    System.Runtime.Serialization.SerializationInfo.

  

  

   si: The System.Runtime.Serialization.SerializationInfo that describes the 

    System.Windows.Forms.TreeNode.

  

   context: The System.Runtime.Serialization.StreamingContext that indicates the state of the stream during 

    serialization
  """
  pass
 def Toggle(self):
  """
  Toggle(self: TreeNode)

   Toggles the tree node to either the expanded or collapsed state.
  """
  pass
 def ToString(self):
  """
  ToString(self: TreeNode) -> str

   Returns: A string that represents the current object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,text=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,text: str)

  __new__(cls: type,text: str,children: Array[TreeNode])

  __new__(cls: type,text: str,imageIndex: int,selectedImageIndex: int)

  __new__(cls: type,text: str,imageIndex: int,selectedImageIndex: int,children: Array[TreeNode])

  __new__(cls: type,serializationInfo: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the tree node.



Get: BackColor(self: TreeNode) -> Color



Set: BackColor(self: TreeNode)=value

"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the tree node.



Get: Bounds(self: TreeNode) -> Rectangle



"""

 Checked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the tree node is in a checked state.



Get: Checked(self: TreeNode) -> bool



Set: Checked(self: TreeNode)=value

"""

 ContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the shortcut menu that is associated with this tree node.



Get: ContextMenu(self: TreeNode) -> ContextMenu



Set: ContextMenu(self: TreeNode)=value

"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu associated with this tree node.



Get: ContextMenuStrip(self: TreeNode) -> ContextMenuStrip



Set: ContextMenuStrip(self: TreeNode)=value

"""

 FirstNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first child tree node in the tree node collection.



Get: FirstNode(self: TreeNode) -> TreeNode



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the tree node.



Get: ForeColor(self: TreeNode) -> Color



Set: ForeColor(self: TreeNode)=value

"""

 FullPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the path from the root tree node to the current tree node.



Get: FullPath(self: TreeNode) -> str



"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle of the tree node.



Get: Handle(self: TreeNode) -> IntPtr



"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image list index value of the image displayed when the tree node is in the unselected state.



Get: ImageIndex(self: TreeNode) -> int



Set: ImageIndex(self: TreeNode)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key for the image associated with this tree node when the node is in an unselected state.



Get: ImageKey(self: TreeNode) -> str



Set: ImageKey(self: TreeNode)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position of the tree node in the tree node collection.



Get: Index(self: TreeNode) -> int



"""

 IsEditing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the tree node is in an editable state.



Get: IsEditing(self: TreeNode) -> bool



"""

 IsExpanded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the tree node is in the expanded state.



Get: IsExpanded(self: TreeNode) -> bool



"""

 IsSelected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the tree node is in the selected state.



Get: IsSelected(self: TreeNode) -> bool



"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the tree node is visible or partially visible.



Get: IsVisible(self: TreeNode) -> bool



"""

 LastNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last child tree node.



Get: LastNode(self: TreeNode) -> TreeNode



"""

 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based depth of the tree node in the System.Windows.Forms.TreeView control.



Get: Level(self: TreeNode) -> int



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the tree node.



Get: Name(self: TreeNode) -> str



Set: Name(self: TreeNode)=value

"""

 NextNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the next sibling tree node.



Get: NextNode(self: TreeNode) -> TreeNode



"""

 NextVisibleNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the next visible tree node.



Get: NextVisibleNode(self: TreeNode) -> TreeNode



"""

 NodeFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font that is used to display the text on the tree node label.



Get: NodeFont(self: TreeNode) -> Font



Set: NodeFont(self: TreeNode)=value

"""

 Nodes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.Forms.TreeNode objects assigned to the current tree node.



Get: Nodes(self: TreeNode) -> TreeNodeCollection



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent tree node of the current tree node.



Get: Parent(self: TreeNode) -> TreeNode



"""

 PrevNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous sibling tree node.



Get: PrevNode(self: TreeNode) -> TreeNode



"""

 PrevVisibleNode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous visible tree node.



Get: PrevVisibleNode(self: TreeNode) -> TreeNode



"""

 SelectedImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image list index value of the image that is displayed when the tree node is in the selected state.



Get: SelectedImageIndex(self: TreeNode) -> int



Set: SelectedImageIndex(self: TreeNode)=value

"""

 SelectedImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key of the image displayed in the tree node when it is in a selected state.



Get: SelectedImageKey(self: TreeNode) -> str



Set: SelectedImageKey(self: TreeNode)=value

"""

 StateImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the image that is used to indicate the state of the System.Windows.Forms.TreeNode when the parent System.Windows.Forms.TreeView has its System.Windows.Forms.TreeView.CheckBoxes property set to false.



Get: StateImageIndex(self: TreeNode) -> int



Set: StateImageIndex(self: TreeNode)=value

"""

 StateImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key of the image that is used to indicate the state of the System.Windows.Forms.TreeNode when the parent System.Windows.Forms.TreeView has its System.Windows.Forms.TreeView.CheckBoxes property set to false.



Get: StateImageKey(self: TreeNode) -> str



Set: StateImageKey(self: TreeNode)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data about the tree node.



Get: Tag(self: TreeNode) -> object



Set: Tag(self: TreeNode)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text displayed in the label of the tree node.



Get: Text(self: TreeNode) -> str



Set: Text(self: TreeNode)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that appears when the mouse pointer hovers over a System.Windows.Forms.TreeNode.



Get: ToolTipText(self: TreeNode) -> str



Set: ToolTipText(self: TreeNode)=value

"""

 TreeView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent tree view that the tree node is assigned to.



Get: TreeView(self: TreeNode) -> TreeView



"""


