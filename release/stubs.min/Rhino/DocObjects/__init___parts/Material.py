class Material(CommonObject,IDisposable,ISerializable):
 """ Material() """
 def CommitChanges(self):
  """ CommitChanges(self: Material) -> bool """
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
  Default(self: Material)

   Set material to default settings.
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
 def GetUserString(self,key):
  """
  GetUserString(self: Material,key: str) -> str

  

   Gets a user string.

  

   key: id used to retrieve the string.

   Returns: string associated with the key if successful. null if no key was found.
  """
  pass
 def GetUserStrings(self):
  """
  GetUserStrings(self: Material) -> NameValueCollection

  

   Gets an independent copy of the collection of (user text key,user text value) pairs attached to 

    this object.

  

   Returns: A collection of key strings and values strings. This
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
  """ OnSwitchToNonConst(self: Material) """
  pass
 def SetBitmapTexture(self,*__args):
  """
  SetBitmapTexture(self: Material,texture: Texture) -> bool

  SetBitmapTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetBumpTexture(self,*__args):
  """
  SetBumpTexture(self: Material,texture: Texture) -> bool

  SetBumpTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetEnvironmentTexture(self,*__args):
  """
  SetEnvironmentTexture(self: Material,texture: Texture) -> bool

  SetEnvironmentTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetTransparencyTexture(self,*__args):
  """
  SetTransparencyTexture(self: Material,texture: Texture) -> bool

  SetTransparencyTexture(self: Material,filename: str) -> bool
  """
  pass
 def SetUserString(self,key,value):
  """
  SetUserString(self: Material,key: str,value: str) -> bool

  

   Attach a user string (key,value combination) to this geometry.

  

   key: id used to retrieve this string.

   value: string associated with key.

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
 AmbientColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AmbientColor(self: Material) -> Color



Set: AmbientColor(self: Material)=value

"""

 DiffuseColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DiffuseColor(self: Material) -> Color



Set: DiffuseColor(self: Material)=value

"""

 EmissionColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EmissionColor(self: Material) -> Color



Set: EmissionColor(self: Material)=value

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ID of this material.



Get: Id(self: Material) -> Guid



"""

 IndexOfRefraction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of refraction of the material,generally

   >= 1.0 (speed of light in vacuum)/(speed of light in material)



Get: IndexOfRefraction(self: Material) -> float



Set: IndexOfRefraction(self: Material)=value

"""

 IsDefaultMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """By default Rhino layers and objects are assigned the default rendering material.



Get: IsDefaultMaterial(self: Material) -> bool



"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Deleted materials are kept in the runtime material table so that undo

   will work with materials.  Call IsDeleted to determine to determine if

   a material is deleted.



Get: IsDeleted(self: Material) -> bool



"""

 IsDocumentControlled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true this object may not be modified. Any properties or functions that attempt

   to modify this object when it is set to "IsReadOnly" will throw a NotSupportedException.



Get: IsDocumentControlled(self: Material) -> bool



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Rhino allows multiple files to be viewed simultaneously. Materials in the

   document are "normal" or "reference". Reference materials are not saved.



Get: IsReference(self: Material) -> bool



"""

 MaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """



Get: MaterialIndex(self: Material) -> int



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Material) -> str



Set: Name(self: Material)=value

"""

 ReflectionColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReflectionColor(self: Material) -> Color



Set: ReflectionColor(self: Material)=value

"""

 Reflectivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how reflective a material is,0f is no reflection

   1f is 100% reflective.



Get: Reflectivity(self: Material) -> float



Set: Reflectivity(self: Material)=value

"""

 RenderPlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the RenderPlugIn that is associated with this material.



Get: RenderPlugInId(self: Material) -> Guid



Set: RenderPlugInId(self: Material)=value

"""

 Shine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shine factor of the material.



Get: Shine(self: Material) -> float



Set: Shine(self: Material)=value

"""

 SpecularColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SpecularColor(self: Material) -> Color



Set: SpecularColor(self: Material)=value

"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the transparency of the material (0.0=opaque to 1.0=transparent)



Get: Transparency(self: Material) -> float



Set: Transparency(self: Material)=value

"""

 TransparentColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TransparentColor(self: Material) -> Color



Set: TransparentColor(self: Material)=value

"""

 UseCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of objects and layers that use this material.



Get: UseCount(self: Material) -> int



"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserStringCount(self: Material) -> int



"""


 MaxShine=255.0

