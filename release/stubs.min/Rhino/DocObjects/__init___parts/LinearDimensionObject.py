class LinearDimensionObject(AnnotationObjectBase):
 """
 Represents a Rhino.Geometry.LinearDimension

    that is placed in a document.
 """
 DimensionStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Rhino.DocObjects.DimensionStyle

   associated with this LinearDimensionObject.



Get: DimensionStyle(self: LinearDimensionObject) -> DimensionStyle



"""


