class RhinoObject(object):
 """
 Represents an object in the document.

    RhinoObjects should only ever be creatable by the RhinoDoc.
 """
 def CommitChanges(self):
  """
  CommitChanges(self: RhinoObject) -> bool

  

   Moves changes made to this RhinoObject into the RhinoDoc.

   Returns: true if changes were made.
  """
  pass
 def CreateMeshes(self,meshType,parameters,ignoreCustomParameters):
  """
  CreateMeshes(self: RhinoObject,meshType: MeshType,parameters: MeshingParameters,ignoreCustomParameters: bool) -> int

  

   Create meshes used to render and analyze surface and polysrf objects.

  

   meshType: type of meshes to create

   parameters: in parameters that control the quality of the meshes that are created

   ignoreCustomParameters: Default should be false. Should the object ignore any custom meshing

     parameters on 

    the object's attributes

  

   Returns: number of meshes created
  """
  pass
 def DuplicateGeometry(self):
  """
  DuplicateGeometry(self: RhinoObject) -> GeometryBase

  

   Constructs a deep (full) copy of the geometry.

   Returns: A copy of the internal geometry.
  """
  pass
 def EnableCustomGrips(self,customGrips):
  """
  EnableCustomGrips(self: RhinoObject,customGrips: CustomObjectGrips) -> bool

  

   Turns on/off the object's editing grips.

  

   customGrips: The custom object grips.

   Returns: true if the call succeeded.  If you attempt to add custom grips to an

     object that 

    does not support custom grips,then false is returned.
  """
  pass
 def EnableVisualAnalysisMode(self,mode,enable):
  """
  EnableVisualAnalysisMode(self: RhinoObject,mode: VisualAnalysisMode,enable: bool) -> bool

  

   Used to turn analysis modes on and off.

  

   mode: A visual analysis mode.

   enable: true if the mode should be activated; false otherwise.

   Returns: true if this object supports the analysis mode.
  """
  pass
 def GetActiveVisualAnalysisModes(self):
  """
  GetActiveVisualAnalysisModes(self: RhinoObject) -> Array[VisualAnalysisMode]

  

   Gets a list of currently enabled analysis modes for this object.

   Returns: An array of visual analysis modes. The array can be empty,but not null.
  """
  pass
 def GetDynamicTransform(self,transform):
  """
  GetDynamicTransform(self: RhinoObject) -> (bool,Transform)

  

   While an object is being dynamically tranformed (dragged,rotated,...),

     the 

    current transformation can be retrieved and used for creating

     dynamic display.

  

   Returns: True if the object is being edited and its transformation

     is available.  False if 

    the object is not being edited,

     in which case the identity xform is returned.
  """
  pass
 def GetGrips(self):
  """
  GetGrips(self: RhinoObject) -> Array[GripObject]

  

   Returns grips for this object If grips are enabled. If grips are not

     enabled,

    returns null.

  

   Returns: An array of grip objects; or null if there are no grips.
  """
  pass
 def GetGroupList(self):
  """
  GetGroupList(self: RhinoObject) -> Array[int]

  

   Allocates an array of group indices of length GroupCount.

     If 

    Rhino.DocObjects.RhinoObject.GroupCount is 0,then this method returns null.

  

   Returns: An array of group indices,or null if Rhino.DocObjects.RhinoObject.GroupCount is 0.
  """
  pass
 def GetHighlightedSubObjects(self):
  """
  GetHighlightedSubObjects(self: RhinoObject) -> Array[ComponentIndex]

  

   Gets a list of all highlighted subobjects.

   Returns: An array of all highlighted subobjects; or null is there are none.
  """
  pass
 def GetMaterial(self,frontMaterial):
  """
  GetMaterial(self: RhinoObject,frontMaterial: bool) -> Material

  

   Gets material that this object uses based on it's attributes and the document

     that 

    the object is associated with.  In the rare case that a document is not

     associated 

    with this object,null will be returned.

  

  

   frontMaterial: If true,gets the material used to render the object's front side
  """
  pass
 def GetMeshes(self,meshType):
  """
  GetMeshes(self: RhinoObject,meshType: MeshType) -> Array[Mesh]

  

   Get existing meshes used to render and analyze surface and polysrf objects.
  """
  pass
 def GetRenderMaterial(self,frontMaterial):
  """
  GetRenderMaterial(self: RhinoObject,frontMaterial: bool) -> RenderMaterial

  

   Gets the RenderMaterial that this object uses based on it's attributes

     and the 

    document that the object is associated with. If there is no 

     RenderMaterial 

    associated with this object then null is returned.  If

     null is returned you should 

    call GetMaterial to get the material used

     to render this object.

  

  

   frontMaterial: If true,gets the material used to render the object's front side

     otherwise; gets 

    the material used to render the back side of the

     object.

  

   Returns: If there is a RenderMaterial associated with this objects' associated

     Material then 

    it is returned otherwise; null is returned.
  """
  pass
 @staticmethod
 def GetRenderMeshes(rhinoObjects,okToCreate,returnAllObjects):
  """ GetRenderMeshes(rhinoObjects: IEnumerable[RhinoObject],okToCreate: bool,returnAllObjects: bool) -> Array[ObjRef] """
  pass
 def GetRenderMeshParameters(self):
  """
  GetRenderMeshParameters(self: RhinoObject) -> MeshingParameters

  

   Meshing parameters that this object uses for generating render meshes. If the

     

    object's attributes do not have custom meshing parameters,then the document's

     

    meshing parameters are used.
  """
  pass
 def GetRenderPrimitiveList(self,viewport,preview):
  """
  GetRenderPrimitiveList(self: RhinoObject,viewport: ViewportInfo,preview: bool) -> RenderPrimitiveList

  

   Build custom render mesh(es) for this object.

  

   viewport: The viewport being rendered.

   preview: Type of mesh to build,if preview is true then a smaller mesh may be

     generated in 

    less time,false is meant when actually rendering.

  

   Returns: Returns a RenderPrimitiveList if successful otherwise returns null.
  """
  pass
 def GetSelectedSubObjects(self):
  """
  GetSelectedSubObjects(self: RhinoObject) -> Array[ComponentIndex]

  

   Get a list of all selected sub-objects.

   Returns: An array of subobject indices,or null if there are none.
  """
  pass
 def GetSubObjects(self):
  """
  GetSubObjects(self: RhinoObject) -> Array[RhinoObject]

  

   Gets an array of sub-objects.

   Returns: An array of subobjects,or null if there are none.
  """
  pass
 def GetTextureChannels(self):
  """
  GetTextureChannels(self: RhinoObject) -> Array[int]

  

   Get a list of the texture mapping channel Id's associated with object.

   Returns: Returns an array of channel Id's or an empty list if there are not mappings.
  """
  pass
 def GetTextureMapping(self,channel,objectTransform=None):
  """
  GetTextureMapping(self: RhinoObject,channel: int) -> (TextureMapping,Transform)

  

   Get objects texture mapping

  GetTextureMapping(self: RhinoObject,channel: int) -> TextureMapping
  """
  pass
 def Highlight(self,enable):
  """
  Highlight(self: RhinoObject,enable: bool) -> bool

  

   Modifies the highlighting of the object.

  

   enable: true if highlighting should be enabled.

   Returns: true if the object is now highlighted.
  """
  pass
 def HighlightSubObject(self,componentIndex,highlight):
  """
  HighlightSubObject(self: RhinoObject,componentIndex: ComponentIndex,highlight: bool) -> bool

  

   Highlights a subobject.

  

   componentIndex: A subobject component index.

   highlight: true if the subobject should be highlighted.

   Returns: true if the subobject is now highlighted.
  """
  pass
 def InVisualAnalysisMode(self,mode=None):
  """
  InVisualAnalysisMode(self: RhinoObject,mode: VisualAnalysisMode) -> bool

  

   Reports if a visual analysis mode is currently active for an object.

  

   mode: The mode to check for.

     Use null if you want to see if any mode is active.

   Returns: true if the specified analysis mode is active; otherwise false.

  InVisualAnalysisMode(self: RhinoObject) -> bool

  

   Reports if any visual analysis mode is currently active for an object.

   Returns: true if an analysis mode is active; otherwise false.
  """
  pass
 def IsActiveInViewport(self,viewport):
  """
  IsActiveInViewport(self: RhinoObject,viewport: RhinoViewport) -> bool

  

   Determine if this object is active in a particular viewport.

   Returns: True if the object is active in viewport
  """
  pass
 def IsHighlighted(self,checkSubObjects):
  """
  IsHighlighted(self: RhinoObject,checkSubObjects: bool) -> int

  

   Check highlight state.

  

   checkSubObjects: If true and the entire object is not highlighted,and some subset of the object

     is 

    highlighted,like some edges of a surface,then 3 is returned.

     If false and the 

    entire object is not highlighted,then zero is returned.

  

   Returns: 0: object is not highlighted.1: entire object is highlighted.3: one or more proper sub-objects 

    are highlighted.
  """
  pass
 def IsMeshable(self,meshType):
  """
  IsMeshable(self: RhinoObject,meshType: MeshType) -> bool

  

   Returns true if the object is capable of having a mesh of the specified type
  """
  pass
 def IsSelectable(self,ignoreSelectionState=None,ignoreGripsState=None,ignoreLayerLocking=None,ignoreLayerVisibility=None):
  """
  IsSelectable(self: RhinoObject) -> bool

  

   Reports if an object can be selected.

   Returns: true if object is capable of being selected.

  IsSelectable(self: RhinoObject,ignoreSelectionState: bool,ignoreGripsState: bool,ignoreLayerLocking: bool,ignoreLayerVisibility: bool) -> bool

  

   Reports if an object can be selected.

  

   ignoreSelectionState: If true,then selected objects are selectable.

     If false,then selected objects are 

    not selectable.

  

   ignoreGripsState: If true,then objects with grips on can be selected.

     If false,then the value 

    returned by the object's IsSelectableWithGripsOn() function decides if the object can be 

    selected.

  

   ignoreLayerLocking: If true,then objects on locked layers are selectable.

     If false,then objects on 

    locked layers are not selectable.

  

   ignoreLayerVisibility: If true,then objects on hidden layers are selectable.

     If false,then objects on 

    hidden layers are not selectable.

  

   Returns: true if object is capable of being selected.
  """
  pass
 def IsSelected(self,checkSubObjects):
  """
  IsSelected(self: RhinoObject,checkSubObjects: bool) -> int

  

   Check selection state.

  

   checkSubObjects: (false is good default)

     If true and the entire object is not selected,and some 

    subset of the object

     is selected,like some edges of a surface,then 3 is returned.


    
     If false and the entire object is not selected,then zero is returned.

  

   Returns: 0=object is not selected.

     1=object is selected.

     2=entire object 

    is selected persistently.

     3=one or more proper sub-objects are selected.
  """
  pass
 def IsSubObjectHighlighted(self,componentIndex):
  """
  IsSubObjectHighlighted(self: RhinoObject,componentIndex: ComponentIndex) -> bool

  

   Determines if a subobject is highlighted.

  

   componentIndex: A subobject component index.

   Returns: true if the subobject is highlighted.
  """
  pass
 def IsSubObjectSelectable(self,componentIndex,ignoreSelectionState):
  """
  IsSubObjectSelectable(self: RhinoObject,componentIndex: ComponentIndex,ignoreSelectionState: bool) -> bool

  

   Reports if a subobject can be selected.

  

   componentIndex: index of subobject to check.

   ignoreSelectionState: If true,then selected objects are selectable.

     If false,then selected objects are 

    not selectable.

  

   Returns: true if the specified subobject can be selected.
  """
  pass
 def IsSubObjectSelected(self,componentIndex):
  """
  IsSubObjectSelected(self: RhinoObject,componentIndex: ComponentIndex) -> bool

  

   Check sub-object selection state.

  

   componentIndex: Index of subobject to check.

   Returns: true if the subobject is selected.
  """
  pass
 def MemoryEstimate(self):
  """
  MemoryEstimate(self: RhinoObject) -> UInt32

  

   Computes an estimate of the number of bytes that this object is using in memory.

     

    Note that this is a runtime memory estimate and does not directly compare to the

     

    amount of space take up by the object when saved to a file.

  

   Returns: The estimated number of bytes this object occupies in memory.
  """
  pass
 def MeshCount(self,meshType,parameters):
  """
  MeshCount(self: RhinoObject,meshType: MeshType,parameters: MeshingParameters) -> int

  

   RhinoObjects can have several different types of meshes and 

     different numbers of 

    meshes.  A b-rep can have a render and 

     an analysis mesh on each face.  A mesh 

    object has a single 

     render mesh and no analysis mesh. Curve,point,and annotation


    
     objects have no meshes.

  

  

   meshType: type of mesh to count

   parameters: if not null and if the object can change its mesh (like a brep),

     then only meshes 

    that were created with these mesh parameters are counted.

  

   Returns: number of meshes
  """
  pass
 @staticmethod
 def MeshObjects(rhinoObjects,parameters,*__args):
  """
  MeshObjects(rhinoObjects: IEnumerable[RhinoObject],parameters: MeshingParameters,simpleDialog: bool) -> (Result,MeshingParameters,bool,Array[Mesh],Array[ObjectAttributes])

  MeshObjects(rhinoObjects: IEnumerable[RhinoObject],parameters: MeshingParameters) -> (Result,Array[Mesh],Array[ObjectAttributes])
  """
  pass
 def OnAddToDocument(self,*args):
  """
  OnAddToDocument(self: RhinoObject,doc: RhinoDoc)

   This call informs an object it is about to be added to the list of

     active objects 

    in the document.
  """
  pass
 def OnDeleteFromDocument(self,*args):
  """
  OnDeleteFromDocument(self: RhinoObject,doc: RhinoDoc)

   This call informs an object it is about to be deleted.

     Some objects,like clipping 

    planes,need to do a little extra cleanup

     before they are deleted.
  """
  pass
 def OnDraw(self,*args):
  """
  OnDraw(self: RhinoObject,e: DrawEventArgs)

   Called when Rhino wants to draw this object
  """
  pass
 def OnDuplicate(self,*args):
  """
  OnDuplicate(self: RhinoObject,source: RhinoObject)

   Called when this a new instance of this object is created and copied from

     an 

    existing object
  """
  pass
 def OnPick(self,*args):
  """
  OnPick(self: RhinoObject,context: PickContext) -> IEnumerable[ObjRef]

  

   Called to determine if this object or some sub-portion of this object should be

     

    picked given a pick context.
  """
  pass
 def OnPicked(self,*args):
  """ OnPicked(self: RhinoObject,context: PickContext,pickedItems: IEnumerable[ObjRef]) """
  pass
 def OnSelectionChanged(self,*args):
  """
  OnSelectionChanged(self: RhinoObject)

   Called when the selection state of this object has changed
  """
  pass
 def OnSpaceMorph(self,*args):
  """
  OnSpaceMorph(self: RhinoObject,morph: SpaceMorph)

   Called when a space morph has been applied to the geometry.

     Currently this only 

    works for CustomMeshObject instances
  """
  pass
 def OnTransform(self,*args):
  """
  OnTransform(self: RhinoObject,transform: Transform)

   Called when a transformation has been applied to the geometry
  """
  pass
 def Select(self,on,syncHighlight=None,persistentSelect=None,ignoreGripsState=None,ignoreLayerLocking=None,ignoreLayerVisibility=None):
  """
  Select(self: RhinoObject,on: bool,syncHighlight: bool) -> int

  

   Selects an object.

  

   on: The new selection state; true activates selection.

   syncHighlight: If true,then the object is hightlighted if it is selected

     and not hightlighted if 

    is is not selected.

     Highlighting can be and stay out of sync,as its specification 

    is independent.

  

   Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.

  Select(self: RhinoObject,on: bool) -> int

  

   Selects an object.

  

   on: The new selection state; true activates selection.

   Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.

  Select(self: RhinoObject,on: bool,syncHighlight: bool,persistentSelect: bool,ignoreGripsState: bool,ignoreLayerLocking: bool,ignoreLayerVisibility: bool) -> int

  

   Selects an object.

  

   on: The new selection state; true activates selection.

   syncHighlight: If true,then the object is highlighted if it is selected 

     and unhighlighted if is 

    is not selected.

     Highlighting can be and stay out of sync,as its specification is 

    independent.

  

   persistentSelect: Objects that are persistently selected stay selected when a command terminates.

   ignoreGripsState: If true,then objects with grips on can be selected.

     If false,then the value 

    returned by the object's IsSelectableWithGripsOn() function

     decides if the object 

    can be selected when it has grips turned on.

  

   ignoreLayerLocking: If true,then objects on locked layers can be selected.

     If false,then objects on 

    locked layers cannot be selected.

  

   ignoreLayerVisibility: If true,then objects on hidden layers can be selectable.

     If false,then objects on 

    hidden layers cannot be selected.

  

   Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.
  """
  pass
 def SelectSubObject(self,componentIndex,select,syncHighlight):
  """
  SelectSubObject(self: RhinoObject,componentIndex: ComponentIndex,select: bool,syncHighlight: bool) -> int

  

   Reports if an object can be selected.

  

   componentIndex: Index of subobject to check.

   select: The new selection state; true activates selection.

   syncHighlight: (default=true)

     If true,then the object is highlighted if it is selected 

     

    and unhighlighted if is is not selected.

  

   Returns: 0: object is not selected

     1: object is selected

     2: object is selected 

    persistently.
  """
  pass
 def ShortDescription(self,plural):
  """
  ShortDescription(self: RhinoObject,plural: bool) -> str

  

   Gets a localized short descriptive name of the object.

  

   plural: true if the descriptive name should in plural.

   Returns: A string with the short localized descriptive name.
  """
  pass
 def SupportsRenderPrimitiveList(self,viewport,preview):
  """
  SupportsRenderPrimitiveList(self: RhinoObject,viewport: ViewportInfo,preview: bool) -> bool

  

   Determines if custom render meshes will be built for a particular object.

  

   viewport: The viewport being rendered.

   preview: Type of mesh to build. If preview is true then a smaller mesh may be

     generated in 

    less time,false is meant when actually rendering.

  

   Returns: Returns true if custom render mesh(es) will get built for this object.
  """
  pass
 def TryGetRenderPrimitiveBoundingBox(self,viewport,preview,boundingBox):
  """
  TryGetRenderPrimitiveBoundingBox(self: RhinoObject,viewport: ViewportInfo,preview: bool) -> (bool,BoundingBox)

  

   Get the bounding box for the custom render meshes associated with this

     object.

  

   viewport: The viewport being rendered.

   preview: Type of mesh to build,if preview is true then a smaller mesh may be

     generated in 

    less time,false is meant when actually rendering.

  

   Returns: Returns true if the bounding box was successfully calculated otherwise

     returns 

    false on error.
  """
  pass
 def UnhighlightAllSubObjects(self):
  """
  UnhighlightAllSubObjects(self: RhinoObject) -> int

  

   Removes highlighting from all subobjects.

   Returns: The number of changed subobjects.
  """
  pass
 def UnselectAllSubObjects(self):
  """
  UnselectAllSubObjects(self: RhinoObject) -> int

  

   Removes selection from all subobjects.

   Returns: The number of unselected subobjects.
  """
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object attributes.



Get: Attributes(self: RhinoObject) -> ObjectAttributes



Set: Attributes(self: RhinoObject)=value

"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the document that owns this object.



Get: Document(self: RhinoObject) -> RhinoDoc



"""

 Geometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying geometry for this object.

   All rhino objects are composed of geometry and attributes.



Get: Geometry(self: RhinoObject) -> GeometryBase



"""

 GripsOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the activation state of object default editing grips.



Get: GripsOn(self: RhinoObject) -> bool



Set: GripsOn(self: RhinoObject)=value

"""

 GripsSelected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if grips are turned on and at least one is selected.



Get: GripsSelected(self: RhinoObject) -> bool



"""

 GroupCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of groups object belongs to.



Get: GroupCount(self: RhinoObject) -> int



"""

 HasDynamicTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the object has a dynamic transformation



Get: HasDynamicTransform(self: RhinoObject) -> bool



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Every object has a Guid (globally unique identifier,also known as UUID,or universally

   unique identifier). The default value is Guid.Empty.

   

   When an object is added to a model,the value is checked.  If the value is Guid.Empty,a

   new Guid is created. If the value is not null but it is already used by another object

   in the model,a new Guid is created. If the value is not Guid.Empty and it is not used by

   another object in the model,then that value persists. When an object is updated,by

   a move for example,the value of ObjectId persists.

   This value is the same as the one returned by this.Attributes.ObjectId.



Get: Id(self: RhinoObject) -> Guid



"""

 IsDeletable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Some objects cannot be deleted,like grips on lights and annotation objects.



Get: IsDeletable(self: RhinoObject) -> bool



"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the object is deleted. Deleted objects are kept by the document

   for undo purposes. Call RhinoDoc.UndeleteObject to undelete an object.



Get: IsDeleted(self: RhinoObject) -> bool



"""

 IsHidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An object must be in one of three modes: normal,locked or hidden.

   If an object is in normal mode,then the object's layer controls visibility

   and selectability. If an object is locked,then the object's layer controls

   visibility by the object cannot be selected. If the object is hidden,it is

   not visible and it cannot be selected.



Get: IsHidden(self: RhinoObject) -> bool



"""

 IsInstanceDefinitionGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if the object is used as part of an instance definition.



Get: IsInstanceDefinitionGeometry(self: RhinoObject) -> bool



"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An object must be in one of three modes: normal,locked or hidden.

   If an object is in normal mode,then the object's layer controls visibility

   and selectability. If an object is locked,then the object's layer controls

   visibility by the object cannot be selected. If the object is hidden,it is

   not visible and it cannot be selected.



Get: IsLocked(self: RhinoObject) -> bool



"""

 IsNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An object must be in one of three modes: normal,locked or hidden.

   If an object is in normal mode,then the object's layer controls visibility

   and selectability. If an object is locked,then the object's layer controls

   visibility by the object cannot be selected. If the object is hidden,it is

   not visible and it cannot be selected.



Get: IsNormal(self: RhinoObject) -> bool



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating if an object is a reference object. An object from a work session

   reference model is a reference object and cannot be modified. An object is

   a reference object if,and only if,it is on a reference layer.



Get: IsReference(self: RhinoObject) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tests an object to see if its data members are correctly initialized.



Get: IsValid(self: RhinoObject) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Rhino objects have optional text names.  More than one object in

   a model can have the same name and some objects may have no name.



Get: Name(self: RhinoObject) -> str



"""

 ObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Rhino-based object type.



Get: ObjectType(self: RhinoObject) -> ObjectType



"""

 RenderMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the render material associated with this object or null if there

   is none.  This does not pay attention to the material source and will

   not check parent objects or layers for a RenderMaterial.



Get: RenderMaterial(self: RhinoObject) -> RenderMaterial



"""

 RuntimeSerialNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the objects runtime serial number.



Get: RuntimeSerialNumber(self: RhinoObject) -> UInt32



"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object visibility.



Get: Visible(self: RhinoObject) -> bool



"""


