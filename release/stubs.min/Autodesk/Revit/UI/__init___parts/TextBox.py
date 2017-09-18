class TextBox(RibbonItem):
 """ The TextBox object represents text-based control that allows the user to enter text. """
 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image of the TextBox.



Get: Image(self: TextBox) -> ImageSource



Set: Image(self: TextBox)=value

"""

 PromptText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The prompt text for the text box.



Get: PromptText(self: TextBox) -> str



Set: PromptText(self: TextBox)=value

"""

 SelectTextOnFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A value that indicates if the text is selected when the text box gains focus.



Get: SelectTextOnFocus(self: TextBox) -> bool



Set: SelectTextOnFocus(self: TextBox)=value

"""

 ShowImageAsButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates if the Image set 

in the text box should be displayed as a clickable button.



Get: ShowImageAsButton(self: TextBox) -> bool



Set: ShowImageAsButton(self: TextBox)=value

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The object that supplies the text value.



Get: Value(self: TextBox) -> object



Set: Value(self: TextBox)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the TextBox.



Get: Width(self: TextBox) -> float



Set: Width(self: TextBox)=value

"""


 EnterPressed=None
 m_ItemType=None

