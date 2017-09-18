class MeshPart(object):
 """ Represents a portion of a mesh for partitioning """
 EndFaceIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End of subinterval of parent mesh face array



Get: EndFaceIndex(self: MeshPart) -> int



"""

 EndVertexIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End of subinterval of parent mesh vertex array



Get: EndVertexIndex(self: MeshPart) -> int



"""

 StartFaceIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Start of subinterval of parent mesh face array



Get: StartFaceIndex(self: MeshPart) -> int



"""

 StartVertexIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Start of subinterval of parent mesh vertex array



Get: StartVertexIndex(self: MeshPart) -> int



"""

 TriangleCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """



Get: TriangleCount(self: MeshPart) -> int



"""

 VertexCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EndVertexIndex - StartVertexIndex



Get: VertexCount(self: MeshPart) -> int



"""


