class DrawTreeNodeEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.DrawNode event.

 

 DrawTreeNodeEventArgs(graphics: Graphics,node: TreeNode,bounds: Rectangle,state: TreeNodeStates)
 """
 @staticmethod
 def __new__(self,graphics,node,bounds,state):
  """ __new__(cls: type,graphics: Graphics,node: TreeNode,bounds: Rectangle,state: TreeNodeStates) """
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the System.Windows.Forms.TreeNode to draw.



Get: Bounds(self: DrawTreeNodeEventArgs) -> Rectangle



"""

 DrawDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.TreeNode should be drawn by the operating system rather than being owner drawn.



Get: DrawDefault(self: DrawTreeNodeEventArgs) -> bool



Set: DrawDefault(self: DrawTreeNodeEventArgs)=value

"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics object used to draw the System.Windows.Forms.TreeNode.



Get: Graphics(self: DrawTreeNodeEventArgs) -> Graphics



"""

 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.TreeNode to draw.



Get: Node(self: DrawTreeNodeEventArgs) -> TreeNode



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the System.Windows.Forms.TreeNode to draw.



Get: State(self: DrawTreeNodeEventArgs) -> TreeNodeStates



"""


