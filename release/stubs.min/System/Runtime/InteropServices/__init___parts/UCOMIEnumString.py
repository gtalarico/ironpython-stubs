class UCOMIEnumString:
 """ Use System.Runtime.InteropServices.ComTypes.IEnumString instead. """
 def Clone(self,ppenum):
  """
  Clone(self: UCOMIEnumString) -> UCOMIEnumString

  

   Creates another enumerator that contains the same enumeration state as the current one.
  """
  pass
 def Next(self,celt,rgelt,pceltFetched):
  """
  Next(self: UCOMIEnumString,celt: int) -> (int,Array[str],int)

  

   Retrieves a specified number of items in the enumeration sequence.

  

   celt: The number of strings to return in rgelt.

   Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def Reset(self):
  """
  Reset(self: UCOMIEnumString) -> int

  

   Resets the enumeration sequence to the beginning.

   Returns: An HRESULT with the value S_OK.
  """
  pass
 def Skip(self,celt):
  """
  Skip(self: UCOMIEnumString,celt: int) -> int

  

   Skips over a specified number of items in the enumeration sequence.

  

   celt: The number of elements to skip in the enumeration.

   Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
