class TreeViewHitTestInfo(object):
 """
 Contains information about an area of a System.Windows.Forms.TreeView control or a System.Windows.Forms.TreeNode.

 

 TreeViewHitTestInfo(hitNode: TreeNode,hitLocation: TreeViewHitTestLocations)
 """
 @staticmethod
 def __new__(self,hitNode,hitLocation):
  """ __new__(cls: type,hitNode: TreeNode,hitLocation: TreeViewHitTestLocations) """
  pass
 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of a hit test on a System.Windows.Forms.TreeView control,in relation to the System.Windows.Forms.TreeView and the nodes it contains.



Get: Location(self: TreeViewHitTestInfo) -> TreeViewHitTestLocations



"""

 Node=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.TreeNode at the position indicated by a hit test of a System.Windows.Forms.TreeView control.



Get: Node(self: TreeViewHitTestInfo) -> TreeNode



"""


