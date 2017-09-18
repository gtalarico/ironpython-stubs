class CableTraySizes(Element,IDisposable,IEnumerable[MEPSize],IEnumerable):
 """ Cable tray sizes. """
 def AddSize(self,sizeInfo):
  """
  AddSize(self: CableTraySizes,sizeInfo: MEPSize)

   Inserts a new MEPSize into the cable tray sizes.

     For cable tray,the 

    nominal diameter of MEPSize is used .

  

  

   sizeInfo: The new MEPSize to be added.
  """
  pass
 def ClearAll(self):
  """
  ClearAll(self: CableTraySizes)

   Removes all MEPSizes in the cable tray sizes.
  """
  pass
 def Contains(self,nominalDiameter):
  """
  Contains(self: CableTraySizes,nominalDiameter: float) -> bool

  

   Checks whether a cable tray size with the nominal diameter exists.

  

   nominalDiameter: Nominal diameter.

   Returns: True if a cable tray size with the nominal diameter exists.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetCableTraySizes(aDoc):
  """
  GetCableTraySizes(aDoc: Document) -> CableTraySizes

  

   Gets the cable tray sizes of the project.

  

   aDoc: The document.

   Returns: The cable tray sizes of the project.
  """
  pass
 def GetCableTraySizesIterator(self):
  """
  GetCableTraySizesIterator(self: CableTraySizes) -> CableTraySizeIterator

  

   Returns a CableTraySizeIterator to the MEP cable tray sizes.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CableTraySizes) -> IEnumerator[MEPSize]

  

   Returns an enumerator that iterates through a collection.

   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetSizeCount(self):
  """
  GetSizeCount(self: CableTraySizes) -> int

  

   Gets the size count of the cable tray size table.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveSize(self,sizeInfo):
  """
  RemoveSize(self: CableTraySizes,sizeInfo: MEPSize)

   Erases the existing MEPSize.

     For cable tray,the nominal diameter is used 

    in MEPSize.

  

  

   sizeInfo: The MEPSize to be removed..
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __contains__(self,*args):
  """ __contains__[MEPSize](enumerable: IEnumerable[MEPSize],value: MEPSize) -> bool """
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
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
