class Linetype(CommonObject,IDisposable,ISerializable):
 """ Linetype() """
 def AppendSegment(self,length,isSolid):
  """
  AppendSegment(self: Linetype,length: float,isSolid: bool) -> int

  

   Adds a segment to the pattern.

  

   length: The length of the segment to be added.

   isSolid: If true,the length is interpreted as a line. If false,

     then the length is 

    interpreted as a space.

  

   Returns: Index of the added segment.
  """
  pass
 def CommitChanges(self):
  """ CommitChanges(self: Linetype) -> bool """
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
  Default(self: Linetype)

   Set linetype to default settings.
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
 def GetSegment(self,index,length,isSolid):
  """
  GetSegment(self: Linetype,index: int) -> (float,bool)

  

   Gets the segment information at a index.

  

   index: Zero based index of the segment.
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
 def RemoveSegment(self,index):
  """
  RemoveSegment(self: Linetype,index: int) -> bool

  

   Removes a segment in the linetype.

  

   index: Zero based index of the segment to remove.

   Returns: true if the segment index was removed.
  """
  pass
 def SetSegment(self,index,length,isSolid):
  """
  SetSegment(self: Linetype,index: int,length: float,isSolid: bool) -> bool

  

   Sets the length and type of the segment at index.

  

   index: Zero based index of the segment.

   length: The length of the segment to be added in millimeters.

   isSolid: If true,the length is interpreted as a line. If false,

     then the length is 

    interpreted as a space.

  

   Returns: true if the operation was successful; otherwise false.
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
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ID of this linetype object.



Get: Id(self: Linetype) -> Guid



Set: Id(self: Linetype)=value

"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this linetype has been deleted and is 

   currently in the Undo buffer.



Get: IsDeleted(self: Linetype) -> bool



"""

 IsModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if this linetype has been modified by LinetypeTable.ModifyLinetype()

   and the modifications can be undone.



Get: IsModified(self: Linetype) -> bool



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicting whether this linetype is a referenced linetype. 

   Referenced linetypes are part of referenced documents.



Get: IsReference(self: Linetype) -> bool



"""

 LinetypeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of this linetype.



Get: LinetypeIndex(self: Linetype) -> int



Set: LinetypeIndex(self: Linetype)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of this linetype.



Get: Name(self: Linetype) -> str



Set: Name(self: Linetype)=value

"""

 PatternLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Total length of one repeat of the pattern.



Get: PatternLength(self: Linetype) -> float



"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of segments in the pattern.



Get: SegmentCount(self: Linetype) -> int



"""


