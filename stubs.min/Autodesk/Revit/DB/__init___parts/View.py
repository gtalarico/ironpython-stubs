class View(Element,IDisposable):
 """ Base class for all types of views in Autodesk Revit. """
 def AddFilter(self,filterElementId):
  """
  AddFilter(self: View,filterElementId: ElementId)
   Adds a filter to the view.
  
   filterElementId: ElementId of the filter.
  """
  pass
 def AllowsAnalysisDisplay(self):
  """
  AllowsAnalysisDisplay(self: View) -> bool
  
   Identifies if this view allows display of Analysis results.
   Returns: True if the view allows display of Analysis results,false otherwise.
  """
  pass
 def ApplyViewTemplateParameters(self,otherView):
  """
  ApplyViewTemplateParameters(self: View,otherView: View)
   Applies to this view the parameters of the input view that are not controlled 
    by the current view template.
  
  
   otherView: The view whose parameters are to be applied to this view.
     It does not have 
    to be a valid template (property IsTemplate can be true or false).
  """
  pass
 def AreGraphicsOverridesAllowed(self):
  """
  AreGraphicsOverridesAllowed(self: View) -> bool
  
   Determines if Visibility/Graphics Overriddes can be applied to the view.
   Returns: True if Overriddes can be applied to the view,false otherwise.
  """
  pass
 def CanCategoryBeHidden(self,elementId):
  """
  CanCategoryBeHidden(self: View,elementId: ElementId) -> bool
  
   Checks whether the category can be hidden in the view.
  
   elementId: ElementId of the category.
   Returns: True if the category can be hidden,false otherwise.
  """
  pass
 def CanCategoryBeHiddenTemporary(self,elementId):
  """
  CanCategoryBeHiddenTemporary(self: View,elementId: ElementId) -> bool
  
   Check if category can be temporarily hidden in the view.
  
   elementId: Id of the category to be checked
  """
  pass
 def CanEnableTemporaryViewPropertiesMode(self):
  """
  CanEnableTemporaryViewPropertiesMode(self: View) -> bool
  
   Indicates if Temporary View Properties mode can be applied for view in current 
    state.
  
   Returns: True if view can use Temporary View Properties mode in current state.
  """
  pass
 def CanModifyDetailLevel(self):
  """
  CanModifyDetailLevel(self: View) -> bool
  
   Check if Detail Level can be modified.
   Returns: True if Detail Level can be modified.
  """
  pass
 def CanModifyDisplayStyle(self):
  """
  CanModifyDisplayStyle(self: View) -> bool
  
   Indicates if DisplayStyle can be modified.
   Returns: True if DisplayStyle can be modified.
  """
  pass
 def CanModifyViewDiscipline(self):
  """
  CanModifyViewDiscipline(self: View) -> bool
  
   Indicates if the View Discipline can be modified
   Returns: True if View Discipline can be modified
  """
  pass
 def CanUseDepthCueing(self):
  """
  CanUseDepthCueing(self: View) -> bool
  
   Indicates if view can use Depth Cueing
   Returns: True if view can use Depth Cueing
  """
  pass
 def CanUseTemporaryVisibilityModes(self):
  """
  CanUseTemporaryVisibilityModes(self: View) -> bool
  
   Indicates if view can use temporary visibility modes
   Returns: True if view can use temporary visibility modes
  """
  pass
 def CanViewBeDuplicated(self,duplicateOption):
  """
  CanViewBeDuplicated(self: View,duplicateOption: ViewDuplicateOption) -> bool
  
   Identifies if this view can be duplicated.
  
   duplicateOption: The option to use when duplicating the view.
   Returns: True if the view can be duplicated,false otherwise.
  """
  pass
 def ConvertTemporaryHideIsolateToPermanent(self):
  """
  ConvertTemporaryHideIsolateToPermanent(self: View)
   Convert all temporary hidden elements or categories to permanently hidden in 
    view.
  """
  pass
 def ConvertToIndependent(self):
  """
  ConvertToIndependent(self: View)
   Convert the dependent view to independent.
  """
  pass
 def DisableTemporaryViewMode(self,mode):
  """
  DisableTemporaryViewMode(self: View,mode: TemporaryViewMode)
   Disables the specified temporary view mode.
  
   mode: The mode to disable.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def Duplicate(self,duplicateOption):
  """
  Duplicate(self: View,duplicateOption: ViewDuplicateOption) -> ElementId
  
   Duplicates this view.
  
   duplicateOption: The option to use when duplicating the view.
   Returns: The id of the newly created view.
  """
  pass
 def EnableRevealHiddenMode(self):
  """
  EnableRevealHiddenMode(self: View)
   Enables Reveal Hidden elements mode.
  """
  pass
 def EnableTemporaryViewPropertiesMode(self,viewTemplateId):
  """
  EnableTemporaryViewPropertiesMode(self: View,viewTemplateId: ElementId) -> bool
  
   Allow to enable or disable Temporary View Properties mode.
  
   viewTemplateId: ID of DBView that will be used to override current view settings.
     Provide 
    ElementId.InvalidElementId constant to disable Temporary View Properties mode.
  
   Returns: Returns true when DBView provided by viewTemplateId was applied and Temporary 
    View Properties was successfully started.
  """
  pass
 def GetBackground(self):
  """
  GetBackground(self: View) -> ViewDisplayBackground
  
   Returns the current background set for the view.
   Returns: Current background.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetCategoryHidden(self,categoryId):
  """
  GetCategoryHidden(self: View,categoryId: ElementId) -> bool
  
   Checks if elements of the given category are set to be invisible (hidden) in 
    this view.
  
  
   categoryId: The ID of the category.
   Returns: True if the category is invisible (hidden),false otherwise.
  """
  pass
 def GetCategoryOverrides(self,categoryId):
  """
  GetCategoryOverrides(self: View,categoryId: ElementId) -> OverrideGraphicSettings
  
   Gets graphic overrides for a category in view.
  
   categoryId: Category to be checked.
   Returns: Object representing all graphic overrides of the category categoryId in view. A 
    default OverrideGraphicSettings object will be returned if it not previously 
    been set for this view.
  """
  pass
 def GetCropRegionShapeManager(self):
  """
  GetCropRegionShapeManager(self: View) -> ViewCropRegionShapeManager
  
   Returns an object for managing view crop region shape.
   Returns: The crop region shape manager.
  """
  pass
 @staticmethod
 def GetCropRegionShapeManagerForReferenceCallout(doc,callout):
  """
  GetCropRegionShapeManagerForReferenceCallout(doc: Document,callout: ElementId) -> ViewCropRegionShapeManager
  
   Returns an object for managing view crop region shape for reference callout.
  
   doc: Document to which the callout belongs.
   callout: Element id of reference callout.
   Returns: The crop region shape manager.
  """
  pass
 def GetDependentViewIds(self):
  """
  GetDependentViewIds(self: View) -> ICollection[ElementId]
  
   Get the ids of dependent views.
   Returns: Ids of the dependent views.
  """
  pass
 def GetDepthCueing(self):
  """
  GetDepthCueing(self: View) -> ViewDisplayDepthCueing
  
   Returns the current depth cueing settings for the view.
   Returns: Current depth cueing settings.
  """
  pass
 def GetElementOverrides(self,elementId):
  """
  GetElementOverrides(self: View,elementId: ElementId) -> OverrideGraphicSettings
  
   Gets graphic overrides for an element in the view.
  
   elementId: The element.
   Returns: An object representing all graphic overrides of the element elementId in view.
  """
  pass
 def GetFilterOverrides(self,filterElementId):
  """
  GetFilterOverrides(self: View,filterElementId: ElementId) -> OverrideGraphicSettings
  
   Gets graphic overrides that a filter applies to the view.
  
   filterElementId: ElementId of the filter.
   Returns: Object representing all graphic overrides of the filter in the view.
  """
  pass
 def GetFilters(self):
  """
  GetFilters(self: View) -> ICollection[ElementId]
  
   Gets the filters applied to the view.
   Returns: The ElementIds of the Filters.
  """
  pass
 def GetFilterVisibility(self,filterElementId):
  """
  GetFilterVisibility(self: View,filterElementId: ElementId) -> bool
  
   Gets the visibility of the elements associated with a filter.
  
   filterElementId: The ElementId of the filter.
   Returns: True if the elements associated with the filter are visible in the view,false 
    otherwise.
  """
  pass
 def GetNonControlledTemplateParameterIds(self):
  """
  GetNonControlledTemplateParameterIds(self: View) -> ICollection[ElementId]
  
   Returns a list of parameters that are not marked as included when this view is 
    used as a template.
  
   Returns: The parameter ids that are not marked to be included.
  """
  pass
 def GetPointCloudOverrides(self):
  """
  GetPointCloudOverrides(self: View) -> PointCloudOverrides
  
   Returns point cloud overrides object for the view.
   Returns: Point cloud overrides for the view
  """
  pass
 def GetPrimaryViewId(self):
  """
  GetPrimaryViewId(self: View) -> ElementId
  
   Get the id of the primary view.
   Returns: The id of the primary view,or InvalidElementId if there is no primary view.
  """
  pass
 def GetReferenceCallouts(self):
  """
  GetReferenceCallouts(self: View) -> ICollection[ElementId]
  
   Returns element ids of all reference callouts in the view.
   Returns: Element ids of all reference callouts in the view.
  """
  pass
 def GetReferenceElevations(self):
  """
  GetReferenceElevations(self: View) -> ICollection[ElementId]
  
   Returns element ids of all reference elevations in the view.
   Returns: Element ids of all reference elevations in the view.
  """
  pass
 def GetReferenceSections(self):
  """
  GetReferenceSections(self: View) -> ICollection[ElementId]
  
   Returns element ids of all reference sections in the view.
   Returns: Element ids of all reference sections in the view.
  """
  pass
 def GetSketchyLines(self):
  """
  GetSketchyLines(self: View) -> ViewDisplaySketchyLines
  
   Returns the current sketchy lines settings for the view.
   Returns: Current sketchy lines settings.
  """
  pass
 def GetTemplateParameterIds(self):
  """
  GetTemplateParameterIds(self: View) -> IList[ElementId]
  
   Returns a list of parameter ids that may be controlled when this view is 
    assigned as a template.
  
   Returns: The parameter ids that may be controlled.
  """
  pass
 def GetTemporaryViewPropertiesId(self):
  """
  GetTemporaryViewPropertiesId(self: View) -> ElementId
  
   When Temporary View Properties mode is in progress it provides DBView ID that 
    overrode settings for current view.
     Outside Temporary View Properties mode 
    InvalidElementId will be returned.
  """
  pass
 def GetTemporaryViewPropertiesName(self):
  """
  GetTemporaryViewPropertiesName(self: View) -> str
  
   When Temporary View Properties mode is in progress,name of applied template is 
    returned.
     Outside Temporary View Properties mode,empty string will be 
    returned.
  """
  pass
 def GetViewDisplayModel(self):
  """
  GetViewDisplayModel(self: View) -> ViewDisplayModel
  
   Returns the current view display model settings for the view.
   Returns: Current view display model settings.
  """
  pass
 def GetVisibility(self,category):
  """
  GetVisibility(self: View,category: Category) -> bool
  
   Checks if elements of the given category are set to be visible in this view.
  
   category: The category.
   Returns: True if the category is visible,false otherwise.
  """
  pass
 def GetWorksetVisibility(self,worksetId):
  """
  GetWorksetVisibility(self: View,worksetId: WorksetId) -> WorksetVisibility
  
   Returns the visibility settings of a workset for this particular view.
  
   worksetId: Id of the workset.
   Returns: The visibility of a workset for this particular view.
  """
  pass
 def GetWorksharingDisplayMode(self):
  """
  GetWorksharingDisplayMode(self: View) -> WorksharingDisplayMode
  
   Gets the current worksharing display mode for this view.
   Returns: The active worksharing display mode in this view.
  """
  pass
 def HasDetailLevel(self):
  """
  HasDetailLevel(self: View) -> bool
  
   Check if the view has a Detail Level property
   Returns: True if the view has a Detail Level,false otherwise
  """
  pass
 def HasDisplayStyle(self):
  """
  HasDisplayStyle(self: View) -> bool
  
   Indicates if view has a DisplayStyle property
   Returns: True if view has a DisplayStyle property
  """
  pass
 def HasViewDiscipline(self):
  """
  HasViewDiscipline(self: View) -> bool
  
   Indicates if the view has a Discipline property
   Returns: True if the view has a Discipline property
  """
  pass
 def HideActiveWorkPlane(self):
  """
  HideActiveWorkPlane(self: View)
   Hide the active work plane of the view.
  """
  pass
 def HideCategoriesTemporary(self,elementIds):
  """ HideCategoriesTemporary(self: View,elementIds: ICollection[ElementId]) """
  pass
 def HideCategoryTemporary(self,elementId):
  """
  HideCategoryTemporary(self: View,elementId: ElementId)
   Set one category to be temporarily hidden in the view.
  
   elementId: Id of the category to be hidden
  """
  pass
 def HideElements(self,elementIdSet):
  """ HideElements(self: View,elementIdSet: ICollection[ElementId]) """
  pass
 def HideElementsTemporary(self,elementIdSet):
  """ HideElementsTemporary(self: View,elementIdSet: ICollection[ElementId]) """
  pass
 def HideElementTemporary(self,elementId):
  """
  HideElementTemporary(self: View,elementId: ElementId)
   Set one element to be temporarily hidden in the view.
  
   elementId: The id of the element to be temporarily hidden.
  """
  pass
 def IsCategoryOverridable(self,categoryId):
  """
  IsCategoryOverridable(self: View,categoryId: ElementId) -> bool
  
   Checks whether the category can have graphic overrides in this view.
  
   categoryId: ElementId of the category.
   Returns: True if category can be overridden,false otherwise.
  """
  pass
 def IsElementVisibleInTemporaryViewMode(self,mode,id):
  """
  IsElementVisibleInTemporaryViewMode(self: View,mode: TemporaryViewMode,id: ElementId) -> bool
  
   Identifies if the input element is visible for the temporary view mode for this 
    view.
  
  
   mode: The temporary view mode.  Only TemporaryHideIsolate and AnalyticalModel modes 
    are supported
     by this option.  Other modes will result in an exception.
  
   id: The element id.
   Returns: True if the element is visible,false if the element is hidden in the view mode.
  """
  pass
 def IsFilterApplied(self,filterElementId):
  """
  IsFilterApplied(self: View,filterElementId: ElementId) -> bool
  
   Indicates if a filter is applied to the view.
  
   filterElementId: ElementId of the filter.
   Returns: True if the filter is applied to the view,false otherwise.
  """
  pass
 def IsInTemporaryViewMode(self,mode):
  """
  IsInTemporaryViewMode(self: View,mode: TemporaryViewMode) -> bool
  
   Returns true if the view is in a particular temporary view mode.
  
   mode: The mode.
   Returns: True if this view is in the temporary view mode indicated,false otherwise.
  """
  pass
 def IsolateCategoriesTemporary(self,elementIds):
  """ IsolateCategoriesTemporary(self: View,elementIds: ICollection[ElementId]) """
  pass
 def IsolateCategoryTemporary(self,elementId):
  """
  IsolateCategoryTemporary(self: View,elementId: ElementId)
   Set one category to be temporarily isolated in the view.
  
   elementId: Id of category to be isolated.
  """
  pass
 def IsolateElementsTemporary(self,elementIds):
  """ IsolateElementsTemporary(self: View,elementIds: ICollection[ElementId]) """
  pass
 def IsolateElementTemporary(self,elementId):
  """
  IsolateElementTemporary(self: View,elementId: ElementId)
   Set one element to be temporarily isolated in the view.
  
   elementId: Id of element to be isolated.
  """
  pass
 def IsTemporaryHideIsolateActive(self):
  """
  IsTemporaryHideIsolateActive(self: View) -> bool
  
   Indicates if the view is temporarily hiding or isolating elements or categories.
   Returns: True if elements/categories are being temporarily hidden or isolated,false 
    otherwise.
  """
  pass
 def IsTemporaryViewPropertiesModeEnabled(self):
  """
  IsTemporaryViewPropertiesModeEnabled(self: View) -> bool
  
   Returns true when Temporary View Properties mode is in progress,false 
    otherwise.
  """
  pass
 @staticmethod
 def IsValidViewScale(viewScale):
  """
  IsValidViewScale(viewScale: int) -> bool
  
   This validator checks that the view scale is in the allowable range.
  
   viewScale: The denominator X in the view scale 1/X.
   Returns: True if the view scale is within the allowable range,false otherwise.
  """
  pass
 def IsValidViewTemplate(self,templateId):
  """
  IsValidViewTemplate(self: View,templateId: ElementId) -> bool
  
   Verifies that the view represented by templateId can be set as the controlling 
    view template for this view.
  
  
   templateId: The id to be validated as a view template for this view.
   Returns: True if the view is valid for us as a view template and compatible with this 
    view,or if it is InvalidElementId,false otherwise.
  """
  pass
 def IsWorksetVisible(self,worksetId):
  """
  IsWorksetVisible(self: View,worksetId: WorksetId) -> bool
  
   Indicates whether the workset is visible in this view.
  
   worksetId: Id of the workset.
   Returns: Whether the workset is visible.
  """
  pass
 def Print(self,*__args):
  """
  Print(self: View,viewTemplate: View,useCurrentPrintSettings: bool)
   Print this view with the given view template,and either the view's document's 
    print setting or the print setting of the current active document.
  
  
   viewTemplate: The view template which apply to the view.
   useCurrentPrintSettings: If true,print the view with the print setting of the current active document;
  
    otherwise with the view's document's print setting.
  
  Print(self: View,useCurrentPrintSettings: bool)
   Print this view with the default view template,and either the view's 
    document's print setting or the print setting of the current active document.
  
  
   useCurrentPrintSettings: If true,print the view with the print setting of the current active document;
  
    otherwise with the view's document's print setting.
  
  Print(self: View,viewTemplate: View)
   Print this view with the given view template and using the print setting of the 
    current active document.
  
  
   viewTemplate: The view template which apply to the view.
  Print(self: View)
   Print this view with the default view template and using the print setting of 
    the current active document.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveFilter(self,filterElementId):
  """
  RemoveFilter(self: View,filterElementId: ElementId)
   Removes a filter from the view.
  
   filterElementId: ElementId of the filter.
  """
  pass
 def SetBackground(self,background):
  """
  SetBackground(self: View,background: ViewDisplayBackground)
   Sets the background for the view.  Background can only be set for 3d views and 
    for Sections/Elevations.
  
  
   background: Background to set.  See 'ViewDisplayBackground' class and its 'create' methods.
  """
  pass
 def SetCategoryHidden(self,categoryId,hide):
  """
  SetCategoryHidden(self: View,categoryId: ElementId,hide: bool)
   Sets if elements of the given category will be visible in this view.
  
   categoryId: The ID of the category.
   hide: True to make elements of this category invisible,false to make them visible.
  """
  pass
 def SetCategoryOverrides(self,categoryId,overrideGraphicSettings):
  """
  SetCategoryOverrides(self: View,categoryId: ElementId,overrideGraphicSettings: OverrideGraphicSettings)
   Sets graphic overrides for a category in view.
  
   categoryId: Category to be overridden
   overrideGraphicSettings: Object representing all graphic overrides of the category categoryId in view.
  """
  pass
 def SetDepthCueing(self,depthCueing):
  """
  SetDepthCueing(self: View,depthCueing: ViewDisplayDepthCueing)
   Sets the depth cueing settings for the view.
  
   depthCueing: Depth cueing settings to set.
  """
  pass
 def SetElementOverrides(self,elementId,overrideGraphicSettings):
  """
  SetElementOverrides(self: View,elementId: ElementId,overrideGraphicSettings: OverrideGraphicSettings)
   Sets graphic overrides for an element in the view.
  
   elementId: Element to override.
   overrideGraphicSettings: An object representing all graphic overrides of the element in view.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetFilterOverrides(self,filterElementId,overrideGraphicSettings):
  """
  SetFilterOverrides(self: View,filterElementId: ElementId,overrideGraphicSettings: OverrideGraphicSettings)
   Sets the overrides associated with a filter.
  
   filterElementId: ElementId of the filter.
   overrideGraphicSettings: The overrides to apply to the filter.
  """
  pass
 def SetFilterVisibility(self,filterElementId,visibility):
  """
  SetFilterVisibility(self: View,filterElementId: ElementId,visibility: bool)
   Sets the visibility of the elements associated with a filter.
  
   filterElementId: The ElementId of the filter.
   visibility: True if the elements associated with the filter are visible in the view,false 
    otherwise.
  """
  pass
 def SetNonControlledTemplateParameterIds(self,newSet):
  """ SetNonControlledTemplateParameterIds(self: View,newSet: ICollection[ElementId]) """
  pass
 def SetSketchyLines(self,sketchyLines):
  """
  SetSketchyLines(self: View,sketchyLines: ViewDisplaySketchyLines)
   Sets the sketchy lines settings for the view.
  
   sketchyLines: Sketchy Lines settings to set.
  """
  pass
 def SetViewDisplayModel(self,viewDisplayModel):
  """
  SetViewDisplayModel(self: View,viewDisplayModel: ViewDisplayModel)
   Sets the view display model settings for the view.
  
   viewDisplayModel: View display model settings to set.
  """
  pass
 def SetVisibility(self,category,visible):
  """
  SetVisibility(self: View,category: Category,visible: bool)
   Sets if elements of the given category will be visible in this view.
  
   category: The category.
   visible: True to make elements of this category visible,false to make them invisible.
  """
  pass
 def SetWorksetVisibility(self,worksetId,visible):
  """
  SetWorksetVisibility(self: View,worksetId: WorksetId,visible: WorksetVisibility)
   Sets visibility for a workset in this view.
  
   worksetId: Id of the workset.
   visible: The visibility of the workset.
  """
  pass
 def SetWorksharingDisplayMode(self,displayMode):
  """
  SetWorksharingDisplayMode(self: View,displayMode: WorksharingDisplayMode)
   Sets the worksharing display mode for this view.
  
   displayMode: The desired display mode.  "Off" will turn off all worksharing display modes.
  """
  pass
 def ShowActiveWorkPlane(self):
  """
  ShowActiveWorkPlane(self: View)
   Show the active work plane of the view.
  """
  pass
 def SupportsRevealConstraints(self):
  """
  SupportsRevealConstraints(self: View) -> bool
  
   Checks that the view can have the Reveal Constraints mode activated.
   Returns: True if the view has a view type that allows Reveal Constraints mode to be 
    activated.
  """
  pass
 def SupportsWorksharingDisplayMode(self,mode):
  """
  SupportsWorksharingDisplayMode(self: View,mode: WorksharingDisplayMode) -> bool
  
   Checks whether this view supports the given worksharing display mode.
  
   mode: The mode of interest.
   Returns: Returns True if this view is a graphical view in a workshared document or if 
    the desired mode is Off.
     Returns False if this view is a non-graphical view 
    (such as a schedule or the project browser)
     or if this view is not in a 
    workshared document.
  """
  pass
 def UnhideElements(self,elementIdSet):
  """ UnhideElements(self: View,elementIdSet: ICollection[ElementId]) """
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
 AnalysisDisplayStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element id of Analysis Display Style associated with the view.

Get: AnalysisDisplayStyleId(self: View) -> ElementId

Set: AnalysisDisplayStyleId(self: View)=value
"""

 AreAnalyticalModelCategoriesHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if analytical model categories are currently hidden in the view.

Get: AreAnalyticalModelCategoriesHidden(self: View) -> bool

Set: AreAnalyticalModelCategoriesHidden(self: View)=value
"""

 AreAnnotationCategoriesHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if annotation categories are currently hidden in the view.

Get: AreAnnotationCategoriesHidden(self: View) -> bool

Set: AreAnnotationCategoriesHidden(self: View)=value
"""

 AreImportCategoriesHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if import categories are currently hidden in the view.

Get: AreImportCategoriesHidden(self: View) -> bool

Set: AreImportCategoriesHidden(self: View)=value
"""

 AreModelCategoriesHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if model categories are currently hidden in the view.

Get: AreModelCategoriesHidden(self: View) -> bool

Set: AreModelCategoriesHidden(self: View)=value
"""

 ArePointCloudsHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if point clouds are currently hidden in the view.

Get: ArePointCloudsHidden(self: View) -> bool

Set: ArePointCloudsHidden(self: View)=value
"""

 AssociatedAssemblyInstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the assembly instance that owns the assembly view.

Get: AssociatedAssemblyInstanceId(self: View) -> ElementId

"""

 CanBePrinted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Test whether the view can be printed.

Get: CanBePrinted(self: View) -> bool

"""

 CropBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Crop Box applied to the view,or an outline encompassing the crop region applied to the view.

Get: CropBox(self: View) -> BoundingBoxXYZ

Set: CropBox(self: View)=value
"""

 CropBoxActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not the Crop Box/Region is active for the view.

Get: CropBoxActive(self: View) -> bool

Set: CropBoxActive(self: View)=value
"""

 CropBoxVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not the Crop Box/Region is visible for the view.

Get: CropBoxVisible(self: View) -> bool

Set: CropBoxVisible(self: View)=value
"""

 DetailLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The detail level of this view.

Get: DetailLevel(self: View) -> ViewDetailLevel

Set: DetailLevel(self: View)=value
"""

 Discipline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Discipline of the view.

Get: Discipline(self: View) -> ViewDiscipline

Set: Discipline(self: View)=value
"""

 DisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The DisplayStyle of the view.
   Returns DisplayStyle.Wireframe if the view has no display style.

Get: DisplayStyle(self: View) -> DisplayStyle

Set: DisplayStyle(self: View)=value
"""

 GenLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The level for the view.

Get: GenLevel(self: View) -> Level

"""

 IsAssemblyView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the view is assembly view.

Get: IsAssemblyView(self: View) -> bool

"""

 IsTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Test whether the view is a view template.

Get: IsTemplate(self: View) -> bool

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the origin of the screen.

Get: Origin(self: View) -> XYZ

"""

 Outline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bounds of the view in paper space (in inches).

Get: Outline(self: View) -> BoundingBoxUV

"""

 PartsVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The visibility setting for parts in this view.

Get: PartsVisibility(self: View) -> PartsVisibility

Set: PartsVisibility(self: View)=value
"""

 RevealConstraintsMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the Reveal Constraints mode is activated in the view.

Get: RevealConstraintsMode(self: View) -> bool

Set: RevealConstraintsMode(self: View)=value
"""

 RightDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction towards the right side of the screen.

Get: RightDirection(self: View) -> XYZ

"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The scale of the view.

Get: Scale(self: View) -> int

Set: Scale(self: View)=value
"""

 ShadowIntensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The intesity of cast shadows - 0=no shadows,100=black.

Get: ShadowIntensity(self: View) -> int

Set: ShadowIntensity(self: View)=value
"""

 SketchPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sketch plane assigned to the view for model curve creation.

Get: SketchPlane(self: View) -> SketchPlane

Set: SketchPlane(self: View)=value
"""

 SunAndShadowSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sun and shadow settings assigned to the view for shadow calculation and rendering.

Get: SunAndShadowSettings(self: View) -> SunAndShadowSettings

"""

 SunlightIntensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The intensity of the simulated (directional) sunlight.  0=no directional light; maximum value is 100.

Get: SunlightIntensity(self: View) -> int

Set: SunlightIntensity(self: View)=value
"""

 TemporaryViewModes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Data of temporary view modes associated with this view.

Get: TemporaryViewModes(self: View) -> TemporaryViewModes

"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The view title. This consists of the view name plus other modifiers,such as the view type,
   sheet number,area scheme,and/or assembly type,depending on the specifics of the view.

Get: Title(self: View) -> str

"""

 UpDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction towards the top of the screen.

Get: UpDirection(self: View) -> XYZ

"""

 ViewDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The direction towards the viewer.

Get: ViewDirection(self: View) -> XYZ

"""

 ViewName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the view.

Get: ViewName(self: View) -> str

Set: ViewName(self: View)=value
"""

 ViewTemplateId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the template view that controls this view's parameters.

Get: ViewTemplateId(self: View) -> ElementId

Set: ViewTemplateId(self: View)=value
"""

 ViewType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of the view.

Get: ViewType(self: View) -> ViewType

"""


