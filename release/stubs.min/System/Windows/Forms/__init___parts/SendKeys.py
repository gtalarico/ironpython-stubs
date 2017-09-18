class SendKeys(object):
 """ Provides methods for sending keystrokes to an application. """
 @staticmethod
 def Flush():
  """
  Flush()

   Processes all the Windows messages currently in the message queue.
  """
  pass
 @staticmethod
 def Send(keys):
  """
  Send(keys: str)

   Sends keystrokes to the active application.

  

   keys: The string of keystrokes to send.
  """
  pass
 @staticmethod
 def SendWait(keys):
  """
  SendWait(keys: str)

   Sends the given keys to the active application,and then waits for the messages to be processed.

  

   keys: The string of keystrokes to send.
  """
  pass
