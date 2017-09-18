class ToolStripLabel(ToolStripItem,IComponent,IDisposable,IDropTarget,ISupportOleDropSource,IArrangedElement):
 """
 Represents a nonselectable System.Windows.Forms.ToolStripItem that renders text and images and can display hyperlinks.

 

 ToolStripLabel()

 ToolStripLabel(text: str)

 ToolStripLabel(image: Image)

 ToolStripLabel(text: str,image: Image)

 ToolStripLabel(text: str,image: Image,isLink: bool)

 ToolStripLabel(text: str,image: Image,isLink: bool,onClick: EventHandler)

 ToolStripLabel(text: str,image: Image,isLink: bool,onClick: EventHandler,name: str)
 """
 def CreateAccessibilityInstance(self,*args):
  """ CreateAccessibilityInstance(self: ToolStripLabel) -> AccessibleObject """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripItem,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripItem and optionally 

    releases the managed resources.

  

  

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
  OnFontChanged(self: ToolStripLabel,e: EventArgs)

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
  OnMouseEnter(self: ToolStripLabel,e: EventArgs)

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
  OnMouseLeave(self: ToolStripLabel,e: EventArgs)

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
  OnPaint(self: ToolStripLabel,e: PaintEventArgs)

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
  ProcessMnemonic(self: ToolStripLabel,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
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

  __new__(cls: type,text: str,image: Image,isLink: bool)

  __new__(cls: type,text: str,image: Image,isLink: bool,onClick: EventHandler)

  __new__(cls: type,text: str,image: Image,isLink: bool,onClick: EventHandler,name: str)
  """
  pass
 def __str__(self,*args):
  pass
 ActiveLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used to display an active link.



Get: ActiveLinkColor(self: ToolStripLabel) -> Color



Set: ActiveLinkColor(self: ToolStripLabel)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CanSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the selectable state of a System.Windows.Forms.ToolStripLabel.



Get: CanSelect(self: ToolStripLabel) -> bool



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

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 IsLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripLabel is a hyperlink.



Get: IsLink(self: ToolStripLabel) -> bool



Set: IsLink(self: ToolStripLabel)=value

"""

 LinkBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that represents the behavior of a link.



Get: LinkBehavior(self: ToolStripLabel) -> LinkBehavior



Set: LinkBehavior(self: ToolStripLabel)=value

"""

 LinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used when displaying a normal link.



Get: LinkColor(self: ToolStripLabel) -> Color



Set: LinkColor(self: ToolStripLabel)=value

"""

 LinkVisited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a link should be displayed as though it were visited.



Get: LinkVisited(self: ToolStripLabel) -> bool



Set: LinkVisited(self: ToolStripLabel)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the System.Windows.Forms.ToolStripItem.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether to show or hide shortcut keys.



"""

 VisitedLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used when displaying a link that that has been previously visited.



Get: VisitedLinkColor(self: ToolStripLabel) -> Color



Set: VisitedLinkColor(self: ToolStripLabel)=value

"""


