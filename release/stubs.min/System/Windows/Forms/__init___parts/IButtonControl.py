class IButtonControl:
 """ Allows a control to act like a button on a form. """
 def NotifyDefault(self,value):
  """
  NotifyDefault(self: IButtonControl,value: bool)

   Notifies a control that it is the default button so that its appearance and behavior is adjusted 

    accordingly.

  

  

   value: true if the control should behave as a default button; otherwise false.
  """
  pass
 def PerformClick(self):
  """
  PerformClick(self: IButtonControl)

   Generates a System.Windows.Forms.Control.Click event for the control.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 DialogResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value returned to the parent form when the button is clicked.



Get: DialogResult(self: IButtonControl) -> DialogResult



Set: DialogResult(self: IButtonControl)=value

"""


