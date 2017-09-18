class WaitForChangedResult(object):
 """ Contains information on the change that occurred. """
 ChangeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of change that occurred.



Get: ChangeType(self: WaitForChangedResult) -> WatcherChangeTypes



Set: ChangeType(self: WaitForChangedResult)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the file or directory that changed.



Get: Name(self: WaitForChangedResult) -> str



Set: Name(self: WaitForChangedResult)=value

"""

 OldName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the original name of the file or directory that was renamed.



Get: OldName(self: WaitForChangedResult) -> str



Set: OldName(self: WaitForChangedResult)=value

"""

 TimedOut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the wait operation timed out.



Get: TimedOut(self: WaitForChangedResult) -> bool



Set: TimedOut(self: WaitForChangedResult)=value

"""


