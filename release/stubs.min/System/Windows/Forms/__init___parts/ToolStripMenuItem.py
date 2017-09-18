class ToolStripMenuItem(ToolStripDropDownItem,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """
 Represents a selectable option displayed on a System.Windows.Forms.MenuStrip or System.Windows.Forms.ContextMenuStrip. Although System.Windows.Forms.ToolStripMenuItem replaces and adds functionality to the System.Windows.Forms.MenuItem control of previous versions,System.Windows.Forms.MenuItem is retained for both backward compatibility and future use if you choose.

 

 ToolStripMenuItem()

 ToolStripMenuItem(text: str)

 ToolStripMenuItem(image: Image)

 ToolStripMenuItem(text: str,image: Image)

 ToolStripMenuItem(text: str,image: Image,onClick: EventHandler)

 ToolStripMenuItem(text: str,image: Image,onClick: EventHandler,name: str)

 ToolStripMenuItem(text: str,image: Image,*dropDownItems: Array[ToolStripItem])

 ToolStripMenuItem(text: str,image: Image,onClick: EventHandler,shortcutKeys: Keys)
 """
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: ToolStripMenuItem) -> AccessibleObject

  

   Creates a new accessibility object for the System.Windows.Forms.ToolStripMenuItem.

   Returns: A new System.Windows.Forms.AccessibleObject for the System.Windows.Forms.ToolStripMenuItem.
  """
  pass
 def CreateDefaultDropDown(self,*args):
  """
  CreateDefaultDropDown(self: ToolStripMenuItem) -> ToolStripDropDown

  

   Creates a generic System.Windows.Forms.ToolStripDropDown for which events can be defined.

   Returns: A System.Windows.Forms.ToolStripDropDown.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripMenuItem,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripMenuItem and 

    optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
  """ OnBoundsChanged(self: ToolStripDropDownItem) """
  pass
 def OnCheckedChanged(self,*args):
  """
  OnCheckedChanged(self: ToolStripMenuItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripMenuItem.CheckedChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCheckStateChanged(self,*args):
  """
  OnCheckStateChanged(self: ToolStripMenuItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripMenuItem.CheckStateChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: ToolStripMenuItem,e: EventArgs)

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
 def OnDropDownClosed(self,*args):
  """
  OnDropDownClosed(self: ToolStripDropDownItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripDropDownItem.DropDownClosed event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDropDownHide(self,*args):
  """
  OnDropDownHide(self: ToolStripMenuItem,e: EventArgs)

   Raised in response to the System.Windows.Forms.ToolStripDropDownItem.HideDropDown method.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDropDownItemClicked(self,*args):
  """
  OnDropDownItemClicked(self: ToolStripDropDownItem,e: ToolStripItemClickedEventArgs)

   Raises the System.Windows.Forms.ToolStripDropDownItem.DropDownItemClicked event.

  

   e: A System.Windows.Forms.ToolStripItemClickedEventArgs that contains the event data.
  """
  pass
 def OnDropDownOpened(self,*args):
  """
  OnDropDownOpened(self: ToolStripDropDownItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripDropDownItem.DropDownOpened event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDropDownShow(self,*args):
  """
  OnDropDownShow(self: ToolStripMenuItem,e: EventArgs)

   Raised in response to the System.Windows.Forms.ToolStripDropDownItem.ShowDropDown method.

  

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
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: ToolStripMenuItem,e: EventArgs)

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
 def OnLayout(self,*args):
  """
  OnLayout(self: ToolStripItem,e: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event.

  

   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLocationChanged(self,*args):
  """
  OnLocationChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.LocationChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: ToolStripMenuItem,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseDown event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: ToolStripMenuItem,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseEnter event.

  

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
  OnMouseLeave(self: ToolStripMenuItem,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseLeave event.

  

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
  OnMouseUp(self: ToolStripMenuItem,e: MouseEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.MouseUp event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnOwnerChanged(self,*args):
  """
  OnOwnerChanged(self: ToolStripMenuItem,e: EventArgs)

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
  OnPaint(self: ToolStripMenuItem,e: PaintEventArgs)

   Raises the System.Windows.Forms.Control.Paint event.

  

   e: An System.EventArgs that contains the event data.
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
  OnParentChanged(self: ToolStripItem,oldParent: ToolStrip,newParent: ToolStrip)

   Raises the System.Windows.Forms.Control.ParentChanged event.

  

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
  OnRightToLeftChanged(self: ToolStripDropDownItem,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.TextChanged event.

  

   e: An System.EventArgs that contains the event data.
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
  ProcessCmdKey(self: ToolStripMenuItem,m: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   m: A System.Windows.Forms.Message,passed by reference,which represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: ToolStripDropDownItem,keyData: Keys) -> bool

  

   Processes a dialog key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed by the item; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: ToolStripMenuItem,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def SetBounds(self,*args):
  """
  SetBounds(self: ToolStripMenuItem,rect: Rectangle)

   Sets the size and location of the System.Windows.Forms.ToolStripMenuItem.

  

   rect: A System.Drawing.Rectangle that represents the size and location of the 

    System.Windows.Forms.ToolStripMenuItem.
  """
  pass
 def SetVisibleCore(self,*args):
  """
  SetVisibleCore(self: ToolStripItem,visible: bool)

   Sets the System.Windows.Forms.ToolStripItem to the specified visible state.

  

   visible: true to make the System.Windows.Forms.ToolStripItem visible; otherwise,false.
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

  __new__(cls: type,text: str)

  __new__(cls: type,image: Image)

  __new__(cls: type,text: str,image: Image)

  __new__(cls: type,text: str,image: Image,onClick: EventHandler)

  __new__(cls: type,text: str,image: Image,onClick: EventHandler,name: str)

  __new__(cls: type,text: str,image: Image,*dropDownItems: Array[ToolStripItem])

  __new__(cls: type,text: str,image: Image,onClick: EventHandler,shortcutKeys: Keys)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Checked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripMenuItem is checked.



Get: Checked(self: ToolStripMenuItem) -> bool



Set: Checked(self: ToolStripMenuItem)=value

"""

 CheckOnClick=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripMenuItem should automatically appear checked and unchecked when clicked.



Get: CheckOnClick(self: ToolStripMenuItem) -> bool



Set: CheckOnClick(self: ToolStripMenuItem)=value

"""

 CheckState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a System.Windows.Forms.ToolStripMenuItem is in the checked,unchecked,or indeterminate state.



Get: CheckState(self: ToolStripMenuItem) -> CheckState



Set: CheckState(self: ToolStripMenuItem)=value

"""

 DefaultAutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to display the System.Windows.Forms.ToolTip that is defined as the default.



"""

 DefaultDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating what is displayed on the System.Windows.Forms.ToolStripItem.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the spacing between the System.Windows.Forms.ToolStripMenuItem and an adjacent item.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing within the System.Windows.Forms.ToolStripMenuItem.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the System.Windows.Forms.ToolStripMenuItem.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DismissWhenClicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items on a System.Windows.Forms.ToolStripDropDown are hidden after they are clicked.



"""

 DropDownLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the screen coordinates,in pixels,of the upper-left corner of the System.Windows.Forms.ToolStripDropDownItem.



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control is enabled.



Get: Enabled(self: ToolStripMenuItem) -> bool



Set: Enabled(self: ToolStripMenuItem)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 IsMdiWindowListEntry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.ToolStripMenuItem appears on a multiple document interface (MDI) window list.



Get: IsMdiWindowListEntry(self: ToolStripMenuItem) -> bool



"""

 Overflow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripMenuItem is attached to the System.Windows.Forms.ToolStrip or the System.Windows.Forms.ToolStripOverflowButton or whether it can float between the two.



Get: Overflow(self: ToolStripMenuItem) -> ToolStripItemOverflow



Set: Overflow(self: ToolStripMenuItem)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 ShortcutKeyDisplayString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut key text.



Get: ShortcutKeyDisplayString(self: ToolStripMenuItem) -> str



Set: ShortcutKeyDisplayString(self: ToolStripMenuItem)=value

"""

 ShortcutKeys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut keys associated with the System.Windows.Forms.ToolStripMenuItem.



Get: ShortcutKeys(self: ToolStripMenuItem) -> Keys



Set: ShortcutKeys(self: ToolStripMenuItem)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 ShowShortcutKeys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the shortcut keys that are associated with the System.Windows.Forms.ToolStripMenuItem are displayed next to the System.Windows.Forms.ToolStripMenuItem.



Get: ShowShortcutKeys(self: ToolStripMenuItem) -> bool



Set: ShowShortcutKeys(self: ToolStripMenuItem)=value

"""


 CheckedChanged=None
 CheckStateChanged=None

