class FailureDefinitionRegistry(object,IDisposable):
 """ The global registry for all FailureDefinitions in the Revit session. """
 def Dispose(self):
  """ Dispose(self: FailureDefinitionRegistry) """
  pass
 def FindFailureDefinition(self,id):
  """
  FindFailureDefinition(self: FailureDefinitionRegistry,id: FailureDefinitionId) -> FailureDefinitionAccessor

  

   Finds a specific FailureDefinition by a given FailureDefinitionId.

  

   id: The id of the FailureDefinition.

   Returns: The accessor of the found FailureDefinition,or null,if the FailureDefinition 

    was not found.
  """
  pass
 def ListAllFailureDefinitions(self):
  """
  ListAllFailureDefinitions(self: FailureDefinitionRegistry) -> IList[FailureDefinitionAccessor]

  

   Retrieves all the registered FailureDefinitions.

   Returns: All the registered FailureDefinitions.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FailureDefinitionRegistry,disposing: bool) """
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



Get: IsValidObject(self: FailureDefinitionRegistry) -> bool



"""


