class EventTrigger(TriggerBase,IAddChild):
 """
 Represents a trigger that applies a set of actions in response to an event.
 
 EventTrigger()
 EventTrigger(routedEvent: RoutedEvent)
 """
 def AddChild(self,*args):
  """
  AddChild(self: EventTrigger,value: object)
   Adds the specified object to the System.Windows.EventTrigger.Actions collection 
    of the current event trigger.
  
  
   value: A System.Windows.TriggerAction object to add to the 
    System.Windows.EventTrigger.Actions collection of this trigger.
  """
  pass
 def AddText(self,*args):
  """
  AddText(self: EventTrigger,text: str)
   This method is not supported and results in an exception.
  
   text: This parameter is not used.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.DependencyObject has been updated. The specific dependency 
    property that changed is reported in the event data.
  
  
   e: Event data that will contain the dependency property identifier of interest,
    the property metadata for the type,and old and new values.
  
  OnPropertyChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def ShouldSerializeActions(self):
  """
  ShouldSerializeActions(self: EventTrigger) -> bool
  
   Returns whether serialization processes should serialize the effective value of 
    the System.Windows.EventTrigger.Actions property on instances of this class.
  
   Returns: Returns true if the System.Windows.EventTrigger.Actions property value should 
    be serialized; otherwise,false.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,routedEvent=None):
  """
  __new__(cls: type)
  __new__(cls: type,routedEvent: RoutedEvent)
  """
  pass
 Actions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of actions to apply when the event occurs.

Get: Actions(self: EventTrigger) -> TriggerActionCollection

"""

 RoutedEvent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.RoutedEvent that will activate this trigger.

Get: RoutedEvent(self: EventTrigger) -> RoutedEvent

Set: RoutedEvent(self: EventTrigger)=value
"""

 SourceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the object with the event that activates this trigger. This is only used by element triggers or template triggers.

Get: SourceName(self: EventTrigger) -> str

Set: SourceName(self: EventTrigger)=value
"""


