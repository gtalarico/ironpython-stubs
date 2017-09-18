class ToolStripTextBox(ToolStripControlHost,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """
 Represents a text box in a System.Windows.Forms.ToolStrip that allows the user to enter text.

 

 ToolStripTextBox()

 ToolStripTextBox(name: str)

 ToolStripTextBox(c: Control)
 """
 def AppendText(self,text):
  """
  AppendText(self: ToolStripTextBox,text: str)

   Appends text to the current text of the System.Windows.Forms.ToolStripTextBox.

  

   text: The text to append to the current contents of the System.Windows.Forms.ToolStripTextBox.
  """
  pass
 def Clear(self):
  """
  Clear(self: ToolStripTextBox)

   Clears all text from the System.Windows.Forms.ToolStripTextBox control.
  """
  pass
 def ClearUndo(self):
  """
  ClearUndo(self: ToolStripTextBox)

   Clears information about the most recent operation from the undo buffer of the 

    System.Windows.Forms.ToolStripTextBox.
  """
  pass
 def Copy(self):
  """
  Copy(self: ToolStripTextBox)

   Copies the current selection in the System.Windows.Forms.ToolStripTextBox to the Clipboard.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """ CreateAccessibilityInstance(self: ToolStripControlHost) -> AccessibleObject """
  pass
 def Cut(self):
  """
  Cut(self: ToolStripTextBox)

   Moves the current selection in the System.Windows.Forms.ToolStripTextBox to the Clipboard.
  """
  pass
 def DeselectAll(self):
  """
  DeselectAll(self: ToolStripTextBox)

   Specifies that the value of the System.Windows.Forms.ToolStripTextBox.SelectionLength property 

    is zero so that no characters are selected in the control.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripControlHost,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripControlHost and 

    optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetCharFromPosition(self,pt):
  """
  GetCharFromPosition(self: ToolStripTextBox,pt: Point) -> Char

  

   Retrieves the character that is closest to the specified location within the control.

  

   pt: The location from which to seek the nearest character.

   Returns: The character at the specified location.
  """
  pass
 def GetCharIndexFromPosition(self,pt):
  """
  GetCharIndexFromPosition(self: ToolStripTextBox,pt: Point) -> int

  

   Retrieves the index of the character nearest to the specified location.

  

   pt: The location to search.

   Returns: The zero-based character index at the specified location.
  """
  pass
 def GetFirstCharIndexFromLine(self,lineNumber):
  """
  GetFirstCharIndexFromLine(self: ToolStripTextBox,lineNumber: int) -> int

  

   Retrieves the index of the first character of a given line.

  

   lineNumber: The line for which to get the index of its first character.

   Returns: The zero-based character index in the specified line.
  """
  pass
 def GetFirstCharIndexOfCurrentLine(self):
  """
  GetFirstCharIndexOfCurrentLine(self: ToolStripTextBox) -> int

  

   Retrieves the index of the first character of the current line.

   Returns: The zero-based character index in the current line.
  """
  pass
 def GetLineFromCharIndex(self,index):
  """
  GetLineFromCharIndex(self: ToolStripTextBox,index: int) -> int

  

   Retrieves the line number from the specified character position within the text of the control.

  

   index: The character index position to search.

   Returns: The zero-based line number in which the character index is located.
  """
  pass
 def GetPositionFromCharIndex(self,index):
  """
  GetPositionFromCharIndex(self: ToolStripTextBox,index: int) -> Point

  

   Retrieves the location within the control at the specified character index.

  

   index: The index of the character for which to retrieve the location.

   Returns: The location of the specified character.
  """
  pass
 def GetPreferredSize(self,constrainingSize):
  """
  GetPreferredSize(self: ToolStripTextBox,constrainingSize: Size) -> Size

  

   constrainingSize: The custom-sized area for a control.

   Returns: An ordered pair of type System.Drawing.Size representing the width and height of a rectangle.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def IsInputChar(self,*args):
  """
  IsInputChar(self: ToolStripItem,charCode: Char) -> bool

  

   Determines whether a character is an input character that the item recognizes.

  

   charCode: The character to test.

   Returns: true if the character should be sent directly to the item and not preprocessed; otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: ToolStripItem,keyData: Keys) -> bool

  

   Determines whether the specified key is a regular input key or a special key that requires 

    preprocessing.

  

  

   keyData: One of the System.Windows.Forms.Keys values.

   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnAcceptsTabChanged(self,*args):
  """
  OnAcceptsTabChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.AcceptsTabChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnAvailableChanged(self,*args):
  """
  OnAvailableChanged(self: ToolStripItem,e: EventArgs)

   Raises the AvailableChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBorderStyleChanged(self,*args):
  """
  OnBorderStyleChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.BorderStyleChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnBoundsChanged(self,*args):
  """
  OnBoundsChanged(self: ToolStripControlHost)

   Occurs when the System.Windows.Forms.ToolStripItem.Bounds property changes.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.Click event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDisplayStyleChanged(self,*args):
  """
  OnDisplayStyleChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DisplayStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDoubleClick(self,*args):
  """
  OnDoubleClick(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DoubleClick event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragDrop(self,*args):
  """
  OnDragDrop(self: ToolStripItem,dragEvent: DragEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DragDrop event.

  

   dragEvent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: ToolStripItem,dragEvent: DragEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DragEnter event.

  

   dragEvent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DragLeave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: ToolStripItem,dragEvent: DragEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.DragOver event.

  

   dragEvent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnEnabledChanged(self,*args):
  """
  OnEnabledChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.EnabledChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: ToolStripControlHost,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.Control.FontChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.ForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: ToolStripItem,giveFeedbackEvent: GiveFeedbackEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.GiveFeedback event.

  

   giveFeedbackEvent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: ToolStripControlHost,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.GotFocus event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHideSelectionChanged(self,*args):
  """
  OnHideSelectionChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.HideSelectionChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnHostedControlResize(self,*args):
  """
  OnHostedControlResize(self: ToolStripControlHost,e: EventArgs)

   Synchronizes the resizing of the control host with the resizing of the hosted control.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: ToolStripControlHost,e: KeyEventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.KeyDown event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: ToolStripControlHost,e: KeyPressEventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.KeyPress event.

  

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: ToolStripControlHost,e: KeyEventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.KeyUp event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnLayout(self,*args):
  """
  OnLayout(self: ToolStripControlHost,e: LayoutEventArgs)

   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: ToolStripControlHost,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.Leave event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnLocationChanged(self,*args):
  """
  OnLocationChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.LocationChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: ToolStripControlHost,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.LostFocus event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnModifiedChanged(self,*args):
  """
  OnModifiedChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.ModifiedChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: ToolStripItem,e: MouseEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseDown event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseEnter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseHover(self,*args):
  """
  OnMouseHover(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseHover event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseLeave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: ToolStripItem,mea: MouseEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseMove event.

  

   mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: ToolStripItem,e: MouseEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseUp event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMultilineChanged(self,*args):
  """
  OnMultilineChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.MultilineChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnOwnerChanged(self,*args):
  """
  OnOwnerChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.OwnerChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnOwnerFontChanged(self,*args):
  """
  OnOwnerFontChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.Control.FontChanged event when the 

    System.Windows.Forms.ToolStripItem.Font property has changed on the parent of the 

    System.Windows.Forms.ToolStripItem.

  

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnPaint(self,*args):
  """
  OnPaint(self: ToolStripControlHost,e: PaintEventArgs)

   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnParentBackColorChanged(self,*args):
  """
  OnParentBackColorChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentChanged(self,*args):
  """
  OnParentChanged(self: ToolStripControlHost,oldParent: ToolStrip,newParent: ToolStrip)

   oldParent: The original parent of the item.

   newParent: The new parent of the item.
  """
  pass
 def OnParentEnabledChanged(self,*args):
  """
  OnParentEnabledChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.EnabledChanged event when the 

    System.Windows.Forms.ToolStripItem.Enabled property value of the item's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentForeColorChanged(self,*args):
  """
  OnParentForeColorChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.ForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentRightToLeftChanged(self,*args):
  """
  OnParentRightToLeftChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.RightToLeftChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: ToolStripItem,queryContinueDragEvent: QueryContinueDragEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.QueryContinueDrag event.

  

   queryContinueDragEvent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnReadOnlyChanged(self,*args):
  """
  OnReadOnlyChanged(self: ToolStripTextBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripTextBox.ReadOnlyChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.RightToLeftChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSubscribeControlEvents(self,*args):
  """
  OnSubscribeControlEvents(self: ToolStripTextBox,control: Control)

   control: The control from which to subscribe events.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.TextChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnUnsubscribeControlEvents(self,*args):
  """
  OnUnsubscribeControlEvents(self: ToolStripTextBox,control: Control)

   control: The control from which to unsubscribe events.
  """
  pass
 def OnValidated(self,*args):
  """
  OnValidated(self: ToolStripControlHost,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.Validated event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnValidating(self,*args):
  """
  OnValidating(self: ToolStripControlHost,e: CancelEventArgs)

   Raises the System.Windows.Forms.ToolStripControlHost.Validating event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnVisibleChanged(self,*args):
  """
  OnVisibleChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.VisibleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def Paste(self):
  """
  Paste(self: ToolStripTextBox)

   Replaces the current selection in the text box with the contents of the Clipboard.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: ToolStripControlHost,m: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: false in all cases.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: ToolStripControlHost,keyData: Keys) -> bool

  

   Processes a dialog key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed by the item; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: ToolStripControlHost,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def ScrollToCaret(self):
  """
  ScrollToCaret(self: ToolStripTextBox)

   Scrolls the contents of the control to the current caret position.
  """
  pass
 def Select(self,start=None,length=None):
  """
  Select(self: ToolStripTextBox,start: int,length: int)

   Selects a range of text in the text box.

  

   start: The position of the first character in the current text selection within the text box.

   length: The number of characters to select.
  """
  pass
 def SelectAll(self):
  """
  SelectAll(self: ToolStripTextBox)

   Selects all text in the text box.
  """
  pass
 def SetBounds(self,*args):
  """
  SetBounds(self: ToolStripItem,bounds: Rectangle)

   Sets the size and location of the item.

  

   bounds: A System.Drawing.Rectangle that represents the size and location of the 

    System.Windows.Forms.ToolStripItem
  """
  pass
 def SetVisibleCore(self,*args):
  """
  SetVisibleCore(self: ToolStripControlHost,visible: bool)

   visible: true to make the System.Windows.Forms.ToolStripItem visible; otherwise,false.
  """
  pass
 def Undo(self):
  """
  Undo(self: ToolStripTextBox)

   Undoes the last edit operation in the text box.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,name: str)

  __new__(cls: type,c: Control)
  """
  pass
 def __str__(self,*args):
  pass
 AcceptsReturn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether pressing ENTER in a multiline System.Windows.Forms.TextBox control creates a new line of text in the control or activates the default button for the form.



Get: AcceptsReturn(self: ToolStripTextBox) -> bool



Set: AcceptsReturn(self: ToolStripTextBox)=value

"""

 AcceptsTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether pressing the TAB key in a multiline text box control types a TAB character in the control instead of moving the focus to the next control in the tab order.



Get: AcceptsTab(self: ToolStripTextBox) -> bool



Set: AcceptsTab(self: ToolStripTextBox)=value

"""

 AutoCompleteCustomSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a custom string collection to use when the System.Windows.Forms.ToolStripTextBox.AutoCompleteSource property is set to CustomSource.



Get: AutoCompleteCustomSource(self: ToolStripTextBox) -> AutoCompleteStringCollection



Set: AutoCompleteCustomSource(self: ToolStripTextBox)=value

"""

 AutoCompleteMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an option that controls how automatic completion works for the System.Windows.Forms.ToolStripTextBox.



Get: AutoCompleteMode(self: ToolStripTextBox) -> AutoCompleteMode



Set: AutoCompleteMode(self: ToolStripTextBox)=value

"""

 AutoCompleteSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the source of complete strings used for automatic completion.



Get: AutoCompleteSource(self: ToolStripTextBox) -> AutoCompleteSource



Set: AutoCompleteSource(self: ToolStripTextBox)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImage(self: ToolStripTextBox) -> Image



Set: BackgroundImage(self: ToolStripTextBox)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImageLayout(self: ToolStripTextBox) -> ImageLayout



Set: BackgroundImageLayout(self: ToolStripTextBox)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border type of the System.Windows.Forms.ToolStripTextBox control.



Get: BorderStyle(self: ToolStripTextBox) -> BorderStyle



Set: BorderStyle(self: ToolStripTextBox)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CanUndo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user can undo the previous operation in a System.Windows.Forms.ToolStripTextBox control.



Get: CanUndo(self: ToolStripTextBox) -> bool



"""

 CharacterCasing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the System.Windows.Forms.ToolStripTextBox control modifies the case of characters as they are typed.



Get: CharacterCasing(self: ToolStripTextBox) -> CharacterCasing



Set: CharacterCasing(self: ToolStripTextBox)=value

"""

 DefaultAutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to display the System.Windows.Forms.ToolTip that is defined as the default.



"""

 DefaultDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating what is displayed on the System.Windows.Forms.ToolStripItem.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the spacing,in pixels,between the System.Windows.Forms.ToolStripTextBox and adjacent items.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing characteristics of the item.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the System.Windows.Forms.ToolStripTextBox.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DismissWhenClicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items on a System.Windows.Forms.ToolStripDropDown are hidden after they are clicked.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 HideSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the selected text in the text box control remains highlighted when the control loses focus.



Get: HideSelection(self: ToolStripTextBox) -> bool



Set: HideSelection(self: ToolStripTextBox)=value

"""

 Lines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lines of text in a System.Windows.Forms.ToolStripTextBox control.



Get: Lines(self: ToolStripTextBox) -> Array[str]



Set: Lines(self: ToolStripTextBox)=value

"""

 MaxLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of characters the user can type or paste into the text box control.



Get: MaxLength(self: ToolStripTextBox) -> int



Set: MaxLength(self: ToolStripTextBox)=value

"""

 Modified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates that the System.Windows.Forms.ToolStripTextBox control has been modified by the user since the control was created or its contents were last set.



Get: Modified(self: ToolStripTextBox) -> bool



Set: Modified(self: ToolStripTextBox)=value

"""

 Multiline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Multiline(self: ToolStripTextBox) -> bool



Set: Multiline(self: ToolStripTextBox)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether text in the System.Windows.Forms.ToolStripTextBox is read-only.



Get: ReadOnly(self: ToolStripTextBox) -> bool



Set: ReadOnly(self: ToolStripTextBox)=value

"""

 SelectedText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the currently selected text in the control.



Get: SelectedText(self: ToolStripTextBox) -> str



Set: SelectedText(self: ToolStripTextBox)=value

"""

 SelectionLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of characters selected in theSystem.Windows.Forms.ToolStripTextBox.



Get: SelectionLength(self: ToolStripTextBox) -> int



Set: SelectionLength(self: ToolStripTextBox)=value

"""

 SelectionStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the starting point of text selected in theSystem.Windows.Forms.ToolStripTextBox.



Get: SelectionStart(self: ToolStripTextBox) -> int



Set: SelectionStart(self: ToolStripTextBox)=value

"""

 ShortcutsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the defined shortcuts are enabled.



Get: ShortcutsEnabled(self: ToolStripTextBox) -> bool



Set: ShortcutsEnabled(self: ToolStripTextBox)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 TextBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hosted System.Windows.Forms.TextBox control.



Get: TextBox(self: ToolStripTextBox) -> TextBox



"""

 TextBoxTextAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how text is aligned in a System.Windows.Forms.TextBox control.



Get: TextBoxTextAlign(self: ToolStripTextBox) -> HorizontalAlignment



Set: TextBoxTextAlign(self: ToolStripTextBox)=value

"""

 TextLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of text in the control.



Get: TextLength(self: ToolStripTextBox) -> int



"""

 WordWrap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: WordWrap(self: ToolStripTextBox) -> bool



Set: WordWrap(self: ToolStripTextBox)=value

"""


 AcceptsTabChanged=None
 BorderStyleChanged=None
 HideSelectionChanged=None
 ModifiedChanged=None
 MultilineChanged=None
 ReadOnlyChanged=None
 TextBoxTextAlignChanged=None

