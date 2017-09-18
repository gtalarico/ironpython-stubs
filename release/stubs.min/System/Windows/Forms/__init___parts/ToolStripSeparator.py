class ToolStripSeparator(ToolStripItem,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """
 Represents a line used to group items of a System.Windows.Forms.ToolStrip or the drop-down items of a System.Windows.Forms.MenuStrip or System.Windows.Forms.ContextMenuStrip or other System.Windows.Forms.ToolStripDropDown control.

 

 ToolStripSeparator()
 """
 def CreateAccessibilityInstance(self,*args):
  """ CreateAccessibilityInstance(self: ToolStripSeparator) -> AccessibleObject """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripItem,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripItem and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetPreferredSize(self,constrainingSize):
  """
  GetPreferredSize(self: ToolStripSeparator,constrainingSize: Size) -> Size

  

   Retrieves the size of a rectangular area into which a System.Windows.Forms.ToolStripSeparator 

    can be fitted.

  

  

   constrainingSize: A System.Drawing.Size representing the height and width of the 

    System.Windows.Forms.ToolStripSeparator,in pixels.

  

   Returns: A System.Drawing.Size representing the height and width of the 

    System.Windows.Forms.ToolStripSeparator,in pixels.
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
  OnFontChanged(self: ToolStripSeparator,e: EventArgs)

   This method is not relevant to this class.

  

   e: A System.EventArgs that contains the event data.
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
  OnPaint(self: ToolStripSeparator,e: PaintEventArgs)

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
 def SetBounds(self,*args):
  """
  SetBounds(self: ToolStripSeparator,rect: Rectangle)

   Sets the size and location of the System.Windows.Forms.ToolStripSeparator.

  

   rect: A System.Drawing.Rectangle specifying the size and location of the 

    System.Windows.Forms.ToolStripSeparator.
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
 def __str__(self,*args):
  pass
 AutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: AutoToolTip(self: ToolStripSeparator) -> bool



Set: AutoToolTip(self: ToolStripSeparator)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImage(self: ToolStripSeparator) -> Image



Set: BackgroundImage(self: ToolStripSeparator)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImageLayout(self: ToolStripSeparator) -> ImageLayout



Set: BackgroundImageLayout(self: ToolStripSeparator)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CanSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.ToolStripSeparator can be selected.



Get: CanSelect(self: ToolStripSeparator) -> bool



"""

 DefaultAutoToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to display the System.Windows.Forms.ToolTip that is defined as the default.



"""

 DefaultDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating what is displayed on the System.Windows.Forms.ToolStripItem.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing characteristics of the item.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DismissWhenClicked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether items on a System.Windows.Forms.ToolStripDropDown are hidden after they are clicked.



"""

 DisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: DisplayStyle(self: ToolStripSeparator) -> ToolStripItemDisplayStyle



Set: DisplayStyle(self: ToolStripSeparator)=value

"""

 DoubleClickEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: DoubleClickEnabled(self: ToolStripSeparator) -> bool



Set: DoubleClickEnabled(self: ToolStripSeparator)=value

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Enabled(self: ToolStripSeparator) -> bool



Set: Enabled(self: ToolStripSeparator)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Font(self: ToolStripSeparator) -> Font



Set: Font(self: ToolStripSeparator)=value

"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Image(self: ToolStripSeparator) -> Image



Set: Image(self: ToolStripSeparator)=value

"""

 ImageAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ImageAlign(self: ToolStripSeparator) -> ContentAlignment



Set: ImageAlign(self: ToolStripSeparator)=value

"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ImageIndex(self: ToolStripSeparator) -> int



Set: ImageIndex(self: ToolStripSeparator)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ImageKey(self: ToolStripSeparator) -> str



Set: ImageKey(self: ToolStripSeparator)=value

"""

 ImageScaling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ImageScaling(self: ToolStripSeparator) -> ToolStripItemImageScaling



Set: ImageScaling(self: ToolStripSeparator)=value

"""

 ImageTransparentColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ImageTransparentColor(self: ToolStripSeparator) -> Color



Set: ImageTransparentColor(self: ToolStripSeparator)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 RightToLeftAutoMirrorImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: RightToLeftAutoMirrorImage(self: ToolStripSeparator) -> bool



Set: RightToLeftAutoMirrorImage(self: ToolStripSeparator)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Text(self: ToolStripSeparator) -> str



Set: Text(self: ToolStripSeparator)=value

"""

 TextAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: TextAlign(self: ToolStripSeparator) -> ContentAlignment



Set: TextAlign(self: ToolStripSeparator)=value

"""

 TextDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: TextDirection(self: ToolStripSeparator) -> ToolStripTextDirection



Set: TextDirection(self: ToolStripSeparator)=value

"""

 TextImageRelation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: TextImageRelation(self: ToolStripSeparator) -> TextImageRelation



Set: TextImageRelation(self: ToolStripSeparator)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: ToolTipText(self: ToolStripSeparator) -> str



Set: ToolTipText(self: ToolStripSeparator)=value

"""


 DisplayStyleChanged=None
 EnabledChanged=None
 TextChanged=None

