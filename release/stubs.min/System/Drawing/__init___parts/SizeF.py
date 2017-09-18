class SizeF(object):
 """
 Stores an ordered pair of floating-point numbers,typically the width and height of a rectangle.

 

 SizeF(size: SizeF)

 SizeF(pt: PointF)

 SizeF(width: Single,height: Single)
 """
 @staticmethod
 def Add(sz1,sz2):
  """
  Add(sz1: SizeF,sz2: SizeF) -> SizeF

  

   Adds the width and height of one System.Drawing.SizeF structure to the width and height of 

    another System.Drawing.SizeF structure.

  

  

   sz1: The first System.Drawing.SizeF structure to add.

   sz2: The second System.Drawing.SizeF structure to add.

   Returns: A System.Drawing.SizeF structure that is the result of the addition operation.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: SizeF,obj: object) -> bool

  

   Tests to see whether the specified object is a System.Drawing.SizeF structure with the same 

    dimensions as this System.Drawing.SizeF structure.

  

  

   obj: The System.Object to test.

   Returns: This method returns true if obj is a System.Drawing.SizeF and has the same width and height as 

    this System.Drawing.SizeF; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SizeF) -> int

  

   Returns a hash code for this System.Drawing.Size structure.

   Returns: An integer value that specifies a hash value for this System.Drawing.Size structure.
  """
  pass
 @staticmethod
 def Subtract(sz1,sz2):
  """
  Subtract(sz1: SizeF,sz2: SizeF) -> SizeF

  

   Subtracts the width and height of one System.Drawing.SizeF structure from the width and height 

    of another System.Drawing.SizeF structure.

  

  

   sz1: The System.Drawing.SizeF structure on the left side of the subtraction operator.

   sz2: The System.Drawing.SizeF structure on the right side of the subtraction operator.

   Returns: A System.Drawing.SizeF structure that is a result of the subtraction operation.
  """
  pass
 def ToPointF(self):
  """
  ToPointF(self: SizeF) -> PointF

  

   Converts a System.Drawing.SizeF structure to a System.Drawing.PointF structure.

   Returns: Returns a System.Drawing.PointF structure.
  """
  pass
 def ToSize(self):
  """
  ToSize(self: SizeF) -> Size

  

   Converts a System.Drawing.SizeF structure to a System.Drawing.Size structure.

   Returns: Returns a System.Drawing.Size structure.
  """
  pass
 def ToString(self):
  """
  ToString(self: SizeF) -> str

  

   Creates a human-readable string that represents this System.Drawing.SizeF structure.

   Returns: A string that represents this System.Drawing.SizeF structure.
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
  __new__[SizeF]() -> SizeF

  

  __new__(cls: type,size: SizeF)

  __new__(cls: type,pt: PointF)

  __new__(cls: type,width: Single,height: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(sz1: SizeF,sz2: SizeF) -> SizeF

  

   Adds the width and height of one System.Drawing.SizeF structure to the width and height of 

    another System.Drawing.SizeF structure.

  

  

   sz1: The first System.Drawing.SizeF structure to add.

   sz2: The second System.Drawing.SizeF structure to add.

   Returns: A System.Drawing.Size structure that is the result of the addition operation.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(sz1: SizeF,sz2: SizeF) -> SizeF

  

   Subtracts the width and height of one System.Drawing.SizeF structure from the width and height 

    of another System.Drawing.SizeF structure.

  

  

   sz1: The System.Drawing.SizeF structure on the left side of the subtraction operator.

   sz2: The System.Drawing.SizeF structure on the right side of the subtraction operator.

   Returns: A System.Drawing.SizeF that is the result of the subtraction operation.
  """
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the vertical component of this System.Drawing.SizeF structure.



Get: Height(self: SizeF) -> Single



Set: Height(self: SizeF)=value

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Drawing.SizeF structure has zero width and height.



Get: IsEmpty(self: SizeF) -> bool



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the horizontal component of this System.Drawing.SizeF structure.



Get: Width(self: SizeF) -> Single



Set: Width(self: SizeF)=value

"""


 Empty=None

