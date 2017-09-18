class DataGridViewColumnDesignTimeVisibleAttribute(Attribute,_Attribute):
 """
 Specifies whether a column type is visible in the System.Windows.Forms.DataGridView designer. This class cannot be inherited.

 

 DataGridViewColumnDesignTimeVisibleAttribute(visible: bool)

 DataGridViewColumnDesignTimeVisibleAttribute()
 """
 def Equals(self,obj):
  """
  Equals(self: DataGridViewColumnDesignTimeVisibleAttribute,obj: object) -> bool

  

   Gets a value indicating whether this object is equivalent to the specified object.

  

   obj: The System.Object to compare with the current System.Object.

   Returns: true to indicate that the specified object is a 

    System.Windows.Forms.DataGridViewColumnDesignTimeVisibleAttribute instance with the same 

    System.Windows.Forms.DataGridViewColumnDesignTimeVisibleAttribute.Visible property value as this 

    instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridViewColumnDesignTimeVisibleAttribute) -> int

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DataGridViewColumnDesignTimeVisibleAttribute) -> bool

  

   Gets a value indicating whether this attribute instance is equal to the 

    System.Windows.Forms.DataGridViewColumnDesignTimeVisibleAttribute.Default attribute value.

  

   Returns: true to indicate that this instance is equal to the 

    System.Windows.Forms.DataGridViewColumnDesignTimeVisibleAttribute.Default instance; otherwise,

    false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,visible=None):
  """
  __new__(cls: type,visible: bool)

  __new__(cls: type)
  """
  pass
 def __ne__(self,*args):
  pass
 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the column type is visible in the System.Windows.Forms.DataGridView designer.



Get: Visible(self: DataGridViewColumnDesignTimeVisibleAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

