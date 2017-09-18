class InputMethod(DispatcherObject):
 """ Provides facilities for managing and interacting with the Text Services Framework,which provides support for alternate text input methods such as speech and handwriting. """
 @staticmethod
 def GetInputScope(target):
  """
  GetInputScope(target: DependencyObject) -> InputScope
  
   Returns the value of the System.Windows.Input.InputMethod.InputScope �attached 
    property for a specified dependency object.
  
  
   target: The dependency object for which to retrieve the input scope.
   Returns: An System.Windows.Input.InputScope object representing the current input scope 
    for the specified dependency object.
  """
  pass
 @staticmethod
 def GetIsInputMethodEnabled(target):
  """
  GetIsInputMethodEnabled(target: DependencyObject) -> bool
  
   Returns the value of the System.Windows.Input.InputMethod.IsInputMethodEnabled �
    attached property for a specified dependency object.
  
  
   target: The dependency object for which to retrieve the value of 
    System.Windows.Input.InputMethod.IsInputMethodEnabled.
  
   Returns: The current value of System.Windows.Input.InputMethod.IsInputMethodEnabled for 
    the specified dependency object.
  """
  pass
 @staticmethod
 def GetIsInputMethodSuspended(target):
  """
  GetIsInputMethodSuspended(target: DependencyObject) -> bool
  
   Returns the value of the 
    System.Windows.Input.InputMethod.IsInputMethodSuspended �attached property for 
    a specified dependency object.
  
  
   target: The dependency object for which to retrieve the value of 
    System.Windows.Input.InputMethod.IsInputMethodSuspended.
  
   Returns: The current value of System.Windows.Input.InputMethod.IsInputMethodSuspended 
    for the specified dependency object.
  """
  pass
 @staticmethod
 def GetPreferredImeConversionMode(target):
  """
  GetPreferredImeConversionMode(target: DependencyObject) -> ImeConversionModeValues
  
   Returns the value of the 
    System.Windows.Input.InputMethod.PreferredImeConversionMode �attached property 
    for a specified dependency object.
  
  
   target: The dependency object for which to retrieve the value of 
    System.Windows.Input.InputMethod.PreferredImeConversionMode.
  
   Returns: A member of the System.Windows.Input.ImeConversionModeValues enumeration 
    specifying the current 
    System.Windows.Input.InputMethod.PreferredImeConversionMode for the specified 
    dependency object.
  """
  pass
 @staticmethod
 def GetPreferredImeSentenceMode(target):
  """
  GetPreferredImeSentenceMode(target: DependencyObject) -> ImeSentenceModeValues
  
   Returns the value of the 
    System.Windows.Input.InputMethod.PreferredImeSentenceMode �attached property 
    for a specified dependency object.
  
  
   target: The dependency object for which to retrieve the value of 
    System.Windows.Input.InputMethod.PreferredImeSentenceMode.
  
   Returns: A member of the System.Windows.Input.ImeSentenceModeValues enumeration 
    specifying the current 
    System.Windows.Input.InputMethod.PreferredImeSentenceMode for the specified 
    dependency object.
  """
  pass
 @staticmethod
 def GetPreferredImeState(target):
  """
  GetPreferredImeState(target: DependencyObject) -> InputMethodState
  
   Returns the value of the System.Windows.Input.InputMethod.PreferredImeState �
    attached property for a specified dependency object.
  
  
   target: The dependency object for which to retrieve the value of 
    System.Windows.Input.InputMethod.PreferredImeState.
  
   Returns: A member of the System.Windows.Input.InputMethodState enumeration specifying 
    the current System.Windows.Input.InputMethod.PreferredImeState for the 
    specified dependency object.
  """
  pass
 @staticmethod
 def SetInputScope(target,value):
  """
  SetInputScope(target: DependencyObject,value: InputScope)
   Sets the value of the System.Windows.Input.InputMethod.InputScope attached 
    property on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.InputScope attached property.
  
   value: An System.Windows.Input.InputScope object representing the new value for the 
    System.Windows.Input.InputMethod.InputScope attached property.
  """
  pass
 @staticmethod
 def SetIsInputMethodEnabled(target,value):
  """
  SetIsInputMethodEnabled(target: DependencyObject,value: bool)
   Sets the value of the System.Windows.Input.InputMethod.IsInputMethodEnabled 
    attached property on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.IsInputMethodEnabled attached property.
  
   value: The new value for the System.Windows.Input.InputMethod.IsInputMethodEnabled 
    attached property.
  """
  pass
 @staticmethod
 def SetIsInputMethodSuspended(target,value):
  """
  SetIsInputMethodSuspended(target: DependencyObject,value: bool)
   Sets the value of the System.Windows.Input.InputMethod.IsInputMethodSuspended 
    attached property on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.IsInputMethodSuspended attached property.
  
   value: The new value for the System.Windows.Input.InputMethod.IsInputMethodSuspended 
    attached property.
  """
  pass
 @staticmethod
 def SetPreferredImeConversionMode(target,value):
  """
  SetPreferredImeConversionMode(target: DependencyObject,value: ImeConversionModeValues)
   Sets the value of the 
    System.Windows.Input.InputMethod.PreferredImeConversionMode attached property 
    on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.PreferredImeConversionMode attached property.
  
   value: A member of the System.Windows.Input.ImeConversionModeValues enumeration 
    representing the new value for the 
    System.Windows.Input.InputMethod.PreferredImeConversionMode attached property.
  """
  pass
 @staticmethod
 def SetPreferredImeSentenceMode(target,value):
  """
  SetPreferredImeSentenceMode(target: DependencyObject,value: ImeSentenceModeValues)
   Sets the value of the System.Windows.Input.InputMethod.PreferredImeSentenceMode 
    attached property on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.PreferredImeSentenceMode attached property.
  
   value: A member of the System.Windows.Input.ImeConversionModeValues enumeration 
    representing the new value for the 
    System.Windows.Input.InputMethod.PreferredImeSentenceMode attached property.
  """
  pass
 @staticmethod
 def SetPreferredImeState(target,value):
  """
  SetPreferredImeState(target: DependencyObject,value: InputMethodState)
   Sets the value of the System.Windows.Input.InputMethod.PreferredImeState 
    attached property on the specified dependency object.
  
  
   target: The dependency object on which to set the 
    System.Windows.Input.InputMethod.PreferredImeState attached property.
  
   value: A member of the System.Windows.Input.ImeConversionModeValues enumeration 
    representing the new value for the 
    System.Windows.Input.InputMethod.PreferredImeState attached property.
  """
  pass
 def ShowConfigureUI(self,element=None):
  """
  ShowConfigureUI(self: InputMethod,element: UIElement)
   Displays configuration user interface (UI) associated with the currently active 
    keyboard text service,using a specified System.Windows.UIElement as the parent 
    element for the configuration UI.
  
  
   element: A System.Windows.UIElement that will be used as the parent element for the 
    configuration UI.  This parameter can be null.
  
  ShowConfigureUI(self: InputMethod)
   Displays configuration user interface (UI) associated with the currently active 
    keyboard text service.
  """
  pass
 def ShowRegisterWordUI(self,*__args):
  """
  ShowRegisterWordUI(self: InputMethod,element: UIElement,registeredText: str)
   Displays word registration user interface (UI) associated with the currently 
    active keyboard text service.  Accepts a specified string as the default value 
    to register,and a specified System.Windows.UIElement as the parent element for 
    the configuration UI.
  
  
   element: A System.Windows.UIElement that will be used as the parent element for the word 
    registration UI.  This parameter can be null.
  
   registeredText: A string that specifies a value to register.
  ShowRegisterWordUI(self: InputMethod,registeredText: str)
   Displays word registration user interface (UI) associated with the currently 
    active keyboard text service.  Accepts a specified string as the default value 
    to register.
  
  
   registeredText: A string that specifies a value to register.
  ShowRegisterWordUI(self: InputMethod)
   Displays word registration user interface (UI) associated with the currently 
    active keyboard text service.
  """
  pass
 CanShowConfigurationUI=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether or not this input method can display configuration user interface (UI).

Get: CanShowConfigurationUI(self: InputMethod) -> bool

"""

 CanShowRegisterWordUI=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this input method can display word registration user interface (UI).

Get: CanShowRegisterWordUI(self: InputMethod) -> bool

"""

 HandwritingState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current state of handwriting input for this input method.

Get: HandwritingState(self: InputMethod) -> InputMethodState

Set: HandwritingState(self: InputMethod)=value
"""

 ImeConversionMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current conversion mode for the input method editor associated with this input method.

Get: ImeConversionMode(self: InputMethod) -> ImeConversionModeValues

Set: ImeConversionMode(self: InputMethod)=value
"""

 ImeSentenceMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current sentence mode for the input method editor associated with this input method.

Get: ImeSentenceMode(self: InputMethod) -> ImeSentenceModeValues

Set: ImeSentenceMode(self: InputMethod)=value
"""

 ImeState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current state of the input method editor associated with this input method.

Get: ImeState(self: InputMethod) -> InputMethodState

Set: ImeState(self: InputMethod)=value
"""

 MicrophoneState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current state of microphone input for this input method.

Get: MicrophoneState(self: InputMethod) -> InputMethodState

Set: MicrophoneState(self: InputMethod)=value
"""

 SpeechMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the speech mode for this input method.

Get: SpeechMode(self: InputMethod) -> SpeechMode

Set: SpeechMode(self: InputMethod)=value
"""


 Current=None
 InputScopeProperty=None
 IsInputMethodEnabledProperty=None
 IsInputMethodSuspendedProperty=None
 PreferredImeConversionModeProperty=None
 PreferredImeSentenceModeProperty=None
 PreferredImeStateProperty=None
 StateChanged=None

