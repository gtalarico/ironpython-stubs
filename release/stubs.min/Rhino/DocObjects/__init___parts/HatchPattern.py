class HatchPattern(CommonObject,IDisposable,ISerializable):
 """ HatchPattern() """
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
 @staticmethod
 def ReadFromFile(filename,quiet):
  """
  ReadFromFile(filename: str,quiet: bool) -> Array[HatchPattern]

  

   Reads hatch pattern definitions from a file.

  

   filename: Name of an existing file. If filename is null or empty,default hatch pattern filename is used.

   quiet: If file doesn't exist,and quiet is false,an error meesage box is shown.

   Returns: An array of hatch patterns. This can be null,but not empty.
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: HatchPattern) -> str



Set: Description(self: HatchPattern)=value

"""

 FillType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FillType(self: HatchPattern) -> HatchPatternFillType



Set: FillType(self: HatchPattern)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index in the hatch pattern table for this pattern. -1 if not in the table.



Get: Index(self: HatchPattern) -> int



"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Deleted hatch patterns are kept in the runtime hatch pattern table so that undo

   will work with hatch patterns.  Call IsDeleted to determine to determine if

   a hatch pattern is deleted.



Get: IsDeleted(self: HatchPattern) -> bool



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Rhino allows multiple files to be viewed simultaneously. Hatch patterns in the

   document are "normal" or "reference". Reference hatch patterns are not saved.



Get: IsReference(self: HatchPattern) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: HatchPattern) -> str



Set: Name(self: HatchPattern)=value

"""


