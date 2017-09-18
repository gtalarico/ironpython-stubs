class Element(object,IDisposable):
 """ Base class for most persistent data within a Revit document. """
 def ArePhasesModifiable(self):
  """
  ArePhasesModifiable(self: Element) -> bool

  

   Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be 

    modified for this Element.

  

   Returns: True if the properties CreatedPhaseId and DemolishedPhaseId can be modified for 

    this Element,false otherwise.
  """
  pass
 def CanBeHidden(self,pView):
  """
  CanBeHidden(self: Element,pView: View) -> bool

  

   Indicates if the element can be hidden in the view.

   Returns: If the element is not permitted to be hidden,false is returned.
  """
  pass
 def CanBeLocked(self):
  """
  CanBeLocked(self: Element) -> bool

  

   Identifies if the element can be locked.

   Returns: True if the element can be locked,false otherwise.
  """
  pass
 def CanHaveAnalyticalModel(self):
  """
  CanHaveAnalyticalModel(self: Element) -> bool

  

   Indicates whether the Element can have an Analytical Model.

   Returns: True if the Element can have an Analytical Model,false otherwise.
  """
  pass
 @staticmethod
 def CanHaveTypeAssigned(document=None,elementIds=None):
  """
  CanHaveTypeAssigned(self: Element) -> bool

  

   Identifies if the element can have a type assigned.

   Returns: True if element can have a type assigned,false otherwise.

  CanHaveTypeAssigned(document: Document,elementIds: ICollection[ElementId]) -> bool
  """
  pass
 @staticmethod
 def ChangeTypeId(*__args):
  """
  ChangeTypeId(self: Element,typeId: ElementId) -> ElementId

  

   Changes the type of the element.

  

   typeId: Identifier of the type to assign to this element.

   Returns: The new element id if new element is created,or InvalidElementId if the 

    element's type changed without creating a new element.

  

  ChangeTypeId(document: Document,elementIds: ICollection[ElementId],typeId: ElementId) -> IDictionary[ElementId,ElementId]
  """
  pass
 def DeleteEntity(self,schema):
  """
  DeleteEntity(self: Element,schema: Schema) -> bool

  

   Deletes the existing entity created by %schema% in the element

  

   schema: Schema used for creation of the entity

   Returns: True if entity was deleted,false if entity didn't exist
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element) """
  pass
 def GetAnalyticalModel(self):
  """
  GetAnalyticalModel(self: Element) -> AnalyticalModel

  

   Retrieves writeable Analytical Model for Element.

   Returns: Writeable Analytical Model.
  """
  pass
 def GetAnalyticalModelId(self):
  """
  GetAnalyticalModelId(self: Element) -> ElementId

  

   Retrieves the Element Id of the Analytical Model Element for this Element.

   Returns: Element Id.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetChangeTypeAny():
  """
  GetChangeTypeAny() -> ChangeType

  

   Returns ChangeType associated with any change in an element.

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on any change in an element.
  """
  pass
 @staticmethod
 def GetChangeTypeElementAddition():
  """
  GetChangeTypeElementAddition() -> ChangeType

  

   Returns ChangeType associated with element addition

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on element addition.
  """
  pass
 @staticmethod
 def GetChangeTypeElementDeletion():
  """
  GetChangeTypeElementDeletion() -> ChangeType

  

   Returns ChangeType associated with element deletion.

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on element deletion.
  """
  pass
 @staticmethod
 def GetChangeTypeGeometry():
  """
  GetChangeTypeGeometry() -> ChangeType

  

   Returns ChangeType associated with a change in the geometry of an element

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on a geometry change in an element
  """
  pass
 @staticmethod
 def GetChangeTypeParameter(*__args):
  """
  GetChangeTypeParameter(param: Parameter) -> ChangeType

  

   Returns ChangeType associated with a change in a parameter's value

  

   param: Parameter for the ChangeType to trigger on

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on parameter value change

  

  GetChangeTypeParameter(parameterId: ElementId) -> ChangeType

  

   Returns ChangeType associated with a change in a parameter's value

  

   parameterId: ElementId of parameter for the ChangeType to trigger on.

   Returns: ChangeType that can be used to define a trigger for an Updater,

     triggering 

    on parameter value change.
  """
  pass
 def GetEntity(self,schema):
  """
  GetEntity(self: Element,schema: Schema) -> Entity

  

   Returns the existing entity corresponding to the Schema if it has been saved in 

    the

     Element,or an invalid entity otherwise.

  

  

   schema: The Schema describing the Entity.

   Returns: The returned Entity.
  """
  pass
 def GetEntitySchemaGuids(self):
  """
  GetEntitySchemaGuids(self: Element) -> IList[Guid]

  

   Returns the Schema guids of any Entities stored in this element.

   Returns: The schema Entity guids.
  """
  pass
 def GetExternalFileReference(self):
  """
  GetExternalFileReference(self: Element) -> ExternalFileReference

  

   Gets information pertaining to the external file referenced

     by the element.

   Returns: An object containing path and type information for the external

     file 

    referenced by the element.
  """
  pass
 def GetExternalResourceReference(self,resourceType):
  """
  GetExternalResourceReference(self: Element,resourceType: ExternalResourceType) -> ExternalResourceReference

  

   Gets the ExternalResourceReference associated with a specified external 

    resource type.

  

  

   resourceType: The desired external resource type.

   Returns: The copy of the ExternalResourceReference associated with a specified external 

    resource type.
  """
  pass
 def GetExternalResourceReferences(self):
  """
  GetExternalResourceReferences(self: Element) -> IDictionary[ExternalResourceType,ExternalResourceReference]

  

   Gets the full map of the external resource references referenced

     by the 

    element.

  

   Returns: The full map of the external resource references referenced by the element.
  """
  pass
 def GetGeneratingElementIds(self,geometryObject):
  """
  GetGeneratingElementIds(self: Element,geometryObject: GeometryObject) -> ICollection[ElementId]

  

   Returns the ids of the element(s) that generated the input geometry object.

  

   geometryObject: The geometry object whose generating element is requested.

   Returns: The id(s) of the element(s) that generated (or may have generated) the given 

    geometry object.  Empty if no generating elements are found. If the set 

    contains just one id,it is the id of the element that generated the geometry 

    object.
  """
  pass
 def GetGeometryObjectFromReference(self,reference):
  """
  GetGeometryObjectFromReference(self: Element,reference: Reference) -> GeometryObject

  

   Retrieve one geometric primitive contained in the element given a reference.

  

   reference: The geometric object referenced by this instance will be retrieved from the 

    model.

  

   Returns: The geometric object referenced by the input reference.
  """
  pass
 def GetMaterialArea(self,materialId,usePaintMaterial):
  """
  GetMaterialArea(self: Element,materialId: ElementId,usePaintMaterial: bool) -> float

  

   Gets the area of the material with the given id.

  

   materialId: The material id returned from 

    Autodesk.Revit.DB.Element.GetMaterialIds(System.Boolean).

  

   usePaintMaterial: If true,this material id was returned as a paint material from 

    Autodesk.Revit.DB.Element.GetMaterialIds(System.Boolean) and the area returned 

    should be calculated from paint applied to the element.

     If false,this 

    material id was returned as a non-paint element material from 

    Autodesk.Revit.DB.Element.GetMaterialIds(System.Boolean) and the area is 

    calculated from the element geometry and layers.

  

   Returns: The area of the material for this element.  Returns 0.0 if the material id is 

    not a part of this element.
  """
  pass
 def GetMaterialIds(self,returnPaintMaterials):
  """
  GetMaterialIds(self: Element,returnPaintMaterials: bool) -> ICollection[ElementId]

  

   Gets the element ids of all materials present in the element.

  

   returnPaintMaterials: If true,this returns material ids assigned to element faces by the Paint 

    tools.  If false,this returns ids associated to the material through

     its 

    geometry or compound structure layers.

  

   Returns: The set of material ids.
  """
  pass
 def GetMaterialVolume(self,materialId):
  """
  GetMaterialVolume(self: Element,materialId: ElementId) -> float

  

   Gets the volume of the material with the given id.

  

   materialId: The material id returned from 

    Autodesk.Revit.DB.Element.GetMaterialIds(System.Boolean).

  

   Returns: The volume of the material for this element.  Returns 0.0 if the material is 

    not a part of this element.
  """
  pass
 def GetMonitoredLinkElementIds(self):
  """
  GetMonitoredLinkElementIds(self: Element) -> IList[ElementId]

  

   Provides the link instance IDs when the element is monitoring.

   Returns: The IDs of linked instances.
  """
  pass
 def GetMonitoredLocalElementIds(self):
  """
  GetMonitoredLocalElementIds(self: Element) -> IList[ElementId]

  

   Provides the local element IDs when the element is monitoring.

   Returns: The IDs of local element IDs being monitored by this element.
  """
  pass
 def GetOrderedParameters(self):
  """
  GetOrderedParameters(self: Element) -> IList[Parameter]

  

   Gets the parameters associated to the element in order.

   Returns: A collection containing all parameters.
  """
  pass
 def GetParameterFormatOptions(self,parameterId):
  """
  GetParameterFormatOptions(self: Element,parameterId: ElementId) -> FormatOptions

  

   Returns a FormatOptions override for the element Parameter,or a default 

    FormatOptions if no override exists.

  

  

   parameterId: Id of parameter for which FormatOptions will be returned.

   Returns: Format options of element parameter. If the UseDefault property is true,then 

    no formatting overrides have been defined in the element for the specified 

    parameter,and the FormatOptions for the parameter should be obtained from the 

    Unit object,which can be obtained from the Document.
  """
  pass
 def GetParameters(self,name):
  """
  GetParameters(self: Element,name: str) -> IList[Parameter]

  

   Retrieves the parameters from the element via the given name.

  

   name: The name of the parameter to be retrieved.

   Returns: A collection containing the parameters having the same given parameter name.
  """
  pass
 def GetPhaseStatus(self,phaseId):
  """
  GetPhaseStatus(self: Element,phaseId: ElementId) -> ElementOnPhaseStatus

  

   Gets the status of a given element in the input phase

  

   phaseId: Id of the phase.

   Returns: The status of the element in the phase.
  """
  pass
 def GetTypeId(self):
  """
  GetTypeId(self: Element) -> ElementId

  

   Returns the identifier of this element's type.

   Returns: The id of the element's type,or invalid element id if the element cannot have 

    type assigned.
  """
  pass
 @staticmethod
 def GetValidTypes(document=None,elementIds=None):
  """
  GetValidTypes(self: Element) -> ICollection[ElementId]

  

   Obtains a set of types that are valid for this element.

   Returns: A set of element IDs of types that are valid for this element or an empty set 

    if element cannot have type assigned.

  

  GetValidTypes(document: Document,elementIds: ICollection[ElementId]) -> ICollection[ElementId]
  """
  pass
 def HasPhases(self):
  """
  HasPhases(self: Element) -> bool

  

   Returns true if this Element has the properties CreatedPhaseId and 

    DemolishedPhaseId.

  

   Returns: True if this Element has the properties CreatedPhaseId and DemolishedPhaseId,

    false otherwise.
  """
  pass
 def IsExternalFileReference(self):
  """
  IsExternalFileReference(self: Element) -> bool

  

   Determines whether this Element represents an external

     file.

   Returns: True if this element contains information about some external

     file,false 

    if it does not.
  """
  pass
 def IsHidden(self,pView):
  """
  IsHidden(self: Element,pView: View) -> bool

  

   Identifies if the element has been permanently hidden in the view.
  """
  pass
 def IsMonitoringLinkElement(self):
  """
  IsMonitoringLinkElement(self: Element) -> bool

  

   Indicate whether an element is monitoring any elements in any linked models.

   Returns: True if this element is monitoring elements in a linked models. Otherwise,

    false will be returned.
  """
  pass
 def IsMonitoringLocalElement(self):
  """
  IsMonitoringLocalElement(self: Element) -> bool

  

   Indicate whether an element is monitoring other local elements.

   Returns: True if this element is monitoring other elements in same project. Otherwise,

    false will be returned.
  """
  pass
 def IsPhaseCreatedValid(self,createdPhaseId):
  """
  IsPhaseCreatedValid(self: Element,createdPhaseId: ElementId) -> bool

  

   Returns true if createdPhaseId is an allowed value for the property 

    CreatedPhaseId in this Element.

  

  

   createdPhaseId: The id of a Phase.

   Returns: True if createdPhaseId is an allowed value for the property CreatedPhaseId in 

    this Element,false otherwise.
  """
  pass
 def IsPhaseDemolishedValid(self,demolishedPhaseId):
  """
  IsPhaseDemolishedValid(self: Element,demolishedPhaseId: ElementId) -> bool

  

   Returns true if demolishedPhaseId is an allowed value for the property 

    DemolishedPhaseId in this Element.

  

  

   demolishedPhaseId: The id of a Phase or invalidElementId.

   Returns: True if demolishedPhaseId is an allowed value for the property 

    DemolishedPhaseId in this Element,false otherwise.
  """
  pass
 @staticmethod
 def IsValidType(*__args):
  """
  IsValidType(self: Element,typeId: ElementId) -> bool

  

   Checks if given type is valid for this element.

  

   typeId: ElementId of the type to check.

   Returns: True if element can have a type assigned and this type is valid for this 

    element,false otherwise.

  

  IsValidType(document: Document,elementIds: ICollection[ElementId],typeId: ElementId) -> bool
  """
  pass
 def LookupParameter(self,name):
  """
  LookupParameter(self: Element,name: str) -> Parameter

  

   Attempts to find a parameter on the element which has the given name.

  

   name: The name of the parameter to be retrieved.

   Returns: The matching parameter. This return may be ll if there is no matching 

    parameter. If there are multiple matching parameters the first one found is 

    returned.
  """
  pass
 def RefersToExternalResourceReference(self,resourceType):
  """
  RefersToExternalResourceReference(self: Element,resourceType: ExternalResourceType) -> bool

  

   Determines whether this Element uses external resources associated with

     a 

    specified external resource type.

  

  

   resourceType: The desired external resource type.

   Returns: Returns true if this Element uses external resources associated with

     the 

    specified external resource type; otherwise,false.
  """
  pass
 def RefersToExternalResourceReferences(self):
  """
  RefersToExternalResourceReferences(self: Element) -> bool

  

   Determines whether this Element uses external resources.

   Returns: True if this element uses external resources,false if it does not.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetEntity(self,entity):
  """
  SetEntity(self: Element,entity: Entity)

   Stores the entity in the element. If an Entity described by the same Schema 

    already

     exists,it is overwritten.

  

  

   entity: The Entity to be stored.
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
 AssemblyInstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the assembly instance to which the element belongs.



Get: AssemblyInstanceId(self: Element) -> ElementId



"""

 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves a Category object that represents the category or sub category in which the

element resides.



Get: Category(self: Element) -> Category



"""

 CreatedPhaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of a Phase at which the Element was created.



Get: CreatedPhaseId(self: Element) -> ElementId



Set: CreatedPhaseId(self: Element)=value

"""

 DemolishedPhaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of a Phase at which the Element was demolished.



Get: DemolishedPhaseId(self: Element) -> ElementId



Set: DemolishedPhaseId(self: Element)=value

"""

 DesignOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the design option to which the element belongs.



Get: DesignOption(self: Element) -> DesignOption



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Document in which the Element resides.



Get: Document(self: Element) -> Document



"""

 GroupId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the group to which an element belongs.



Get: GroupId(self: Element) -> ElementId



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A unique identifier for an Element in an Autodesk Revit project.



Get: Id(self: Element) -> ElementId



"""

 IsTransient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether an element is transient or permanent.



Get: IsTransient(self: Element) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: Element) -> bool



"""

 LevelId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the level associated with the element.



Get: LevelId(self: Element) -> ElementId



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to find the physical location of an element within a project.



Get: Location(self: Element) -> Location



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A human readable name for the Element.



Get: Name(self: Element) -> str



Set: Name(self: Element)=value

"""

 OwnerViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the view that owns the element.



Get: OwnerViewId(self: Element) -> ElementId



"""

 Parameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves a set containing all of the parameters that are contained within the element.



Get: Parameters(self: Element) -> ParameterSet



"""

 ParametersMap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves a map containing all of the parameters that are contained within the element.



Get: ParametersMap(self: Element) -> ParameterMap



"""

 Pinned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the element has been pinned to prevent changes.



Get: Pinned(self: Element) -> bool



Set: Pinned(self: Element)=value

"""

 UniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A stable unique identifier for an element within the document.



Get: UniqueId(self: Element) -> str



"""

 ViewSpecific=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the element is owned by a view.



Get: ViewSpecific(self: Element) -> bool



"""

 WorksetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get Id of the Workset which owns the element.



Get: WorksetId(self: Element) -> WorksetId



"""


