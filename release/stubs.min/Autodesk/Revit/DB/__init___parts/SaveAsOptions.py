class SaveAsOptions(object,IDisposable):
 """
 This class contains options available for saving a document to disk with a new filename.

 

 SaveAsOptions()
 """
 def Dispose(self):
  """ Dispose(self: SaveAsOptions) """
  pass
 def GetWorksharingOptions(self):
  """
  GetWorksharingOptions(self: SaveAsOptions) -> WorksharingSaveAsOptions

  

   Gets Worksharing options for SaveAs.

   Returns: Defaults to ll.

     For a workshared model,if ll default values for 

    WorksharingSaveAsOptions are used.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SaveAsOptions,disposing: bool) """
  pass
 def SetWorksharingOptions(self,worksharingOptions):
  """
  SetWorksharingOptions(self: SaveAsOptions,worksharingOptions: WorksharingSaveAsOptions)

   Sets Worksharing options for SaveAs.

  

   worksharingOptions: Must be ll for a non-workshared model.  Allowed to be ll for a workshared 

    model,

     in which case default values for WorksharingSaveAsOptions are used.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Compact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Default is false: let the OS eliminate as much or as little dead data as it wants to.

   True: force the OS to eliminate all dead data from the file on disk.



Get: Compact(self: SaveAsOptions) -> bool



Set: Compact(self: SaveAsOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: SaveAsOptions) -> bool



"""

 MaximumBackups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum number of backups to keep on disk.



Get: MaximumBackups(self: SaveAsOptions) -> int



Set: MaximumBackups(self: SaveAsOptions)=value

"""

 OverwriteExistingFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the operation should be able to overwrite an existing file.



Get: OverwriteExistingFile(self: SaveAsOptions) -> bool



Set: OverwriteExistingFile(self: SaveAsOptions)=value

"""

 PreviewViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The view id that will be used to generate the preview; this id is not saved to the document's permanent settings.



Get: PreviewViewId(self: SaveAsOptions) -> ElementId



Set: PreviewViewId(self: SaveAsOptions)=value

"""


