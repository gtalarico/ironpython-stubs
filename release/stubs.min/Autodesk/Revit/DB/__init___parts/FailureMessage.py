class FailureMessage(object,IDisposable):
 """
 Represents a message describing a failure of an operation in Revit.

 

 FailureMessage(id: FailureDefinitionId)
 """
 def AddResolution(self,type,resolution):
  """
  AddResolution(self: FailureMessage,type: FailureResolutionType,resolution: FailureResolution) -> FailureMessage

  

   Adds a resolution for the failure.

  

   type: The type of the resolution.

   resolution: The resolution.

   Returns: The FailureMessage.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FailureMessage) """
  pass
 def GetAdditionalElements(self):
  """
  GetAdditionalElements(self: FailureMessage) -> ICollection[ElementId]

  

   Retrieves list of the additional reference elements for the failure.

   Returns: The additional elements.
  """
  pass
 def GetDefaultResolutionCaption(self):
  """
  GetDefaultResolutionCaption(self: FailureMessage) -> str

  

   Retrieves the caption of the default resolution of the failure.

   Returns: The caption of the default resolution of the failure.
  """
  pass
 def GetDescriptionText(self):
  """
  GetDescriptionText(self: FailureMessage) -> str

  

   Retrieves the description text of the failure.

   Returns: The description text.
  """
  pass
 def GetFailingElements(self):
  """
  GetFailingElements(self: FailureMessage) -> ICollection[ElementId]

  

   Retrieves list of the elements that have caused the failure.

   Returns: The elements that have caused the failure.
  """
  pass
 def GetFailureDefinitionId(self):
  """
  GetFailureDefinitionId(self: FailureMessage) -> FailureDefinitionId

  

   Retrieves the id of the failure definition for the failure.

   Returns: The id of the FailureDefinition for the failure.
  """
  pass
 def GetSeverity(self):
  """
  GetSeverity(self: FailureMessage) -> FailureSeverity

  

   Retrieves the severity of the failure.

   Returns: The severity of the failure.
  """
  pass
 def HasResolutionOfType(self,type):
  """
  HasResolutionOfType(self: FailureMessage,type: FailureResolutionType) -> bool

  

   Checks if failure has a resolution of a given type.

  

   type: The type of resolution.

   Returns: True if the failure has a type of resolutions,else false.
  """
  pass
 def HasResolutions(self):
  """
  HasResolutions(self: FailureMessage) -> bool

  

   Checks if the failure has any resolutions.

   Returns: True if the failure has any resolutions,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureMessage,disposing: bool) """
  pass
 def SetAdditionalElement(self,additionalElement):
  """
  SetAdditionalElement(self: FailureMessage,additionalElement: ElementId) -> FailureMessage

  

   Sets the additional reference element for the failure.

  

   additionalElement: The additional element.

   Returns: The FailureMessage.
  """
  pass
 def SetAdditionalElements(self,additionalElements):
  """ SetAdditionalElements(self: FailureMessage,additionalElements: ICollection[ElementId]) -> FailureMessage """
  pass
 def SetFailingElement(self,id):
  """
  SetFailingElement(self: FailureMessage,id: ElementId) -> FailureMessage

  

   Sets the element that has caused the failure.

  

   id: The element that has caused the failure.

   Returns: The FailureMessage.
  """
  pass
 def SetFailingElements(self,idsToShow):
  """ SetFailingElements(self: FailureMessage,idsToShow: ICollection[ElementId]) -> FailureMessage """
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
 def __new__(self,id):
  """ __new__(cls: type,id: FailureDefinitionId) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FailureMessage) -> bool



"""


