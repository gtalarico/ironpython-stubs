class RebarShapeParameters(object,IDisposable):
 """ Class containing functions that create and retrieve shared parameters for RebarShapes. """
 def Dispose(self):
  """ Dispose(self: RebarShapeParameters) """
  pass
 @staticmethod
 def GetAllRebarShapeParameters(doc):
  """
  GetAllRebarShapeParameters(doc: Document) -> IList[ElementId]
  
   List all shape parameters used by all the existing RebarShapes in the specified 
    document.
  
  
   doc: The document.
   Returns: ElementIds corresponding to the external parameters.
  """
  pass
 @staticmethod
 def GetElementIdForExternalDefinition(doc,externalDefinition):
  """
  GetElementIdForExternalDefinition(doc: Document,externalDefinition: ExternalDefinition) -> ElementId
  
   Retrieve the ElementId corresponding to an external rebar shape parameter
     
    in the document,if it exists; otherwise,return InvalidElementId.
  
  
   doc: A document.
   externalDefinition: A shared parameter.
   Returns: An ElementId representing the shared parameter stored in the document,
     or 
    InvalidElementId if the parameter is not stored in the document.
  """
  pass
 @staticmethod
 def GetExternalDefinitionForElementId(doc,paramId,definitionFile):
  """
  GetExternalDefinitionForElementId(doc: Document,paramId: ElementId,definitionFile: DefinitionFile) -> ExternalDefinition
  
   Seach a DefinitionFile for the ExternalDefinition corresponding to a parameter
  
    in a document.
  
  
   doc: A document.
   paramId: The id of a shared parameter in the document.
   definitionFile: A database of shared parameters.
   Returns: The external parameter corresponding to the parameter's ElementId,
     or null 
    if the Id does not correspond to an external parameter,
     or the parameter is 
    not in the definition file.
  """
  pass
 @staticmethod
 def GetOrCreateElementIdForExternalDefinition(doc,externalDefinition):
  """
  GetOrCreateElementIdForExternalDefinition(doc: Document,externalDefinition: ExternalDefinition) -> ElementId
  
   Retrieve the ElementId corresponding to an external rebar shape parameter
     
    in the document,if it exists; otherwise,add the parameter to the document
     
    and generate a new ElementId.
  
  
   doc: A document.
   externalDefinition: A shared parameter.
   Returns: An ElementId representing the shared parameter stored in the document.
  """
  pass
 @staticmethod
 def IsValidExternalDefinition(param):
  """
  IsValidExternalDefinition(param: ExternalDefinition) -> bool
  
   Checks that an ExternalDefinition (shared parameter) may be used as a Rebar 
    Shape parameter.
  
  
   param: Definition of a shared parameter.
   Returns: True if the definition is of type Length,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarShapeParameters,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeParameters) -> bool

"""


