class RepeatingReferenceSource(object,IDisposable):
 """ Represents a collection of repeating references. """
 def Dispose(self):
  """ Dispose(self: RepeatingReferenceSource) """
  pass
 def GetBounds(self):
  """
  GetBounds(self: RepeatingReferenceSource) -> RepeaterBounds

  

   Returns information about the boundaries of the repeating reference array.

   Returns: The bounds of the repeating reference source.
  """
  pass
 @staticmethod
 def GetDefaultRepeatingReferenceSource(document,elementId):
  """
  GetDefaultRepeatingReferenceSource(document: Document,elementId: ElementId) -> RepeatingReferenceSource

  

   Returns the default repeating reference source for a given element.

  

   document: The document that contains the element.

   elementId: The id of the element.

   Returns: The default repeating reference source of the given element.
  """
  pass
 def GetReference(self,coordinates):
  """
  GetReference(self: RepeatingReferenceSource,coordinates: RepeaterCoordinates) -> Reference

  

   Returns an individual repeating reference given by coordinates in the array,or 

    ll if there is no reference at the coordinates (for example if there is a hole 

    in a divided surface.)

  

  

   coordinates: The coordinates in the array of repeating references.

   Returns: The repeating reference.
  """
  pass
 @staticmethod
 def HasRepeatingReferenceSource(document,elementId):
  """
  HasRepeatingReferenceSource(document: Document,elementId: ElementId) -> bool

  

   Determines whether an element has any repeating reference sources that can be 

    used when creating component repeaters.

  

  

   document: The document that contains the element.

   elementId: The id of the element.

   Returns: True if the element has any repeating reference sources.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RepeatingReferenceSource,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DimensionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension count of the repeating reference array.



Get: DimensionCount(self: RepeatingReferenceSource) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RepeatingReferenceSource) -> bool



"""


