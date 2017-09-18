class SlabShapeVertex(object):
 """ A vertex used in Slab Shape Editing. """
 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position of the vertex.



Get: Position(self: SlabShapeVertex) -> XYZ



"""

 VertexType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the vertex.



Get: VertexType(self: SlabShapeVertex) -> SlabShapeVertexType



"""


