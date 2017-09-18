class TextObject(AnnotationObjectBase):
 """
 Represents a text object in a document.

    This is a wrapper for CRhinoAnnotationText.
 """
 TextGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text entity geometry of this text object.



Get: TextGeometry(self: TextObject) -> TextEntity



"""


