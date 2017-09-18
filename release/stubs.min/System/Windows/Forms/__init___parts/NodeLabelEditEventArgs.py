class NodeLabelEditEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.BeforeLabelEdit and System.Windows.Forms.TreeView.AfterLabelEdit events.

 

 NodeLabelEditEventArgs(node: TreeNode)

 NodeLabelEditEventArgs(node: TreeNode,label: str)
 """
 @staticmethod
 def __new__(self,node,label=None):
  """
  __new__(cls: type,node: TreeNode)

  __new__(cls: type,node: TreeNode,label: str)
  """
  pass
 CancelEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the edit has been canceled.



Get: CancelEdit(self: NodeLabelEditEventArgs) -> bool



Set: CancelEdit(self: NodeLabelEditEventArgs)=value

"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new text to associate with the tree node.



Get: Label(self: NodeLabelEditEventArgs) -> str



"""

 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the tree node containing the text to edit.



Get: Node(self: NodeLabelEditEventArgs) -> TreeNode



"""


