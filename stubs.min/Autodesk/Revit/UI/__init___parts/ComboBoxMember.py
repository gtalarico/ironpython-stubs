class ComboBoxMember(RibbonItem):
 """ This class represents an item in the drop-down list of a ComboBox. """
 GroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The group to which the ComboBoxMember is assigned.

Get: GroupName(self: ComboBoxMember) -> str

"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image shown on the ComboBoxMember.

Get: Image(self: ComboBoxMember) -> ImageSource

Set: Image(self: ComboBoxMember)=value
"""


 m_ItemType=None

