class ConduitSizes(object,IEnumerable[ConduitSize],IEnumerable,IDisposable):
 """ Class ConduitSizeSet being used to store the conduit sizes. """
 def Contains(self,nominalDiameter):
  """
  Contains(self: ConduitSizes,nominalDiameter: float) -> bool
  
   Checks whether a conduit size with the nominal diameter exists.
  
   nominalDiameter: Nominal diameter.
   Returns: True if a conduit size with the nominal diameter exists.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ConduitSizes) """
  pass
 def GetConduitSizesIterator(self):
  """
  GetConduitSizesIterator(self: ConduitSizes) -> ConduitSizeIterator
  
   Returns a ConduitSizeIterator to the conduit sizes.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ConduitSizes) -> IEnumerator[ConduitSize]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ConduitSizes,disposing: bool) """
  pass
 def __contains__(self,*args):
  """ __contains__[ConduitSize](enumerable: IEnumerable[ConduitSize],value: ConduitSize) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Count of the items contained in the collection.

Get: Count(self: ConduitSizes) -> int

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSizes) -> bool

"""


