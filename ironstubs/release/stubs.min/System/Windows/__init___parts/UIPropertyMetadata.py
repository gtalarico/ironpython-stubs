class UIPropertyMetadata(PropertyMetadata):
 """
 Provides property metadata for non-framework properties that do have rendering/user interface impact at the core level.
 
 UIPropertyMetadata()
 UIPropertyMetadata(defaultValue: object)
 UIPropertyMetadata(propertyChangedCallback: PropertyChangedCallback)
 UIPropertyMetadata(defaultValue: object,propertyChangedCallback: PropertyChangedCallback)
 UIPropertyMetadata(defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback)
 UIPropertyMetadata(defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback,isAnimationProhibited: bool)
 """
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,defaultValue: object)
  __new__(cls: type,propertyChangedCallback: PropertyChangedCallback)
  __new__(cls: type,defaultValue: object,propertyChangedCallback: PropertyChangedCallback)
  __new__(cls: type,defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback)
  __new__(cls: type,defaultValue: object,propertyChangedCallback: PropertyChangedCallback,coerceValueCallback: CoerceValueCallback,isAnimationProhibited: bool)
  """
  pass
 IsAnimationProhibited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value declaring whether animations should be disabled on the dependency property where the containing metadata instance is applied.

Get: IsAnimationProhibited(self: UIPropertyMetadata) -> bool

Set: IsAnimationProhibited(self: UIPropertyMetadata)=value
"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether the metadata has been applied to a property in some way,resulting in the immutable state of that metadata instance.

"""


