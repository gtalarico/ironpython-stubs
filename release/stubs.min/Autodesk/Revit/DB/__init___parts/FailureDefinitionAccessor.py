class FailureDefinitionAccessor(object,IDisposable):
 """ A class that provides access to the details of a FailureDefinition after the definition has been defined. """
 def Dispose(self):
  """ Dispose(self: FailureDefinitionAccessor) """
  pass
 def GetApplicableResolutionTypes(self):
  """
  GetApplicableResolutionTypes(self: FailureDefinitionAccessor) -> IList[FailureResolutionType]

  

   Retrieves a list of resolution types applicable to the failure.

   Returns: The list of resolution types applicable to the failure.
  """
  pass
 def GetDefaultResolutionType(self):
  """
  GetDefaultResolutionType(self: FailureDefinitionAccessor) -> FailureResolutionType

  

   Retrieves the default resolution type for the failure.

   Returns: The default resolution type for the failure.
  """
  pass
 def GetDescriptionText(self):
  """
  GetDescriptionText(self: FailureDefinitionAccessor) -> str

  

   Retrieves the description text of the failure.

   Returns: The description text.
  """
  pass
 def GetId(self):
  """
  GetId(self: FailureDefinitionAccessor) -> FailureDefinitionId

  

   Retrieves the unique identifier of the FailureDefinition.

   Returns: The unique identifier of the FailureDefinition.
  """
  pass
 def GetResolutionCaption(self,type):
  """
  GetResolutionCaption(self: FailureDefinitionAccessor,type: FailureResolutionType) -> str

  

   Retrieves the caption for a specific resolution type.

  

   type: The resolution type.

   Returns: The caption of the resolution.
  """
  pass
 def GetSeverity(self):
  """
  GetSeverity(self: FailureDefinitionAccessor) -> FailureSeverity

  

   Retrieves severity of the failure.

   Returns: The severity of the failure.
  """
  pass
 def HasResolutions(self):
  """
  HasResolutions(self: FailureDefinitionAccessor) -> bool

  

   Checks if the FailureDefinition has at least one resolution.

   Returns: True if at least one resolution is defined in the FailureDefinition.
  """
  pass
 def IsResolutionApplicable(self,type):
  """
  IsResolutionApplicable(self: FailureDefinitionAccessor,type: FailureResolutionType) -> bool

  

   Checks if the given resolution type is applicable to the failure.

  

   type: The resolution type to check.

   Returns: True if the given resolution type is applicable to the failure,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureDefinitionAccessor,disposing: bool) """
  pass
 def SetDefaultResolutionType(self,type):
  """
  SetDefaultResolutionType(self: FailureDefinitionAccessor,type: FailureResolutionType)

   Sets the default resolution type for the failure.

  

   type: The type of resolution to be used as default.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FailureDefinitionAccessor) -> bool



"""


