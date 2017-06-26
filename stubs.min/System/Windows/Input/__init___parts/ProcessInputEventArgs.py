class ProcessInputEventArgs(NotifyInputEventArgs):
 """ Provides data for postprocess input events. """
 def PeekInput(self):
  """
  PeekInput(self: ProcessInputEventArgs) -> StagingAreaInputItem
  
   Gets,but does not pop,the input event on the top of the staging area stack.
   Returns: The input event that is on the top of the staging area stack.
  """
  pass
 def PopInput(self):
  """
  PopInput(self: ProcessInputEventArgs) -> StagingAreaInputItem
  
   Removes the input event off the top of the staging area stack.
   Returns: The input event that was on the top of the staging area stack. This will be 
    null if the staging area is empty.
  """
  pass
 def PushInput(self,input,promote=None):
  """
  PushInput(self: ProcessInputEventArgs,input: StagingAreaInputItem) -> StagingAreaInputItem
  
   Puts the specified input event onto the top of the staging area stack.
  
   input: The input event to put on the staging area stack.
   Returns: The staging area input item.
  PushInput(self: ProcessInputEventArgs,input: InputEventArgs,promote: StagingAreaInputItem) -> StagingAreaInputItem
  
   Puts the specified input event onto the top of the specified staging area stack.
  
   input: The input event to put on the staging area stack.
   promote: An existing staging area item to promote the state from.
   Returns: The staging area input item that wraps the specified input.
  """
  pass
