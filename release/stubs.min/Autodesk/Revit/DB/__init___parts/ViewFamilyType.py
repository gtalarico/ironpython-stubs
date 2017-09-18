class ViewFamilyType(ElementType,IDisposable):
 """ Represents a type of a Revit view. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsValidDefaultTemplate(self,templateId):
  """
  IsValidDefaultTemplate(self: ViewFamilyType,templateId: ElementId) -> bool
  
   Verifies that the input can be used as a default template for this view type.
  
   templateId: Id to be validated as default template.
   Returns: True if %templateId% is valid as default template,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 DefaultTemplateId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default template id assigned to this view type.

Get: DefaultTemplateId(self: ViewFamilyType) -> ElementId

Set: DefaultTemplateId(self: ViewFamilyType)=value
"""

 PlanViewDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The PlanViewDirection of this view.

Get: PlanViewDirection(self: ViewFamilyType) -> PlanViewDirection

Set: PlanViewDirection(self: ViewFamilyType)=value
"""

 ViewFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ViewFamily for this view type.

Get: ViewFamily(self: ViewFamilyType) -> ViewFamily

"""


