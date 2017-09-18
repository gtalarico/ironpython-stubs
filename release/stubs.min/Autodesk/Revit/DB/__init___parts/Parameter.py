class Parameter(APIObject,IDisposable):
 """ The parameter object contains the value data assigned to that parameter. """
 def AsDouble(self):
  """
  AsDouble(self: Parameter) -> float

  

   Provides access to the double precision number within the parameter.

   Returns: The double value contained in the parameter.
  """
  pass
 def AsElementId(self):
  """
  AsElementId(self: Parameter) -> ElementId

  

   Provides access to the Autodesk::Revit::DB::ElementId^ stored within the 

    parameter.

  

   Returns: The Autodesk::Revit::DB::ElementId^ contained in the parameter.
  """
  pass
 def AsInteger(self):
  """
  AsInteger(self: Parameter) -> int

  

   Provides access to the integer number within the parameter.

   Returns: The integer value contained in the parameter.
  """
  pass
 def AssociateWithGlobalParameter(self,gpId):
  """
  AssociateWithGlobalParameter(self: Parameter,gpId: ElementId)

   Associates this parameter with a global parameter in the same document.

  

   gpId: Id of a global parameter contained in this parameter's document
  """
  pass
 def AsString(self):
  """
  AsString(self: Parameter) -> str

  

   Provides access to the string contents of the parameter.

   Returns: The string contained in the parameter.
  """
  pass
 def AsValueString(self,formatOptions=None):
  """
  AsValueString(self: Parameter) -> str

  

   Get the parameter value as a string with units.

   Returns: The string that represents the parameter value.

  AsValueString(self: Parameter,formatOptions: FormatOptions) -> str

  

   Get the parameter value as a string with units.

  

   formatOptions: Options for formatting the string.

   Returns: The string that represents the parameter value.
  """
  pass
 def CanBeAssociatedWithGlobalParameter(self,gpId):
  """
  CanBeAssociatedWithGlobalParameter(self: Parameter,gpId: ElementId) -> bool

  

   Tests whether this parameter can be associated with the given global parameter.

  

   gpId: Id of a global parameter contained in this parameter's document

   Returns: True if this parameter can be associated with the given global parameter; False 

    otherwise.
  """
  pass
 def CanBeAssociatedWithGlobalParameters(self):
  """
  CanBeAssociatedWithGlobalParameters(self: Parameter) -> bool

  

   Tests whether this parameter can be associated with any global parameter.

   Returns: True if the given parameter can be associated (is parametrizable); False 

    otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def DissociateFromGlobalParameter(self):
  """
  DissociateFromGlobalParameter(self: Parameter)

   Dissociates this parameter from a global parameter.
  """
  pass
 def GetAssociatedGlobalParameter(self):
  """
  GetAssociatedGlobalParameter(self: Parameter) -> ElementId

  

   Returns a global parameter,if any,currently associated with this parameter.

   Returns: Id of a global parameter or InvalidElemetnId.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def Set(self,value):
  """
  Set(self: Parameter,value: int) -> bool

  

   Sets the parameter to a new integer value.

  

   value: The new integer value to which the parameter is to be set.

   Returns: The Set method will return True if the parameter was successfully set to the 

    new value,otherwise false.

  

  Set(self: Parameter,value: str) -> bool

  

   Sets the parameter to a new string of text.

  

   value: The new text value to which the parameter is to be set.

   Returns: The Set method will return True if the parameter was successfully set to the 

    new value,otherwise false.

  

  Set(self: Parameter,value: ElementId) -> bool

  

   Sets the parameter to a new element id.

  

   value: The new element id to which the parameter is to be set.

   Returns: The Set method will return True if the parameter was successfully set to the 

    new value,otherwise false.

  

  Set(self: Parameter,value: float) -> bool

  

   Sets the parameter to a new real number value.

  

   value: The new double value to which the parameter is to be set.

   Returns: The Set method will return True if the parameter was successfully set to the 

    new value,otherwise false.
  """
  pass
 def SetValueString(self,valueString):
  """
  SetValueString(self: Parameter,valueString: str) -> bool

  

   Set the parameter value according to the input string.

  

   valueString: The string that represents the parameter value.

   Returns: Indicates whether the parameter value is successfully set.
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
 Definition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Definition object that describes the data type,name and other details of the

parameter.



Get: Definition(self: Parameter) -> Definition



"""

 DisplayUnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the display unit type of the parameter object.



Get: DisplayUnitType(self: Parameter) -> DisplayUnitType



"""

 Element=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element to which this parameter belongs.



Get: Element(self: Parameter) -> Element



"""

 GUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Guid for a shared parameter.



Get: GUID(self: Parameter) -> Guid



"""

 HasValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the parameter has an assigned value.



Get: HasValue(self: Parameter) -> bool



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the parameter.



Get: Id(self: Parameter) -> ElementId



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the readonly property of the parameter.



Get: IsReadOnly(self: Parameter) -> bool



"""

 IsShared=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the parameter is a shared parameter.



Get: IsShared(self: Parameter) -> bool



"""

 StorageType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Describes the type that is used internally within the parameter to store its value.



Get: StorageType(self: Parameter) -> StorageType



"""

 UserModifiable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the interactive user can modify the value of this parameter.



Get: UserModifiable(self: Parameter) -> bool



"""


