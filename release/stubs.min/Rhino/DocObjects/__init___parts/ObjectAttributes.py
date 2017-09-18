class ObjectAttributes(CommonObject,IDisposable,ISerializable):
 """
 Attributes (color,material,layer,...) associated with a rhino object

 

 ObjectAttributes()
 """
 def AddToGroup(self,groupIndex):
  """
  AddToGroup(self: ObjectAttributes,groupIndex: int)

   Adds object to the group with specified index by appending index to

     group list.

     

       If the object is already in group,nothing is changed.

  

  

   groupIndex: The index that will be added.
  """
  pass
 def ComputedPlotColor(self,document,viewportId=None):
  """
  ComputedPlotColor(self: ObjectAttributes,document: RhinoDoc,viewportId: Guid) -> Color

  ComputedPlotColor(self: ObjectAttributes,document: RhinoDoc) -> Color
  """
  pass
 def ComputedPlotWeight(self,document,viewportId=None):
  """
  ComputedPlotWeight(self: ObjectAttributes,document: RhinoDoc,viewportId: Guid) -> float

  ComputedPlotWeight(self: ObjectAttributes,document: RhinoDoc) -> float
  """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def DrawColor(self,document,viewportId=None):
  """
  DrawColor(self: ObjectAttributes,document: RhinoDoc,viewportId: Guid) -> Color

  DrawColor(self: ObjectAttributes,document: RhinoDoc) -> Color
  """
  pass
 def Duplicate(self):
  """
  Duplicate(self: ObjectAttributes) -> ObjectAttributes

  

   Constructs a copy of this Rhino.DocObjects.ObjectAttributes instance.

   Returns: A new instance on success,or null on failure.
  """
  pass
 def GetGroupList(self):
  """
  GetGroupList(self: ObjectAttributes) -> Array[int]

  

   Returns an array of GroupCount group indices.  If GroupCount is zero,then GetGroupList() 

    returns null.

  

   Returns: An array of group indices. null might be retuned in place of an empty array.
  """
  pass
 def GetUserString(self,key):
  """
  GetUserString(self: ObjectAttributes,key: str) -> str

  

   Gets a user string.

  

   key: id used to retrieve the string.

   Returns: string associated with the key if successful. null if no key was found.
  """
  pass
 def GetUserStrings(self):
  """
  GetUserStrings(self: ObjectAttributes) -> NameValueCollection

  

   Gets an independent copy of the collection of (user text key,user text value) pairs attached to 

    this object.

  

   Returns: A collection of key strings and values strings. This
  """
  pass
 def HasDisplayModeOverride(self,viewportId):
  """
  HasDisplayModeOverride(self: ObjectAttributes,viewportId: Guid) -> bool

  

   Determines if an object has a display mode override for a given viewport.

  

   viewportId: Id of a Rhino Viewport.

   Returns: true if the object has a display mode override for the viewport; otherwise,false.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: CommonObject)

   Is called when a non-const operation first occurs.
  """
  pass
 def RemoveDisplayModeOverride(self,rhinoViewportId=None):
  """
  RemoveDisplayModeOverride(self: ObjectAttributes,rhinoViewportId: Guid)

   By default,objects are drawn using the display mode of the viewport that

     the 

    object is being drawn in. Setting a specific display mode,instructs

     Rhino to 

    always use that display mode,regardless of the viewport's mode.

     This function 

    resets an object to use the viewport's display mode.

  

  

   rhinoViewportId: viewport that display mode overrides should be cleared from.

  RemoveDisplayModeOverride(self: ObjectAttributes)

   By default,objects are drawn using the display mode of the viewport that

     the 

    object is being drawn in. Setting a specific display mode,instructs

     Rhino to 

    always use that display mode,regardless of the viewport's mode.

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
 def RemoveFromGroup(self,groupIndex):
  """
  RemoveFromGroup(self: ObjectAttributes,groupIndex: int)

   removes object from the group with specified index.

     If the object is not in the 

    group,nothing is changed.

  

  

   groupIndex: The index that will be removed.
  """
  pass
 def SetDisplayModeOverride(self,mode,rhinoViewportId=None):
  """
  SetDisplayModeOverride(self: ObjectAttributes,mode: DisplayModeDescription,rhinoViewportId: Guid) -> bool

  

   By default,objects are drawn using the display mode of the viewport that

     the 

    object is being drawn in. Setting a specific display mode,instructs

     Rhino to 

    always use that display mode,regardless of the viewport's mode.

     This version sets 

    a display mode for a specific viewport.

  

  

   mode: The display mode.

   rhinoViewportId: The Rhino viewport ID.

   Returns: true on success.

  SetDisplayModeOverride(self: ObjectAttributes,mode: DisplayModeDescription) -> bool

  

   By default,objects are drawn using the display mode of the viewport that

     the 

    object is being drawn in. Setting a specific display mode,instructs

     Rhino to 

    always use that display mode,regardless of the viewport's mode.

     This version 

    affects the object's display mode for all viewports.

  

  

   mode: The display mode.

   Returns: true if setting was successful.
  """
  pass
 def SetUserString(self,key,value):
  """
  SetUserString(self: ObjectAttributes,key: str,value: str) -> bool

  

   Attach a user string (key,value combination) to this geometry.

  

   key: id used to retrieve this string.

   value: string associated with key. If null,the key will be removed

   Returns: true on success.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 ColorSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color used to display an object is specified in one of three ways.

   If ColorSource is ON::color_from_layer,then the object's layer ON_Layer::Color() is used.

   If ColorSource is ON::color_from_object,then value of m_color is used.

   If ColorSource is ON::color_from_material,then the diffuse color of the object's

   render material is used.  See ON_3dmObjectAttributes::MaterialSource() to

   determine where to get the definition of the object's render material.



Get: ColorSource(self: ObjectAttributes) -> ObjectColorSource



Set: ColorSource(self: ObjectAttributes)=value

"""

 Decals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all object decals associated with this object.



Get: Decals(self: ObjectAttributes) -> Decals



"""

 DisplayOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Display order used to force objects to be drawn on top or behind each other.

   Larger numbers draw on top of smaller numbers.

   0 =draw object in standard depth buffered order<0=draw object behind "normal" draw order objects>0=draw object on top of "normal" draw order objects



Get: DisplayOrder(self: ObjectAttributes) -> int



Set: DisplayOrder(self: ObjectAttributes)=value

"""

 GroupCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """number of groups object belongs to.



Get: GroupCount(self: ObjectAttributes) -> int



"""

 HasMapping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A mapping from any plugin source is associated with these attributes

   Need to do this here to respond correctly to ModifyObjectAttributes event



Get: HasMapping(self: ObjectAttributes) -> bool



"""

 IsDocumentControlled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDocumentControlled(self: ObjectAttributes) -> bool



"""

 IsInstanceDefinitionObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Use this query to determine if an object is part of an instance definition.



Get: IsInstanceDefinitionObject(self: ObjectAttributes) -> bool



"""

 LayerIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an associated layer index.

   Layer definitions in an OpenNURBS model are stored in a layer table.

   The layer table is conceptually an array of ON_Layer classes.  Every

   OpenNURBS object in a model is on some layer.  The object's layer

   is specified by zero based indicies into the ON_Layer array.



Get: LayerIndex(self: ObjectAttributes) -> int



Set: LayerIndex(self: ObjectAttributes)=value

"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the linetype index.

   Linetype definitions in an OpenNURBS model are stored in a linetype table.

   The linetype table is conceptually an array of ON_Linetype classes. Every

   OpenNURBS object in a model references some linetype.  The object's linetype

   is specified by zero based indicies into the ON_Linetype array.Index 0 is reserved for continuous linetype (no pattern).



Get: LinetypeIndex(self: ObjectAttributes) -> int



Set: LinetypeIndex(self: ObjectAttributes)=value

"""

 LinetypeSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Linetype used to display an object is specified in one of two ways.

   If LinetypeSource is ON::linetype_from_layer,then the object's layer ON_Layer::Linetype() is used.

   If LinetypeSource is ON::linetype_from_object,then value of m_linetype is used.



Get: LinetypeSource(self: ObjectAttributes) -> ObjectLinetypeSource



Set: LinetypeSource(self: ObjectAttributes)=value

"""

 MaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the material index.

   If you want something simple and fast,set the index of

   the rendering material.



Get: MaterialIndex(self: ObjectAttributes) -> int



Set: MaterialIndex(self: ObjectAttributes)=value

"""

 MaterialRefs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If you are developing a high quality plug-in renderer,and a user is

   assigning a custom render material to this object,then add rendering

   material information to the MaterialRefs dictionary.

   

   Note to developers:

    As soon as the MaterialRefs dictionary contains items rendering

    material queries slow down.  Do not populate the MaterialRefs

   dictionary when setting the MaterialIndex will take care of your needs.



Get: MaterialRefs(self: ObjectAttributes) -> MaterialRefs



"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the simple material should come from the object or from it's layer.

   High quality rendering plug-ins should use m_rendering_attributes.



Get: MaterialSource(self: ObjectAttributes) -> ObjectMaterialSource



Set: MaterialSource(self: ObjectAttributes)=value

"""

 Mode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An object must be in one of three modes: normal,locked or hidden.

   If an object is in normal mode,then the object's layer controls visibility

   and selectability. If an object is locked,then the object's layer controls

   visibility by the object cannot be selected. If the object is hidden,it is

   not visible and it cannot be selected.



Get: Mode(self: ObjectAttributes) -> ObjectMode



Set: Mode(self: ObjectAttributes)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object optional text name.

   More than one object in a model can have the same name and

   some objects may have no name.



Get: Name(self: ObjectAttributes) -> str



Set: Name(self: ObjectAttributes)=value

"""

 ObjectColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If ON::color_from_object == ColorSource,then color is the object's display color.



Get: ObjectColor(self: ObjectAttributes) -> Color



Set: ObjectColor(self: ObjectAttributes)=value

"""

 ObjectDecoration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Used to indicate an object has a decoration (like an arrowhead on a curve)



Get: ObjectDecoration(self: ObjectAttributes) -> ObjectDecoration



Set: ObjectDecoration(self: ObjectAttributes)=value

"""

 ObjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Every object has a Guid (globally unique identifier,also known as UUID,or universally

   unique identifier). The default value is Guid.Empty.

   

   When an object is added to a model,the value is checked.  If the value is Guid.Empty,a

   new Guid is created. If the value is not null but it is already used by another object

   in the model,a new Guid is created. If the value is not Guid.Empty and it is not used by

   another object in the model,then that value persists. When an object is updated,by

   a move for example,the value of ObjectId persists.

   This value is the same as the one returned by object.Id.



Get: ObjectId(self: ObjectAttributes) -> Guid



Set: ObjectId(self: ObjectAttributes)=value

"""

 PlotColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If plot_color_from_object == PlotColorSource,then PlotColor is the object's plotting color.



Get: PlotColor(self: ObjectAttributes) -> Color



Set: PlotColor(self: ObjectAttributes)=value

"""

 PlotColorSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color used to plot an object on paper is specified in one of three ways.

   If PlotColorSource is ON::plot_color_from_layer,then the object's layer ON_Layer::PlotColor() is used.

   If PlotColorSource is ON::plot_color_from_object,then value of PlotColor() is used.



Get: PlotColorSource(self: ObjectAttributes) -> ObjectPlotColorSource



Set: PlotColorSource(self: ObjectAttributes)=value

"""

 PlotWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Plot weight in millimeters.

   =0.0 means use the default width

   <0.0 means don't plot (visible for screen display,but does not show on plot)



Get: PlotWeight(self: ObjectAttributes) -> float



Set: PlotWeight(self: ObjectAttributes)=value

"""

 PlotWeightSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PlotWeightSource(self: ObjectAttributes) -> ObjectPlotWeightSource



Set: PlotWeightSource(self: ObjectAttributes)=value

"""

 Space=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Starting with V4,objects can be in either model space or page space.

   If an object is in page space,then ViewportId is not nil and

   identifies the page it is on.



Get: Space(self: ObjectAttributes) -> ActiveSpace



Set: Space(self: ObjectAttributes)=value

"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: ObjectAttributes) -> int



"""

 ViewportId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If ViewportId is nil,the object is active in all viewports. If ViewportId is not nil,then 

   this object is only active in a specific view. This field is primarily used to assign page

   space objects to a specific page,but it can also be used to restrict model space to a

   specific view.



Get: ViewportId(self: ObjectAttributes) -> Guid



Set: ViewportId(self: ObjectAttributes)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """object visibility.



Get: Visible(self: ObjectAttributes) -> bool



Set: Visible(self: ObjectAttributes)=value

"""

 WireDensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When a surface object is displayed in wireframe,this controls

   how many isoparametric wires are used.

   value number of isoparametric wires

   -1    boundary wires (off)

   0  boundary and knot wires 

   1  boundary and knot wires and,if there are no interior knots,a single interior wire.

   N>=2  boundary and knot wires and (N+1) interior wires.



Get: WireDensity(self: ObjectAttributes) -> int



Set: WireDensity(self: ObjectAttributes)=value

"""


