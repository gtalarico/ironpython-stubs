class KeyBasedTreeEntryTable(Element,IDisposable):
 """ KeyBasedTreeEntryTable represents the collection of key-based tree entries for a document. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetKeyBasedTreeEntries(self):
  """
  GetKeyBasedTreeEntries(self: KeyBasedTreeEntryTable) -> KeyBasedTreeEntries
  
   Gets the KeyBasedTreeEntries for this table.
   Returns: The KeyBasedTreeEntries for this table.
  """
  pass
 def LoadFrom(self,desiredResourceReference,loadResults):
  """
  LoadFrom(self: KeyBasedTreeEntryTable,desiredResourceReference: ExternalResourceReference,loadResults: KeyBasedTreeEntriesLoadResults) -> ExternalResourceLoadStatus
  
   Loads KeyBasedTreeEntries from the specified external resource into this 
    KeyBasedTreeEntryTable.
  
  
   desiredResourceReference: An external resource reference describing the source of the desired 
    KeyBasedTreeEntry data.
  
   loadResults: If provided,Revit will use this object to store any
     errors or warnings 
    that were encountered. This argument may be ll.
  
   Returns: Returns whether the operation succeeded or failed.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def Reload(self,loadResults):
  """
  Reload(self: KeyBasedTreeEntryTable,loadResults: KeyBasedTreeEntriesLoadResults) -> ExternalResourceLoadStatus
  
   Reloads KeyBasedTreeEntries from their currently-stored location into this 
    KeyBasedTreeEntryTable.
  
  
   loadResults: If provided,Revit will use this object to store any
     errors or warnings 
    that were encountered.  Note that if the KeyBasedTreeEntries in the model are
   
      already up to date,no errors or warnings will be added to this object. This 
    argument may be ll.
  
   Returns: Returns the outcome of the reload operation.
  """
  pass
 def ServerSupports(self,extRef):
  """
  ServerSupports(self: KeyBasedTreeEntryTable,extRef: ExternalResourceReference) -> bool
  
   Checks if the server referenced by the given ExternalResourceReference supports 
    the
     ExternalResourceReferenceType of this KeyBasedTreeEntryTable.
  
  
   extRef: The ExternalResourceReference to check.
   Returns: True if the ExternalResourceReference refers to a server that supports the 
    ExternalResourceReferenceType of this KeyBasedTreeEntryTable.
     False 
    otherwise.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
