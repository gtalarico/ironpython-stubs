class TreeNodeMouseClickEventArgs(MouseEventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.NodeMouseClick and System.Windows.Forms.TreeView.NodeMouseDoubleClick events.

 

 TreeNodeMouseClickEventArgs(node: TreeNode,button: MouseButtons,clicks: int,x: int,y: int)
 """
 @staticmethod
 def __new__(self,node,button,clicks,x,y):
  """ __new__(cls: type,node: TreeNode,button: MouseButtons,clicks: int,x: int,y: int) """
  pass
 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the node that was clicked.



Get: Node(self: TreeNodeMouseClickEventArgs) -> TreeNode



"""


