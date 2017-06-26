class TreeView(Control, IComponent, IDisposable, IOleControl, IOleObject, IOleInPlaceObject, IOleInPlaceActiveObject, IOleWindow, IViewObject, IViewObject2, IPersist, IPersistStreamInit, IPersistPropertyBag, IPersistStorage, IQuickActivate, ISupportOleDropSource, IDropTarget, ISynchronizeInvoke, IWin32Window, IArrangedElement, IBindableComponent):
    """
    Displays a hierarchical collection of labeled items, each represented by a System.Windows.Forms.TreeNode.
    
    TreeView()
    """
    def AccessibilityNotifyClients(self, *args): #cannot find CLR method
        """
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, objectID: int, childID: int)
            Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control .
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            objectID: The identifier of the System.Windows.Forms.AccessibleObject.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, childID: int)
            Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control.
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        """
        pass

    def BeginUpdate(self):
        """
        BeginUpdate(self: TreeView)
            Disables any redrawing of the tree view.
        """
        pass

    def CollapseAll(self):
        """
        CollapseAll(self: TreeView)
            Collapses all the tree nodes.
        """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: Control) -> AccessibleObject
        
            Creates a new accessibility object for the control.
            Returns: A new System.Windows.Forms.AccessibleObject for the control.
        """
        pass

    def CreateControlsInstance(self, *args): #cannot find CLR method
        """
        CreateControlsInstance(self: Control) -> ControlCollection
        
            Creates a new instance of the control collection for the control.
            Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
        """
        pass

    def CreateHandle(self, *args): #cannot find CLR method
        """ CreateHandle(self: TreeView) """
        pass

    def DefWndProc(self, *args): #cannot find CLR method
        """
        DefWndProc(self: Control, m: Message) -> Message
        
            Sends the specified message to the default window procedure.
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def DestroyHandle(self, *args): #cannot find CLR method
        """
        DestroyHandle(self: Control)
            Destroys the handle associated with the control.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TreeView, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.TreeView and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EndUpdate(self):
        """
        EndUpdate(self: TreeView)
            Enables the redrawing of the tree view.
        """
        pass

    def ExpandAll(self):
        """
        ExpandAll(self: TreeView)
            Expands all the tree nodes.
        """
        pass

    def GetAccessibilityObjectById(self, *args): #cannot find CLR method
        """
        GetAccessibilityObjectById(self: Control, objectId: int) -> AccessibleObject
        
            Retrieves the specified System.Windows.Forms.AccessibleObject.
        
            objectId: An Int32 that identifies the System.Windows.Forms.AccessibleObject to retrieve.
            Returns: An System.Windows.Forms.AccessibleObject.
        """
        pass

    def GetAutoSizeMode(self, *args): #cannot find CLR method
        """
        GetAutoSizeMode(self: Control) -> AutoSizeMode
        
            Retrieves a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
            Returns: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def GetItemRenderStyles(self, *args): #cannot find CLR method
        """
        GetItemRenderStyles(self: TreeView, node: TreeNode, state: int) -> OwnerDrawPropertyBag
        
            Returns an System.Windows.Forms.OwnerDrawPropertyBag for the specified System.Windows.Forms.TreeNode.
        
            node: The System.Windows.Forms.TreeNode for which to return an System.Windows.Forms.OwnerDrawPropertyBag.
            state: The visible state of the System.Windows.Forms.TreeNode.
            Returns: An System.Windows.Forms.OwnerDrawPropertyBag for the specified System.Windows.Forms.TreeNode.
        """
        pass

    def GetNodeAt(self, *__args):
        """
        GetNodeAt(self: TreeView, x: int, y: int) -> TreeNode
        
            Retrieves the tree node at the point with the specified coordinates.
        
            x: The System.Drawing.Point.X position to evaluate and retrieve the node from.
            y: The System.Drawing.Point.Y position to evaluate and retrieve the node from.
            Returns: The System.Windows.Forms.TreeNode at the specified location, in tree view (client) coordinates, or null if there is no node at that location.
        GetNodeAt(self: TreeView, pt: Point) -> TreeNode
        
            Retrieves the tree node that is at the specified point.
        
            pt: The System.Drawing.Point to evaluate and retrieve the node from.
            Returns: The System.Windows.Forms.TreeNode at the specified point, in tree view (client) coordinates, or null if there is no node at that location.
        """
        pass

    def GetNodeCount(self, includeSubTrees):
        """
        GetNodeCount(self: TreeView, includeSubTrees: bool) -> int
        
            Retrieves the number of tree nodes, optionally including those in all subtrees, assigned to the tree view control.
        
            includeSubTrees: true to count the System.Windows.Forms.TreeNode items that the subtrees contain; otherwise, false.
            Returns: The number of tree nodes, optionally including those in all subtrees, assigned to the tree view control.
        """
        pass

    def GetScaledBounds(self, *args): #cannot find CLR method
        """
        GetScaledBounds(self: Control, bounds: Rectangle, factor: SizeF, specified: BoundsSpecified) -> Rectangle
        
            Retrieves the bounds within which the control is scaled.
        
            bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
            factor: The height and width of the control's bounds.
            specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the control to use when defining its size and position.
            Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def GetStyle(self, *args): #cannot find CLR method
        """
        GetStyle(self: Control, flag: ControlStyles) -> bool
        
            Retrieves the value of the specified control style bit for the control.
        
            flag: The System.Windows.Forms.ControlStyles bit to return the value from.
            Returns: true if the specified control style bit is set to true; otherwise, false.
        """
        pass

    def GetTopLevel(self, *args): #cannot find CLR method
        """
        GetTopLevel(self: Control) -> bool
        
            Determines if the control is a top-level control.
            Returns: true if the control is a top-level control; otherwise, false.
        """
        pass

    def HitTest(self, *__args):
        """
        HitTest(self: TreeView, x: int, y: int) -> TreeViewHitTestInfo
        
            Provides node information, given x- and y-coordinates.
        
            x: The x-coordinate at which to retrieve node information
            y: The y-coordinate at which to retrieve node information.
            Returns: A System.Windows.Forms.TreeViewHitTestInfo.
        HitTest(self: TreeView, pt: Point) -> TreeViewHitTestInfo
        
            Provides node information, given a point.
        
            pt: The System.Drawing.Point at which to retrieve node information.
            Returns: A System.Windows.Forms.TreeViewHitTestInfo.
        """
        pass

    def InitLayout(self, *args): #cannot find CLR method
        """
        InitLayout(self: Control)
            Called after the control has been added to another container.
        """
        pass

    def InvokeGotFocus(self, *args): #cannot find CLR method
        """
        InvokeGotFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeLostFocus(self, *args): #cannot find CLR method
        """
        InvokeLostFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeOnClick(self, *args): #cannot find CLR method
        """
        InvokeOnClick(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Click event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokePaint(self, *args): #cannot find CLR method
        """
        InvokePaint(self: Control, c: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def InvokePaintBackground(self, *args): #cannot find CLR method
        """
        InvokePaintBackground(self: Control, c: Control, e: PaintEventArgs)
            Raises the PaintBackground event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def IsInputChar(self, *args): #cannot find CLR method
        """
        IsInputChar(self: Control, charCode: Char) -> bool
        
            Determines if a character is an input character that the control recognizes.
        
            charCode: The character to test.
            Returns: true if the character should be sent directly to the control and not preprocessed; otherwise, false.
        """
        pass

    def IsInputKey(self, *args): #cannot find CLR method
        """
        IsInputKey(self: TreeView, keyData: Keys) -> bool
        
            Determines whether the specified key is a regular input key or a special key that requires preprocessing.
        
            keyData: One of the Keys values.
            Returns: true if the specified key is a regular input key; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is 
             usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NotifyInvalidate(self, *args): #cannot find CLR method
        """
        NotifyInvalidate(self: Control, invalidatedArea: Rectangle)
            Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control to invalidate.
        
            invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
        """
        pass

    def OnAfterCheck(self, *args): #cannot find CLR method
        """
        OnAfterCheck(self: TreeView, e: TreeViewEventArgs)
            Raises the System.Windows.Forms.TreeView.AfterCheck event.
        
            e: A System.Windows.Forms.TreeViewEventArgs that contains the event data.
        """
        pass

    def OnAfterCollapse(self, *args): #cannot find CLR method
        """
        OnAfterCollapse(self: TreeView, e: TreeViewEventArgs)
            Raises the System.Windows.Forms.TreeView.AfterCollapse event.
        
            e: A System.Windows.Forms.TreeViewEventArgs that contains the event data.
        """
        pass

    def OnAfterExpand(self, *args): #cannot find CLR method
        """
        OnAfterExpand(self: TreeView, e: TreeViewEventArgs)
            Raises the System.Windows.Forms.TreeView.AfterExpand event.
        
            e: A System.Windows.Forms.TreeViewEventArgs that contains the event data.
        """
        pass

    def OnAfterLabelEdit(self, *args): #cannot find CLR method
        """
        OnAfterLabelEdit(self: TreeView, e: NodeLabelEditEventArgs)
            Raises the System.Windows.Forms.TreeView.AfterLabelEdit event.
        
            e: A System.Windows.Forms.NodeLabelEditEventArgs that contains the event data.
        """
        pass

    def OnAfterSelect(self, *args): #cannot find CLR method
        """
        OnAfterSelect(self: TreeView, e: TreeViewEventArgs)
            Raises the System.Windows.Forms.TreeView.AfterSelect event.
        
            e: A System.Windows.Forms.TreeViewEventArgs that contains the event data.
        """
        pass

    def OnAutoSizeChanged(self, *args): #cannot find CLR method
        """
        OnAutoSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.AutoSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackColorChanged(self, *args): #cannot find CLR method
        """
        OnBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackgroundImageLayoutChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageLayoutChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBeforeCheck(self, *args): #cannot find CLR method
        """
        OnBeforeCheck(self: TreeView, e: TreeViewCancelEventArgs)
            Raises the System.Windows.Forms.TreeView.BeforeCheck event.
        
            e: A System.Windows.Forms.TreeViewCancelEventArgs that contains the event data.
        """
        pass

    def OnBeforeCollapse(self, *args): #cannot find CLR method
        """
        OnBeforeCollapse(self: TreeView, e: TreeViewCancelEventArgs)
            Raises the System.Windows.Forms.TreeView.BeforeCollapse event.
        
            e: A System.Windows.Forms.TreeViewCancelEventArgs that contains the event data.
        """
        pass

    def OnBeforeExpand(self, *args): #cannot find CLR method
        """
        OnBeforeExpand(self: TreeView, e: TreeViewCancelEventArgs)
            Raises the System.Windows.Forms.TreeView.BeforeExpand event.
        
            e: A System.Windows.Forms.TreeViewCancelEventArgs that contains the event data.
        """
        pass

    def OnBeforeLabelEdit(self, *args): #cannot find CLR method
        """
        OnBeforeLabelEdit(self: TreeView, e: NodeLabelEditEventArgs)
            Raises the System.Windows.Forms.TreeView.BeforeLabelEdit event.
        
            e: A System.Windows.Forms.NodeLabelEditEventArgs that contains the event data.
        """
        pass

    def OnBeforeSelect(self, *args): #cannot find CLR method
        """
        OnBeforeSelect(self: TreeView, e: TreeViewCancelEventArgs)
            Raises the System.Windows.Forms.TreeView.BeforeSelect event.
        
            e: A System.Windows.Forms.TreeViewCancelEventArgs that contains the event data.
        """
        pass

    def OnBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnCausesValidationChanged(self, *args): #cannot find CLR method
        """
        OnCausesValidationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CausesValidationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnChangeUICues(self, *args): #cannot find CLR method
        """
        OnChangeUICues(self: Control, e: UICuesEventArgs)
            Raises the System.Windows.Forms.Control.ChangeUICues event.
        
            e: A System.Windows.Forms.UICuesEventArgs that contains the event data.
        """
        pass

    def OnClick(self, *args): #cannot find CLR method
        """
        OnClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnClientSizeChanged(self, *args): #cannot find CLR method
        """
        OnClientSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ClientSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnContextMenuChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnContextMenuStripChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuStripChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuStripChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnControlAdded(self, *args): #cannot find CLR method
        """
        OnControlAdded(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlAdded event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnControlRemoved(self, *args): #cannot find CLR method
        """
        OnControlRemoved(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlRemoved event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnCreateControl(self, *args): #cannot find CLR method
        """
        OnCreateControl(self: Control)
            Raises the System.Windows.Forms.Control.CreateControl method.
        """
        pass

    def OnCursorChanged(self, *args): #cannot find CLR method
        """
        OnCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDockChanged(self, *args): #cannot find CLR method
        """
        OnDockChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DockChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDoubleClick(self, *args): #cannot find CLR method
        """
        OnDoubleClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DoubleClick event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDragDrop(self, *args): #cannot find CLR method
        """
        OnDragDrop(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragDrop event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragEnter event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DragLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragOver event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDrawNode(self, *args): #cannot find CLR method
        """
        OnDrawNode(self: TreeView, e: DrawTreeNodeEventArgs)
            Raises the System.Windows.Forms.TreeView.DrawNode event.
        
            e: A System.Windows.Forms.DrawTreeNodeEventArgs that contains the event data.
        """
        pass

    def OnEnabledChanged(self, *args): #cannot find CLR method
        """
        OnEnabledChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.EnabledChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnEnter(self, *args): #cannot find CLR method
        """
        OnEnter(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Enter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnFontChanged(self, *args): #cannot find CLR method
        """
        OnFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnForeColorChanged(self, *args): #cannot find CLR method
        """
        OnForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: Control, gfbevent: GiveFeedbackEventArgs)
            Raises the System.Windows.Forms.Control.GiveFeedback event.
        
            gfbevent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleCreated(self, *args): #cannot find CLR method
        """
        OnHandleCreated(self: TreeView, e: EventArgs)
            Overrides System.Windows.Forms.Control.OnHandleCreated(System.EventArgs).
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleDestroyed(self, *args): #cannot find CLR method
        """
        OnHandleDestroyed(self: TreeView, e: EventArgs)
            Overrides System.Windows.Forms.Control.OnHandleDestroyed(System.EventArgs).
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHelpRequested(self, *args): #cannot find CLR method
        """
        OnHelpRequested(self: Control, hevent: HelpEventArgs)
            Raises the System.Windows.Forms.Control.HelpRequested event.
        
            hevent: A System.Windows.Forms.HelpEventArgs that contains the event data.
        """
        pass

    def OnImeModeChanged(self, *args): #cannot find CLR method
        """
        OnImeModeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ImeModeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnInvalidated(self, *args): #cannot find CLR method
        """
        OnInvalidated(self: Control, e: InvalidateEventArgs)
            Raises the System.Windows.Forms.Control.Invalidated event.
        
            e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
        """
        pass

    def OnItemDrag(self, *args): #cannot find CLR method
        """
        OnItemDrag(self: TreeView, e: ItemDragEventArgs)
            Raises the System.Windows.Forms.TreeView.ItemDrag event.
        
            e: An System.Windows.Forms.ItemDragEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: TreeView, e: KeyEventArgs)
            Raises the System.Windows.Forms.Control.KeyDown event.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyPress(self, *args): #cannot find CLR method
        """
        OnKeyPress(self: TreeView, e: KeyPressEventArgs)
            Raises the System.Windows.Forms.Control.KeyPress event.
        
            e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: TreeView, e: KeyEventArgs)
            Overrides System.Windows.Forms.Control.OnKeyUp(System.Windows.Forms.KeyEventArgs).
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnLayout(self, *args): #cannot find CLR method
        """
        OnLayout(self: Control, levent: LayoutEventArgs)
            Raises the System.Windows.Forms.Control.Layout event.
        
            levent: A System.Windows.Forms.LayoutEventArgs that contains the event data.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Leave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLocationChanged(self, *args): #cannot find CLR method
        """
        OnLocationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LocationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMarginChanged(self, *args): #cannot find CLR method
        """
        OnMarginChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MarginChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """
        OnMouseCaptureChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseCaptureChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseClick(self, *args): #cannot find CLR method
        """
        OnMouseClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDoubleClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDown event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseEnter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseHover(self, *args): #cannot find CLR method
        """
        OnMouseHover(self: TreeView, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseHover event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: TreeView, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseLeave event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseMove event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseUp event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseWheel event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMove(self, *args): #cannot find CLR method
        """
        OnMove(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Move event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnNodeMouseClick(self, *args): #cannot find CLR method
        """
        OnNodeMouseClick(self: TreeView, e: TreeNodeMouseClickEventArgs)
            Raises the System.Windows.Forms.TreeView.NodeMouseClick event.
        
            e: A System.Windows.Forms.TreeNodeMouseClickEventArgs that contains the event data.
        """
        pass

    def OnNodeMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnNodeMouseDoubleClick(self: TreeView, e: TreeNodeMouseClickEventArgs)
            Raises the System.Windows.Forms.TreeView.NodeMouseDoubleClick event.
        
            e: A System.Windows.Forms.TreeNodeMouseClickEventArgs that contains the event data.
        """
        pass

    def OnNodeMouseHover(self, *args): #cannot find CLR method
        """
        OnNodeMouseHover(self: TreeView, e: TreeNodeMouseHoverEventArgs)
            Raises the System.Windows.Forms.TreeView.NodeMouseHover event.
        
            e: The System.Windows.Forms.TreeNodeMouseHoverEventArgs that contains the event data.
        """
        pass

    def OnNotifyMessage(self, *args): #cannot find CLR method
        """
        OnNotifyMessage(self: Control, m: Message)
            Notifies the control of Windows messages.
        
            m: A System.Windows.Forms.Message that represents the Windows message.
        """
        pass

    def OnPaddingChanged(self, *args): #cannot find CLR method
        """
        OnPaddingChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.PaddingChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnPaint(self, *args): #cannot find CLR method
        """
        OnPaint(self: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnPaintBackground(self, *args): #cannot find CLR method
        """
        OnPaintBackground(self: Control, pevent: PaintEventArgs)
            Paints the background of the control.
        
            pevent: A System.Windows.Forms.PaintEventArgs that contains information about the control to paint.
        """
        pass

    def OnParentBackColorChanged(self, *args): #cannot find CLR method
        """
        OnParentBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event when the System.Windows.Forms.Control.BackColor property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnParentBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnParentBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event when the System.Windows.Forms.Control.BindingContext property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentChanged(self, *args): #cannot find CLR method
        """
        OnParentChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ParentChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentCursorChanged(self, *args): #cannot find CLR method
        """
        OnParentCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentEnabledChanged(self, *args): #cannot find CLR method
        """
        OnParentEnabledChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.EnabledChanged event when the System.Windows.Forms.Control.Enabled property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentFontChanged(self, *args): #cannot find CLR method
        """
        OnParentFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event when the System.Windows.Forms.Control.Font property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentForeColorChanged(self, *args): #cannot find CLR method
        """
        OnParentForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event when the System.Windows.Forms.Control.ForeColor property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnParentRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event when the System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentVisibleChanged(self, *args): #cannot find CLR method
        """
        OnParentVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event when the System.Windows.Forms.Control.Visible property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: Control, e: PreviewKeyDownEventArgs)
            Raises the System.Windows.Forms.Control.PreviewKeyDown event.
        
            e: A System.Windows.Forms.PreviewKeyDownEventArgs that contains the event data.
        """
        pass

    def OnPrint(self, *args): #cannot find CLR method
        """
        OnPrint(self: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: Control, qcdevent: QueryContinueDragEventArgs)
            Raises the System.Windows.Forms.Control.QueryContinueDrag event.
        
            qcdevent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnRegionChanged(self, *args): #cannot find CLR method
        """
        OnRegionChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RegionChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnResize(self, *args): #cannot find CLR method
        """
        OnResize(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Resize event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftLayoutChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftLayoutChanged(self: TreeView, e: EventArgs)
            Raises the System.Windows.Forms.TreeView.RightToLeftLayoutChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnSizeChanged(self, *args): #cannot find CLR method
        """
        OnSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.StyleChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnSystemColorsChanged(self, *args): #cannot find CLR method
        """
        OnSystemColorsChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SystemColorsChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabIndexChanged(self, *args): #cannot find CLR method
        """
        OnTabIndexChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabIndexChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabStopChanged(self, *args): #cannot find CLR method
        """
        OnTabStopChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabStopChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTextChanged(self, *args): #cannot find CLR method
        """
        OnTextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TextChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidated(self, *args): #cannot find CLR method
        """
        OnValidated(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Validated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidating(self, *args): #cannot find CLR method
        """
        OnValidating(self: Control, e: CancelEventArgs)
            Raises the System.Windows.Forms.Control.Validating event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnVisibleChanged(self, *args): #cannot find CLR method
        """
        OnVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def ProcessCmdKey(self, *args): #cannot find CLR method
        """
        ProcessCmdKey(self: Control, msg: Message, keyData: Keys) -> (bool, Message)
        
            Processes a command key.
        
            msg: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogChar(self, *args): #cannot find CLR method
        """
        ProcessDialogChar(self: Control, charCode: Char) -> bool
        
            Processes a dialog character.
        
            charCode: The character to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogKey(self, *args): #cannot find CLR method
        """
        ProcessDialogKey(self: Control, keyData: Keys) -> bool
        
            Processes a dialog key.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the key was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyEventArgs(self, *args): #cannot find CLR method
        """
        ProcessKeyEventArgs(self: Control, m: Message) -> (bool, Message)
        
            Processes a key message and generates the appropriate control events.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyMessage(self, *args): #cannot find CLR method
        """
        ProcessKeyMessage(self: Control, m: Message) -> (bool, Message)
        
            Processes a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyPreview(self, *args): #cannot find CLR method
        """
        ProcessKeyPreview(self: Control, m: Message) -> (bool, Message)
        
            Previews a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessMnemonic(self, *args): #cannot find CLR method
        """
        ProcessMnemonic(self: Control, charCode: Char) -> bool
        
            Processes a mnemonic character.
        
            charCode: The character to process.
            Returns: true if the character was processed as a mnemonic by the control; otherwise, false.
        """
        pass

    def RaiseDragEvent(self, *args): #cannot find CLR method
        """
        RaiseDragEvent(self: Control, key: object, e: DragEventArgs)
            Raises the appropriate drag event.
        
            key: The event to raise.
            e: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def RaiseKeyEvent(self, *args): #cannot find CLR method
        """
        RaiseKeyEvent(self: Control, key: object, e: KeyEventArgs)
            Raises the appropriate key event.
        
            key: The event to raise.
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def RaiseMouseEvent(self, *args): #cannot find CLR method
        """
        RaiseMouseEvent(self: Control, key: object, e: MouseEventArgs)
            Raises the appropriate mouse event.
        
            key: The event to raise.
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def RaisePaintEvent(self, *args): #cannot find CLR method
        """
        RaisePaintEvent(self: Control, key: object, e: PaintEventArgs)
            Raises the appropriate paint event.
        
            key: The event to raise.
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def RecreateHandle(self, *args): #cannot find CLR method
        """
        RecreateHandle(self: Control)
            Forces the re-creation of the handle for the control.
        """
        pass

    def ResetMouseEventArgs(self, *args): #cannot find CLR method
        """
        ResetMouseEventArgs(self: Control)
            Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
        """
        pass

    def RtlTranslateAlignment(self, *args): #cannot find CLR method
        """
        RtlTranslateAlignment(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        RtlTranslateAlignment(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        RtlTranslateAlignment(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateContent(self, *args): #cannot find CLR method
        """
        RtlTranslateContent(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        """
        pass

    def RtlTranslateHorizontal(self, *args): #cannot find CLR method
        """
        RtlTranslateHorizontal(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateLeftRight(self, *args): #cannot find CLR method
        """
        RtlTranslateLeftRight(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        """
        pass

    def ScaleControl(self, *args): #cannot find CLR method
        """
        ScaleControl(self: Control, factor: SizeF, specified: BoundsSpecified)
            Scales a control's location, size, padding and margin.
        
            factor: The factor by which the height and width of the control will be scaled.
            specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use when defining its size and position.
        """
        pass

    def ScaleCore(self, *args): #cannot find CLR method
        """
        ScaleCore(self: Control, dx: Single, dy: Single)
            This method is not relevant for this class.
        
            dx: The horizontal scaling factor.
            dy: The vertical scaling factor.
        """
        pass

    def Select(self):
        """
        Select(self: Control, directed: bool, forward: bool)
            Activates a child control. Optionally specifies the direction in the tab order to select the control from.
        
            directed: true to specify the direction of the control to select; otherwise, false.
            forward: true to move forward in the tab order; false to move backward in the tab order.
        """
        pass

    def SetAutoSizeMode(self, *args): #cannot find CLR method
        """
        SetAutoSizeMode(self: Control, mode: AutoSizeMode)
            Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
        
            mode: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def SetBoundsCore(self, *args): #cannot find CLR method
        """
        SetBoundsCore(self: Control, x: int, y: int, width: int, height: int, specified: BoundsSpecified)
            Performs the work of setting the specified bounds of this control.
        
            x: The new System.Windows.Forms.Control.Left property value of the control.
            y: The new System.Windows.Forms.Control.Top property value of the control.
            width: The new System.Windows.Forms.Control.Width property value of the control.
            height: The new System.Windows.Forms.Control.Height property value of the control.
            specified: A bitwise combination of the System.Windows.Forms.BoundsSpecified values.
        """
        pass

    def SetClientSizeCore(self, *args): #cannot find CLR method
        """
        SetClientSizeCore(self: Control, x: int, y: int)
            Sets the size of the client area of the control.
        
            x: The client area width, in pixels.
            y: The client area height, in pixels.
        """
        pass

    def SetStyle(self, *args): #cannot find CLR method
        """
        SetStyle(self: Control, flag: ControlStyles, value: bool)
            Sets a specified System.Windows.Forms.ControlStyles flag to either true or false.
        
            flag: The System.Windows.Forms.ControlStyles bit to set.
            value: true to apply the specified style to the control; otherwise, false.
        """
        pass

    def SetTopLevel(self, *args): #cannot find CLR method
        """
        SetTopLevel(self: Control, value: bool)
            Sets the control as the top-level control.
        
            value: true to set the control as the top-level control; otherwise, false.
        """
        pass

    def SetVisibleCore(self, *args): #cannot find CLR method
        """
        SetVisibleCore(self: Control, value: bool)
            Sets the control to the specified visible state.
        
            value: true to make the control visible; otherwise, false.
        """
        pass

    def SizeFromClientSize(self, *args): #cannot find CLR method
        """
        SizeFromClientSize(self: Control, clientSize: Size) -> Size
        
            Determines the size of the entire control from the height and width of its client area.
        
            clientSize: A System.Drawing.Size value representing the height and width of the control's client area.
            Returns: A System.Drawing.Size value representing the height and width of the entire control.
        """
        pass

    def Sort(self):
        """
        Sort(self: TreeView)
            Sorts the items in System.Windows.Forms.TreeView control.
        """
        pass

    def ToString(self):
        """
        ToString(self: TreeView) -> str
        
            Overrides System.ComponentModel.Component.ToString.
        """
        pass

    def UpdateBounds(self, *args): #cannot find CLR method
        """
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int, clientWidth: int, clientHeight: int)
            Updates the bounds of the control with the specified size, location, and client size.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
            clientWidth: The client System.Drawing.Size.Width of the control.
            clientHeight: The client System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int)
            Updates the bounds of the control with the specified size and location.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control)
            Updates the bounds of the control with the current size and location.
        """
        pass

    def UpdateStyles(self, *args): #cannot find CLR method
        """
        UpdateStyles(self: Control)
            Forces the assigned styles to be reapplied to the control.
        """
        pass

    def UpdateZOrder(self, *args): #cannot find CLR method
        """
        UpdateZOrder(self: Control)
            Updates the control in its parent's z-order.
        """
        pass

    def WndProc(self, *args): #cannot find CLR method
        """
        WndProc(self: TreeView, m: Message) -> Message
        
            Overrides System.Windows.Forms.Control.WndProc(System.Windows.Forms.Message@).
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackColor(self: TreeView) -> Color

Set: BackColor(self: TreeView) = value
"""

    BackgroundImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set the background image for the System.Windows.Forms.TreeView control.

Get: BackgroundImage(self: TreeView) -> Image

Set: BackgroundImage(self: TreeView) = value
"""

    BackgroundImageLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the layout of the background image for the System.Windows.Forms.TreeView control.

Get: BackgroundImageLayout(self: TreeView) -> ImageLayout

Set: BackgroundImageLayout(self: TreeView) = value
"""

    BorderStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the border style of the tree view control.

Get: BorderStyle(self: TreeView) -> BorderStyle

Set: BorderStyle(self: TreeView) = value
"""

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value, to enable IME support.

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if events can be raised on the control.

"""

    CheckBoxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether check boxes are displayed next to the tree nodes in the tree view control.

Get: CheckBoxes(self: TreeView) -> bool

Set: CheckBoxes(self: TreeView) = value
"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Overrides System.Windows.Forms.Control.CreateParams.

"""

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cursor for the control.

"""

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default Input Method Editor (IME) mode supported by the control.

"""

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the space, in pixels, that is specified by default between controls.

"""

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default maximum size of a control.

"""

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default minimum size of a control.

"""

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal spacing, in pixels, of the contents of a control.

"""

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control should redraw its surface using a secondary buffer. The System.Windows.Forms.TreeView.DoubleBuffered property does not affect the System.Windows.Forms.TreeView control.

"""

    DrawMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the mode in which the control is drawn.

Get: DrawMode(self: TreeView) -> TreeViewDrawMode

Set: DrawMode(self: TreeView) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the font of the control.

"""

    ForeColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current foreground color for this control, which is the color the control uses to draw its text.

Get: ForeColor(self: TreeView) -> Color

Set: ForeColor(self: TreeView) = value
"""

    FullRowSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the selection highlight spans the width of the tree view control.

Get: FullRowSelect(self: TreeView) -> bool

Set: FullRowSelect(self: TreeView) = value
"""

    HideSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the selected tree node remains highlighted even when the tree view has lost the focus.

Get: HideSelection(self: TreeView) -> bool

Set: HideSelection(self: TreeView) = value
"""

    HotTracking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether a tree node label takes on the appearance of a hyperlink as the mouse pointer passes over it.

Get: HotTracking(self: TreeView) -> bool

Set: HotTracking(self: TreeView) = value
"""

    ImageIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image-list index value of the default image that is displayed by the tree nodes.

Get: ImageIndex(self: TreeView) -> int

Set: ImageIndex(self: TreeView) = value
"""

    ImageKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key of the default image for each node in the System.Windows.Forms.TreeView control when it is in an unselected state.

Get: ImageKey(self: TreeView) -> str

Set: ImageKey(self: TreeView) = value
"""

    ImageList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Forms.ImageList that contains the System.Drawing.Image objects that are used by the tree nodes.

Get: ImageList(self: TreeView) -> ImageList

Set: ImageList(self: TreeView) = value
"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IME mode of a control.

"""

    Indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance to indent each child tree node level.

Get: Indent(self: TreeView) -> int

Set: Indent(self: TreeView) = value
"""

    ItemHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of each tree node in the tree view control.

Get: ItemHeight(self: TreeView) -> int

Set: ItemHeight(self: TreeView) = value
"""

    LabelEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the label text of the tree nodes can be edited.

Get: LabelEdit(self: TreeView) -> bool

Set: LabelEdit(self: TreeView) = value
"""

    LineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the lines connecting the nodes of the System.Windows.Forms.TreeView control.

Get: LineColor(self: TreeView) -> Color

Set: LineColor(self: TreeView) = value
"""

    Nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of tree nodes that are assigned to the tree view control.

Get: Nodes(self: TreeView) -> TreeNodeCollection

"""

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the spacing between the System.Windows.Forms.TreeView control's contents and its edges.

Get: Padding(self: TreeView) -> Padding

Set: Padding(self: TreeView) = value
"""

    PathSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the delimiter string that the tree node path uses.

Get: PathSeparator(self: TreeView) -> str

Set: PathSeparator(self: TreeView) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is now obsolete.

"""

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control redraws itself when resized.

"""

    RightToLeftLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Forms.TreeView should be laid out from right-to-left.

Get: RightToLeftLayout(self: TreeView) -> bool

Set: RightToLeftLayout(self: TreeView) = value
"""

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines the scaling of child controls.

"""

    Scrollable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the tree view control displays scroll bars when they are needed.

Get: Scrollable(self: TreeView) -> bool

Set: Scrollable(self: TreeView) = value
"""

    SelectedImageIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image list index value of the image that is displayed when a tree node is selected.

Get: SelectedImageIndex(self: TreeView) -> int

Set: SelectedImageIndex(self: TreeView) = value
"""

    SelectedImageKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key of the default image shown when a System.Windows.Forms.TreeNode is in a selected state.

Get: SelectedImageKey(self: TreeView) -> str

Set: SelectedImageKey(self: TreeView) = value
"""

    SelectedNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tree node that is currently selected in the tree view control.

Get: SelectedNode(self: TreeView) -> TreeNode

Set: SelectedNode(self: TreeView) = value
"""

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the control should display focus rectangles.

"""

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

    ShowLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether lines are drawn between tree nodes in the tree view control.

Get: ShowLines(self: TreeView) -> bool

Set: ShowLines(self: TreeView) = value
"""

    ShowNodeToolTips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating ToolTips are shown when the mouse pointer hovers over a System.Windows.Forms.TreeNode.

Get: ShowNodeToolTips(self: TreeView) -> bool

Set: ShowNodeToolTips(self: TreeView) = value
"""

    ShowPlusMinus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether plus-sign (+) and minus-sign (-) buttons are displayed next to tree nodes that contain child tree nodes.

Get: ShowPlusMinus(self: TreeView) -> bool

Set: ShowPlusMinus(self: TreeView) = value
"""

    ShowRootLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether lines are drawn between the tree nodes that are at the root of the tree view.

Get: ShowRootLines(self: TreeView) -> bool

Set: ShowRootLines(self: TreeView) = value
"""

    Sorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the tree nodes in the tree view are sorted.

Get: Sorted(self: TreeView) -> bool

Set: Sorted(self: TreeView) = value
"""

    StateImageList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image list that is used to indicate the state of the System.Windows.Forms.TreeView and its nodes.

Get: StateImageList(self: TreeView) -> ImageList

Set: StateImageList(self: TreeView) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text of the System.Windows.Forms.TreeView.

Get: Text(self: TreeView) -> str

Set: Text(self: TreeView) = value
"""

    TopNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first fully-visible tree node in the tree view control.

Get: TopNode(self: TreeView) -> TreeNode

Set: TopNode(self: TreeView) = value
"""

    TreeViewNodeSorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the implementation of System.Collections.IComparer to perform a custom sort of the System.Windows.Forms.TreeView nodes.

Get: TreeViewNodeSorter(self: TreeView) -> IComparer

Set: TreeViewNodeSorter(self: TreeView) = value
"""

    VisibleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of tree nodes that can be fully visible in the tree view control.

Get: VisibleCount(self: TreeView) -> int

"""


    AfterCheck = None
    AfterCollapse = None
    AfterExpand = None
    AfterLabelEdit = None
    AfterSelect = None
    BackgroundImageChanged = None
    BackgroundImageLayoutChanged = None
    BeforeCheck = None
    BeforeCollapse = None
    BeforeExpand = None
    BeforeLabelEdit = None
    BeforeSelect = None
    DrawNode = None
    ItemDrag = None
    NodeMouseClick = None
    NodeMouseDoubleClick = None
    NodeMouseHover = None
    PaddingChanged = None
    Paint = None
    RightToLeftLayoutChanged = None
    TextChanged = None

