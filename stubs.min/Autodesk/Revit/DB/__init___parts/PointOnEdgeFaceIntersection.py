class PointOnEdgeFaceIntersection(PointElementReference):
 """
 Define a ReferencePoint at the intersection of a referenceable
 edge or curve and a referenceable face.
 """
 def GetEdgeReference(self):
  """
  GetEdgeReference(self: PointOnEdgeFaceIntersection) -> Reference
  
   Get a copy of the edge or curve reference.
  """
  pass
 def GetFaceReference(self):
  """
  GetFaceReference(self: PointOnEdgeFaceIntersection) -> Reference
  
   Get a copy of the face reference.
  """
  pass
 def SetEdgeReference(self,edgeReference):
  """
  SetEdgeReference(self: PointOnEdgeFaceIntersection,edgeReference: Reference)
   Change the edge or curve reference.
  """
  pass
 def SetFaceReference(self,reference):
  """
  SetFaceReference(self: PointOnEdgeFaceIntersection,reference: Reference)
   Change the face reference.
  """
  pass
 OrientWithEdge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether to orient the ReferencePoint to the edge or the face.

Get: OrientWithEdge(self: PointOnEdgeFaceIntersection) -> bool

Set: OrientWithEdge(self: PointOnEdgeFaceIntersection)=value
"""


