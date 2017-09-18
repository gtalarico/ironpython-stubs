class GeneratorPosition(object):
 """
 System.Windows.Controls.Primitives.GeneratorPosition is used to describe the position of an item that is managed by System.Windows.Controls.ItemContainerGenerator.

 

 GeneratorPosition(index: int,offset: int)
 """
 def Equals(self,o):
  """
  Equals(self: GeneratorPosition,o: object) -> bool

  

   Compares the specified instance and the current instance of 

    System.Windows.Controls.Primitives.GeneratorPosition for value equality.

  

  

   o: The System.Windows.Controls.Primitives.GeneratorPosition instance to compare.

   Returns: true if o and this instance of System.Windows.Controls.Primitives.GeneratorPosition have the 

    same values.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GeneratorPosition) -> int

  

   Returns the hash code for this System.Windows.Controls.Primitives.GeneratorPosition.

   Returns: The hash code for this System.Windows.Controls.Primitives.GeneratorPosition.
  """
  pass
 def ToString(self):
  """
  ToString(self: GeneratorPosition) -> str

  

   Returns a string representation of this instance of 

    System.Windows.Controls.Primitives.GeneratorPosition.

  

   Returns: A string representation of this instance of System.Windows.Controls.Primitives.GeneratorPosition
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,index,offset):
  """
  __new__(cls: type,index: int,offset: int)

  __new__[GeneratorPosition]() -> GeneratorPosition
  """
  pass
 def __ne__(self,*args):
  pass
 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Int32 index that is relative to the generated (realized) items.



Get: Index(self: GeneratorPosition) -> int



Set: Index(self: GeneratorPosition)=value

"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Int32 offset that is relative to the ungenerated (unrealized) items near the indexed item.



Get: Offset(self: GeneratorPosition) -> int



Set: Offset(self: GeneratorPosition)=value

"""


