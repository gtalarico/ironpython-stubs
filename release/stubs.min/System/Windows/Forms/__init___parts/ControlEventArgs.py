class ControlEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.ControlAdded and System.Windows.Forms.Control.ControlRemoved events.

 

 ControlEventArgs(control: Control)
 """
 @staticmethod
 def __new__(self,control):
  """ __new__(cls: type,control: Control) """
  pass
 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control object used by this event.



Get: Control(self: ControlEventArgs) -> Control



"""


