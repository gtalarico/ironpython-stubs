class GenericForm(CombinableElement,IDisposable):
 """ Provides access to the Generic Form model in Autodesk Revit. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetVisibility(self):
  """
  GetVisibility(self: GenericForm) -> FamilyElementVisibility

  

   Gets the visibility for the generic form.

   Returns: A copy of visibility settings for the generic form.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetVisibility(self,visibility):
  """
  SetVisibility(self: GenericForm,visibility: FamilyElementVisibility)

   Sets the visibility for the generic form.
  """
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
 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the GenericForm is a solid or a void element.



Get: IsSolid(self: GenericForm) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get and Set the Name property



Set: Name(self: GenericForm)=value

"""

 Subcategory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The subcategory.



Get: Subcategory(self: GenericForm) -> Category



Set: Subcategory(self: GenericForm)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The visibility of the GenericForm.



Get: Visible(self: GenericForm) -> bool



"""


