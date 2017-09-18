class FailureMessageAccessor(object,IDisposable):
 """ Restricted accessor for FailureMessage. """
 def CloneFailureMessage(self):
  """
  CloneFailureMessage(self: FailureMessageAccessor) -> FailureMessage

  

   Creates a copy of the FailureMessage.

   Returns: Copy of the FailureMesassge.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FailureMessageAccessor) """
  pass
 def GetAdditionalElementIds(self):
  """
  GetAdditionalElementIds(self: FailureMessageAccessor) -> ICollection[ElementId]

  

   Retrieves Ids of Elements that have not caused the failure but are related to 

    it

     Checks if the failure has resolution of a given resolution type.

  

   Returns: Ids of Elements related to the failure
  """
  pass
 def GetCurrentResolutionType(self):
  """
  GetCurrentResolutionType(self: FailureMessageAccessor) -> FailureResolutionType

  

   Retrieves the type of resolution to be used to resolve the failure.

   Returns: The type of failure resolution to be used to resolve the failure.
  """
  pass
 def GetDefaultResolutionCaption(self):
  """
  GetDefaultResolutionCaption(self: FailureMessageAccessor) -> str

  

   Retrieves the caption of default resolution of the failure.

   Returns: The caption of default resolution of the failure.
  """
  pass
 def GetDescriptionText(self):
  """
  GetDescriptionText(self: FailureMessageAccessor) -> str

  

   Retrieves the description of the failure.

   Returns: The description text.
  """
  pass
 def GetFailingElementIds(self):
  """
  GetFailingElementIds(self: FailureMessageAccessor) -> ICollection[ElementId]

  

   Retrieves Ids of Elements that have caused the failure.

   Returns: Ids of Elements that have caused the failure.
  """
  pass
 def GetFailureDefinitionId(self):
  """
  GetFailureDefinitionId(self: FailureMessageAccessor) -> FailureDefinitionId

  

   Retrieves the Id of the FailureDefinition of the failure.

   Returns: The Id of the FailureDefinition of the failure.
  """
  pass
 def GetNumberOfResolutions(self):
  """
  GetNumberOfResolutions(self: FailureMessageAccessor) -> int

  

   Retrieves number of resolutions that can be used to resolve failure.

   Returns: Number of resolutions that can be used to resolve failure
  """
  pass
 def GetSeverity(self):
  """
  GetSeverity(self: FailureMessageAccessor) -> FailureSeverity

  

   Retrieves the severity of the failure.

   Returns: The severity of the failure.
  """
  pass
 def HasResolutionOfType(self,type):
  """
  HasResolutionOfType(self: FailureMessageAccessor,type: FailureResolutionType) -> bool

  

   Checks if failure has a resolution of a given type.

  

   type: The type of resolution.

   Returns: True if failure has a resolution of a given type,false otherwise.
  """
  pass
 def HasResolutions(self):
  """
  HasResolutions(self: FailureMessageAccessor) -> bool

  

   Checks if the failure has any resolutions.

   Returns: True if the failure has any resolutions,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureMessageAccessor,disposing: bool) """
  pass
 def SetCurrentResolutionType(self,resolutionType):
  """
  SetCurrentResolutionType(self: FailureMessageAccessor,resolutionType: FailureResolutionType)

   Sets the type of a resolution to be used to resolve the failure.

  

   resolutionType: The type of failure resolution to be used to resolve the failure.
  """
  pass
 def ShouldMergeWithMessage(self,messageToMergeWith):
  """
  ShouldMergeWithMessage(self: FailureMessageAccessor,messageToMergeWith: FailureMessageAccessor) -> bool

  

   Checks if the FailureMessage should be merged with the other FailureMessage for 

    better user experience.

  

   Returns: True if messages should be merged
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



Get: IsValidObject(self: FailureMessageAccessor) -> bool



"""


