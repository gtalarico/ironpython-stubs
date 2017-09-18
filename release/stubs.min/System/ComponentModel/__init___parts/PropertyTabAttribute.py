class PropertyTabAttribute(Attribute,_Attribute):
 """
 Identifies the property tab or tabs to display for the specified class or classes.

 

 PropertyTabAttribute()

 PropertyTabAttribute(tabClass: Type)

 PropertyTabAttribute(tabClassName: str)

 PropertyTabAttribute(tabClass: Type,tabScope: PropertyTabScope)

 PropertyTabAttribute(tabClassName: str,tabScope: PropertyTabScope)
 """
 def Equals(self,other):
  """
  Equals(self: PropertyTabAttribute,other: PropertyTabAttribute) -> bool

  

   Returns a value indicating whether this instance is equal to a specified attribute.

  

   other: A System.ComponentModel.PropertyTabAttribute to compare to this instance,or null.

   Returns: true if the System.ComponentModel.PropertyTabAttribute instances are equal; otherwise,false.

  Equals(self: PropertyTabAttribute,other: object) -> bool

  

   Returns a value indicating whether this instance is equal to a specified object.

  

   other: An object to compare to this instance,or null.

   Returns: true if other refers to the same System.ComponentModel.PropertyTabAttribute instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PropertyTabAttribute) -> int

  

   Gets the hash code for this object.

   Returns: The hash code for the object the attribute belongs to.
  """
  pass
 def InitializeArrays(self,*args):
  """
  InitializeArrays(self: PropertyTabAttribute,tabClasses: Array[Type],tabScopes: Array[PropertyTabScope])

   Initializes the attribute using the specified names of tab classes and array of tab scopes.

  

   tabClasses: The types of tabs to create.

   tabScopes: The scope of each tab. If the scope is System.ComponentModel.PropertyTabScope.Component,it is 

    shown only for components with the corresponding System.ComponentModel.PropertyTabAttribute. If 

    it is System.ComponentModel.PropertyTabScope.Document,it is shown for all components on the 

    document.

  

  InitializeArrays(self: PropertyTabAttribute,tabClassNames: Array[str],tabScopes: Array[PropertyTabScope])

   Initializes the attribute using the specified names of tab classes and array of tab scopes.

  

   tabClassNames: An array of fully qualified type names of the types to create for tabs on the Properties window.

   tabScopes: The scope of each tab. If the scope is System.ComponentModel.PropertyTabScope.Component,it is 

    shown only for components with the corresponding System.ComponentModel.PropertyTabAttribute. If 

    it is System.ComponentModel.PropertyTabScope.Document,it is shown for all components on the 

    document.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,tabClass: Type)

  __new__(cls: type,tabClassName: str)

  __new__(cls: type,tabClass: Type,tabScope: PropertyTabScope)

  __new__(cls: type,tabClassName: str,tabScope: PropertyTabScope)
  """
  pass
 def __ne__(self,*args):
  pass
 TabClasses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the types of tabs that this attribute uses.



Get: TabClasses(self: PropertyTabAttribute) -> Array[Type]



"""

 TabClassNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the names of the tab classes that this attribute uses.



"""

 TabScopes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of tab scopes of each tab of this System.ComponentModel.PropertyTabAttribute.



Get: TabScopes(self: PropertyTabAttribute) -> Array[PropertyTabScope]



"""


