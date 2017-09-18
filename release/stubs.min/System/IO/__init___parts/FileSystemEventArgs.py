class FileSystemEventArgs(EventArgs):
 """
 Provides data for the directory events: System.IO.FileSystemWatcher.Changed,System.IO.FileSystemWatcher.Created,System.IO.FileSystemWatcher.Deleted.

 

 FileSystemEventArgs(changeType: WatcherChangeTypes,directory: str,name: str)
 """
 @staticmethod
 def __new__(self,changeType,directory,name):
  """ __new__(cls: type,changeType: WatcherChangeTypes,directory: str,name: str) """
  pass
 ChangeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of directory event that occurred.



Get: ChangeType(self: FileSystemEventArgs) -> WatcherChangeTypes



"""

 FullPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualifed path of the affected file or directory.



Get: FullPath(self: FileSystemEventArgs) -> str



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the affected file or directory.



Get: Name(self: FileSystemEventArgs) -> str



"""


