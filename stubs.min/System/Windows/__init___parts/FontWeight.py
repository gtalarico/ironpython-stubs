class FontWeight(object,IFormattable):
 """ Refers to the density of a typeface,in terms of the lightness or heaviness of the strokes. """
 @staticmethod
 def Compare(left,right):
  """
  Compare(left: FontWeight,right: FontWeight) -> int
  
   Compares two instances of System.Windows.FontWeight.
  
   left: The first System.Windows.FontWeight object to compare.
   right: The second System.Windows.FontWeight object to compare.
   Returns: An System.Int32 value that indicates the relationship between the two instances 
    of System.Windows.FontWeight. When the return value is less than zero,left is 
    less than right. When this value is zero,it indicates that both operands are 
    equal. When the value is greater than zero,it indicates that left is greater 
    than right.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: FontWeight,obj: object) -> bool
  
   Determines whether the current System.Windows.FontWeight object is equal to a 
    specified object.
  
  
   obj: The System.Object to compare for equality.
   Returns: true if the two instances are equal; otherwise,false.
  Equals(self: FontWeight,obj: FontWeight) -> bool
  
   Determines whether the current System.Windows.FontWeight object is equal to a 
    specified System.Windows.FontWeight object.
  
  
   obj: The instance of System.Windows.FontWeight to compare for equality.
   Returns: true if the two instances are equal; otherwise,false.
  """
  pass
 @staticmethod
 def FromOpenTypeWeight(weightValue):
  """
  FromOpenTypeWeight(weightValue: int) -> FontWeight
  
   Creates a new instance of System.Windows.FontWeight that corresponds to the 
    OpenType�usWeightClass value.
  
  
   weightValue: An integer value between 1 and 999 that corresponds to the usWeightClass 
    definition in the OpenType specification.
  
   Returns: A new instance of System.Windows.FontWeight.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FontWeight) -> int
  
   Retrieves the hash code for this object.
   Returns: A 32-bit hash code,which is a signed integer.
  """
  pass
 def ToOpenTypeWeight(self):
  """
  ToOpenTypeWeight(self: FontWeight) -> int
  
   Returns a value that represents the OpenType�usWeightClass for the 
    System.Windows.FontWeight object.
  
   Returns: An integer value between 1 and 999 that corresponds to the usWeightClass 
    definition in the OpenType specification.
  """
  pass
 def ToString(self):
  """
  ToString(self: FontWeight) -> str
  
   Returns a text string that represents the value of the 
    System.Windows.FontWeight object and is based on the 
    System.Globalization.CultureInfo.CurrentCulture property information.
  
   Returns: A System.String that represents the value of the System.Windows.FontWeight 
    object,such as "Light","Normal",or "UltraBold".
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
