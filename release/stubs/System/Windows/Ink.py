# encoding: utf-8
# module System.Windows.Ink calls itself Ink
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ApplicationGesture(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the available application-specific gesture.
    
    enum ApplicationGesture, values: AllGestures (0), ArrowDown (61497), ArrowLeft (61498), ArrowRight (61499), ArrowUp (61496), Check (61445), ChevronDown (61489), ChevronLeft (61490), ChevronRight (61491), ChevronUp (61488), Circle (61472), Curlicue (61456), DoubleCircle (61473), DoubleCurlicue (61457), DoubleTap (61681), Down (61529), DownLeft (61546), DownLeftLong (61542), DownRight (61547), DownRightLong (61543), DownUp (61537), Exclamation (61604), Left (61530), LeftDown (61549), LeftRight (61538), LeftUp (61548), NoGesture (61440), Right (61531), RightDown (61551), RightLeft (61539), RightUp (61550), ScratchOut (61441), SemicircleLeft (61480), SemicircleRight (61481), Square (61443), Star (61444), Tap (61680), Triangle (61442), Up (61528), UpDown (61536), UpLeft (61544), UpLeftLong (61540), UpRight (61545), UpRightLong (61541)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllGestures = None
    ArrowDown = None
    ArrowLeft = None
    ArrowRight = None
    ArrowUp = None
    Check = None
    ChevronDown = None
    ChevronLeft = None
    ChevronRight = None
    ChevronUp = None
    Circle = None
    Curlicue = None
    DoubleCircle = None
    DoubleCurlicue = None
    DoubleTap = None
    Down = None
    DownLeft = None
    DownLeftLong = None
    DownRight = None
    DownRightLong = None
    DownUp = None
    Exclamation = None
    Left = None
    LeftDown = None
    LeftRight = None
    LeftUp = None
    NoGesture = None
    Right = None
    RightDown = None
    RightLeft = None
    RightUp = None
    ScratchOut = None
    SemicircleLeft = None
    SemicircleRight = None
    Square = None
    Star = None
    Tap = None
    Triangle = None
    Up = None
    UpDown = None
    UpLeft = None
    UpLeftLong = None
    UpRight = None
    UpRightLong = None
    value__ = None


class DrawingAttributeIds(object):
    """ Contains a set of GUIDs that identify the properties in the System.Windows.Ink.DrawingAttributes class. """
    Color = None
    DrawingFlags = None
    IsHighlighter = None
    StylusHeight = None
    StylusTip = None
    StylusTipTransform = None
    StylusWidth = None
    __all__ = [
        'Color',
        'DrawingFlags',
        'IsHighlighter',
        'StylusHeight',
        'StylusTip',
        'StylusTipTransform',
        'StylusWidth',
    ]


class DrawingAttributes(object, INotifyPropertyChanged):
    """
    Specifies the appearance of a System.Windows.Ink.Stroke
    
    DrawingAttributes()
    """
    def AddPropertyData(self, propertyDataId, propertyData):
        """
        AddPropertyData(self: DrawingAttributes, propertyDataId: Guid, propertyData: object)
            Adds a custom property to the System.Windows.Ink.DrawingAttributes object.
        
            propertyDataId: The System.Guid to associate with the custom property.
            propertyData: The value of the custom property. propertyData must be of type System.Char, System.Byte, 
             System.Int16, System.UInt16, System.Int32, System.UInt32, System.Int64, System.UInt64, 
             System.Single, System.Double, System.DateTime, System.Boolean, System.String, System.Decimal or 
             an array of these data types; however it cannot be an array of type System.String.
        """
        pass

    def Clone(self):
        """
        Clone(self: DrawingAttributes) -> DrawingAttributes
        
            Copies the System.Windows.Ink.DrawingAttributes object.
            Returns: A copy of the System.Windows.Ink.DrawingAttributes object.
        """
        pass

    def ContainsPropertyData(self, propertyDataId):
        """
        ContainsPropertyData(self: DrawingAttributes, propertyDataId: Guid) -> bool
        
            Returns a value that indicates whether the specified property data identifier is in the 
             System.Windows.Ink.DrawingAttributes object.
        
        
            propertyDataId: The System.Guid to locate in the System.Windows.Ink.DrawingAttributes object .
            Returns: true if the specified property data identifier is in the System.Windows.Ink.DrawingAttributes 
             object; otherwise, false.
        """
        pass

    def Equals(self, o):
        """
        Equals(self: DrawingAttributes, o: object) -> bool
        
            Determines whether the specified System.Windows.Ink.DrawingAttributes object is equal to the 
             current System.Windows.Ink.DrawingAttributes object.
        
        
            o: The System.Windows.Ink.DrawingAttributes object to compare to the current 
             System.Windows.Ink.DrawingAttributes object.
        
            Returns: true if the objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DrawingAttributes) -> int """
        pass

    def GetPropertyData(self, propertyDataId):
        """
        GetPropertyData(self: DrawingAttributes, propertyDataId: Guid) -> object
        
            Gets the value of the custom property associated with the specified System.Guid.
        
            propertyDataId: The System.Guid associated with the custom property to get.
            Returns: The value of the custom property associated with the specified System.Guid.
        """
        pass

    def GetPropertyDataIds(self):
        """
        GetPropertyDataIds(self: DrawingAttributes) -> Array[Guid]
        
            Returns the GUIDs of any custom properties associated with the 
             System.Windows.Ink.StrokeCollection.
        
            Returns: An array of type System.Guid that represents the property data identifiers.
        """
        pass

    def OnAttributeChanged(self, *args): #cannot find CLR method
        """
        OnAttributeChanged(self: DrawingAttributes, e: PropertyDataChangedEventArgs)
            Raises the System.Windows.Ink.DrawingAttributes.AttributeChanged event.
        
            e: A System.Windows.Ink.PropertyDataChangedEventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DrawingAttributes, e: PropertyChangedEventArgs)
            Occurs when any System.Windows.Ink.DrawingAttributes property changes.
        
            e: EventArgs
        """
        pass

    def OnPropertyDataChanged(self, *args): #cannot find CLR method
        """
        OnPropertyDataChanged(self: DrawingAttributes, e: PropertyDataChangedEventArgs)
            Raises the System.Windows.Ink.DrawingAttributes.PropertyDataChanged event.
        
            e: A System.Windows.Ink.PropertyDataChangedEventArgs that contains the event data.
        """
        pass

    def RemovePropertyData(self, propertyDataId):
        """
        RemovePropertyData(self: DrawingAttributes, propertyDataId: Guid)
            Removes the custom property associated with the specified System.Guid.
        
            propertyDataId: The System.Guid associated with the custom property to remove.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of a System.Windows.Ink.Stroke.

Get: Color(self: DrawingAttributes) -> Color

Set: Color(self: DrawingAttributes) = value
"""

    FitToCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether Bezier smoothing is used to render the System.Windows.Ink.Stroke.

Get: FitToCurve(self: DrawingAttributes) -> bool

Set: FitToCurve(self: DrawingAttributes) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the stylus used to draw the System.Windows.Ink.Stroke.

Get: Height(self: DrawingAttributes) -> float

Set: Height(self: DrawingAttributes) = value
"""

    IgnorePressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the thickness of a rendered System.Windows.Ink.Stroke changes according the amount of pressure applied.

Get: IgnorePressure(self: DrawingAttributes) -> bool

Set: IgnorePressure(self: DrawingAttributes) = value
"""

    IsHighlighter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Ink.Stroke looks like a highlighter.

Get: IsHighlighter(self: DrawingAttributes) -> bool

Set: IsHighlighter(self: DrawingAttributes) = value
"""

    StylusTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the shape of the stylus used to draw the System.Windows.Ink.Stroke.

Get: StylusTip(self: DrawingAttributes) -> StylusTip

Set: StylusTip(self: DrawingAttributes) = value
"""

    StylusTipTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Matrix that specifies the transformation to perform on the stylus' tip.

Get: StylusTipTransform(self: DrawingAttributes) -> Matrix

Set: StylusTipTransform(self: DrawingAttributes) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the stylus used to draw the System.Windows.Ink.Stroke.

Get: Width(self: DrawingAttributes) -> float

Set: Width(self: DrawingAttributes) = value
"""


    AttributeChanged = None
    MaxHeight = 162329.46141732301
    MaxWidth = 162329.46141732301
    MinHeight = 3.77952755905512e-05
    MinWidth = 3.77952755905512e-05
    PropertyDataChanged = None


class DrawingAttributesReplacedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Controls.InkCanvas.DefaultDrawingAttributesReplaced event.
    
    DrawingAttributesReplacedEventArgs(newDrawingAttributes: DrawingAttributes, previousDrawingAttributes: DrawingAttributes)
    """
    @staticmethod # known case of __new__
    def __new__(self, newDrawingAttributes, previousDrawingAttributes):
        """ __new__(cls: type, newDrawingAttributes: DrawingAttributes, previousDrawingAttributes: DrawingAttributes) """
        pass

    NewDrawingAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new System.Windows.Ink.DrawingAttributes.

Get: NewDrawingAttributes(self: DrawingAttributesReplacedEventArgs) -> DrawingAttributes

"""

    PreviousDrawingAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the old System.Windows.Ink.DrawingAttributes.

Get: PreviousDrawingAttributes(self: DrawingAttributesReplacedEventArgs) -> DrawingAttributes

"""



class DrawingAttributesReplacedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Controls.InkCanvas.DefaultDrawingAttributesReplaced event of an System.Windows.Controls.InkCanvas.
    
    DrawingAttributesReplacedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DrawingAttributesReplacedEventHandler, sender: object, e: DrawingAttributesReplacedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DrawingAttributesReplacedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DrawingAttributesReplacedEventHandler, sender: object, e: DrawingAttributesReplacedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StylusShape(object):
    """ Represents the tip of a stylus. """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the stylus.

Get: Height(self: StylusShape) -> float

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the angle of the stylus.

Get: Rotation(self: StylusShape) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the stylus.

Get: Width(self: StylusShape) -> float

"""



class EllipseStylusShape(StylusShape):
    """
    Represents a stylus tip shaped like an ellipse.
    
    EllipseStylusShape(width: float, height: float)
    EllipseStylusShape(width: float, height: float, rotation: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, width, height, rotation=None):
        """
        __new__(cls: type, width: float, height: float)
        __new__(cls: type, width: float, height: float, rotation: float)
        """
        pass


class GestureRecognitionResult(object):
    """ Contains information about an ink gesture. """
    ApplicationGesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the recognized ink gesture.

Get: ApplicationGesture(self: GestureRecognitionResult) -> ApplicationGesture

"""

    RecognitionConfidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level of confidence that the System.Windows.Ink.GestureRecognizer has in the recognition of the gesture.

Get: RecognitionConfidence(self: GestureRecognitionResult) -> RecognitionConfidence

"""



class GestureRecognizer(DependencyObject, IDisposable):
    """
    Recognizes ink gestures.
    
    GestureRecognizer()
    GestureRecognizer(enabledApplicationGestures: IEnumerable[ApplicationGesture])
    """
    def Dispose(self):
        """
        Dispose(self: GestureRecognizer)
            Releases all resources used by the System.Windows.Ink.GestureRecognizer.
        """
        pass

    def GetEnabledGestures(self):
        """
        GetEnabledGestures(self: GestureRecognizer) -> ReadOnlyCollection[ApplicationGesture]
        
            Gets the gestures that the System.Windows.Ink.GestureRecognizer recognizes.
            Returns: An array of type System.Windows.Ink.ApplicationGesture that contains gestures the 
             System.Windows.Ink.GestureRecognizer is set to recognize.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.DependencyObject has been updated. The specific dependency property that changed 
             is reported in the event data.
        
        
            e: Event data that will contain the dependency property identifier of interest, the property 
             metadata for the type, and old and new values.
        """
        pass

    def Recognize(self, strokes):
        """
        Recognize(self: GestureRecognizer, strokes: StrokeCollection) -> ReadOnlyCollection[GestureRecognitionResult]
        
            Looks for gestures in the specified System.Windows.Ink.StrokeCollection.
        
            strokes: The System.Windows.Ink.StrokeCollection to search for gestures.
            Returns: An array of type System.Windows.Ink.GestureRecognitionResult that contains application gestures 
             that the System.Windows.Ink.GestureRecognizer recognized.
        """
        pass

    def SetEnabledGestures(self, applicationGestures):
        """ SetEnabledGestures(self: GestureRecognizer, applicationGestures: IEnumerable[ApplicationGesture]) """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
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

    @staticmethod # known case of __new__
    def __new__(self, enabledApplicationGestures=None):
        """
        __new__(cls: type)
        __new__(cls: type, enabledApplicationGestures: IEnumerable[ApplicationGesture])
        """
        pass

    IsRecognizerAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean that indicates whether the gesture recognizer is available on the user's system.

Get: IsRecognizerAvailable(self: GestureRecognizer) -> bool

"""



class IncrementalHitTester(object):
    """ Dynamically performs hit testing on a System.Windows.Ink.Stroke. """
    def AddPoint(self, point):
        """
        AddPoint(self: IncrementalHitTester, point: Point)
            Adds a System.Windows.Point to the System.Windows.Ink.IncrementalHitTester.
        
            point: The System.Windows.Point to add to the System.Windows.Ink.IncrementalHitTester.
        """
        pass

    def AddPoints(self, *__args):
        """
        AddPoints(self: IncrementalHitTester, stylusPoints: StylusPointCollection)
            Adds the specified System.Windows.Input.StylusPoint objects to the 
             System.Windows.Ink.IncrementalHitTester.
        
        
            stylusPoints: A collection of System.Windows.Input.StylusPoint objects to add to the 
             System.Windows.Ink.IncrementalHitTester.
        
        AddPoints(self: IncrementalHitTester, points: IEnumerable[Point])
        """
        pass

    def AddPointsCore(self, *args): #cannot find CLR method
        """ AddPointsCore(self: IncrementalHitTester, points: IEnumerable[Point]) """
        pass

    def EndHitTesting(self):
        """
        EndHitTesting(self: IncrementalHitTester)
            Releases resources used by the System.Windows.Ink.IncrementalHitTester.
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the System.Windows.Ink.IncrementalHitTester is hit testing.

Get: IsValid(self: IncrementalHitTester) -> bool

"""



class IncrementalLassoHitTester(IncrementalHitTester):
    """ Dynamically hit tests a System.Windows.Ink.Stroke with a lasso. """
    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: IncrementalLassoHitTester, eventArgs: LassoSelectionChangedEventArgs)
            Raises the System.Windows.Ink.IncrementalLassoHitTester.SelectionChanged event.
        
            eventArgs: Event data.
        """
        pass

    SelectionChanged = None


class IncrementalStrokeHitTester(IncrementalHitTester):
    """ Dynamically hit tests a stroke with an eraser path. """
    def OnStrokeHit(self, *args): #cannot find CLR method
        """
        OnStrokeHit(self: IncrementalStrokeHitTester, eventArgs: StrokeHitEventArgs)
            Raises the System.Windows.Ink.IncrementalStrokeHitTester.StrokeHit event.
        
            eventArgs: Event data.
        """
        pass

    StrokeHit = None


class LassoSelectionChangedEventArgs(EventArgs):
    """ Provides data for the System.Windows.Ink.IncrementalLassoHitTester.SelectionChanged event. """
    DeselectedStrokes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the strokes that have been removed from lasso path since the last time the System.Windows.Ink.IncrementalLassoHitTester.SelectionChanged event was raised.

Get: DeselectedStrokes(self: LassoSelectionChangedEventArgs) -> StrokeCollection

"""

    SelectedStrokes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the strokes that have been surrounded by the lasso path since the last time the System.Windows.Ink.IncrementalLassoHitTester.SelectionChanged event was raised.

Get: SelectedStrokes(self: LassoSelectionChangedEventArgs) -> StrokeCollection

"""



class LassoSelectionChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Ink.IncrementalLassoHitTester.SelectionChanged event of a System.Windows.Ink.IncrementalLassoHitTester.
    
    LassoSelectionChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: LassoSelectionChangedEventHandler, sender: object, e: LassoSelectionChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LassoSelectionChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LassoSelectionChangedEventHandler, sender: object, e: LassoSelectionChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class PropertyDataChangedEventArgs(EventArgs):
    """
    Provides data for the PropertyDataChanged event.
    
    PropertyDataChangedEventArgs(propertyGuid: Guid, newValue: object, previousValue: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, propertyGuid, newValue, previousValue):
        """ __new__(cls: type, propertyGuid: Guid, newValue: object, previousValue: object) """
        pass

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new custom property object.

Get: NewValue(self: PropertyDataChangedEventArgs) -> object

"""

    PreviousValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the previous custom property object.

Get: PreviousValue(self: PropertyDataChangedEventArgs) -> object

"""

    PropertyGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Guid of the custom property which changed.

Get: PropertyGuid(self: PropertyDataChangedEventArgs) -> Guid

"""



class PropertyDataChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the PropertyDataChanged event.
    
    PropertyDataChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PropertyDataChangedEventHandler, sender: object, e: PropertyDataChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PropertyDataChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PropertyDataChangedEventHandler, sender: object, e: PropertyDataChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class RecognitionConfidence(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the confidence level that the System.Windows.Ink.GestureRecognizer determines for a particular ink gesture.
    
    enum RecognitionConfidence, values: Intermediate (1), Poor (2), Strong (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Intermediate = None
    Poor = None
    Strong = None
    value__ = None


class RectangleStylusShape(StylusShape):
    """
    Represents a rectangular stylus tip.
    
    RectangleStylusShape(width: float, height: float)
    RectangleStylusShape(width: float, height: float, rotation: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, width, height, rotation=None):
        """
        __new__(cls: type, width: float, height: float)
        __new__(cls: type, width: float, height: float, rotation: float)
        """
        pass


class Stroke(object, INotifyPropertyChanged):
    """
    Represents a single ink stroke.
    
    Stroke(stylusPoints: StylusPointCollection)
    Stroke(stylusPoints: StylusPointCollection, drawingAttributes: DrawingAttributes)
    """
    def AddPropertyData(self, propertyDataId, propertyData):
        """
        AddPropertyData(self: Stroke, propertyDataId: Guid, propertyData: object)
            Adds a custom property to the System.Windows.Ink.Stroke object.
        
            propertyDataId: The unique identifier for the property.
            propertyData: The value of the custom property. propertyData must be of type System.Char, 
             System.Byte,System.Int16,,System.UInt16, System.Int32, System.UInt32, System.Int64, 
             System.UInt64, System.Single, System.Double, System.DateTime, System.Boolean, System.String, 
             System.Decimal  or an array of these data types, except System.String, which is not allowed.
        """
        pass

    def Clone(self):
        """
        Clone(self: Stroke) -> Stroke
        
            Returns a deep copy of the existing System.Windows.Ink.Stroke object.
            Returns: The new System.Windows.Ink.Stroke object.
        """
        pass

    def ContainsPropertyData(self, propertyDataId):
        """
        ContainsPropertyData(self: Stroke, propertyDataId: Guid) -> bool
        
            Returns a value that indicates whether the System.Windows.Ink.Stroke object contains the 
             specified custom property.
        
        
            propertyDataId: The unique identifier for the property.
            Returns: Returns true if the custom property exists; otherwise, returns false.
        """
        pass

    def Draw(self, *__args):
        """
        Draw(self: Stroke, drawingContext: DrawingContext, drawingAttributes: DrawingAttributes)
            Renders the System.Windows.Ink.Stroke object based upon the specified 
             System.Windows.Media.DrawingContext and Microsoft.Ink.DrawingAttributes.
        
        
            drawingContext: The System.Windows.Media.DrawingContext object onto which the stroke will be rendered.
            drawingAttributes: The Microsoft.Ink.DrawingAttributes object defining the attributes of the stroke that is drawn.
        Draw(self: Stroke, context: DrawingContext)
            Renders the System.Windows.Ink.Stroke object based upon the specified 
             System.Windows.Media.DrawingContext.
        """
        pass

    def DrawCore(self, *args): #cannot find CLR method
        """
        DrawCore(self: Stroke, drawingContext: DrawingContext, drawingAttributes: DrawingAttributes)
            Renders the System.Windows.Ink.Stroke on the specified System.Windows.Media.DrawingContext using 
             the specified Microsoft.Ink.DrawingAttributes.
        
        
            drawingContext: The System.Windows.Media.DrawingContext object onto which the stroke will be rendered.
            drawingAttributes: The Microsoft.Ink.DrawingAttributes object defining the attributes of the stroke that is drawn.
        """
        pass

    def GetBezierStylusPoints(self):
        """
        GetBezierStylusPoints(self: Stroke) -> StylusPointCollection
        
            Returns the stylus points the System.Windows.Ink.Stroke uses when 
             System.Windows.Ink.DrawingAttributes.FitToCurve is true.
        
            Returns: A System.Windows.Input.StylusPointCollection that contains the stylus points along the spine of 
             a System.Windows.Ink.Stroke when System.Windows.Ink.DrawingAttributes.FitToCurve is true
        """
        pass

    def GetBounds(self):
        """
        GetBounds(self: Stroke) -> Rect
        
            Retrieves the bounding box for the System.Windows.Ink.Stroke object.
            Returns: A System.Windows.Rect structure defining the bounding box for the System.Windows.Ink.Stroke 
             object.
        """
        pass

    def GetClipResult(self, *__args):
        """
        GetClipResult(self: Stroke, lassoPoints: IEnumerable[Point]) -> StrokeCollection
        GetClipResult(self: Stroke, bounds: Rect) -> StrokeCollection
        
            Returns segments of the current System.Windows.Ink.Stroke that are within the specified 
             rectangle.
        
        
            bounds: A System.Windows.Rect that specifies the area to clip.
            Returns: A System.Windows.Ink.StrokeCollection that contains copies of the segments of the current 
             System.Windows.Ink.Stroke that are within the bounds of bounds.
        """
        pass

    def GetEraseResult(self, *__args):
        """
        GetEraseResult(self: Stroke, eraserPath: IEnumerable[Point], eraserShape: StylusShape) -> StrokeCollection
        GetEraseResult(self: Stroke, lassoPoints: IEnumerable[Point]) -> StrokeCollection
        GetEraseResult(self: Stroke, bounds: Rect) -> StrokeCollection
        
            Returns segments of the current System.Windows.Ink.Stroke that are outside the specified 
             rectangle.
        
        
            bounds: A System.Windows.Rect that specifies the area to erase.
            Returns: A System.Windows.Ink.StrokeCollection that contains the segments of the current 
             System.Windows.Ink.Stroke that are outside the bounds of the specified System.Windows.Rect.
        """
        pass

    def GetGeometry(self, drawingAttributes=None):
        """
        GetGeometry(self: Stroke, drawingAttributes: DrawingAttributes) -> Geometry
        
            Gets the System.Windows.Media.Geometry of the current System.Windows.Ink.Stroke using the 
             specified System.Windows.Ink.DrawingAttributes.
        
        
            drawingAttributes: The System.Windows.Ink.DrawingAttributes that determines the System.Windows.Media.Geometry of 
             the System.Windows.Ink.Stroke.
        
            Returns: A System.Windows.Media.Geometry that represents the System.Windows.Ink.Stroke.
        GetGeometry(self: Stroke) -> Geometry
        
            Gets the System.Windows.Media.Geometry of the current System.Windows.Ink.Stroke.
            Returns: A System.Windows.Media.Geometry that represents the System.Windows.Ink.Stroke.
        """
        pass

    def GetPropertyData(self, propertyDataId):
        """
        GetPropertyData(self: Stroke, propertyDataId: Guid) -> object
        
            Retrieves the property data for the specified GUID.
        
            propertyDataId: The unique identifier for the property.
            Returns: An object containing the property data.
        """
        pass

    def GetPropertyDataIds(self):
        """
        GetPropertyDataIds(self: Stroke) -> Array[Guid]
        
            Retrieves the GUIDs of any custom properties associated with the System.Windows.Ink.Stroke 
             object.
        
            Returns: An array of System.Guid objects.
        """
        pass

    def HitTest(self, *__args):
        """
        HitTest(self: Stroke, lassoPoints: IEnumerable[Point], percentageWithinLasso: int) -> bool
        HitTest(self: Stroke, path: IEnumerable[Point], stylusShape: StylusShape) -> bool
        HitTest(self: Stroke, bounds: Rect, percentageWithinBounds: int) -> bool
        
            Returns a value that indicates whether the System.Windows.Ink.Stroke is within the bounds of the 
             specified rectangle.
        
        
            percentageWithinBounds: The percentage of the length of the System.Windows.Ink.Stroke, that must be in 
             percentageWithinBounds for the System.Windows.Ink.Stroke to be considered hit..
        
            Returns: true if the current stroke is within the bounds of bounds; otherwise false.
        HitTest(self: Stroke, point: Point) -> bool
        
            Returns a value that indicates whether current System.Windows.Ink.Stroke intersects the 
             specified point.
        
        
            point: The System.Windows.Point to hit test.
            Returns: true if point intersects the current stroke; otherwise, false.
        HitTest(self: Stroke, point: Point, diameter: float) -> bool
        
            Returns a value that indicates whether current System.Windows.Ink.Stroke intersects the 
             specified area.
        
        
            point: The System.Windows.Point that defines the center of the area to hit test.
            diameter: The diameter of the area to hit test.
            Returns: true if the specified area intersects the current stroke; otherwise, false.
        """
        pass

    def OnDrawingAttributesChanged(self, *args): #cannot find CLR method
        """
        OnDrawingAttributesChanged(self: Stroke, e: PropertyDataChangedEventArgs)
            Allows derived classes to modify the default behavior of the 
             System.Windows.Ink.Stroke.DrawingAttributesChanged event.
        
        
            e: The System.Windows.Ink.PropertyDataChangedEventArgs object that contains the event data.
        """
        pass

    def OnDrawingAttributesReplaced(self, *args): #cannot find CLR method
        """
        OnDrawingAttributesReplaced(self: Stroke, e: DrawingAttributesReplacedEventArgs)
            Allows derived classes to modify the default behavior of the 
             System.Windows.Ink.Stroke.DrawingAttributesReplaced event.
        
        
            e: The System.Windows.Ink.DrawingAttributesReplacedEventArgs object that contains the event data.
        """
        pass

    def OnInvalidated(self, *args): #cannot find CLR method
        """
        OnInvalidated(self: Stroke, e: EventArgs)
            Raises the System.Windows.Ink.Stroke.Invalidated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Stroke, e: PropertyChangedEventArgs)
            Occurs when any System.Windows.Ink.Stroke property changes.
        """
        pass

    def OnPropertyDataChanged(self, *args): #cannot find CLR method
        """
        OnPropertyDataChanged(self: Stroke, e: PropertyDataChangedEventArgs)
            Allows derived classes to modify the default behavior of the 
             System.Windows.Ink.Stroke.PropertyDataChanged event.
        
        
            e: The System.Windows.Ink.PropertyDataChangedEventArgs object that contains the event data.
        """
        pass

    def OnStylusPointsChanged(self, *args): #cannot find CLR method
        """
        OnStylusPointsChanged(self: Stroke, e: EventArgs)
            Raises the System.Windows.Ink.Stroke.StylusPointsChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnStylusPointsReplaced(self, *args): #cannot find CLR method
        """
        OnStylusPointsReplaced(self: Stroke, e: StylusPointsReplacedEventArgs)
            Raises the System.Windows.Ink.Stroke.StylusPointsReplaced event.
        
            e: A System.Windows.Ink.StylusPointsReplacedEventArgs that contains the event data.
        """
        pass

    def RemovePropertyData(self, propertyDataId):
        """
        RemovePropertyData(self: Stroke, propertyDataId: Guid)
            Deletes a custom property from the System.Windows.Ink.Stroke object.
        
            propertyDataId: The unique identifier for the property.
        """
        pass

    def Transform(self, transformMatrix, applyToStylusTip):
        """
        Transform(self: Stroke, transformMatrix: Matrix, applyToStylusTip: bool)
            Performs a transformation based upon the specified System.Windows.Media.Matrix object.
        
            transformMatrix: The System.Windows.Media.Matrix object defining the transformation.
            applyToStylusTip: true to apply the transformation to the tip of the stylus; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stylusPoints, drawingAttributes=None):
        """
        __new__(cls: type, stylusPoints: StylusPointCollection)
        __new__(cls: type, stylusPoints: StylusPointCollection, drawingAttributes: DrawingAttributes)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DrawingAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Ink.DrawingAttributes for the System.Windows.Ink.Stroke object.

Get: DrawingAttributes(self: Stroke) -> DrawingAttributes

Set: DrawingAttributes(self: Stroke) = value
"""

    StylusPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the stylus points of the System.Windows.Ink.Stroke.

Get: StylusPoints(self: Stroke) -> StylusPointCollection

Set: StylusPoints(self: Stroke) = value
"""


    DrawingAttributesChanged = None
    DrawingAttributesReplaced = None
    Invalidated = None
    PropertyDataChanged = None
    StylusPointsChanged = None
    StylusPointsReplaced = None


class StrokeCollection(Collection[Stroke], IList[Stroke], ICollection[Stroke], IEnumerable[Stroke], IEnumerable, IList, ICollection, IReadOnlyList[Stroke], IReadOnlyCollection[Stroke], INotifyPropertyChanged, INotifyCollectionChanged):
    """
    Represents a collection of System.Windows.Ink.Stroke objects.
    
    StrokeCollection()
    StrokeCollection(strokes: IEnumerable[Stroke])
    StrokeCollection(stream: Stream)
    """
    def Add(self, *__args):
        """
        Add(self: StrokeCollection, strokes: StrokeCollection)
            Adds the specified strokes to the System.Windows.Ink.StrokeCollection.
        
            strokes: The System.Windows.Ink.StrokeCollection to add to the collection.
        """
        pass

    def AddPropertyData(self, propertyDataId, propertyData):
        """
        AddPropertyData(self: StrokeCollection, propertyDataId: Guid, propertyData: object)
            Adds a custom property to the System.Windows.Ink.StrokeCollection.
        
            propertyDataId: The System.Guid to associate with the custom property.
            propertyData: The value of the custom property. propertyData must be of type System.Char, 
             System.Byte,System.Int16,,System.UInt16, System.Int32, System.UInt32, System.Int64, 
             System.UInt64, System.Single, System.Double, System.DateTime, System.Boolean, System.String, 
             System.Decimal or an array of these data types, except System.String, which is not allowed.
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: StrokeCollection)
            Clears all strokes from the System.Windows.Ink.StrokeCollection.
        """
        pass

    def Clip(self, *__args):
        """
        Clip(self: StrokeCollection, bounds: Rect)
            Replaces all strokes that are clipped by the specified rectangle with new strokes that do not 
             extend beyond the specified rectangle.
        
        
            bounds: A System.Windows.Rect that specifies the area to be clipped.
        Clip(self: StrokeCollection, lassoPoints: IEnumerable[Point])
        """
        pass

    def Clone(self):
        """
        Clone(self: StrokeCollection) -> StrokeCollection
        
            Copies the System.Windows.Ink.StrokeCollection.
            Returns: A copy of the System.Windows.Ink.StrokeCollection.
        """
        pass

    def ContainsPropertyData(self, propertyDataId):
        """
        ContainsPropertyData(self: StrokeCollection, propertyDataId: Guid) -> bool
        
            Returns whether the specified custom property identifier is in the 
             System.Windows.Ink.StrokeCollection.
        
        
            propertyDataId: The System.Guid to locate in the System.Windows.Ink.StrokeCollection.
            Returns: true if the specified custom property identifier is in the System.Windows.Ink.StrokeCollection; 
             otherwise, false.
        """
        pass

    def Draw(self, context):
        """
        Draw(self: StrokeCollection, context: DrawingContext)
            Draws the strokes in the System.Windows.Ink.StrokeCollection.
        
            context: The System.Windows.Media.DrawingContext on which to draw the System.Windows.Ink.StrokeCollection.
        """
        pass

    def Erase(self, *__args):
        """
        Erase(self: StrokeCollection, eraserPath: IEnumerable[Point], eraserShape: StylusShape)Erase(self: StrokeCollection, bounds: Rect)
            Replaces all strokes that are clipped by the specified rectangle with new strokes that do not 
             enter the bounds of the specified rectangle.
        
        Erase(self: StrokeCollection, lassoPoints: IEnumerable[Point])
        """
        pass

    def GetBounds(self):
        """
        GetBounds(self: StrokeCollection) -> Rect
        
            Returns the bounds of the strokes in the collection.
            Returns: A System.Windows.Rect that contains the bounds of the strokes in the 
             System.Windows.Ink.StrokeCollection.
        """
        pass

    def GetIncrementalLassoHitTester(self, percentageWithinLasso):
        """
        GetIncrementalLassoHitTester(self: StrokeCollection, percentageWithinLasso: int) -> IncrementalLassoHitTester
        
            Creates an System.Windows.Ink.IncrementalLassoHitTester that hit tests the 
             System.Windows.Ink.StrokeCollection with a lasso (freehand) path.
        
        
            percentageWithinLasso: The minimum percentage of each System.Windows.Ink.Stroke that must be contained within the lasso 
             for it to be considered hit.
        
            Returns: An System.Windows.Ink.IncrementalLassoHitTester that hit tests the 
             System.Windows.Ink.StrokeCollection.
        """
        pass

    def GetIncrementalStrokeHitTester(self, eraserShape):
        """
        GetIncrementalStrokeHitTester(self: StrokeCollection, eraserShape: StylusShape) -> IncrementalStrokeHitTester
        
            Creates an System.Windows.Ink.IncrementalStrokeHitTester that hit tests the 
             System.Windows.Ink.StrokeCollection with an erasing path.
        
        
            eraserShape: A System.Windows.Ink.StylusShape that specifies the tip of the stylus.
            Returns: An System.Windows.Ink.IncrementalStrokeHitTester that hit tests the 
             System.Windows.Ink.StrokeCollection.
        """
        pass

    def GetPropertyData(self, propertyDataId):
        """
        GetPropertyData(self: StrokeCollection, propertyDataId: Guid) -> object
        
            Returns the value of the custom property associated with the specified System.Guid.
        
            propertyDataId: The System.Guid associated with the custom property to get.
            Returns: The value of the custom property associated with the specified System.Guid.
        """
        pass

    def GetPropertyDataIds(self):
        """
        GetPropertyDataIds(self: StrokeCollection) -> Array[Guid]
        
            Returns the GUIDs of any custom properties associated with the 
             System.Windows.Ink.StrokeCollection.
        
            Returns: An array of type System.Guid that represent the custom property identifiers.
        """
        pass

    def HitTest(self, *__args):
        """
        HitTest(self: StrokeCollection, bounds: Rect, percentageWithinBounds: int) -> StrokeCollection
        
            Returns a collection of strokes that have at least the specified percentage of length within the 
             specified rectangle.
        
        
            bounds: A System.Windows.Rect that specifies the bounds to be hit tested.
            percentageWithinBounds: The minimum required length of a Stroke that must exist within bounds for it to be considered 
             hit.
        
            Returns: A System.Windows.Ink.StrokeCollection that has strokes with at least the specified percentage 
             within the System.Windows.Rect.
        
        HitTest(self: StrokeCollection, path: IEnumerable[Point], stylusShape: StylusShape) -> StrokeCollection
        HitTest(self: StrokeCollection, lassoPoints: IEnumerable[Point], percentageWithinLasso: int) -> StrokeCollection
        HitTest(self: StrokeCollection, point: Point) -> StrokeCollection
        
            Returns a collection of strokes that intersect the specified point.
        
            point: The point to hit test.
            Returns: A collection of System.Windows.Ink.Stroke objects that intersect the specified point.
        HitTest(self: StrokeCollection, point: Point, diameter: float) -> StrokeCollection
        
            Returns a collection of strokes that intersect the specified area.
        
            point: The System.Windows.Point to hit test.
            diameter: The size of the area around the System.Windows.Point to hit test.
            Returns: A collection of System.Windows.Ink.Stroke objects that intersect the specified point.
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: StrokeCollection, stroke: Stroke) -> int
        
            Returns the index of the specified System.Windows.Ink.Stroke in the 
             System.Windows.Ink.StrokeCollection.
        
        
            stroke: The stroke whose position is required.
            Returns: The index of the stroke.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: StrokeCollection, index: int, stroke: Stroke)
            Inserts a stroke into the System.Windows.Ink.StrokeCollection at the specified index.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: StrokeCollection, e: PropertyChangedEventArgs)
            Occurs when any System.Windows.Ink.StrokeCollection property changes.
        
            e: Event data.
        """
        pass

    def OnPropertyDataChanged(self, *args): #cannot find CLR method
        """
        OnPropertyDataChanged(self: StrokeCollection, e: PropertyDataChangedEventArgs)
            Raises the System.Windows.Ink.StrokeCollection.PropertyDataChanged event.
        """
        pass

    def OnStrokesChanged(self, *args): #cannot find CLR method
        """
        OnStrokesChanged(self: StrokeCollection, e: StrokeCollectionChangedEventArgs)
            Raises the System.Windows.Ink.StrokeCollection.StrokesChanged event.
        
            e: A System.Windows.Ink.StrokeCollectionChangedEventArgs that contains the event data.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: StrokeCollection, strokes: StrokeCollection)
            Removes the specified strokes from the collection.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: StrokeCollection, index: int)
            Removes the stroke at the specified index from the System.Windows.Ink.StrokeCollection.
        
            index: The specified index.
        """
        pass

    def RemovePropertyData(self, propertyDataId):
        """
        RemovePropertyData(self: StrokeCollection, propertyDataId: Guid)
            Removes the custom property associated with the specified System.Guid.
        
            propertyDataId: The System.Guid associated with the custom property to remove.
        """
        pass

    def Replace(self, *__args):
        """
        Replace(self: StrokeCollection, strokesToReplace: StrokeCollection, strokesToReplaceWith: StrokeCollection)
            Replaces the specified System.Windows.Ink.StrokeCollection with a new 
             System.Windows.Ink.StrokeCollection.
        
        
            strokesToReplace: The destination System.Windows.Ink.StrokeCollection.
            strokesToReplaceWith: The source System.Windows.Ink.StrokeCollection.
        Replace(self: StrokeCollection, strokeToReplace: Stroke, strokesToReplaceWith: StrokeCollection)
            Replaces the specified System.Windows.Ink.Stroke with the specified 
             System.Windows.Ink.StrokeCollection.
        
        
            strokeToReplace: The System.Windows.Ink.Stroke to replace.
            strokesToReplaceWith: The source System.Windows.Ink.StrokeCollection.
        """
        pass

    def Save(self, stream, compress=None):
        """
        Save(self: StrokeCollection, stream: Stream)
            Saves the System.Windows.Ink.StrokeCollection to the specified System.IO.Stream.
        
            stream: The System.IO.Stream to which to save the System.Windows.Ink.StrokeCollection.
        Save(self: StrokeCollection, stream: Stream, compress: bool)
            Saves the System.Windows.Ink.StrokeCollection to the specified System.IO.Stream and compresses 
             it, when specified.
        
        
            stream: The System.IO.Stream to which to save the System.Windows.Ink.StrokeCollection.
            compress: true to compress the System.Windows.Ink.StrokeCollection; otherwise, false.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: StrokeCollection, index: int, stroke: Stroke)
            Replaces the stroke at the specified index.
        """
        pass

    def Transform(self, transformMatrix, applyToStylusTip):
        """
        Transform(self: StrokeCollection, transformMatrix: Matrix, applyToStylusTip: bool)
            Modifies each of the System.Windows.Ink.Stroke.StylusPoints and optionally the 
             System.Windows.Ink.DrawingAttributes.StylusTipTransform for each stroke in the 
             System.Windows.Ink.StrokeCollection according to the specified System.Windows.Media.Matrix.
        
        
            transformMatrix: A System.Windows.Media.Matrix which specifies the transformation to perform on the 
             System.Windows.Ink.StrokeCollection.
        
            applyToStylusTip: true to apply the transformation to the tip of the stylus; otherwise, false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, strokes: IEnumerable[Stroke])
        __new__(cls: type, stream: Stream)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


    InkSerializedFormat = 'Ink Serialized Format'
    PropertyDataChanged = None
    StrokesChanged = None


class StrokeCollectionChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Ink.StrokeCollection.StrokesChanged event.
    
    StrokeCollectionChangedEventArgs(added: StrokeCollection, removed: StrokeCollection)
    """
    @staticmethod # known case of __new__
    def __new__(self, added, removed):
        """ __new__(cls: type, added: StrokeCollection, removed: StrokeCollection) """
        pass

    Added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the strokes that have been added to the System.Windows.Ink.StrokeCollection.

Get: Added(self: StrokeCollectionChangedEventArgs) -> StrokeCollection

"""

    Removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the strokes that have been removed from the System.Windows.Ink.StrokeCollection.

Get: Removed(self: StrokeCollectionChangedEventArgs) -> StrokeCollection

"""



class StrokeCollectionChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Ink.StrokeCollection.StrokesChanged event of a System.Windows.Ink.StrokeCollection.
    
    StrokeCollectionChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StrokeCollectionChangedEventHandler, sender: object, e: StrokeCollectionChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StrokeCollectionChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StrokeCollectionChangedEventHandler, sender: object, e: StrokeCollectionChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StrokeHitEventArgs(EventArgs):
    """ Represents the method that will handle the System.Windows.Ink.IncrementalStrokeHitTester.StrokeHit event of a System.Windows.Ink.IncrementalStrokeHitTester. """
    def GetPointEraseResults(self):
        """
        GetPointEraseResults(self: StrokeHitEventArgs) -> StrokeCollection
        
            Returns the strokes that are a result of the eraser path erasing a stroke.
            Returns: A System.Windows.Ink.StrokeCollection that contains the strokes that are created after the 
             eraser path erases part of System.Windows.Ink.StrokeHitEventArgs.HitStroke.
        """
        pass

    HitStroke = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Ink.Stroke that is intersected by the eraser path.

Get: HitStroke(self: StrokeHitEventArgs) -> Stroke

"""



class StrokeHitEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Ink.IncrementalStrokeHitTester.StrokeHit event of a System.Windows.Ink.IncrementalStrokeHitTester.
    
    StrokeHitEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StrokeHitEventHandler, sender: object, e: StrokeHitEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StrokeHitEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StrokeHitEventHandler, sender: object, e: StrokeHitEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StylusPointsReplacedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Ink.Stroke.StylusPointsReplaced event.
    
    StylusPointsReplacedEventArgs(newStylusPoints: StylusPointCollection, previousStylusPoints: StylusPointCollection)
    """
    @staticmethod # known case of __new__
    def __new__(self, newStylusPoints, previousStylusPoints):
        """ __new__(cls: type, newStylusPoints: StylusPointCollection, previousStylusPoints: StylusPointCollection) """
        pass

    NewStylusPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new System.Windows.Input.StylusPointCollection for the System.Windows.Ink.Stroke.

Get: NewStylusPoints(self: StylusPointsReplacedEventArgs) -> StylusPointCollection

"""

    PreviousStylusPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the replaced System.Windows.Input.StylusPointCollection.

Get: PreviousStylusPoints(self: StylusPointsReplacedEventArgs) -> StylusPointCollection

"""



class StylusPointsReplacedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Ink.Stroke.StylusPointsReplaced event of a System.Windows.Ink.Stroke.
    
    StylusPointsReplacedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StylusPointsReplacedEventHandler, sender: object, e: StylusPointsReplacedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StylusPointsReplacedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StylusPointsReplacedEventHandler, sender: object, e: StylusPointsReplacedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StylusTip(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the tip to be used to draw a System.Windows.Ink.Stroke.
    
    enum StylusTip, values: Ellipse (1), Rectangle (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Ellipse = None
    Rectangle = None
    value__ = None


