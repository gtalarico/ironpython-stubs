class RebarShapeDefinition(object,IDisposable):
 """
 A class to assist in defining rebar shapes.

    A RebarShape element needs exactly one RebarShapeDefinition.
 """
 def AddFormulaParameter(self,paramId,formula):
  """
  AddFormulaParameter(self: RebarShapeDefinition,paramId: ElementId,formula: str)

   Add a formula-driven parameter to the shape definition.

  

   paramId: The parameter. To obtain the id of a shared parameter,

     call 

    RebarShapeParameters.GetElementIdForExternalDefinition.

  

   formula: The formula expressed as a string. The string is exactly what a user would

     

    type into the Family Types dialog,e.g. "Total Length*3.14159*(Bar 

    Diameter/2)*(Bar Diameter/2)"
  """
  pass
 def AddParameter(self,paramId,defaultValue):
  """
  AddParameter(self: RebarShapeDefinition,paramId: ElementId,defaultValue: float)

   Add a parameter to the shape definition.

  

   paramId: The parameter. To obtain the id of a shared parameter,

     call 

    RebarShapeParameters.GetElementIdForExternalDefinition.

  

   defaultValue: A default value for this parameter in shapes. The default values

     should be 

    chosen carefully,because they are required to be consistent as a set of 

    constraints.
  """
  pass
 def CheckDefaultParameterValues(self,bendRadius,barDiameter):
  """
  CheckDefaultParameterValues(self: RebarShapeDefinition,bendRadius: float,barDiameter: float) -> bool

  

   Check that the shape can be solved with the default parameter values.

  

   bendRadius: A value for the Bend Radius parameter. Zero is allowed.

   barDiameter: A value for the Bar Diameter parameter. Zero is allowed.

   Returns: True if the rebar can be solved with the

     default parameter values and the 

    given bend radius and

     bar diameter; false if it cannot.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RebarShapeDefinition) """
  pass
 def GetParameterDefaultValue(self,paramId):
  """
  GetParameterDefaultValue(self: RebarShapeDefinition,paramId: ElementId) -> float

  

   Return the parameter's default value as stored in the definition.

  

   paramId: Id of a parameter in the definition.

   Returns: The parameter value.
  """
  pass
 def GetParameterFormula(self,paramId):
  """
  GetParameterFormula(self: RebarShapeDefinition,paramId: ElementId) -> str

  

   Return the parameter's formula,if one is associated with it.

  

   paramId: Id of a parameter in the definition.

   Returns: The formula,or an empty string if there is no formula for the parameter.
  """
  pass
 def GetParameters(self):
  """
  GetParameters(self: RebarShapeDefinition) -> IList[ElementId]

  

   Return the Ids of the shared parameters in the Definition.

   Returns: List of parameters as ElementIds.
  """
  pass
 def HasParameter(self,paramId):
  """
  HasParameter(self: RebarShapeDefinition,paramId: ElementId) -> bool

  

   Whether the definition stores the parameter.

  

   paramId: Id of a parameter.

   Returns: True if the definition stores the parameter,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarShapeDefinition,disposing: bool) """
  pass
 def RemoveParameter(self,paramId):
  """
  RemoveParameter(self: RebarShapeDefinition,paramId: ElementId)

   Remove the parameter from the definition.

  

   paramId: Id of a parameter in the definition.
  """
  pass
 def SetParameterDefaultValue(self,paramId,value):
  """
  SetParameterDefaultValue(self: RebarShapeDefinition,paramId: ElementId,value: float)

   Change the parameter's value as stored in the definition.

  

   paramId: Id of a parameter in the definition.

   value: New value for the parameter.
  """
  pass
 def SetParameterFormula(self,paramId,formula):
  """
  SetParameterFormula(self: RebarShapeDefinition,paramId: ElementId,formula: str)

   Associate a formula with the parameter.

  

   paramId: Id of a parameter in the definition.

   formula: The formula expressed as a string. The string is exactly what a user would

     

    type into the Family Types dialog,e.g. "Total Length*3.14159*(Bar 

    Diameter/2)*(Bar Diameter/2)"
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
 Complete=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Report whether the shape definition is fully

   constrained.



Get: Complete(self: RebarShapeDefinition) -> bool



"""

 IsPlanar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Reports whether the shape definition lies within a plane: false if a spiral,

   true in all other cases.



Get: IsPlanar(self: RebarShapeDefinition) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RebarShapeDefinition) -> bool



"""


