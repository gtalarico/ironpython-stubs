class UCOMIEnumVARIANT:
 """ Use System.Runtime.InteropServices.ComTypes.IEnumVARIANT instead. """
 def Clone(self,ppenum):
  """
  Clone(self: UCOMIEnumVARIANT,ppenum: int)

   Creates another enumerator that contains the same enumeration state as the current one.

  

   ppenum: On successful return,a reference to the newly created enumerator.
  """
  pass
 def Next(self,celt,rgvar,pceltFetched):
  """
  Next(self: UCOMIEnumVARIANT,celt: int,rgvar: int,pceltFetched: int) -> int

  

   Retrieves a specified number of items in the enumeration sequence.

  

   celt: The number of elements to return in rgelt.

   rgvar: On successful return,a reference to the enumerated elements.

   pceltFetched: On successful return,a reference to the actual number of elements enumerated in rgelt.

   Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise,S_FALSE.
  """
  pass
 def Reset(self):
  """
  Reset(self: UCOMIEnumVARIANT) -> int

  

   Resets the enumeration sequence to the beginning.

   Returns: An HRESULT with the value S_OK.
  """
  pass
 def Skip(self,celt):
  """
  Skip(self: UCOMIEnumVARIANT,celt: int) -> int

  

   Skips over a specified number of items in the enumeration sequence.

  

   celt: The number of elements to skip in the enumeration.

   Returns: S_OK if the number of elements skipped equals celt parameter; otherwise,S_FALSE.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
