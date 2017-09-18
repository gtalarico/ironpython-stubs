class DimensionStyle(CommonObject,IDisposable,ISerializable):
 """ DimensionStyle() """
 def CommitChanges(self):
  """ CommitChanges(self: DimensionStyle) -> bool """
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
 AlternateLengthFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AlternateLengthFactor(self: DimensionStyle) -> float



Set: AlternateLengthFactor(self: DimensionStyle)=value

"""

 AngleResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleResolution(self: DimensionStyle) -> int



Set: AngleResolution(self: DimensionStyle)=value

"""

 ArrowLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArrowLength(self: DimensionStyle) -> float



Set: ArrowLength(self: DimensionStyle)=value

"""

 ArrowType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArrowType(self: DimensionStyle) -> DimensionStyleArrowType



Set: ArrowType(self: DimensionStyle)=value

"""

 CenterMarkSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CenterMarkSize(self: DimensionStyle) -> float



Set: CenterMarkSize(self: DimensionStyle)=value

"""

 ExtensionLineExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLineExtension(self: DimensionStyle) -> float



Set: ExtensionLineExtension(self: DimensionStyle)=value

"""

 ExtensionLineOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLineOffset(self: DimensionStyle) -> float



Set: ExtensionLineOffset(self: DimensionStyle)=value

"""

 FontIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FontIndex(self: DimensionStyle) -> int



Set: FontIndex(self: DimensionStyle)=value

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: DimensionStyle) -> Guid



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Index(self: DimensionStyle) -> int



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsReference(self: DimensionStyle) -> bool



"""

 LeaderArrowLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LeaderArrowLength(self: DimensionStyle) -> float



Set: LeaderArrowLength(self: DimensionStyle)=value

"""

 LeaderArrowType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LeaderArrowType(self: DimensionStyle) -> DimensionStyleArrowType



Set: LeaderArrowType(self: DimensionStyle)=value

"""

 LengthFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LengthFactor(self: DimensionStyle) -> float



Set: LengthFactor(self: DimensionStyle)=value

"""

 LengthFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LengthFormat(self: DimensionStyle) -> DistanceDisplayMode



Set: LengthFormat(self: DimensionStyle)=value

"""

 LengthResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Linear display precision.



Get: LengthResolution(self: DimensionStyle) -> int



Set: LengthResolution(self: DimensionStyle)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: DimensionStyle) -> str



Set: Name(self: DimensionStyle)=value

"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Prefix(self: DimensionStyle) -> str



Set: Prefix(self: DimensionStyle)=value

"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Suffix(self: DimensionStyle) -> str



Set: Suffix(self: DimensionStyle)=value

"""

 TextAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextAlignment(self: DimensionStyle) -> TextDisplayAlignment



Set: TextAlignment(self: DimensionStyle)=value

"""

 TextGap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextGap(self: DimensionStyle) -> float



Set: TextGap(self: DimensionStyle)=value

"""

 TextHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextHeight(self: DimensionStyle) -> float



Set: TextHeight(self: DimensionStyle)=value

"""


