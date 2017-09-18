class CategoryAttribute(Attribute,_Attribute):
 """
 Specifies the name of the category in which to group the property or event when displayed in a System.Windows.Forms.PropertyGrid control set to Categorized mode.

 

 CategoryAttribute()

 CategoryAttribute(category: str)
 """
 def Equals(self,obj):
  """
  Equals(self: CategoryAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.CategoryAttribute..

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CategoryAttribute) -> int

  

   Returns the hash code for this attribute.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetLocalizedString(self,*args):
  """
  GetLocalizedString(self: CategoryAttribute,value: str) -> str

  

   Looks up the localized name of the specified category.

  

   value: The identifer for the category to look up.

   Returns: The localized name of the category,or null if a localized name does not exist.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: CategoryAttribute) -> bool

  

   Determines if this attribute is the default.

   Returns: true if the attribute is the default value for this attribute class; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,category=None):
  """
  __new__(cls: type)

  __new__(cls: type,category: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the category for the property or event that this attribute is applied to.



Get: Category(self: CategoryAttribute) -> str



"""


 Action=None
 Appearance=None
 Asynchronous=None
 Behavior=None
 Data=None
 Default=None
 Design=None
 DragDrop=None
 Focus=None
 Format=None
 Key=None
 Layout=None
 Mouse=None
 WindowStyle=None

