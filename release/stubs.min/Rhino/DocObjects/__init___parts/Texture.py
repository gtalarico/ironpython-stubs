class Texture(CommonObject,IDisposable,ISerializable):
 """
 Represents a texture that is mapped on objects.

 

 Texture()
 """
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
 def GetAlphaBlendValues(self,constant,a0,a1,a2,a3):
  """
  GetAlphaBlendValues(self: Texture) -> (float,float,float,float,float)

  

   If the TextureCombineMode is Blend,then the blending function

     for alpha is 

    determined by

     

     new alpha=constant

        + 

    a0*(current alpha)

        + a1*(texture alpha)

        + 

    a2*min(current alpha,texture alpha)

        + a3*max(current alpha,texture 

    alpha)
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
 def SetAlphaBlendValues(self,constant,a0,a1,a2,a3):
  """
  SetAlphaBlendValues(self: Texture,constant: float,a0: float,a1: float,a2: float,a3: float)

   If the TextureCombineMode is Blend,then the blending function

     for alpha is 

    determined by

     

     new alpha=constant

        + 

    a0*(current alpha)

        + a1*(texture alpha)

        + 

    a2*min(current alpha,texture alpha)

        + a3*max(current alpha,texture 

    alpha)
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
 ApplyUvwTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true then the UVW transform is applied to the texture

   otherwise the UVW transform is ignored.



Get: ApplyUvwTransform(self: Texture) -> bool



Set: ApplyUvwTransform(self: Texture)=value

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If the texture is enabled then it will be visible in the rendered

   display otherwise it will not.



Get: Enabled(self: Texture) -> bool



Set: Enabled(self: Texture)=value

"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a file name that is used by this texture.

   NOTE: this filename may well not be a path that makes sense

   on a user's computer because it was a path initially set on

   a different user's computer. If you want to get a workable path

   for this user,use the BitmapTable.Find function using this

   property.



Get: FileName(self: Texture) -> str



Set: FileName(self: Texture)=value

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the globally unique identifier of this texture.



Get: Id(self: Texture) -> Guid



"""

 MappingChannelId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """



Get: MappingChannelId(self: Texture) -> int



"""

 TextureCombineMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines how this texture is combined with others in a material's

   texture list.



Get: TextureCombineMode(self: Texture) -> TextureCombineMode



Set: TextureCombineMode(self: Texture)=value

"""

 TextureType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Controls how the pixels in the bitmap are interpreted



Get: TextureType(self: Texture) -> TextureType



Set: TextureType(self: Texture)=value

"""

 UvwTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transform to be applied to each instance of this texture

   if ApplyUvw is true



Get: UvwTransform(self: Texture) -> Transform



Set: UvwTransform(self: Texture)=value

"""

 WrapU=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Texture wrapping mode in the U direction



Get: WrapU(self: Texture) -> TextureUvwWrapping



Set: WrapU(self: Texture)=value

"""

 WrapV=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Texture wrapping mode in the V direction



Get: WrapV(self: Texture) -> TextureUvwWrapping



Set: WrapV(self: Texture)=value

"""

 WrapW=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Texture wrapping mode in the W direction



Get: WrapW(self: Texture) -> TextureUvwWrapping



Set: WrapW(self: Texture)=value

"""


