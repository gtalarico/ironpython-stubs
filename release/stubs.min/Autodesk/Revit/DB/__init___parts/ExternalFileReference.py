class ExternalFileReference(object,IDisposable):
 """ A class that contains the details of a reference to a file outside of a given document. """
 def Dispose(self):
  """ Dispose(self: ExternalFileReference) """
  pass
 def GetAbsolutePath(self):
  """
  GetAbsolutePath(self: ExternalFileReference) -> ModelPath
  
   Returns an absolute path to the referenced file,
     regardless of whether the 
    PathType.Enum is relative or absolute.
  
   Returns: A full path to the linked model.
  """
  pass
 def GetLinkedFileStatus(self):
  """
  GetLinkedFileStatus(self: ExternalFileReference) -> LinkedFileStatus
  
   Returns a LinkedFileStatus.Enum corresponding to the
     load status of the 
    referenced file.
  """
  pass
 def GetPath(self):
  """
  GetPath(self: ExternalFileReference) -> ModelPath
  
   Gets the path of the link,relative or absolute according
     to the link's 
    settings
  
   Returns: The path of the link. This path will be relative for
     relatively-pathed 
    links.
  """
  pass
 def GetReferencingId(self):
  """
  GetReferencingId(self: ExternalFileReference) -> ElementId
  
   Gets the ElementId corresponding to the element which
     this 
    ExternalFileReference is associated with.
  """
  pass
 @staticmethod
 def IsValidExternalFileReference(data):
  """
  IsValidExternalFileReference(data: ExternalFileReference) -> bool
  
   Checks an ExternalFileReference to see if it is
     properly created.
  
   data: The ExternalFileReference to be checked
  """
  pass
 def IsValidPathTypeForExternalFileReference(self,pathType):
  """
  IsValidPathTypeForExternalFileReference(self: ExternalFileReference,pathType: PathType) -> bool
  
   Checks whether a PathType enum value will be valid to
     use with this 
    ExternalFileReference.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalFileReference,disposing: bool) """
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
 ExternalFileReferenceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of external file which this object
   references.

Get: ExternalFileReferenceType(self: ExternalFileReference) -> ExternalFileReferenceType

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalFileReference) -> bool

"""

 PathType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path type of the link (relative,absolute,or server).

Get: PathType(self: ExternalFileReference) -> PathType

"""


