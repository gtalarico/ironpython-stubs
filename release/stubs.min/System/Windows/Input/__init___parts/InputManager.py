class InputManager(DispatcherObject):
 """ Manages all the input systems in Windows Presentation Foundation (WPF). """
 def PopMenuMode(self,menuSite):
  """
  PopMenuMode(self: InputManager,menuSite: PresentationSource)
   Called by components to leave menu mode.
  
   menuSite: The menu to leave.
  """
  pass
 def ProcessInput(self,input):
  """
  ProcessInput(self: InputManager,input: InputEventArgs) -> bool
  
   Processes the specified input synchronously.
  
   input: The input to process.
   Returns: true if all input events were handled; otherwise,false.
  """
  pass
 def PushMenuMode(self,menuSite):
  """
  PushMenuMode(self: InputManager,menuSite: PresentationSource)
   Called by components to enter menu mode.
  
   menuSite: The menu to enter.
  """
  pass
 InputProviders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Input.InputManager.InputProviders registered with the System.Windows.Input.InputManager.

Get: InputProviders(self: InputManager) -> ICollection

"""

 IsInMenuMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Windows.Interop.ComponentDispatcher is in menu mode.

Get: IsInMenuMode(self: InputManager) -> bool

"""

 MostRecentInputDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents the input device associated with the most recent input event.

Get: MostRecentInputDevice(self: InputManager) -> InputDevice

"""

 PrimaryKeyboardDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the primary keyboard device.

Get: PrimaryKeyboardDevice(self: InputManager) -> KeyboardDevice

"""

 PrimaryMouseDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the primary mouse device.

Get: PrimaryMouseDevice(self: InputManager) -> MouseDevice

"""


 Current=None
 EnterMenuMode=None
 HitTestInvalidatedAsync=None
 LeaveMenuMode=None
 PostNotifyInput=None
 PostProcessInput=None
 PreNotifyInput=None
 PreProcessInput=None

