class ConduitSizeSettings(Element,IDisposable,IEnumerable[KeyValuePair[str,ConduitSizes]],IEnumerable):
 """ Conduit sizes settings """
 def AddSize(self,standardName,sizeInfo):
  """
  AddSize(self: ConduitSizeSettings,standardName: str,sizeInfo: ConduitSize)
   Inserts a new ConduitSize in to the conduit size settings. The conduit standard 
    name determines the location of the new size in the size table.
  
  
   standardName: The conduit standard name.
   sizeInfo: The new ConduitSize to be added.
  """
  pass
 def CreateConduitStandardTypeFromExisingStandardType(self,pADoc,newStandardName,existingStandardName):
  """
  CreateConduitStandardTypeFromExisingStandardType(self: ConduitSizeSettings,pADoc: Document,newStandardName: str,existingStandardName: str) -> bool
  
   Creates one conduit standard type with the new name and assign the conduit 
    sizes to it from the existing standard type.
  
  
   pADoc: The document.
   newStandardName: The new conduit standard name.
   existingStandardName: The existing conduit standard name.
   Returns: True if creating success; otherwise false.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def DoesConduitStandardTypeExist(self,standardName):
  """
  DoesConduitStandardTypeExist(self: ConduitSizeSettings,standardName: str) -> bool
  
   Checks if the specified conduit standard exist.
  
   standardName: The conduit standard name.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetConduitSizeSettings(aDoc):
  """
  GetConduitSizeSettings(aDoc: Document) -> ConduitSizeSettings
  
   Gets the conduit size settings of the project.
  
   aDoc: The document.
   Returns: The conduit size settings of the project.
  """
  pass
 def GetConduitSizeSettingsIterator(self):
  """
  GetConduitSizeSettingsIterator(self: ConduitSizeSettings) -> ConduitSizeSettingIterator
  
   Returns a ConduitSizeSettingIterator to the conduit size settings.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ConduitSizeSettings) -> IEnumerator[KeyValuePair[str,ConduitSizes]]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetSizeCount(self,standardName):
  """
  GetSizeCount(self: ConduitSizeSettings,standardName: str) -> int
  
   Gets the size count of the conduit size table. The conduit standard name the 
    location of the size in the size table.
  
  
   standardName: The conduit standard name.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveConduitStandardType(self,pADoc,standardName):
  """
  RemoveConduitStandardType(self: ConduitSizeSettings,pADoc: Document,standardName: str) -> bool
  
   Erases the existing ConduitSizes with this conduit standard name; the consuit 
    standard type can not be removed if it is in use.
  
  
   pADoc: The document.
   standardName: The conduit standard name.
   Returns: True if removing success; otherwise false.
  """
  pass
 def RemoveSize(self,standardName,nominalDiameter):
  """
  RemoveSize(self: ConduitSizeSettings,standardName: str,nominalDiameter: float)
   Erase the existing ConduitSize with this nominal diameter. The conduit standard 
    name determines the location of the size in the size table.
  
  
   standardName: The conduit standard name.
   nominalDiameter: Nominal diameter.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyValuePair[str,ConduitSizes]](enumerable: IEnumerable[KeyValuePair[str,ConduitSizes]],value: KeyValuePair[str,ConduitSizes]) -> bool """
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
