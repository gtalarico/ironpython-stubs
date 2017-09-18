class ExternalDefinition(Definition,IDisposable):
 """ The ExternalDefinition object adds properties specific to Autodesk Revit shared parameter definitions. """
 def Dispose(self):
  """ Dispose(self: ExternalDefinition) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalDefinition,disposing: bool) """
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of the parameter. The description will be used as tooltip in the Revit UI including in the properties palette.



Get: Description(self: ExternalDefinition) -> str



"""

 GUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the GUID associated with the shared parameter definition.



Get: GUID(self: ExternalDefinition) -> Guid



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExternalDefinition) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user visible name for the parameter.



Get: Name(self: ExternalDefinition) -> str



"""

 OwnerGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns or change the group ID of the external parameter definition.



Get: OwnerGroup(self: ExternalDefinition) -> DefinitionGroup



Set: OwnerGroup(self: ExternalDefinition)=value

"""

 ParameterGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the group ID of the parameter definition.



Get: ParameterGroup(self: ExternalDefinition) -> BuiltInParameterGroup



"""

 ParameterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the user visible interpretation of the parameter data.



Get: ParameterType(self: ExternalDefinition) -> ParameterType



"""

 UserModifiable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the parameter can be modified by the user interface.



Get: UserModifiable(self: ExternalDefinition) -> bool



"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the parameter is visible in the Autodesk Revit user interface.



Get: Visible(self: ExternalDefinition) -> bool



"""


