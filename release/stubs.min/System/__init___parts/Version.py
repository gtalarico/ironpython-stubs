class Version(object,ICloneable,IComparable,IComparable[Version],IEquatable[Version]):
 """
 Represents the version number of an assembly,operating system,or the common language runtime. This class cannot be inherited.

 

 Version(major: int,minor: int,build: int,revision: int)

 Version(major: int,minor: int,build: int)

 Version(major: int,minor: int)

 Version(version: str)

 Version()
 """
 def Clone(self):
  """
  Clone(self: Version) -> object

  

   Returns a new System.Version object whose value is the same as the current System.Version object.

   Returns: A new System.Object whose values are a copy of the current System.Version object.
  """
  pass
 def CompareTo(self,*__args):
  """
  CompareTo(self: Version,value: Version) -> int

  

   Compares the current System.Version object to a specified System.Version object and returns an 

    indication of their relative values.

  

  

   value: A System.Version object to compare to the current System.Version object,or null.

   Returns: A signed integer that indicates the relative values of the two objects,as shown in the 

    following table.Return value Meaning Less than zero The current System.Version object is a 

    version before value. Zero The current System.Version object is the same version as value. 

    Greater than zero The current System.Version object is a version subsequent to value. -or-value 

    is null.

  

  CompareTo(self: Version,version: object) -> int

  

   Compares the current System.Version object to a specified object and returns an indication of 

    their relative values.

  

  

   version: An object to compare,or null.

   Returns: A signed integer that indicates the relative values of the two objects,as shown in the 

    following table.Return value Meaning Less than zero The current System.Version object is a 

    version before version. Zero The current System.Version object is the same version as version. 

    Greater than zero The current System.Version object is a version subsequent to version.-or- 

    version is null.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Version,obj: Version) -> bool

  

   Returns a value indicating whether the current System.Version object and a specified 

    System.Version object represent the same value.

  

  

   obj: A System.Version object to compare to the current System.Version object,or null.

   Returns: true if every component of the current System.Version object matches the corresponding component 

    of the obj parameter; otherwise,false.

  

  Equals(self: Version,obj: object) -> bool

  

   Returns a value indicating whether the current System.Version object is equal to a specified 

    object.

  

  

   obj: An object to compare with the current System.Version object,or null.

   Returns: true if the current System.Version object and obj are both System.Version objects,and every 

    component of the current System.Version object matches the corresponding component of obj; 

    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Version) -> int

  

   Returns a hash code for the current System.Version object.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def Parse(input):
  """
  Parse(input: str) -> Version

  

   Converts the string representation of a version number to an equivalent System.Version object.

  

   input: A string that contains a version number to convert.

   Returns: An object that is equivalent to the version number specified in the input parameter.
  """
  pass
 def ToString(self,fieldCount=None):
  """
  ToString(self: Version,fieldCount: int) -> str

  

   Converts the value of the current System.Version object to its equivalent System.String 

    representation. A specified count indicates the number of components to return.

  

  

   fieldCount: The number of components to return. The fieldCount ranges from 0 to 4.

   Returns: The System.String representation of the values of the major,minor,build,and revision 

    components of the current System.Version object,each separated by a period character ('.'). The 

    fieldCount parameter determines how many components are returned.fieldCount Return Value 0 An 

    empty string (""). 1 major 2 major.minor 3 major.minor.build 4 major.minor.build.revision For 

    example,if you create System.Version object using the constructor Version(1,3,5),ToString(2) 

    returns "1.3" and ToString(4) throws an exception.

  

  ToString(self: Version) -> str

  

   Converts the value of the current System.Version object to its equivalent System.String 

    representation.

  

   Returns: The System.String representation of the values of the major,minor,build,and revision 

    components of the current System.Version object,as depicted in the following format. Each 

    component is separated by a period character ('.'). Square brackets ('[' and ']') indicate a 

    component that will not appear in the return value if the component is not defined: 

    major.minor[.build[.revision]] For example,if you create a System.Version object using the 

    constructor Version(1,1),the returned string is "1.1". If you create a System.Version object 

    using the constructor Version(1,3,4,2),the returned string is "1.3.4.2".
  """
  pass
 @staticmethod
 def TryParse(input,result):
  """
  TryParse(input: str) -> (bool,Version)

  

   Tries to convert the string representation of a version number to an equivalent System.Version 

    object,and returns a value that indicates whether the conversion succeeded.

  

  

   input: A string that contains a version number to convert.

   Returns: true if the input parameter was converted successfully; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,major: int,minor: int,build: int,revision: int)

  __new__(cls: type,major: int,minor: int,build: int)

  __new__(cls: type,major: int,minor: int)

  __new__(cls: type,version: str)

  __new__(cls: type)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Build=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the build component of the version number for the current System.Version object.



Get: Build(self: Version) -> int



"""

 Major=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the major component of the version number for the current System.Version object.



Get: Major(self: Version) -> int



"""

 MajorRevision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the high 16 bits of the revision number.



Get: MajorRevision(self: Version) -> Int16



"""

 Minor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the minor component of the version number for the current System.Version object.



Get: Minor(self: Version) -> int



"""

 MinorRevision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the low 16 bits of the revision number.



Get: MinorRevision(self: Version) -> Int16



"""

 Revision=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the revision component of the version number for the current System.Version object.



Get: Revision(self: Version) -> int



"""


