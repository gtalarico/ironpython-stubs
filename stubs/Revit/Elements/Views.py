# encoding: utf-8
# module Revit.Elements.Views calls itself Views
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class View(Element, IDisposable, IGraphicItem, IFormattable):
    """ An abstract Revit View - All view types inherit from this type """
    def AddFilter(self, parameterFilter):
        """
        AddFilter(self: View, parameterFilter: ParameterFilterElement)
            Add Filter to View
        
            parameterFilter: Parameter filter
        """
        pass

    def ExportAsImage(self, path):
        """
        ExportAsImage(self: View, path: str) -> Bitmap
        
            Export the view as an image to the given path - defaults to png, but you can 
             override 
                    the file type but supplying a path with the appropriate 
             extension
        
        
            path: A valid path for the image
            Returns: The image
        """
        pass

    def FilterOverrides(self, parameterFilter):
        """
        FilterOverrides(self: View, parameterFilter: ParameterFilterElement) -> OverrideGraphicSettings
        
            Get Filter overrides
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def SetFilterOverrides(self, parameterFilter, overrides):
        """
        SetFilterOverrides(self: View, parameterFilter: ParameterFilterElement, overrides: OverrideGraphicSettings)
            Set Filter overrides
        
            parameterFilter: Parameter filter
            overrides: overrides settings
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """ ToString(self: View) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get View Filters

Get: Filters(self: View) -> IEnumerable[ParameterFilterElement]

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class View3D(View, IDisposable, IGraphicItem, IFormattable):
    # no doc
    def BuildOrientation3D(self, *args): #cannot find CLR method
        """
        BuildOrientation3D(eyePoint: XYZ, target: XYZ) -> ViewOrientation3D
        
            Build Orientation3D object for eye point and a target point
        """
        pass

    def Create3DView(self, *args): #cannot find CLR method
        """
        Create3DView(orient: ViewOrientation3D, name: str, isPerspective: bool) -> View3D
        
            Create a Revit 3D View
        """
        pass

    @staticmethod
    def CreateUniqueViewName(name):
        """
        CreateUniqueViewName(name: str) -> str
        
            Determines whether a view with the provided name already exists.
                    
             If a view exists with the provided name, and new view is created with
                 
                a unique name. Otherwise, the original view name is returned.
        
            Returns: The original name if it is already unique, or 
                    a unique version of 
             the name.
        """
        pass

    def GetPointCloud(self, *args): #cannot find CLR method
        """ GetPointCloud(solid: Solid, pts: List[XYZ])GetPointCloud(geomInst: GeometryInstance, pts: List[XYZ])GetPointCloud(e: Element, pts: List[XYZ]) """
        pass

    def GetVisibleElementFilter(self, *args): #cannot find CLR method
        """
        GetVisibleElementFilter() -> FilteredElementCollector
        
            Utility method to create a filtered element collector which collects all 
             elements in a view
                    which Dynamo would like to view or on which 
             Dynamo would like to operate.
        """
        pass

    def InternalIsolateInView(self, *args): #cannot find CLR method
        """
        InternalIsolateInView(self: View3D, bbox: BoundingBoxXYZ)
            Isolate the bounding box in the current view
        InternalIsolateInView(self: View3D, element: Element)
            Isolate the element in the current view by creating a mininum size crop box 
             around it
        """
        pass

    def InternalRemoveIsolation(self, *args): #cannot find CLR method
        """
        InternalRemoveIsolation(self: View3D)
            Show all hiddent elements in the view
        """
        pass

    def InternalSetName(self, *args): #cannot find CLR method
        """
        InternalSetName(self: View3D, name: str)
            Set the name of the current view
        """
        pass

    def InternalSetOrientation(self, *args): #cannot find CLR method
        """
        InternalSetOrientation(self: View3D, orient: ViewOrientation3D)
            Set the orientation of the view
        """
        pass

    def InternalSetView3D(self, *args): #cannot find CLR method
        """
        InternalSetView3D(self: View3D, view: View3D)
            Set the InternalView3D property and the associated element id and unique id
        """
        pass

    def IsolateInView(self, *args): #cannot find CLR method
        """
        IsolateInView(view: View3D, element: Element)
            Make a single element appear in a particular view
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: View3D) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    DEFAULT_VIEW_NAME = 'dynamo3D'
    InternalUniqueId = None


class AxonometricView(View3D, IDisposable, IGraphicItem, IFormattable):
    """ A Revit View3D """
    @staticmethod
    def ByEyePointAndTarget(eyePoint, target, name):
        """
        ByEyePointAndTarget(eyePoint: Point, target: Point, name: str) -> AxonometricView
        
            Create a Revit Axonometric (isometric) View from an eye position
                    
             and a target position.
        
        
            eyePoint: A Point representing the eye point in meters.
            target: A Point representing the target of view in meters.
            name: The name of the view.
            Returns: An AxonometricView object.
        """
        pass

    @staticmethod
    def ByEyePointTargetAndBoundingBox(eyePoint, target, boundingBox, name, isolateElement):
        """
        ByEyePointTargetAndBoundingBox(eyePoint: Point, target: Point, boundingBox: BoundingBox, name: str, isolateElement: bool) -> AxonometricView
        
            Create a Revit Axonometric (isometric) View from an Eye position and target 
             position and Bounding Box
        
        
            eyePoint: A Point representing the eye point.
            target: A Point representing the target of view.
            boundingBox: A BoundingBox. The view will be cropped to this bounding box
            name: The name of the view.
            isolateElement: If this argument is set to true, the element or 
                    bounding box will 
             be isolated in the current view by creating a minimum size
                    crop 
             box around it.
        
            Returns: An AxonometricView object.
        """
        pass

    @staticmethod
    def ByEyePointTargetAndElement(eyePoint, target, name, element, isolateElement):
        """
        ByEyePointTargetAndElement(eyePoint: Point, target: Point, name: str, element: Element, isolateElement: bool) -> AxonometricView
        
            Create a Revit Axonometric (isometric) View from an Eye position and target 
             position and Element
        
        
            eyePoint: A Point representing the eye point.
            target: A Point representing the target of view.
            name: The name of the view.
            element: This argument cannot be null, and it has to be either a 
                    
             Revit.Elements.Element or  Revit.GeometryObjectsBoundingBox.
        
            isolateElement: If this argument is set to true, the element or 
                    bounding box will 
             be isolated in the current view by creating a minimum size
                    crop 
             box around it.
        
            Returns: An AxonometricView object.
        """
        pass

    def InternalIsolateInView(self, *args): #cannot find CLR method
        """
        InternalIsolateInView(self: View3D, bbox: BoundingBoxXYZ)
            Isolate the bounding box in the current view
        InternalIsolateInView(self: View3D, element: Element)
            Isolate the element in the current view by creating a mininum size crop box 
             around it
        """
        pass

    def InternalRemoveIsolation(self, *args): #cannot find CLR method
        """
        InternalRemoveIsolation(self: View3D)
            Show all hiddent elements in the view
        """
        pass

    def InternalSetName(self, *args): #cannot find CLR method
        """
        InternalSetName(self: View3D, name: str)
            Set the name of the current view
        """
        pass

    def InternalSetOrientation(self, *args): #cannot find CLR method
        """
        InternalSetOrientation(self: View3D, orient: ViewOrientation3D)
            Set the orientation of the view
        """
        pass

    def InternalSetView3D(self, *args): #cannot find CLR method
        """
        InternalSetView3D(self: View3D, view: View3D)
            Set the InternalView3D property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class CeilingPlanView(PlanView, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewPlan """
    @staticmethod
    def ByLevel(level):
        """
        ByLevel(level: Level) -> CeilingPlanView
        
            Create a Revit Floor Plan at a given Level
        """
        pass

    def InternalSetPlanView(self, *args): #cannot find CLR method
        """
        InternalSetPlanView(self: PlanView, plan: ViewPlan)
            Set the InternalViewPlan property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class DraftingView(View, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewDrafting """
    @staticmethod
    def ByName(name):
        """
        ByName(name: str) -> DraftingView
        
            Create a Revit DraftingView given it's name
        
            name: Name of the view
            Returns: The view
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: DraftingView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class FloorPlanView(PlanView, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewPlan """
    @staticmethod
    def ByLevel(level):
        """
        ByLevel(level: Level) -> FloorPlanView
        
            Create a Revit Floor Plan at a given Level
        """
        pass

    def InternalSetPlanView(self, *args): #cannot find CLR method
        """
        InternalSetPlanView(self: PlanView, plan: ViewPlan)
            Set the InternalViewPlan property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class PerspectiveView(View3D, IDisposable, IGraphicItem, IFormattable):
    """ A Revit View3D """
    @staticmethod
    def ByEyePointAndTarget(eyePoint, target, element, name, isolateElement):
        """
        ByEyePointAndTarget(eyePoint: Point, target: Point, element: object, name: str, isolateElement: bool) -> PerspectiveView
        
            Create a Revit Perspective View from an Eye position, a target position, and 
         
                        either an Element or BoundingBox.
        
        
            eyePoint: A Point representing the eye point.
            target: A Point representing the target of view.
            element: This argument cannot be null, and it has to be either a 
                    
             Revit.Elements.Element or  Revit.GeometryObjectsBoundingBox.
        
            name: The name of the view.
            isolateElement: If this argument is set to true, the element or 
                    bounding box will 
             be isolated in the current view by creating a minimum size
                    crop 
             box around it.
        
            Returns: Returns the resulting PerspectiveView object.
        """
        pass

    @staticmethod
    def ByEyePointTargetAndBoundingBox(eyePoint, target, boundingBox, name, isolateElement):
        """
        ByEyePointTargetAndBoundingBox(eyePoint: Point, target: Point, boundingBox: BoundingBox, name: str, isolateElement: bool) -> PerspectiveView
        
            Create a Revit Perspective View from an Eye position and target position and 
             Bounding Box
        
        
            eyePoint: Eye point in meters
            target: Target of view in meters
            boundingBox: Bounding box represented in meters
        """
        pass

    @staticmethod
    def ByEyePointTargetAndElement(eyePoint, target, element, name, isolateElement):
        """
        ByEyePointTargetAndElement(eyePoint: Point, target: Point, element: Element, name: str, isolateElement: bool) -> PerspectiveView
        
            Create a Revit Perspective View from an Eye position and target position and 
             Element
        """
        pass

    def InternalIsolateInView(self, *args): #cannot find CLR method
        """
        InternalIsolateInView(self: View3D, bbox: BoundingBoxXYZ)
            Isolate the bounding box in the current view
        InternalIsolateInView(self: View3D, element: Element)
            Isolate the element in the current view by creating a mininum size crop box 
             around it
        """
        pass

    def InternalRemoveIsolation(self, *args): #cannot find CLR method
        """
        InternalRemoveIsolation(self: View3D)
            Show all hiddent elements in the view
        """
        pass

    def InternalSetName(self, *args): #cannot find CLR method
        """
        InternalSetName(self: View3D, name: str)
            Set the name of the current view
        """
        pass

    def InternalSetOrientation(self, *args): #cannot find CLR method
        """
        InternalSetOrientation(self: View3D, orient: ViewOrientation3D)
            Set the orientation of the view
        """
        pass

    def InternalSetView3D(self, *args): #cannot find CLR method
        """
        InternalSetView3D(self: View3D, view: View3D)
            Set the InternalView3D property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class SectionView(View, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewSection """
    @staticmethod
    def ByBoundingBox(box):
        """
        ByBoundingBox(box: BoundingBox) -> SectionView
        
            Create a Revit ViewSection by a bounding box
        
            box: The bounding box of the view in meters
        """
        pass

    @staticmethod
    def ByCoordinateSystemMinPointMaxPoint(cs, minPoint, maxPoint):
        """
        ByCoordinateSystemMinPointMaxPoint(cs: CoordinateSystem, minPoint: Point, maxPoint: Point) -> SectionView
        
            Creates a Revit ViewSection by a specified corrdinate system, minPoint and 
             maxPoint
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: SectionView) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


class Sheet(Element, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewSheet """
    @staticmethod
    def ByNameNumberTitleBlockAndView(sheetName, sheetNumber, titleBlockFamilyType, view):
        """
        ByNameNumberTitleBlockAndView(sheetName: str, sheetNumber: str, titleBlockFamilyType: FamilyType, view: View) -> Sheet
        
            Create a Revit Sheet by the sheet name, number, a title block FamilyType, and a 
             collection of views.  This method will automatically
                    pack the view 
             onto the sheet.
        """
        pass

    @staticmethod
    def ByNameNumberTitleBlockAndViews(sheetName, sheetNumber, titleBlockFamilyType, views):
        """
        ByNameNumberTitleBlockAndViews(sheetName: str, sheetNumber: str, titleBlockFamilyType: FamilyType, views: Array[View]) -> Sheet
        
            Create a Revit Sheet by the sheet name, number, a title block FamilyType, and a 
             collection of views.  This method will automatically
                    pack the 
             views onto the sheet.
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference to the Element

Get: InternalElement(self: Sheet) -> Element

"""

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""

    SheetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the SheetName of the Sheet

Get: SheetName(self: Sheet) -> str

"""

    SheetNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the SheetNumber of the Sheet

Get: SheetNumber(self: Sheet) -> str

"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Views on a Sheet

Get: Views(self: Sheet) -> Array[View]

"""


    InternalUniqueId = None


class StructuralPlanView(PlanView, IDisposable, IGraphicItem, IFormattable):
    """ A Revit ViewPlan """
    @staticmethod
    def ByLevel(level):
        """
        ByLevel(level: Level) -> StructuralPlanView
        
            Create a Structural Plan View at the given Level.
        
            level: The Level on which the StructuralPlanView is based.
            Returns: A StructuralPlanView if successful.
        """
        pass

    def InternalSetPlanView(self, *args): #cannot find CLR method
        """
        InternalSetPlanView(self: PlanView, plan: ViewPlan)
            Set the InternalViewPlan property and the associated element id and unique id
        """
        pass

    def SafeInit(self, *args): #cannot find CLR method
        """
        SafeInit(self: Element, init: Action)
            Handling exceptions when calling the initializing function
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InternalElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id for this element

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is this element still alive in Revit, and good to be drawn, queried etc.

"""


    InternalUniqueId = None


