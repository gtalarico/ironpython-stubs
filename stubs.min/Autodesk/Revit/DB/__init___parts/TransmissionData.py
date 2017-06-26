class TransmissionData(object,IDisposable):
 """
 A class representing information on all external file references
    in a document.
 
 TransmissionData(other: TransmissionData)
 """
 def Dispose(self):
  """ Dispose(self: TransmissionData) """
  pass
 @staticmethod
 def DocumentIsNotTransmitted(filePath):
  """
  DocumentIsNotTransmitted(filePath: ModelPath) -> bool
  
   Determines whether the document at a given file location
     is not transmitted.
  
   filePath: The path to the document whose transmitted state will be checked.
   Returns: False if the document is a transmitted file,true otherwise.
  """
  pass
 def GetAllExternalFileReferenceIds(self):
  """
  GetAllExternalFileReferenceIds(self: TransmissionData) -> ICollection[ElementId]
  
   Gets the ids of all ExternalFileReferences.
   Returns: The ids of all ExternalFileReferences.
  """
  pass
 def GetDesiredReferenceData(self,elemId):
  """
  GetDesiredReferenceData(self: TransmissionData,elemId: ElementId) -> ExternalFileReference
  
   Gets the ExternalFileReference representing path
     and load status 
    information to be used the next time
     this TransmissionData's document is 
    loaded.
  
  
   elemId: The ElementId of the Element which the external file
     reference is a 
    component of.
  
   Returns: An ExternalFileReference containing the requested
     path and load status 
    information for an external file
  """
  pass
 def GetLastSavedReferenceData(self,elemId):
  """
  GetLastSavedReferenceData(self: TransmissionData,elemId: ElementId) -> ExternalFileReference
  
   Gets the ExternalFileReference representing path
     and load status 
    information concerning the most
     recent time this TransmissionData's 
    document was opened.
  
  
   elemId: The ElementId of the Element which the external file
     reference is a 
    component of.
  
   Returns: An ExternalFileReference containing the previous
     path and load status 
    information for an external file
  """
  pass
 @staticmethod
 def IsDocumentTransmitted(filePath):
  """
  IsDocumentTransmitted(filePath: ModelPath) -> bool
  
   Determines whether the document at a given file location
     is transmitted.
  
   filePath: The path to the document whose transmitted state will be checked.
   Returns: True if the document is a transmitted file,false otherwise.
  """
  pass
 @staticmethod
 def ReadTransmissionData(path):
  """
  ReadTransmissionData(path: ModelPath) -> TransmissionData
  
   Reads the TransmissionData associated with the
     file at the given location.
  
   path: A ModelPath indicating the file Revit should read
     the TransmissionData of.
  
    If this ModelPath is a file path,it must be an absolute path.
  
   Returns: The TransmissionData containing external file
     information for the file at 
    the given location.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TransmissionData,disposing: bool) """
  pass
 def SetDesiredReferenceData(self,elemId,path,pathType,shouldLoad):
  """
  SetDesiredReferenceData(self: TransmissionData,elemId: ElementId,path: ModelPath,pathType: PathType,shouldLoad: bool)
   Sets the ExternalFileReference information which
     Revit should use the next 
    time it opens the document
     which this TransmissionData belongs to.
  
  
   elemId: The id of the element associated with this reference.
   path: A ModelPath indicating the location to load the external
     file reference 
    from.
  
   pathType: A PathType value indicating what type of path the ModelPath is.
   shouldLoad: True if the external file should be loaded the next time Revit
     opens the 
    document. False if it should be unloaded.
  """
  pass
 @staticmethod
 def WriteTransmissionData(path,data):
  """
  WriteTransmissionData(path: ModelPath,data: TransmissionData)
   Writes the given TransmissionData into the Revit file at the
     given location.
  
   path: A ModelPath indicating the file Revit should write
     the TransmissionData of.
    
     This ModelPath must be a file path and an absolute path.
  
   data: The TransmissionData to be written into the document.
     Note that Revit will 
    not check that the ElementIds in
     the TransmissionData correspond to real 
    Elements.
  """
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
 @staticmethod
 def __new__(self,other):
  """ __new__(cls: type,other: TransmissionData) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsTransmitted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether this file has been transmitted or not.

Get: IsTransmitted(self: TransmissionData) -> bool

Set: IsTransmitted(self: TransmissionData)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TransmissionData) -> bool

"""

 UserData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A string which users can store notes in.

Get: UserData(self: TransmissionData) -> str

Set: UserData(self: TransmissionData)=value
"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The format version for TransmissionData

Get: Version(self: TransmissionData) -> int

"""


