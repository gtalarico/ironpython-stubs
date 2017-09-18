class TreeViewEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.AfterCheck,System.Windows.Forms.TreeView.AfterCollapse,System.Windows.Forms.TreeView.AfterExpand,or System.Windows.Forms.TreeView.AfterSelect events of a System.Windows.Forms.TreeView control.

 

 TreeViewEventArgs(node: TreeNode)

 TreeViewEventArgs(node: TreeNode,action: TreeViewAction)
 """
 @staticmethod
 def __new__(self,node,action=None):
  """
  __new__(cls: type,node: TreeNode)

  __new__(cls: type,node: TreeNode,action: TreeViewAction)
  """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of action that raised the event.



Get: Action(self: TreeViewEventArgs) -> TreeViewAction



"""

 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the tree node that has been checked,expanded,collapsed,or selected.



Get: Node(self: TreeViewEventArgs) -> TreeNode



"""


