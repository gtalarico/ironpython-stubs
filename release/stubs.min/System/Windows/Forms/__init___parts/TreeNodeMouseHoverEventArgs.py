class TreeNodeMouseHoverEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.NodeMouseHover event.

 

 TreeNodeMouseHoverEventArgs(node: TreeNode)
 """
 @staticmethod
 def __new__(self,node):
  """ __new__(cls: type,node: TreeNode) """
  pass
 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the node the mouse pointer is currently resting on.



Get: Node(self: TreeNodeMouseHoverEventArgs) -> TreeNode



"""


