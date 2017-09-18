class TabControlEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.TabControl.Selected and System.Windows.Forms.TabControl.Deselected events of a System.Windows.Forms.TabControl control.

 

 TabControlEventArgs(tabPage: TabPage,tabPageIndex: int,action: TabControlAction)
 """
 @staticmethod
 def __new__(self,tabPage,tabPageIndex,action):
  """ __new__(cls: type,tabPage: TabPage,tabPageIndex: int,action: TabControlAction) """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating which event is occurring.



Get: Action(self: TabControlEventArgs) -> TabControlAction



"""

 TabPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.TabPage the event is occurring for.



Get: TabPage(self: TabControlEventArgs) -> TabPage



"""

 TabPageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the System.Windows.Forms.TabControlEventArgs.TabPage in the System.Windows.Forms.TabControl.TabPages collection.



Get: TabPageIndex(self: TabControlEventArgs) -> int



"""


