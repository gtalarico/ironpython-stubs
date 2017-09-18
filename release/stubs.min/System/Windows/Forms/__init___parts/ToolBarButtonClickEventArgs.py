class ToolBarButtonClickEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolBar.ButtonClick event.

 

 ToolBarButtonClickEventArgs(button: ToolBarButton)
 """
 @staticmethod
 def __new__(self,button):
  """ __new__(cls: type,button: ToolBarButton) """
  pass
 Button=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.ToolBarButton that was clicked.



Get: Button(self: ToolBarButtonClickEventArgs) -> ToolBarButton



Set: Button(self: ToolBarButtonClickEventArgs)=value

"""


