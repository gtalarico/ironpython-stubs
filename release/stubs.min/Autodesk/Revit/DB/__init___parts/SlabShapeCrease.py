class SlabShapeCrease(object):
 """ A crease used in Slab Shape Editing. """
 CreaseType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the crease.



Get: CreaseType(self: SlabShapeCrease) -> SlabShapeCreaseType



"""

 Curve=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The geometry of the crease.



Get: Curve(self: SlabShapeCrease) -> Curve



"""

 EndPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vertices of the crease.



Get: EndPoints(self: SlabShapeCrease) -> SlabShapeVertexArray



"""


