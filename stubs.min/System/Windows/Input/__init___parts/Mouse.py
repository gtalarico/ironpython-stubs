class Mouse(object):
    """ Represents the mouse device to a specific thread. """
    @staticmethod
    def AddGotMouseCaptureHandler(element, handler):
        """
        AddGotMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.GotMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddLostMouseCaptureHandler(element, handler):
        """
        AddLostMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.LostMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseDownHandler(element, handler):
        """
        AddMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseEnterHandler(element, handler):
        """
        AddMouseEnterHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseLeaveHandler(element, handler):
        """
        AddMouseLeaveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseMoveHandler(element, handler):
        """
        AddMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseUpHandler(element, handler):
        """
        AddMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddMouseWheelHandler(element, handler):
        """
        AddMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.MouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseDownHandler(element, handler):
        """
        AddPreviewMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseDownOutsideCapturedElementHandler(element, handler):
        """
        AddPreviewMouseDownOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseDownOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseMoveHandler(element, handler):
        """
        AddPreviewMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseUpHandler(element, handler):
        """
        AddPreviewMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseUpOutsideCapturedElementHandler(element, handler):
        """
        AddPreviewMouseUpOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseUpOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddPreviewMouseWheelHandler(element, handler):
        """
        AddPreviewMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.PreviewMouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def AddQueryCursorHandler(element, handler):
        """
        AddQueryCursorHandler(element: DependencyObject, handler: QueryCursorEventHandler)
            Adds a handler for the System.Windows.Input.Mouse.QueryCursor�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def Capture(element, captureMode=None):
        """
        Capture(element: IInputElement, captureMode: CaptureMode) -> bool
        
            Captures mouse input to the specified element using the specified System.Windows.Input.CaptureMode.
        
            element: The element to capture the mouse.
            captureMode: The capture policy to use.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        Capture(element: IInputElement) -> bool
        
            Captures mouse input to the specified element.
        
            element: The element to capture the mouse.
            Returns: true if the element was able to capture the mouse; otherwise, false.
        """
        pass

    @staticmethod
    def GetIntermediatePoints(relativeTo, points):
        """
        GetIntermediatePoints(relativeTo: IInputElement, points: Array[Point]) -> int
        
            Retrieves up to 64 previous coordinates of the mouse pointer since the last mouse move event.
        
            relativeTo: The elements points are in relation to.
            points: An array of objects.
            Returns: The number of points returned.
        """
        pass

    @staticmethod
    def GetPosition(relativeTo):
        """
        GetPosition(relativeTo: IInputElement) -> Point
        
            Gets the position of the mouse relative to a specified element.
        
            relativeTo: The coordinate space in which to calculate the position of the mouse.
            Returns: The position of the mouse relative to the parameter relativeTo.
        """
        pass

    @staticmethod
    def RemoveGotMouseCaptureHandler(element, handler):
        """
        RemoveGotMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.GotMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveLostMouseCaptureHandler(element, handler):
        """
        RemoveLostMouseCaptureHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.LostMouseCapture�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseDownHandler(element, handler):
        """
        RemoveMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseEnterHandler(element, handler):
        """
        RemoveMouseEnterHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseEnter�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseLeaveHandler(element, handler):
        """
        RemoveMouseLeaveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseLeave�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseMoveHandler(element, handler):
        """
        RemoveMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseUpHandler(element, handler):
        """
        RemoveMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveMouseWheelHandler(element, handler):
        """
        RemoveMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.MouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseDownHandler(element, handler):
        """
        RemovePreviewMouseDownHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseDown�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseDownOutsideCapturedElementHandler(element, handler):
        """
        RemovePreviewMouseDownOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseDownOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseMoveHandler(element, handler):
        """
        RemovePreviewMouseMoveHandler(element: DependencyObject, handler: MouseEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseMove�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseUpHandler(element, handler):
        """
        RemovePreviewMouseUpHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseUp�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseUpOutsideCapturedElementHandler(element, handler):
        """
        RemovePreviewMouseUpOutsideCapturedElementHandler(element: DependencyObject, handler: MouseButtonEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseUpOutsideCapturedElement�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemovePreviewMouseWheelHandler(element, handler):
        """
        RemovePreviewMouseWheelHandler(element: DependencyObject, handler: MouseWheelEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.PreviewMouseWheel�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def RemoveQueryCursorHandler(element, handler):
        """
        RemoveQueryCursorHandler(element: DependencyObject, handler: QueryCursorEventHandler)
            Removes a handler for the System.Windows.Input.Mouse.QueryCursor�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler.
        """
        pass

    @staticmethod
    def SetCursor(cursor):
        """
        SetCursor(cursor: Cursor) -> bool
        
            Sets the mouse pointer to the specified System.Windows.Input.Cursor.
        
            cursor: The cursor to set the mouse pointer to.
            Returns: true, if the cursor was set; otherwise, false.
        """
        pass

    @staticmethod
    def Synchronize():
        """
        Synchronize()
            Forces the mouse to resynchronize.
        """
        pass

    @staticmethod
    def UpdateCursor():
        """
        UpdateCursor()
            Forces the mouse cursor to be updated.
        """
        pass

    Captured = None
    DirectlyOver = None
    GotMouseCaptureEvent = None
    LeftButton = None
    LostMouseCaptureEvent = None
    MiddleButton = None
    MouseDownEvent = None
    MouseEnterEvent = None
    MouseLeaveEvent = None
    MouseMoveEvent = None
    MouseUpEvent = None
    MouseWheelDeltaForOneLine = 120
    MouseWheelEvent = None
    OverrideCursor = None
    PreviewMouseDownEvent = None
    PreviewMouseDownOutsideCapturedElementEvent = None
    PreviewMouseMoveEvent = None
    PreviewMouseUpEvent = None
    PreviewMouseUpOutsideCapturedElementEvent = None
    PreviewMouseWheelEvent = None
    PrimaryDevice = None
    QueryCursorEvent = None
    RightButton = None
    XButton1 = None
    XButton2 = None
    __all__ = [
        'AddGotMouseCaptureHandler',
        'AddLostMouseCaptureHandler',
        'AddMouseDownHandler',
        'AddMouseEnterHandler',
        'AddMouseLeaveHandler',
        'AddMouseMoveHandler',
        'AddMouseUpHandler',
        'AddMouseWheelHandler',
        'AddPreviewMouseDownHandler',
        'AddPreviewMouseDownOutsideCapturedElementHandler',
        'AddPreviewMouseMoveHandler',
        'AddPreviewMouseUpHandler',
        'AddPreviewMouseUpOutsideCapturedElementHandler',
        'AddPreviewMouseWheelHandler',
        'AddQueryCursorHandler',
        'Capture',
        'GetIntermediatePoints',
        'GetPosition',
        'GotMouseCaptureEvent',
        'LostMouseCaptureEvent',
        'MouseDownEvent',
        'MouseEnterEvent',
        'MouseLeaveEvent',
        'MouseMoveEvent',
        'MouseUpEvent',
        'MouseWheelDeltaForOneLine',
        'MouseWheelEvent',
        'PreviewMouseDownEvent',
        'PreviewMouseDownOutsideCapturedElementEvent',
        'PreviewMouseMoveEvent',
        'PreviewMouseUpEvent',
        'PreviewMouseUpOutsideCapturedElementEvent',
        'PreviewMouseWheelEvent',
        'QueryCursorEvent',
        'RemoveGotMouseCaptureHandler',
        'RemoveLostMouseCaptureHandler',
        'RemoveMouseDownHandler',
        'RemoveMouseEnterHandler',
        'RemoveMouseLeaveHandler',
        'RemoveMouseMoveHandler',
        'RemoveMouseUpHandler',
        'RemoveMouseWheelHandler',
        'RemovePreviewMouseDownHandler',
        'RemovePreviewMouseDownOutsideCapturedElementHandler',
        'RemovePreviewMouseMoveHandler',
        'RemovePreviewMouseUpHandler',
        'RemovePreviewMouseUpOutsideCapturedElementHandler',
        'RemovePreviewMouseWheelHandler',
        'RemoveQueryCursorHandler',
        'SetCursor',
        'Synchronize',
        'UpdateCursor',
    ]

