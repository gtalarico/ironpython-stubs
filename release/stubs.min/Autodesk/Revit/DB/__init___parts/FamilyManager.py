class FamilyManager(APIObject,IDisposable):
 """ The family manager object to manage the family types and parameters in family document. """
 def AddParameter(self,*__args):
  """
  AddParameter(self: FamilyManager,familyDefinition: ExternalDefinition,parameterGroup: BuiltInParameterGroup,isInstance: bool) -> FamilyParameter

  

   Add a new shared parameter to the family.

  

   familyDefinition: The definition of the loaded shared parameter.

   parameterGroup: The group to which the family parameter belongs.

   isInstance: Indicates if the new parameter is instance or type.

   Returns: If creation was successful the new shared parameter is returned,

  otherwise an 

    exception with failure information will be thrown.

  

  AddParameter(self: FamilyManager,parameterName: str,parameterGroup: BuiltInParameterGroup,parameterType: ParameterType,isInstance: bool) -> FamilyParameter

  

   Add a new family parameter with a given name.

  

   parameterName: The name of the new family parameter.

   parameterGroup: The group to which the family parameter belongs.

   parameterType: The type of new family parameter.

   isInstance: Indicates if the new family parameter is instance or type.

   Returns: If creation was successful the new parameter is returned,

  otherwise an 

    exception with failure information will be thrown.

  

  AddParameter(self: FamilyManager,parameterName: str,parameterGroup: BuiltInParameterGroup,familyCategory: Category,isInstance: bool) -> FamilyParameter

  

   Add a new family type parameter to control the type of a nested family within 

    another family.

  

  

   parameterName: The name of the new family parameter.

   parameterGroup: The group to which the family parameter belongs.

   familyCategory: The category to which the new family parameter binds.

   isInstance: Indicates if the new family parameter is instance or type.

   Returns: If creation was successful the new parameter is returned,

  otherwise an 

    exception with failure information will be thrown.
  """
  pass
 def AssociateElementParameterToFamilyParameter(self,elementParameter,familyParameter):
  """
  AssociateElementParameterToFamilyParameter(self: FamilyManager,elementParameter: Parameter,familyParameter: FamilyParameter)

   Associates or disassociates the element parameter to an existing family 

    parameter.

  

  

   elementParameter: The parameter of an element in family.

   familyParameter: The existing family parameter. If the input to this argument is ll,

  it will 

    disassociate the element parameter from any family parameters.
  """
  pass
 def CanElementParameterBeAssociated(self,elementParameter):
  """
  CanElementParameterBeAssociated(self: FamilyManager,elementParameter: Parameter) -> bool

  

   Indicates if this element parameter can be associated with a family parameter.
  """
  pass
 def DeleteCurrentType(self):
  """
  DeleteCurrentType(self: FamilyManager)

   Remove the current family type.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def GetAssociatedFamilyParameter(self,elementParameter):
  """
  GetAssociatedFamilyParameter(self: FamilyManager,elementParameter: Parameter) -> FamilyParameter

  

   Gets the associated family parameter of an element parameter.

  

   elementParameter: The parameter of an element in family.

   Returns: The associated family parameter if there is an association between them,

    returns ll if not.
  """
  pass
 def GetParameters(self):
  """
  GetParameters(self: FamilyManager) -> IList[FamilyParameter]

  

   Gets the parameters associated to family types in order.

   Returns: A collection containing all family parameters.
  """
  pass
 def IsParameterLockable(self,familyParameter):
  """
  IsParameterLockable(self: FamilyManager,familyParameter: FamilyParameter) -> bool

  

   For Conceptual Mass and Curtain Panel families,

  indicate whether the specified 

    parameter can be locked.

  

   Returns: True if the family is a Conceptual Mass or Curtain

  Panel Family and the 

    parameter drives one or more

  dimensions; false otherwise.
  """
  pass
 def IsParameterLocked(self,familyParameter):
  """
  IsParameterLocked(self: FamilyManager,familyParameter: FamilyParameter) -> bool

  

   For Conceptual Mass and Curtain Panel families,

  indicate whether the specified 

    dimension-driving

  parameter is locked.

  

   Returns: True if the parameter is lockable

  and is locked; false otherwise.
  """
  pass
 def IsUserAssignableParameterGroup(self,parameterGroup):
  """
  IsUserAssignableParameterGroup(self: FamilyManager,parameterGroup: BuiltInParameterGroup) -> bool

  

   Checks if the given parameter group can be assigned to new parameters.

   Returns: True if the parameter group can be assigned to new parameters,false otherwise.
  """
  pass
 def MakeInstance(self,familyParameter):
  """
  MakeInstance(self: FamilyManager,familyParameter: FamilyParameter)

   Set the family parameter as an instance parameter.
  """
  pass
 def MakeNonReporting(self,familyParameter):
  """
  MakeNonReporting(self: FamilyManager,familyParameter: FamilyParameter)

   Set the reporting family parameter as a regular/driving parameter.
  """
  pass
 def MakeReporting(self,familyParameter):
  """
  MakeReporting(self: FamilyManager,familyParameter: FamilyParameter)

   Set the family parameter as a reporting parameter.
  """
  pass
 def MakeType(self,familyParameter):
  """
  MakeType(self: FamilyManager,familyParameter: FamilyParameter)

   Set the family parameter as a type parameter.
  """
  pass
 def NewType(self,typeName):
  """
  NewType(self: FamilyManager,typeName: str) -> FamilyType

  

   Add a new family type with a given name and makes it be the current type.

  

   typeName: The name of new family type.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def RemoveParameter(self,familyParameter):
  """
  RemoveParameter(self: FamilyManager,familyParameter: FamilyParameter)

   Remove an existing family parameter from the family.

  

   familyParameter: The family parameter.
  """
  pass
 def RenameCurrentType(self,typeName):
  """
  RenameCurrentType(self: FamilyManager,typeName: str)

   Rename the current family type.

  

   typeName: The new name of the current family type.
  """
  pass
 def RenameParameter(self,familyParameter,name):
  """
  RenameParameter(self: FamilyManager,familyParameter: FamilyParameter,name: str)

   Rename a family parameter.

  

   familyParameter: The family parameter.

   name: The new name.
  """
  pass
 def ReorderParameters(self,parameters):
  """ ReorderParameters(self: FamilyManager,parameters: IList[FamilyParameter]) """
  pass
 def ReplaceParameter(self,currentParameter,*__args):
  """
  ReplaceParameter(self: FamilyManager,currentParameter: FamilyParameter,familyDefinition: ExternalDefinition,parameterGroup: BuiltInParameterGroup,isInstance: bool) -> FamilyParameter

  

   Replace a family parameter with a shared parameter.

  

   currentParameter: The current family parameter.

   familyDefinition: The definition of the loaded shared parameter.

   parameterGroup: The group to which the new shared parameter belongs.

   isInstance: Indicates if the new parameter is instance or type.

   Returns: If replacement was successful the new shared parameter is returned,

  otherwise 

    an exception with failure information will be thrown.

  

  ReplaceParameter(self: FamilyManager,currentParameter: FamilyParameter,parameterName: str,parameterGroup: BuiltInParameterGroup,isInstance: bool) -> FamilyParameter

  

   Replace a shared family parameter with a new non-shared family parameter.

  

   currentParameter: The current family parameter.

   parameterName: The name of the new family parameter.

   parameterGroup: The group to which the new family parameter belongs.

   isInstance: Indicates if the new parameter is instance or type.

   Returns: If replacement was successful the new family parameter is returned,

  otherwise 

    an exception with failure information will be thrown.
  """
  pass
 def Set(self,familyParameter,value):
  """
  Set(self: FamilyManager,familyParameter: FamilyParameter,value: str)

   Set the string value of a family parameter of the current family type.

  

   familyParameter: A family parameter of the current type.

   value: The new value for family parameter.

  Set(self: FamilyManager,familyParameter: FamilyParameter,value: int)

   Set the integer value of a family parameter of the current family type.

  

   familyParameter: A family parameter of the current type.

   value: The new value for family parameter.

  Set(self: FamilyManager,familyParameter: FamilyParameter,value: ElementId)

   Set the ElementId value of a family parameter of the current family type.

  

   familyParameter: A family parameter of the current type.

   value: The new value for family parameter.

  Set(self: FamilyManager,familyParameter: FamilyParameter,value: float)

   Set the double value of a family parameter of the current family type.

  

   familyParameter: A family parameter of the current type.

   value: The new value for family parameter.
  """
  pass
 def SetDescription(self,familyParameter,description):
  """
  SetDescription(self: FamilyManager,familyParameter: FamilyParameter,description: str)

   Set the description for an existing family parameter. 

  The description will be 

    used as tooltip in the Revit UI including in the properties palette.

  

  

   familyParameter: The family parameter.

   description: The description of the family parameter.
  """
  pass
 def SetFormula(self,familyParameter,formula):
  """
  SetFormula(self: FamilyManager,familyParameter: FamilyParameter,formula: str)

   Set the formula of a family parameter.

  

   familyParameter: The family parameter.

   formula: The formula string,input ll to clean the formula of the parameter.
  """
  pass
 def SetParameterLocked(self,familyParameter,locked):
  """
  SetParameterLocked(self: FamilyManager,familyParameter: FamilyParameter,locked: bool)

   For Conceptual Mass and Curtain Panel families,

  lock or unlock a 

    dimension-driving

  parameter.
  """
  pass
 def SetValueString(self,familyParameter,value):
  """
  SetValueString(self: FamilyManager,familyParameter: FamilyParameter,value: str)

   Set the string value of a family parameter of the current family type.

  

   familyParameter: The family parameter of current type.

   value: The new value string for family parameter.
  """
  pass
 def SortParameters(self,order):
  """
  SortParameters(self: FamilyManager,order: ParametersOrder)

   Sorts the family parameters according to the desired sort order.

  

   order: The desired sort order.
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
 CurrentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current family type.



Get: CurrentType(self: FamilyManager) -> FamilyType



Set: CurrentType(self: FamilyManager)=value

"""

 Parameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All family parameters in this family.



Get: Parameters(self: FamilyManager) -> FamilyParameterSet



"""

 Types=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All family types in the family.



Get: Types(self: FamilyManager) -> FamilyTypeSet



"""


