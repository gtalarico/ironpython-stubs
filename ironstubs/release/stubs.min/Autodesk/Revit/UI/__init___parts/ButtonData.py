class ButtonData(RibbonItemData):
 """ Base class used to contain information necessary to construct a button in the Ribbon. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,name: str,text: str) """
  pass
 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image of the button.

Get: Image(self: ButtonData) -> ImageSource

Set: Image(self: ButtonData)=value
"""

 LargeImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The large image of the button.

Get: LargeImage(self: ButtonData) -> ImageSource

Set: LargeImage(self: ButtonData)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user-visible text of the button.

Get: Text(self: ButtonData) -> str

Set: Text(self: ButtonData)=value
"""


