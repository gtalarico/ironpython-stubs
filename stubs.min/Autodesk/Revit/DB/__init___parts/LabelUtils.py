class LabelUtils(object,IDisposable):
 """ Used to obtain user-visible names for enums. """
 def Dispose(self):
  """ Dispose(self: LabelUtils) """
  pass
 @staticmethod
 def GetLabelFor(*__args):
  """
  GetLabelFor(ductLossMethodType: DuctLossMethodType,doc: Document) -> str
  
   Gets the user-visible name for a DuctLossMethodType.
  
   ductLossMethodType: The DuctLossMethodType to get the user-visible name.
   doc: The document from which to get the DuctLossMethodType.
  GetLabelFor(pipeLossMethodType: PipeLossMethodType,doc: Document) -> str
  
   Gets the user-visible name for a PipeLossMethodType.
  
   pipeLossMethodType: The PipeLossMethodType to get the user-visible name.
   doc: The document from which to get the PipeLossMethodType.
  GetLabelFor(builtInParamGroup: BuiltInParameterGroup) -> str
  
   Gets the user-visible name for a BuiltInParameterGroup.
  
   builtInParamGroup: The BuiltInParameterGroup to get the user-visible name.
  GetLabelFor(builtInParam: BuiltInParameter) -> str
  
   Gets the user-visible name for a BuiltInParameter.
  
   builtInParam: The BuiltInParameter to get the user-visible name.
  GetLabelFor(paramType: ParameterType) -> str
  
   Gets the user-visible name for a ParameterType.
  
   paramType: The ParameterType to get the user-visible name.
  GetLabelFor(unitSymbolType: UnitSymbolType) -> str
  
   Gets the user-visible name for a UnitSymbolType.
  
   unitSymbolType: The UnitSymbolType to get the user-visible name.
  GetLabelFor(buildingType: gbXMLBuildingType,document: Document) -> str
  
   Gets the user-visible name for a gbXMLBuildingType.
  
   buildingType: The gbXMLBuildingType to get the user-visible name.
   document: The document from which to get the gbXMLBuildingType.
  GetLabelFor(unitType: UnitType) -> str
  
   Gets the user-visible name for a UnitType.
  
   unitType: The UnitType to get the user-visible name.
  GetLabelFor(pipeFlowState: PipeFlowState,doc: Document) -> str
  
   Gets the user-visible name for a PipeFlowState.
  
   pipeFlowState: The PipeFlowState to get the user-visible name.
   doc: The document from which to get the PipeFlowState.
  GetLabelFor(displayUnitType: DisplayUnitType) -> str
  
   Gets the user-visible name for a DisplayUnitType.
  
   displayUnitType: The DisplayUnitType to get the user-visible name.
  """
  pass
 @staticmethod
 def GetStructuralSectionShapeName(shape):
  """
  GetStructuralSectionShapeName(shape: StructuralSectionShape) -> str
  
   Gets the user-visible name for a StructuralSectionShape.
  
   shape: The StructuralSectionShape to get the user-visible name.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: LabelUtils,disposing: bool) """
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

Get: IsValidObject(self: LabelUtils) -> bool

"""


