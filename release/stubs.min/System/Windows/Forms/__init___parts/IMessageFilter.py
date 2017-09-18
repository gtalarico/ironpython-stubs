class IMessageFilter:
 """ Defines a message filter interface. """
 def PreFilterMessage(self,m):
  """
  PreFilterMessage(self: IMessageFilter,m: Message) -> (bool,Message)

  

   Filters out a message before it is dispatched.

  

   m: The message to be dispatched. You cannot modify this message.

   Returns: true to filter the message and stop it from being dispatched; false to allow the message to 

    continue to the next filter or control.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
