class ICollectData:
 """ Prepares performance data for the performance DLL the system loads when working with performance counters. """
 def CloseData(self):
  """
  CloseData(self: ICollectData)

   Called by the performance DLL's close performance data function.
  """
  pass
 def CollectData(self,id,valueName,data,totalBytes,res):
  """
  CollectData(self: ICollectData,id: int,valueName: IntPtr,data: IntPtr,totalBytes: int) -> IntPtr

  

   Collects the performance data for the performance DLL.

  

   id: The call index.

   valueName: A pointer to a Unicode string list with the requested object identifiers.

   data: A pointer to the data buffer.

   totalBytes: A pointer to a number of bytes.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
