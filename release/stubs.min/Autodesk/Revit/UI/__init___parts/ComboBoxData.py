class ComboBoxData(RibbonItemData):
 """
 This class contains information necessary to construct a combo box in the Ribbon.

 

 ComboBoxData(name: str)
 """
 @staticmethod
 def __new__(self,name):
  """ __new__(cls: type,name: str) """
  pass
 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The image shown on the ComboBox.



Get: Image(self: ComboBoxData) -> ImageSource



Set: Image(self: ComboBoxData)=value

"""


