class TextDot(GeometryBase,IDisposable,ISerializable):
 """
 Represents a text dot,or an annotation entity with text that always faces the camera and always has the same size.

    This class refers to the geometric element that is independent from the document.

 

 TextDot(text: str,location: Point3d)
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
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
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
 def __new__(self,text,location):
  """
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type,text: str,location: Point3d)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 FontFace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Font face used for displaying the dot



Get: FontFace(self: TextDot) -> str



Set: FontFace(self: TextDot)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height of font used for displaying the dot



Get: FontHeight(self: TextDot) -> int



Set: FontHeight(self: TextDot)=value

"""

 Point=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of the textdot.



Get: Point(self: TextDot) -> Point3d



Set: Point(self: TextDot)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the textdot.



Get: Text(self: TextDot) -> str



Set: Text(self: TextDot)=value

"""


