# encoding: utf-8
# module Rhino.Input calls itself Input
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GetBoxMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all Box getter modes.
    
    enum GetBoxMode, values: All (0), Center (4), Corner (1), ThreePoint (2), Vertical (3)
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

    All = None
    Center = None
    Corner = None
    ThreePoint = None
    value__ = None
    Vertical = None


class GetResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results from GetObject.Get(), GetPoint.Get(), etc...
    
    enum GetResult, values: Angle (20), Cancel (1), Circle (16), Color (5), CustomMessage (14), Cylinder (18), Direction (22), Distance (21), ExitRhino (268435455), Frame (23), Line2d (10), Miss (7), NoResult (0), Nothing (2), Number (4), Object (12), Option (3), Plane (17), Point (8), Point2d (9), Rectangle2d (11), Sphere (19), String (13), Timeout (15), Undo (6), User1 (4294967295), User2 (4294967294), User3 (4294967293), User4 (4294967292), User5 (4294967291)
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

    Angle = None
    Cancel = None
    Circle = None
    Color = None
    CustomMessage = None
    Cylinder = None
    Direction = None
    Distance = None
    ExitRhino = None
    Frame = None
    Line2d = None
    Miss = None
    NoResult = None
    Nothing = None
    Number = None
    Object = None
    Option = None
    Plane = None
    Point = None
    Point2d = None
    Rectangle2d = None
    Sphere = None
    String = None
    Timeout = None
    Undo = None
    User1 = None
    User2 = None
    User3 = None
    User4 = None
    User5 = None
    value__ = None


class RhinoGet(object):
    """
    Base class for GetObject, GetPoint, GetSphere, etc.
                
                You will never directly create a RhinoGet but you will use its member
                functions after calling GetObject::GetObjects(), GetPoint::GetPoint(), and so on.
                
                Provides tools to set command prompt, set command options, and specify
                if the "get" can optionally accept numbers, nothing (pressing enter),
                and undo.
    """
    @staticmethod
    def Get2dRectangle(solidPen, rectangle, rectView):
        """
        Get2dRectangle(solidPen: bool) -> (Result, Rectangle, RhinoView)
        
            Gets a rectangle in view window coordinates.
        
            solidPen: If true, a solid pen is used for drawing while the user selects a rectangle.
                    If 
             false, a dotted pen is used for drawing while the user selects a rectangle.
        
            Returns: Success or Cancel.
        """
        pass

    @staticmethod
    def GetAngle(commandPrompt, basePoint, referencePoint, defaultAngleRadians, angleRadians):
        """
        GetAngle(commandPrompt: str, basePoint: Point3d, referencePoint: Point3d, defaultAngleRadians: float) -> (Result, float)
        
            Allows user to interactively pick an angle
        
            commandPrompt: if null, a default prompt will be displayed
        """
        pass

    @staticmethod
    def GetArc(arc):
        """ GetArc() -> (Result, Arc) """
        pass

    @staticmethod
    def GetBool(prompt, acceptNothing, offPrompt, onPrompt, boolValue):
        """
        GetBool(prompt: str, acceptNothing: bool, offPrompt: str, onPrompt: str, boolValue: bool) -> (Result, bool)
        
            Easy to use bool getter.
        
            prompt: Command prompt.
            acceptNothing: If true, the user can press enter.
            offPrompt: The 'false/off' message.
            onPrompt: The 'true/on' message.
            boolValue: Default bool value set to this and returned here.
            Returns: The getter result based on user choice.
                    Commands.Result.Success - got 
             value.Commands.Result.Nothing - user pressed enter.Commands.Result.Cancel - user cancelled value 
             getting.
        """
        pass

    @staticmethod
    def GetBox(box, mode=None, basePoint=None, prompt1=None, prompt2=None, prompt3=None):
        """
        GetBox(mode: GetBoxMode, basePoint: Point3d, prompt1: str, prompt2: str, prompt3: str) -> (Result, Box)
        
            Asks the user to select a Box in the viewport.
        
            mode: A particular "get box" mode, or Rhino.Input.GetBoxMode.All.
            basePoint: Optional base point. Supply Point3d.Unset if you don't want to use this.
            prompt1: Optional first prompt. Supply null to use the default prompt.
            prompt2: Optional second prompt. Supply null to use the default prompt.
            prompt3: Optional third prompt. Supply null to use the default prompt.
            Returns: Commands.Result.Success if successful.
        GetBox() -> (Result, Box)
        
            Asks the user to select a Box in the viewport.
            Returns: Commands.Result.Success if successful.
        """
        pass

    @staticmethod
    def GetCircle(circle):
        """ GetCircle() -> (Result, Circle) """
        pass

    @staticmethod
    def GetColor(prompt, acceptNothing, color):
        """
        GetColor(prompt: str, acceptNothing: bool, color: Color) -> (Result, Color)
        
            Easy to use color getter.
        
            prompt: Command prompt.
            acceptNothing: If true, the user can press enter.
            color: Color value returned here. also used as default color.
            Returns: Commands.Result.Success - got color.Commands.Result.Nothing - user pressed 
             enter.Commands.Result.Cancel - user cancel color getting.
        """
        pass

    @staticmethod
    def GetFileName(mode, defaultName, title, parent):
        """ GetFileName(mode: GetFileNameMode, defaultName: str, title: str, parent: IWin32Window) -> str """
        pass

    @staticmethod
    def GetFileNameScripted(mode, defaultName):
        """ GetFileNameScripted(mode: GetFileNameMode, defaultName: str) -> str """
        pass

    @staticmethod
    def GetGrip(grip, prompt):
        """ GetGrip(prompt: str) -> (Result, GripObject) """
        pass

    @staticmethod
    def GetGrips(grips, prompt):
        """ GetGrips(prompt: str) -> (Result, Array[GripObject]) """
        pass

    @staticmethod
    def GetHelix(helix):
        """ GetHelix() -> (Result, NurbsCurve) """
        pass

    @staticmethod
    def GetInteger(prompt, acceptNothing, outputNumber, lowerLimit=None, upperLimit=None):
        """
        GetInteger(prompt: str, acceptNothing: bool, outputNumber: int, lowerLimit: int, upperLimit: int) -> (Result, int)
        
            Easy to use number getter.
        
            prompt: The command prompt.
            acceptNothing: If true, the user can press enter.
            outputNumber: default number is set to this value and number value returned here.
            lowerLimit: The minimum allowed value.
            upperLimit: The maximum allowed value.
            Returns: Commands.Result.Success - got number
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel number getting.
        
        GetInteger(prompt: str, acceptNothing: bool, outputNumber: int) -> (Result, int)
        
            Easy to use number getter.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            outputNumber: default number is set to this value and number value returned here.
            Returns: Commands.Result.Success - got number
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel number getting.
        """
        pass

    @staticmethod
    def GetLine(line):
        """ GetLine() -> (Result, Line) """
        pass

    @staticmethod
    def GetLinearDimension(dimension):
        """ GetLinearDimension() -> (Result, LinearDimension) """
        pass

    @staticmethod
    def GetMultipleObjects(prompt, acceptNothing, filter, rhObjects):
        """
        GetMultipleObjects(prompt: str, acceptNothing: bool, filter: GetObjectGeometryFilter) -> (Result, Array[ObjRef])
        
            Easy to use object getter for getting multiple objects.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            filter: geometry filter to use when getting objects.
            Returns: Commands.Result.Success - got object
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel object getting.
        
        GetMultipleObjects(prompt: str, acceptNothing: bool, filter: ObjectType) -> (Result, Array[ObjRef])
        
            Easy to use object getter for getting multiple objects.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            filter: geometry filter to use when getting objects.
            Returns: Commands.Result.Success - got object
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel object getting.
        """
        pass

    @staticmethod
    def GetNumber(prompt, acceptNothing, outputNumber, lowerLimit=None, upperLimit=None):
        """
        GetNumber(prompt: str, acceptNothing: bool, outputNumber: float) -> (Result, float)
        
            Easy to use number getter.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            outputNumber: default number is set to this value and number value returned here.
            Returns: Commands.Result.Success - got number
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel number getting.
        
        GetNumber(prompt: str, acceptNothing: bool, outputNumber: float, lowerLimit: float, upperLimit: float) -> (Result, float)
        
            Easy to use number getter.
        
            prompt: The command prompt.
            acceptNothing: If true, the user can press Enter.
            outputNumber: Default number is set to this value and the return number value is assigned to this variable 
             during the call.
        
            lowerLimit: The minimum allowed value.
            upperLimit: The maximum allowed value.
            Returns: Commands.Result.Success - got number.Commands.Result.Nothing - user pressed 
             enter.Commands.Result.Cancel - user cancel number getting.
        """
        pass

    @staticmethod
    def GetOneObject(prompt, acceptNothing, filter, *__args):
        """
        GetOneObject(prompt: str, acceptNothing: bool, filter: GetObjectGeometryFilter) -> (Result, ObjRef)
        
            Easy to use object getter.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            filter: geometry filter to use when getting objects.
            Returns: Commands.Result.Success - got object
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel object getting.
        
        GetOneObject(prompt: str, acceptNothing: bool, filter: ObjectType) -> (Result, ObjRef)
        
            Easy to use object getter.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            filter: geometry filter to use when getting objects.
            Returns: Commands.Result.Success - got object
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel object getting.
        """
        pass

    @staticmethod
    def GetPlane(plane):
        """
        GetPlane() -> (Result, Plane)
        
            Gets an oriented infinite plane.
            Returns: Commands.Result.Success - got plane.Commands.Result.Nothing - user pressed 
             enter.Commands.Result.Cancel - user cancel number getting.
        """
        pass

    @staticmethod
    def GetPoint(prompt, acceptNothing, point):
        """
        GetPoint(prompt: str, acceptNothing: bool) -> (Result, Point3d)
        
            Gets a point coordinate from the document.
        
            prompt: Prompt to display in command line during the operation.
            acceptNothing: if true, the user can press enter.
            Returns: Commands.Result.Success - got point
                    Commands.Result.Nothing - user pressed enter
          
                       Commands.Result.Cancel - user cancel point getting.
        """
        pass

    @staticmethod
    def GetPointOnMesh(*__args):
        """
        GetPointOnMesh(meshObject: MeshObject, prompt: str, acceptNothing: bool) -> (Result, Point3d)
        
            Gets a point constrained to an existing mesh in the document.
        
            meshObject: An mesh object in the document.
            prompt: Text prompt.
            acceptNothing: true if nothing else should be accepted.
            Returns: The command result based on user choice.
        GetPointOnMesh(meshObjectId: Guid, prompt: str, acceptNothing: bool) -> (Result, Point3d)
        
            Gets a point constrained to an existing mesh in the document.
        
            meshObjectId: An ID of a mesh in the document.
            prompt: Text prompt.
            acceptNothing: true if nothing else should be accepted.
            Returns: A command result based on user choice.
        """
        pass

    @staticmethod
    def GetPolyline(polyline):
        """ GetPolyline() -> (Result, Polyline) """
        pass

    @staticmethod
    def GetRectangle(*__args):
        """
        GetRectangle(mode: GetBoxMode, firstPoint: Point3d, prompts: IEnumerable[str]) -> (Result, Array[Point3d])
        GetRectangle() -> (Result, Array[Point3d])
        
            Gets a 3d rectangle.
            Returns: Commands.Result.Success if successful.
        """
        pass

    @staticmethod
    def GetSpiral(spiral):
        """ GetSpiral() -> (Result, NurbsCurve) """
        pass

    @staticmethod
    def GetString(prompt, acceptNothing, outputString):
        """
        GetString(prompt: str, acceptNothing: bool, outputString: str) -> (Result, str)
        
            Easy to use string getter.
        
            prompt: command prompt.
            acceptNothing: if true, the user can press enter.
            outputString: default string set to this value and string value returned here.
            Returns: Commands.Result.Success - got string
                    Commands.Result.Nothing - user pressed enter
         
                        Commands.Result.Cancel - user cancel string getting.
        """
        pass

    @staticmethod
    def GetView(commandPrompt, view):
        """
        GetView(commandPrompt: str) -> (Result, RhinoView)
        
            Allows the user to interactively pick a viewport.
        
            commandPrompt: The command prompt during the request.
            Returns: The result based on user choice.
        """
        pass

    @staticmethod
    def InGet(doc):
        """
        InGet(doc: RhinoDoc) -> bool
        
            Returns true if the document is current in a "Get" operation.
            Returns: true if a getter is currently active.
        """
        pass

    __all__ = [
        'Get2dRectangle',
        'GetAngle',
        'GetArc',
        'GetBool',
        'GetBox',
        'GetCircle',
        'GetColor',
        'GetFileName',
        'GetFileNameScripted',
        'GetGrip',
        'GetGrips',
        'GetHelix',
        'GetInteger',
        'GetLine',
        'GetLinearDimension',
        'GetMultipleObjects',
        'GetNumber',
        'GetOneObject',
        'GetPlane',
        'GetPoint',
        'GetPointOnMesh',
        'GetPolyline',
        'GetRectangle',
        'GetSpiral',
        'GetString',
        'GetView',
        'InGet',
    ]


# variables with complex values

