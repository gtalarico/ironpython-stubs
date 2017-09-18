# encoding: utf-8
# module System.Windows.Input.StylusPlugIns calls itself StylusPlugIns
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class StylusPlugIn(object):
    """ Represents a plug-in that can be added to a control's System.Windows.UIElement.StylusPlugIns property. """
    def OnAdded(self, *args): #cannot find CLR method
        """
        OnAdded(self: StylusPlugIn)
            Occurs when the System.Windows.Input.StylusPlugIns.StylusPlugIn is added to an element.
        """
        pass

    def OnEnabledChanged(self, *args): #cannot find CLR method
        """
        OnEnabledChanged(self: StylusPlugIn)
            Occurs when the System.Windows.Input.StylusPlugIns.StylusPlugIn.Enabled property changes.
        """
        pass

    def OnIsActiveForInputChanged(self, *args): #cannot find CLR method
        """
        OnIsActiveForInputChanged(self: StylusPlugIn)
            Occurs when the System.Windows.Input.StylusPlugIns.StylusPlugIn.IsActiveForInput property 
             changes.
        """
        pass

    def OnRemoved(self, *args): #cannot find CLR method
        """
        OnRemoved(self: StylusPlugIn)
            Occurs when the System.Windows.Input.StylusPlugIns.StylusPlugIn is removed from an element.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: StylusPlugIn, rawStylusInput: RawStylusInput)
            Occurs on a thread in the pen thread pool when the tablet pen touches the digitizer.
        
            rawStylusInput: A System.Windows.Input.StylusPlugIns.RawStylusInput that contains information about input from 
             the pen.
        """
        pass

    def OnStylusDownProcessed(self, *args): #cannot find CLR method
        """
        OnStylusDownProcessed(self: StylusPlugIn, callbackData: object, targetVerified: bool)
            Occurs on the application UI (user interface) thread when the tablet pen touches the digitizer.
        
            callbackData: The object that the application passed to the 
             System.Windows.Input.StylusPlugIns.RawStylusInput.NotifyWhenProcessed(System.Object) method.
        
            targetVerified: true if the pen's input was correctly routed to the 
             System.Windows.Input.StylusPlugIns.StylusPlugIn; otherwise, false.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: StylusPlugIn, rawStylusInput: RawStylusInput, confirmed: bool)
            Occurs on a pen thread when the cursor enters the bounds of an element.
        
            rawStylusInput: A System.Windows.Input.StylusPlugIns.RawStylusInput that contains information about input from 
             the pen.
        
            confirmed: true if the pen actually entered the bounds of the element; otherwise, false.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: StylusPlugIn, rawStylusInput: RawStylusInput, confirmed: bool)
            Occurs on a pen thread when the cursor leaves the bounds of an element.
        
            rawStylusInput: A System.Windows.Input.StylusPlugIns.RawStylusInput that contains information about input from 
             the pen.
        
            confirmed: true if the pen actually left the bounds of the element; otherwise, false.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: StylusPlugIn, rawStylusInput: RawStylusInput)
            Occurs on a pen thread when the tablet pen moves on the digitizer.
        
            rawStylusInput: A System.Windows.Input.StylusPlugIns.RawStylusInput that contains information about input from 
             the pen.
        """
        pass

    def OnStylusMoveProcessed(self, *args): #cannot find CLR method
        """
        OnStylusMoveProcessed(self: StylusPlugIn, callbackData: object, targetVerified: bool)
            Occurs on the application UI (user interface) thread when the tablet pen moves on the digitizer.
        
            callbackData: The object that the application passed to the 
             System.Windows.Input.StylusPlugIns.RawStylusInput.NotifyWhenProcessed(System.Object) method.
        
            targetVerified: true if the pen's input was correctly routed to the 
             System.Windows.Input.StylusPlugIns.StylusPlugIn; otherwise, false.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: StylusPlugIn, rawStylusInput: RawStylusInput)
            Occurs on a pen thread when the user lifts the tablet pen from the digitizer.
        
            rawStylusInput: A System.Windows.Input.StylusPlugIns.RawStylusInput that contains information about input from 
             the pen.
        """
        pass

    def OnStylusUpProcessed(self, *args): #cannot find CLR method
        """
        OnStylusUpProcessed(self: StylusPlugIn, callbackData: object, targetVerified: bool)
            Occurs on the application UI (user interface) thread when the user lifts the tablet pen from the 
             digitizer.
        
        
            callbackData: The object that the application passed to the 
             System.Windows.Input.StylusPlugIns.RawStylusInput.NotifyWhenProcessed(System.Object) method.
        
            targetVerified: true if the pen's input was correctly routed to the 
             System.Windows.Input.StylusPlugIns.StylusPlugIn; otherwise, false.
        """
        pass

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.UIElement to which the System.Windows.Input.StylusPlugIns.StylusPlugIn is attached.

Get: Element(self: StylusPlugIn) -> UIElement

"""

    ElementBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cached bounds of the element.

Get: ElementBounds(self: StylusPlugIn) -> Rect

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the System.Windows.Input.StylusPlugIns.StylusPlugIn is active.

Get: Enabled(self: StylusPlugIn) -> bool

Set: Enabled(self: StylusPlugIn) = value
"""

    IsActiveForInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the System.Windows.Input.StylusPlugIns.StylusPlugIn is able to accept input.

Get: IsActiveForInput(self: StylusPlugIn) -> bool

"""



class DynamicRenderer(StylusPlugIn):
    """
    Draws ink on a surface as the user moves the tablet pen.
    
    DynamicRenderer()
    """
    def GetDispatcher(self, *args): #cannot find CLR method
        """
        GetDispatcher(self: DynamicRenderer) -> Dispatcher
        
            Returns a System.Windows.Threading.Dispatcher for the rendering thread.
            Returns: A System.Windows.Threading.Dispatcher for the rendering thread.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: DynamicRenderer, drawingContext: DrawingContext, stylusPoints: StylusPointCollection, geometry: Geometry, fillBrush: Brush)
            Draws the ink in real-time so it appears to "flow" from the tablet pen or other pointing device.
        
            drawingContext: The System.Windows.Media.DrawingContext object onto which the stroke is rendered.
            stylusPoints: The System.Windows.Input.StylusPointCollection that represents the segment of the stroke to draw.
            geometry: A System.Windows.Media.Geometry that represents the path of the mouse pointer.
            fillBrush: A Brush that specifies the appearance of the current stroke.
        """
        pass

    def OnDrawingAttributesReplaced(self, *args): #cannot find CLR method
        """
        OnDrawingAttributesReplaced(self: DynamicRenderer)
            Occurs when the System.Windows.Input.StylusPlugIns.DynamicRenderer.DrawingAttributes property 
             changes.
        """
        pass

    def Reset(self, stylusDevice, stylusPoints):
        """
        Reset(self: DynamicRenderer, stylusDevice: StylusDevice, stylusPoints: StylusPointCollection)
            Clears rendering on the current stroke and redraws it.
        
            stylusDevice: The current stylus device.
            stylusPoints: The stylus points to be redrawn.
        """
        pass

    DrawingAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Ink.DrawingAttributes that specifies the appearance of the rendered ink.

Get: DrawingAttributes(self: DynamicRenderer) -> DrawingAttributes

Set: DrawingAttributes(self: DynamicRenderer) = value
"""

    RootVisual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root visual for the System.Windows.Input.StylusPlugIns.DynamicRenderer.

Get: RootVisual(self: DynamicRenderer) -> Visual

"""



class RawStylusInput(object):
    """ Provides information about input from a System.Windows.Input.StylusDevice to a System.Windows.Input.StylusPlugIns.StylusPlugIn. """
    def GetStylusPoints(self):
        """
        GetStylusPoints(self: RawStylusInput) -> StylusPointCollection
        
            Gets the stylus points that are collected from the stylus.
            Returns: The stylus points that are collected from the stylus.
        """
        pass

    def NotifyWhenProcessed(self, callbackData):
        """
        NotifyWhenProcessed(self: RawStylusInput, callbackData: object)
            Subscribes to the application thread's corresponding stylus methods.
        
            callbackData: The data to pass to the application thread.
        """
        pass

    def SetStylusPoints(self, stylusPoints):
        """
        SetStylusPoints(self: RawStylusInput, stylusPoints: StylusPointCollection)
            Sets the stylus points that are passed to the application thread.
        
            stylusPoints: The stylus points to pass to the application thread.
        """
        pass

    StylusDeviceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of the current stylus device.

Get: StylusDeviceId(self: RawStylusInput) -> int

"""

    TabletDeviceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of the current tablet device.

Get: TabletDeviceId(self: RawStylusInput) -> int

"""

    Timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time at which the input occurred.

Get: Timestamp(self: RawStylusInput) -> int

"""



class StylusPlugInCollection(Collection[StylusPlugIn], IList[StylusPlugIn], ICollection[StylusPlugIn], IEnumerable[StylusPlugIn], IEnumerable, IList, ICollection, IReadOnlyList[StylusPlugIn], IReadOnlyCollection[StylusPlugIn]):
    """ Represent a collection of System.Windows.Input.StylusPlugIns.StylusPlugIn objects. """
    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: StylusPlugInCollection) """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: StylusPlugInCollection, index: int, plugIn: StylusPlugIn) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: StylusPlugInCollection, index: int) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: StylusPlugInCollection, index: int, plugIn: StylusPlugIn) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""



