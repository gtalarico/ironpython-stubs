class TreeViewCancelEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.TreeView.BeforeCheck,System.Windows.Forms.TreeView.BeforeCollapse,System.Windows.Forms.TreeView.BeforeExpand,and System.Windows.Forms.TreeView.BeforeSelect events of a System.Windows.Forms.TreeView control.

 

 TreeViewCancelEventArgs(node: TreeNode,cancel: bool,action: TreeViewAction)
 """
 @staticmethod
 def __new__(self,node,cancel,action):
  """ __new__(cls: type,node: TreeNode,cancel: bool,action: TreeViewAction) """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of System.Windows.Forms.TreeView action that raised the event.



Get: Action(self: TreeViewCancelEventArgs) -> TreeViewAction



"""

 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the tree node to be checked,expanded,collapsed,or selected.



Get: Node(self: TreeViewCancelEventArgs) -> TreeNode



"""


