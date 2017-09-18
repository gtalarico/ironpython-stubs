class UCOMIEnumConnections:
 """ Use System.Runtime.InteropServices.ComTypes.IEnumConnections instead. """
 def Clone(self,ppenum):
  """
  Clone(self: UCOMIEnumConnections) -> UCOMIEnumConnections

  

   Creates another enumerator that contains the same enumeration state as the current one.
  """
  pass
 def Next(self,celt,rgelt,pceltFetched):
  """
  Next(self: UCOMIEnumConnections,celt: int) -> (int,Array[CONNECTDATA],int)

  

   Retrieves a specified number of items in the enumeration sequence.

  

   celt: The number of System.Runtime.InteropServices.CONNECTDATA structures to return in rgelt.

   Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def Reset(self):
  """
  Reset(self: UCOMIEnumConnections)

   Resets the enumeration sequence to the beginning.
  """
  pass
 def Skip(self,celt):
  """
  Skip(self: UCOMIEnumConnections,celt: int) -> int

  

   Skips over a specified number of items in the enumeration sequence.

  

   celt: The number of elements to skip in the enumeration.

   Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
