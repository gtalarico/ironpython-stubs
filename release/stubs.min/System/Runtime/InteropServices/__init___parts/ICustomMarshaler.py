class ICustomMarshaler:
 """ Provides custom wrappers for handling method calls. """
 def CleanUpManagedData(self,ManagedObj):
  """
  CleanUpManagedData(self: ICustomMarshaler,ManagedObj: object)

   Performs necessary cleanup of the managed data when it is no longer needed.

  

   ManagedObj: The managed object to be destroyed.
  """
  pass
 def CleanUpNativeData(self,pNativeData):
  """
  CleanUpNativeData(self: ICustomMarshaler,pNativeData: IntPtr)

   Performs necessary cleanup of the unmanaged data when it is no longer needed.

  

   pNativeData: A pointer to the unmanaged data to be destroyed.
  """
  pass
 def GetNativeDataSize(self):
  """
  GetNativeDataSize(self: ICustomMarshaler) -> int

  

   Returns the size of the native data to be marshaled.

   Returns: The size,in bytes,of the native data.
  """
  pass
 def MarshalManagedToNative(self,ManagedObj):
  """
  MarshalManagedToNative(self: ICustomMarshaler,ManagedObj: object) -> IntPtr

  

   Converts the managed data to unmanaged data.

  

   ManagedObj: The managed object to be converted.

   Returns: A pointer to the COM view of the managed object.
  """
  pass
 def MarshalNativeToManaged(self,pNativeData):
  """
  MarshalNativeToManaged(self: ICustomMarshaler,pNativeData: IntPtr) -> object

  

   Converts the unmanaged data to managed data.

  

   pNativeData: A pointer to the unmanaged data to be wrapped.

   Returns: An object that represents the managed view of the COM data.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
