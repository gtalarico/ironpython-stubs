class UCOMIStream:
 """ Use System.Runtime.InteropServices.ComTypes.IStream instead. """
 def Clone(self,ppstm):
  """
  Clone(self: UCOMIStream) -> UCOMIStream

  

   Creates a new stream object with its own seek pointer that references the same bytes as the 

    original stream.
  """
  pass
 def Commit(self,grfCommitFlags):
  """
  Commit(self: UCOMIStream,grfCommitFlags: int)

   Ensures that any changes made to a stream object open in transacted mode are reflected in the 

    parent storage.

  

  

   grfCommitFlags: Controls how the changes for the stream object are committed.
  """
  pass
 def CopyTo(self,pstm,cb,pcbRead,pcbWritten):
  """
  CopyTo(self: UCOMIStream,pstm: UCOMIStream,cb: Int64,pcbRead: IntPtr,pcbWritten: IntPtr)

   Copies a specified number of bytes from the current seek pointer in the stream to the current 

    seek pointer in another stream.

  

  

   pstm: Reference to the destination stream.

   cb: The number of bytes to copy from the source stream.

   pcbRead: On successful return,contains the actual number of bytes read from the source.

   pcbWritten: On successful return,contains the actual number of bytes written to the destination.
  """
  pass
 def LockRegion(self,libOffset,cb,dwLockType):
  """
  LockRegion(self: UCOMIStream,libOffset: Int64,cb: Int64,dwLockType: int)

   Restricts access to a specified range of bytes in the stream.

  

   libOffset: The byte offset for the beginning of the range.

   cb: The length of the range,in bytes,to restrict.

   dwLockType: The requested restrictions on accessing the range.
  """
  pass
 def Read(self,pv,cb,pcbRead):
  """
  Read(self: UCOMIStream,cb: int,pcbRead: IntPtr) -> Array[Byte]

  

   Reads a specified number of bytes from the stream object into memory starting at the current 

    seek pointer.

  

  

   cb: The number of bytes to read from the stream object.

   pcbRead: Pointer to a ULONG variable that receives the actual number of bytes read from the stream object.
  """
  pass
 def Revert(self):
  """
  Revert(self: UCOMIStream)

   Discards all changes that have been made to a transacted stream since the last 

    System.Runtime.InteropServices.UCOMIStream.Commit(System.Int32) call.
  """
  pass
 def Seek(self,dlibMove,dwOrigin,plibNewPosition):
  """
  Seek(self: UCOMIStream,dlibMove: Int64,dwOrigin: int,plibNewPosition: IntPtr)

   Changes the seek pointer to a new location relative to the beginning of the stream,to the end 

    of the stream,or to the current seek pointer.

  

  

   dlibMove: Displacement to add to dwOrigin.

   dwOrigin: Specifies the origin of the seek. The origin can be the beginning of the file,the current seek 

    pointer,or the end of the file.

  

   plibNewPosition: On successful return,contains the offset of the seek pointer from the beginning of the stream.
  """
  pass
 def SetSize(self,libNewSize):
  """
  SetSize(self: UCOMIStream,libNewSize: Int64)

   Changes the size of the stream object.

  

   libNewSize: Specifies the new size of the stream as a number of bytes.
  """
  pass
 def Stat(self,pstatstg,grfStatFlag):
  """
  Stat(self: UCOMIStream,grfStatFlag: int) -> STATSTG

  

   Retrieves the System.Runtime.InteropServices.STATSTG structure for this stream.

  

   grfStatFlag: Specifies some of the members in the STATSTG structure that this method does not return,thus 

    saving some memory allocation operations.
  """
  pass
 def UnlockRegion(self,libOffset,cb,dwLockType):
  """
  UnlockRegion(self: UCOMIStream,libOffset: Int64,cb: Int64,dwLockType: int)

   Removes the access restriction on a range of bytes previously restricted with 

    System.Runtime.InteropServices.UCOMIStream.LockRegion(System.Int64,System.Int64,System.Int32).

  

  

   libOffset: The byte offset for the beginning of the range.

   cb: The length,in bytes,of the range to restrict.

   dwLockType: The access restrictions previously placed on the range.
  """
  pass
 def Write(self,pv,cb,pcbWritten):
  """
  Write(self: UCOMIStream,pv: Array[Byte],cb: int,pcbWritten: IntPtr)

   Writes a specified number of bytes into the stream object starting at the current seek pointer.

  

   pv: Buffer to write this stream to.

   cb: The number of bytes to write into the stream.

   pcbWritten: On successful return,contains the actual number of bytes written to the stream object. The 

    caller can set this pointer to null,in which case this method does not provide the actual 

    number of bytes written.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
