class StructuralConnectionType(ElementType,IDisposable):
 """ A type element that represents a connection symbol applied to structural members. """
 @staticmethod
 def Create(doc,applyTo,name,familySymbolId):
  """
  Create(doc: Document,applyTo: StructuralConnectionApplyTo,name: str,familySymbolId: ElementId) -> StructuralConnectionType
  
   Create a new StructuralConnectionType,allowing the specified
     annotation 
    FamilySymbol to be applied to structural members.
  
  
   applyTo: Specify which type of member this connection type can be applied to.
   name: A name for the connection type. It must be unique within the document.
   familySymbolId: The id of an annotation FamilySymbol. InvalidElementId is
     allowed. 
    Otherwise,the FamilySymbol must
     be in the category "Connection Symbols"
    
     (OST_StructConnectionSymbols) and have its "Apply
     To" parameter set to 
    match the applyTo argument.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def GetAllStructuralConnectionTypeIds(cda,ids):
  """ GetAllStructuralConnectionTypeIds(cda: Document) -> ICollection[ElementId] """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFamilySymbolId(self):
  """
  GetFamilySymbolId(self: StructuralConnectionType) -> ElementId
  
   FamilySymbol of the annotation to use for this connection type.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetFamilySymbolId(self,familySymbolId):
  """
  SetFamilySymbolId(self: StructuralConnectionType,familySymbolId: ElementId)
   FamilySymbol of the annotation to use for this connection type.
  """
  pass
 @staticmethod
 def ValidFamilySymbolId(doc,applyTo,familySymbolId):
  """
  ValidFamilySymbolId(doc: Document,applyTo: StructuralConnectionApplyTo,familySymbolId: ElementId) -> bool
  
   Checks whether the family symbol id is allowed for
     
    StructuralConnectionTypes with the given value for the applyTo
     property.
  
   Returns: True if %familySymbolId% is invalidElementId; or if it is
     the id of a 
    FamilySymbol of category "Connection
     Symbols" (OST_StructConnectionSymbols) 
    with its "Apply
     To" parameter set to match the applyTo property.
     
    Returns false otherwise.
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
 ApplyTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Choose whether this connection type applies to beams and
   braces,to tops of columns,or to bases of columns.

Get: ApplyTo(self: StructuralConnectionType) -> StructuralConnectionApplyTo

"""


