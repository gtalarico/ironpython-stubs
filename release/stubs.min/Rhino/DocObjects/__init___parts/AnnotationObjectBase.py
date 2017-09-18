class AnnotationObjectBase(RhinoObject):
 """
 Provides a base class for Rhino.Geometry.AnnotationBase-derived

    objects that are placed in a document.
 """
 DisplayText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text that is displayed to users.



Get: DisplayText(self: AnnotationObjectBase) -> str



"""


