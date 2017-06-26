class RadioButtonGroup(RibbonItem):
    """ Represents a group of related buttons in the Ribbon. """
    def AddItem(self, buttonData):
        """
        AddItem(self: RadioButtonGroup, buttonData: ToggleButtonData) -> ToggleButton
        
            Adds a new ToggleButton to the RadioButtonGroup.
        
            buttonData: An object containing the data needed to construct the ToggleButton.
            Returns: The newly added ToggleButton.
        """
        pass

    def AddItems(self, buttonData):
        """ AddItems(self: RadioButtonGroup, buttonData: IList[ToggleButtonData]) -> IList[ToggleButton] """
        pass

    def GetItems(self):
        """
        GetItems(self: RadioButtonGroup) -> IList[ToggleButton]
        
            Gets the collection of ToggleButtons assigned to the RadioButtonGroup.
        """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current checked ToggleButton of the RadioButtonGroup.

Get: Current(self: RadioButtonGroup) -> ToggleButton

Set: Current(self: RadioButtonGroup) = value
"""


    m_ItemType = None

