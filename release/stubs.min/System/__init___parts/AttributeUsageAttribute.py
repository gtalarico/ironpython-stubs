class AttributeUsageAttribute(Attribute,_Attribute):
 """
 Specifies the usage of another attribute class. This class cannot be inherited.

 

 AttributeUsageAttribute(validOn: AttributeTargets)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,validOn):
  """ __new__(cls: type,validOn: AttributeTargets) """
  pass
 def __reduce_ex__(self,*args):
  pass
 AllowMultiple=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value indicating whether more than one instance of the indicated attribute can be specified for a single program element.



Get: AllowMultiple(self: AttributeUsageAttribute) -> bool



Set: AllowMultiple(self: AttributeUsageAttribute)=value

"""

 Inherited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value indicating whether the indicated attribute can be inherited by derived classes and overriding members.



Get: Inherited(self: AttributeUsageAttribute) -> bool



Set: Inherited(self: AttributeUsageAttribute)=value

"""

 ValidOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a set of values identifying which program elements that the indicated attribute can be applied to.



Get: ValidOn(self: AttributeUsageAttribute) -> AttributeTargets



"""


