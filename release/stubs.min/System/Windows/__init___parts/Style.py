class Style(DispatcherObject,INameScope,IAddChild,ISealable,IHaveResources,IQueryAmbient):
 """
 Enables the sharing of properties,resources,and event handlers between instances of a type.
 
 Style()
 Style(targetType: Type)
 Style(targetType: Type,basedOn: Style)
 """
 def GetHashCode(self):
  """
  GetHashCode(self: Style) -> int
  
   Returns the hash code for this System.Windows.Style.
   Returns: The hash code for this System.Windows.Style.
  """
  pass
 def RegisterName(self,name,scopedElement):
  """
  RegisterName(self: Style,name: str,scopedElement: object)
   Registers a new name-object pair in the current namescope.
  
   name: The name to register.
   scopedElement: The object to map to the specified name.
  """
  pass
 def Seal(self):
  """
  Seal(self: Style)
   Locks this style and all factories and triggers so they cannot be changed.
  """
  pass
 def UnregisterName(self,name):
  """
  UnregisterName(self: Style,name: str)
   Removes a name-object mapping from the namescope.
  
   name: The name of the mapping to remove.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,targetType=None,basedOn=None):
  """
  __new__(cls: type)
  __new__(cls: type,targetType: Type)
  __new__(cls: type,targetType: Type,basedOn: Style)
  """
  pass
 BasedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a defined style that is the basis of the current style.

Get: BasedOn(self: Style) -> Style

Set: BasedOn(self: Style)=value
"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the style is read-only and cannot be changed.

Get: IsSealed(self: Style) -> bool

"""

 Resources=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of resources that can be used within the scope of this style.

Get: Resources(self: Style) -> ResourceDictionary

Set: Resources(self: Style)=value
"""

 Setters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Setter and System.Windows.EventSetter objects.

Get: Setters(self: Style) -> SetterBaseCollection

"""

 TargetType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type for which this style is intended.

Get: TargetType(self: Style) -> Type

Set: TargetType(self: Style)=value
"""

 Triggers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.TriggerBase objects that apply property values based on specified conditions.

Get: Triggers(self: Style) -> TriggerCollection

"""


