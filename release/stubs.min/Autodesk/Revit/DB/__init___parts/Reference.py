class Reference(APIObject,IDisposable):
 """
 A stable reference to a geometric object in a Revit model.

 

 Reference(element: Element)
 """
 def ConvertToStableRepresentation(self,document):
  """
  ConvertToStableRepresentation(self: Reference,document: Document) -> str

  

   Converts the reference to a stable String representation.

  

   document: The document.
  """
  pass
 def CreateLinkReference(self,revitLinkInstance):
  """
  CreateLinkReference(self: Reference,revitLinkInstance: RevitLinkInstance) -> Reference

  

   Creates a Reference from a Reference in an RVT Link.

  

   revitLinkInstance: Id of the RevitLinkInstance that contains the reference.
  """
  pass
 def CreateReferenceInLink(self):
  """
  CreateReferenceInLink(self: Reference) -> Reference

  

   Creates a Reference in an RVT Link from a Reference in the RVT host file.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 @staticmethod
 def ParseFromStableRepresentation(document,representation):
  """
  ParseFromStableRepresentation(document: Document,representation: str) -> Reference

  

   Converts a stable String representation of a reference to a Reference object.

  

   document: The document.

   representation: The reference representation.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 @staticmethod
 def __new__(self,element):
  """ __new__(cls: type,element: Element) """
  pass
 ElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id for this reference.



Get: ElementId(self: Reference) -> ElementId



"""

 ElementReferenceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of reference.



Get: ElementReferenceType(self: Reference) -> ElementReferenceType



"""

 GlobalPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The position on which the reference is hit.



Get: GlobalPoint(self: Reference) -> XYZ



"""

 LinkedElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the top-level element in the linked document that is referred to by this reference.



Get: LinkedElementId(self: Reference) -> ElementId



"""

 UVPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The UV parameters of the reference,if the reference contains a face.



Get: UVPoint(self: Reference) -> UV



"""


