class Layer(CommonObject,IDisposable,ISerializable):
 """ Layer() """
 def CommitChanges(self):
  """ CommitChanges(self: Layer) -> bool """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

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

     color=

    Rhino.ApplicationSettings.AppearanceSettings.DefaultLayerColorline style=

    Rhino.ApplicationSettings.AppearanceSettings.DefaultLayerLineStylematerial index=-1iges level 

   =-1mode=NormalLayername=emptylayer index=0 (ignored by AddLayer)

  

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

    In this case,when a parent layer is locked,

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

    not nil). In this case,when a parent layer is

     turned off,then child layers are 

    also turned off. The persistent

     visibility setting determines what happens when the 

    parent is turned on

     again.
  """
  pass
 def GetUserString(self,key):
  """
  GetUserString(self: Layer,key: str) -> str

  

   Gets user string from this geometry.

  

   key: id used to retrieve the string.

   Returns: string associated with the key if successful. null if no key was found.
  """
  pass
 def GetUserStrings(self):
  """
  GetUserStrings(self: Layer) -> NameValueCollection

  

   Gets a copy of all (user key string,user value string) pairs attached to this geometry.

   Returns: A new collection.
  """
  pass
 def IsChildOf(self,*__args):
  """
  IsChildOf(self: Layer,otherLayer: Layer) -> bool

  IsChildOf(self: Layer,layerIndex: int) -> bool
  """
  pass
 def IsParentOf(self,*__args):
  """
  IsParentOf(self: Layer,otherLayer: Layer) -> bool

  IsParentOf(self: Layer,layerIndex: int) -> bool
  """
  pass
 @staticmethod
 def IsValidName(name):
  """
  IsValidName(name: str) -> bool

  

   Determines if a given string is valid for a layer name.

  

   name: A name to be validated.

   Returns: true if the name is valid for a layer name; otherwise,false.
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
 def SetPersistentLocking(self,persistentLocking):
  """
  SetPersistentLocking(self: Layer,persistentLocking: bool)

   Set the persistent locking setting for this layer
  """
  pass
 def SetPersistentVisibility(self,persistentVisibility):
  """
  SetPersistentVisibility(self: Layer,persistentVisibility: bool)

   Set the persistent visibility setting for this layer
  """
  pass
 def SetUserString(self,key,value):
  """
  SetUserString(self: Layer,key: str,value: str) -> bool

  

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
 def __str__(self,*args):
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display color for this layer.



Get: Color(self: Layer) -> Color



Set: Color(self: Layer)=value

"""

 FullPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full path to this layer. The full path includes nesting information.



Get: FullPath(self: Layer) -> str



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ID of this layer object. 

   You typically do not need to assign a custom ID.



Get: Id(self: Layer) -> Guid



Set: Id(self: Layer)=value

"""

 IgesLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IGES level for this layer.



Get: IgesLevel(self: Layer) -> int



Set: IgesLevel(self: Layer)=value

"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this layer has been deleted and is 

   currently in the Undo buffer.



Get: IsDeleted(self: Layer) -> bool



"""

 IsExpanded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this layer is expanded in the Rhino Layer dialog.



Get: IsExpanded(self: Layer) -> bool



Set: IsExpanded(self: Layer)=value

"""

 IsLocked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the locked state of this layer.



Get: IsLocked(self: Layer) -> bool



Set: IsLocked(self: Layer)=value

"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicting whether this layer is a referenced layer. 

   Referenced layers are part of referenced documents.



Get: IsReference(self: Layer) -> bool



"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the visibility of this layer.



Get: IsVisible(self: Layer) -> bool



Set: IsVisible(self: Layer)=value

"""

 LayerIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of this layer.



Get: LayerIndex(self: Layer) -> int



Set: LayerIndex(self: Layer)=value

"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the line-type index for this layer.



Get: LinetypeIndex(self: Layer) -> int



Set: LinetypeIndex(self: Layer)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of this layer.



Get: Name(self: Layer) -> str



Set: Name(self: Layer)=value

"""

 ParentLayerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ID of the parent layer. Layers can be origanized in a hierarchical structure,

   in which case this returns the parent layer ID. If the layer has no parent,

   Guid.Empty will be returned.



Get: ParentLayerId(self: Layer) -> Guid



Set: ParentLayerId(self: Layer)=value

"""

 PlotColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the plot color for this layer.



Get: PlotColor(self: Layer) -> Color



Set: PlotColor(self: Layer)=value

"""

 PlotWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the thickness of the plotting pen in millimeters. 

   A thickness of 0.0 indicates the "default" pen weight should be used.



Get: PlotWeight(self: Layer) -> float



Set: PlotWeight(self: Layer)=value

"""

 RenderMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Rhino.Render.RenderMaterial for objects on

   this layer that have MaterialSource() == MaterialFromLayer.

   A null result indicates that no Rhino.Render.RenderMaterial has

   been assigned  and the material created by the default Material

   constructor or the Rhino.DocObjects.Layer.RenderMaterialIndex should be used.



Get: RenderMaterial(self: Layer) -> RenderMaterial



Set: RenderMaterial(self: Layer)=value

"""

 RenderMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of render material for objects on this layer that have

   MaterialSource() == MaterialFromLayer. 

   A material index of -1 indicates no material has been assigned 

   and the material created by the default Material constructor 

   should be used.



Get: RenderMaterialIndex(self: Layer) -> int



Set: RenderMaterialIndex(self: Layer)=value

"""

 SortIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Runtime index used to sort layers in layer dialog.



Get: SortIndex(self: Layer) -> int



"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of user strings.



Get: UserStringCount(self: Layer) -> int



"""


