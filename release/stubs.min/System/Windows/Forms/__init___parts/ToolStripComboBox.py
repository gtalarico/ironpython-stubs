class ToolStripComboBox(ToolStripControlHost,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """
 Represents a System.Windows.Forms.ToolStripComboBox that is properly rendered in a System.Windows.Forms.ToolStrip.

 

 ToolStripComboBox()

 ToolStripComboBox(name: str)

 ToolStripComboBox(c: Control)
 """
 def BeginUpdate(self):
  """
  BeginUpdate(self: ToolStripComboBox)

   Maintains performance when items are added to the System.Windows.Forms.ToolStripComboBox one at 

    a time.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """ CreateAccessibilityInstance(self: ToolStripControlHost) -> AccessibleObject """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripControlHost,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripControlHost and 

    optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndUpdate(self):
  """
  EndUpdate(self: ToolStripComboBox)

   Resumes painting the System.Windows.Forms.ToolStripComboBox control after painting is suspended 

    by the System.Windows.Forms.ToolStripComboBox.BeginUpdate method.
  """
  pass
 def FindString(self,s,startIndex=None):
  """
  FindString(self: ToolStripComboBox,s: str,startIndex: int) -> int

  

   Finds the first item after the given index which starts with the given string.

  

   s: The System.String to search for.

   startIndex: The zero-based index of the item before the first item to be searched. Set to -1 to search from 

    the beginning of the control.

  

   Returns: The zero-based index of the first item found; returns -1 if no match is found.

  FindString(self: ToolStripComboBox,s: str) -> int

  

   Finds the first item in the System.Windows.Forms.ToolStripComboBox that starts with the 

    specified string.

  

  

   s: The System.String to search for.

   Returns: The zero-based index of the first item found; returns -1 if no match is found.
  """
  pass
 def FindStringExact(self,s,startIndex=None):
  """
  FindStringExact(self: ToolStripComboBox,s: str,startIndex: int) -> int

  

   Finds the first item after the specified index that exactly matches the specified string.

  

   s: The System.String to search for.

   startIndex: The zero-based index of the item before the first item to be searched. Set to -1 to search from 

    the beginning of the control.

  

   Returns: The zero-based index of the first item found; returns -1 if no match is found.

  FindStringExact(self: ToolStripComboBox,s: str) -> int

  

   Finds the first item in the System.Windows.Forms.ToolStripComboBox that exactly matches the 

    specified string.

  

  

   s: The System.String to search for.

   Returns: The zero-based index of the first item found; -1 if no match is found.
  """
  pass
 def GetItemHeight(self,index):
  """
  GetItemHeight(self: ToolStripComboBox,index: int) -> int

  

   Returns the height,in pixels,of an item in the System.Windows.Forms.ToolStripComboBox.

  

   index: The index of the item to return the height of.

   Returns: The height,in pixels,of the item at the specified index.
  """
  pass
 def GetPreferredSize(self,constrainingSize):
  """
  GetPreferredSize(self: ToolStripComboBox,constrainingSize: Size) -> Size

  

   Retrieves the size of a rectangular area into which a control can be fitted.

  

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
 def OnDropDown(self,*args):
  """
  OnDropDown(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripComboBox.DropDown event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDropDownClosed(self,*args):
  """
  OnDropDownClosed(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripComboBox.DropDownClosed event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDropDownStyleChanged(self,*args):
  """
  OnDropDownStyleChanged(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripComboBox.DropDownStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
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
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.RightToLeftChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSelectedIndexChanged(self,*args):
  """
  OnSelectedIndexChanged(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripComboBox.SelectedIndexChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSelectionChangeCommitted(self,*args):
  """
  OnSelectionChangeCommitted(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ComboBox.SelectionChangeCommitted event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSubscribeControlEvents(self,*args):
  """
  OnSubscribeControlEvents(self: ToolStripComboBox,control: Control)

   Subscribes events from the specified control.

  

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
 def OnTextUpdate(self,*args):
  """
  OnTextUpdate(self: ToolStripComboBox,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripComboBox.TextUpdate event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnUnsubscribeControlEvents(self,*args):
  """
  OnUnsubscribeControlEvents(self: ToolStripComboBox,control: Control)

   Unsubscribes events from the specified control.

  

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
 def Select(self,start=None,length=None):
  """
  Select(self: ToolStripComboBox,start: int,length: int)

   Selects a range of text in the editable portion of the System.Windows.Forms.ToolStripComboBox.

  

   start: The position of the first character in the current text selection within the text box.

   length: The number of characters to select.
  """
  pass
 def SelectAll(self):
  """
  SelectAll(self: ToolStripComboBox)

   Selects all the text in the editable portion of the System.Windows.Forms.ToolStripComboBox.
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
 def ToString(self):
  """
  ToString(self: ToolStripComboBox) -> str

  

   Returns a string representation of the System.Windows.Forms.ToolStripComboBox.

   Returns: A string that represents the System.Windows.Forms.ToolStripComboBox.
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
 AutoCompleteCustomSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the custom string collection to use when the System.Windows.Forms.ToolStripComboBox.AutoCompleteSource property is set to System.Windows.Forms.AutoCompleteSource.CustomSource.



Get: AutoCompleteCustomSource(self: ToolStripComboBox) -> AutoCompleteStringCollection



Set: AutoCompleteCustomSource(self: ToolStripComboBox)=value

"""

 AutoCompleteMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates the text completion behavior of the System.Windows.Forms.ToolStripComboBox.



Get: AutoCompleteMode(self: ToolStripComboBox) -> AutoCompleteMode



Set: AutoCompleteMode(self: ToolStripComboBox)=value

"""

 AutoCompleteSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the source of complete strings used for automatic completion.



Get: AutoCompleteSource(self: ToolStripComboBox) -> AutoCompleteSource



Set: AutoCompleteSource(self: ToolStripComboBox)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImage(self: ToolStripComboBox) -> Image



Set: BackgroundImage(self: ToolStripComboBox)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImageLayout(self: ToolStripComboBox) -> ImageLayout



Set: BackgroundImageLayout(self: ToolStripComboBox)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 ComboBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Forms.ComboBox in which the user can enter text,along with a list from which the user can select.



Get: ComboBox(self: ToolStripComboBox) -> ComboBox



"""

 DefaultAutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to display the System.Windows.Forms.ToolTip that is defined as the default.



"""

 DefaultDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating what is displayed on the System.Windows.Forms.ToolStripItem.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default spacing,in pixels,between the System.Windows.Forms.ToolStripComboBox and an adjacent item.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing characteristics of the item.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the System.Windows.Forms.ToolStripComboBox.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DismissWhenClicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items on a System.Windows.Forms.ToolStripDropDown are hidden after they are clicked.



"""

 DropDownHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height,in pixels,of the drop-down portion box of a System.Windows.Forms.ToolStripComboBox.



Get: DropDownHeight(self: ToolStripComboBox) -> int



Set: DropDownHeight(self: ToolStripComboBox)=value

"""

 DropDownStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the style of the System.Windows.Forms.ToolStripComboBox.



Get: DropDownStyle(self: ToolStripComboBox) -> ComboBoxStyle



Set: DropDownStyle(self: ToolStripComboBox)=value

"""

 DropDownWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the drop-down portion of a System.Windows.Forms.ToolStripComboBox.



Get: DropDownWidth(self: ToolStripComboBox) -> int



Set: DropDownWidth(self: ToolStripComboBox)=value

"""

 DroppedDown=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripComboBox currently displays its drop-down portion.



Get: DroppedDown(self: ToolStripComboBox) -> bool



Set: DroppedDown(self: ToolStripComboBox)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FlatStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the appearance of the System.Windows.Forms.ToolStripComboBox.



Get: FlatStyle(self: ToolStripComboBox) -> FlatStyle



Set: FlatStyle(self: ToolStripComboBox)=value

"""

 IntegralHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripComboBox should resize to avoid showing partial items.



Get: IntegralHeight(self: ToolStripComboBox) -> bool



Set: IntegralHeight(self: ToolStripComboBox)=value

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of the items contained in this System.Windows.Forms.ToolStripComboBox.



Get: Items(self: ToolStripComboBox) -> ObjectCollection



"""

 MaxDropDownItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of items to be shown in the drop-down portion of the System.Windows.Forms.ToolStripComboBox.



Get: MaxDropDownItems(self: ToolStripComboBox) -> int



Set: MaxDropDownItems(self: ToolStripComboBox)=value

"""

 MaxLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of characters allowed in the editable portion of a combo box.



Get: MaxLength(self: ToolStripComboBox) -> int



Set: MaxLength(self: ToolStripComboBox)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 SelectedIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index specifying the currently selected item.



Get: SelectedIndex(self: ToolStripComboBox) -> int



Set: SelectedIndex(self: ToolStripComboBox)=value

"""

 SelectedItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets currently selected item in the System.Windows.Forms.ToolStripComboBox.



Get: SelectedItem(self: ToolStripComboBox) -> object



Set: SelectedItem(self: ToolStripComboBox)=value

"""

 SelectedText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that is selected in the editable portion of a System.Windows.Forms.ToolStripComboBox.



Get: SelectedText(self: ToolStripComboBox) -> str



Set: SelectedText(self: ToolStripComboBox)=value

"""

 SelectionLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of characters selected in the editable portion of the System.Windows.Forms.ToolStripComboBox.



Get: SelectionLength(self: ToolStripComboBox) -> int



Set: SelectionLength(self: ToolStripComboBox)=value

"""

 SelectionStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the starting index of text selected in the System.Windows.Forms.ToolStripComboBox.



Get: SelectionStart(self: ToolStripComboBox) -> int



Set: SelectionStart(self: ToolStripComboBox)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 Sorted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the items in the System.Windows.Forms.ToolStripComboBox are sorted.



Get: Sorted(self: ToolStripComboBox) -> bool



Set: Sorted(self: ToolStripComboBox)=value

"""


 DoubleClick=None
 DropDown=None
 DropDownClosed=None
 DropDownStyleChanged=None
 SelectedIndexChanged=None
 TextUpdate=None

