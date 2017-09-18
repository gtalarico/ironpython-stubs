class GeometryElement(GeometryObject,IDisposable,IEnumerable[GeometryObject],IEnumerable):
 """ Geometric representation of an element. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def GetBoundingBox(self):
  """
  GetBoundingBox(self: GeometryElement) -> BoundingBoxXYZ

  

   Retrieves a box that encloses the geometry element.

   Returns: The bounding box.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GeometryElement) -> IEnumerator[GeometryObject]

  

   Returns an enumerator that iterates through the collection.

   Returns: An IEnumerator(GeometryObject) object that can be used to iterate through the 

    collection.
  """
  pass
 def GetTransformed(self,transform):
  """
  GetTransformed(self: GeometryElement,transform: Transform) -> GeometryElement

  

   Returns a transformed copy of the geometry in this element.

  

   transform: The transformation to apply to the geometry.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def __contains__(self,*args):
  """ __contains__[GeometryObject](enumerable: IEnumerable[GeometryObject],value: GeometryObject) -> bool """
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
 MaterialElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element describing the material from which this element is composed.



Get: MaterialElement(self: GeometryElement) -> Material



"""


