class DocumentVersion(object,IDisposable):
 """ This class uniquely identifies an edition of a given document. """
 def Dispose(self):
  """ Dispose(self: DocumentVersion) """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: DocumentVersion,other: DocumentVersion) -> bool
  
   Checks whether two DocumentVersions are identical.
     They are identical if 
    both the GUID and number of saves
     are equal. If two DocumentVersions are 
    identical,they
     come from the same document,with the same set of changes.
  
  
   other: The DocumentVersion to compare to this DocumentVersion.
   Returns: True if the two DocumentVersions are equal. False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: DocumentVersion,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DocumentVersion) -> bool

"""

 NumberOfSaves=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of times the document has been saved. The save number and GUID
   are both necessary to uniquely identify a document version.

Get: NumberOfSaves(self: DocumentVersion) -> int

"""

 VersionGUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The GUID portion of the DocumentVersion. The GUID is updated when changes
   are made to the document,but may not update with every change to the document.
   The GUID and save number are both necessary to uniquely identify a document version.

Get: VersionGUID(self: DocumentVersion) -> Guid

"""


