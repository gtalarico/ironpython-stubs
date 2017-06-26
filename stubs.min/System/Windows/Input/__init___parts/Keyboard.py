class Keyboard(object):
 """ Represents the keyboard device. """
 @staticmethod
 def AddGotKeyboardFocusHandler(element,handler):
  """
  AddGotKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.GotKeyboardFocus�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddKeyboardInputProviderAcquireFocusHandler(element,handler):
  """
  AddKeyboardInputProviderAcquireFocusHandler(element: DependencyObject,handler: KeyboardInputProviderAcquireFocusEventHandler)
   Adds a handler for the 
    System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus�attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddKeyDownHandler(element,handler):
  """
  AddKeyDownHandler(element: DependencyObject,handler: KeyEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.KeyDown�attached event.
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddKeyUpHandler(element,handler):
  """
  AddKeyUpHandler(element: DependencyObject,handler: KeyEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.KeyUp�attached event.
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddLostKeyboardFocusHandler(element,handler):
  """
  AddLostKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.LostKeyboardFocus�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddPreviewGotKeyboardFocusHandler(element,handler):
  """
  AddPreviewGotKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
    attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddPreviewKeyboardInputProviderAcquireFocusHandler(element,handler):
  """
  AddPreviewKeyboardInputProviderAcquireFocusHandler(element: DependencyObject,handler: KeyboardInputProviderAcquireFocusEventHandler)
   Adds a handler for the 
    System.Windows.Input.Keyboard.PreviewKeyboardInputProviderAcquireFocus�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddPreviewKeyDownHandler(element,handler):
  """
  AddPreviewKeyDownHandler(element: DependencyObject,handler: KeyEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddPreviewKeyUpHandler(element,handler):
  """
  AddPreviewKeyUpHandler(element: DependencyObject,handler: KeyEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.PreviewKeyUp�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def AddPreviewLostKeyboardFocusHandler(element,handler):
  """
  AddPreviewLostKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Adds a handler for the System.Windows.Input.Keyboard.PreviewLostKeyboardFocus�
    attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be added.
  """
  pass
 @staticmethod
 def ClearFocus():
  """
  ClearFocus()
   Clears focus.
  """
  pass
 @staticmethod
 def Focus(element):
  """
  Focus(element: IInputElement) -> IInputElement
  
   Sets keyboard focus on the specified element.
  
   element: The element on which to set keyboard focus.
   Returns: The element with keyboard focus.
  """
  pass
 @staticmethod
 def GetKeyStates(key):
  """
  GetKeyStates(key: Key) -> KeyStates
  
   Gets the set of key states for the specified key.
  
   key: The specified key.
   Returns: A bitwise combination of the System.Windows.Input.KeyStates values.
  """
  pass
 @staticmethod
 def IsKeyDown(key):
  """
  IsKeyDown(key: Key) -> bool
  
   Determines whether the specified key is pressed.
  
   key: The specified key.
   Returns: true if key is in the down state; otherwise,false.
  """
  pass
 @staticmethod
 def IsKeyToggled(key):
  """
  IsKeyToggled(key: Key) -> bool
  
   Determines whether the specified key is toggled.
  
   key: The specified key.
   Returns: true if key is in the toggled state; otherwise,false.
  """
  pass
 @staticmethod
 def IsKeyUp(key):
  """
  IsKeyUp(key: Key) -> bool
  
   Determines whether the specified key is released.
  
   key: The key to check.
   Returns: true if key is in the up state; otherwise,false.
  """
  pass
 @staticmethod
 def RemoveGotKeyboardFocusHandler(element,handler):
  """
  RemoveGotKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.GotKeyboardFocus�
    attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemoveKeyboardInputProviderAcquireFocusHandler(element,handler):
  """
  RemoveKeyboardInputProviderAcquireFocusHandler(element: DependencyObject,handler: KeyboardInputProviderAcquireFocusEventHandler)
   Removes a handler for the 
    System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus�attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemoveKeyDownHandler(element,handler):
  """
  RemoveKeyDownHandler(element: DependencyObject,handler: KeyEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.KeyDown�attached event.
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemoveKeyUpHandler(element,handler):
  """
  RemoveKeyUpHandler(element: DependencyObject,handler: KeyEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.KeyUp�attached event.
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemoveLostKeyboardFocusHandler(element,handler):
  """
  RemoveLostKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.LostKeyboardFocus�
    attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemovePreviewGotKeyboardFocusHandler(element,handler):
  """
  RemovePreviewGotKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
    attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemovePreviewKeyboardInputProviderAcquireFocusHandler(element,handler):
  """
  RemovePreviewKeyboardInputProviderAcquireFocusHandler(element: DependencyObject,handler: KeyboardInputProviderAcquireFocusEventHandler)
   Removes a handler for the 
    System.Windows.Input.Keyboard.PreviewKeyboardInputProviderAcquireFocus�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemovePreviewKeyDownHandler(element,handler):
  """
  RemovePreviewKeyDownHandler(element: DependencyObject,handler: KeyEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemovePreviewKeyUpHandler(element,handler):
  """
  RemovePreviewKeyUpHandler(element: DependencyObject,handler: KeyEventHandler)
   Removes a handler for the System.Windows.Input.Keyboard.PreviewKeyUp�attached 
    event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 @staticmethod
 def RemovePreviewLostKeyboardFocusHandler(element,handler):
  """
  RemovePreviewLostKeyboardFocusHandler(element: DependencyObject,handler: KeyboardFocusChangedEventHandler)
   Removes a handler for the 
    System.Windows.Input.Keyboard.PreviewLostKeyboardFocus�attached event.
  
  
   element: The System.Windows.UIElement or System.Windows.ContentElement that listens to 
    this event.
  
   handler: The event handler to be removed.
  """
  pass
 DefaultRestoreFocusMode=None
 FocusedElement=None
 GotKeyboardFocusEvent=None
 KeyboardInputProviderAcquireFocusEvent=None
 KeyDownEvent=None
 KeyUpEvent=None
 LostKeyboardFocusEvent=None
 Modifiers=None
 PreviewGotKeyboardFocusEvent=None
 PreviewKeyboardInputProviderAcquireFocusEvent=None
 PreviewKeyDownEvent=None
 PreviewKeyUpEvent=None
 PreviewLostKeyboardFocusEvent=None
 PrimaryDevice=None
 __all__=[
  'AddGotKeyboardFocusHandler',
  'AddKeyboardInputProviderAcquireFocusHandler',
  'AddKeyDownHandler',
  'AddKeyUpHandler',
  'AddLostKeyboardFocusHandler',
  'AddPreviewGotKeyboardFocusHandler',
  'AddPreviewKeyboardInputProviderAcquireFocusHandler',
  'AddPreviewKeyDownHandler',
  'AddPreviewKeyUpHandler',
  'AddPreviewLostKeyboardFocusHandler',
  'ClearFocus',
  'Focus',
  'GetKeyStates',
  'GotKeyboardFocusEvent',
  'IsKeyDown',
  'IsKeyToggled',
  'IsKeyUp',
  'KeyboardInputProviderAcquireFocusEvent',
  'KeyDownEvent',
  'KeyUpEvent',
  'LostKeyboardFocusEvent',
  'PreviewGotKeyboardFocusEvent',
  'PreviewKeyboardInputProviderAcquireFocusEvent',
  'PreviewKeyDownEvent',
  'PreviewKeyUpEvent',
  'PreviewLostKeyboardFocusEvent',
  'RemoveGotKeyboardFocusHandler',
  'RemoveKeyboardInputProviderAcquireFocusHandler',
  'RemoveKeyDownHandler',
  'RemoveKeyUpHandler',
  'RemoveLostKeyboardFocusHandler',
  'RemovePreviewGotKeyboardFocusHandler',
  'RemovePreviewKeyboardInputProviderAcquireFocusHandler',
  'RemovePreviewKeyDownHandler',
  'RemovePreviewKeyUpHandler',
  'RemovePreviewLostKeyboardFocusHandler',
 ]

