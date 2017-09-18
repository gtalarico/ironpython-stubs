class ComboBoxMemberData(RibbonItemData):
 """
 This class contains information necessary to construct a ComboBoxMember.
 
 ComboBoxMemberData(name: str,text: str)
 """
 @staticmethod
 def __new__(self,name,text):
  """ __new__(cls: type,name: str,text: str) """
  pass
 GroupName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a group name for the ComboBoxMember.

Get: GroupName(self: ComboBoxMemberData) -> str

Set: GroupName(self: ComboBoxMemberData)=value
"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image shown on the ComboBoxMember.

Get: Image(self: ComboBoxMemberData) -> ImageSource

Set: Image(self: ComboBoxMemberData)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user-visible text of the ComboBoxMember.

Get: Text(self: ComboBoxMemberData) -> str

Set: Text(self: ComboBoxMemberData)=value
"""


