class MemberDescriptor(object):
 """ Represents a class member,such as a property or event. This is an abstract base class. """
 def CreateAttributeCollection(self,*args):
  """
  CreateAttributeCollection(self: MemberDescriptor) -> AttributeCollection

  

   Creates a collection of attributes using the array of attributes passed to the constructor.

   Returns: A new System.ComponentModel.AttributeCollection that contains the 

    System.ComponentModel.MemberDescriptor.AttributeArray attributes.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: MemberDescriptor,obj: object) -> bool

  

   Compares this instance to the given object to see if they are equivalent.

  

   obj: The object to compare to the current instance.

   Returns: true if equivalent; otherwise,false.
  """
  pass
 def FillAttributes(self,*args):
  """
  FillAttributes(self: MemberDescriptor,attributeList: IList)

   When overridden in a derived class,adds the attributes of the inheriting class to the specified 

    list of attributes in the parent class.

  

  

   attributeList: An System.Collections.IList that lists the attributes in the parent class. Initially,this is 

    empty.
  """
  pass
 def FindMethod(self,*args):
  """
  FindMethod(componentClass: Type,name: str,args: Array[Type],returnType: Type,publicOnly: bool) -> MethodInfo

  

   Finds the given method through reflection,with an option to search only public methods.

  

   componentClass: The component that contains the method.

   name: The name of the method to find.

   args: An array of parameters for the method,used to choose between overloaded methods.

   returnType: The type to return for the method.

   publicOnly: Whether to restrict search to public methods.

   Returns: A System.Reflection.MethodInfo that represents the method,or null if the method is not found.

  FindMethod(componentClass: Type,name: str,args: Array[Type],returnType: Type) -> MethodInfo

  

   Finds the given method through reflection,searching only for public methods.

  

   componentClass: The component that contains the method.

   name: The name of the method to find.

   args: An array of parameters for the method,used to choose between overloaded methods.

   returnType: The type to return for the method.

   Returns: A System.Reflection.MethodInfo that represents the method,or null if the method is not found.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MemberDescriptor) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.MemberDescriptor.
  """
  pass
 def GetInvocationTarget(self,*args):
  """
  GetInvocationTarget(self: MemberDescriptor,type: Type,instance: object) -> object

  

   Retrieves the object that should be used during invocation of members.

  

   type: The System.Type of the invocation target.

   instance: The potential invocation target.

   Returns: The object to be used during member invocations.
  """
  pass
 def GetInvokee(self,*args):
  """
  GetInvokee(componentClass: Type,component: object) -> object

  

   Gets the component on which to invoke a method.

  

   componentClass: A System.Type representing the type of component this System.ComponentModel.MemberDescriptor is 

    bound to. For example,if this System.ComponentModel.MemberDescriptor describes a property,this 

    parameter should be the class that the property is declared on.

  

   component: An instance of the object to call.

   Returns: An instance of the component to invoke. This method returns a visual designer when the property 

    is attached to a visual designer.
  """
  pass
 def GetSite(self,*args):
  """
  GetSite(component: object) -> ISite

  

   Gets a component site for the given component.

  

   component: The component for which you want to find a site.

   Returns: The site of the component,or null if a site does not exist.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,name: str)

  __new__(cls: type,name: str,attributes: Array[Attribute])

  __new__(cls: type,descr: MemberDescriptor)

  __new__(cls: type,oldMemberDescriptor: MemberDescriptor,newAttributes: Array[Attribute])
  """
  pass
 def __ne__(self,*args):
  pass
 AttributeArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of attributes.



"""

 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of attributes for this member.



Get: Attributes(self: MemberDescriptor) -> AttributeCollection



"""

 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the category to which the member belongs,as specified in the System.ComponentModel.CategoryAttribute.



Get: Category(self: MemberDescriptor) -> str



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description of the member,as specified in the System.ComponentModel.DescriptionAttribute.



Get: Description(self: MemberDescriptor) -> str



"""

 DesignTimeOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether this member should be set only at design time,as specified in the System.ComponentModel.DesignOnlyAttribute.



Get: DesignTimeOnly(self: MemberDescriptor) -> bool



"""

 DisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name that can be displayed in a window,such as a Properties window.



Get: DisplayName(self: MemberDescriptor) -> str



"""

 IsBrowsable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the member is browsable,as specified in the System.ComponentModel.BrowsableAttribute.



Get: IsBrowsable(self: MemberDescriptor) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the member.



Get: Name(self: MemberDescriptor) -> str



"""

 NameHashCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hash code for the name of the member,as specified in System.String.GetHashCode.



"""


