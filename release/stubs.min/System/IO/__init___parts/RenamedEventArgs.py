class RenamedEventArgs(FileSystemEventArgs):
 """
 Provides data for the System.IO.FileSystemWatcher.Renamed event.

 

 RenamedEventArgs(changeType: WatcherChangeTypes,directory: str,name: str,oldName: str)
 """
 @staticmethod
 def __new__(self,changeType,directory,name,oldName):
  """ __new__(cls: type,changeType: WatcherChangeTypes,directory: str,name: str,oldName: str) """
  pass
 OldFullPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous fully qualified path of the affected file or directory.



Get: OldFullPath(self: RenamedEventArgs) -> str



"""

 OldName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the old name of the affected file or directory.



Get: OldName(self: RenamedEventArgs) -> str



"""


