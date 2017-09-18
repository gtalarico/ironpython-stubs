class ConsoleKeyInfo(object):
 """
 Describes the console key that was pressed,including the character represented by the console key and the state of the SHIFT,ALT,and CTRL modifier keys.

 

 ConsoleKeyInfo(keyChar: Char,key: ConsoleKey,shift: bool,alt: bool,control: bool)
 """
 def Equals(self,*__args):
  """
  Equals(self: ConsoleKeyInfo,obj: ConsoleKeyInfo) -> bool

  

   Gets a value indicating whether the specified System.ConsoleKeyInfo object is equal to the 

    current System.ConsoleKeyInfo object.

  

  

   obj: An object to compare to the current System.ConsoleKeyInfo object.

   Returns: true if obj is equal to the current System.ConsoleKeyInfo object; otherwise,false.

  Equals(self: ConsoleKeyInfo,value: object) -> bool

  

   Gets a value indicating whether the specified object is equal to the current 

    System.ConsoleKeyInfo object.

  

  

   value: An object to compare to the current System.ConsoleKeyInfo object.

   Returns: true if value is a System.ConsoleKeyInfo object and is equal to the current 

    System.ConsoleKeyInfo object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ConsoleKeyInfo) -> int

  

   Returns the hash code for the current System.ConsoleKeyInfo object.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,keyChar,key,shift,alt,control):
  """
  __new__(cls: type,keyChar: Char,key: ConsoleKey,shift: bool,alt: bool,control: bool)

  __new__[ConsoleKeyInfo]() -> ConsoleKeyInfo
  """
  pass
 def __ne__(self,*args):
  pass
 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the console key represented by the current System.ConsoleKeyInfo object.



Get: Key(self: ConsoleKeyInfo) -> ConsoleKey



"""

 KeyChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Unicode character represented by the current System.ConsoleKeyInfo object.



Get: KeyChar(self: ConsoleKeyInfo) -> Char



"""

 Modifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a bitwise combination of System.ConsoleModifiers values that specifies one or more modifier keys pressed simultaneously with the console key.



Get: Modifiers(self: ConsoleKeyInfo) -> ConsoleModifiers



"""


