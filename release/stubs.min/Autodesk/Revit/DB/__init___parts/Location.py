class Location(APIObject,IDisposable):
 """ Provides location functionality for all elements. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def Move(self,translation):
  """
  Move(self: Location,translation: XYZ) -> bool

  

   Move the element within the project by a specified vector.

  

   translation: The vector by which the element is to be moved.

   Returns: If the element is moved successfully then the method return True,otherwise 

    False.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def Rotate(self,axis,angle):
  """
  Rotate(self: Location,axis: Line,angle: float) -> bool

  

   Rotate the element within the project by a specified angle around a given axis.

  

   axis: An unbounded line that represents the axis of rotation.

   angle: The angle,in radians,by which the element is to be rotated around the 

    specified axis.

  

   Returns: If the element is rotate successfully then the method returns True,otherwise 

    False.
  """
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
