class UCOMIEnumMoniker:
 """ Use System.Runtime.InteropServices.ComTypes.IEnumMoniker instead. """
 def Clone(self,ppenum):
  """
  Clone(self: UCOMIEnumMoniker) -> UCOMIEnumMoniker

  

   Creates another enumerator that contains the same enumeration state as the current one.
  """
  pass
 def Next(self,celt,rgelt,pceltFetched):
  """
  Next(self: UCOMIEnumMoniker,celt: int) -> (int,Array[UCOMIMoniker],int)

  

   Retrieves a specified number of items in the enumeration sequence.

  

   celt: The number of monikers to return in rgelt.

   Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def Reset(self):
  """
  Reset(self: UCOMIEnumMoniker) -> int

  

   Resets the enumeration sequence to the beginning.

   Returns: An HRESULT with the value S_OK.
  """
  pass
 def Skip(self,celt):
  """
  Skip(self: UCOMIEnumMoniker,celt: int) -> int

  

   Skips over a specified number of items in the enumeration sequence.

  

   celt: The number of elements to skip in the enumeration.

   Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
