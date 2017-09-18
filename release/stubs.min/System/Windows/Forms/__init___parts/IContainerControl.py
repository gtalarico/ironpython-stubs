class IContainerControl:
 """ Provides the functionality for a control to act as a parent for other controls. """
 def ActivateControl(self,active):
  """
  ActivateControl(self: IContainerControl,active: Control) -> bool

  

   Activates a specified control.

  

   active: The System.Windows.Forms.Control being activated.

   Returns: true if the control is successfully activated; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ActiveControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control that is active on the container control.



Get: ActiveControl(self: IContainerControl) -> Control



Set: ActiveControl(self: IContainerControl)=value

"""


