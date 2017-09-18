class Size(object):
 """
 Stores an ordered pair of integers,which specify a System.Drawing.Size.Height and System.Drawing.Size.Width.

 

 Size(pt: Point)

 Size(width: int,height: int)
 """
 @staticmethod
 def Add(sz1,sz2):
  """
  Add(sz1: Size,sz2: Size) -> Size

  

   Adds the width and height of one System.Drawing.Size structure to the width and height of 

    another System.Drawing.Size structure.

  

  

   sz1: The first System.Drawing.Size structure to add.

   sz2: The second System.Drawing.Size structure to add.

   Returns: A System.Drawing.Size structure that is the result of the addition operation.
  """
  pass
 @staticmethod
 def Ceiling(value):
  """
  Ceiling(value: SizeF) -> Size

  

   Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 

    rounding the values of the System.Drawing.Size structure to the next higher integer values.

  

  

   value: The System.Drawing.SizeF structure to convert.

   Returns: The System.Drawing.Size structure this method converts to.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Size,obj: object) -> bool

  

   Tests to see whether the specified object is a System.Drawing.Size structure with the same 

    dimensions as this System.Drawing.Size structure.

  

  

   obj: The System.Object to test.

   Returns: true if obj is a System.Drawing.Size and has the same width and height as this 

    System.Drawing.Size; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Size) -> int

  

   Returns a hash code for this System.Drawing.Size structure.

   Returns: An integer value that specifies a hash value for this System.Drawing.Size structure.
  """
  pass
 @staticmethod
 def Round(value):
  """
  Round(value: SizeF) -> Size

  

   Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 

    rounding the values of the System.Drawing.SizeF structure to the nearest integer values.

  

  

   value: The System.Drawing.SizeF structure to convert.

   Returns: The System.Drawing.Size structure this method converts to.
  """
  pass
 @staticmethod
 def Subtract(sz1,sz2):
  """
  Subtract(sz1: Size,sz2: Size) -> Size

  

   Subtracts the width and height of one System.Drawing.Size structure from the width and height of 

    another System.Drawing.Size structure.

  

  

   sz1: The System.Drawing.Size structure on the left side of the subtraction operator.

   sz2: The System.Drawing.Size structure on the right side of the subtraction operator.

   Returns: A System.Drawing.Size structure that is a result of the subtraction operation.
  """
  pass
 def ToString(self):
  """
  ToString(self: Size) -> str

  

   Creates a human-readable string that represents this System.Drawing.Size structure.

   Returns: A string that represents this System.Drawing.Size.
  """
  pass
 @staticmethod
 def Truncate(value):
  """
  Truncate(value: SizeF) -> Size

  

   Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 

    truncating the values of the System.Drawing.SizeF structure to the next lower integer values.

  

  

   value: The System.Drawing.SizeF structure to convert.

   Returns: The System.Drawing.Size structure this method converts to.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Size]() -> Size

  

  __new__(cls: type,pt: Point)

  __new__(cls: type,width: int,height: int)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(sz1: Size,sz2: Size) -> Size

  

   Adds the width and height of one System.Drawing.Size structure to the width and height of 

    another System.Drawing.Size structure.

  

  

   sz1: The first System.Drawing.Size to add.

   sz2: The second System.Drawing.Size to add.

   Returns: A System.Drawing.Size structure that is the result of the addition operation.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(sz1: Size,sz2: Size) -> Size

  

   Subtracts the width and height of one System.Drawing.Size structure from the width and height of 

    another System.Drawing.Size structure.

  

  

   sz1: The System.Drawing.Size structure on the left side of the subtraction operator.

   sz2: The System.Drawing.Size structure on the right side of the subtraction operator.

   Returns: A System.Drawing.Size structure that is the result of the subtraction operation.
  """
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the vertical component of this System.Drawing.Size structure.



Get: Height(self: Size) -> int



Set: Height(self: Size)=value

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tests whether this System.Drawing.Size structure has width and height of 0.



Get: IsEmpty(self: Size) -> bool



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the horizontal component of this System.Drawing.Size structure.



Get: Width(self: Size) -> int



Set: Width(self: Size)=value

"""


 Empty=None

