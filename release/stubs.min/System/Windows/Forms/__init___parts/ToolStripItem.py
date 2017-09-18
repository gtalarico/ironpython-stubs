class ToolStripItem(Component,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """ Represents the abstract base class that manages events and layout for all the elements that a System.Windows.Forms.ToolStrip or System.Windows.Forms.ToolStripDropDown can contain. """
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: ToolStripItem) -> AccessibleObject

  

   Creates a new accessibility object for the System.Windows.Forms.ToolStripItem.

   Returns: A new System.Windows.Forms.AccessibleObject for the System.Windows.Forms.ToolStripItem.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripItem,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripItem and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def DoDragDrop(self,data,allowedEffects):
  """
  DoDragDrop(self: ToolStripItem,data: object,allowedEffects: DragDropEffects) -> DragDropEffects

  

   Begins a drag-and-drop operation.

  

   data: The object to be dragged.

   allowedEffects: The drag operations that can occur.

   Returns: One of the System.Windows.Forms.DragDropEffects values.
  """
  pass
 def GetCurrentParent(self):
  """
  GetCurrentParent(self: ToolStripItem) -> ToolStrip

  

   Retrieves the System.Windows.Forms.ToolStrip that is the container of the current 

    System.Windows.Forms.ToolStripItem.

  

   Returns: A System.Windows.Forms.ToolStrip that is the container of the current 

    System.Windows.Forms.ToolStripItem.
  """
  pass
 def GetPreferredSize(self,constrainingSize):
  """
  GetPreferredSize(self: ToolStripItem,constrainingSize: Size) -> Size

  

   Retrieves the size of a rectangular area into which a control can be fit.

  

   constrainingSize: The custom-sized area for a control.

   Returns: A System.Drawing.Size ordered pair,representing the width and height of a rectangle.
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
 def Invalidate(self,r=None):
  """
  Invalidate(self: ToolStripItem,r: Rectangle)

   Invalidates the specified region of the System.Windows.Forms.ToolStripItem by adding it to the 

    update region of the System.Windows.Forms.ToolStripItem,which is the area that will be 

    repainted at the next paint operation,and causes a paint message to be sent to the 

    System.Windows.Forms.ToolStripItem.

  

  

   r: A System.Drawing.Rectangle that represents the region to invalidate.

  Invalidate(self: ToolStripItem)

   Invalidates the entire surface of the System.Windows.Forms.ToolStripItem and causes it to be 

    redrawn.
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
  OnBoundsChanged(self: ToolStripItem)

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
  OnPaint(self: ToolStripItem,e: PaintEventArgs)

   Raises the System.Windows.Forms.ToolStripItem.Paint event.

  

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
  OnRightToLeftChanged(self: ToolStripItem,e: EventArgs)

   Raises the System.Windows.Forms.ToolStripItem.RightToLeftChanged event.

  

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
 def PerformClick(self):
  """
  PerformClick(self: ToolStripItem)

   Activates the System.Windows.Forms.ToolStripItem when it is clicked with the mouse.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: ToolStripItem,m: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: false in all cases.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: ToolStripItem,keyData: Keys) -> bool

  

   Processes a dialog key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed by the item; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: ToolStripItem,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true in all cases.
  """
  pass
 def ResetBackColor(self):
  """
  ResetBackColor(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetDisplayStyle(self):
  """
  ResetDisplayStyle(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetFont(self):
  """
  ResetFont(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetForeColor(self):
  """
  ResetForeColor(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetImage(self):
  """
  ResetImage(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetMargin(self):
  """
  ResetMargin(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetPadding(self):
  """
  ResetPadding(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetRightToLeft(self):
  """
  ResetRightToLeft(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def ResetTextDirection(self):
  """
  ResetTextDirection(self: ToolStripItem)

   This method is not relevant to this class.
  """
  pass
 def Select(self):
  """
  Select(self: ToolStripItem)

   Selects the item.
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
  SetVisibleCore(self: ToolStripItem,visible: bool)

   Sets the System.Windows.Forms.ToolStripItem to the specified visible state.

  

   visible: true to make the System.Windows.Forms.ToolStripItem visible; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: ToolStripItem) -> str

   Returns: A System.String containing the name of the System.ComponentModel.Component,if any,or null if 

    the System.ComponentModel.Component is unnamed.
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,text: str,image: Image,onClick: EventHandler)

  __new__(cls: type,text: str,image: Image,onClick: EventHandler,name: str)
  """
  pass
 def __str__(self,*args):
  pass
 AccessibilityObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.AccessibleObject assigned to the control.



Get: AccessibilityObject(self: ToolStripItem) -> AccessibleObject



"""

 AccessibleDefaultActionDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default action description of the control for use by accessibility client applications.



Get: AccessibleDefaultActionDescription(self: ToolStripItem) -> str



Set: AccessibleDefaultActionDescription(self: ToolStripItem)=value

"""

 AccessibleDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the description that will be reported to accessibility client applications.



Get: AccessibleDescription(self: ToolStripItem) -> str



Set: AccessibleDescription(self: ToolStripItem)=value

"""

 AccessibleName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the control for use by accessibility client applications.



Get: AccessibleName(self: ToolStripItem) -> str



Set: AccessibleName(self: ToolStripItem)=value

"""

 AccessibleRole=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the accessible role of the control,which specifies the type of user interface element of the control.



Get: AccessibleRole(self: ToolStripItem) -> AccessibleRole



Set: AccessibleRole(self: ToolStripItem)=value

"""

 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item aligns towards the beginning or end of the System.Windows.Forms.ToolStrip.



Get: Alignment(self: ToolStripItem) -> ToolStripItemAlignment



Set: Alignment(self: ToolStripItem)=value

"""

 AllowDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether drag-and-drop and item reordering are handled through events that you implement.



Get: AllowDrop(self: ToolStripItem) -> bool



Set: AllowDrop(self: ToolStripItem)=value

"""

 Anchor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edges of the container to which a System.Windows.Forms.ToolStripItem is bound and determines how a System.Windows.Forms.ToolStripItem  is resized with its parent.



Get: Anchor(self: ToolStripItem) -> AnchorStyles



Set: Anchor(self: ToolStripItem)=value

"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is automatically sized.



Get: AutoSize(self: ToolStripItem) -> bool



Set: AutoSize(self: ToolStripItem)=value

"""

 AutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to use the System.Windows.Forms.ToolStripItem.Text property or the System.Windows.Forms.ToolStripItem.ToolTipText property for the System.Windows.Forms.ToolStripItem ToolTip.



Get: AutoToolTip(self: ToolStripItem) -> bool



Set: AutoToolTip(self: ToolStripItem)=value

"""

 Available=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripItem should be placed on a System.Windows.Forms.ToolStrip.



Get: Available(self: ToolStripItem) -> bool



Set: Available(self: ToolStripItem)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the item.



Get: BackColor(self: ToolStripItem) -> Color



Set: BackColor(self: ToolStripItem)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image displayed in the item.



Get: BackgroundImage(self: ToolStripItem) -> Image



Set: BackgroundImage(self: ToolStripItem)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image layout used for the System.Windows.Forms.ToolStripItem.



Get: BackgroundImageLayout(self: ToolStripItem) -> ImageLayout



Set: BackgroundImageLayout(self: ToolStripItem)=value

"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the item.



Get: Bounds(self: ToolStripItem) -> Rectangle



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CanSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the item can be selected.



Get: CanSelect(self: ToolStripItem) -> bool



"""

 ContentRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the area where content,such as text and icons,can be placed within a System.Windows.Forms.ToolStripItem without overwriting background borders.



Get: ContentRectangle(self: ToolStripItem) -> Rectangle



"""

 DefaultAutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to display the System.Windows.Forms.ToolTip that is defined as the default.



"""

 DefaultDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating what is displayed on the System.Windows.Forms.ToolStripItem.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default margin of an item.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing characteristics of the item.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the item.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DismissWhenClicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items on a System.Windows.Forms.ToolStripDropDown are hidden after they are clicked.



"""

 DisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether text and images are displayed on a System.Windows.Forms.ToolStripItem.



Get: DisplayStyle(self: ToolStripItem) -> ToolStripItemDisplayStyle



Set: DisplayStyle(self: ToolStripItem)=value

"""

 Dock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets which System.Windows.Forms.ToolStripItem borders are docked to its parent control and determines how a System.Windows.Forms.ToolStripItem is resized with its parent.



Get: Dock(self: ToolStripItem) -> DockStyle



Set: Dock(self: ToolStripItem)=value

"""

 DoubleClickEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripItem can be activated by double-clicking the mouse.



Get: DoubleClickEnabled(self: ToolStripItem) -> bool



Set: DoubleClickEnabled(self: ToolStripItem)=value

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the parent control of the System.Windows.Forms.ToolStripItem is enabled.



Get: Enabled(self: ToolStripItem) -> bool



Set: Enabled(self: ToolStripItem)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text displayed by the item.



Get: Font(self: ToolStripItem) -> Font



Set: Font(self: ToolStripItem)=value

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the item.



Get: ForeColor(self: ToolStripItem) -> Color



Set: ForeColor(self: ToolStripItem)=value

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height,in pixels,of a System.Windows.Forms.ToolStripItem.



Get: Height(self: ToolStripItem) -> int



Set: Height(self: ToolStripItem)=value

"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image that is displayed on a System.Windows.Forms.ToolStripItem.



Get: Image(self: ToolStripItem) -> Image



Set: Image(self: ToolStripItem)=value

"""

 ImageAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of the image on a System.Windows.Forms.ToolStripItem.



Get: ImageAlign(self: ToolStripItem) -> ContentAlignment



Set: ImageAlign(self: ToolStripItem)=value

"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index value of the image that is displayed on the item.



Get: ImageIndex(self: ToolStripItem) -> int



Set: ImageIndex(self: ToolStripItem)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key accessor for the image in the System.Windows.Forms.ToolStrip.ImageList that is displayed on a System.Windows.Forms.ToolStripItem.



Get: ImageKey(self: ToolStripItem) -> str



Set: ImageKey(self: ToolStripItem)=value

"""

 ImageScaling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether an image on a System.Windows.Forms.ToolStripItem is automatically resized to fit in a container.



Get: ImageScaling(self: ToolStripItem) -> ToolStripItemImageScaling



Set: ImageScaling(self: ToolStripItem)=value

"""

 ImageTransparentColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color to treat as transparent in a System.Windows.Forms.ToolStripItem image.



Get: ImageTransparentColor(self: ToolStripItem) -> Color



Set: ImageTransparentColor(self: ToolStripItem)=value

"""

 IsDisposed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the object has been disposed of.



Get: IsDisposed(self: ToolStripItem) -> bool



"""

 IsOnDropDown=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the container of the current System.Windows.Forms.Control is a System.Windows.Forms.ToolStripDropDown.



Get: IsOnDropDown(self: ToolStripItem) -> bool



"""

 IsOnOverflow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.ToolStripItem.Placement property is set to System.Windows.Forms.ToolStripItemPlacement.Overflow.



Get: IsOnOverflow(self: ToolStripItem) -> bool



"""

 Margin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between the item and adjacent items.



Get: Margin(self: ToolStripItem) -> Padding



Set: Margin(self: ToolStripItem)=value

"""

 MergeAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how child menus are merged with parent menus.



Get: MergeAction(self: ToolStripItem) -> MergeAction



Set: MergeAction(self: ToolStripItem)=value

"""

 MergeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of a merged item within the current System.Windows.Forms.ToolStrip.



Get: MergeIndex(self: ToolStripItem) -> int



Set: MergeIndex(self: ToolStripItem)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the item.



Get: Name(self: ToolStripItem) -> str



Set: Name(self: ToolStripItem)=value

"""

 Overflow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the item is attached to the System.Windows.Forms.ToolStrip or System.Windows.Forms.ToolStripOverflowButton or can float between the two.



Get: Overflow(self: ToolStripItem) -> ToolStripItemOverflow



Set: Overflow(self: ToolStripItem)=value

"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the owner of this item.



Get: Owner(self: ToolStripItem) -> ToolStrip



Set: Owner(self: ToolStripItem)=value

"""

 OwnerItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent System.Windows.Forms.ToolStripItem of this System.Windows.Forms.ToolStripItem.



Get: OwnerItem(self: ToolStripItem) -> ToolStripItem



"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the internal spacing,in pixels,between the item's contents and its edges.



Get: Padding(self: ToolStripItem) -> Padding



Set: Padding(self: ToolStripItem)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 Placement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current layout of the item.



Get: Placement(self: ToolStripItem) -> ToolStripItemPlacement



"""

 Pressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the state of the item is pressed.



Get: Pressed(self: ToolStripItem) -> bool



"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether items are to be placed from right to left and text is to be written from right to left.



Get: RightToLeft(self: ToolStripItem) -> RightToLeft



Set: RightToLeft(self: ToolStripItem)=value

"""

 RightToLeftAutoMirrorImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Mirrors automatically the System.Windows.Forms.ToolStripItem image when the System.Windows.Forms.ToolStripItem.RightToLeft property is set to System.Windows.Forms.RightToLeft.Yes.



Get: RightToLeftAutoMirrorImage(self: ToolStripItem) -> bool



Set: RightToLeftAutoMirrorImage(self: ToolStripItem)=value

"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the item is selected.



Get: Selected(self: ToolStripItem) -> bool



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the item.



Get: Size(self: ToolStripItem) -> Size



Set: Size(self: ToolStripItem)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data about the item.



Get: Tag(self: ToolStripItem) -> object



Set: Tag(self: ToolStripItem)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that is to be displayed on the item.



Get: Text(self: ToolStripItem) -> str



Set: Text(self: ToolStripItem)=value

"""

 TextAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of the text on a System.Windows.Forms.ToolStripLabel.



Get: TextAlign(self: ToolStripItem) -> ContentAlignment



Set: TextAlign(self: ToolStripItem)=value

"""

 TextDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the orientation of text used on a System.Windows.Forms.ToolStripItem.



Get: TextDirection(self: ToolStripItem) -> ToolStripTextDirection



Set: TextDirection(self: ToolStripItem)=value

"""

 TextImageRelation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of System.Windows.Forms.ToolStripItem text and image relative to each other.



Get: TextImageRelation(self: ToolStripItem) -> TextImageRelation



Set: TextImageRelation(self: ToolStripItem)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that appears as a System.Windows.Forms.ToolTip for a control.



Get: ToolTipText(self: ToolStripItem) -> str



Set: ToolTipText(self: ToolStripItem)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is displayed.



Get: Visible(self: ToolStripItem) -> bool



Set: Visible(self: ToolStripItem)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width in pixels of a System.Windows.Forms.ToolStripItem.



Get: Width(self: ToolStripItem) -> int



Set: Width(self: ToolStripItem)=value

"""


 AvailableChanged=None
 BackColorChanged=None
 Click=None
 DisplayStyleChanged=None
 DoubleClick=None
 DragDrop=None
 DragEnter=None
 DragLeave=None
 DragOver=None
 EnabledChanged=None
 ForeColorChanged=None
 GiveFeedback=None
 LocationChanged=None
 MouseDown=None
 MouseEnter=None
 MouseHover=None
 MouseLeave=None
 MouseMove=None
 MouseUp=None
 OwnerChanged=None
 Paint=None
 QueryAccessibilityHelp=None
 QueryContinueDrag=None
 RightToLeftChanged=None
 TextChanged=None
 ToolStripItemAccessibleObject=None
 VisibleChanged=None

