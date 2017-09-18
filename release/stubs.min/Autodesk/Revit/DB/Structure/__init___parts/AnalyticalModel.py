class AnalyticalModel(Element,IDisposable):
 """ AnalyticalModel represents the Analytical Model portion of a given Structural Element. """
 def Approximate(self,enableApproximation):
  """
  Approximate(self: AnalyticalModel,enableApproximation: bool)

   Switches between non-approximated (e.g.,Curved) Analytical Models

     and 

    approximated (made up of lines only) Analytical Models

  

  

   enableApproximation: Enable/disable approximated function.
  """
  pass
 def CanApproximate(self):
  """
  CanApproximate(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model can be approximated or not.

   Returns: True if Analytical Model can be approximated; false otherwise.
  """
  pass
 def CanDisableAutoDetect(self,direction):
  """
  CanDisableAutoDetect(self: AnalyticalModel,direction: AnalyticalDirection) -> bool

  

   Indicates if Analytical Auto-detect can be disabled programmatically

  

   direction: Direction in which to test whether Analytical Auto-detect can be disabled

   Returns: True if Analytical Auto-detect can be disabled,false otherwise
  """
  pass
 def CanHaveRigidLinks(self):
  """
  CanHaveRigidLinks(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model supports Rigid Links.

   Returns: True if Analytical Model supports Rigid Links; false otherwise.
  """
  pass
 def CanUseHardPoints(self):
  """
  CanUseHardPoints(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model can use Hard Points.

   Returns: True if Analytical Model can use Hard Points,false otherwise.
  """
  pass
 def CloneAdjustment(self,source,end):
  """
  CloneAdjustment(self: AnalyticalModel,source: AnalyticalModel,end: int)

   The method clones the adjustment of one end of the AM on another AM,

     with 

    respect to the one of the ends.

     One of the Analytical Model ends
  """
  pass
 def Disconnect(self,selector):
  """
  Disconnect(self: AnalyticalModel,selector: AnalyticalElementSelector)

   Unjoin from Hub Element.

  

   selector: End of the analytical model.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def Enable(self,enable):
  """
  Enable(self: AnalyticalModel,enable: bool)

   Enables or disables Analytical Model,if the Element allows a one-operation 

    Analytical Model toggle.

  

  

   enable: Enable (true) or disable (false) Analytical Model.
  """
  pass
 def EnableAutoDetect(self,direction,enabled):
  """
  EnableAutoDetect(self: AnalyticalModel,direction: AnalyticalDirection,enabled: bool)

   Enable or disable Analytical Auto-detect.

  

   direction: Direction in which to enable Analytical Auto-detect

   enabled: Turn Analytical Auto-detect on (true) or off (false)
  """
  pass
 def GetAnalyticalModelSketchComponents(self):
  """
  GetAnalyticalModelSketchComponents(self: AnalyticalModel) -> IList[AnalyticalModelSketchComponent]

  

   Retrieves a collection of AnalyticalModelSketchComponent objects,which are 

    useful for those Analytical Models

     that have finer calibration below the 

    Element level.

  

   Returns: If the Analytical Model supports Sketch-based adjustment of the Analytical 

    Model,

     then this will return an array of AnalyticalModelSketchComponents.  

    Otherwise,it will

     return an empty array.
  """
  pass
 def GetAnalyticalModelSupports(self):
  """
  GetAnalyticalModelSupports(self: AnalyticalModel) -> IList[AnalyticalModelSupport]

  

   Retrieves the AnalyticalModelSupport array,which is useful to extract 

    Analytical

     Support Information from Elements.

  

   Returns: Array of AnalyticalModelSupport objects,each one representing a support.
  """
  pass
 def GetAnalyzeAs(self):
  """
  GetAnalyzeAs(self: AnalyticalModel) -> AnalyzeAs

  

   Returns value of Analyze As parameter for Analytical Model.

   Returns: AnalyzeAs enumeration,indicating how Analytical Model is analyzed.
  """
  pass
 def GetApproximationDeviation(self):
  """
  GetApproximationDeviation(self: AnalyticalModel) -> float

  

   Retrieves amount by which approximation is made.

   Returns: Maximum distance from approximated line to curve.

     If approximation does not 

    make sense,then this will be 0.0.
  """
  pass
 def GetAutoDetectMatchedElements(self,direction):
  """
  GetAutoDetectMatchedElements(self: AnalyticalModel,direction: AnalyticalDirection) -> ICollection[ElementId]

  

   Retrieves other Element Ids that this Element is Auto-detecting against.

  

   direction: Direction in which Analytical Auto-detect is being done.

   Returns: A set of Element Ids against which this Element is Auto-detecting.

     The set 

    may be empty if this Element is not Auto-detecting against anything.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetCurve(self):
  """
  GetCurve(self: AnalyticalModel) -> Curve

  

   Returns the single curve of the Analytical Model,if it is only one curve.

   Returns: Single curve of the Analytical Model.
  """
  pass
 def GetCurves(self,curveType):
  """
  GetCurves(self: AnalyticalModel,curveType: AnalyticalCurveType) -> IList[Curve]

  

   Retrieves all curves for the Analytical Model of a given type.

  

   curveType: Which curve type should be returned.

   Returns: An array of curves representing analytical model.
  """
  pass
 def GetElementId(self):
  """
  GetElementId(self: AnalyticalModel) -> ElementId

  

   Retrieves Element Id of the structural element corresponding to the Analytical 

    Model.

  

   Returns: Element Id for a structural element.
  """
  pass
 def GetLocalCoordinateSystem(self):
  """
  GetLocalCoordinateSystem(self: AnalyticalModel) -> Transform

  

   Gets the local coordinate system (LCS) for an analytical model element.

   Returns: Transformation matrix.

     Returns ll for analytical model elements that do not 

    have local coordinate system.

     Origin returned by transform is point for 

    which local coordinate system was calculated.
  """
  pass
 def GetManualAdjustmentMatchedElements(self):
  """
  GetManualAdjustmentMatchedElements(self: AnalyticalModel) -> ICollection[ElementId]

  

   Retrieves other Element Ids against which the Analytical Model has been 

    adjusted.

  

   Returns: Set of Element Ids,representing those Elements against which the Analytical 

    Model has been adjusted.

     The set may be empty if Analytical Model is not 

    participating in locked Manual Analytical Adjustment.
  """
  pass
 def GetOffset(self,selector):
  """
  GetOffset(self: AnalyticalModel,selector: AnalyticalElementSelector) -> XYZ

  

   Gets the offset of the analytical model at end.

  

   selector: End of the analytical model.

   Returns: Offset of analytical model from base analytical model at the given end.
  """
  pass
 def GetPoint(self):
  """
  GetPoint(self: AnalyticalModel) -> XYZ

  

   Retrieves point of the Analytical Model.

   Returns: Point of the Analytical Model.
  """
  pass
 def GetReference(self,selector):
  """
  GetReference(self: AnalyticalModel,selector: AnalyticalModelSelector) -> Reference

  

   Returns a reference to a given curve within the analytical model.

  

   selector: Specifies where in the analytical model the reference lies.

   Returns: Requested reference.
  """
  pass
 def GetRigidLink(self,selector):
  """
  GetRigidLink(self: AnalyticalModel,selector: AnalyticalModelSelector) -> Curve

  

   Returns rigid link curve corresponding to selector.

  

   selector: Identifies from which end of the analytical model to get the Rigid Link.

   Returns: Rigid link satisfying selector.
  """
  pass
 def HasDeletedLinks(self):
  """
  HasDeletedLinks(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model contains deleted Analytical Links.

   Returns: True if contains,false otherwise.
  """
  pass
 def HasRigidLinksWith(self,neighborId):
  """
  HasRigidLinksWith(self: AnalyticalModel,neighborId: ElementId) -> bool

  

   Indicates if Analytical Model has Rigid Links with specified element.

  

   neighborId: neighboring Element,to which Rigid Links may exist.

   Returns: true if Rigid Links exist,false otherwise.
  """
  pass
 def IsAnalyzeAsValid(self,analyzeAs):
  """
  IsAnalyzeAsValid(self: AnalyticalModel,analyzeAs: AnalyzeAs) -> bool

  

   Determines if the given Analyze As parameter is valid for this Element.

  

   analyzeAs: Indicates how Analytical Model is analyzed.

   Returns: True if valid; false otherwise.
  """
  pass
 def IsApproximated(self):
  """
  IsApproximated(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model is approximated or not.

   Returns: True if the Analytical Model is approximated,false otherwise.

     False if 

    approximation is meaningless for Analytical Model.
  """
  pass
 def IsAutoDetectEnabled(self,direction):
  """
  IsAutoDetectEnabled(self: AnalyticalModel,direction: AnalyticalDirection) -> bool

  

   Reports if Analytical Auto-detect for the given direction is enabled.

  

   direction: Direction in which Auto-detect behavior may be enabled.

   Returns: True if enabled in the given direction,false otherwise.
  """
  pass
 def IsElementFullySupported(self):
  """
  IsElementFullySupported(self: AnalyticalModel) -> bool

  

   Indicates if Analytical Model is fully supported.

   Returns: True if Analytical Model is fully supported,false otherwise.
  """
  pass
 def IsEnabled(self):
  """
  IsEnabled(self: AnalyticalModel) -> bool

  

   Reports whether the Analytical Model is enabled or disabled.

   Returns: True if Analytical Model is enabled,false otherwise.
  """
  pass
 def IsManuallyAdjusted(self):
  """
  IsManuallyAdjusted(self: AnalyticalModel) -> bool

  

   Indicates if the Analytical Model has been manually adjusted by the user.

   Returns: True if user has manually adjusted the Analytical Model; false otherwise.
  """
  pass
 def IsModified(self):
  """
  IsModified(self: AnalyticalModel) -> bool

  

   Checks if AM has been adjusted from auto-detect at any end.
  """
  pass
 def IsSingleCurve(self):
  """
  IsSingleCurve(self: AnalyticalModel) -> bool

  

   Indicates if the Analytical Model can be expressed as a single curve.

   Returns: True if Analytical Model can be expressed as a single curve,false otherwise.
  """
  pass
 def IsSinglePoint(self):
  """
  IsSinglePoint(self: AnalyticalModel) -> bool

  

   Indicates if the Analytical Model can be expressed as a single point.

   Returns: True if Analytical Model can be expressed as a single point,false otherwise.
  """
  pass
 def IsValidDirectionForAutoDetect(self,direction):
  """
  IsValidDirectionForAutoDetect(self: AnalyticalModel,direction: AnalyticalDirection) -> bool

  

   Tests if the supplied direction is valid for Analytical Auto-detect.

  

   direction: Direction in which Auto-detect behavior may be valid.

   Returns: True if direction is valid,false otherwise.
  """
  pass
 def IsValidForManualAdjustment(self,reference):
  """
  IsValidForManualAdjustment(self: AnalyticalModel,reference: Reference) -> bool

  

   Indicates if the identified reference is acceptable for Manual Analytical 

    Adjustment.

  

  

   reference: Reference that will be examined.

   Returns: True if reference can be used,false otherwise.
  """
  pass
 def IsValidManualAdjustmentSource(self,source,adjustmentDirection):
  """
  IsValidManualAdjustmentSource(self: AnalyticalModel,source: Reference,adjustmentDirection: AnalyticalDirection) -> bool

  

   Indicates if the identified reference is acceptable as a source for Manual 

    Analytical Adjustment.

  

  

   source: Reference to be examined.

   adjustmentDirection: Direction in which adjustment will occur.

   Returns: True if reference can be used as source; false otherwise.
  """
  pass
 def IsValidManualAdjustmentTarget(self,target,source,direction):
  """
  IsValidManualAdjustmentTarget(self: AnalyticalModel,target: Reference,source: Reference,direction: AnalyticalDirection) -> bool

  

   Indicates if reference is acceptable as a "Target" for Manual Analytical 

    Adjustment.

  

  

   target: Target reference.

   source: Source reference.  This is necessary to avoid illegal conditions.  For instance 

    if Element A

     is manually adjusted against Element B,Element B cannot in 

    general be adjusted against Element A.

  

   direction: Direction in which source Element can be adjusted against target Element.

   Returns: True if reference can be used,false otherwise.
  """
  pass
 def IsValidRigidLinksOption(self,rigidLinksOption):
  """
  IsValidRigidLinksOption(self: AnalyticalModel,rigidLinksOption: AnalyticalRigidLinksOption) -> bool

  

   Indicates if Rigid Links option is valid for the Analytical Model.

  

   rigidLinksOption: Rigid Links option to validate.

   Returns: True if option is valid,false otherwise.
  """
  pass
 def IsValidSelector(self,selector):
  """
  IsValidSelector(self: AnalyticalModel,selector: AnalyticalModelSelector) -> bool

  

   Indicates if the input selector is valid for the Analytical Model.

  

   selector: Portion of the analytical model geometry.

   Returns: True if selector is valid for this Analytical Model,false otherwise.
  """
  pass
 def ManuallyAdjust(self,source,target):
  """
  ManuallyAdjust(self: AnalyticalModel,source: Reference,target: Reference) -> bool

  

   Perform Manual Analytical Adjustment on analytical model,with respect to 

    another Element

  

  

   source: Which part of Analytical Model needs to change.

   target: Which part of another Analytical Model change should be made against.

   Returns: Indicates the successful completion of the Manual Analytical Adjustment 

    operation.

     True if source Element was adjusted successfully,false 

    otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def ResetLinks(self):
  """
  ResetLinks(self: AnalyticalModel)

   The function is trying to recreate analytical link elements that were deleted 

    by the user.
  """
  pass
 def ResetManualAdjustment(self):
  """
  ResetManualAdjustment(self: AnalyticalModel) -> bool

  

   Resets all manual adjustments performed by the user onto the Analytical Model.

   Returns: Indicates the successful reset of all manual adjustment.

     True if reset 

    succeeds,false otherwise.
  """
  pass
 def SetAnalyzeAs(self,analyzeAs):
  """
  SetAnalyzeAs(self: AnalyticalModel,analyzeAs: AnalyzeAs)

   Sets value of Analyze As parameter for this Element.

  

   analyzeAs: Indicates how Analytical Model is analyzed .
  """
  pass
 def SetApproximationDeviation(self,deviation):
  """
  SetApproximationDeviation(self: AnalyticalModel,deviation: float)

   Adjusts the amount by which approximation is made.

  

   deviation: Maximum distance from line to actual curve
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetOffset(self,selector,offset):
  """
  SetOffset(self: AnalyticalModel,selector: AnalyticalElementSelector,offset: XYZ)

   Sets the offset of the analytical model at end.

  

   selector: End of analytical model to offset.

   offset: New offset for end of analytical model.
  """
  pass
 def SetUsesHardPoints(self,hardPoints):
  """
  SetUsesHardPoints(self: AnalyticalModel,hardPoints: bool)

   Sets Hard Points for the Analytical Model.

  

   hardPoints: Enable/disable Hard Points (true=enable).
  """
  pass
 def SupportsManualAdjustment(self):
  """
  SupportsManualAdjustment(self: AnalyticalModel) -> bool

  

   Indicates if the Element supports Manual Analytical Adjustment.

   Returns: True if Manual Adjustment is possible,false otherwise.
  """
  pass
 def UsesHardPoints(self):
  """
  UsesHardPoints(self: AnalyticalModel) -> bool

  

   Indicates if the Analytical Model is using Hard Points during approximation.

   Returns: True if Hard Points are being used,false otherwise.

     False if Hard Points 

    are meaningless for Analytical Model.
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
 RigidLinksOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if parameters indicate if Rigid Links should be formed.



Get: RigidLinksOption(self: AnalyticalModel) -> AnalyticalRigidLinksOption



Set: RigidLinksOption(self: AnalyticalModel)=value

"""


