class FailureDefinition(object,IDisposable):
 """ Defines persistent information about a failure. """
 def AddResolutionType(self,type,caption,classOfResolution):
  """
  AddResolutionType(self: FailureDefinition,type: FailureResolutionType,caption: str,classOfResolution: Type) -> FailureDefinition

  

   Adds a type of possible resolution for the failure.

  

   type: Type of the resolution to add. The type of resolution can be used only once for 

    the FailureDefinition.

  

   caption: A simple description of the resolution.

   classOfResolution: The runtime class of the resolution. Used to ensure that the actual 

    FailureResoution object added to the instance of FailureMessage

     belongs to 

    an applicable class.

  

   Returns: The FailureDefinition.
  """
  pass
 @staticmethod
 def CreateFailureDefinition(id,severity,messageString):
  """
  CreateFailureDefinition(id: FailureDefinitionId,severity: FailureSeverity,messageString: str) -> FailureDefinition

  

   Creates an instance of a FailureDefinition.

  

   id: Unique identifier of the failure.

   severity: The severity of the failure. Cannot be FailureSeverity::None.

   messageString: A user-visible string describing the failure.

   Returns: The created FailureDefinition instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FailureDefinition) """
  pass
 def GetApplicableResolutionTypes(self):
  """
  GetApplicableResolutionTypes(self: FailureDefinition) -> IList[FailureResolutionType]

  

   Retrieves a list of resolution types applicable to the failure.

   Returns: The list of resolution types applicable to the failure.
  """
  pass
 def GetDefaultResolutionType(self):
  """
  GetDefaultResolutionType(self: FailureDefinition) -> FailureResolutionType

  

   Retrieves the default resolution type for the failure.

   Returns: The Default resolution type for the failure.
  """
  pass
 def GetDescriptionText(self):
  """
  GetDescriptionText(self: FailureDefinition) -> str

  

   Retrieves the description text of the failure.

   Returns: The description text.
  """
  pass
 def GetResolutionCaption(self,type):
  """
  GetResolutionCaption(self: FailureDefinition,type: FailureResolutionType) -> str

  

   Retrieves the caption for a specific resolution type.

  

   type: The resolution type.

   Returns: The caption of the resolution.
  """
  pass
 def HasResolutions(self):
  """
  HasResolutions(self: FailureDefinition) -> bool

  

   Checks if the FailureDefinition has at least one resolution.

   Returns: True if at least one resolution is defined in the FailureDefinition.
  """
  pass
 def IsResolutionApplicable(self,type):
  """
  IsResolutionApplicable(self: FailureDefinition,type: FailureResolutionType) -> bool

  

   Checks if the given resolution type is applicable to the failure.

  

   type: The resolution type to check.

   Returns: True if the given resolution type is applicable to the failure,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureDefinition,disposing: bool) """
  pass
 def SetDefaultResolutionType(self,type):
  """
  SetDefaultResolutionType(self: FailureDefinition,type: FailureResolutionType) -> FailureDefinition

  

   Sets the default resolution type for the failure.

  

   type: The type of resolution to be used as default.

   Returns: The FailureDefinition.
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



Get: IsValidObject(self: FailureDefinition) -> bool



"""

 Severity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The severity of the failure.



Get: Severity(self: FailureDefinition) -> FailureSeverity



"""


