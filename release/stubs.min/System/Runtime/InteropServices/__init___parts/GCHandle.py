class GCHandle(object):
 """ Provides a way to access a managed object from unmanaged memory. """
 def AddrOfPinnedObject(self):
  """
  AddrOfPinnedObject(self: GCHandle) -> IntPtr

  

   Retrieves the address of an object in a System.Runtime.InteropServices.GCHandleType.Pinned 

    handle.

  

   Returns: The address of the of the Pinned object as an System.IntPtr.
  """
  pass
 @staticmethod
 def Alloc(value,type=None):
  """
  Alloc(value: object,type: GCHandleType) -> GCHandle

  

   Allocates a handle of the specified type for the specified object.

  

   value: The object that uses the System.Runtime.InteropServices.GCHandle.

   type: One of the System.Runtime.InteropServices.GCHandleType values,indicating the type of 

    System.Runtime.InteropServices.GCHandle to create.

  

   Returns: A new System.Runtime.InteropServices.GCHandle of the specified type. This 

    System.Runtime.InteropServices.GCHandle must be released with 

    System.Runtime.InteropServices.GCHandle.Free when it is no longer needed.

  

  Alloc(value: object) -> GCHandle

  

   Allocates a System.Runtime.InteropServices.GCHandleType.Normal handle for the specified object.

  

   value: The object that uses the System.Runtime.InteropServices.GCHandle.

   Returns: A new System.Runtime.InteropServices.GCHandle that protects the object from garbage collection. 

    This System.Runtime.InteropServices.GCHandle must be released with 

    System.Runtime.InteropServices.GCHandle.Free when it is no longer needed.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: GCHandle,o: object) -> bool

  

   Determines whether the specified System.Runtime.InteropServices.GCHandle object is equal to the 

    current System.Runtime.InteropServices.GCHandle object.

  

  

   o: The System.Runtime.InteropServices.GCHandle object to compare with the current 

    System.Runtime.InteropServices.GCHandle object.

  

   Returns: true if the specified System.Runtime.InteropServices.GCHandle object is equal to the current 

    System.Runtime.InteropServices.GCHandle object; otherwise,false.
  """
  pass
 def Free(self):
  """
  Free(self: GCHandle)

   Releases a System.Runtime.InteropServices.GCHandle.
  """
  pass
 @staticmethod
 def FromIntPtr(value):
  """
  FromIntPtr(value: IntPtr) -> GCHandle

  

   Returns a new System.Runtime.InteropServices.GCHandle object created from a handle to a managed 

    object.

  

  

   value: An System.IntPtr handle to a managed object to create a System.Runtime.InteropServices.GCHandle 

    object from.

  

   Returns: A new System.Runtime.InteropServices.GCHandle object that corresponds to the value parameter.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GCHandle) -> int

  

   Returns an identifier for the current System.Runtime.InteropServices.GCHandle object.

   Returns: An identifier for the current System.Runtime.InteropServices.GCHandle object.
  """
  pass
 @staticmethod
 def ToIntPtr(value):
  """
  ToIntPtr(value: GCHandle) -> IntPtr

  

   Returns the internal integer representation of a System.Runtime.InteropServices.GCHandle object.

  

   value: A System.Runtime.InteropServices.GCHandle object to retrieve an internal integer representation 

    from.

  

   Returns: An System.IntPtr object that represents a System.Runtime.InteropServices.GCHandle object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 IsAllocated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the handle is allocated.



Get: IsAllocated(self: GCHandle) -> bool



"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object this handle represents.



Get: Target(self: GCHandle) -> object



Set: Target(self: GCHandle)=value

"""


