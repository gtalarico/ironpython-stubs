# encoding: utf-8
# module Rhino.Input.Custom calls itself Custom
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CommandLineOption(object):
    # no doc
    @staticmethod
    def IsValidOptionName(optionName):
        """
        IsValidOptionName(optionName: str) -> bool
        
            Test a string to see if it can be used as an option name in any of the 
             RhinoGet::AddCommandOption...() functions.
        
        
            optionName: The string to be tested.
            Returns: true if string can be used as an option name.
        """
        pass

    @staticmethod
    def IsValidOptionValueName(optionValue):
        """
        IsValidOptionValueName(optionValue: str) -> bool
        
            Test a string to see if it can be used as an option value in RhinoGet::AddCommandOption,
               
                  RhinoGet::AddCommandOptionToggle, or RhinoGet::AddCommandOptionList.
        
        
            optionValue: The string to be tested.
            Returns: true if string can be used as an option value.
        """
        pass

    CurrentListOptionIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentListOptionIndex(self: CommandLineOption) -> int

"""

    EnglishName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnglishName(self: CommandLineOption) -> str

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: CommandLineOption) -> int

"""



class GeometryAttributeFilter(Enum, IComparable, IFormattable, IConvertible):
    """
    If an object passes the geometry TYPE filter, then the geometry ATTRIBUTE
                filter is applied.
    
    enum (flags) GeometryAttributeFilter, values: AcceptAllAttributes (4294967295), BoundaryEdge (384), BoundaryInnerLoop (2097152), BoundaryOuterLoop (8388608), ClosedCurve (4), ClosedMesh (524288), ClosedPolysrf (131072), ClosedSurface (512), EdgeCurve (2), InnerLoop (6291456), ManifoldEdge (32), ManifoldPolysrf (32768), MatedEdge (112), MatedInnerLoop (4194304), MatedOuterLoop (16777216), NonmanifoldEdge (64), NonmanifoldPolysrf (65536), OpenCurve (8), OpenMesh (1048576), OpenPolysrf (262144), OpenSurface (1024), OuterLoop (25165824), SeamEdge (16), SpecialLoop (33554432), SubSurface (8192), SurfaceBoundaryEdge (128), TopSurface (16384), TrimmedSurface (2048), TrimmingBoundaryEdge (256), UntrimmedSurface (4096), WireCurve (1)
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

    AcceptAllAttributes = None
    BoundaryEdge = None
    BoundaryInnerLoop = None
    BoundaryOuterLoop = None
    ClosedCurve = None
    ClosedMesh = None
    ClosedPolysrf = None
    ClosedSurface = None
    EdgeCurve = None
    InnerLoop = None
    ManifoldEdge = None
    ManifoldPolysrf = None
    MatedEdge = None
    MatedInnerLoop = None
    MatedOuterLoop = None
    NonmanifoldEdge = None
    NonmanifoldPolysrf = None
    OpenCurve = None
    OpenMesh = None
    OpenPolysrf = None
    OpenSurface = None
    OuterLoop = None
    SeamEdge = None
    SpecialLoop = None
    SubSurface = None
    SurfaceBoundaryEdge = None
    TopSurface = None
    TrimmedSurface = None
    TrimmingBoundaryEdge = None
    UntrimmedSurface = None
    value__ = None
    WireCurve = None


class GetBaseClass(object, IDisposable):
    """
    Base class for GetObject, GetPoint, GetSphere, etc.
                
                You will never directly create a GetBaseClass but you will use its member
                functions after calling GetObject.Gets(), GetPoint.Get(), and so on.
                
                Provides tools to set command prompt, set command options, and specify
                if the "get" can optionally accept numbers, nothing (pressing enter),
                and undo.
    """
    def AcceptColor(self, enable):
        """
        AcceptColor(self: GetBaseClass, enable: bool)
            If you want to allow the user to be able to type in a color r,g,b or name
                    during 
             GetPoint.Get(), GetObject::GetObjects(), etc., then call AcceptColor(true)
                    before 
             calling GetPoint()/GetObject(). If the user chooses to type in a color,
                    then the 
             result code GetResult.Color is returned and you can use RhinoGet.Color()
                    to get the 
             value of the color.  If the get accepts points, then the user will not
                    be able to 
             type in r,g,b colors but will be able to type color names.
        
        
            enable: true if user is able to type a color.
        """
        pass

    def AcceptCustomMessage(self, enable):
        """ AcceptCustomMessage(self: GetBaseClass, enable: bool) """
        pass

    def AcceptNothing(self, enable):
        """
        AcceptNothing(self: GetBaseClass, enable: bool)
            If you want to allow the user to be able to press enter in order to
                    skip selecting 
             a something in GetPoint.Get(), GetObject::GetObjects(),
                    etc., then call 
             AcceptNothing( true ) beforehand.
        
        
            enable: true if user is able to press enter in order to skip selecting.
        """
        pass

    def AcceptNumber(self, enable, acceptZero):
        """
        AcceptNumber(self: GetBaseClass, enable: bool, acceptZero: bool)
            If you want to allow the user to be able to type in a number during GetPoint.Get(),
                    
             GetObject::GetObjects(), etc., then call AcceptNumber() beforehand.
                    If the user 
             chooses to type in a number, then the result code GetResult.Number is
                    returned and 
             you can use RhinoGet.Number() to get the value of the number. If you
                    are using 
             GetPoint and you want "0" to return (0,0,0) instead of the number zero, 
                    then set 
             acceptZero = false.
        
        
            enable: true if user is able to type a number.
            acceptZero: If you are using GetPoint and you want "0" to return (0,0,0) instead of the number zero, 
              
                   then set acceptZero = false.
        """
        pass

    def AcceptPoint(self, enable):
        """
        AcceptPoint(self: GetBaseClass, enable: bool)
            If you want to allow the user to be able to type in a point then call AcceptPoint(true)
                
                 before calling GetPoint()/GetObject(). If the user chooses to type in a number, then
               
                  the result code GetResult.Point is returned and you can use RhinoGet.Point()
                    
             to get the value of the point.
        
        
            enable: true if user is able to type in a point.
        """
        pass

    def AcceptString(self, enable):
        """
        AcceptString(self: GetBaseClass, enable: bool)
            If you want to allow the user to be able to type in a string during GetPoint.Get(),
                    
             GetObject::GetObjects(), etc., then call AcceptString(true) before calling
                    
             GetPoint()/GetObject(). If the user chooses to type in a string, then the result code
                  
               GetResult.String is returned and you can use RhinoGet.String() to get the value of the string.
        
        
            enable: true if user is able to type a string.
        """
        pass

    def AcceptUndo(self, enable):
        """
        AcceptUndo(self: GetBaseClass, enable: bool)
            If you want to allow the user to have an 'undo' option in GetPoint.Get(),
                    
             GetObject.GetObjects(), etc., then call AcceptUndo(true) beforehand.
        
        
            enable: true if user is able to choose the 'Undo' option.
        """
        pass

    def AddOption(self, *__args):
        """
        AddOption(self: GetBaseClass, optionName: LocalizeStringPair) -> int
        
            Adds a command line option.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOption(self: GetBaseClass, optionName: LocalizeStringPair, optionValue: LocalizeStringPair) -> int
        
            Adds a command line option.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            optionValue: The localized value visualized after an equality sign.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOption(self: GetBaseClass, englishOption: str) -> int
        
            Adds a command line option.
        
            englishOption: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOption(self: GetBaseClass, englishOption: str, englishOptionValue: str) -> int
        
            Adds a command line option.
        
            englishOption: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            englishOptionValue: The option value in English, visualized after an equality sign.
            Returns: Option index value (>0) or 0 if option cannot be added.
        """
        pass

    def AddOptionColor(self, *__args):
        """
        AddOptionColor(self: GetBaseClass, englishName: str, colorValue: OptionColor, prompt: str) -> (int, OptionColor)
        
            Add a command line option to get colors and automatically save the value.
        
            englishName: option description
            colorValue: The current color value.
            prompt: The command prompt will show this during picking.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionColor(self: GetBaseClass, englishName: str, colorValue: OptionColor) -> (int, OptionColor)
        
            Add a command line option to get colors and automatically save the value.
        
            englishName: option description
            colorValue: The current color value.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionColor(self: GetBaseClass, optionName: LocalizeStringPair, colorValue: OptionColor, prompt: str) -> (int, OptionColor)
        
            Add a command line option to get colors and automatically save the value.
        
            optionName: option description.
            colorValue: The current color value.
            prompt: option prompt shown if the user selects this option
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionColor(self: GetBaseClass, optionName: LocalizeStringPair, colorValue: OptionColor) -> (int, OptionColor)
        
            Add a command line option to get colors and automatically save the value.
        
            optionName: option description
            colorValue: The current color value.
            Returns: option index value (>0) or 0 if option cannot be added.
        """
        pass

    def AddOptionDouble(self, *__args):
        """
        AddOptionDouble(self: GetBaseClass, englishName: str, numberValue: OptionDouble) -> (int, OptionDouble)
        
            Adds a command line option to get numbers and automatically save the value.
        
            englishName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            numberValue: The current number value.
            Returns: Option index value (>0) or 0 if option cannot be added.
        AddOptionDouble(self: GetBaseClass, optionName: LocalizeStringPair, numberValue: OptionDouble) -> (int, OptionDouble)
        
            Adds a command line option to get numbers and automatically save the value.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            numberValue: The current number value.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionDouble(self: GetBaseClass, englishName: str, numberValue: OptionDouble, prompt: str) -> (int, OptionDouble)
        
            Adds a command line option to get numbers and automatically save the value.
        
            englishName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            numberValue: Current value.
            prompt: option prompt shown if the user selects this option.  If null or empty, then the
                    
             option name is used as the get number prompt.
        
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionDouble(self: GetBaseClass, optionName: LocalizeStringPair, numberValue: OptionDouble, prompt: str) -> (int, OptionDouble)
        
            Adds a command line option to get numbers and automatically saves the value.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            numberValue: The current number value.
            prompt: option prompt shown if the user selects this option.  If null or empty, then the
                    
             option name is used as the get number prompt.
        
            Returns: option index value (>0) or 0 if option cannot be added.
        """
        pass

    def AddOptionEnumList(self, englishOptionName, defaultValue):
        """ AddOptionEnumList[T](self: GetBaseClass, englishOptionName: str, defaultValue: T) -> int """
        pass

    def AddOptionEnumSelectionList(self, englishOptionName, enumSelection, listCurrentIndex):
        """ AddOptionEnumSelectionList[T](self: GetBaseClass, englishOptionName: str, enumSelection: IEnumerable[T], listCurrentIndex: int) -> int """
        pass

    def AddOptionInteger(self, *__args):
        """
        AddOptionInteger(self: GetBaseClass, englishName: str, intValue: OptionInteger) -> (int, OptionInteger)
        
            Adds a command line option to get integers and automatically save the value.
        
            englishName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            intValue: The current integer value.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionInteger(self: GetBaseClass, optionName: LocalizeStringPair, intValue: OptionInteger) -> (int, OptionInteger)
        
            Adds a command line option to get integers and automatically save the value.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            intValue: The current integer value.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionInteger(self: GetBaseClass, englishName: str, intValue: OptionInteger, prompt: str) -> (int, OptionInteger)
        
            Adds a command line option to get integers and automatically save the value.
        
            englishName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            intValue: The current integer value.
            prompt: option prompt shown if the user selects this option.  If null or empty, then the
                    
             option name is used as the get number prompt.
        
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionInteger(self: GetBaseClass, optionName: LocalizeStringPair, intValue: OptionInteger, prompt: str) -> (int, OptionInteger)
        
            Adds a command line option to get integers and automatically save the value.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            intValue: The current integer value.
            prompt: option prompt shown if the user selects this option.  If null or empty, then the
                    
             option name is used as the get number prompt.
        
            Returns: option index value (>0) or 0 if option cannot be added.
        """
        pass

    def AddOptionList(self, *__args):
        """
        AddOptionList(self: GetBaseClass, optionName: LocalizeStringPair, listValues: IEnumerable[LocalizeStringPair], listCurrentIndex: int) -> int
        AddOptionList(self: GetBaseClass, englishOptionName: str, listValues: IEnumerable[str], listCurrentIndex: int) -> int
        """
        pass

    def AddOptionToggle(self, *__args):
        """
        AddOptionToggle(self: GetBaseClass, optionName: LocalizeStringPair, toggleValue: OptionToggle) -> (int, OptionToggle)
        
            Adds a command line option to toggle a setting.
        
            optionName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            toggleValue: The current toggle value.
            Returns: option index value (>0) or 0 if option cannot be added.
        AddOptionToggle(self: GetBaseClass, englishName: str, toggleValue: OptionToggle) -> (int, OptionToggle)
        
            Adds a command line option to toggle a setting.
        
            englishName: Must only consist of letters and numbers (no characters list periods, spaces, or dashes)
            toggleValue: The current toggle value.
            Returns: option index value (>0) or 0 if option cannot be added.
        """
        pass

    def ClearCommandOptions(self):
        """
        ClearCommandOptions(self: GetBaseClass)
            Clear all command options.
        """
        pass

    def ClearDefault(self):
        """
        ClearDefault(self: GetBaseClass)
            Clears any defaults set using SetDefaultPoint, SetDefaultNumber, SetDefaultString, or 
             SetCommandPromptDefault.
        """
        pass

    def Color(self):
        """
        Color(self: GetBaseClass) -> Color
        
            Gets a color if Get*() returns GetResult.Color.
            Returns: The color chosen by the user.
        """
        pass

    def CommandResult(self):
        """
        CommandResult(self: GetBaseClass) -> Result
        
            Helper method for getting command result value from getter results.
            Returns: The converted command result.
        """
        pass

    def CustomMessage(self):
        """ CustomMessage(self: GetBaseClass) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: GetBaseClass) """
        pass

    def EnableTransparentCommands(self, enable):
        """
        EnableTransparentCommands(self: GetBaseClass, enable: bool)
            Control the availability of transparent commands during the get.
        
            enable: If true, then transparent commands can be run during the get.
                    If false, then 
             transparent commands cannot be run during the get.
        """
        pass

    def GetSelectedEnumValue(self):
# Error generating skeleton for function GetSelectedEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetSelectedEnumValueFromSelectionList(self, selectionList):
# Error generating skeleton for function GetSelectedEnumValueFromSelectionList: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GotDefault(self):
        """
        GotDefault(self: GetBaseClass) -> bool
        
            Returns true if user pressed Enter to accept a default point, number,
                    or string set 
             using SetDefaultPoint, SetDefaultNumber, or SetDefaultString.
        
            Returns: true if the result if the default point, number or string set. Otherwise, false.
        """
        pass

    def Line2d(self):
        """
        Line2d(self: GetBaseClass) -> Array[Point]
        
            Returns two points defining the location in the view window of the 2d line selected
                    
             in GetPoint::Get2dLine().
                    (0,0) = upper left corner of window.
        
            Returns: An array with two 2D points.
        """
        pass

    def Number(self):
        """
        Number(self: GetBaseClass) -> float
        
            Gets a number if GetPoint.Get(), GetObject.GetObjects(), etc., returns GetResult.Number.
            Returns: The number chosen by the user.
        """
        pass

    def Option(self):
        """ Option(self: GetBaseClass) -> CommandLineOption """
        pass

    def OptionIndex(self):
        """ OptionIndex(self: GetBaseClass) -> int """
        pass

    def PickRectangle(self):
        """
        PickRectangle(self: GetBaseClass) -> Rectangle
        
            If the get was a GetObjects() and the mouse was used to select the objects,
                    then 
             the returned rect has left < right and top < bottom. This rect
                    is the Windows GDI 
             screen coordinates of the picking rectangle.
                    RhinoViewport.GetPickXform( pick_rect, 
             pick_xform )
                    will calculate the picking transformation that was used.
                    
             In all other cases, left=right=top=bottom=0;
        
            Returns: The picking rectangle; or 0 in the specified cases.
        """
        pass

    def Point(self):
        """
        Point(self: GetBaseClass) -> Point3d
        
            Gets a point if Get*() returns GetResult.Point.
            Returns: The point chosen by the user.
        """
        pass

    def Point2d(self):
        """
        Point2d(self: GetBaseClass) -> Point
        
            Returns location in view of point in selected in GetPoint::Get() or GetPoint::Get2dPoint().
            
                     (0,0) = upper left corner of window.
        
            Returns: The location.
        """
        pass

    @staticmethod
    def PostCustomMessage(messageData):
        """ PostCustomMessage(messageData: object) """
        pass

    def Rectangle2d(self):
        """
        Rectangle2d(self: GetBaseClass) -> Rectangle
        
            Returns the location in the view of the 2d rectangle selected in GetPoint::Get2dRectangle().
           
                      rect.left < rect.right and rect.top < rect.bottom
                    (0,0) = upper left 
             corner of window.
        
            Returns: The rectangle.
        """
        pass

    def Result(self):
        """
        Result(self: GetBaseClass) -> GetResult
        
            Returns result of the Get*() call.
            Returns: The result of the last Get*() call.
        """
        pass

    def SetCommandPrompt(self, prompt):
        """
        SetCommandPrompt(self: GetBaseClass, prompt: str)
            Sets prompt message that appears in the command prompt window.
        
            prompt: command prompt message.
        """
        pass

    def SetCommandPromptDefault(self, defaultValue):
        """
        SetCommandPromptDefault(self: GetBaseClass, defaultValue: str)
            Sets message that describes what default value will be used if the user presses enter.
                 
                This description appears in angle brackets <> in the command prompt window. You do
                  
               not need to provide a default value description unless you explicity enable AcceptNothing.
        
        
            defaultValue: description of default value.
        """
        pass

    def SetDefaultColor(self, defaultColor):
        """
        SetDefaultColor(self: GetBaseClass, defaultColor: Color)
            Sets a color as default value that will be returned if the user presses ENTER key during the get.
        
            defaultColor: value for default color.
        """
        pass

    def SetDefaultInteger(self, defaultValue):
        """
        SetDefaultInteger(self: GetBaseClass, defaultValue: int)
            Sets a number as default value that will be returned if the user presses ENTER key during the 
             get.
        
        
            defaultValue: value for default number.
        """
        pass

    def SetDefaultNumber(self, defaultNumber):
        """
        SetDefaultNumber(self: GetBaseClass, defaultNumber: float)
            Sets a number as default value that will be returned if the user presses ENTER key during the 
             get.
        
        
            defaultNumber: value for default number.
        """
        pass

    def SetDefaultPoint(self, point):
        """
        SetDefaultPoint(self: GetBaseClass, point: Point3d)
            Sets a point as default value that will be returned if the user presses the ENTER key during the 
             get.
        
        
            point: value for default point.
        """
        pass

    def SetDefaultString(self, defaultValue):
        """
        SetDefaultString(self: GetBaseClass, defaultValue: str)
            Sets a string as default value that will be returned
                    if the user presses ENTER key 
             during the get.
        
        
            defaultValue: value for default string.
        """
        pass

    def SetWaitDuration(self, milliseconds):
        """
        SetWaitDuration(self: GetBaseClass, milliseconds: int)
            Sets the wait duration (in milliseconds) of the getter. If the duration passes without 
                
                 the user making a decision, the GetResult.Timeout code is returned.
        
        
            milliseconds: Number of milliseconds to wait.
        """
        pass

    def StringResult(self):
        """
        StringResult(self: GetBaseClass) -> str
        
            Gets a string if GetPoint.Get(), GetObject.GetObjects(), etc., returns GetResult.String.
            Returns: The string chosen by the user.
        """
        pass

    def Vector(self):
        """
        Vector(self: GetBaseClass) -> Vector3d
        
            Gets a direction if Get*() returns GetResult.Point (Set by some digitizers, but in general it's 
             (0,0,0).
        
            Returns: The vector chosen by the user.
        """
        pass

    def View(self):
        """
        View(self: GetBaseClass) -> RhinoView
        
            Gets a view the user clicked in during GetPoint.Get(), GetObject.GetObjects(), etc.
            Returns: The view chosen by the user.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class GetFileNameMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GetFileNameMode, values: Attach (8), Export (14), Import (7), Open (0), OpenImage (2), OpenRhinoOnly (3), OpenTemplate (1), OpenTextFile (5), OpenWorksession (6), Save (10), SaveImage (13), SaveSmall (11), SaveTemplate (12), SaveTextFile (17), SaveWorksession (18) """
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

    Attach = None
    Export = None
    Import = None
    Open = None
    OpenImage = None
    OpenRhinoOnly = None
    OpenTemplate = None
    OpenTextFile = None
    OpenWorksession = None
    Save = None
    SaveImage = None
    SaveSmall = None
    SaveTemplate = None
    SaveTextFile = None
    SaveWorksession = None
    value__ = None


class GetInteger(GetBaseClass, IDisposable):
    """
    Used to get integer numbers.
    
    GetInteger()
    """
    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def Get(self):
        """
        Get(self: GetInteger) -> GetResult
        
            Call to get an integer.
            Returns: If the user chose a number, then Rhino.Input.GetResult.Number; another enumeration value 
             otherwise.
        """
        pass

    def Number(self):
        """ Number(self: GetInteger) -> int """
        pass

    def SetLowerLimit(self, lowerLimit, strictlyGreaterThan):
        """
        SetLowerLimit(self: GetInteger, lowerLimit: int, strictlyGreaterThan: bool)
            Sets a lower limit on the number that can be returned.
                    By default there is no lower 
             limit.
        
        
            lowerLimit: smallest acceptable number.
            strictlyGreaterThan: If true, then the returned number will be > lower_limit.
        """
        pass

    def SetUpperLimit(self, upperLimit, strictlyLessThan):
        """
        SetUpperLimit(self: GetInteger, upperLimit: int, strictlyLessThan: bool)
            Sets an upper limit on the number that can be returned.
                    By default there is no 
             upper limit.
        
        
            upperLimit: largest acceptable number.
            strictlyLessThan: If true, then the returned number will be < upper_limit.
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


class GetLine(object, IDisposable):
    """
    Use to interactively get a line.  The Rhino "Line" command uses GetLine.
    
    GetLine()
    """
    def Dispose(self):
        """
        Dispose(self: GetLine)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def EnableAllVariations(self, on):
        """
        EnableAllVariations(self: GetLine, on: bool)
            If true, then all line variations are shown if the default line mode is used
        """
        pass

    def EnableFromBothSidesOption(self, on):
        """
        EnableFromBothSidesOption(self: GetLine, on: bool)
            If true, then the "BothSides" option shows up when the
                    start point is inteactively 
             picked.
        """
        pass

    def EnableFromMidPointOption(self, on):
        """
        EnableFromMidPointOption(self: GetLine, on: bool)
            If true, the the "MidPoint" options shows up
        """
        pass

    def Get(self, line):
        """
        Get(self: GetLine) -> (Result, Line)
        
            Perform the 'get' operation.
        """
        pass

    def SetFirstPoint(self, point):
        """
        SetFirstPoint(self: GetLine, point: Point3d)
            Use SetFirstPoint to specify the line's starting point and skip
                    the start point 
             interactive picking
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AcceptZeroLengthLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls whether or not a zero length line is acceptable.
            The default is to require the user to keep picking the end
            point until we get a point different than the start point.

Get: AcceptZeroLengthLine(self: GetLine) -> bool

Set: AcceptZeroLengthLine(self: GetLine) = value
"""

    FeedbackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If set, the feedback color is used to draw the dynamic
            line when the second point is begin picked.  If not set,
            the active layer color is used.

Get: FeedbackColor(self: GetLine) -> Color

Set: FeedbackColor(self: GetLine) = value
"""

    FirstPointPrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Prompt when getting first point

Get: FirstPointPrompt(self: GetLine) -> str

Set: FirstPointPrompt(self: GetLine) = value
"""

    FixedLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If FixedLength > 0, the line must have the specified length

Get: FixedLength(self: GetLine) -> float

Set: FixedLength(self: GetLine) = value
"""

    GetLineMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Mode used

Get: GetLineMode(self: GetLine) -> GetLineMode

Set: GetLineMode(self: GetLine) = value
"""

    HaveFeedbackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the feedback color is used to draw the dynamic
            line when the second point is begin picked.  If false,
            the active layer color is used.

Get: HaveFeedbackColor(self: GetLine) -> bool

"""

    MidPointPrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Prompt when getting midpoint

Get: MidPointPrompt(self: GetLine) -> str

Set: MidPointPrompt(self: GetLine) = value
"""

    SecondPointPrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Prompt when getting second point

Get: SecondPointPrompt(self: GetLine) -> str

Set: SecondPointPrompt(self: GetLine) = value
"""



class GetLineMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GetLineMode, values: Angled (2), Bisector (5), CPlaneNormalVector (9), CurveEnd (8), FourPoint (4), Perpendicular (6), SurfaceNormal (1), Tangent (7), TwoPoint (0), Vertical (3) """
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

    Angled = None
    Bisector = None
    CPlaneNormalVector = None
    CurveEnd = None
    FourPoint = None
    Perpendicular = None
    SurfaceNormal = None
    Tangent = None
    TwoPoint = None
    value__ = None
    Vertical = None


class GetNumber(GetBaseClass, IDisposable):
    """
    Used to get double precision numbers.
    
    GetNumber()
    """
    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def Get(self):
        """
        Get(self: GetNumber) -> GetResult
        
            Call to get a number.
            Returns: If the user chose a number, then Rhino.Input.GetResult.Number; another enumeration value 
             otherwise.
        """
        pass

    def SetLowerLimit(self, lowerLimit, strictlyGreaterThan):
        """
        SetLowerLimit(self: GetNumber, lowerLimit: float, strictlyGreaterThan: bool)
            Sets a lower limit on the number that can be returned.
                    By default there is no lower 
             limit.
        
        
            lowerLimit: smallest acceptable number.
            strictlyGreaterThan: If true, then the returned number will be > lower_limit.
        """
        pass

    def SetUpperLimit(self, upperLimit, strictlyLessThan):
        """
        SetUpperLimit(self: GetNumber, upperLimit: float, strictlyLessThan: bool)
            Sets an upper limit on the number that can be returned.
                    By default there is no 
             upper limit.
        
        
            upperLimit: largest acceptable number.
            strictlyLessThan: If true, then the returned number will be < upper_limit.
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


class GetObject(GetBaseClass, IDisposable):
    """
    The GetObject class is the tool commands use to interactively select objects.
    
    GetObject()
    """
    def CustomGeometryFilter(self, rhObject, geometry, componentIndex):
        """
        CustomGeometryFilter(self: GetObject, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool
        
            Checks geometry to see if it can be selected.
                    Override to provide fancy filtering.
        
            rhObject: parent object being considered.
            geometry: geometry being considered.
            componentIndex: if >= 0, geometry is a proper sub-part of object->Geometry() with componentIndex.
            Returns: The default returns true unless you've set a custom geometry filter. If a custom
                    
             filter has been set, that delegate is called
        """
        pass

    def DisablePreSelect(self):
        """ DisablePreSelect(self: GetObject) """
        pass

    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def EnableClearObjectsOnEntry(self, enable):
        """
        EnableClearObjectsOnEntry(self: GetObject, enable: bool)
            By default the picked object list is cleared when GetObject.GetObjects() is called.
                    
             If you are reusing a GetObject class and do not want the existing object list
                    
             cleared when you call Input, then call EnableClearObjectsOnEntry(false) before
                    
             calling GetObjects().
        
        
            enable: The state to set.
        """
        pass

    def EnableHighlight(self, enable):
        """
        EnableHighlight(self: GetObject, enable: bool)
            By default, any object post-pick selected by GetObjects() is highlighted.
                    If you 
             want to post-pick objects and not have them automatically highlight,
                    then call 
             EnableHighlight = false.
        """
        pass

    def EnableIgnoreGrips(self, enable):
        """
        EnableIgnoreGrips(self: GetObject, enable: bool)
            By default, post selection will select objects with grips on. If you do
                    not want to 
             be able to post select objects with grips on, then call
                    EnableIgnoreGrips = false. 
             The ability to preselect an object with grips
                    on is determined by the value 
             returned by the virtual
                    RhinoObject.IsSelectableWithGripsOn.
        """
        pass

    def EnablePostSelect(self, enable):
        """
        EnablePostSelect(self: GetObject, enable: bool)
            Control the availability of post selection in GetObjects.
        """
        pass

    def EnablePreSelect(self, enable, ignoreUnacceptablePreselectedObjects):
        """
        EnablePreSelect(self: GetObject, enable: bool, ignoreUnacceptablePreselectedObjects: bool)
            Control the pre selection behavior GetObjects.
        
            enable: if true, pre-selection is enabled.
            ignoreUnacceptablePreselectedObjects: If true and some acceptable objects are pre-selected, then any unacceptable
                    
             pre-selected objects are ignored. If false and any unacceptable are pre-selected,
                    
             then the user is forced to post-select.
        """
        pass

    def EnablePressEnterWhenDonePrompt(self, enable):
        """
        EnablePressEnterWhenDonePrompt(self: GetObject, enable: bool)
            By default, when GetObject.GetObjects is called with minimumNumber > 0
                    and 
             maximumNumber = 0, the command prompt automatically includes "Press Enter
                    when 
             done" after the user has selected at least minimumNumber of objects. If
                    you want to 
             prohibit the addition of the "Press Enter when done", then call
                    
             EnablePressEnterWhenDonePrompt = false;
        """
        pass

    def EnableSelPrevious(self, enable):
        """
        EnableSelPrevious(self: GetObject, enable: bool)
            By default, any object selected during a command becomes part of the
                    "previous 
             selection set" and can be reselected by the SelPrev command.
                    If you need to select 
             objects but do not want them to be selected by
                    a subsquent call to SelPrev, then 
             call EnableSelPrev = false.
        """
        pass

    def EnableUnselectObjectsOnExit(self, enable):
        """
        EnableUnselectObjectsOnExit(self: GetObject, enable: bool)
            By default any objects in the object list are unselected when GetObject.GetObjects()
                   
              exits with any return code besides Object. If you want to leave the objects
                    
             selected when non-object input is returned, then call EnableUnselectObjectsOnExit(false)
               
                  before calling GetObjects().
        
        
            enable: The state to set.
        """
        pass

    def Get(self):
        """
        Get(self: GetObject) -> GetResult
        
            Call to select a single object.
            Returns: Success - objects selected.
                    Cancel - user pressed ESCAPE to cancel the get.
               
                  See GetResults for other possible values that may be returned when options, numbers,
              
                   etc., are acceptable responses.
        """
        pass

    def GetMultiple(self, minimumNumber, maximumNumber):
        """
        GetMultiple(self: GetObject, minimumNumber: int, maximumNumber: int) -> GetResult
        
            Call to select objects.
        
            minimumNumber: minimum number of objects to select.
            maximumNumber: maximum number of objects to select.
                    If 0, then the user must press enter to finish 
             object selection.
                    If -1, then object selection stops as soon as there are at least 
             minimumNumber of object selected.
                    If >0, then the picking stops when there are 
             maximumNumber objects.  If a window pick, crossing
                    pick, or Sel* command attempts 
             to add more than maximumNumber, then the attempt is ignored.
        
            Returns: Success - objects selected.
                    Cancel - user pressed ESCAPE to cancel the get.
               
                  See GetResults for other possible values that may be returned when options, numbers,
              
                   etc., are acceptable responses.
        """
        pass

    def Object(self, index):
        """ Object(self: GetObject, index: int) -> ObjRef """
        pass

    def Objects(self):
        """ Objects(self: GetObject) -> Array[ObjRef] """
        pass

    def PassesGeometryAttributeFilter(self, rhObject, geometry, componentIndex):
        """
        PassesGeometryAttributeFilter(self: GetObject, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool
        
            Checks geometry to see if it passes the basic GeometryAttributeFilter.
        
            rhObject: parent object being considered.
            geometry: geometry being considered.
            componentIndex: if >= 0, geometry is a proper sub-part of object->Geometry() with componentIndex.
            Returns: true if the geometry passes the filter returned by GeometryAttributeFilter().
        """
        pass

    def SetCustomGeometryFilter(self, filter):
        """
        SetCustomGeometryFilter(self: GetObject, filter: GetObjectGeometryFilter)
            Set filter callback function that will be called by the CustomGeometryFilter
        """
        pass

    def SetPressEnterWhenDonePrompt(self, prompt):
        """
        SetPressEnterWhenDonePrompt(self: GetObject, prompt: str)
            The default prompt when EnablePressEnterWhenDonePrompt is enabled is "Press Enter
                    
             when done". Use this function to specify a different string to be appended.
        
        
            prompt: The text that will be displayed just after the prompt,
                    after the selection has been 
             made.
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

    AlreadySelectedObjectSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow selecting objects that are already selected. By default, GetObjects() disallows
            selection of objects that are already selected to avoid putting the same object
            in the selection set more than once. Calling EnableAlreadySelectedObjectSelect = true
            overrides that restriction and allows selected objects to be selected and
            returned by GetObjects. This is useful because, coupled with the return immediately
            mode of GetObjects(1, -1), it is possible to select a selected object to deselect
            when the selected objects are being managed outside GetObjects() as in the case of
            CRhinoPolyEdge::GetEdge().

Get: AlreadySelectedObjectSelect(self: GetObject) -> bool

Set: AlreadySelectedObjectSelect(self: GetObject) = value
"""

    BottomObjectPreference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, if a call to Input is permitted to select different parts of
            the same object, like a polysurface, a surface and an edge, then the
            top-most object is prefered. (polysurface beats face beats edge). If
            you want the bottom most object to be prefered, then call 
            EnableBottomObjectPreference = true before calling GetObjects().

Get: BottomObjectPreference(self: GetObject) -> bool

Set: BottomObjectPreference(self: GetObject) = value
"""

    ChooseOneQuestion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, if a call to Input is permitted to select different parts
            of the same object, like a polysurface and an edge of that polysurface,
            then the top-most object is automatically selected. If you want the
            choose-one-object mechanism to include pop up in these cases, then call
            EnableChooseOneQuestion = true before calling GetObjects().

Get: ChooseOneQuestion(self: GetObject) -> bool

Set: ChooseOneQuestion(self: GetObject) = value
"""

    DeselectAllBeforePostSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if pre-selected input will be deselected before
            post-selection begins when no pre-selected input is valid.

Get: DeselectAllBeforePostSelect(self: GetObject) -> bool

Set: DeselectAllBeforePostSelect(self: GetObject) = value
"""

    GeometryAttributeFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The geometry attribute filter provides a secondary filter that
            can be used to restrict which objects can be selected. Control
            of the type of geometry (points, curves, surfaces, meshes, etc.)
            is provided by GetObject.SetGeometryFilter. The geometry attribute
            filter is used to require the selected geometry to have certain
            attributes (open, closed, etc.). The default attribute filter
            permits selection of all types of geometry.

Get: GeometryAttributeFilter(self: GetObject) -> GeometryAttributeFilter

Set: GeometryAttributeFilter(self: GetObject) = value
"""

    GeometryFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The geometry type filter controls which types of geometry
            (points, curves, surfaces, meshes, etc.) can be selected.
            The default geometry type filter permits selection of all
            types of geometry.
            NOTE: the filter can be a bitwise combination of multiple ObjectTypes.

Get: GeometryFilter(self: GetObject) -> ObjectType

Set: GeometryFilter(self: GetObject) = value
"""

    GroupSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, groups are ignored in GetObject. If you want your call to
            GetObjects() to select every object in a group that has any objects
            selected, then enable group selection.

Get: GroupSelect(self: GetObject) -> bool

Set: GroupSelect(self: GetObject) = value
"""

    InactiveDetailPickEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, objects in inactive details are not permitted to be picked.
            In a few rare cases this is used (ex. picking circles during DimRadius)

Get: InactiveDetailPickEnabled(self: GetObject) -> bool

Set: InactiveDetailPickEnabled(self: GetObject) = value
"""

    ObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of objects that were selected.

Get: ObjectCount(self: GetObject) -> int

"""

    ObjectsWerePreselected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectsWerePreselected(self: GetObject) -> bool

"""

    OneByOnePostSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """In one-by-one post selection, the user is forced
            to select objects by post picking them one at a time.

Get: OneByOnePostSelect(self: GetObject) -> bool

Set: OneByOnePostSelect(self: GetObject) = value
"""

    ReferenceObjectSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, reference objects can be selected. If you do not want to be
            able to select reference objects, then call EnableReferenceObjectSelect=false.

Get: ReferenceObjectSelect(self: GetObject) -> bool

Set: ReferenceObjectSelect(self: GetObject) = value
"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Each instance of GetObject has a unique runtime serial number that
            is used to identify object selection events associated with that instance.

Get: SerialNumber(self: GetObject) -> UInt32

"""

    SubObjectSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """By default, GetObject.Input will permit a user to select
            sub-objects (like a curve in a b-rep or a curve in a group).
            If you only want the user to select "top" level objects,
            then call EnableSubObjectSelect = false.

Get: SubObjectSelect(self: GetObject) -> bool

Set: SubObjectSelect(self: GetObject) = value
"""



class GetObjectGeometryFilter(MulticastDelegate, ICloneable, ISerializable):
    """ GetObjectGeometryFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, rhObject, geometry, componentIndex, callback, object):
        """ BeginInvoke(self: GetObjectGeometryFilter, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: GetObjectGeometryFilter, result: IAsyncResult) -> bool """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, rhObject, geometry, componentIndex):
        """ Invoke(self: GetObjectGeometryFilter, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool """
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


class GetOption(GetBaseClass, IDisposable):
    """
    If you want to explicitly get string input, then use GetString class with
                options. If you only want to get options, then use this class (GetOption)
    
    GetOption()
    """
    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def Get(self):
        """
        Get(self: GetOption) -> GetResult
        
            Call to get an option. A return value of "option" means the user selected
                    a valid 
             option. Use Option() the determine which option.
        
            Returns: If the user chose an option, then Rhino.Input.GetResult.Option; another enumeration value 
             otherwise.
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


class GetPoint(GetBaseClass, IDisposable):
    """ GetPoint() """
    def AddConstructionPoint(self, point):
        """
        AddConstructionPoint(self: GetPoint, point: Point3d) -> int
        
            Adds a point to the list of construction points.
        
            point: A point to be added.
            Returns: Total number of construction points.
        """
        pass

    def AddConstructionPoints(self, points):
        """
        AddConstructionPoints(self: GetPoint, points: Array[Point3d]) -> int
        
            Adds points to the list of construction points.
        
            points: An array of points to be added.
            Returns: Total number of construction points.
        """
        pass

    def AddSnapPoint(self, point):
        """
        AddSnapPoint(self: GetPoint, point: Point3d) -> int
        
            Adds a point to the list of osnap points.
        
            point: A point.
            Returns: Total number of snap points.
        """
        pass

    def AddSnapPoints(self, points):
        """
        AddSnapPoints(self: GetPoint, points: Array[Point3d]) -> int
        
            Adds points to the list of osnap points.
        
            points: An array of points to snap onto.
            Returns: Total number of snap points.
        """
        pass

    def ClearConstraints(self):
        """
        ClearConstraints(self: GetPoint)
            Removes any explicit constraints added by calls to GetPoint::Constraint() and enable
                   
              the built-in constraint options.
        """
        pass

    def ClearConstructionPoints(self):
        """
        ClearConstructionPoints(self: GetPoint)
            Remove all construction points.
        """
        pass

    def ClearSnapPoints(self):
        """
        ClearSnapPoints(self: GetPoint)
            Remove all snap points.
        """
        pass

    def Constrain(self, *__args):
        """
        Constrain(self: GetPoint, curve: Curve, allowPickingPointOffObject: bool) -> bool
        
            Constrains the picked point to lie on a curve.
        
            curve: A curve to use as constraint.
            allowPickingPointOffObject: defines whether the point pick is allowed to happen off object. When false,
                    a "no 
             no" cursor is shown when the cursor is not on the object. When true,
                    a normal point 
             picking cursor is used and the marker is visible also when
                    the cursor is not on the 
             object.
        
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, cylinder: Cylinder) -> bool
        
            Constrains the picked point to lie on a cylinder.
        
            cylinder: A cylinder to use as constraint.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, surface: Surface, allowPickingPointOffObject: bool) -> bool
        
            Constrains the picked point to lie on a surface.
        
            surface: A surface to use as constraint.
            allowPickingPointOffObject: defines whether the point pick is allowed to happen off object. When false,
                    a "no 
             no" cursor is shown when the cursor is not on the object. When true,
                    a normal point 
             picking cursor is used and the marker is visible also when
                    the cursor is not on the 
             object.
        
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, mesh: Mesh, allowPickingPointOffObject: bool) -> bool
        
            Constrains the picked point to lie on a mesh.
        
            mesh: A mesh to use as constraint.
            allowPickingPointOffObject: defines whether the point pick is allowed to happen off object. When false,
                    a "no 
             no" cursor is shown when the cursor is not on the object. When true,
                    a normal point 
             picking cursor is used and the marker is visible also when
                    the cursor is not on the 
             object.
        
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, brep: Brep, wireDensity: int, faceIndex: int, allowPickingPointOffObject: bool) -> bool
        
            Constrains the picked point to lie on a brep.
        
            brep: A brep to use as constraint.
            wireDensity: When wire_density<0, isocurve intersection snapping is turned off, when wire_density>=0, the 
             value
                    defines the isocurve density used for isocurve intersection snapping.
        
            faceIndex: When face_index <0, constrain to whole brep. When face_index >=0, constrain to individual face.
            allowPickingPointOffObject: defines whether the point pick is allowed to happen off object. When false,
                    a "no 
             no" cursor is shown when the cursor is not on the object. When true,
                    a normal point 
             picking cursor is used and the marker is visible also when
                    the cursor is not on the 
             object.
        
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, sphere: Sphere) -> bool
        
            Constrains the picked point to lie on a sphere.
        
            sphere: A sphere to use as constraint.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, line: Line) -> bool
        
            Constrains the picked point to lie on a line.
        
            line: A line to use as constraint.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, from: Point3d, to: Point3d) -> bool
        
            Constrains the picked point to lie on a line.
        
            from: The start point of constraint.
            to: The end point of constraint.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, arc: Arc) -> bool
        
            Constrains the picked point to lie on an arc.
        
            arc: An arc to use as constraint.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, plane: Plane, allowElevator: bool) -> bool
        
            constrain the picked point to lie on a plane.
        
            plane: A plane to use as constraint.
            allowElevator: true if elevator mode should be allowed at user request.
            Returns: true if constraint could be applied.
        Constrain(self: GetPoint, circle: Circle) -> bool
        
            Constrains the picked point to lie on a circle.
        
            circle: A circle to use as constraint.
            Returns: true if constraint could be applied.
        """
        pass

    def ConstrainDistanceFromBasePoint(self, distance):
        """
        ConstrainDistanceFromBasePoint(self: GetPoint, distance: float)
            Sets distance constraint from base point.
        
            distance: pass UnsetValue to clear this constraint. Pass 0.0 to disable the
                    ability to set 
             this constraint by typing a number during GetPoint.
        """
        pass

    def ConstrainToConstructionPlane(self, throughBasePoint):
        """
        ConstrainToConstructionPlane(self: GetPoint, throughBasePoint: bool) -> bool
        
            If enabled, the picked point is constrained to be on the active construction plane.
                    
             If the base point is set, then the point is constrained to be on the plane that contains
               
                  the base point and is parallel to the active construction plane. By default this
                  
               constraint is enabled.
        
        
            throughBasePoint: true if the base point should be used as compulsory level reference.
            Returns: If true and the base point is set, then the point is constrained to be on the plane parallel
           
                      to the construction plane that passes through the base point, even when planar mode is 
             off.
                    If throughBasePoint is false, then the base point shift only happens if planar 
             mode is on.
        """
        pass

    def ConstrainToTargetPlane(self):
        """
        ConstrainToTargetPlane(self: GetPoint)
            Constrains point to lie on a plane that is parallel to the
                    viewing plane and passes 
             through the view's target point.
        """
        pass

    def ConstrainToVirtualCPlaneIntersection(self, plane):
        """
        ConstrainToVirtualCPlaneIntersection(self: GetPoint, plane: Plane) -> bool
        
            If enabled, the picked point is constrained to be on the 
                    intersection of the plane 
             and the virtual CPlane going through
                    the plane origin.
                    If the planes 
             are parallel, the constraint works just like planar constraint.
        
        
            plane: The plane used for the plane - virtual CPlane intersection.
            Returns: true if the operation succeeded; false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def DrawLineFromPoint(self, startPoint, showDistanceInStatusBar):
        """
        DrawLineFromPoint(self: GetPoint, startPoint: Point3d, showDistanceInStatusBar: bool)
            Use DrawLineFromPoint() if you want a dynamic line drawn from a point to the point being picked.
        
            startPoint: The line is drawn from startPoint to the point being picked. If the base
                    point has 
             not been set, then it is set to startPoint.
        
            showDistanceInStatusBar: if true, the distance from the basePoint to the point begin picked is shown in the status bar.
        """
        pass

    def EnableCurveSnapArrow(self, drawDirectionArrowAtSnapPoint, reverseArrow):
        """
        EnableCurveSnapArrow(self: GetPoint, drawDirectionArrowAtSnapPoint: bool, reverseArrow: bool)
            Controls display of the curve snap arrow icon.
        
            drawDirectionArrowAtSnapPoint: true to draw arrow icon whenever GetPoint snaps to a curve.
            reverseArrow: true if arrow icon direction should be the reverse of the first derivative direction.
        """
        pass

    def EnableCurveSnapPerpBar(self, drawPerpBarAtSnapPoint, drawEndPoints):
        """
        EnableCurveSnapPerpBar(self: GetPoint, drawPerpBarAtSnapPoint: bool, drawEndPoints: bool)
            Controls display of the curve snap perpendicular bar icon.
        
            drawPerpBarAtSnapPoint: true to draw a tangent bar icon  whenever GetPoint snaps to a curve.
            drawEndPoints: true to draw points at the end of the tangent bar.
        """
        pass

    def EnableCurveSnapTangentBar(self, drawTangentBarAtSnapPoint, drawEndPoints):
        """
        EnableCurveSnapTangentBar(self: GetPoint, drawTangentBarAtSnapPoint: bool, drawEndPoints: bool)
            Controls display of the curve snap tangent bar icon.
        
            drawTangentBarAtSnapPoint: true to draw a tangent bar icon whenever GetPoint snaps to a curve.
            drawEndPoints: true to draw points at the end of the tangent bar.
        """
        pass

    def EnableDrawLineFromPoint(self, enable):
        """
        EnableDrawLineFromPoint(self: GetPoint, enable: bool)
            Controls drawing of dynamic a line from the start point.
        
            enable: if true, a dynamic line is drawn from the DrawLineFromPoint startPoint to the point being picked.
        """
        pass

    def EnableSnapToCurves(self, enable):
        """
        EnableSnapToCurves(self: GetPoint, enable: bool)
            If you want GetPoint() to try to snap to curves when the mouse is near a curve
                    
             (like the center point in the Circle command when the AroundCurve option is on),
                    
             then enable the snap to curves option.
        
        
            enable: Whether points should be enabled.
        """
        pass

    def Get(self, onMouseUp=None, get2DPoint=None):
        """
        Get(self: GetPoint) -> GetResult
        
            After setting up options and so on, call GetPoint::Get to get a 3d point. The
                    point 
             is retrieved when the mouse goes down.
        
        Get(self: GetPoint, onMouseUp: bool, get2DPoint: bool) -> GetResult
        
            After setting up options and so on, call this method to get a 2d or 3d point.
        
            onMouseUp: If false, the point is returned when the left mouse button goes down.
                    If true, the 
             point is returned when the left mouse button goes up.
        
            get2DPoint: If true then get a 2d point otherwise get a 2d point
            Returns: Rhino.Input.GetResult.Point if the user chose a 3d point; Rhino.Input.GetResult.Point2d if the 
             user chose a 2d point; other enumeration value otherwise.
        
        Get(self: GetPoint, onMouseUp: bool) -> GetResult
        
            After setting up options and so on, call this method to get a 3d point.
        
            onMouseUp: If false, the point is returned when the left mouse button goes down.
                    If true, the 
             point is returned when the left mouse button goes up.
        
            Returns: Rhino.Input.GetResult.Point if the user chose a point; other enumeration value otherwise.
        """
        pass

    def GetConstructionPoints(self):
        """
        GetConstructionPoints(self: GetPoint) -> Array[Point3d]
        
            Gets current construction points.
            Returns: An array of points.
        """
        pass

    def GetSnapPoints(self):
        """
        GetSnapPoints(self: GetPoint) -> Array[Point3d]
        
            Gets current snap points.
            Returns: An array of points.
        """
        pass

    def InterruptMouseMove(self):
        """
        InterruptMouseMove(self: GetPoint) -> bool
        
            If you have lengthy computations in OnMouseMove() and/or DymanicDraw()
                    overrides, 
             then periodically call InterruptMouseMove() to see if you
                    should interrupt your 
             work because the mouse has moved again.
        
            Returns: true if you should interrupt your work; false otherwise.
        """
        pass

    def OnDynamicDraw(self, *args): #cannot find CLR method
        """
        OnDynamicDraw(self: GetPoint, e: GetPointDrawEventArgs)
            Default calls the DynamicDraw event.
        
            e: Current argument for the event.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: GetPoint, e: GetPointMouseEventArgs)
            Default calls the MouseDown event.
        
            e: Current argument for the event.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: GetPoint, e: GetPointMouseEventArgs)
            Calls the Rhino.Input.Custom.GetPoint.MouseMove event and can/should be called by overriding 
             implementation.
        
        
            e: Current argument for the event.
        """
        pass

    def OnPostDrawObjects(self, *args): #cannot find CLR method
        """
        OnPostDrawObjects(self: GetPoint, e: DrawEventArgs)
            In the "rare" case that you need to draw some depth buffered geometry during
                    a 
             GetPoint operation, override the OnPostDrawObjects function.
                    NOTE!! Overriding this 
             function comes with a significant performance penalty because the
                    scene needs to be 
             fully regenerated every frame where the standard
                    DynamicDraw event draws temporary 
             decorations (geometry) on top of a static scene.
        
        
            e: Current argument for the event.
        """
        pass

    def PermitConstraintOptions(self, permit):
        """
        PermitConstraintOptions(self: GetPoint, permit: bool)
            Control the availability of the built-in linear, planar, curve, and surface
                    
             constraint options like "Along", "AlongPerp", "AlongTan", "AlongParallel",
                    
             "Between", "OnCrv", "OnSrf", ".x", ".y", ".z", ".xy", etc.
        
        
            permit: if true, then the built-in contraint options are automatically avaiable in GetPoint.
        """
        pass

    def PermitElevatorMode(self, permitMode):
        """
        PermitElevatorMode(self: GetPoint, permitMode: int)
            Permits the use of the control key to define a line constraint.
        
            permitMode: 0: no elevator modes are permitted
                    1: fixed plane elevator mode (like the Line 
             command)
                    2: cplane elevator mode (like object dragging)
        """
        pass

    def PermitFromOption(self, permit):
        """
        PermitFromOption(self: GetPoint, permit: bool)
            Control the availability of the built-in "From" option. By default, the "From" option is enabled.
        
            permit: if true, then the "From" option is automatically avaiable in GetPoint.
        """
        pass

    def PermitObjectSnap(self, permit):
        """
        PermitObjectSnap(self: GetPoint, permit: bool)
            By default, object snaps like "end", "near", etc. are controled by the user.
                    If you 
             want to disable this ability, then call PermitObjectSnap(false).
        
        
            permit: true to permit snapping to objects.
        """
        pass

    def PermitOrthoSnap(self, permit):
        """
        PermitOrthoSnap(self: GetPoint, permit: bool)
            Controls availability of ortho snap. Default is true.
        
            permit: if true, then GetPoint pays attention to the Rhino "ortho snap" and "planar snap" settings
             
                    reported by ModelAidSettings.Ortho and ModelAidSettings.Planar.
        """
        pass

    def PermitTabMode(self, permit):
        """
        PermitTabMode(self: GetPoint, permit: bool)
            Permits the use of the tab key to define a line constraint.
        
            permit: If true, then the built-in tab key mode is available.
        """
        pass

    def PointOnCurve(self, t):
        """
        PointOnCurve(self: GetPoint) -> (Curve, float)
        
            Use to determine is point was on a curve.
            Returns: A curve at a specified parameter value.
        """
        pass

    def PointOnObject(self):
        """
        PointOnObject(self: GetPoint) -> ObjRef
        
            Call this function to see if the point was on an object. If the point was
                    on an 
             object an ObjRef is returned; otherwise null is returned.
        
            Returns: A point object reference.
        """
        pass

    def SetBasePoint(self, basePoint, showDistanceInStatusBar):
        """
        SetBasePoint(self: GetPoint, basePoint: Point3d, showDistanceInStatusBar: bool)
            Sets a base point used by ortho snap, from snap, planar snap, etc.
        
            basePoint: The new base point.
            showDistanceInStatusBar: If true, then the distance from base_point to the current point will be in the
                    
             status bar distance pane.
        """
        pass

    def SetCursor(self, cursor):
        """ SetCursor(self: GetPoint, cursor: Cursor) """
        pass

    def TryGetBasePoint(self, basePoint):
        """ TryGetBasePoint(self: GetPoint) -> (bool, Point3d) """
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

    DynamicDrawColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color used by CRhinoGetPoint::DynamicDraw to draw the current point and
            the line from the base point to the current point.

Get: DynamicDrawColor(self: GetPoint) -> Color

Set: DynamicDrawColor(self: GetPoint) = value
"""

    FullFrameRedrawDuringGet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """In the "RARE" case that you need to draw some depth buffered geometry during
            a Get() operation, setting this value to true will force entire frames to be redrawn
            while the user moves the mouse. This allows DisplayPipeline events to be triggered
            as well as OnPostDrawObjects
            NOTE!! Setting this value to true comes with a significant performance penalty because the
            scene needs to be fully regenerated every frame where the standard
            DynamicDraw event draws temporary decorations (geometry) on top of a static scene.

Get: FullFrameRedrawDuringGet(self: GetPoint) -> bool

Set: FullFrameRedrawDuringGet(self: GetPoint) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an arbitrary object that can be attached to this Rhino.Input.Custom.GetPoint instance.
            Useful for passing some/ information that you may need in a DynamicDraw event since you can get at this Tag from
            the GetPointDrawEventArgs.

Get: Tag(self: GetPoint) -> object

Set: Tag(self: GetPoint) = value
"""


    DynamicDraw = None
    MouseDown = None
    MouseMove = None
    PostDrawObjects = None


class GetPointDrawEventArgs(DrawEventArgs):
    # no doc
    CurrentPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPoint(self: GetPointDrawEventArgs) -> Point3d

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """GetPoint class that this draw event originated from.

Get: Source(self: GetPointDrawEventArgs) -> GetPoint

"""



class GetPointMouseEventArgs(EventArgs):
    # no doc
    ControlKeyDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlKeyDown(self: GetPointMouseEventArgs) -> bool

"""

    LeftButtonDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftButtonDown(self: GetPointMouseEventArgs) -> bool

"""

    MiddleButtonDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleButtonDown(self: GetPointMouseEventArgs) -> bool

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: GetPointMouseEventArgs) -> Point3d

"""

    RightButtonDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightButtonDown(self: GetPointMouseEventArgs) -> bool

"""

    ShiftKeyDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShiftKeyDown(self: GetPointMouseEventArgs) -> bool

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: GetPointMouseEventArgs) -> GetPoint

"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: GetPointMouseEventArgs) -> RhinoViewport

"""

    WindowPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowPoint(self: GetPointMouseEventArgs) -> Point

"""



class GetString(GetBaseClass, IDisposable):
    """ GetString() """
    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def Get(self):
        """
        Get(self: GetString) -> GetResult
        
            Returns the string that the user typed. By default, space stops the string input.
            Returns: The result type. If the user typed a string, this is Rhino.Input.GetResult.String.
        """
        pass

    def GetLiteralString(self):
        """
        GetLiteralString(self: GetString) -> GetResult
        
            Returns the string that the user typed. By default, space does not stop input.
            Returns: The result type. If the user typed a string, this is Rhino.Input.GetResult.String.
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


class GetTransform(GetPoint, IDisposable):
    # no doc
    def AddTransformObjects(self, list):
        """
        AddTransformObjects(self: GetTransform, list: TransformObjectList)
            Adds any objects you want transformed and grips you want transformed.
                    Make sure no 
             duplicates are in the list and that no grip ownwers are
                    passed in as objects.
        
        
            list: A custom transform object list.
        """
        pass

    def CalculateTransform(self, viewport, point):
        """
        CalculateTransform(self: GetTransform, viewport: RhinoViewport, point: Point3d) -> Transform
        
            Retrieves the final transformation.
                    Override this virtual function to provide your 
             own custom transformation method.
        
        
            viewport: A Rhino viewport that the user is using.
            point: A point that the user is selecting.
            Returns: A transformation matrix value.
        """
        pass

    def Dispose(self):
        """ Dispose(self: GetBaseClass, disposing: bool) """
        pass

    def GetXform(self):
        """
        GetXform(self: GetTransform) -> GetResult
        
            Gets the Transformation.
                    Call this after having set up options and so on.
            Returns: The result based on user choice.
        """
        pass

    def OnDynamicDraw(self, *args): #cannot find CLR method
        """
        OnDynamicDraw(self: GetPoint, e: GetPointDrawEventArgs)
            Default calls the DynamicDraw event.
        
            e: Current argument for the event.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: GetPoint, e: GetPointMouseEventArgs)
            Default calls the MouseDown event.
        
            e: Current argument for the event.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: GetPoint, e: GetPointMouseEventArgs)
            Calls the Rhino.Input.Custom.GetPoint.MouseMove event and can/should be called by overriding 
             implementation.
        
        
            e: Current argument for the event.
        """
        pass

    def OnPostDrawObjects(self, *args): #cannot find CLR method
        """
        OnPostDrawObjects(self: GetPoint, e: DrawEventArgs)
            In the "rare" case that you need to draw some depth buffered geometry during
                    a 
             GetPoint operation, override the OnPostDrawObjects function.
                    NOTE!! Overriding this 
             function comes with a significant performance penalty because the
                    scene needs to be 
             fully regenerated every frame where the standard
                    DynamicDraw event draws temporary 
             decorations (geometry) on top of a static scene.
        
        
            e: Current argument for the event.
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

    HaveTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HaveTransform(self: GetTransform) -> bool

Set: HaveTransform(self: GetTransform) = value
"""

    ObjectList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectList(self: GetTransform) -> TransformObjectList

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: GetTransform) -> Transform

Set: Transform(self: GetTransform) = value
"""



class OptionColor(object, IDisposable):
    """ OptionColor(initialValue: Color) """
    def Dispose(self):
        """ Dispose(self: OptionColor) """
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
    def __new__(self, initialValue):
        """ __new__(cls: type, initialValue: Color) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValue(self: OptionColor) -> Color

Set: CurrentValue(self: OptionColor) = value
"""

    InitialValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialValue(self: OptionColor) -> Color

"""



class OptionDouble(object, IDisposable):
    """
    OptionDouble(initialValue: float)
    OptionDouble(initialValue: float, lowerLimit: float, upperLimit: float)
    OptionDouble(initialValue: float, setLowerLimit: bool, limit: float)
    """
    def Dispose(self):
        """ Dispose(self: OptionDouble) """
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
    def __new__(self, initialValue, *__args):
        """
        __new__(cls: type, initialValue: float)
        __new__(cls: type, initialValue: float, lowerLimit: float, upperLimit: float)
        __new__(cls: type, initialValue: float, setLowerLimit: bool, limit: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValue(self: OptionDouble) -> float

Set: CurrentValue(self: OptionDouble) = value
"""

    InitialValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialValue(self: OptionDouble) -> float

"""



class OptionInteger(object, IDisposable):
    """
    OptionInteger(initialValue: int)
    OptionInteger(initialValue: int, lowerLimit: int, upperLimit: int)
    OptionInteger(initialValue: int, setLowerLimit: bool, limit: int)
    """
    def Dispose(self):
        """ Dispose(self: OptionInteger) """
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
    def __new__(self, initialValue, *__args):
        """
        __new__(cls: type, initialValue: int)
        __new__(cls: type, initialValue: int, lowerLimit: int, upperLimit: int)
        __new__(cls: type, initialValue: int, setLowerLimit: bool, limit: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValue(self: OptionInteger) -> int

Set: CurrentValue(self: OptionInteger) = value
"""

    InitialValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialValue(self: OptionInteger) -> int

"""



class OptionToggle(object, IDisposable):
    """
    OptionToggle(initialValue: bool, offValue: str, onValue: str)
    OptionToggle(initialValue: bool, offValue: LocalizeStringPair, onValue: LocalizeStringPair)
    """
    def Dispose(self):
        """ Dispose(self: OptionToggle) """
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
    def __new__(self, initialValue, offValue, onValue):
        """
        __new__(cls: type, initialValue: bool, offValue: str, onValue: str)
        __new__(cls: type, initialValue: bool, offValue: LocalizeStringPair, onValue: LocalizeStringPair)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValue(self: OptionToggle) -> bool

Set: CurrentValue(self: OptionToggle) = value
"""

    InitialValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialValue(self: OptionToggle) -> bool

"""



class PickContext(object, IDisposable):
    """
    Provides storage for picking operations.
    
    PickContext()
    """
    def Dispose(self):
        """ Dispose(self: PickContext) """
        pass

    def PickFrustumTest(self, *__args):
        """
        PickFrustumTest(self: PickContext, curve: NurbsCurve) -> (bool, float, float, float)
        PickFrustumTest(self: PickContext, bezier: BezierCurve) -> (bool, float, float, float)
        PickFrustumTest(self: PickContext, mesh: Mesh, pickStyle: MeshPickStyle) -> (bool, Point3d, float, float, MeshHitFlag, int)
        PickFrustumTest(self: PickContext, mesh: Mesh, pickStyle: MeshPickStyle) -> (bool, Point3d, Point2d, Point2d, float, float, MeshHitFlag, int)
        PickFrustumTest(self: PickContext, line: Line) -> (bool, float, float, float)
        PickFrustumTest(self: PickContext, point: Point3d) -> (bool, float, float)
        
            Utility for picking 3d point
            Returns: true if there is a hit
        PickFrustumTest(self: PickContext, box: BoundingBox) -> (bool, bool)
        
            Fast test to check if a bounding box intersects a pick frustum.
            Returns: False if bbox is invalid or box does not intersect the pick frustum
        PickFrustumTest(self: PickContext, cloud: PointCloud) -> (bool, int, float, float)
        PickFrustumTest(self: PickContext, points: Array[Point3d]) -> (bool, int, float, float)
        """
        pass

    def PickMeshTopologyVertices(self, mesh):
        """
        PickMeshTopologyVertices(self: PickContext, mesh: Mesh) -> Array[int]
        
            Utility for picking mesh vertices
            Returns: indices of mesh topology vertices that were picked
        """
        pass

    def SetPickTransform(self, transform):
        """ SetPickTransform(self: PickContext, transform: Transform) """
        pass

    def UpdateClippingPlanes(self):
        """
        UpdateClippingPlanes(self: PickContext)
            Updates the clipping plane information in pick region. The
                    SetClippingPlanes and 
             View fields must be called before calling
                    UpdateClippingPlanes().
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GetObjectUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetObjectUsed(self: PickContext) -> GetObject

"""

    PickGroupsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thue if GroupObjects should be added to the pick list

Get: PickGroupsEnabled(self: PickContext) -> bool

Set: PickGroupsEnabled(self: PickContext) = value
"""

    PickLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """pick chord starts on near clipping plane and ends on far clipping plane.

Get: PickLine(self: PickContext) -> Line

Set: PickLine(self: PickContext) = value
"""

    PickMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickMode(self: PickContext) -> PickMode

Set: PickMode(self: PickContext) = value
"""

    PickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickStyle(self: PickContext) -> PickStyle

Set: PickStyle(self: PickContext) = value
"""

    SubObjectSelectionEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the user had activated subobject selection

Get: SubObjectSelectionEnabled(self: PickContext) -> bool

Set: SubObjectSelectionEnabled(self: PickContext) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This view can be a model view or a page view. When view is a page view,
            then you need to distingish between the viewports MainViewport() and
            ActiveViewport().  When m_view is a model view, both MainViewport() and
            ActiveViewport() return the world view's viewport.

Get: View(self: PickContext) -> RhinoView

Set: View(self: PickContext) = value
"""


    MeshHitFlag = None
    MeshPickStyle = None


class PickMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Picking can happen in wireframe or shaded display mode
    
    enum PickMode, values: Shaded (2), Wireframe (1)
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

    Shaded = None
    value__ = None
    Wireframe = None


class PickStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides picking values that describe common CAD picking behavior.
    
    enum PickStyle, values: CrossingPick (3), None (0), PointPick (1), WindowPick (2)
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

    CrossingPick = None
    None = None
    PointPick = None
    value__ = None
    WindowPick = None


