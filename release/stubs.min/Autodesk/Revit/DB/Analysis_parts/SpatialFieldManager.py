class SpatialFieldManager(Element,IDisposable):
 """
 Exposes all API for an external analysis application.

    Its primary role is creation,deletion and modification of SpatialFieldElement elements.
 """
 def AddSpatialFieldPrimitive(self,*__args):
  """
  AddSpatialFieldPrimitive(self: SpatialFieldManager,reference: Reference) -> int

  

   Creates an empty analysis results primitive associated with a reference.

  

   reference: Reference pointing to the curve or face to be associated with the primitive

   Returns: Unique index of primitive for future references

  AddSpatialFieldPrimitive(self: SpatialFieldManager) -> int

  

   Creates empty analysis results primitive not associated with any geometry 

    element

  

   Returns: Unique index of primitive for future references

  AddSpatialFieldPrimitive(self: SpatialFieldManager,reference: Reference,hidingMode: SpatialFieldPrimitiveHideMode) -> int

  

   Creates an empty analysis results primitive associated with a reference,with 

    the option to control how the reference element is hidden.

  

  

   reference: Reference pointing to the curve or face to be associated with the primitive

   hidingMode: The mode used to hide the original model element

   Returns: Unique index of primitive for future references

  AddSpatialFieldPrimitive(self: SpatialFieldManager,curve: Curve,trf: Transform) -> int

  

   Creates empty analysis results primitive associated with a curve and a 

    transform.

  

  

   curve: Curve to be associated with the primitive.

     %curve% does NOT correspond to 

    actual Revit geometry,i.e. it cannot be associated with reference;

     

    otherwise the other overload of the method must be used (taking "reference" as 

    the input)

  

   trf: Conformal Transform to be applied to %curve%.

   Returns: Unique index of primitive for future references

  AddSpatialFieldPrimitive(self: SpatialFieldManager,face: Face,trf: Transform) -> int

  

   Creates empty analysis results primitive associated with a face and a transform.

  

   face: Face to be associated with the primitive

   trf: Conformal Transform to be applied to %face%

   Returns: Unique index of primitive for future references
  """
  pass
 def Clear(self):
  """
  Clear(self: SpatialFieldManager)

   Clear all analysis results managed by this manager object
  """
  pass
 @staticmethod
 def CreateSpatialFieldManager(view,numberOfMeasurements):
  """
  CreateSpatialFieldManager(view: View,numberOfMeasurements: int) -> SpatialFieldManager

  

   Factory method - creates manager object for the given view

  

   view: View for which manager object is created or retrieved

   numberOfMeasurements: Total number of measurements in the calculated results.

     This number defines 

    the length of value arrays in ValueAtPoint objects

  

   Returns: Manager object for the view passed in the argument
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetLegend(self):
  """
  GetLegend(self: SpatialFieldManager) -> AnalysisDisplayLegend

  

   Returns legend element or NULL

   Returns: The legend element or NULL
  """
  pass
 def GetMaximum(self,resultIndex,rawValue):
  """
  GetMaximum(self: SpatialFieldManager,resultIndex: int,rawValue: bool) -> float

  

   Calculates the maximum value for all primitives

  

   resultIndex: Index of result schema

   rawValue: If true returned value is NOT multiplied by the current result's units 

    multiplier,otherwise it IS

  

   Returns: Resulting maximum value
  """
  pass
 def GetMinimum(self,resultIndex,rawValue):
  """
  GetMinimum(self: SpatialFieldManager,resultIndex: int,rawValue: bool) -> float

  

   Calculates the minimum value for all primitives

  

   resultIndex: Index of result schema

   rawValue: If true returned value is NOT multiplied by the current result's units 

    multiplier,otherwise it IS

  

   Returns: Resulting minimum value
  """
  pass
 def GetRegisteredResults(self):
  """
  GetRegisteredResults(self: SpatialFieldManager) -> IList[int]

  

   Returns an array of indices of all registered results
  """
  pass
 def GetResultSchema(self,idx):
  """
  GetResultSchema(self: SpatialFieldManager,idx: int) -> AnalysisResultSchema

  

   Returns result schema by index

  

   idx: Index of registered result schema
  """
  pass
 @staticmethod
 def GetSpatialFieldManager(view):
  """
  GetSpatialFieldManager(view: View) -> SpatialFieldManager

  

   Retrieves manager object for the given view or returns NULL

  

   view: View for which manager object is retrieved

   Returns: Manager object for the view passed in the argument
  """
  pass
 def IsResultSchemaNameUnique(self,name,resultIndexToSkip):
  """
  IsResultSchemaNameUnique(self: SpatialFieldManager,name: str,resultIndexToSkip: int) -> bool

  

   Verify the uniqueness of the name among all registered result schemas.

  

   name: Name to verify uniqueness of.

   resultIndexToSkip: Index of result (e.g. to be replaced) which names should not count for 

    uniqueness; negative number means nothing is excluded from comparison.

  

   Returns: True if name is unique,false otherwise.
  """
  pass
 @staticmethod
 def IsTextTypeIdValid(textTypeId,doc):
  """
  IsTextTypeIdValid(textTypeId: ElementId,doc: Document) -> bool

  

   Verify if text type id is valid.

  

   textTypeId: Text type id to be validated.

   doc: Document for which %textTypeId% is validated.

   Returns: True if text type id is valid,false otherwise.
  """
  pass
 def RegisterResult(self,resultSchema):
  """
  RegisterResult(self: SpatialFieldManager,resultSchema: AnalysisResultSchema) -> int

  

   Registers result and assigns it a unique result index

  

   resultSchema: Result schema to be registered

   Returns: Unique index assigned to the result
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveSpatialFieldPrimitive(self,idx):
  """
  RemoveSpatialFieldPrimitive(self: SpatialFieldManager,idx: int)

   Removes analysis results primitive identified by the unique index

  

   idx: Unique index identifying the primitive
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetMeasurementDescriptions(self,measurementDescriptions):
  """ SetMeasurementDescriptions(self: SpatialFieldManager,measurementDescriptions: IList[str]) """
  pass
 def SetMeasurementNames(self,measurementNames):
  """ SetMeasurementNames(self: SpatialFieldManager,measurementNames: IList[str]) """
  pass
 def SetResultSchema(self,idx,resultSchema):
  """
  SetResultSchema(self: SpatialFieldManager,idx: int,resultSchema: AnalysisResultSchema)

   Sets a new value for an existing result schema in the result registry

  

   idx: Index of registered result schema

   resultSchema: Result schema replacing the existent one
  """
  pass
 def UpdateSpatialFieldPrimitive(self,idx,fieldDomainPoints,fieldValues,resultIndex):
  """
  UpdateSpatialFieldPrimitive(self: SpatialFieldManager,idx: int,fieldDomainPoints: FieldDomainPoints,fieldValues: FieldValues,resultIndex: int)

   Populates analysis results data (or replaces the existing data) in the existing 

    primitive identified by the unique index

  

  

   idx: Unique index identifying the primitive

   fieldDomainPoints: Set of domain points.

     If the new set of domain points is supplied,all 

    previously supplied domain points and field values for all results are removed 

    from the primitive.

     If %fieldDomainPoints% is ll only fieldValues are 

    updated

  

   fieldValues: Set of data values.

     Number of values in fieldValues must coincide with the 

    number of points in fieldDomainPoints

  

   resultIndex: Unique index identifying the result schema
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
 CurrentMeasurement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores the currently displayed measurement



Get: CurrentMeasurement(self: SpatialFieldManager) -> int



Set: CurrentMeasurement(self: SpatialFieldManager)=value

"""

 LegendPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores current position of analysis results legend element in view



Get: LegendPosition(self: SpatialFieldManager) -> XYZ



Set: LegendPosition(self: SpatialFieldManager)=value

"""

 LegendShowConfigurationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true legend contains analysis configuration name.



Get: LegendShowConfigurationName(self: SpatialFieldManager) -> bool



Set: LegendShowConfigurationName(self: SpatialFieldManager)=value

"""

 LegendShowDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true legend contains analysis description.



Get: LegendShowDescription(self: SpatialFieldManager) -> bool



Set: LegendShowDescription(self: SpatialFieldManager)=value

"""

 LegendTextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores element id of text associated with common (result-independent) part of legend in view.



Get: LegendTextTypeId(self: SpatialFieldManager) -> ElementId



Set: LegendTextTypeId(self: SpatialFieldManager)=value

"""

 NumberOfMeasurements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores the total number of measurements



Get: NumberOfMeasurements(self: SpatialFieldManager) -> int



"""

 ResultsVisibleInView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Enables analysis results visibility in the view.



Get: ResultsVisibleInView(self: SpatialFieldManager) -> bool



Set: ResultsVisibleInView(self: SpatialFieldManager)=value

"""

 UseRangeForAllMeasurements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Governs how minimum and maximum values (the data range) are calculated.



Get: UseRangeForAllMeasurements(self: SpatialFieldManager) -> bool



Set: UseRangeForAllMeasurements(self: SpatialFieldManager)=value

"""


