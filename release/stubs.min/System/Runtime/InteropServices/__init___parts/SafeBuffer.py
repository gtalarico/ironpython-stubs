class SafeBuffer(SafeHandleZeroOrMinusOneIsInvalid,IDisposable):
 """ Provides a controlled memory buffer that can be used for reading and writing. Attempts to access memory outside the controlled buffer (underruns and overruns) raise exceptions. """
 def AcquirePointer(self,pointer):
  """
  AcquirePointer(self: SafeBuffer,pointer: Byte*) -> Byte*

  

   Obtains a pointer from a System.Runtime.InteropServices.SafeBuffer object for a block of memory.

  

   pointer: A byte pointer,passed by reference,to receive the pointer from within the 

    System.Runtime.InteropServices.SafeBuffer object. You must set this pointer to null before you 

    call this method.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: SafeHandle,disposing: bool)

   Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 

    specifying whether to perform a normal dispose operation.

  

  

   disposing: true for a normal dispose operation; false to finalize the handle.
  """
  pass
 def Initialize(self,*__args):
  """
  Initialize[T](self: SafeBuffer,numElements: UInt32)Initialize(self: SafeBuffer,numElements: UInt32,sizeOfEachElement: UInt32)

   Specifies the allocation size of the memory buffer by using the specified number of elements and 

    element size. You must call this method before you use the 

    System.Runtime.InteropServices.SafeBuffer instance.

  

  

   numElements: The number of elements in the buffer.

   sizeOfEachElement: The size of each element in the buffer.

  Initialize(self: SafeBuffer,numBytes: UInt64)

   Defines the allocation size of the memory region in bytes. You must call this method before you 

    use the System.Runtime.InteropServices.SafeBuffer instance.

  

  

   numBytes: The number of bytes in the buffer.
  """
  pass
 def Read(self,byteOffset):
  """ Read[T](self: SafeBuffer,byteOffset: UInt64) -> T """
  pass
 def ReadArray(self,byteOffset,array,index,count):
  """ ReadArray[T](self: SafeBuffer,byteOffset: UInt64,array: Array[T],index: int,count: int) """
  pass
 def ReleaseHandle(self,*args):
  """
  ReleaseHandle(self: SafeHandle) -> bool

  

   When overridden in a derived class,executes the code required to free the handle.

   Returns: true if the handle is released successfully; otherwise,in the event of a catastrophic failure,

    false. In this case,it generates a releaseHandleFailed MDA Managed Debugging Assistant.
  """
  pass
 def ReleasePointer(self):
  """
  ReleasePointer(self: SafeBuffer)

   Releases a pointer that was obtained by the 

    System.Runtime.InteropServices.SafeBuffer.AcquirePointer(System.Byte*@) method.
  """
  pass
 def SetHandle(self,*args):
  """
  SetHandle(self: SafeHandle,handle: IntPtr)

   Sets the handle to the specified pre-existing handle.

  

   handle: The pre-existing handle to use.
  """
  pass
 def Write(self,byteOffset,value):
  """ Write[T](self: SafeBuffer,byteOffset: UInt64,value: T) """
  pass
 def WriteArray(self,byteOffset,array,index,count):
  """ WriteArray[T](self: SafeBuffer,byteOffset: UInt64,array: Array[T],index: int,count: int) """
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
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,ownsHandle: bool) """
  pass
 ByteLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of the buffer,in bytes.



Get: ByteLength(self: SafeBuffer) -> UInt64



"""


 handle=None

