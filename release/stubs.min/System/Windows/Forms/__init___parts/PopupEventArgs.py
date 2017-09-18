class PopupEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.ToolTip.Popup event.

 

 PopupEventArgs(associatedWindow: IWin32Window,associatedControl: Control,isBalloon: bool,size: Size)
 """
 @staticmethod
 def __new__(self,associatedWindow,associatedControl,isBalloon,size):
  """ __new__(cls: type,associatedWindow: IWin32Window,associatedControl: Control,isBalloon: bool,size: Size) """
  pass
 AssociatedControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control for which the System.Windows.Forms.ToolTip is being drawn.



Get: AssociatedControl(self: PopupEventArgs) -> Control



"""

 AssociatedWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window to which this System.Windows.Forms.ToolTip is bound.



Get: AssociatedWindow(self: PopupEventArgs) -> IWin32Window



"""

 IsBalloon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the ToolTip is displayed as a standard rectangular or a balloon window.



Get: IsBalloon(self: PopupEventArgs) -> bool



"""

 ToolTipSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the ToolTip.



Get: ToolTipSize(self: PopupEventArgs) -> Size



Set: ToolTipSize(self: PopupEventArgs)=value

"""


