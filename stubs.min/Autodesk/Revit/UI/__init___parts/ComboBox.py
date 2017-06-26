class ComboBox(RibbonItem):
    """ This class represents a selection control with a drop-down list that can be shown or hidden by clicking the arrow. """
    def AddItem(self, memberData):
        """
        AddItem(self: ComboBox, memberData: ComboBoxMemberData) -> ComboBoxMember
        
            Adds a new item to the ComboBox.
        
            memberData: An object containing the data needed to construct the ComboBoxMember.
            Returns: The newly added ComboBoxMember.
        """
        pass

    def AddItems(self, memberData):
        """ AddItems(self: ComboBox, memberData: IList[ComboBoxMemberData]) -> IList[ComboBoxMember] """
        pass

    def AddSeparator(self):
        """
        AddSeparator(self: ComboBox)
            Adds a separator to the drop-down list.
        """
        pass

    def GetItems(self):
        """
        GetItems(self: ComboBox) -> IList[ComboBoxMember]
        
            Gets the copy of a collection of the ComboBoxMembers assigned to the ComboBox.
        """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current checked ComboBox member of the ComboBox.

Get: Current(self: ComboBox) -> ComboBoxMember

Set: Current(self: ComboBox) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBox.

Get: Image(self: ComboBox) -> ImageSource

Set: Image(self: ComboBox) = value
"""


    CurrentChanged = None
    DropDownClosed = None
    DropDownOpened = None
    m_ItemType = None

