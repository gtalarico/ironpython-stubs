class HtmlElementEventArgs(EventArgs):
 """ Provides data for the events defined on System.Windows.Forms.HtmlDocument and System.Windows.Forms.HtmlElement. """
 AltKeyPressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the ALT key was pressed when this event occurred.



Get: AltKeyPressed(self: HtmlElementEventArgs) -> bool



"""

 BubbleEvent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the current event bubbles up through the element hierarchy of the HTML Document Object Model.



Get: BubbleEvent(self: HtmlElementEventArgs) -> bool



Set: BubbleEvent(self: HtmlElementEventArgs)=value

"""

 ClientMousePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of the mouse cursor in the document's client area.



Get: ClientMousePosition(self: HtmlElementEventArgs) -> Point



"""

 CtrlKeyPressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the CTRL key was pressed when this event occurred.



Get: CtrlKeyPressed(self: HtmlElementEventArgs) -> bool



"""

 EventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the event that was raised.



Get: EventType(self: HtmlElementEventArgs) -> str



"""

 FromElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.HtmlElement the mouse pointer is moving away from.



Get: FromElement(self: HtmlElementEventArgs) -> HtmlElement



"""

 KeyPressedCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ASCII value of the keyboard character typed in a System.Windows.Forms.HtmlElement.KeyPress,System.Windows.Forms.HtmlElement.KeyDown,or System.Windows.Forms.HtmlElement.KeyUp event.



Get: KeyPressedCode(self: HtmlElementEventArgs) -> int



"""

 MouseButtonsPressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the mouse button that was clicked during a System.Windows.Forms.HtmlElement.MouseDown or System.Windows.Forms.HtmlElement.MouseUp event.



Get: MouseButtonsPressed(self: HtmlElementEventArgs) -> MouseButtons



"""

 MousePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of the mouse cursor relative to a relatively positioned parent element.



Get: MousePosition(self: HtmlElementEventArgs) -> Point



"""

 OffsetMousePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of the mouse cursor relative to the element that raises the event.



Get: OffsetMousePosition(self: HtmlElementEventArgs) -> Point



"""

 ReturnValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the return value of the handled event.



Get: ReturnValue(self: HtmlElementEventArgs) -> bool



Set: ReturnValue(self: HtmlElementEventArgs)=value

"""

 ShiftKeyPressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the SHIFT key was pressed when this event occurred.



Get: ShiftKeyPressed(self: HtmlElementEventArgs) -> bool



"""

 ToElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.HtmlElement toward which the user is moving the mouse pointer.



Get: ToElement(self: HtmlElementEventArgs) -> HtmlElement



"""


