class TabControlCancelEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.TabControl.Selecting and System.Windows.Forms.TabControl.Deselecting events of a System.Windows.Forms.TabControl control.

 

 TabControlCancelEventArgs(tabPage: TabPage,tabPageIndex: int,cancel: bool,action: TabControlAction)
 """
 @staticmethod
 def __new__(self,tabPage,tabPageIndex,cancel,action):
  """ __new__(cls: type,tabPage: TabPage,tabPageIndex: int,cancel: bool,action: TabControlAction) """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating which event is occurring.



Get: Action(self: TabControlCancelEventArgs) -> TabControlAction



"""

 TabPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.TabPage the event is occurring for.



Get: TabPage(self: TabControlCancelEventArgs) -> TabPage



"""

 TabPageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the System.Windows.Forms.TabControlCancelEventArgs.TabPage in the System.Windows.Forms.TabControl.TabPages collection.



Get: TabPageIndex(self: TabControlCancelEventArgs) -> int



"""


