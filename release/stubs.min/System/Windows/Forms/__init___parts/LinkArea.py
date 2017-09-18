class LinkArea(object):
 """
 Represents an area within a System.Windows.Forms.LinkLabel control that represents a hyperlink within the control.

 

 LinkArea(start: int,length: int)
 """
 def Equals(self,o):
  """
  Equals(self: LinkArea,o: object) -> bool

  

   Determines whether this System.Windows.Forms.LinkArea is equal to the specified object.

  

   o: The object to compare to this System.Windows.Forms.LinkArea.

   Returns: true if the specified object is equal to the current System.Windows.Forms.LinkArea; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: LinkArea) -> int

   Returns: A 32-bit signed integer that is the hash code for this instance.
  """
  pass
 def ToString(self):
  """ ToString(self: LinkArea) -> str """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,start,length):
  """
  __new__(cls: type,start: int,length: int)

  __new__[LinkArea]() -> LinkArea
  """
  pass
 def __ne__(self,*args):
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.LinkArea is empty.



Get: IsEmpty(self: LinkArea) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of characters in the link area.



Get: Length(self: LinkArea) -> int



Set: Length(self: LinkArea)=value

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the starting location of the link area within the text of the System.Windows.Forms.LinkLabel.



Get: Start(self: LinkArea) -> int



Set: Start(self: LinkArea)=value

"""


 LinkAreaConverter=None

