class FileDialogCustomPlace(object):
 """
 Represents an entry in a System.Windows.Forms.FileDialog custom place collection for Windows Vista.

 

 FileDialogCustomPlace(path: str)

 FileDialogCustomPlace(knownFolderGuid: Guid)
 """
 def ToString(self):
  """
  ToString(self: FileDialogCustomPlace) -> str

  

   Returns a string that represents this System.Windows.Forms.FileDialogCustomPlace instance.

   Returns: A string that represents this System.Windows.Forms.FileDialogCustomPlace instance.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,path: str)

  __new__(cls: type,knownFolderGuid: Guid)
  """
  pass
 KnownFolderGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Windows Vista Known Folder GUID for the custom place.



Get: KnownFolderGuid(self: FileDialogCustomPlace) -> Guid



Set: KnownFolderGuid(self: FileDialogCustomPlace)=value

"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the folder path to the custom place.



Get: Path(self: FileDialogCustomPlace) -> str



Set: Path(self: FileDialogCustomPlace)=value

"""


