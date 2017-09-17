class ComponentDispatcher(object):
 """ Enables shared control of the message pump between Win32 and WPF in interoperation scenarios. """
 @staticmethod
 def PopModal():
  """
  PopModal()
   Called to indicate that a modal thread is no longer modal.
  """
  pass
 @staticmethod
 def PushModal():
  """
  PushModal()
   Called to indicate that the thread is modal.
  """
  pass
 @staticmethod
 def RaiseIdle():
  """
  RaiseIdle()
   Called to indicate that a thread is idle.
  """
  pass
 @staticmethod
 def RaiseThreadMessage(msg):
  """
  RaiseThreadMessage(msg: MSG) -> (bool,MSG)
  
   Indicates that a new message is available for possible handling.
  
   msg: The message and its associated data.
   Returns: true,if one of the modules listening to the message loop processed the 
    message. The owner of the message loop should ignore the message. false,if the 
    message was not processed. In this case,the owner of the message pump should 
    call the Win32 function TranslateMessage followed by DispatchMessage.
  """
  pass
 CurrentKeyboardMessage=None
 EnterThreadModal=None
 IsThreadModal=True
 LeaveThreadModal=None
 ThreadFilterMessage=None
 ThreadIdle=None
 ThreadPreprocessMessage=None
 __all__=[
  'EnterThreadModal',
  'LeaveThreadModal',
  'PopModal',
  'PushModal',
  'RaiseIdle',
  'RaiseThreadMessage',
  'ThreadFilterMessage',
  'ThreadIdle',
  'ThreadPreprocessMessage',
 ]

