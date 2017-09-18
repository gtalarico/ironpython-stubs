class PropertyMetadata(object):
 """
 Defines certain behavior aspects of a dependency property as it is applied to a specific type,including conditions it was registered with.
 
 PropertyMetadata()
 PropertyMetadata(defaultValue: object)
 PropertyMetadata(propertyChangedCallback: PropertyChangedCallback)
 PropertyMetadata(defaultValue: object,propertyChangedCallback: PropertyChangedCallback)
 PropertyMetadata(defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback)
 """
 def Merge(self,*args):
  """
  Merge(self: PropertyMetadata,baseMetadata: PropertyMetadata,dp: DependencyProperty)
   Merges this metadata with the base metadata.
  
   baseMetadata: The base metadata to merge with this instance's values.
   dp: The dependency property to which this metadata is being applied.
  """
  pass
 def OnApply(self,*args):
  """
  OnApply(self: PropertyMetadata,dp: DependencyProperty,targetType: Type)
   Called when this metadata has been applied to a property,which indicates that 
    the metadata is being sealed.
  
  
   dp: The dependency property to which the metadata has been applied.
   targetType: The type associated with this metadata if this is type-specific metadata. If 
    this is default metadata,this value is a null reference.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,defaultValue: object)
  __new__(cls: type,propertyChangedCallback: PropertyChangedCallback)
  __new__(cls: type,defaultValue: object,propertyChangedCallback: PropertyChangedCallback)
  __new__(cls: type,defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback)
  """
  pass
 CoerceValueCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.CoerceValueCallback implementation specified in this metadata.

Get: CoerceValueCallback(self: PropertyMetadata) -> CoerceValueCallback

Set: CoerceValueCallback(self: PropertyMetadata)=value
"""

 DefaultValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default value of the dependency property.

Get: DefaultValue(self: PropertyMetadata) -> object

Set: DefaultValue(self: PropertyMetadata)=value
"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether the metadata has been applied to a property in some way,resulting in the immutable state of that metadata instance.

"""

 PropertyChangedCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.PropertyChangedCallback implementation specified in this metadata.

Get: PropertyChangedCallback(self: PropertyMetadata) -> PropertyChangedCallback

Set: PropertyChangedCallback(self: PropertyMetadata)=value
"""


