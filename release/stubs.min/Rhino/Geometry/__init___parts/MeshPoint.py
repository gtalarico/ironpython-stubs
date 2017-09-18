class MeshPoint(object):
 """ Represents a point that is found on a mesh. """
 def GetTriangle(self,a,b,c):
  """
  GetTriangle(self: MeshPoint) -> (bool,int,int,int)

  

   Gets the mesh face indices of the triangle where the

     intersection is on the face 

    takes into consideration

     the way the quad was split during the intersection.
  """
  pass
 ComponentIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the component index of the intersecting element in the mesh.



Get: ComponentIndex(self: MeshPoint) -> ComponentIndex



"""

 EdgeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When set,EdgeIndex is an index of an edge in the mesh's edge list.



Get: EdgeIndex(self: MeshPoint) -> int



"""

 EdgeParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Edge parameter when found.



Get: EdgeParameter(self: MeshPoint) -> float



"""

 FaceIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """FaceIndex is an index of a face in mesh.Faces.

   When ComponentIndex refers to a vertex,any face that uses the vertex

   may appear as FaceIndex.  When ComponenctIndex refers to an Edge or

   EdgeIndex is set,then any face that uses that edge may appear as FaceIndex.



Get: FaceIndex(self: MeshPoint) -> int



"""

 Mesh=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The mesh that is ralated to this point.



Get: Mesh(self: MeshPoint) -> Mesh



"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location (position) of this point.



Get: Point(self: MeshPoint) -> Point3d



"""

 T=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Barycentric quad coordinates for the point on the mesh

   face mesh.Faces[FaceIndex].  If the face is a triangle

   disregard T[3] (it should be set to 0.0). If the face is

   a quad and is split between vertexes 0 and 2,then T[3]

   will be 0.0 when point is on the triangle defined by vi[0],

   vi[1],vi[2] and T[1] will be 0.0 when point is on the

   triangle defined by vi[0],vi[2],vi[3]. If the face is a

   quad and is split between vertexes 1 and 3,then T[2] will

   be -1 when point is on the triangle defined by vi[0],

   vi[1],vi[3] and m_t[0] will be -1 when point is on the

   triangle defined by vi[1],vi[2],vi[3].



Get: T(self: MeshPoint) -> Array[float]



"""

 Triangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Face triangle where the intersection takes place:

   0 is unsetA is 0,1,2B is 0,2,3C is 0,1,3D is 1,2,3



Get: Triangle(self: MeshPoint) -> Char



"""


