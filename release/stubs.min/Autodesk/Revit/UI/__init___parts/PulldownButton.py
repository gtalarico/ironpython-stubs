class PulldownButton(RibbonButton):
 """ The PulldownButton object represents a button with a drop-down list on RibbonPanel. """
 def AddPushButton(self,buttonData):
  """
  AddPushButton(self: PulldownButton,buttonData: PushButtonData) -> PushButton

  

   Adds a new pushbutton to the pulldown button and associates it with an 

    ExternalCommand.

  

  

   buttonData: An object containing the data needed to construct the pushbutton.

   Returns: The newly added pushbutton.
  """
  pass
 def AddSeparator(self):
  """
  AddSeparator(self: PulldownButton)

   Adds a separator to the drop-down list.
  """
  pass
 def GetItems(self):
  """
  GetItems(self: PulldownButton) -> IList[PushButton]

  

   Gets a copy of the collection of buttons assigned to the pulldown button.
  """
  pass
 m_ItemType=None

