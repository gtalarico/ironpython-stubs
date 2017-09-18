# encoding: utf-8
# module Rhino.DocObjects.Custom calls itself Custom
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CustomBrepObject(BrepObject, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: CustomBrepObject) """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, brep: Brep)
        """
        pass


class CustomCurveObject(CurveObject, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: CustomCurveObject) """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
        """
        pass

    def SetCurve(self, *args): #cannot find CLR method
        """
        SetCurve(self: CustomCurveObject, curve: Curve) -> Curve
        
            Only for developers who are defining custom subclasses of CurveObject.
                    Directly 
             sets the internal curve geometry for this object.  Note that
                    this function does not 
             work with Rhino's "undo".
        
            Returns: The old curve geometry that was set for this object
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, curve: Curve)
        """
        pass


class CustomGripObject(GripObject, IDisposable):
    """ CustomGripObject() """
    def Dispose(self):
        """ Dispose(self: CustomGripObject) """
        pass

    def NewLocation(self):
        """ NewLocation(self: CustomGripObject) """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
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

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: CustomGripObject) -> int

Set: Index(self: CustomGripObject) = value
"""

    OriginalLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalLocation(self: CustomGripObject) -> Point3d

Set: OriginalLocation(self: CustomGripObject) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: CustomGripObject) -> float

Set: Weight(self: CustomGripObject) = value
"""



class CustomMeshObject(MeshObject, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: CustomMeshObject) """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
        """
        pass

    def SetMesh(self, *args): #cannot find CLR method
        """
        SetMesh(self: MeshObject, mesh: Mesh) -> Mesh
        
            Only for developers who are defining custom subclasses of MeshObject.
                    Directly sets 
             the internal mesh geometry for this object.  Note that
                    this function does not work 
             with Rhino's "undo".
        
            Returns: The old mesh geometry that was set for this object
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, mesh: Mesh)
        """
        pass


class CustomObjectGrips(object, IDisposable):
    # no doc
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: CustomObjectGrips, grip: CustomGripObject) """
        pass

    def Dispose(self):
        """ Dispose(self: CustomObjectGrips) """
        pass

    @staticmethod
    def Dragging():
        """
        Dragging() -> bool
        
            Determines if grips are currently being dragged.
            Returns: true if grips are dragged.
        """
        pass

    def Grip(self, index):
        """ Grip(self: CustomObjectGrips, index: int) -> CustomGripObject """
        pass

    def NeighborGrip(self, *args): #cannot find CLR method
        """
        NeighborGrip(self: CustomObjectGrips, gripIndex: int, dr: int, ds: int, dt: int, wrap: bool) -> GripObject
        
            Get neighbors.
        
            gripIndex: index of grip where the search begins.
            dr: 1 = next grip in the first parameter direction.-1 = prev grip in the first parameter direction.
            ds: 1 = next grip in the second parameter direction.-1 = prev grip in the second parameter direction.
            dt: 1 = next grip in the third parameter direction.-1 = prev grip in the third parameter direction.
            wrap: If true and object is "closed", the search will wrap.
            Returns: Pointer to the desired neighbor or NULL if there is no neighbor.
        """
        pass

    def NewGeometry(self, *args): #cannot find CLR method
        """
        NewGeometry(self: CustomObjectGrips) -> GeometryBase
        
            If the grips control just one object, then override NewGeometry(). When
                    
             NewGeometry() is called, return new geometry calculated from the current
                    grip 
             locations. This happens once at the end of a grip drag.
        
            Returns: The new geometry. The default implementation returns null.
        """
        pass

    def NurbsSurface(self, *args): #cannot find CLR method
        """
        NurbsSurface(self: CustomObjectGrips) -> NurbsSurface
        
            If the grips control a NURBS surface, this returns a pointer to that
                    surface.  You 
             can look at but you must NEVER change this surface.
        
            Returns: A pointer to a NURBS surface or null.
        """
        pass

    def NurbsSurfaceGrip(self, *args): #cannot find CLR method
        """
        NurbsSurfaceGrip(self: CustomObjectGrips, i: int, j: int) -> GripObject
        
            If the grips are control points of a NURBS surface, then this gets the
                    index of the 
             grip that controls the (i,j)-th cv.
        
        
            i: The index in the first dimension.
            j: The index in the second dimension.
            Returns: A grip controling a NURBS surface CV or null.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: CustomObjectGrips, args: GripsDrawEventArgs)
            Draws the grips. In your implementation, override this if you need to draw
                    dynamic 
             elements and then call this base implementation to draw the grips themselves.
        
        
            args: The grips draw event arguments.
        """
        pass

    def OnReset(self, *args): #cannot find CLR method
        """
        OnReset(self: CustomObjectGrips)
            Resets location of all grips to original spots and cleans up stuff that
                    was created 
             by dynamic dragging.  This is required when dragging is
                    canceled or in the Copy 
             command when grips are "copied". The override
                    should clean up dynamic workspace 
             stuff.
        """
        pass

    def OnResetMeshes(self, *args): #cannot find CLR method
        """
        OnResetMeshes(self: CustomObjectGrips)
            Just before Rhino turns off object grips, it calls this function.
                    If grips have 
             modified any display meshes, they must override
                    this function and restore the 
             meshes to their original states.
        """
        pass

    def OnUpdateMesh(self, *args): #cannot find CLR method
        """
        OnUpdateMesh(self: CustomObjectGrips, meshType: MeshType)
            Just before Rhino shades an object with grips on, it calls this method
                    to update 
             the display meshes.  Grips that modify surface or mesh objects
                    must override this 
             function and modify the display meshes here.
        
        
            meshType: The mesh type being updated.
        """
        pass

    @staticmethod
    def RegisterGripsEnabler(enabler, customGripsType):
        """ RegisterGripsEnabler(enabler: TurnOnGripsEventHandler, customGripsType: Type) """
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

    GripCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripCount(self: CustomObjectGrips) -> int

"""

    GripsMoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If GripsMoved is true if some of the grips have ever been moved
            GripObject.NewLocation() sets GripsMoved=true.

Get: GripsMoved(self: CustomObjectGrips) -> bool

"""

    NewLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if some of the grips have been moved. GripObject.NewLocation() sets
            NewLocation=true.  Derived classes can set NewLocation to false after 
            updating temporary display information.

Get: NewLocation(self: CustomObjectGrips) -> bool

Set: NewLocation(self: CustomObjectGrips) = value
"""

    OwnerObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Owner of the grips.

Get: OwnerObject(self: CustomObjectGrips) -> RhinoObject

"""



class CustomPointObject(PointObject, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: CustomPointObject) """
        pass

    def OnAddToDocument(self, *args): #cannot find CLR method
        """
        OnAddToDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be added to the list of
                    active objects 
             in the document.
        """
        pass

    def OnDeleteFromDocument(self, *args): #cannot find CLR method
        """
        OnDeleteFromDocument(self: RhinoObject, doc: RhinoDoc)
            This call informs an object it is about to be deleted.
                    Some objects, like clipping 
             planes, need to do a little extra cleanup
                    before they are deleted.
        """
        pass

    def OnDraw(self, *args): #cannot find CLR method
        """
        OnDraw(self: RhinoObject, e: DrawEventArgs)
            Called when Rhino wants to draw this object
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: RhinoObject, source: RhinoObject)
            Called when this a new instance of this object is created and copied from
                    an 
             existing object
        """
        pass

    def OnPick(self, *args): #cannot find CLR method
        """
        OnPick(self: RhinoObject, context: PickContext) -> IEnumerable[ObjRef]
        
            Called to determine if this object or some sub-portion of this object should be
                    
             picked given a pick context.
        """
        pass

    def OnPicked(self, *args): #cannot find CLR method
        """ OnPicked(self: RhinoObject, context: PickContext, pickedItems: IEnumerable[ObjRef]) """
        pass

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """
        OnSelectionChanged(self: RhinoObject)
            Called when the selection state of this object has changed
        """
        pass

    def OnSpaceMorph(self, *args): #cannot find CLR method
        """
        OnSpaceMorph(self: RhinoObject, morph: SpaceMorph)
            Called when a space morph has been applied to the geometry.
                    Currently this only 
             works for CustomMeshObject instances
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: RhinoObject, transform: Transform)
            Called when a transformation has been applied to the geometry
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, point: Point)
        """
        pass


class GripsDrawEventArgs(DrawEventArgs):
    # no doc
    def DrawControlPolygonLine(self, *__args):
        """
        DrawControlPolygonLine(self: GripsDrawEventArgs, start: Point3d, end: Point3d, startStatus: int, endStatus: int)
            Draws the lines in a control polygons.
                    This is an helper function.
        
            start: The point start.
            end: The point end.
            startStatus: Index of Grip status at start of line defined by start and end.
            endStatus: Index if Grip status at end of line defined by start and end.
        DrawControlPolygonLine(self: GripsDrawEventArgs, line: Line, startStatus: int, endStatus: int)
            Draws the lines in a control polygons.
                    This is an helper function.
        
            line: Line between two grips.
            startStatus: Index of Grip status at start of line.
            endStatus: Index if Grip status at end of line.
        DrawControlPolygonLine(self: GripsDrawEventArgs, line: Line, startStatus: GripStatus, endStatus: GripStatus)
            Draws the lines in a control polygons.
                    This is an helper function.
        
            line: Line between two grips.
            startStatus: Grip status at start of line.
            endStatus: Grip status at end of line.
        """
        pass

    def GripStatus(self, index):
        """ GripStatus(self: GripsDrawEventArgs, index: int) -> GripStatus """
        pass

    def RestoreViewportSettings(self):
        """ RestoreViewportSettings(self: GripsDrawEventArgs) """
        pass

    ControlPolygonStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """What kind of line is used to display things like control polygons.
            0 = no control polygon,  1 = solid control polygon,  2 = dotted control polygon.

Get: ControlPolygonStyle(self: GripsDrawEventArgs) -> int

Set: ControlPolygonStyle(self: GripsDrawEventArgs) = value
"""

    DrawDynamicStuff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, then draw stuff that does not move when grips are
            dragged, like the control polygon of the "original" curve.

Get: DrawDynamicStuff(self: GripsDrawEventArgs) -> bool

"""

    DrawStaticStuff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, then draw stuff that moves when grips are dragged,
            like the curve being bent by a dragged control point.

Get: DrawStaticStuff(self: GripsDrawEventArgs) -> bool

"""

    GripColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripColor(self: GripsDrawEventArgs) -> Color

Set: GripColor(self: GripsDrawEventArgs) = value
"""

    GripStatusCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripStatusCount(self: GripsDrawEventArgs) -> int

"""

    LockedGripColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockedGripColor(self: GripsDrawEventArgs) -> Color

Set: LockedGripColor(self: GripsDrawEventArgs) = value
"""

    SelectedGripColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedGripColor(self: GripsDrawEventArgs) -> Color

Set: SelectedGripColor(self: GripsDrawEventArgs) = value
"""



class GripStatus(object):
    # no doc
    Culled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Culled(self: GripStatus) -> bool

Set: Culled(self: GripStatus) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GripStatus) -> bool

"""



class TurnOnGripsEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ TurnOnGripsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, rhObj, callback, object):
        """ BeginInvoke(self: TurnOnGripsEventHandler, rhObj: RhinoObject, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: TurnOnGripsEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, rhObj):
        """ Invoke(self: TurnOnGripsEventHandler, rhObj: RhinoObject) """
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


class UserData(object, IDisposable):
    """
    Provides a base class for custom classes of information which may be attached to
                geometry or attribute classes.
    """
    @staticmethod
    def Copy(source, destination):
        """
        Copy(source: CommonObject, destination: CommonObject)
            Expert user tool that copies user data that has a positive 
                    CopyCount from the 
             source object to a destination object.
                    Generally speaking you don't need to use 
             Copy().
                    Simply rely on things like the copy constructors to do the right thing.
        
        
            source: A source object for the data.
            destination: A destination object for the data.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: UserData)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    @staticmethod
    def MoveUserDataFrom(objectWithUserData):
        """
        MoveUserDataFrom(objectWithUserData: CommonObject) -> Guid
        
            Moves the user data from objectWithUserData to a temporary data storage
                    identifierd 
             by the return Guid.  When MoveUserDataFrom returns, the
                    objectWithUserData will not 
             have any user data.
        
        
            objectWithUserData: Object with user data attached.
            Returns: Guid identifier for storage of UserData that is held in a temporary list
                    by this 
             class. This function should be used in conjunction with MoveUserDataTo
                    to transfer 
             the user data to a different object.
                    Returns Guid.Empty if there was no user data 
             to transfer.
        """
        pass

    @staticmethod
    def MoveUserDataTo(objectToGetUserData, id, append):
        """
        MoveUserDataTo(objectToGetUserData: CommonObject, id: Guid, append: bool)
            Moves the user data.
                    See 
             Rhino.DocObjects.Custom.UserData.MoveUserDataFrom(Rhino.Runtime.CommonObject) for more 
             information.
        
        
            objectToGetUserData: Object data source.
            id: Target.
            append: If the data should be appended or replaced.
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: UserData, source: UserData)
            Is called when the object is being duplicated.
        
            source: The source data.
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: UserData, transform: Transform)
            Is called when the object associated with this data is transformed. If you override this
               
                  function, make sure to call the base class if you want the stored Transform to be updated.
        
        
            transform: The transform being applied.
        """
        pass

    def Read(self, *args): #cannot find CLR method
        """
        Read(self: UserData, archive: BinaryArchiveReader) -> bool
        
            Reads the content of this data from a stream archive.
        
            archive: An archive.
            Returns: true if the data was successfully written. The default implementation always returns false.
        """
        pass

    def Write(self, *args): #cannot find CLR method
        """
        Write(self: UserData, archive: BinaryArchiveWriter) -> bool
        
            Writes the content of this data to a stream archive.
        
            archive: An archive.
            Returns: true if the data was successfully written. The default implementation always returns false.
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

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Descriptive name of the user data.

Get: Description(self: UserData) -> str

"""

    ShouldWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If you want to save this user data in a 3dm file, override
            ShouldWrite and return true.  If you do support serialization,
            you must also override the Read and Write functions.

Get: ShouldWrite(self: UserData) -> bool

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Updated if user data is attached to a piece of geometry that is
            transformed and the virtual OnTransform() is not overridden.  If you
            override OnTransform() and want Transform to be updated, then call the 
            base class OnTransform() in your override.
            The default constructor sets Transform to the identity.

Get: Transform(self: UserData) -> Transform

"""



class UnknownUserData(UserData, IDisposable):
    """
    Represents user data with unknown origin.
    
    UnknownUserData(pointerNativeUserData: IntPtr)
    """
    def Dispose(self):
        """
        Dispose(self: UserData, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: UserData, source: UserData)
            Is called when the object is being duplicated.
        
            source: The source data.
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: UserData, transform: Transform)
            Is called when the object associated with this data is transformed. If you override this
               
                  function, make sure to call the base class if you want the stored Transform to be updated.
        
        
            transform: The transform being applied.
        """
        pass

    def Read(self, *args): #cannot find CLR method
        """
        Read(self: UserData, archive: BinaryArchiveReader) -> bool
        
            Reads the content of this data from a stream archive.
        
            archive: An archive.
            Returns: true if the data was successfully written. The default implementation always returns false.
        """
        pass

    def Write(self, *args): #cannot find CLR method
        """
        Write(self: UserData, archive: BinaryArchiveWriter) -> bool
        
            Writes the content of this data to a stream archive.
        
            archive: An archive.
            Returns: true if the data was successfully written. The default implementation always returns false.
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
    def __new__(self, pointerNativeUserData):
        """ __new__(cls: type, pointerNativeUserData: IntPtr) """
        pass


class UserDataList(object):
    """ Represents a collection of user data. """
    def Add(self, userdata):
        """
        Add(self: UserDataList, userdata: UserData) -> bool
        
            If the userdata is already in a different UserDataList, it
                    will be removed from 
             that list and added to this list.
        
        
            userdata: Data element.
            Returns: Whether this operation succeeded.
        """
        pass

    def Find(self, userdataType):
        """
        Find(self: UserDataList, userdataType: Type) -> UserData
        
            Finds a specific data type in this regulated collection.
        
            userdataType: A data type.
            Returns: The found data, or null of nothing was found.
        """
        pass

    def Remove(self, userdata):
        """
        Remove(self: UserDataList, userdata: UserData) -> bool
        
            Remove the userdata from this list
            Returns: true if the user data was successfully removed
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of UserData objects in this list.

Get: Count(self: UserDataList) -> int

"""



class UserDictionary(UserData, IDisposable):
    """
    Defines the storage data class for a Rhino.Collections.ArchivableDictionaryuser dictionary.
    
    UserDictionary()
    """
    def Dispose(self):
        """
        Dispose(self: UserData, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def OnDuplicate(self, *args): #cannot find CLR method
        """
        OnDuplicate(self: UserDictionary, source: UserData)
            Clones the user data.
        
            source: The source data.
        """
        pass

    def OnTransform(self, *args): #cannot find CLR method
        """
        OnTransform(self: UserData, transform: Transform)
            Is called when the object associated with this data is transformed. If you override this
               
                  function, make sure to call the base class if you want the stored Transform to be updated.
        
        
            transform: The transform being applied.
        """
        pass

    def Read(self, *args): #cannot find CLR method
        """
        Read(self: UserDictionary, archive: BinaryArchiveReader) -> bool
        
            Is called to read this entity.
        
            archive: An archive.
            Returns: Always returns true.
        """
        pass

    def Write(self, *args): #cannot find CLR method
        """
        Write(self: UserDictionary, archive: BinaryArchiveWriter) -> bool
        
            Is called to write this entity.
        
            archive: An archive.
            Returns: Always returns true.
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

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text "RhinoCommon UserDictionary".

Get: Description(self: UserDictionary) -> str

"""

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the dictionary that is associated with this class.
            This dictionary is unique.

Get: Dictionary(self: UserDictionary) -> ArchivableDictionary

"""

    ShouldWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Writes this entity if the count is larger than 0.

Get: ShouldWrite(self: UserDictionary) -> bool

"""



