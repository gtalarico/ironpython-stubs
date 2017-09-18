class PageRange(object):
 """
 Specifies a range of pages.

 

 PageRange(page: int)

 PageRange(pageFrom: int,pageTo: int)
 """
 def Equals(self,*__args):
  """
  Equals(self: PageRange,pageRange: PageRange) -> bool

  

   Tests whether a System.Windows.Controls.PageRange is equal to this 

    System.Windows.Controls.PageRange.

  

  

   pageRange: The System.Windows.Controls.PageRange tested.

   Returns: true if the two System.Windows.Controls.PageRange objects are equal; otherwise,false.

  Equals(self: PageRange,obj: object) -> bool

  

   Tests whether an object of unknown type is equal to this System.Windows.Controls.PageRange.

  

   obj: The object tested.

   Returns: true if the object is of type System.Windows.Controls.PageRange and is equal to this 

    System.Windows.Controls.PageRange; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PageRange) -> int

  

   Gets the hash code value for the System.Windows.Controls.PageRange.

   Returns: The hash code value for the System.Windows.Controls.PageRange.
  """
  pass
 def ToString(self):
  """
  ToString(self: PageRange) -> str

  

   Gets a string representation of the range.

   Returns: A string that represents the range of pages in the format 

    "System.Windows.Controls.PageRange.PageFrom-System.Windows.Controls.PageRange.PageTo".
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,page: int)

  __new__(cls: type,pageFrom: int,pageTo: int)

  __new__[PageRange]() -> PageRange
  """
  pass
 def __ne__(self,*args):
  pass
 PageFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the page number of the first page in the range.



Get: PageFrom(self: PageRange) -> int



Set: PageFrom(self: PageRange)=value

"""

 PageTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the page number of the last page in the range.



Get: PageTo(self: PageRange) -> int



Set: PageTo(self: PageRange)=value

"""


