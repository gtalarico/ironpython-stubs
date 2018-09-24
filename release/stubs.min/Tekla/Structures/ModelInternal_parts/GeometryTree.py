class GeometryTree(object):
 """ GeometryTree(node: IGeometryNode) """
 def AddBranch(self,branchSource,branchRoot):
  """ AddBranch(self: GeometryTree,branchSource: GeometryTree,branchRoot: IGeometryNode) """
  pass
 def AddEdge(self,*__args):
  """ AddEdge(self: GeometryTree,fromIndex: int,toIndex: int)AddEdge(self: GeometryTree,from: IGeometryNode,to: IGeometryNode) """
  pass
 def AddNode(self,node):
  """ AddNode(self: GeometryTree,node: IGeometryNode) -> int """
  pass
 def Clone(self):
  """ Clone(self: GeometryTree) -> GeometryTree """
  pass
 def GetBranch(self,node):
  """ GetBranch(self: GeometryTree,node: IGeometryNode) -> GeometryTree """
  pass
 def GetChildren(self,node):
  """ GetChildren(self: GeometryTree,node: IGeometryNode) -> IList[IGeometryNode] """
  pass
 def GetConnection(self,node1Index,node2Index):
  """ GetConnection(self: GeometryTree,node1Index: int,node2Index: int) -> IList[LineSegment] """
  pass
 def GetGeometryTreeLeafSections(self):
  """ GetGeometryTreeLeafSections(self: GeometryTree) -> IList[GeometrySection] """
  pass
 def GetNeighborSections(self,nodeIndex):
  """ GetNeighborSections(self: GeometryTree,nodeIndex: int) -> IList[GeometrySection] """
  pass
 def GetNodeByIndex(self,index):
  """ GetNodeByIndex(self: GeometryTree,index: int) -> IGeometryNode """
  pass
 def GetNodeId(self,node):
  """ GetNodeId(self: GeometryTree,node: IGeometryNode) -> int """
  pass
 def GetParentNode(self,node):
  """ GetParentNode(self: GeometryTree,node: IGeometryNode) -> IGeometryNode """
  pass
 def IsTransitivelyConnectedTo(self,fromIndex,toIndex):
  """ IsTransitivelyConnectedTo(self: GeometryTree,fromIndex: int,toIndex: int) -> bool """
  pass
 def IsValidId(self,index):
  """ IsValidId(self: GeometryTree,index: int) -> bool """
  pass
 def IsValidLeafToRemove(self,geometrySection):
  """ IsValidLeafToRemove(self: GeometryTree,geometrySection: GeometrySection) -> bool """
  pass
 def RemoveBranch(self,branchRoot):
  """ RemoveBranch(self: GeometryTree,branchRoot: IGeometryNode) """
  pass
 def RemoveEdge(self,*__args):
  """ RemoveEdge(self: GeometryTree,fromIndex: int,toIndex: int)RemoveEdge(self: GeometryTree,from: IGeometryNode,to: IGeometryNode) """
  pass
 def Split(self,nodeIndex):
  """ Split(self: GeometryTree,nodeIndex: int) -> IList[GeometryTree] """
  pass
 @staticmethod
 def __new__(self,node):
  """ __new__(cls: type,node: IGeometryNode) """
  pass
 Edges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Edges(self: GeometryTree) -> Dictionary[int,HashSet[int]]

"""

 NodesById=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NodesById(self: GeometryTree) -> Dictionary[int,IGeometryNode]

"""

 Root=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Root(self: GeometryTree) -> IGeometryNode

Set: Root(self: GeometryTree)=value
"""


 InvalidGeometryNodeId=-1

