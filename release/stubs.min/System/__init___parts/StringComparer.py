class StringComparer(object,IComparer,IEqualityComparer,IComparer[str],IEqualityComparer[str]):
 """ Represents a string comparison operation that uses specific case and culture-based or ordinal comparison rules. """
 def Compare(self,x,y):
  """
  Compare(self: StringComparer,x: str,y: str) -> int

  

   When overridden in a derived class,compares two strings and returns an indication of their 

    relative sort order.

  

  

   x: A string to compare to y.

   y: A string to compare to x.

   Returns: A signed integer that indicates the relative values of x and y,as shown in the following 

    table.ValueMeaningLess than zerox is less than y.-or-x is null.Zerox is equal to y.Greater than 

    zerox is greater than y.-or-y is null.

  

  Compare(self: StringComparer,x: object,y: object) -> int

  

   When overridden in a derived class,compares two objects and returns an indication of their 

    relative sort order.

  

  

   x: An object to compare to y.

   y: An object to compare to x.

   Returns: A signed integer that indicates the relative values of x and y,as shown in the following 

    table.ValueMeaningLess than zerox is less than y. -or-x is null.Zerox is equal to y.Greater than 

    zerox is greater than y.-or-y is null.
  """
  pass
 @staticmethod
 def Create(culture,ignoreCase):
  """
  Create(culture: CultureInfo,ignoreCase: bool) -> StringComparer

  

   Creates a System.StringComparer object that compares strings according to the rules of a 

    specified culture.

  

  

   culture: A culture whose linguistic rules are used to perform a string comparison.

   ignoreCase: true to specify that comparison operations be case-insensitive; false to specify that comparison 

    operations be case-sensitive.

  

   Returns: A new System.StringComparer object that performs string comparisons according to the comparison 

    rules used by the culture parameter and the case rule specified by the ignoreCase parameter.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: StringComparer,x: str,y: str) -> bool

  

   When overridden in a derived class,indicates whether two strings are equal.

  

   x: A string to compare to y.

   y: A string to compare to x.

   Returns: true if x and y refer to the same object,or x and y are equal; otherwise,false.

  Equals(self: StringComparer,x: object,y: object) -> bool

  

   When overridden in a derived class,indicates whether two objects are equal.

  

   x: An object to compare to y.

   y: An object to compare to x.

   Returns: true if x and y refer to the same object,or x and y are both the same type of object and those 

    objects are equal; otherwise,false.
  """
  pass
 def GetHashCode(self,obj=None):
  """
  GetHashCode(self: StringComparer,obj: str) -> int

  

   When overridden in a derived class,gets the hash code for the specified string.

  

   obj: A string.

   Returns: A 32-bit signed hash code calculated from the value of the obj parameter.

  GetHashCode(self: StringComparer,obj: object) -> int

  

   When overridden in a derived class,gets the hash code for the specified object.

  

   obj: An object.

   Returns: A 32-bit signed hash code calculated from the value of the obj parameter.
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CurrentCulture=None
 CurrentCultureIgnoreCase=None
 InvariantCulture=None
 InvariantCultureIgnoreCase=None
 Ordinal=None
 OrdinalIgnoreCase=None

