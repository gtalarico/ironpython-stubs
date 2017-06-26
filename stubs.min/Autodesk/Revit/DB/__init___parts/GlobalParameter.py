class GlobalParameter(ParameterElement,IDisposable):
 """ This class represents a GlobalParameter element in Revit. """
 def CanChangeReporting(self):
  """
  CanChangeReporting(self: GlobalParameter) -> bool
  
   Tests whether the global parameter permits a change of its current value of the 
    IsReporting attribute.
  
   Returns: Returns True if the change is allowed; False otherwise.
  """
  pass
 def CanLabelDimension(self,dimensionId):
  """
  CanLabelDimension(self: GlobalParameter,dimensionId: ElementId) -> bool
  
   Tests whether a dimension can be labeled by the global parameter.
  
   dimensionId: Id of a dimension element.
   Returns: True of the input dimension can be labeled by this global parameter; False 
    oterwise.
  """
  pass
 @staticmethod
 def Create(document,name,datatype):
  """
  Create(document: Document,name: str,datatype: ParameterType) -> GlobalParameter
  
   Creates a new Global Parameter in the given document.
  
   document: Document in which the new parameter is to be created
   name: The name of the new parameter. It must be unique in the document
   datatype: Type of the data the parameter is to store
   Returns: An instance of the new global parameter
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAffectedElements(self):
  """
  GetAffectedElements(self: GlobalParameter) -> ISet[ElementId]
  
   Returns all elements of which properties are driven by this global parameter.
   Returns: Collection of Element Ids.
  """
  pass
 def GetAffectedGlobalParameters(self):
  """
  GetAffectedGlobalParameters(self: GlobalParameter) -> ISet[ElementId]
  
   Returns all other global parameters which refer to this global parameter in 
    their formulas.
  
   Returns: Collection of Element Ids.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetFormula(self):
  """
  GetFormula(self: GlobalParameter) -> str
  
   Returns the parameter's expression in form of a string.
   Returns: The string representing the expression assigned to the parameter.
  """
  pass
 def GetLabeledDimensions(self):
  """
  GetLabeledDimensions(self: GlobalParameter) -> ISet[ElementId]
  
   Returns all dimension elements that are currently labeled by this global 
    parameter.
  
   Returns: Collection of Element Ids.
  """
  pass
 def GetLabelName(self):
  """
  GetLabelName(self: GlobalParameter) -> str
  
   Returns the name of this parameter's label,which is used to label dimension 
    elements.
  
   Returns: The name of the parameter's label.
  """
  pass
 def GetValue(self):
  """
  GetValue(self: GlobalParameter) -> ParameterValue
  
   Obtains the curent value of the global parameter.
   Returns: An instance of one of the classes derived from the ParameterValue base class.
  """
  pass
 def HasValidTypeForReporting(self):
  """
  HasValidTypeForReporting(self: GlobalParameter) -> bool
  
   Tests that the global parameter has data of a type that supports reporting.
   Returns: True if the parameter has data of a type that supports reporting; False 
    otherwise.
  """
  pass
 @staticmethod
 def IsValidDataType(datatype):
  """
  IsValidDataType(datatype: ParameterType) -> bool
  
   Tests whether the input Data Type is valid as a type of a global parameter.
  
   datatype: Type of the data the parameter is to store.
   Returns: True if the data type is suitable for a global parameter; False otherwise.
  """
  pass
 def IsValidFormula(self,expression):
  """
  IsValidFormula(self: GlobalParameter,expression: str) -> bool
  
   Tests that the given expression is a valid as formula for this parameter.
  """
  pass
 def LabelDimension(self,dimensionId):
  """
  LabelDimension(self: GlobalParameter,dimensionId: ElementId)
   Labels a dimension with this global parameter.
  
   dimensionId: Id of a dimension element.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetDrivingDimension(self,dimensionId):
  """
  SetDrivingDimension(self: GlobalParameter,dimensionId: ElementId)
   Set a dimension to drive the value of this parameter.
  
   dimensionId: Id of a dimension element.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetFormula(self,expression):
  """
  SetFormula(self: GlobalParameter,expression: str)
   Sets a formula expression for this parameter.
  
   expression: Valid formula string.
  """
  pass
 def SetValue(self,value):
  """
  SetValue(self: GlobalParameter,value: ParameterValue)
   Sets a new value of the global parameter.
  
   value: An instance of one of the value classes derived from ParameterValue.
  """
  pass
 def UnlabelDimension(self,dimensionId):
  """
  UnlabelDimension(self: GlobalParameter,dimensionId: ElementId)
   Unlabels a dimension that is currently labeled by this global parameter.
  
   dimensionId: Id of a dimension element.
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
 IsDrivenByDimension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this parameter is driven by a dimension or not.

Get: IsDrivenByDimension(self: GlobalParameter) -> bool

"""

 IsDrivenByFormula=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this parameter is driven by a formula or not.

Get: IsDrivenByFormula(self: GlobalParameter) -> bool

"""

 IsReporting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this is a reporting global parameter or not.

Get: IsReporting(self: GlobalParameter) -> bool

Set: IsReporting(self: GlobalParameter)=value
"""


