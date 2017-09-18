class CharacterRange(object):
 """
 Specifies a range of character positions within a string.

 

 CharacterRange(First: int,Length: int)
 """
 def Equals(self,obj):
  """
  Equals(self: CharacterRange,obj: object) -> bool

  

   Gets a value indicating whether this object is equivalent to the specified object.

  

   obj: The object to compare to for equality.

   Returns: true to indicate the specified object is an instance with the same 

    System.Drawing.CharacterRange.First and System.Drawing.CharacterRange.Length value as this 

    instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: CharacterRange) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,First,Length):
  """
  __new__[CharacterRange]() -> CharacterRange

  

  __new__(cls: type,First: int,Length: int)
  """
  pass
 def __ne__(self,*args):
  pass
 First=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position in the string of the first character of this System.Drawing.CharacterRange.



Get: First(self: CharacterRange) -> int



Set: First(self: CharacterRange)=value

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of positions in this System.Drawing.CharacterRange.



Get: Length(self: CharacterRange) -> int



Set: Length(self: CharacterRange)=value

"""


