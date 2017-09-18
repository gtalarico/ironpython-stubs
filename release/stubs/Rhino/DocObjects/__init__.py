# encoding: utf-8
# module Rhino.DocObjects calls itself DocObjects
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ActiveSpace(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the current working space.
    
    enum ActiveSpace, values: ModelSpace (1), None (0), PageSpace (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ModelSpace = None
    None = None
    PageSpace = None
    value__ = None


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

    def CreateMeshes(self, meshType, parameters, ignoreCustomParameters):
        """
        CreateMeshes(self: RhinoObject, meshType: MeshType, parameters: MeshingParameters, ignoreCustomParameters: bool) -> int
        
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

    def EnableCustomGrips(self, customGrips):
        """
        EnableCustomGrips(self: RhinoObject, customGrips: CustomObjectGrips) -> bool
        
            Turns on/off the object's editing grips.
        
            customGrips: The custom object grips.
            Returns: true if the call succeeded.  If you attempt to add custom grips to an
                    object that 
             does not support custom grips, then false is returned.
        """
        pass

    def EnableVisualAnalysisMode(self, mode, enable):
        """
        EnableVisualAnalysisMode(self: RhinoObject, mode: VisualAnalysisMode, enable: bool) -> bool
        
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
            Returns: An array of visual analysis modes. The array can be empty, but not null.
        """
        pass

    def GetDynamicTransform(self, transform):
        """
        GetDynamicTransform(self: RhinoObject) -> (bool, Transform)
        
            While an object is being dynamically tranformed (dragged, rotated, ...),
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
             Rhino.DocObjects.RhinoObject.GroupCount is 0, then this method returns null.
        
            Returns: An array of group indices, or null if Rhino.DocObjects.RhinoObject.GroupCount is 0.
        """
        pass

    def GetHighlightedSubObjects(self):
        """
        GetHighlightedSubObjects(self: RhinoObject) -> Array[ComponentIndex]
        
            Gets a list of all highlighted subobjects.
            Returns: An array of all highlighted subobjects; or null is there are none.
        """
        pass

    def GetMaterial(self, frontMaterial):
        """
        GetMaterial(self: RhinoObject, frontMaterial: bool) -> Material
        
            Gets material that this object uses based on it's attributes and the document
                    that 
             the object is associated with.  In the rare case that a document is not
                    associated 
             with this object, null will be returned.
        
        
            frontMaterial: If true, gets the material used to render the object's front side
        """
        pass

    def GetMeshes(self, meshType):
        """
        GetMeshes(self: RhinoObject, meshType: MeshType) -> Array[Mesh]
        
            Get existing meshes used to render and analyze surface and polysrf objects.
        """
        pass

    def GetRenderMaterial(self, frontMaterial):
        """
        GetRenderMaterial(self: RhinoObject, frontMaterial: bool) -> RenderMaterial
        
            Gets the RenderMaterial that this object uses based on it's attributes
                    and the 
             document that the object is associated with. If there is no 
                    RenderMaterial 
             associated with this object then null is returned.  If
                    null is returned you should 
             call GetMaterial to get the material used
                    to render this object.
        
        
            frontMaterial: If true, gets the material used to render the object's front side
                    otherwise; gets 
             the material used to render the back side of the
                    object.
        
            Returns: If there is a RenderMaterial associated with this objects' associated
                    Material then 
             it is returned otherwise; null is returned.
        """
        pass

    @staticmethod
    def GetRenderMeshes(rhinoObjects, okToCreate, returnAllObjects):
        """ GetRenderMeshes(rhinoObjects: IEnumerable[RhinoObject], okToCreate: bool, returnAllObjects: bool) -> Array[ObjRef] """
        pass

    def GetRenderMeshParameters(self):
        """
        GetRenderMeshParameters(self: RhinoObject) -> MeshingParameters
        
            Meshing parameters that this object uses for generating render meshes. If the
                    
             object's attributes do not have custom meshing parameters, then the document's
                    
             meshing parameters are used.
        """
        pass

    def GetRenderPrimitiveList(self, viewport, preview):
        """
        GetRenderPrimitiveList(self: RhinoObject, viewport: ViewportInfo, preview: bool) -> RenderPrimitiveList
        
            Build custom render mesh(es) for this object.
        
            viewport: The viewport being rendered.
            preview: Type of mesh to build, if preview is true then a smaller mesh may be
                    generated in 
             less time, false is meant when actually rendering.
        
            Returns: Returns a RenderPrimitiveList if successful otherwise returns null.
        """
        pass

    def GetSelectedSubObjects(self):
        """
        GetSelectedSubObjects(self: RhinoObject) -> Array[ComponentIndex]
        
            Get a list of all selected sub-objects.
            Returns: An array of subobject indices, or null if there are none.
        """
        pass

    def GetSubObjects(self):
        """
        GetSubObjects(self: RhinoObject) -> Array[RhinoObject]
        
            Gets an array of sub-objects.
            Returns: An array of subobjects, or null if there are none.
        """
        pass

    def GetTextureChannels(self):
        """
        GetTextureChannels(self: RhinoObject) -> Array[int]
        
            Get a list of the texture mapping channel Id's associated with object.
            Returns: Returns an array of channel Id's or an empty list if there are not mappings.
        """
        pass

    def GetTextureMapping(self, channel, objectTransform=None):
        """
        GetTextureMapping(self: RhinoObject, channel: int) -> (TextureMapping, Transform)
        
            Get objects texture mapping
        GetTextureMapping(self: RhinoObject, channel: int) -> TextureMapping
        """
        pass

    def Highlight(self, enable):
        """
        Highlight(self: RhinoObject, enable: bool) -> bool
        
            Modifies the highlighting of the object.
        
            enable: true if highlighting should be enabled.
            Returns: true if the object is now highlighted.
        """
        pass

    def HighlightSubObject(self, componentIndex, highlight):
        """
        HighlightSubObject(self: RhinoObject, componentIndex: ComponentIndex, highlight: bool) -> bool
        
            Highlights a subobject.
        
            componentIndex: A subobject component index.
            highlight: true if the subobject should be highlighted.
            Returns: true if the subobject is now highlighted.
        """
        pass

    def InVisualAnalysisMode(self, mode=None):
        """
        InVisualAnalysisMode(self: RhinoObject, mode: VisualAnalysisMode) -> bool
        
            Reports if a visual analysis mode is currently active for an object.
        
            mode: The mode to check for.
                    Use null if you want to see if any mode is active.
            Returns: true if the specified analysis mode is active; otherwise false.
        InVisualAnalysisMode(self: RhinoObject) -> bool
        
            Reports if any visual analysis mode is currently active for an object.
            Returns: true if an analysis mode is active; otherwise false.
        """
        pass

    def IsActiveInViewport(self, viewport):
        """
        IsActiveInViewport(self: RhinoObject, viewport: RhinoViewport) -> bool
        
            Determine if this object is active in a particular viewport.
            Returns: True if the object is active in viewport
        """
        pass

    def IsHighlighted(self, checkSubObjects):
        """
        IsHighlighted(self: RhinoObject, checkSubObjects: bool) -> int
        
            Check highlight state.
        
            checkSubObjects: If true and the entire object is not highlighted, and some subset of the object
                    is 
             highlighted, like some edges of a surface, then 3 is returned.
                    If false and the 
             entire object is not highlighted, then zero is returned.
        
            Returns: 0: object is not highlighted.1: entire object is highlighted.3: one or more proper sub-objects 
             are highlighted.
        """
        pass

    def IsMeshable(self, meshType):
        """
        IsMeshable(self: RhinoObject, meshType: MeshType) -> bool
        
            Returns true if the object is capable of having a mesh of the specified type
        """
        pass

    def IsSelectable(self, ignoreSelectionState=None, ignoreGripsState=None, ignoreLayerLocking=None, ignoreLayerVisibility=None):
        """
        IsSelectable(self: RhinoObject) -> bool
        
            Reports if an object can be selected.
            Returns: true if object is capable of being selected.
        IsSelectable(self: RhinoObject, ignoreSelectionState: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> bool
        
            Reports if an object can be selected.
        
            ignoreSelectionState: If true, then selected objects are selectable.
                    If false, then selected objects are 
             not selectable.
        
            ignoreGripsState: If true, then objects with grips on can be selected.
                    If false, then the value 
             returned by the object's IsSelectableWithGripsOn() function decides if the object can be 
             selected.
        
            ignoreLayerLocking: If true, then objects on locked layers are selectable.
                    If false, then objects on 
             locked layers are not selectable.
        
            ignoreLayerVisibility: If true, then objects on hidden layers are selectable.
                    If false, then objects on 
             hidden layers are not selectable.
        
            Returns: true if object is capable of being selected.
        """
        pass

    def IsSelected(self, checkSubObjects):
        """
        IsSelected(self: RhinoObject, checkSubObjects: bool) -> int
        
            Check selection state.
        
            checkSubObjects: (false is good default)
                    If true and the entire object is not selected, and some 
             subset of the object
                    is selected, like some edges of a surface, then 3 is returned.
             
                    If false and the entire object is not selected, then zero is returned.
        
            Returns: 0 = object is not selected.
                    1 = object is selected.
                    2 = entire object 
             is selected persistently.
                    3 = one or more proper sub-objects are selected.
        """
        pass

    def IsSubObjectHighlighted(self, componentIndex):
        """
        IsSubObjectHighlighted(self: RhinoObject, componentIndex: ComponentIndex) -> bool
        
            Determines if a subobject is highlighted.
        
            componentIndex: A subobject component index.
            Returns: true if the subobject is highlighted.
        """
        pass

    def IsSubObjectSelectable(self, componentIndex, ignoreSelectionState):
        """
        IsSubObjectSelectable(self: RhinoObject, componentIndex: ComponentIndex, ignoreSelectionState: bool) -> bool
        
            Reports if a subobject can be selected.
        
            componentIndex: index of subobject to check.
            ignoreSelectionState: If true, then selected objects are selectable.
                    If false, then selected objects are 
             not selectable.
        
            Returns: true if the specified subobject can be selected.
        """
        pass

    def IsSubObjectSelected(self, componentIndex):
        """
        IsSubObjectSelected(self: RhinoObject, componentIndex: ComponentIndex) -> bool
        
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

    def MeshCount(self, meshType, parameters):
        """
        MeshCount(self: RhinoObject, meshType: MeshType, parameters: MeshingParameters) -> int
        
            RhinoObjects can have several different types of meshes and 
                    different numbers of 
             meshes.  A b-rep can have a render and 
                    an analysis mesh on each face.  A mesh 
             object has a single 
                    render mesh and no analysis mesh. Curve, point, and annotation
             
                    objects have no meshes.
        
        
            meshType: type of mesh to count
            parameters: if not null and if the object can change its mesh (like a brep),
                    then only meshes 
             that were created with these mesh parameters are counted.
        
            Returns: number of meshes
        """
        pass

    @staticmethod
    def MeshObjects(rhinoObjects, parameters, *__args):
        """
        MeshObjects(rhinoObjects: IEnumerable[RhinoObject], parameters: MeshingParameters, simpleDialog: bool) -> (Result, MeshingParameters, bool, Array[Mesh], Array[ObjectAttributes])
        MeshObjects(rhinoObjects: IEnumerable[RhinoObject], parameters: MeshingParameters) -> (Result, Array[Mesh], Array[ObjectAttributes])
        """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
        """
        pass

    def Select(self, on, syncHighlight=None, persistentSelect=None, ignoreGripsState=None, ignoreLayerLocking=None, ignoreLayerVisibility=None):
        """
        Select(self: RhinoObject, on: bool, syncHighlight: bool) -> int
        
            Selects an object.
        
            on: The new selection state; true activates selection.
            syncHighlight: If true, then the object is hightlighted if it is selected
                    and not hightlighted if 
             is is not selected.
                    Highlighting can be and stay out of sync, as its specification 
             is independent.
        
            Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.
        Select(self: RhinoObject, on: bool) -> int
        
            Selects an object.
        
            on: The new selection state; true activates selection.
            Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.
        Select(self: RhinoObject, on: bool, syncHighlight: bool, persistentSelect: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> int
        
            Selects an object.
        
            on: The new selection state; true activates selection.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
                    Highlighting can be and stay out of sync, as its specification is 
             independent.
        
            persistentSelect: Objects that are persistently selected stay selected when a command terminates.
            ignoreGripsState: If true, then objects with grips on can be selected.
                    If false, then the value 
             returned by the object's IsSelectableWithGripsOn() function
                    decides if the object 
             can be selected when it has grips turned on.
        
            ignoreLayerLocking: If true, then objects on locked layers can be selected.
                    If false, then objects on 
             locked layers cannot be selected.
        
            ignoreLayerVisibility: If true, then objects on hidden layers can be selectable.
                    If false, then objects on 
             hidden layers cannot be selected.
        
            Returns: 0: object is not selected.1: object is selected.2: object is selected persistently.
        """
        pass

    def SelectSubObject(self, componentIndex, select, syncHighlight):
        """
        SelectSubObject(self: RhinoObject, componentIndex: ComponentIndex, select: bool, syncHighlight: bool) -> int
        
            Reports if an object can be selected.
        
            componentIndex: Index of subobject to check.
            select: The new selection state; true activates selection.
            syncHighlight: (default=true)
                    If true, then the object is highlighted if it is selected 
                 
                and unhighlighted if is is not selected.
        
            Returns: 0: object is not selected
                    1: object is selected
                    2: object is selected 
             persistently.
        """
        pass

    def ShortDescription(self, plural):
        """
        ShortDescription(self: RhinoObject, plural: bool) -> str
        
            Gets a localized short descriptive name of the object.
        
            plural: true if the descriptive name should in plural.
            Returns: A string with the short localized descriptive name.
        """
        pass

    def SupportsRenderPrimitiveList(self, viewport, preview):
        """
        SupportsRenderPrimitiveList(self: RhinoObject, viewport: ViewportInfo, preview: bool) -> bool
        
            Determines if custom render meshes will be built for a particular object.
        
            viewport: The viewport being rendered.
            preview: Type of mesh to build. If preview is true then a smaller mesh may be
                    generated in 
             less time, false is meant when actually rendering.
        
            Returns: Returns true if custom render mesh(es) will get built for this object.
        """
        pass

    def TryGetRenderPrimitiveBoundingBox(self, viewport, preview, boundingBox):
        """
        TryGetRenderPrimitiveBoundingBox(self: RhinoObject, viewport: ViewportInfo, preview: bool) -> (bool, BoundingBox)
        
            Get the bounding box for the custom render meshes associated with this
                    object.
        
            viewport: The viewport being rendered.
            preview: Type of mesh to build, if preview is true then a smaller mesh may be
                    generated in 
             less time, false is meant when actually rendering.
        
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

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object attributes.

Get: Attributes(self: RhinoObject) -> ObjectAttributes

Set: Attributes(self: RhinoObject) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that owns this object.

Get: Document(self: RhinoObject) -> RhinoDoc

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying geometry for this object.
            All rhino objects are composed of geometry and attributes.

Get: Geometry(self: RhinoObject) -> GeometryBase

"""

    GripsOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the activation state of object default editing grips.

Get: GripsOn(self: RhinoObject) -> bool

Set: GripsOn(self: RhinoObject) = value
"""

    GripsSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if grips are turned on and at least one is selected.

Get: GripsSelected(self: RhinoObject) -> bool

"""

    GroupCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of groups object belongs to.

Get: GroupCount(self: RhinoObject) -> int

"""

    HasDynamicTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the object has a dynamic transformation

Get: HasDynamicTransform(self: RhinoObject) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Every object has a Guid (globally unique identifier, also known as UUID, or universally
            unique identifier). The default value is Guid.Empty.
            
            When an object is added to a model, the value is checked.  If the value is Guid.Empty, a
            new Guid is created. If the value is not null but it is already used by another object
            in the model, a new Guid is created. If the value is not Guid.Empty and it is not used by
            another object in the model, then that value persists. When an object is updated, by
            a move for example, the value of ObjectId persists.
            This value is the same as the one returned by this.Attributes.ObjectId.

Get: Id(self: RhinoObject) -> Guid

"""

    IsDeletable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Some objects cannot be deleted, like grips on lights and annotation objects.

Get: IsDeletable(self: RhinoObject) -> bool

"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the object is deleted. Deleted objects are kept by the document
            for undo purposes. Call RhinoDoc.UndeleteObject to undelete an object.

Get: IsDeleted(self: RhinoObject) -> bool

"""

    IsHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object must be in one of three modes: normal, locked or hidden.
            If an object is in normal mode, then the object's layer controls visibility
            and selectability. If an object is locked, then the object's layer controls
            visibility by the object cannot be selected. If the object is hidden, it is
            not visible and it cannot be selected.

Get: IsHidden(self: RhinoObject) -> bool

"""

    IsInstanceDefinitionGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the object is used as part of an instance definition.

Get: IsInstanceDefinitionGeometry(self: RhinoObject) -> bool

"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object must be in one of three modes: normal, locked or hidden.
            If an object is in normal mode, then the object's layer controls visibility
            and selectability. If an object is locked, then the object's layer controls
            visibility by the object cannot be selected. If the object is hidden, it is
            not visible and it cannot be selected.

Get: IsLocked(self: RhinoObject) -> bool

"""

    IsNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object must be in one of three modes: normal, locked or hidden.
            If an object is in normal mode, then the object's layer controls visibility
            and selectability. If an object is locked, then the object's layer controls
            visibility by the object cannot be selected. If the object is hidden, it is
            not visible and it cannot be selected.

Get: IsNormal(self: RhinoObject) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating if an object is a reference object. An object from a work session
            reference model is a reference object and cannot be modified. An object is
            a reference object if, and only if, it is on a reference layer.

Get: IsReference(self: RhinoObject) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests an object to see if its data members are correctly initialized.

Get: IsValid(self: RhinoObject) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rhino objects have optional text names.  More than one object in
            a model can have the same name and some objects may have no name.

Get: Name(self: RhinoObject) -> str

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Rhino-based object type.

Get: ObjectType(self: RhinoObject) -> ObjectType

"""

    RenderMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the render material associated with this object or null if there
            is none.  This does not pay attention to the material source and will
            not check parent objects or layers for a RenderMaterial.

Get: RenderMaterial(self: RhinoObject) -> RenderMaterial

"""

    RuntimeSerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the objects runtime serial number.

Get: RuntimeSerialNumber(self: RhinoObject) -> UInt32

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object visibility.

Get: Visible(self: RhinoObject) -> bool

"""



class AnnotationObjectBase(RhinoObject):
    """
    Provides a base class for Rhino.Geometry.AnnotationBase-derived
                objects that are placed in a document.
    """
    DisplayText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text that is displayed to users.

Get: DisplayText(self: AnnotationObjectBase) -> str

"""



class AngularDimensionObject(AnnotationObjectBase):
    """ Angular style dimension """

class BasepointZero(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies enumerated constants used to indicate the zero level convention relating to a location on Earth.
                This is used in conjunction with the Rhino.DocObjects.EarthAnchorPoint class.
    
    enum BasepointZero, values: CenterOfEarth (2), GroundLevel (0), MeanSeaLevel (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterOfEarth = None
    GroundLevel = None
    MeanSeaLevel = None
    value__ = None


class BitmapEntry(CommonObject, IDisposable, ISerializable):
    """ Rhino.DocObjects.Tables.BitmapTable entry """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def Save(self, fileName):
        """ Save(self: BitmapEntry, fileName: str) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this bitmap.

Get: FileName(self: BitmapEntry) -> str

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicting whether this bitmap is a referenced bitmap. 
            Referenced bitmaps are part of referenced documents.

Get: IsReference(self: BitmapEntry) -> bool

"""



class BrepObject(RhinoObject):
    """ Represents a Rhino.Geometry.Brepbrep in a document. """
    def DuplicateBrepGeometry(self):
        """
        DuplicateBrepGeometry(self: BrepObject) -> Brep
        
            Constructs a new deep copy of the brep geometry.
            Returns: The copy of the geometry.
        """
        pass

    BrepGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brep geometry linked with this object.

Get: BrepGeometry(self: BrepObject) -> Brep

"""



class ClippingPlaneObject(RhinoObject):
    """
    Represents the object of a Rhino.Geometry.ClippingPlaneSurfaceclipping plane,
                stored in the Rhino document and with attributes.
    """
    ClippingPlaneGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the clipping plane surface.

Get: ClippingPlaneGeometry(self: ClippingPlaneObject) -> ClippingPlaneSurface

"""



class ConstructionPlane(object):
    """
    Represents a contruction plane inside the document.
                Use Rhino.DocObjects.Tables.NamedConstructionPlaneTable
                methods and indexers to add and access a Rhino.DocObjects.ConstructionPlane.
    
    ConstructionPlane()
    """
    DepthBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the grid is drawn on top of geometry.
            false=grid is always drawn behind 3d geometrytrue=grid is drawn at its depth as a 3d plane and grid lines obscure things behind the grid.

Get: DepthBuffered(self: ConstructionPlane) -> bool

Set: DepthBuffered(self: ConstructionPlane) = value
"""

    GridLineCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the total amount of grid lines in each direction.

Get: GridLineCount(self: ConstructionPlane) -> int

Set: GridLineCount(self: ConstructionPlane) = value
"""

    GridSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance between grid lines.

Get: GridSpacing(self: ConstructionPlane) -> float

Set: GridSpacing(self: ConstructionPlane) = value
"""

    GridXColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the grid X-axis mark.

Get: GridXColor(self: ConstructionPlane) -> Color

Set: GridXColor(self: ConstructionPlane) = value
"""

    GridYColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the grid Y-axis mark.

Get: GridYColor(self: ConstructionPlane) -> Color

Set: GridYColor(self: ConstructionPlane) = value
"""

    GridZColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the grid Z-axis mark.

Get: GridZColor(self: ConstructionPlane) -> Color

Set: GridZColor(self: ConstructionPlane) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the grid.

Get: Name(self: ConstructionPlane) -> str

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the geometric plane to use for construction.

Get: Plane(self: ConstructionPlane) -> Plane

Set: Plane(self: ConstructionPlane) = value
"""

    ShowAxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the axes of the grid shuld be visible.

Get: ShowAxes(self: ConstructionPlane) -> bool

Set: ShowAxes(self: ConstructionPlane) = value
"""

    ShowGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the grid itself should be visible.

Get: ShowGrid(self: ConstructionPlane) -> bool

Set: ShowGrid(self: ConstructionPlane) = value
"""

    SnapSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """when "grid snap" is enabled, the distance between snap points.
            Typically this is the same distance as grid spacing.

Get: SnapSpacing(self: ConstructionPlane) -> float

Set: SnapSpacing(self: ConstructionPlane) = value
"""

    ThickLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the thicker, wider line.

Get: ThickLineColor(self: ConstructionPlane) -> Color

Set: ThickLineColor(self: ConstructionPlane) = value
"""

    ThickLineFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the recurrence of a wider line on the grid.
            0: No lines are thick, all are drawn thin.1: All lines are thick.2: Every other line is thick.3: One line in three lines is thick (and two are thin).4: ...

Get: ThickLineFrequency(self: ConstructionPlane) -> int

Set: ThickLineFrequency(self: ConstructionPlane) = value
"""

    ThinLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the thinner, less prominent line.

Get: ThinLineColor(self: ConstructionPlane) -> Color

Set: ThinLineColor(self: ConstructionPlane) = value
"""



class CoordinateSystem(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for coordinate systems to use as references.
    
    enum CoordinateSystem, values: Camera (1), Clip (2), Screen (3), World (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Camera = None
    Clip = None
    Screen = None
    value__ = None
    World = None


class CurveObject(RhinoObject):
    """ A Rhino Object that represents curve geometry and attributes """
    def DuplicateCurveGeometry(self):
        """ DuplicateCurveGeometry(self: CurveObject) -> Curve """
        pass

    CurveGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGeometry(self: CurveObject) -> Curve

"""



class DetailViewObject(RhinoObject):
    # no doc
    def CommitViewportChanges(self):
        """ CommitViewportChanges(self: DetailViewObject) -> bool """
        pass

    DetailGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetailGeometry(self: DetailViewObject) -> DetailView

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: DetailViewObject) -> bool

Set: IsActive(self: DetailViewObject) = value
"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: DetailViewObject) -> RhinoViewport

"""



class DimensionStyle(CommonObject, IDisposable, ISerializable):
    """ DimensionStyle() """
    def CommitChanges(self):
        """ CommitChanges(self: DimensionStyle) -> bool """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AlternateLengthFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlternateLengthFactor(self: DimensionStyle) -> float

Set: AlternateLengthFactor(self: DimensionStyle) = value
"""

    AngleResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleResolution(self: DimensionStyle) -> int

Set: AngleResolution(self: DimensionStyle) = value
"""

    ArrowLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowLength(self: DimensionStyle) -> float

Set: ArrowLength(self: DimensionStyle) = value
"""

    ArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: ArrowType(self: DimensionStyle) = value
"""

    CenterMarkSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterMarkSize(self: DimensionStyle) -> float

Set: CenterMarkSize(self: DimensionStyle) = value
"""

    ExtensionLineExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLineExtension(self: DimensionStyle) -> float

Set: ExtensionLineExtension(self: DimensionStyle) = value
"""

    ExtensionLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLineOffset(self: DimensionStyle) -> float

Set: ExtensionLineOffset(self: DimensionStyle) = value
"""

    FontIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontIndex(self: DimensionStyle) -> int

Set: FontIndex(self: DimensionStyle) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DimensionStyle) -> Guid

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: DimensionStyle) -> int

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReference(self: DimensionStyle) -> bool

"""

    LeaderArrowLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderArrowLength(self: DimensionStyle) -> float

Set: LeaderArrowLength(self: DimensionStyle) = value
"""

    LeaderArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderArrowType(self: DimensionStyle) -> DimensionStyleArrowType

Set: LeaderArrowType(self: DimensionStyle) = value
"""

    LengthFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFactor(self: DimensionStyle) -> float

Set: LengthFactor(self: DimensionStyle) = value
"""

    LengthFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFormat(self: DimensionStyle) -> DistanceDisplayMode

Set: LengthFormat(self: DimensionStyle) = value
"""

    LengthResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Linear display precision.

Get: LengthResolution(self: DimensionStyle) -> int

Set: LengthResolution(self: DimensionStyle) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DimensionStyle) -> str

Set: Name(self: DimensionStyle) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: DimensionStyle) -> str

Set: Prefix(self: DimensionStyle) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: DimensionStyle) -> str

Set: Suffix(self: DimensionStyle) = value
"""

    TextAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextAlignment(self: DimensionStyle) -> TextDisplayAlignment

Set: TextAlignment(self: DimensionStyle) = value
"""

    TextGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextGap(self: DimensionStyle) -> float

Set: TextGap(self: DimensionStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: DimensionStyle) -> float

Set: TextHeight(self: DimensionStyle) = value
"""



class DimensionStyleArrowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DimensionStyleArrowType, values: Arrow (4), Dot (1), LongerTriangle (7), LongTriangle (6), Rectangle (5), ShortTriangle (3), SolidTriangle (0), Tick (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Arrow = None
    Dot = None
    LongerTriangle = None
    LongTriangle = None
    Rectangle = None
    ShortTriangle = None
    SolidTriangle = None
    Tick = None
    value__ = None


class DisplayMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for display modes, such as wireframe or shaded.
    
    enum DisplayMode, values: Default (0), RenderPreview (3), Shaded (2), Wireframe (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    RenderPreview = None
    Shaded = None
    value__ = None
    Wireframe = None


class DistanceDisplayMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the display of distances in US customary and Imperial units.
    
    enum DistanceDisplayMode, values: Decimal (0), Feet (1), FeetAndInches (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Decimal = None
    Feet = None
    FeetAndInches = None
    value__ = None


class EarthAnchorPoint(object, IDisposable):
    """
    Contains information about the model's position in latitude, longitude,
                and elevation for GIS mapping applications.
    
    EarthAnchorPoint()
    """
    def Dispose(self):
        """
        Dispose(self: EarthAnchorPoint)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def GetModelCompass(self):
        """
        GetModelCompass(self: EarthAnchorPoint) -> Plane
        
            Returns a plane in model coordinates whose X axis points East,
                    Y axis points North 
             and Z axis points Up. The origin
                    is set to ModelBasepoint.
        
            Returns: A plane value. This might be invalid on error.
        """
        pass

    def GetModelToEarthTransform(self, modelUnitSystem):
        """
        GetModelToEarthTransform(self: EarthAnchorPoint, modelUnitSystem: UnitSystem) -> Transform
        
            Gets a transformation from model coordinates to earth coordinates.
                    This 
             transformation assumes the model is small enough that
                    the curvature of the earth 
             can be ignored.
        
        
            modelUnitSystem: The model unit system.
            Returns: Transform on success. Inalid Transform on error.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the long form of the identifying information about this location.

Get: Description(self: EarthAnchorPoint) -> str

Set: Description(self: EarthAnchorPoint) = value
"""

    EarthBasepointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point elevation on earth, in meters.

Get: EarthBasepointElevation(self: EarthAnchorPoint) -> float

Set: EarthBasepointElevation(self: EarthAnchorPoint) = value
"""

    EarthBasepointElevationZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the zero level convention relating to a location on Earth.

Get: EarthBasepointElevationZero(self: EarthAnchorPoint) -> BasepointZero

Set: EarthBasepointElevationZero(self: EarthAnchorPoint) = value
"""

    EarthBasepointLatitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a point latitude on earth, in decimal degrees.
            +90 = north pole, 0 = equator, -90 = south pole.

Get: EarthBasepointLatitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLatitude(self: EarthAnchorPoint) = value
"""

    EarthBasepointLongitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point longitude on earth, in decimal degrees.
            0 = prime meridian (Greenwich meridian)Values increase towards West

Get: EarthBasepointLongitude(self: EarthAnchorPoint) -> float

Set: EarthBasepointLongitude(self: EarthAnchorPoint) = value
"""

    ModelBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Corresponding model point in model coordinates.

Get: ModelBasePoint(self: EarthAnchorPoint) -> Point3d

Set: ModelBasePoint(self: EarthAnchorPoint) = value
"""

    ModelEast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Earth directions in model coordinates.

Get: ModelEast(self: EarthAnchorPoint) -> Vector3d

Set: ModelEast(self: EarthAnchorPoint) = value
"""

    ModelNorth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Earth directions in model coordinates.

Get: ModelNorth(self: EarthAnchorPoint) -> Vector3d

Set: ModelNorth(self: EarthAnchorPoint) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the short form of the identifying information about this location.

Get: Name(self: EarthAnchorPoint) -> str

Set: Name(self: EarthAnchorPoint) = value
"""



class ExtrusionObject(RhinoObject):
    # no doc
    def DuplicateExtrusionGeometry(self):
        """ DuplicateExtrusionGeometry(self: ExtrusionObject) -> Extrusion """
        pass

    ExtrusionGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtrusionGeometry(self: ExtrusionObject) -> Extrusion

"""



class Font(object):
    # no doc
    @staticmethod
    def AvailableFontFaceNames():
        """ AvailableFontFaceNames() -> Array[str] """
        pass

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bold(self: Font) -> bool

"""

    FaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceName(self: Font) -> str

"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italic(self: Font) -> bool

"""



class GripObject(RhinoObject):
    # no doc
    def Move(self, *__args):
        """
        Move(self: GripObject, newLocation: Point3d)
            Moves the grip to a new location.
        
            newLocation: New location for grip.
        Move(self: GripObject, delta: Vector3d)
            Moves the grip to a new location.
        
            delta: Translation applied to the OriginalLocation point.
        Move(self: GripObject, xform: Transform)
            Moves the grip to a new location.
        
            xform: Transformation appliead to the OriginalLocation point.
        """
        pass

    def NeighborGrip(self, directionR, directionS, directionT, wrap):
        """
        NeighborGrip(self: GripObject, directionR: int, directionS: int, directionT: int, wrap: bool) -> GripObject
        
            Used to get a grip's logical neighbors, like NURBS curve, suface,
                    and cage control 
             point grips.
        
        
            directionR: -1 to go back one grip, +1 to move forward one grip.  For curves, surfaces
                    and 
             cages, this is the first parameter direction.
        
            directionS: -1 to go back one grip, +1 to move forward one grip.  For surfaces and
                    cages this 
             is the second parameter direction.
        
            directionT: For cages this is the third parameter direction
            Returns: logical neighbor or null if the is no logical neighbor
        """
        pass

    def UndoMove(self):
        """
        UndoMove(self: GripObject)
            Undoes any grip moves made by calling Move.
        """
        pass

    CurrentLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLocation(self: GripObject) -> Point3d

Set: CurrentLocation(self: GripObject) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: GripObject) -> int

"""

    Moved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the grip has moved from OriginalLocation.

Get: Moved(self: GripObject) -> bool

"""

    OriginalLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalLocation(self: GripObject) -> Point3d

"""

    OwnerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwnerId(self: GripObject) -> Guid

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The weight of a NURBS control point grip or RhinoMath.UnsetValue
            if the grip is not a NURBS control point grip.

Get: Weight(self: GripObject) -> float

Set: Weight(self: GripObject) = value
"""



class HatchObject(RhinoObject):
    # no doc
    HatchGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchGeometry(self: HatchObject) -> Hatch

"""



class HatchPattern(CommonObject, IDisposable, ISerializable):
    """ HatchPattern() """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    @staticmethod
    def ReadFromFile(filename, quiet):
        """
        ReadFromFile(filename: str, quiet: bool) -> Array[HatchPattern]
        
            Reads hatch pattern definitions from a file.
        
            filename: Name of an existing file. If filename is null or empty, default hatch pattern filename is used.
            quiet: If file doesn't exist, and quiet is false, an error meesage box is shown.
            Returns: An array of hatch patterns. This can be null, but not empty.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: HatchPattern) -> str

Set: Description(self: HatchPattern) = value
"""

    FillType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillType(self: HatchPattern) -> HatchPatternFillType

Set: FillType(self: HatchPattern) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index in the hatch pattern table for this pattern. -1 if not in the table.

Get: Index(self: HatchPattern) -> int

"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deleted hatch patterns are kept in the runtime hatch pattern table so that undo
            will work with hatch patterns.  Call IsDeleted to determine to determine if
            a hatch pattern is deleted.

Get: IsDeleted(self: HatchPattern) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rhino allows multiple files to be viewed simultaneously. Hatch patterns in the
            document are "normal" or "reference". Reference hatch patterns are not saved.

Get: IsReference(self: HatchPattern) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HatchPattern) -> str

Set: Name(self: HatchPattern) = value
"""



class HatchPatternFillType(Enum, IComparable, IFormattable, IConvertible):
    """ enum HatchPatternFillType, values: Gradient (2), Lines (1), Solid (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Gradient = None
    Lines = None
    Solid = None
    value__ = None


class HistoryRecord(object, IDisposable):
    """ HistoryRecord(command: Command, version: int) """
    def Dispose(self):
        """
        Dispose(self: HistoryRecord)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def SetBool(self, id, value):
        """ SetBool(self: HistoryRecord, id: int, value: bool) -> bool """
        pass

    def SetBools(self, id, values):
        """ SetBools(self: HistoryRecord, id: int, values: IEnumerable[bool]) -> bool """
        pass

    def SetBrep(self, id, value):
        """ SetBrep(self: HistoryRecord, id: int, value: Brep) -> bool """
        pass

    def SetColor(self, id, value):
        """ SetColor(self: HistoryRecord, id: int, value: Color) -> bool """
        pass

    def SetColors(self, id, values):
        """ SetColors(self: HistoryRecord, id: int, values: IEnumerable[Color]) -> bool """
        pass

    def SetCurve(self, id, value):
        """ SetCurve(self: HistoryRecord, id: int, value: Curve) -> bool """
        pass

    def SetDouble(self, id, value):
        """ SetDouble(self: HistoryRecord, id: int, value: float) -> bool """
        pass

    def SetDoubles(self, id, values):
        """ SetDoubles(self: HistoryRecord, id: int, values: IEnumerable[float]) -> bool """
        pass

    def SetGuid(self, id, value):
        """ SetGuid(self: HistoryRecord, id: int, value: Guid) -> bool """
        pass

    def SetGuids(self, id, values):
        """ SetGuids(self: HistoryRecord, id: int, values: IEnumerable[Guid]) -> bool """
        pass

    def SetInt(self, id, value):
        """ SetInt(self: HistoryRecord, id: int, value: int) -> bool """
        pass

    def SetInts(self, id, values):
        """ SetInts(self: HistoryRecord, id: int, values: IEnumerable[int]) -> bool """
        pass

    def SetMesh(self, id, value):
        """ SetMesh(self: HistoryRecord, id: int, value: Mesh) -> bool """
        pass

    def SetObjRef(self, id, value):
        """ SetObjRef(self: HistoryRecord, id: int, value: ObjRef) -> bool """
        pass

    def SetPoint3d(self, id, value):
        """ SetPoint3d(self: HistoryRecord, id: int, value: Point3d) -> bool """
        pass

    def SetPoint3dOnObject(self, id, objref, value):
        """ SetPoint3dOnObject(self: HistoryRecord, id: int, objref: ObjRef, value: Point3d) -> bool """
        pass

    def SetPoint3ds(self, id, values):
        """ SetPoint3ds(self: HistoryRecord, id: int, values: IEnumerable[Point3d]) -> bool """
        pass

    def SetString(self, id, value):
        """ SetString(self: HistoryRecord, id: int, value: str) -> bool """
        pass

    def SetStrings(self, id, values):
        """ SetStrings(self: HistoryRecord, id: int, values: IEnumerable[str]) -> bool """
        pass

    def SetSurface(self, id, value):
        """ SetSurface(self: HistoryRecord, id: int, value: Surface) -> bool """
        pass

    def SetTransorm(self, id, value):
        """ SetTransorm(self: HistoryRecord, id: int, value: Transform) -> bool """
        pass

    def SetVector3d(self, id, value):
        """ SetVector3d(self: HistoryRecord, id: int, value: Vector3d) -> bool """
        pass

    def SetVector3ds(self, id, values):
        """ SetVector3ds(self: HistoryRecord, id: int, values: IEnumerable[Vector3d]) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, command, version):
        """ __new__(cls: type, command: Command, version: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wrapped native C++ pointer to CRhinoHistory instance

Get: Handle(self: HistoryRecord) -> IntPtr

"""



class InstanceDefinition(object):
    # no doc
    def CreatePreviewBitmap(self, definedViewportProjection, *__args):
        """
        CreatePreviewBitmap(self: InstanceDefinition, definedViewportProjection: DefinedViewportProjection, bitmapSize: Size) -> Bitmap
        CreatePreviewBitmap(self: InstanceDefinition, definedViewportProjection: DefinedViewportProjection, displayMode: DisplayMode, bitmapSize: Size) -> Bitmap
        """
        pass

    def GetContainers(self):
        """
        GetContainers(self: InstanceDefinition) -> Array[InstanceDefinition]
        
            Gets a list of all the InstanceDefinitions that contain a reference this InstanceDefinition.
            Returns: An array of instance definitions. The returned array can be empty, but not null.
        """
        pass

    def GetObjects(self):
        """
        GetObjects(self: InstanceDefinition) -> Array[RhinoObject]
        
            Gets an array with the objects that belong to this instance definition.
            Returns: An array of Rhino objects. The returned array can be empty, but not null.
        """
        pass

    def GetReferences(self, wheretoLook):
        """
        GetReferences(self: InstanceDefinition, wheretoLook: int) -> Array[InstanceObject]
        
            Gets a list of the CRhinoInstanceObjects (inserts) that contains
                    a reference this 
             instance definition.
        
        
            wheretoLook: 0 = get top level references in active document.1 = get top level and nested references in 
             active document.2 = check for references from other instance definitions.
        
            Returns: An array of instance objects. The returned array can be empty, but not null.
        """
        pass

    def InUse(self, wheretoLook):
        """
        InUse(self: InstanceDefinition, wheretoLook: int) -> bool
        
            Determines whether the instance definition is referenced.
        
            wheretoLook: 0 = check for top level references in active document.1 = check for top level and nested 
             references in active document.2 = check for references in other instance definitions.
        
            Returns: true if the instance definition is used; otherwise false.
        """
        pass

    def Object(self, index):
        """
        Object(self: InstanceDefinition, index: int) -> RhinoObject
        
            returns an object used as part of this definition.
        
            index: 0 <= index < ObjectCount.
            Returns: Returns an object that is used to define the geometry.
                    Does NOT return an object 
             that references this definition.count the number of references to this instance.
        """
        pass

    def UsesDefinition(self, otherIdefIndex):
        """
        UsesDefinition(self: InstanceDefinition, otherIdefIndex: int) -> int
        
            Determines if this instance definition contains a reference to another instance definition.
        
            otherIdefIndex: index of another instance definition.
            Returns: 0      no
                      1      other_idef_index is the index of this instance definition
              
                    >1      This InstanceDefinition uses the instance definition
                             and 
             the returned value is the nesting depth.
        """
        pass

    ArchiveFileStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the archive file status of a linked instance definition.

Get: ArchiveFileStatus(self: InstanceDefinition) -> InstanceDefinitionArchiveFileStatus

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: InstanceDefinition) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: InstanceDefinition) -> Guid

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of this instance definition in the index definition table.

Get: Index(self: InstanceDefinition) -> int

"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeleted(self: InstanceDefinition) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object from a work session reference model is reference a
            reference object and cannot be modified.  An object is a reference
            object if, and only if, it is on a reference layer.

Get: IsReference(self: InstanceDefinition) -> bool

"""

    IsTenuous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTenuous(self: InstanceDefinition) -> bool

"""

    LayerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerStyle(self: InstanceDefinition) -> InstanceDefinitionLayerStyle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: InstanceDefinition) -> str

"""

    ObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of objects this definition uses. This counts the objects that are used to define the geometry.
            This does NOT count the number of references to this instance definition.

Get: ObjectCount(self: InstanceDefinition) -> int

"""

    SkipNestedLinkedDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls how much geometry is read when a linked InstanceDefinition is updated.

Get: SkipNestedLinkedDefinitions(self: InstanceDefinition) -> bool

"""

    SourceArchive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceArchive(self: InstanceDefinition) -> str

"""

    UpdateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateType(self: InstanceDefinition) -> InstanceDefinitionUpdateType

"""

    Url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hyperlink URL that is executed when the UrlDescription hyperlink is clicked on in the Insert and Block UI

Get: Url(self: InstanceDefinition) -> str

"""

    UrlDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The URL description displayed as a hyperlink in the Insert and Block UI

Get: UrlDescription(self: InstanceDefinition) -> str

"""



class InstanceDefinitionArchiveFileStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    The archive file of a linked instance definition can have the following possible states.
                Use InstanceObject.ArchiveFileStatus to query a instance definition's archive file status.
    
    enum InstanceDefinitionArchiveFileStatus, values: LinkedFileIsDifferent (3), LinkedFileIsNewer (1), LinkedFileIsOlder (2), LinkedFileIsUpToDate (0), LinkedFileNotFound (-1), LinkedFileNotReadable (-2), NotALinkedInstanceDefinition (-3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LinkedFileIsDifferent = None
    LinkedFileIsNewer = None
    LinkedFileIsOlder = None
    LinkedFileIsUpToDate = None
    LinkedFileNotFound = None
    LinkedFileNotReadable = None
    NotALinkedInstanceDefinition = None
    value__ = None


class InstanceDefinitionLayerStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    A InstanceDefinitionUpdateType.Static or InstanceDefinitionUpdateType.LinkedAndEmbedded idef
                must have LayerStyle = Unset, a InstanceDefinitionUpdateType.Linked InstanceDefnition must
                have LayerStyle = Active or Reference
    
    enum InstanceDefinitionLayerStyle, values: Active (1), None (0), Reference (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Active = None
    None = None
    Reference = None
    value__ = None


class InstanceDefinitionUpdateType(Enum, IComparable, IFormattable, IConvertible):
    """
    The possible relationships between the instance definition geometry
                and the archive containing the original defition.
    
    enum InstanceDefinitionUpdateType, values: Embedded (1), Linked (3), LinkedAndEmbedded (2), Static (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Embedded = None
    Linked = None
    LinkedAndEmbedded = None
    Static = None
    value__ = None


class InstanceObject(RhinoObject):
    # no doc
    def Explode(self, explodeNestedInstances, pieces, pieceAttributes, pieceTransforms):
        """
        Explode(self: InstanceObject, explodeNestedInstances: bool) -> (Array[RhinoObject], Array[ObjectAttributes], Array[Transform])
        
            Explodes the instance reference into pieces.
        
            explodeNestedInstances: If true, then nested instance references are recursively exploded into pieces
                    until 
             actual geometry is found. If false, an InstanceObject is added to
                    the pieces out 
             parameter when this InstanceObject has nested references.
        """
        pass

    def UsesDefinition(self, definitionIndex, nestingLevel):
        """
        UsesDefinition(self: InstanceObject, definitionIndex: int) -> (bool, int)
        
            Determine if this reference uses an instance definition
            Returns: true or false depending on if the deifinition is used
        """
        pass

    InsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Basepoint coordinates of a block.

Get: InsertionPoint(self: InstanceObject) -> Point3d

"""

    InstanceDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """instance definition that this object uses.

Get: InstanceDefinition(self: InstanceObject) -> InstanceDefinition

"""

    InstanceXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """transformation applied to an instance definition for this object.

Get: InstanceXform(self: InstanceObject) -> Transform

"""



class Layer(CommonObject, IDisposable, ISerializable):
    """ Layer() """
    def CommitChanges(self):
        """ CommitChanges(self: Layer) -> bool """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Default(self):
        """
        Default(self: Layer)
            Sets layer to default settings.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def GetChildren(self):
        """
        GetChildren(self: Layer) -> Array[Layer]
        
            Gets immediate children of this layer. Note that child layers may have their own children.
            Returns: Array of child layers. null if this layer does not have any children.
        """
        pass

    @staticmethod
    def GetDefaultLayerProperties():
        """
        GetDefaultLayerProperties() -> Layer
        
            Constructs a layer with the current default properties.
                    The default layer 
             properties are:
                    color = 
             Rhino.ApplicationSettings.AppearanceSettings.DefaultLayerColorline style = 
             Rhino.ApplicationSettings.AppearanceSettings.DefaultLayerLineStylematerial index = -1iges level 
             = -1mode = NormalLayername = emptylayer index = 0 (ignored by AddLayer)
        
            Returns: A new layer instance.
        """
        pass

    def GetPersistentLocking(self):
        """
        GetPersistentLocking(self: Layer) -> bool
        
            The persistent locking setting is used for layers that can be locked by
                    a "parent" 
             object. A common case is when a layer is a child layer
                    (Layer.ParentI is not nil). 
             In this case, when a parent layer is locked,
                    then child layers are also locked. The 
             persistent locking setting
                    determines what happens when the parent is unlocked 
             again.
        """
        pass

    def GetPersistentVisibility(self):
        """
        GetPersistentVisibility(self: Layer) -> bool
        
            The persistent visbility setting is used for layers whose visibilty can
                    be changed 
             by a "parent" object. A common case is when a layer is a
                    child layer (ParentId is 
             not nil). In this case, when a parent layer is
                    turned off, then child layers are 
             also turned off. The persistent
                    visibility setting determines what happens when the 
             parent is turned on
                    again.
        """
        pass

    def GetUserString(self, key):
        """
        GetUserString(self: Layer, key: str) -> str
        
            Gets user string from this geometry.
        
            key: id used to retrieve the string.
            Returns: string associated with the key if successful. null if no key was found.
        """
        pass

    def GetUserStrings(self):
        """
        GetUserStrings(self: Layer) -> NameValueCollection
        
            Gets a copy of all (user key string, user value string) pairs attached to this geometry.
            Returns: A new collection.
        """
        pass

    def IsChildOf(self, *__args):
        """
        IsChildOf(self: Layer, otherLayer: Layer) -> bool
        IsChildOf(self: Layer, layerIndex: int) -> bool
        """
        pass

    def IsParentOf(self, *__args):
        """
        IsParentOf(self: Layer, otherLayer: Layer) -> bool
        IsParentOf(self: Layer, layerIndex: int) -> bool
        """
        pass

    @staticmethod
    def IsValidName(name):
        """
        IsValidName(name: str) -> bool
        
            Determines if a given string is valid for a layer name.
        
            name: A name to be validated.
            Returns: true if the name is valid for a layer name; otherwise, false.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def SetPersistentLocking(self, persistentLocking):
        """
        SetPersistentLocking(self: Layer, persistentLocking: bool)
            Set the persistent locking setting for this layer
        """
        pass

    def SetPersistentVisibility(self, persistentVisibility):
        """
        SetPersistentVisibility(self: Layer, persistentVisibility: bool)
            Set the persistent visibility setting for this layer
        """
        pass

    def SetUserString(self, key, value):
        """
        SetUserString(self: Layer, key: str, value: str) -> bool
        
            Attach a user string (key,value combination) to this geometry.
        
            key: id used to retrieve this string.
            value: string associated with key.
            Returns: true on success.
        """
        pass

    def ToString(self):
        """ ToString(self: Layer) -> str """
        pass

    def UnsetPersistentLocking(self):
        """
        UnsetPersistentLocking(self: Layer)
            Remove any explicity persistent locking settings from this layer
        """
        pass

    def UnsetPersistentVisibility(self):
        """
        UnsetPersistentVisibility(self: Layer)
            Remove any explicit persistent visibility setting from this layer
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the display color for this layer.

Get: Color(self: Layer) -> Color

Set: Color(self: Layer) = value
"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full path to this layer. The full path includes nesting information.

Get: FullPath(self: Layer) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ID of this layer object. 
            You typically do not need to assign a custom ID.

Get: Id(self: Layer) -> Guid

Set: Id(self: Layer) = value
"""

    IgesLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IGES level for this layer.

Get: IgesLevel(self: Layer) -> int

Set: IgesLevel(self: Layer) = value
"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this layer has been deleted and is 
            currently in the Undo buffer.

Get: IsDeleted(self: Layer) -> bool

"""

    IsExpanded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this layer is expanded in the Rhino Layer dialog.

Get: IsExpanded(self: Layer) -> bool

Set: IsExpanded(self: Layer) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the locked state of this layer.

Get: IsLocked(self: Layer) -> bool

Set: IsLocked(self: Layer) = value
"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicting whether this layer is a referenced layer. 
            Referenced layers are part of referenced documents.

Get: IsReference(self: Layer) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the visibility of this layer.

Get: IsVisible(self: Layer) -> bool

Set: IsVisible(self: Layer) = value
"""

    LayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of this layer.

Get: LayerIndex(self: Layer) -> int

Set: LayerIndex(self: Layer) = value
"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line-type index for this layer.

Get: LinetypeIndex(self: Layer) -> int

Set: LinetypeIndex(self: Layer) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of this layer.

Get: Name(self: Layer) -> str

Set: Name(self: Layer) = value
"""

    ParentLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ID of the parent layer. Layers can be origanized in a hierarchical structure, 
            in which case this returns the parent layer ID. If the layer has no parent, 
            Guid.Empty will be returned.

Get: ParentLayerId(self: Layer) -> Guid

Set: ParentLayerId(self: Layer) = value
"""

    PlotColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the plot color for this layer.

Get: PlotColor(self: Layer) -> Color

Set: PlotColor(self: Layer) = value
"""

    PlotWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the thickness of the plotting pen in millimeters. 
            A thickness of 0.0 indicates the "default" pen weight should be used.

Get: PlotWeight(self: Layer) -> float

Set: PlotWeight(self: Layer) = value
"""

    RenderMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Rhino.Render.RenderMaterial for objects on
            this layer that have MaterialSource() == MaterialFromLayer.
            A null result indicates that no Rhino.Render.RenderMaterial has
            been assigned  and the material created by the default Material
            constructor or the Rhino.DocObjects.Layer.RenderMaterialIndex should be used.

Get: RenderMaterial(self: Layer) -> RenderMaterial

Set: RenderMaterial(self: Layer) = value
"""

    RenderMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of render material for objects on this layer that have
            MaterialSource() == MaterialFromLayer. 
            A material index of -1 indicates no material has been assigned 
            and the material created by the default Material constructor 
            should be used.

Get: RenderMaterialIndex(self: Layer) -> int

Set: RenderMaterialIndex(self: Layer) = value
"""

    SortIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Runtime index used to sort layers in layer dialog.

Get: SortIndex(self: Layer) -> int

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of user strings.

Get: UserStringCount(self: Layer) -> int

"""



class LeaderObject(AnnotationObjectBase):
    """
    Represents a Rhino.Geometry.Leader that
                is picked in a document
    """

class LightObject(RhinoObject):
    # no doc
    def DuplicateLightGeometry(self):
        """ DuplicateLightGeometry(self: LightObject) -> Light """
        pass

    LightGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightGeometry(self: LightObject) -> Light

"""



class LinearDimensionObject(AnnotationObjectBase):
    """
    Represents a Rhino.Geometry.LinearDimension
                that is placed in a document.
    """
    DimensionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Rhino.DocObjects.DimensionStyle
            associated with this LinearDimensionObject.

Get: DimensionStyle(self: LinearDimensionObject) -> DimensionStyle

"""



class Linetype(CommonObject, IDisposable, ISerializable):
    """ Linetype() """
    def AppendSegment(self, length, isSolid):
        """
        AppendSegment(self: Linetype, length: float, isSolid: bool) -> int
        
            Adds a segment to the pattern.
        
            length: The length of the segment to be added.
            isSolid: If true, the length is interpreted as a line. If false,
                    then the length is 
             interpreted as a space.
        
            Returns: Index of the added segment.
        """
        pass

    def CommitChanges(self):
        """ CommitChanges(self: Linetype) -> bool """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Default(self):
        """
        Default(self: Linetype)
            Set linetype to default settings.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def GetSegment(self, index, length, isSolid):
        """
        GetSegment(self: Linetype, index: int) -> (float, bool)
        
            Gets the segment information at a index.
        
            index: Zero based index of the segment.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def RemoveSegment(self, index):
        """
        RemoveSegment(self: Linetype, index: int) -> bool
        
            Removes a segment in the linetype.
        
            index: Zero based index of the segment to remove.
            Returns: true if the segment index was removed.
        """
        pass

    def SetSegment(self, index, length, isSolid):
        """
        SetSegment(self: Linetype, index: int, length: float, isSolid: bool) -> bool
        
            Sets the length and type of the segment at index.
        
            index: Zero based index of the segment.
            length: The length of the segment to be added in millimeters.
            isSolid: If true, the length is interpreted as a line. If false,
                    then the length is 
             interpreted as a space.
        
            Returns: true if the operation was successful; otherwise false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ID of this linetype object.

Get: Id(self: Linetype) -> Guid

Set: Id(self: Linetype) = value
"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this linetype has been deleted and is 
            currently in the Undo buffer.

Get: IsDeleted(self: Linetype) -> bool

"""

    IsModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if this linetype has been modified by LinetypeTable.ModifyLinetype()
            and the modifications can be undone.

Get: IsModified(self: Linetype) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicting whether this linetype is a referenced linetype. 
            Referenced linetypes are part of referenced documents.

Get: IsReference(self: Linetype) -> bool

"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of this linetype.

Get: LinetypeIndex(self: Linetype) -> int

Set: LinetypeIndex(self: Linetype) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this linetype.

Get: Name(self: Linetype) -> str

Set: Name(self: Linetype) = value
"""

    PatternLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total length of one repeat of the pattern.

Get: PatternLength(self: Linetype) -> float

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of segments in the pattern.

Get: SegmentCount(self: Linetype) -> int

"""



class Material(CommonObject, IDisposable, ISerializable):
    """ Material() """
    def CommitChanges(self):
        """ CommitChanges(self: Material) -> bool """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Default(self):
        """
        Default(self: Material)
            Set material to default settings.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def GetBitmapTexture(self):
        """ GetBitmapTexture(self: Material) -> Texture """
        pass

    def GetBumpTexture(self):
        """
        GetBumpTexture(self: Material) -> Texture
        
            Gets the bump texture of this material.
            Returns: A texture; or null if no bump texture has been added to this material.
        """
        pass

    def GetEnvironmentTexture(self):
        """ GetEnvironmentTexture(self: Material) -> Texture """
        pass

    def GetTextures(self):
        """
        GetTextures(self: Material) -> Array[Texture]
        
            Get array of textures that this material uses
        """
        pass

    def GetTransparencyTexture(self):
        """ GetTransparencyTexture(self: Material) -> Texture """
        pass

    def GetUserString(self, key):
        """
        GetUserString(self: Material, key: str) -> str
        
            Gets a user string.
        
            key: id used to retrieve the string.
            Returns: string associated with the key if successful. null if no key was found.
        """
        pass

    def GetUserStrings(self):
        """
        GetUserStrings(self: Material) -> NameValueCollection
        
            Gets an independent copy of the collection of (user text key, user text value) pairs attached to 
             this object.
        
            Returns: A collection of key strings and values strings. This
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: Material) """
        pass

    def SetBitmapTexture(self, *__args):
        """
        SetBitmapTexture(self: Material, texture: Texture) -> bool
        SetBitmapTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetBumpTexture(self, *__args):
        """
        SetBumpTexture(self: Material, texture: Texture) -> bool
        SetBumpTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetEnvironmentTexture(self, *__args):
        """
        SetEnvironmentTexture(self: Material, texture: Texture) -> bool
        SetEnvironmentTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetTransparencyTexture(self, *__args):
        """
        SetTransparencyTexture(self: Material, texture: Texture) -> bool
        SetTransparencyTexture(self: Material, filename: str) -> bool
        """
        pass

    def SetUserString(self, key, value):
        """
        SetUserString(self: Material, key: str, value: str) -> bool
        
            Attach a user string (key,value combination) to this geometry.
        
            key: id used to retrieve this string.
            value: string associated with key.
            Returns: true on success.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AmbientColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientColor(self: Material) -> Color

Set: AmbientColor(self: Material) = value
"""

    DiffuseColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiffuseColor(self: Material) -> Color

Set: DiffuseColor(self: Material) = value
"""

    EmissionColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EmissionColor(self: Material) -> Color

Set: EmissionColor(self: Material) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ID of this material.

Get: Id(self: Material) -> Guid

"""

    IndexOfRefraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of refraction of the material, generally
            >= 1.0 (speed of light in vacuum)/(speed of light in material)

Get: IndexOfRefraction(self: Material) -> float

Set: IndexOfRefraction(self: Material) = value
"""

    IsDefaultMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default Rhino layers and objects are assigned the default rendering material.

Get: IsDefaultMaterial(self: Material) -> bool

"""

    IsDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deleted materials are kept in the runtime material table so that undo
            will work with materials.  Call IsDeleted to determine to determine if
            a material is deleted.

Get: IsDeleted(self: Material) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true this object may not be modified. Any properties or functions that attempt
            to modify this object when it is set to "IsReadOnly" will throw a NotSupportedException.

Get: IsDocumentControlled(self: Material) -> bool

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rhino allows multiple files to be viewed simultaneously. Materials in the
            document are "normal" or "reference". Reference materials are not saved.

Get: IsReference(self: Material) -> bool

"""

    MaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MaterialIndex(self: Material) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Material) -> str

Set: Name(self: Material) = value
"""

    ReflectionColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectionColor(self: Material) -> Color

Set: ReflectionColor(self: Material) = value
"""

    Reflectivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets how reflective a material is, 0f is no reflection
            1f is 100% reflective.

Get: Reflectivity(self: Material) -> float

Set: Reflectivity(self: Material) = value
"""

    RenderPlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the RenderPlugIn that is associated with this material.

Get: RenderPlugInId(self: Material) -> Guid

Set: RenderPlugInId(self: Material) = value
"""

    Shine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the shine factor of the material.

Get: Shine(self: Material) -> float

Set: Shine(self: Material) = value
"""

    SpecularColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecularColor(self: Material) -> Color

Set: SpecularColor(self: Material) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the transparency of the material (0.0 = opaque to 1.0 = transparent)

Get: Transparency(self: Material) -> float

Set: Transparency(self: Material) = value
"""

    TransparentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransparentColor(self: Material) -> Color

Set: TransparentColor(self: Material) = value
"""

    UseCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of objects and layers that use this material.

Get: UseCount(self: Material) -> int

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: Material) -> int

"""


    MaxShine = 255.0


class MaterialRef(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: MaterialRef) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BackFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the Material used to render the back of an object.

Get: BackFaceMaterialId(self: MaterialRef) -> Guid

"""

    BackFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the material used to render the back of an object

Get: BackFaceMaterialIndex(self: MaterialRef) -> int

"""

    FrontFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the Material used to render the front of an object.

Get: FrontFaceMaterialId(self: MaterialRef) -> Guid

"""

    FrontFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the material used to render the front of an object

Get: FrontFaceMaterialIndex(self: MaterialRef) -> int

"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the simple material should come from the object or from
            it's layer.

Get: MaterialSource(self: MaterialRef) -> ObjectMaterialSource

"""

    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies a rendering plug-in

Get: PlugInId(self: MaterialRef) -> Guid

"""



class MaterialRefCreateParams(object):
    """
    Options passed to MaterialRefs.Create
    
    MaterialRefCreateParams()
    """
    BackFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the Material used to render the back of an object.

Get: BackFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: BackFaceMaterialId(self: MaterialRefCreateParams) = value
"""

    BackFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the material used to render the back of an object

Get: BackFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: BackFaceMaterialIndex(self: MaterialRefCreateParams) = value
"""

    FrontFaceMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the Material used to render the front of an object.

Get: FrontFaceMaterialId(self: MaterialRefCreateParams) -> Guid

Set: FrontFaceMaterialId(self: MaterialRefCreateParams) = value
"""

    FrontFaceMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the material used to render the front of an object

Get: FrontFaceMaterialIndex(self: MaterialRefCreateParams) -> int

Set: FrontFaceMaterialIndex(self: MaterialRefCreateParams) = value
"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the simple material should come from the object or from
            it's layer.

Get: MaterialSource(self: MaterialRefCreateParams) -> ObjectMaterialSource

Set: MaterialSource(self: MaterialRefCreateParams) = value
"""

    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies a rendering plug-in

Get: PlugInId(self: MaterialRefCreateParams) -> Guid

Set: PlugInId(self: MaterialRefCreateParams) = value
"""



class MaterialRefs(object, IDictionary[Guid, MaterialRef], ICollection[KeyValuePair[Guid, MaterialRef]], IEnumerable[KeyValuePair[Guid, MaterialRef]], IEnumerable):
    """
    If you are developing a high quality plug-in renderer, and a user is
                assigning a custom render material to this object, then add rendering
                material information to the MaterialRefs dictionary.
                
                Note to developers:
                 As soon as the MaterialRefs dictionary contains items rendering
                 material queries slow down.  Do not populate the MaterialRefs
                dictionary when setting the MaterialIndex will take care of your needs.
    """
    def Add(self, *__args):
        """
        Add(self: MaterialRefs, key: Guid, value: MaterialRef)
            Add or replace an element with the provided key and value to this dictionary.
        
            key: The plug-in associated with this MaterialRef
            value: MaterialRef to add to this dictionary
        Add(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef])
        """
        pass

    def Clear(self):
        """
        Clear(self: MaterialRefs)
            Removes all items from this dictionary.
        """
        pass

    def Contains(self, item):
        """ Contains(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef]) -> bool """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: MaterialRefs, key: Guid) -> bool
        
            Determines whether this dictionary contains an MaterialRef with the
                    specified 
             plug-in id.
        
        
            key: The plug-in Id used to locate a MaterialRef in this dictionary.
            Returns: true if this dictionary contains an element with the specified plug-in
                    Id; 
             otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MaterialRefs, array: Array[KeyValuePair[Guid, MaterialRef]], arrayIndex: int) """
        pass

    def Create(self, createParams):
        """
        Create(self: MaterialRefs, createParams: MaterialRefCreateParams) -> MaterialRef
        
            Call this method to create a MaterialRef which can be used when calling
                    one of the 
             Add methods.
        
        
            createParams: Values used to initialize the MaterialRef
            Returns: A temporary MaterialRef object, the caller is responsible for disposing
                    of this 
             object.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MaterialRefs) -> IEnumerator[KeyValuePair[Guid, MaterialRef]]
        
            Returns an enumerator that iterates through this dictionary.
            Returns: A IEnumerator that can be used to iterate this dictionary.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: MaterialRefs, key: Guid) -> bool
        
            Removes the MaterialRef with the specified plug-in Id from this
                    dictionary.
        
            key: The plug-in Id for the MaterialRef to remove.
            Returns: true if the MaterialRef is successfully removed; otherwise, false. This
                    method also 
             returns false if key was not found in the original dictionary.
        
        Remove(self: MaterialRefs, item: KeyValuePair[Guid, MaterialRef]) -> bool
        """
        pass

    def TryGetValue(self, key, value):
        """
        TryGetValue(self: MaterialRefs, key: Guid) -> (bool, MaterialRef)
        
            Gets the value associated with the specified key.
        
            key: The plug-in Id whose MaterialRef to get.
            Returns: true if this dictionary contains a MaterialRef with the specified key;
                    otherwise, 
             false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Guid, MaterialRef], key: Guid) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in this dictionary

Get: Count(self: MaterialRefs) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IDictionary required property, always returns false for this dictionary.

Get: IsReadOnly(self: MaterialRefs) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an ICollection containing the plug-in Id's in this dictionary.

Get: Keys(self: MaterialRefs) -> ICollection[Guid]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an ICollection containing the MaterialRef objects in this
            dictionary.

Get: Values(self: MaterialRefs) -> ICollection[MaterialRef]

"""



class MeshObject(RhinoObject):
    # no doc
    def DuplicateMeshGeometry(self):
        """ DuplicateMeshGeometry(self: MeshObject) -> Mesh """
        pass

    def SetMesh(self, *args): #cannot find CLR method
        """
        SetMesh(self: MeshObject, mesh: Mesh) -> Mesh
        
            Only for developers who are defining custom subclasses of MeshObject.
                    Directly sets 
             the internal mesh geometry for this object.  Note that
                    this function does not work 
             with Rhino's "undo".
        
            Returns: The old mesh geometry that was set for this object
        """
        pass

    MeshGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshGeometry(self: MeshObject) -> Mesh

"""



class MorphControlObject(RhinoObject):
    """ Represents a Rhino.Geometry.MorphControlMorphControl in a document. """

class ObjectAttributes(CommonObject, IDisposable, ISerializable):
    """
    Attributes (color, material, layer,...) associated with a rhino object
    
    ObjectAttributes()
    """
    def AddToGroup(self, groupIndex):
        """
        AddToGroup(self: ObjectAttributes, groupIndex: int)
            Adds object to the group with specified index by appending index to
                    group list.
           
                      If the object is already in group, nothing is changed.
        
        
            groupIndex: The index that will be added.
        """
        pass

    def ComputedPlotColor(self, document, viewportId=None):
        """
        ComputedPlotColor(self: ObjectAttributes, document: RhinoDoc, viewportId: Guid) -> Color
        ComputedPlotColor(self: ObjectAttributes, document: RhinoDoc) -> Color
        """
        pass

    def ComputedPlotWeight(self, document, viewportId=None):
        """
        ComputedPlotWeight(self: ObjectAttributes, document: RhinoDoc, viewportId: Guid) -> float
        ComputedPlotWeight(self: ObjectAttributes, document: RhinoDoc) -> float
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def DrawColor(self, document, viewportId=None):
        """
        DrawColor(self: ObjectAttributes, document: RhinoDoc, viewportId: Guid) -> Color
        DrawColor(self: ObjectAttributes, document: RhinoDoc) -> Color
        """
        pass

    def Duplicate(self):
        """
        Duplicate(self: ObjectAttributes) -> ObjectAttributes
        
            Constructs a copy of this Rhino.DocObjects.ObjectAttributes instance.
            Returns: A new instance on success, or null on failure.
        """
        pass

    def GetGroupList(self):
        """
        GetGroupList(self: ObjectAttributes) -> Array[int]
        
            Returns an array of GroupCount group indices.  If GroupCount is zero, then GetGroupList() 
             returns null.
        
            Returns: An array of group indices. null might be retuned in place of an empty array.
        """
        pass

    def GetUserString(self, key):
        """
        GetUserString(self: ObjectAttributes, key: str) -> str
        
            Gets a user string.
        
            key: id used to retrieve the string.
            Returns: string associated with the key if successful. null if no key was found.
        """
        pass

    def GetUserStrings(self):
        """
        GetUserStrings(self: ObjectAttributes) -> NameValueCollection
        
            Gets an independent copy of the collection of (user text key, user text value) pairs attached to 
             this object.
        
            Returns: A collection of key strings and values strings. This
        """
        pass

    def HasDisplayModeOverride(self, viewportId):
        """
        HasDisplayModeOverride(self: ObjectAttributes, viewportId: Guid) -> bool
        
            Determines if an object has a display mode override for a given viewport.
        
            viewportId: Id of a Rhino Viewport.
            Returns: true if the object has a display mode override for the viewport; otherwise, false.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def RemoveDisplayModeOverride(self, rhinoViewportId=None):
        """
        RemoveDisplayModeOverride(self: ObjectAttributes, rhinoViewportId: Guid)
            By default, objects are drawn using the display mode of the viewport that
                    the 
             object is being drawn in. Setting a specific display mode, instructs
                    Rhino to 
             always use that display mode, regardless of the viewport's mode.
                    This function 
             resets an object to use the viewport's display mode.
        
        
            rhinoViewportId: viewport that display mode overrides should be cleared from.
        RemoveDisplayModeOverride(self: ObjectAttributes)
            By default, objects are drawn using the display mode of the viewport that
                    the 
             object is being drawn in. Setting a specific display mode, instructs
                    Rhino to 
             always use that display mode, regardless of the viewport's mode.
                    This function 
             resets an object to use the viewport's display mode for all
                    viewports.
        """
        pass

    def RemoveFromAllGroups(self):
        """
        RemoveFromAllGroups(self: ObjectAttributes)
            Removes object from all groups.
        """
        pass

    def RemoveFromGroup(self, groupIndex):
        """
        RemoveFromGroup(self: ObjectAttributes, groupIndex: int)
            removes object from the group with specified index.
                    If the object is not in the 
             group, nothing is changed.
        
        
            groupIndex: The index that will be removed.
        """
        pass

    def SetDisplayModeOverride(self, mode, rhinoViewportId=None):
        """
        SetDisplayModeOverride(self: ObjectAttributes, mode: DisplayModeDescription, rhinoViewportId: Guid) -> bool
        
            By default, objects are drawn using the display mode of the viewport that
                    the 
             object is being drawn in. Setting a specific display mode, instructs
                    Rhino to 
             always use that display mode, regardless of the viewport's mode.
                    This version sets 
             a display mode for a specific viewport.
        
        
            mode: The display mode.
            rhinoViewportId: The Rhino viewport ID.
            Returns: true on success.
        SetDisplayModeOverride(self: ObjectAttributes, mode: DisplayModeDescription) -> bool
        
            By default, objects are drawn using the display mode of the viewport that
                    the 
             object is being drawn in. Setting a specific display mode, instructs
                    Rhino to 
             always use that display mode, regardless of the viewport's mode.
                    This version 
             affects the object's display mode for all viewports.
        
        
            mode: The display mode.
            Returns: true if setting was successful.
        """
        pass

    def SetUserString(self, key, value):
        """
        SetUserString(self: ObjectAttributes, key: str, value: str) -> bool
        
            Attach a user string (key,value combination) to this geometry.
        
            key: id used to retrieve this string.
            value: string associated with key. If null, the key will be removed
            Returns: true on success.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ColorSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color used to display an object is specified in one of three ways.
            If ColorSource is ON::color_from_layer, then the object's layer ON_Layer::Color() is used.
            If ColorSource is ON::color_from_object, then value of m_color is used.
            If ColorSource is ON::color_from_material, then the diffuse color of the object's
            render material is used.  See ON_3dmObjectAttributes::MaterialSource() to
            determine where to get the definition of the object's render material.

Get: ColorSource(self: ObjectAttributes) -> ObjectColorSource

Set: ColorSource(self: ObjectAttributes) = value
"""

    Decals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all object decals associated with this object.

Get: Decals(self: ObjectAttributes) -> Decals

"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Display order used to force objects to be drawn on top or behind each other.
            Larger numbers draw on top of smaller numbers.
            0  = draw object in standard depth buffered order<0 = draw object behind "normal" draw order objects>0 = draw object on top of "normal" draw order objects

Get: DisplayOrder(self: ObjectAttributes) -> int

Set: DisplayOrder(self: ObjectAttributes) = value
"""

    GroupCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of groups object belongs to.

Get: GroupCount(self: ObjectAttributes) -> int

"""

    HasMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A mapping from any plugin source is associated with these attributes
            Need to do this here to respond correctly to ModifyObjectAttributes event

Get: HasMapping(self: ObjectAttributes) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDocumentControlled(self: ObjectAttributes) -> bool

"""

    IsInstanceDefinitionObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this query to determine if an object is part of an instance definition.

Get: IsInstanceDefinitionObject(self: ObjectAttributes) -> bool

"""

    LayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an associated layer index.
            Layer definitions in an OpenNURBS model are stored in a layer table.
            The layer table is conceptually an array of ON_Layer classes.  Every
            OpenNURBS object in a model is on some layer.  The object's layer
            is specified by zero based indicies into the ON_Layer array.

Get: LayerIndex(self: ObjectAttributes) -> int

Set: LayerIndex(self: ObjectAttributes) = value
"""

    LinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the linetype index.
            Linetype definitions in an OpenNURBS model are stored in a linetype table.
            The linetype table is conceptually an array of ON_Linetype classes. Every
            OpenNURBS object in a model references some linetype.  The object's linetype
            is specified by zero based indicies into the ON_Linetype array.Index 0 is reserved for continuous linetype (no pattern).

Get: LinetypeIndex(self: ObjectAttributes) -> int

Set: LinetypeIndex(self: ObjectAttributes) = value
"""

    LinetypeSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Linetype used to display an object is specified in one of two ways.
            If LinetypeSource is ON::linetype_from_layer, then the object's layer ON_Layer::Linetype() is used.
            If LinetypeSource is ON::linetype_from_object, then value of m_linetype is used.

Get: LinetypeSource(self: ObjectAttributes) -> ObjectLinetypeSource

Set: LinetypeSource(self: ObjectAttributes) = value
"""

    MaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the material index.
            If you want something simple and fast, set the index of
            the rendering material.

Get: MaterialIndex(self: ObjectAttributes) -> int

Set: MaterialIndex(self: ObjectAttributes) = value
"""

    MaterialRefs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If you are developing a high quality plug-in renderer, and a user is
            assigning a custom render material to this object, then add rendering
            material information to the MaterialRefs dictionary.
            
            Note to developers:
             As soon as the MaterialRefs dictionary contains items rendering
             material queries slow down.  Do not populate the MaterialRefs
            dictionary when setting the MaterialIndex will take care of your needs.

Get: MaterialRefs(self: ObjectAttributes) -> MaterialRefs

"""

    MaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the simple material should come from the object or from it's layer.
            High quality rendering plug-ins should use m_rendering_attributes.

Get: MaterialSource(self: ObjectAttributes) -> ObjectMaterialSource

Set: MaterialSource(self: ObjectAttributes) = value
"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object must be in one of three modes: normal, locked or hidden.
            If an object is in normal mode, then the object's layer controls visibility
            and selectability. If an object is locked, then the object's layer controls
            visibility by the object cannot be selected. If the object is hidden, it is
            not visible and it cannot be selected.

Get: Mode(self: ObjectAttributes) -> ObjectMode

Set: Mode(self: ObjectAttributes) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object optional text name.
            More than one object in a model can have the same name and
            some objects may have no name.

Get: Name(self: ObjectAttributes) -> str

Set: Name(self: ObjectAttributes) = value
"""

    ObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If ON::color_from_object == ColorSource, then color is the object's display color.

Get: ObjectColor(self: ObjectAttributes) -> Color

Set: ObjectColor(self: ObjectAttributes) = value
"""

    ObjectDecoration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used to indicate an object has a decoration (like an arrowhead on a curve)

Get: ObjectDecoration(self: ObjectAttributes) -> ObjectDecoration

Set: ObjectDecoration(self: ObjectAttributes) = value
"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Every object has a Guid (globally unique identifier, also known as UUID, or universally
            unique identifier). The default value is Guid.Empty.
            
            When an object is added to a model, the value is checked.  If the value is Guid.Empty, a
            new Guid is created. If the value is not null but it is already used by another object
            in the model, a new Guid is created. If the value is not Guid.Empty and it is not used by
            another object in the model, then that value persists. When an object is updated, by
            a move for example, the value of ObjectId persists.
            This value is the same as the one returned by object.Id.

Get: ObjectId(self: ObjectAttributes) -> Guid

Set: ObjectId(self: ObjectAttributes) = value
"""

    PlotColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If plot_color_from_object == PlotColorSource, then PlotColor is the object's plotting color.

Get: PlotColor(self: ObjectAttributes) -> Color

Set: PlotColor(self: ObjectAttributes) = value
"""

    PlotColorSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color used to plot an object on paper is specified in one of three ways.
            If PlotColorSource is ON::plot_color_from_layer, then the object's layer ON_Layer::PlotColor() is used.
            If PlotColorSource is ON::plot_color_from_object, then value of PlotColor() is used.

Get: PlotColorSource(self: ObjectAttributes) -> ObjectPlotColorSource

Set: PlotColorSource(self: ObjectAttributes) = value
"""

    PlotWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plot weight in millimeters.
            =0.0 means use the default width
            <0.0 means don't plot (visible for screen display, but does not show on plot)

Get: PlotWeight(self: ObjectAttributes) -> float

Set: PlotWeight(self: ObjectAttributes) = value
"""

    PlotWeightSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWeightSource(self: ObjectAttributes) -> ObjectPlotWeightSource

Set: PlotWeightSource(self: ObjectAttributes) = value
"""

    Space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Starting with V4, objects can be in either model space or page space.
            If an object is in page space, then ViewportId is not nil and
            identifies the page it is on.

Get: Space(self: ObjectAttributes) -> ActiveSpace

Set: Space(self: ObjectAttributes) = value
"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: ObjectAttributes) -> int

"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If ViewportId is nil, the object is active in all viewports. If ViewportId is not nil, then 
            this object is only active in a specific view. This field is primarily used to assign page
            space objects to a specific page, but it can also be used to restrict model space to a
            specific view.

Get: ViewportId(self: ObjectAttributes) -> Guid

Set: ViewportId(self: ObjectAttributes) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object visibility.

Get: Visible(self: ObjectAttributes) -> bool

Set: Visible(self: ObjectAttributes) = value
"""

    WireDensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When a surface object is displayed in wireframe, this controls
            how many isoparametric wires are used.
            value    number of isoparametric wires
            -1       boundary wires (off)
            0        boundary and knot wires 
            1        boundary and knot wires and, if there are no interior knots, a single interior wire.
            N>=2     boundary and knot wires and (N+1) interior wires.

Get: WireDensity(self: ObjectAttributes) -> int

Set: WireDensity(self: ObjectAttributes) = value
"""



class ObjectColorSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the source of display color of single objects.
    
    enum ObjectColorSource, values: ColorFromLayer (0), ColorFromMaterial (2), ColorFromObject (1), ColorFromParent (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ColorFromLayer = None
    ColorFromMaterial = None
    ColorFromObject = None
    ColorFromParent = None
    value__ = None


class ObjectDecoration(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines bit mask values to represent object decorations.
    
    enum (flags) ObjectDecoration, values: BothArrowhead (24), EndArrowhead (16), None (0), StartArrowhead (8)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BothArrowhead = None
    EndArrowhead = None
    None = None
    StartArrowhead = None
    value__ = None


class ObjectEnumeratorSettings(object):
    """
    Settings used for getting an enumerator of objects in a document
                See Rhino.Collections.ObjectTable.GetEnumerator()
    
    ObjectEnumeratorSettings()
    """
    ActiveObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveObjects(self: ObjectEnumeratorSettings) -> bool

Set: ActiveObjects(self: ObjectEnumeratorSettings) = value
"""

    ClassTypeFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassTypeFilter(self: ObjectEnumeratorSettings) -> Type

Set: ClassTypeFilter(self: ObjectEnumeratorSettings) = value
"""

    DeletedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeletedObjects(self: ObjectEnumeratorSettings) -> bool

Set: DeletedObjects(self: ObjectEnumeratorSettings) = value
"""

    HiddenObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HiddenObjects(self: ObjectEnumeratorSettings) -> bool

Set: HiddenObjects(self: ObjectEnumeratorSettings) = value
"""

    IdefObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When true, ONLY Instance Definitions will be returned

Get: IdefObjects(self: ObjectEnumeratorSettings) -> bool

Set: IdefObjects(self: ObjectEnumeratorSettings) = value
"""

    IncludeGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeGrips(self: ObjectEnumeratorSettings) -> bool

Set: IncludeGrips(self: ObjectEnumeratorSettings) = value
"""

    IncludeLights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeLights(self: ObjectEnumeratorSettings) -> bool

Set: IncludeLights(self: ObjectEnumeratorSettings) = value
"""

    IncludePhantoms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludePhantoms(self: ObjectEnumeratorSettings) -> bool

Set: IncludePhantoms(self: ObjectEnumeratorSettings) = value
"""

    LayerIndexFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerIndexFilter(self: ObjectEnumeratorSettings) -> int

Set: LayerIndexFilter(self: ObjectEnumeratorSettings) = value
"""

    LockedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockedObjects(self: ObjectEnumeratorSettings) -> bool

Set: LockedObjects(self: ObjectEnumeratorSettings) = value
"""

    NameFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameFilter(self: ObjectEnumeratorSettings) -> str

Set: NameFilter(self: ObjectEnumeratorSettings) = value
"""

    NormalObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalObjects(self: ObjectEnumeratorSettings) -> bool

Set: NormalObjects(self: ObjectEnumeratorSettings) = value
"""

    ObjectTypeFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectTypeFilter(self: ObjectEnumeratorSettings) -> ObjectType

Set: ObjectTypeFilter(self: ObjectEnumeratorSettings) = value
"""

    ReferenceObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceObjects(self: ObjectEnumeratorSettings) -> bool

Set: ReferenceObjects(self: ObjectEnumeratorSettings) = value
"""

    SelectedObjectsFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedObjectsFilter(self: ObjectEnumeratorSettings) -> bool

Set: SelectedObjectsFilter(self: ObjectEnumeratorSettings) = value
"""

    ViewportFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Filter on value of object->IsActiveInViewport()

Get: ViewportFilter(self: ObjectEnumeratorSettings) -> RhinoViewport

Set: ViewportFilter(self: ObjectEnumeratorSettings) = value
"""

    VisibleFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisibleFilter(self: ObjectEnumeratorSettings) -> bool

Set: VisibleFilter(self: ObjectEnumeratorSettings) = value
"""



class ObjectLinetypeSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the source of linetype of single objects.
    
    enum ObjectLinetypeSource, values: LinetypeFromLayer (0), LinetypeFromObject (1), LinetypeFromParent (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LinetypeFromLayer = None
    LinetypeFromObject = None
    LinetypeFromParent = None
    value__ = None


class ObjectMaterialSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the source of material of single objects.
    
    enum ObjectMaterialSource, values: MaterialFromLayer (0), MaterialFromObject (1), MaterialFromParent (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MaterialFromLayer = None
    MaterialFromObject = None
    MaterialFromParent = None
    value__ = None


class ObjectMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the display and behavior of single objects.
    
    enum ObjectMode, values: Hidden (1), InstanceDefinitionObject (3), Locked (2), Normal (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Hidden = None
    InstanceDefinitionObject = None
    Locked = None
    Normal = None
    value__ = None


class ObjectPlotColorSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the source of plotting/printing color of single objects.
    
    enum ObjectPlotColorSource, values: PlotColorFromDisplay (2), PlotColorFromLayer (0), PlotColorFromObject (1), PlotColorFromParent (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlotColorFromDisplay = None
    PlotColorFromLayer = None
    PlotColorFromObject = None
    PlotColorFromParent = None
    value__ = None


class ObjectPlotWeightSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the source of plotting/printing weight of single objects.
    
    enum ObjectPlotWeightSource, values: PlotWeightFromLayer (0), PlotWeightFromObject (1), PlotWeightFromParent (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlotWeightFromLayer = None
    PlotWeightFromObject = None
    PlotWeightFromParent = None
    value__ = None


class ObjectType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines binary mask values for each object type that can be found in a document.
    
    enum (flags) ObjectType, values: Annotation (512), AnyObject (4294967295), Brep (16), BrepLoop (524288), Cage (134217728), ClipPlane (536870912), Curve (4), Detail (32768), EdgeFilter (4194304), Extrusion (1073741824), Grip (16384), Hatch (65536), InstanceDefinition (2048), InstanceReference (4096), Light (256), Mesh (32), MeshEdge (33554432), MeshFace (67108864), MeshVertex (16777216), MorphControl (131072), None (0), Phantom (268435456), Point (1), PointSet (2), PolyedgeFilter (8388608), PolysrfFilter (2097152), Surface (8), TextDot (8192)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Annotation = None
    AnyObject = None
    Brep = None
    BrepLoop = None
    Cage = None
    ClipPlane = None
    Curve = None
    Detail = None
    EdgeFilter = None
    Extrusion = None
    Grip = None
    Hatch = None
    InstanceDefinition = None
    InstanceReference = None
    Light = None
    Mesh = None
    MeshEdge = None
    MeshFace = None
    MeshVertex = None
    MorphControl = None
    None = None
    Phantom = None
    Point = None
    PointSet = None
    PolyedgeFilter = None
    PolysrfFilter = None
    Surface = None
    TextDot = None
    value__ = None


class ObjRef(object, IDisposable):
    """
    Represents a reference to a Rhino object.
    
    ObjRef(id: Guid)
    ObjRef(rhinoObject: RhinoObject)
    ObjRef(rhinoObject: RhinoObject, pickContext: PickContext)
    """
    def Brep(self):
        """
        Brep(self: ObjRef) -> Brep
        
            Gets the brep if this reference geometry is one.
            Returns: A boundary representation; or null on error.
        """
        pass

    def ClippingPlaneSurface(self):
        """
        ClippingPlaneSurface(self: ObjRef) -> ClippingPlaneSurface
        
            Gets the clipping plane surface if this reference targeted one.
            Returns: A clipping plane surface, or null if this reference targeted something else.
        """
        pass

    def Curve(self):
        """
        Curve(self: ObjRef) -> Curve
        
            Gets the curve if this reference targeted one.
            Returns: A curve, or null if this reference targeted something else.
        """
        pass

    def CurveParameter(self, parameter):
        """
        CurveParameter(self: ObjRef) -> (Curve, float)
        
            If the reference geometry is a curve or edge with a selection
                    point, then this gets 
             the parameter of the selection point.
        
            Returns: If the selection point was on a curve or edge, then the
                    curve/edge is returned, 
             otherwise null.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ObjRef)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Edge(self):
        """
        Edge(self: ObjRef) -> BrepEdge
        
            Gets the edge if this reference geometry is one.
            Returns: A boundary representation edge; or null on error.
        """
        pass

    def Face(self):
        """
        Face(self: ObjRef) -> BrepFace
        
            If the referenced geometry is a brep face, a brep with one face, or
                    a surface, this 
             returns the brep face.
        
            Returns: A boundary representation face; or null on error.
        """
        pass

    def Geometry(self):
        """
        Geometry(self: ObjRef) -> GeometryBase
        
            Gets the geometry linked to the object targeted by this reference.
            Returns: The geometry.
        """
        pass

    def Hatch(self):
        """
        Hatch(self: ObjRef) -> Hatch
        
            Gets the hatch if the referenced geometry is one.
            Returns: A hatch; or null if the referenced object is not a hatch
        """
        pass

    def Light(self):
        """
        Light(self: ObjRef) -> Light
        
            Gets the light if the referenced geometry is one.
            Returns: A light; or null if the referenced object is not a light, or on error.
        """
        pass

    def Mesh(self):
        """
        Mesh(self: ObjRef) -> Mesh
        
            Gets the mesh if the referenced geometry is one.
            Returns: A mesh; or null if the referenced object is not a mesh, or on error.
        """
        pass

    def Object(self):
        """
        Object(self: ObjRef) -> RhinoObject
        
            Returns the referenced Rhino object.
        """
        pass

    def Point(self):
        """
        Point(self: ObjRef) -> Point
        
            Gets the point if the referenced geometry is one.
            Returns: A point; or null if the referenced object is not a point, or on error.
        """
        pass

    def PointCloud(self):
        """
        PointCloud(self: ObjRef) -> PointCloud
        
            Gets the point cloud if the referenced geometry is one.
            Returns: A point cloud; or null if the referenced object is not a point cloud, or on error.
        """
        pass

    def SelectionMethod(self):
        """
        SelectionMethod(self: ObjRef) -> SelectionMethod
        
            Gets the method used to select this object.
            Returns: The method used to select this object.
        """
        pass

    def SelectionPoint(self):
        """
        SelectionPoint(self: ObjRef) -> Point3d
        
            If the object was selected by picking a point on it, then
                    SelectionPoint() returns 
             the point where the selection
                    occured, otherwise it returns Point3d.Unset.
        
            Returns: The point where the selection occured or Point3d.Unset on failure.
        """
        pass

    def SetSelectionComponent(self, componentIndex):
        """
        SetSelectionComponent(self: ObjRef, componentIndex: ComponentIndex)
            When an object is selected by picking a sub-object, SetSelectionComponent
                    may be 
             used to identify the sub-object.
        """
        pass

    def Surface(self):
        """
        Surface(self: ObjRef) -> Surface
        
            Gets the surface if the referenced geometry is one.
            Returns: A surface; or null if the referenced object is not a surface, or on error.
        """
        pass

    def SurfaceParameter(self, u, v):
        """
        SurfaceParameter(self: ObjRef) -> (Surface, float, float)
        
            If the reference geometry is a surface, brep with one face,
                    or surface edge with a 
             selection point, then this gets the 
                    surface paramters of the selection point.
        
            Returns: If the selection point was on a surface, then the surface is returned.
        """
        pass

    def TextDot(self):
        """
        TextDot(self: ObjRef) -> TextDot
        
            Gets the text dot if the referenced geometry is one.
            Returns: A text dot; or null if the referenced object is not a text dot, or on error.
        """
        pass

    def TextEntity(self):
        """
        TextEntity(self: ObjRef) -> TextEntity
        
            Gets the text entity if the referenced geometry is one.
            Returns: A text entity; or null if the referenced object is not a text entity, or on error.
        """
        pass

    def Trim(self):
        """
        Trim(self: ObjRef) -> BrepTrim
        
            If the referenced geometry is an edge of a surface,
                    this returns the associated 
             brep trim.
        
            Returns: A boundary representation trim; or null on error
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, id: Guid)
        __new__(cls: type, rhinoObject: RhinoObject)
        __new__(cls: type, rhinoObject: RhinoObject, pickContext: PickContext)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GeometryComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component index of the referenced (sub) geometry.
            Some objects have subobjects that are valid pieces of geometry. For
            example, breps have edges and faces that are valid curves and surfaces.
            Each subobject has a component index that is > 0. The parent
            geometry has a component index = -1.

Get: GeometryComponentIndex(self: ObjRef) -> ComponentIndex

"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the id of the referenced Rhino object.

Get: ObjectId(self: ObjRef) -> Guid

"""

    RuntimeSerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If > 0, then this is the value of a Rhino object's serial number field.
            The serial number is used instead of the pointer to prevent crashes in
            cases when the RhinoObject is deleted but an ObjRef continues to reference
            the Rhino object. The value of RuntimeSerialNumber is not saved in archives
            because it generally changes if you save and reload an archive.

Get: RuntimeSerialNumber(self: ObjRef) -> UInt32

"""



class PointCloudObject(RhinoObject):
    # no doc
    def DuplicatePointCloudGeometry(self):
        """ DuplicatePointCloudGeometry(self: PointCloudObject) -> PointCloud """
        pass

    PointCloudGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointCloudGeometry(self: PointCloudObject) -> PointCloud

"""



class PointObject(RhinoObject):
    # no doc
    def DuplicatePointGeometry(self):
        """ DuplicatePointGeometry(self: PointObject) -> Point """
        pass

    PointGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGeometry(self: PointObject) -> Point

"""



class RadialDimensionObject(AnnotationObjectBase):
    """ A radius style dimension """

class ReplayHistoryData(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: ReplayHistoryData) """
        pass

    def GetRhinoObjRef(self, id):
        """
        GetRhinoObjRef(self: ReplayHistoryData, id: int) -> ObjRef
        
            In ReplayHistory, use GetRhinoObjRef to convert the information
                    in a history record 
             into the ObjRef that has up to date
                    RhinoObject pointers
        
        
            id: HistoryRecord value id
            Returns: ObjRef on success, null if not successful
        """
        pass

    def TryGetBool(self, id, value):
        """ TryGetBool(self: ReplayHistoryData, id: int) -> (bool, bool) """
        pass

    def TryGetColor(self, id, value):
        """ TryGetColor(self: ReplayHistoryData, id: int) -> (bool, Color) """
        pass

    def TryGetDouble(self, id, value):
        """ TryGetDouble(self: ReplayHistoryData, id: int) -> (bool, float) """
        pass

    def TryGetGuid(self, id, value):
        """ TryGetGuid(self: ReplayHistoryData, id: int) -> (bool, Guid) """
        pass

    def TryGetInt(self, id, value):
        """ TryGetInt(self: ReplayHistoryData, id: int) -> (bool, int) """
        pass

    def TryGetPoint3d(self, id, value):
        """ TryGetPoint3d(self: ReplayHistoryData, id: int) -> (bool, Point3d) """
        pass

    def TryGetString(self, id, value):
        """ TryGetString(self: ReplayHistoryData, id: int) -> (bool, str) """
        pass

    def TryGetTransform(self, id, value):
        """ TryGetTransform(self: ReplayHistoryData, id: int) -> (bool, Transform) """
        pass

    def TryGetVector3d(self, id, value):
        """ TryGetVector3d(self: ReplayHistoryData, id: int) -> (bool, Vector3d) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document this record belongs to

Get: Document(self: ReplayHistoryData) -> RhinoDoc

"""

    HistoryVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ReplayHistory overrides check the version number to insure the information
            saved in the history record is compatible with the current implementation
            of ReplayHistory

Get: HistoryVersion(self: ReplayHistoryData) -> int

"""

    RecordId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Each history record has a unique id that Rhino assigns when it adds the
            history record to the history record table

Get: RecordId(self: ReplayHistoryData) -> Guid

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ReplayHistoryData) -> Array[ReplayHistoryResult]

"""



class ReplayHistoryResult(object):
    # no doc
    def UpdateToAngularDimension(self, dimension, attributes):
        """ UpdateToAngularDimension(self: ReplayHistoryResult, dimension: AngularDimension, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToArc(self, arc, attributes):
        """ UpdateToArc(self: ReplayHistoryResult, arc: Arc, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToBrep(self, brep, attributes):
        """ UpdateToBrep(self: ReplayHistoryResult, brep: Brep, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToCircle(self, circle, attributes):
        """ UpdateToCircle(self: ReplayHistoryResult, circle: Circle, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToClippingPlane(self, plane, uMagnitude, vMagnitude, *__args):
        """
        UpdateToClippingPlane(self: ReplayHistoryResult, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid], attributes: ObjectAttributes) -> bool
        UpdateToClippingPlane(self: ReplayHistoryResult, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid, attributes: ObjectAttributes) -> bool
        """
        pass

    def UpdateToCurve(self, curve, attributes):
        """ UpdateToCurve(self: ReplayHistoryResult, curve: Curve, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToEllipse(self, ellipse, attributes):
        """ UpdateToEllipse(self: ReplayHistoryResult, ellipse: Ellipse, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToExtrusion(self, extrusion, attributes):
        """ UpdateToExtrusion(self: ReplayHistoryResult, extrusion: Extrusion, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToHatch(self, hatch, attributes):
        """ UpdateToHatch(self: ReplayHistoryResult, hatch: Hatch, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToLeader(self, leader, attributes):
        """ UpdateToLeader(self: ReplayHistoryResult, leader: Leader, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToLine(self, from, to, attributes):
        """ UpdateToLine(self: ReplayHistoryResult, from: Point3d, to: Point3d, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToLinearDimension(self, dimension, attributes):
        """ UpdateToLinearDimension(self: ReplayHistoryResult, dimension: LinearDimension, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToMesh(self, mesh, attributes):
        """ UpdateToMesh(self: ReplayHistoryResult, mesh: Mesh, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToPoint(self, point, attributes):
        """ UpdateToPoint(self: ReplayHistoryResult, point: Point3d, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToPointCloud(self, *__args):
        """
        UpdateToPointCloud(self: ReplayHistoryResult, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> bool
        UpdateToPointCloud(self: ReplayHistoryResult, cloud: PointCloud, attributes: ObjectAttributes) -> bool
        """
        pass

    def UpdateToPolyline(self, points, attributes):
        """ UpdateToPolyline(self: ReplayHistoryResult, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToRadialDimension(self, dimension, attributes):
        """ UpdateToRadialDimension(self: ReplayHistoryResult, dimension: RadialDimension, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToSphere(self, sphere, attributes):
        """ UpdateToSphere(self: ReplayHistoryResult, sphere: Sphere, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToSurface(self, surface, attributes):
        """ UpdateToSurface(self: ReplayHistoryResult, surface: Surface, attributes: ObjectAttributes) -> bool """
        pass

    def UpdateToText(self, text, *__args):
        """
        UpdateToText(self: ReplayHistoryResult, text: TextEntity, attributes: ObjectAttributes) -> bool
        UpdateToText(self: ReplayHistoryResult, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes) -> bool
        """
        pass

    def UpdateToTextDot(self, dot, attributes):
        """ UpdateToTextDot(self: ReplayHistoryResult, dot: TextDot, attributes: ObjectAttributes) -> bool """
        pass

    ExistingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExistingObject(self: ReplayHistoryResult) -> RhinoObject

"""



class RhinoDeselectAllObjectsEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RhinoDeselectAllObjectsEventArgs) -> RhinoDoc

"""

    ObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectCount(self: RhinoDeselectAllObjectsEventArgs) -> int

"""



class RhinoModifyObjectAttributesEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RhinoModifyObjectAttributesEventArgs) -> RhinoDoc

"""

    NewAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewAttributes(self: RhinoModifyObjectAttributesEventArgs) -> ObjectAttributes

"""

    OldAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldAttributes(self: RhinoModifyObjectAttributesEventArgs) -> ObjectAttributes

"""

    RhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoObject(self: RhinoModifyObjectAttributesEventArgs) -> RhinoObject

"""



class RhinoObjectEventArgs(EventArgs):
    # no doc
    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: RhinoObjectEventArgs) -> Guid

"""

    TheObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TheObject(self: RhinoObjectEventArgs) -> RhinoObject

"""



class RhinoObjectSelectionEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RhinoObjectSelectionEventArgs) -> RhinoDoc

"""

    RhinoObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoObjects(self: RhinoObjectSelectionEventArgs) -> Array[RhinoObject]

"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if objects are being selected.
            Returns false if objects are being deseleced.

Get: Selected(self: RhinoObjectSelectionEventArgs) -> bool

"""



class RhinoReplaceObjectEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RhinoReplaceObjectEventArgs) -> RhinoDoc

"""

    NewRhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewRhinoObject(self: RhinoReplaceObjectEventArgs) -> RhinoObject

"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: RhinoReplaceObjectEventArgs) -> Guid

"""

    OldRhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldRhinoObject(self: RhinoReplaceObjectEventArgs) -> RhinoObject

"""



class RhinoTransformObjectsEventArgs(EventArgs):
    """ EventArgs passed to RhinoDoc.BeforeTransform. """
    ObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectCount(self: RhinoTransformObjectsEventArgs) -> int

"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: RhinoTransformObjectsEventArgs) -> Array[RhinoObject]

"""

    ObjectsWillBeCopied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectsWillBeCopied(self: RhinoTransformObjectsEventArgs) -> bool

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: RhinoTransformObjectsEventArgs) -> Transform

"""



class SelectionMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for several kinds of selection methods.
    
    enum SelectionMethod, values: CrossingBox (3), MousePick (1), Other (0), WindowBox (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CrossingBox = None
    MousePick = None
    Other = None
    value__ = None
    WindowBox = None


class SurfaceObject(RhinoObject):
    """ Represents a Rhino.Geometry.Surfacesurface in a document. """
    def DuplicateSurfaceGeometry(self):
        """
        DuplicateSurfaceGeometry(self: SurfaceObject) -> Surface
        
            Constructs a new deep copy of the surface geometry.
            Returns: The copy of the geometry.
        """
        pass

    SurfaceGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the surface geometry linked with this object.

Get: SurfaceGeometry(self: SurfaceObject) -> Surface

"""



class TextDisplayAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the line alignment of text.
    
    enum TextDisplayAlignment, values: AboveLine (2), Horizontal (1), InLine (3), Normal (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AboveLine = None
    Horizontal = None
    InLine = None
    Normal = None
    value__ = None


class TextDotObject(RhinoObject):
    """ Represents a text dot that is a document. """

class TextObject(AnnotationObjectBase):
    """
    Represents a text object in a document.
                This is a wrapper for CRhinoAnnotationText.
    """
    TextGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text entity geometry of this text object.

Get: TextGeometry(self: TextObject) -> TextEntity

"""



class Texture(CommonObject, IDisposable, ISerializable):
    """
    Represents a texture that is mapped on objects.
    
    Texture()
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def GetAlphaBlendValues(self, constant, a0, a1, a2, a3):
        """
        GetAlphaBlendValues(self: Texture) -> (float, float, float, float, float)
        
            If the TextureCombineMode is Blend, then the blending function
                    for alpha is 
             determined by
                    
                    new alpha = constant
                                + 
             a0*(current alpha)
                                + a1*(texture alpha)
                                + 
             a2*min(current alpha,texture alpha)
                                + a3*max(current alpha,texture 
             alpha)
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def SetAlphaBlendValues(self, constant, a0, a1, a2, a3):
        """
        SetAlphaBlendValues(self: Texture, constant: float, a0: float, a1: float, a2: float, a3: float)
            If the TextureCombineMode is Blend, then the blending function
                    for alpha is 
             determined by
                    
                    new alpha = constant
                                + 
             a0*(current alpha)
                                + a1*(texture alpha)
                                + 
             a2*min(current alpha,texture alpha)
                                + a3*max(current alpha,texture 
             alpha)
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ApplyUvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true then the UVW transform is applied to the texture
            otherwise the UVW transform is ignored.

Get: ApplyUvwTransform(self: Texture) -> bool

Set: ApplyUvwTransform(self: Texture) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the texture is enabled then it will be visible in the rendered
            display otherwise it will not.

Get: Enabled(self: Texture) -> bool

Set: Enabled(self: Texture) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a file name that is used by this texture.
            NOTE: this filename may well not be a path that makes sense
            on a user's computer because it was a path initially set on
            a different user's computer. If you want to get a workable path
            for this user, use the BitmapTable.Find function using this
            property.

Get: FileName(self: Texture) -> str

Set: FileName(self: Texture) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the globally unique identifier of this texture.

Get: Id(self: Texture) -> Guid

"""

    MappingChannelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MappingChannelId(self: Texture) -> int

"""

    TextureCombineMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines how this texture is combined with others in a material's
            texture list.

Get: TextureCombineMode(self: Texture) -> TextureCombineMode

Set: TextureCombineMode(self: Texture) = value
"""

    TextureType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls how the pixels in the bitmap are interpreted

Get: TextureType(self: Texture) -> TextureType

Set: TextureType(self: Texture) = value
"""

    UvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transform to be applied to each instance of this texture
            if ApplyUvw is true

Get: UvwTransform(self: Texture) -> Transform

Set: UvwTransform(self: Texture) = value
"""

    WrapU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture wrapping mode in the U direction

Get: WrapU(self: Texture) -> TextureUvwWrapping

Set: WrapU(self: Texture) = value
"""

    WrapV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture wrapping mode in the V direction

Get: WrapV(self: Texture) -> TextureUvwWrapping

Set: WrapV(self: Texture) = value
"""

    WrapW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture wrapping mode in the W direction

Get: WrapW(self: Texture) -> TextureUvwWrapping

Set: WrapW(self: Texture) = value
"""



class TextureCombineMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Determines how this texture is combined with others in a material's
                texture list.
    
    enum TextureCombineMode, values: Blend (3), Decal (2), Modulate (1), None (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Blend = None
    Decal = None
    Modulate = None
    None = None
    value__ = None


class TextureType(Enum, IComparable, IFormattable, IConvertible):
    """
    The TextureType controls how the pixels in the bitmap
                are interpreted.
    
    enum TextureType, values: Bitmap (1), Bump (2), None (0), Transparency (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bitmap = None
    Bump = None
    None = None
    Transparency = None
    value__ = None


class TextureUvwWrapping(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines Texture UVW wrapping modes
    
    enum TextureUvwWrapping, values: Clamp (1), Repeat (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Clamp = None
    Repeat = None
    value__ = None


class ViewInfo(object, IDisposable):
    """
    Represents the name and orientation of a View (and named view).
                views can be thought of as cameras.
    """
    def Dispose(self):
        """
        Dispose(self: ViewInfo)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the NamedView.

Get: Name(self: ViewInfo) -> str

Set: Name(self: ViewInfo) = value
"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the viewport, or viewing frustum, associated with this view.

Get: Viewport(self: ViewInfo) -> ViewportInfo

"""



class ViewportInfo(object, IDisposable, ISerializable):
    """
    Represents a viewing frustum.
    
    ViewportInfo()
    ViewportInfo(other: ViewportInfo)
    ViewportInfo(rhinoViewport: RhinoViewport)
    """
    def ChangeToParallelProjection(self, symmetricFrustum):
        """
        ChangeToParallelProjection(self: ViewportInfo, symmetricFrustum: bool) -> bool
        
            Use this function to change projections of valid viewports
                    from parallel to 
             perspective.  It will make common additional
                    adjustments to the frustum and camera 
             location so the resulting
                    views are similar.  The camera direction and target point 
             are
                    not be changed.
                    If the current projection is parallel and 
             symmetricFrustum,
                    FrustumIsLeftRightSymmetric() and FrustumIsTopBottomSymmetric()
         
                        are all equal, then no changes are made and true is returned.
        
        
            symmetricFrustum: true if you want the resulting frustum to be symmetric.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def ChangeToPerspectiveProjection(self, targetDistance, symmetricFrustum, lensLength):
        """
        ChangeToPerspectiveProjection(self: ViewportInfo, targetDistance: float, symmetricFrustum: bool, lensLength: float) -> bool
        
            Use this function to change projections of valid viewports
                    from parallel to 
             perspective.  It will make common additional
                    adjustments to the frustum and camera 
             location so the resulting
                    views are similar.  The camera direction and target point 
             are
                    not changed.
                    If the current projection is perspective and 
             symmetricFrustum,
                    IsFrustumIsLeftRightSymmetric, and IsFrustumIsTopBottomSymmetric
        
                         are all equal, then no changes are made and true is returned.
        
        
            targetDistance: If RhinoMath.UnsetValue this parameter is ignored.
                    Otherwise it must be > 0 and 
             indicates which plane in the current view frustum should be perserved.
        
            symmetricFrustum: true if you want the resulting frustum to be symmetric.
            lensLength: (pass 50.0 when in doubt)
                    35 mm lens length to use when changing from parallel
            
                     to perspective projections. If the current projection
                    is perspective or 
             lens_length is <= 0.0,
                    then this parameter is ignored.
        
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def ChangeToSymmetricFrustum(self, isLeftRightSymmetric, isTopBottomSymmetric, targetDistance):
        """
        ChangeToSymmetricFrustum(self: ViewportInfo, isLeftRightSymmetric: bool, isTopBottomSymmetric: bool, targetDistance: float) -> bool
        
            If needed, adjusts the current frustum so it has the 
                    specified symmetries and 
             adjust the camera location
                    so the target plane remains visible.
        
        
            isLeftRightSymmetric: If true, the frustum will be adjusted so left = -right.
            isTopBottomSymmetric: If true, the frustum will be adjusted so top = -bottom.
            targetDistance: If projection is not perspective or target_distance is RhinoMath.UnsetValue,
                    then 
             this parameter is ignored. If the projection is perspective and targetDistance
                    is 
             not RhinoMath.UnsetValue, then it must be > 0.0 and it is used to determine
                    which 
             plane in the old frustum will appear unchanged in the new frustum.
        
            Returns: Returns true if the viewport has now a frustum with the specified symmetries.
        """
        pass

    def ChangeToTwoPointPerspectiveProjection(self, targetDistance, up, lensLength):
        """
        ChangeToTwoPointPerspectiveProjection(self: ViewportInfo, targetDistance: float, up: Vector3d, lensLength: float) -> bool
        
            Changes projections of valid viewports
                    to a two point perspective.  It will make 
             common additional
                    adjustments to the frustum and camera location and direction
            
                     so the resulting views are similar.
                    If the current projection is 
             perspective and
                    IsFrustumIsLeftRightSymmetric is true and
                    
             IsFrustumIsTopBottomSymmetric is false, then no changes are
                    made and true is 
             returned.
        
        
            targetDistance: If RhinoMath.UnsetValue this parameter is ignored.  Otherwise
                    it must be > 0 and 
             indicates which plane in the current 
                    view frustum should be perserved.
        
            up: The locked up direction. Pass Vector3d.Zero if you want to use the world
                    axis 
             direction that is closest to the current up direction.
                    Pass CameraY() if you want 
             to preserve the current up direction.
        
            lensLength: (pass 50.0 when in doubt)
                    35 mm lens length to use when changing from parallel
            
                     to perspective projections. If the current projection
                    is perspective or 
             lens_length is <= 0.0,
                    then this parameter is ignored.
        
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ViewportInfo)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def DollyCamera(self, dollyVector):
        """
        DollyCamera(self: ViewportInfo, dollyVector: Vector3d) -> bool
        
            DollyCamera() does not update the frustum's clipping planes.
                    To update the 
             frustum's clipping planes call DollyFrustum(d)
                    with d = dollyVector o cameraFrameZ. 
              To convert screen locations
                    into a dolly vector, use GetDollyCameraVector().
             
                    Does not update frustum.  To update frustum use DollyFrustum(d) with d = dollyVector o 
             cameraFrameZ.
        
        
            dollyVector: dolly vector in world coordinates.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def DollyExtents(self, *__args):
        """
        DollyExtents(self: ViewportInfo, cameraCoordinateBoundingBox: BoundingBox, border: float) -> bool
        
            Dolly the camera location and so that the view frustum contains
                    all of the document 
             objects that can be seen in view.
                    If the projection is perspective, the camera 
             angle is not changed.
        
        
            border: If border > 1.0, then the fustum in enlarged by this factor
                    to provide a border 
             around the view.  1.1 works well for
                    parallel projections; 0.0 is suggested for 
             perspective projections.
        
            Returns: True if successful.
        DollyExtents(self: ViewportInfo, geometry: IEnumerable[GeometryBase], border: float) -> bool
        """
        pass

    def DollyFrustum(self, dollyDistance):
        """
        DollyFrustum(self: ViewportInfo, dollyDistance: float) -> bool
        
            Moves the frustum clipping planes.
        
            dollyDistance: Distance to move in camera direction.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def Extents(self, halfViewAngleRadians, *__args):
        """
        Extents(self: ViewportInfo, halfViewAngleRadians: float, sphere: Sphere) -> bool
        
            Extends this viewport view to include a sphere.
                    Use Extents() as a quick way to set 
             a viewport to so that bounding
                    volume is inside of a viewports frustrum.
                  
               The view angle is used to determine the position of the camera.
        
        
            halfViewAngleRadians: 1/2 smallest subtended view angle in radians.
            sphere: A sphere in 3d world coordinates.
            Returns: true if the operation succeeded; otherwise, false.
        Extents(self: ViewportInfo, halfViewAngleRadians: float, bbox: BoundingBox) -> bool
        
            Extends this viewport view to include a bounding box.
                    Use Extents() as a quick way 
             to set a viewport to so that bounding
                    volume is inside of a viewports frustrum.
           
                      The view angle is used to determine the position of the camera.
        
        
            halfViewAngleRadians: 1/2 smallest subtended view angle in radians.
            bbox: A bounding box in 3d world coordinates.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def FrustumCenterPoint(self, targetDistance):
        """
        FrustumCenterPoint(self: ViewportInfo, targetDistance: float) -> Point3d
        
            Return a point on the central axis of the view frustum.
                    This point is a good choice 
             for a general purpose target point.
        
        
            targetDistance: If targetDistance > 0.0, then the distance from the returned
                    point to the camera 
             plane will be targetDistance. Note that
                    if the frustum is not symmetric, the 
             distance from the
                    returned point to the camera location will be larger than
               
                  targetDistance.
                    If targetDistance == ON_UNSET_VALUE and the frustum
                  
               is valid with near > 0.0, then 0.5*(near + far) will be used
                    as the 
             targetDistance.
        
            Returns: A point on the frustum's central axis.  If the viewport or input
                    is not valid, then 
             ON_3dPoint::UnsetPoint is returned.
        """
        pass

    def GetBoundingBoxDepth(self, bbox, nearDistance, farDistance):
        """
        GetBoundingBoxDepth(self: ViewportInfo, bbox: BoundingBox) -> (bool, float, float)
        
            Gets near and far clipping distances of a bounding box.
                    This function ignores the 
             current value of the viewport's 
                    near and far settings. If the viewport is a 
             perspective
                    projection, the it intersects the semi infinite frustum
                    
             volume with the bounding box and returns the near and far
                    distances of the 
             intersection.  If the viewport is a parallel
                    projection, it instersects the infinte 
             view region with the
                    bounding box and returns the near and far distances of the
           
                      projection.
        
        
            bbox: The bounding box to sample.
            Returns: true if the bounding box intersects the view frustum and near_dist/far_dist were set. 
                 
                false if the bounding box does not intesect the view frustum.
        """
        pass

    def GetCameraAngles(self, halfDiagonalAngleRadians, halfVerticalAngleRadians, halfHorizontalAngleRadians):
        """
        GetCameraAngles(self: ViewportInfo) -> (bool, float, float, float)
        
            Gets the field of view angles.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def GetCameraFrame(self, location, cameraX, cameraY, cameraZ):
        """
        GetCameraFrame(self: ViewportInfo) -> (bool, Point3d, Vector3d, Vector3d, Vector3d)
        
            Gets location and vectors of this camera.
            Returns: true if current camera orientation is valid; otherwise false.
        """
        pass

    def GetDollyCameraVector(self, *__args):
        """
        GetDollyCameraVector(self: ViewportInfo, screen0: Point, screen1: Point, projectionPlaneDistance: float) -> Vector3d
        
            Gets a world coordinate dolly vector that can be passed to DollyCamera().
        
            screen0: Start point.
            screen1: End point.
            projectionPlaneDistance: Distance of projection plane from camera. When in doubt, use 0.5*(frus_near+frus_far).
            Returns: The world coordinate dolly vector.
        GetDollyCameraVector(self: ViewportInfo, screenX0: int, screenY0: int, screenX1: int, screenY1: int, projectionPlaneDistance: float) -> Vector3d
        
            Gets a world coordinate dolly vector that can be passed to DollyCamera().
        
            screenX0: Screen coords of start point.
            screenY0: Screen coords of start point.
            screenX1: Screen coords of end point.
            screenY1: Screen coords of end point.
            projectionPlaneDistance: Distance of projection plane from camera. When in doubt, use 0.5*(frus_near+frus_far).
            Returns: The world coordinate dolly vector.
        """
        pass

    def GetFarPlaneCorners(self):
        """
        GetFarPlaneCorners(self: ViewportInfo) -> Array[Point3d]
        
            Gets the corners of far clipping plane rectangle.
                    4 points are returned in the 
             order of bottom left, bottom right,
                    top left, top right.
        
            Returns: Four corner points on success.
                    Empty array if viewport is not valid.
        """
        pass

    def GetFrustum(self, left, right, bottom, top, nearDistance, farDistance):
        """
        GetFrustum(self: ViewportInfo) -> (bool, float, float, float, float, float, float)
        
            Gets the view frustum.
            Returns: true if operation succeeded; otherwise, false.
        """
        pass

    def GetFrustumLine(self, *__args):
        """
        GetFrustumLine(self: ViewportInfo, screenPoint: PointF) -> Line
        
            Gets the world coordinate line in the view frustum
                    that projects to a point on the 
             screen.
        
        
            screenPoint: screen location
            Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 
             clipping plane.
        
        GetFrustumLine(self: ViewportInfo, screenPoint: Point) -> Line
        
            Gets the world coordinate line in the view frustum
                    that projects to a point on the 
             screen.
        
        
            screenPoint: screen location
            Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 
             clipping plane.
        
        GetFrustumLine(self: ViewportInfo, screenX: float, screenY: float) -> Line
        
            Gets the world coordinate line in the view frustum
                    that projects to a point on the 
             screen.
        
        
            screenX: (screenx,screeny) = screen location.
            screenY: (screenx,screeny) = screen location.
            Returns: 3d world coordinate line segment starting on the near clipping plane and ending on the far 
             clipping plane.
        """
        pass

    def GetNearPlaneCorners(self):
        """
        GetNearPlaneCorners(self: ViewportInfo) -> Array[Point3d]
        
            Gets the corners of near clipping plane rectangle.
                    4 points are returned in the 
             order of bottom left, bottom right,
                    top left, top right.
        
            Returns: Four corner points on success.
                    Empty array if viewport is not valid.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ViewportInfo, info: SerializationInfo, context: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 
             target object.
        
        
            info: The System.Runtime.Serialization.SerializationInfo to populate with data.
            context: The destination (see System.Runtime.Serialization.StreamingContext) for this serialization.
        """
        pass

    def GetPointDepth(self, point, distance):
        """
        GetPointDepth(self: ViewportInfo, point: Point3d) -> (bool, float)
        
            Gets the clipping distance of a point. This function ignores the
                    current value of 
             the viewport's near and far settings. If
                    the viewport is a perspective projection, 
             then it intersects
                    the semi infinite frustum volume with the bounding box and
             
                    returns the near and far distances of the intersection.
                    If the viewport is a 
             parallel projection, it instersects the
                    infinte view region with the bounding box 
             and returns the
                    near and far distances of the projection.
        
        
            point: A point to measure.
            Returns: true if the bounding box intersects the view frustum and
                    near_dist/far_dist were 
             set.
                    false if the bounding box does not intesect the view frustum.
        """
        pass

    def GetScreenPort(self, near=None, far=None):
        """
        GetScreenPort(self: ViewportInfo) -> Rectangle
        
            Gets the location of viewport in pixels.
                    See documentation for 
             Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S
             ystem.Int32,System.Int32)SetScreenPort.
        
            Returns: The rectangle, or System.Drawing.Rectangle.EmptyEmpty rectangle on error.
        GetScreenPort(self: ViewportInfo) -> (Rectangle, int, int)
        
            Gets the location of viewport in pixels.
                    See value meanings in 
             Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S
             ystem.Int32,System.Int32)SetScreenPort.
        
            Returns: The rectangle, or System.Drawing.Rectangle.EmptyEmpty rectangle on error.
        """
        pass

    def GetSphereDepth(self, sphere, nearDistance, farDistance):
        """
        GetSphereDepth(self: ViewportInfo, sphere: Sphere) -> (bool, float, float)
        
            Gets near and far clipping distances of a bounding sphere.
        
            sphere: The sphere to sample.
            Returns: true if the sphere intersects the view frustum and near_dist/far_dist were set.
                    
             false if the sphere does not intesect the view frustum.
        """
        pass

    def GetWorldToScreenScale(self, pointInFrustum):
        """
        GetWorldToScreenScale(self: ViewportInfo, pointInFrustum: Point3d) -> float
        
            Gets the scale factor from point in frustum to screen scale.
        
            pointInFrustum: point in viewing frustum.
            Returns: number of pixels per world unit at the 3d point.
        """
        pass

    def GetXform(self, sourceSystem, destinationSystem):
        """
        GetXform(self: ViewportInfo, sourceSystem: CoordinateSystem, destinationSystem: CoordinateSystem) -> Transform
        
            Computes a transform from a coordinate system to another.
        
            sourceSystem: The coordinate system to map from.
            destinationSystem: The coordinate system to map into.
            Returns: The 4x4 transformation matrix (acts on the left).
        """
        pass

    def SetCameraDirection(self, direction):
        """
        SetCameraDirection(self: ViewportInfo, direction: Vector3d) -> bool
        
            Sets the direction that the camera faces.
        
            direction: A new direction.
            Returns: true if the direction was set; otherwise false.
        """
        pass

    def SetCameraLocation(self, location):
        """
        SetCameraLocation(self: ViewportInfo, location: Point3d) -> bool
        
            Sets the camera location (position) point.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def SetCameraUp(self, up):
        """
        SetCameraUp(self: ViewportInfo, up: Vector3d) -> bool
        
            Sets the camera up vector.
        
            up: A new direction.
            Returns: true if the direction was set; otherwise false.
        """
        pass

    def SetFrustum(self, left, right, bottom, top, nearDistance, farDistance):
        """
        SetFrustum(self: ViewportInfo, left: float, right: float, bottom: float, top: float, nearDistance: float, farDistance: float) -> bool
        
            Sets the view frustum. If FrustumSymmetryIsLocked() is true
                    and left != -right or 
             bottom != -top, then they will be
                    adjusted so the resulting frustum is symmetric.
        
        
            left: A new left value.
            right: A new right value.
            bottom: A new bottom value.
            top: A new top value.
            nearDistance: A new near distance value.
            farDistance: A new far distance value.
            Returns: true if operation succeeded; otherwise, false.
        """
        pass

    def SetFrustumNearFar(self, *__args):
        """
        SetFrustumNearFar(self: ViewportInfo, nearDistance: float, farDistance: float) -> bool
        
            Sets the frustum near and far distances using two values.
        
            nearDistance: The new near distance.
            farDistance: The new far distance.
            Returns: true if operation succeeded; otherwise, false.
        SetFrustumNearFar(self: ViewportInfo, nearDistance: float, farDistance: float, minNearDistance: float, minNearOverFar: float, targetDistance: float) -> bool
        
            Sets near and far clipping distance subject to constraints.
        
            nearDistance: (>0) desired near clipping distance.
            farDistance: (>near_dist) desired near clipping distance.
            minNearDistance: If min_near_dist <= 0.0, it is ignored.
                    If min_near_dist > 0 and near_dist < 
             min_near_dist, then the frustum's near_dist will be increased to min_near_dist.
        
            minNearOverFar: If min_near_over_far <= 0.0, it is ignored.
                    If near_dist < 
             far_dist*min_near_over_far, then
                    near_dist is increased and/or far_dist is 
             decreased
                    so that near_dist = far_dist*min_near_over_far.
                    If near_dist 
             < target_dist < far_dist, then near_dist
                    near_dist is increased and far_dist is 
             decreased so that
                    projection precision will be good at target_dist.
                    
             Otherwise, near_dist is simply set to 
                    far_dist*min_near_over_far.
        
            targetDistance: If target_dist <= 0.0, it is ignored.
                    If target_dist > 0, it is used as described 
             in the
                    description of the min_near_over_far parameter.
        
            Returns: true if operation succeeded; otherwise, false.
        SetFrustumNearFar(self: ViewportInfo, boundingBox: BoundingBox) -> bool
        
            Sets the frustum near and far using a bounding box.
        
            boundingBox: A bounding box to use.
            Returns: true if operation succeeded; otherwise, false.
        SetFrustumNearFar(self: ViewportInfo, center: Point3d, radius: float) -> bool
        
            Sets the frustum near and far using a center point and radius.
        
            center: A center point.
            radius: A radius value.
            Returns: true if operation succeeded; otherwise, false.
        """
        pass

    def SetScreenPort(self, *__args):
        """
        SetScreenPort(self: ViewportInfo, windowRectangle: Rectangle) -> bool
        
            Gets the location of viewport in pixels.
                    See value meanings in 
             Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S
             ystem.Int32,System.Int32)SetScreenPort.
        
        
            windowRectangle: A new rectangle.
            Returns: true if input is valid.
        SetScreenPort(self: ViewportInfo, windowRectangle: Rectangle, near: int, far: int) -> bool
        
            Gets the location of viewport in pixels.
                    See value meanings in 
             Rhino.DocObjects.ViewportInfo.SetScreenPort(System.Int32,System.Int32,System.Int32,System.Int32,S
             ystem.Int32,System.Int32)SetScreenPort.
        
        
            windowRectangle: A new rectangle.
            near: The near value.
            far: The far value.
            Returns: true if input is valid.
        SetScreenPort(self: ViewportInfo, left: int, right: int, bottom: int, top: int, near: int, far: int) -> bool
        
            Location of viewport in pixels.
                    These are provided so you can set the port you are 
             using
                    and get the appropriate transformations to and from
                    screen 
             space.
                    // For a Windows window
                    /      int width = width of window 
             client area in pixels;
                    /      int height = height of window client area in pixels;
        
                         /      port_left = 0;
                    /      port_right = width;
                    /      
             port_top = 0;
                    /      port_bottom = height;
                    /      port_near = 0;
             
                    /      port_far = 1;
                    /      SetScreenPort( port_left, port_right, 
                 
                /                     port_bottom, port_top, 
                    /                     port_near, 
             port_far );
        
        
            left: A left value.
            right: A left value. (port_left != port_right)
            bottom: A bottom value.
            top: A top value. (port_top != port_bottom)
            near: A near value.
            far: A far value.
            Returns: true if input is valid.
        """
        pass

    def TargetDistance(self, useFrustumCenterFallback):
        """
        TargetDistance(self: ViewportInfo, useFrustumCenterFallback: bool) -> float
        
            Gets the distance from the target point to the camera plane.
                    Note that if the 
             frustum is not symmetric, then this distance
                    is shorter than the distance from the 
             target to the camera location.
        
        
            useFrustumCenterFallback: If bUseFrustumCenterFallback is false and the target point is
                    not valid, then 
             ON_UNSET_VALUE is returned.
                    If bUseFrustumCenterFallback is true and the frustum is 
             valid
                    and current target point is not valid or is behind the camera,
                    
             then 0.5*(near + far) is returned.
        
            Returns: Shortest signed distance from camera plane to target point.
                    If the target point is 
             on the visible side of the camera,
                    a positive value is returned.  ON_UNSET_VALUE is 
             returned
                    when the input of view is not valid.
        """
        pass

    def UnlockCamera(self):
        """
        UnlockCamera(self: ViewportInfo)
            Unlocks the camera vectors and location.
        """
        pass

    def UnlockFrustumSymmetry(self):
        """
        UnlockFrustumSymmetry(self: ViewportInfo)
            Unlocks frustum horizontal and vertical symmetries.
        """
        pass

    def ZoomToScreenRect(self, *__args):
        """
        ZoomToScreenRect(self: ViewportInfo, windowRectangle: Rectangle) -> bool
        
            Zooms to a screen zone.
                    View changing from screen input points. Handy for
                 
                using a mouse to manipulate a view.
                    ZoomToScreenRect() may change camera and 
             frustum settings.
        
        
            windowRectangle: The new window rectangle in screen space.
            Returns: true if the operation succeeded; otherwise, false.
        ZoomToScreenRect(self: ViewportInfo, left: int, top: int, right: int, bottom: int) -> bool
        
            Zooms to a screen zone.
                    View changing from screen input points. Handy for
                 
                using a mouse to manipulate a view.
                    ZoomToScreenRect() may change camera and 
             frustum settings.
        
        
            left: Screen coord.
            top: Screen coord.
            right: Screen coord.
            bottom: Screen coord.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: ViewportInfo)
        __new__(cls: type, rhinoViewport: RhinoViewport)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Camera35mmLensLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property assumes the camera is horizontal and crop the
            film rather than the image when the aspect of the frustum
            is not 36/24.  (35mm film is 36mm wide and 24mm high.)
            Setting preserves camera location,
            changes the frustum, but maintains the frustum's aspect.

Get: Camera35mmLensLength(self: ViewportInfo) -> float

Set: Camera35mmLensLength(self: ViewportInfo) = value
"""

    CameraAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 1/2 smallest angle. See Rhino.DocObjects.ViewportInfo.GetCameraAngles(System.Double@,System.Double@,System.Double@) for more information.

Get: CameraAngle(self: ViewportInfo) -> float

Set: CameraAngle(self: ViewportInfo) = value
"""

    CameraDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction that the camera faces.

Get: CameraDirection(self: ViewportInfo) -> Vector3d

"""

    CameraLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the camera location (position) point.

Get: CameraLocation(self: ViewportInfo) -> Point3d

"""

    CameraUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the camera up vector.

Get: CameraUp(self: ViewportInfo) -> Vector3d

"""

    CameraX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit "to the right" vector.

Get: CameraX(self: ViewportInfo) -> Vector3d

"""

    CameraY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit "up" vector.

Get: CameraY(self: ViewportInfo) -> Vector3d

"""

    CameraZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit vector in -CameraDirection.

Get: CameraZ(self: ViewportInfo) -> Vector3d

"""

    FrustumAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Setting FrustumAspect changes the larger of the frustum's width/height
            so that the resulting value of width/height matches the requested
            aspect.  The camera angle is not changed.  If you change the shape
            of the view port with a call SetScreenPort(), then you generally 
            want to call SetFrustumAspect() with the value returned by 
            GetScreenPortAspect().

Get: FrustumAspect(self: ViewportInfo) -> float

Set: FrustumAspect(self: ViewportInfo) = value
"""

    FrustumBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum bottom value. This is -top if the frustum has a horizontal symmetry axis.
            This number is usually negative.

Get: FrustumBottom(self: ViewportInfo) -> float

"""

    FrustumBottomPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum bottom plane that separates visibile from off-screen.

Get: FrustumBottomPlane(self: ViewportInfo) -> Plane

"""

    FrustumCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum center point.

Get: FrustumCenter(self: ViewportInfo) -> Point3d

"""

    FrustumFar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum far-cutting value.

Get: FrustumFar(self: ViewportInfo) -> float

"""

    FrustumFarPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets far clipping plane if camera and frustum
            are valid.  The plane's frame is the same as the camera's
            frame.  The origin is located at the intersection of the
            camera direction ray and the far clipping plane. The plane's
            normal points into the frustum towards the camera location.

Get: FrustumFarPlane(self: ViewportInfo) -> Plane

"""

    FrustumHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum height. This is Rhino.DocObjects.ViewportInfo.FrustumTop - Rhino.DocObjects.ViewportInfo.FrustumBottom.

Get: FrustumHeight(self: ViewportInfo) -> float

"""

    FrustumLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum left value. This is -right if the frustum has a vertical symmetry axis.
            This number is usually negative.

Get: FrustumLeft(self: ViewportInfo) -> float

"""

    FrustumLeftPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum left plane that separates visibile from off-screen.

Get: FrustumLeftPlane(self: ViewportInfo) -> Plane

"""

    FrustumMaximumDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum maximum diameter, or the maximum between Rhino.DocObjects.ViewportInfo.FrustumWidth and Rhino.DocObjects.ViewportInfo.FrustumHeight.

Get: FrustumMaximumDiameter(self: ViewportInfo) -> float

"""

    FrustumMinimumDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum minimum diameter, or the minimum between Rhino.DocObjects.ViewportInfo.FrustumWidth and Rhino.DocObjects.ViewportInfo.FrustumHeight.

Get: FrustumMinimumDiameter(self: ViewportInfo) -> float

"""

    FrustumNear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum near-cutting value.

Get: FrustumNear(self: ViewportInfo) -> float

"""

    FrustumNearPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets near clipping plane if camera and frustum
            are valid.  The plane's frame is the same as the camera's
            frame.  The origin is located at the intersection of the
            camera direction ray and the near clipping plane. The plane's
            normal points out of the frustum towards the camera
            location.

Get: FrustumNearPlane(self: ViewportInfo) -> Plane

"""

    FrustumRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum right value. This is -left if the frustum has a vertical symmetry axis.
            This number is usually positive.

Get: FrustumRight(self: ViewportInfo) -> float

"""

    FrustumRightPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum right plane that separates visibile from off-screen.

Get: FrustumRightPlane(self: ViewportInfo) -> Plane

"""

    FrustumTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum top value. This is -bottom if the frustum has a horizontal symmetry axis.
            This number is usually positive.

Get: FrustumTop(self: ViewportInfo) -> float

"""

    FrustumTopPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum top plane that separates visibile from off-screen.

Get: FrustumTopPlane(self: ViewportInfo) -> Plane

"""

    FrustumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the frustum width. This is Rhino.DocObjects.ViewportInfo.FrustumRight - Rhino.DocObjects.ViewportInfo.FrustumLeft.

Get: FrustumWidth(self: ViewportInfo) -> float

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the viewport's id to the value used to 
            uniquely identify this viewport.
            There is no approved way to change the viewport 
            id once it is set in order to maintain consistency
            across multiple viewports and those routines that 
            manage them.

Get: Id(self: ViewportInfo) -> Guid

"""

    IsCameraDirectionLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the direction that the camera faces is unmodifiable.

Get: IsCameraDirectionLocked(self: ViewportInfo) -> bool

Set: IsCameraDirectionLocked(self: ViewportInfo) = value
"""

    IsCameraLocationLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the camera location is unmodifiable.

Get: IsCameraLocationLocked(self: ViewportInfo) -> bool

Set: IsCameraLocationLocked(self: ViewportInfo) = value
"""

    IsCameraUpLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the camera up vector is unmodifiable.

Get: IsCameraUpLocked(self: ViewportInfo) -> bool

Set: IsCameraUpLocked(self: ViewportInfo) = value
"""

    IsFrustumLeftRightSymmetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the camera frustum has a vertical symmetry axis.

Get: IsFrustumLeftRightSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumLeftRightSymmetric(self: ViewportInfo) = value
"""

    IsFrustumTopBottomSymmetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the camera frustum has a horizontal symmetry axis.

Get: IsFrustumTopBottomSymmetric(self: ViewportInfo) -> bool

Set: IsFrustumTopBottomSymmetric(self: ViewportInfo) = value
"""

    IsParallelProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set whether this projection is parallel.

Get: IsParallelProjection(self: ViewportInfo) -> bool

Set: IsParallelProjection(self: ViewportInfo) = value
"""

    IsPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set whether this projection is perspective.

Get: IsPerspectiveProjection(self: ViewportInfo) -> bool

Set: IsPerspectiveProjection(self: ViewportInfo) = value
"""

    IsTwoPointPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this projection is a two-point perspective.

Get: IsTwoPointPerspectiveProjection(self: ViewportInfo) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this complete object is valid.

Get: IsValid(self: ViewportInfo) -> bool

"""

    IsValidCamera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the camera is valid.

Get: IsValidCamera(self: ViewportInfo) -> bool

"""

    IsValidFrustum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the frustum is valid.

Get: IsValidFrustum(self: ViewportInfo) -> bool

"""

    ScreenPortAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the sceen aspect ratio.
            This is width / height.

Get: ScreenPortAspect(self: ViewportInfo) -> float

"""

    TargetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current value of the target point.  This point does not play
            a role in the view projection calculations.  It can be used as a 
            fixed point when changing the camera so the visible regions of the
            before and after frustums both contain the region of interest.
            The default constructor sets this point on ON_3dPoint::UnsetPoint.
            You must explicitly call one SetTargetPoint() functions to set
            the target point.

Get: TargetPoint(self: ViewportInfo) -> Point3d

Set: TargetPoint(self: ViewportInfo) = value
"""

    ViewScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Applies scaling factors to parallel projection clipping coordinates
            by setting the m_clip_mod transformation. 
            If you want to compress the view projection across the viewing
            plane, then set x = 0.5, y = 1.0, and z = 1.0.

Get: ViewScale(self: ViewportInfo) -> SizeF

Set: ViewScale(self: ViewportInfo) = value
"""



# variables with complex values

