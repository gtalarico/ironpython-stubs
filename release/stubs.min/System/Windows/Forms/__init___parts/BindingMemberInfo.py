class BindingMemberInfo(object):
 """
 Contains information that enables a System.Windows.Forms.Binding to resolve a data binding to either the property of an object or the property of the current object in a list of objects.

 

 BindingMemberInfo(dataMember: str)
 """
 def Equals(self,otherObject):
  """
  Equals(self: BindingMemberInfo,otherObject: object) -> bool

  

   Determines whether the specified object is equal to this System.Windows.Forms.BindingMemberInfo.

  

   otherObject: The object to compare for equality.

   Returns: true if otherObject is a System.Windows.Forms.BindingMemberInfo and both 

    System.Windows.Forms.BindingMemberInfo.BindingMember strings are equal; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: BindingMemberInfo) -> int

  

   Returns the hash code for this System.Windows.Forms.BindingMemberInfo.

   Returns: The hash code for this System.Windows.Forms.BindingMemberInfo.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,dataMember):
  """
  __new__(cls: type,dataMember: str)

  __new__[BindingMemberInfo]() -> BindingMemberInfo
  """
  pass
 def __ne__(self,*args):
  pass
 BindingField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the property name of the data-bound object.



Get: BindingField(self: BindingMemberInfo) -> str



"""

 BindingMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the information that is used to specify the property name of the data-bound object.



Get: BindingMember(self: BindingMemberInfo) -> str



"""

 BindingPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the property name,or the period-delimited hierarchy of property names,that comes before the property name of the data-bound object.



Get: BindingPath(self: BindingMemberInfo) -> str



"""


