# encoding: utf-8
# module Rhino.Geometry calls itself Geometry
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GeometryBase(CommonObject, IDisposable, ISerializable):
    """ Provides a common base for most geometric classes. This class is abstract. """
    def ComponentIndex(self):
        """
        ComponentIndex(self: GeometryBase) -> ComponentIndex
        
            If this piece of geometry is a component in something larger, like a BrepEdge
                    in a 
             Brep, then this function returns the component index.
        
            Returns: This object's component index.  If this object is not a sub-piece of a larger
                    
             geometric entity, then the returned index has 
                    m_type = ComponentIndex.InvalidType
        
                         and m_index = -1.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Duplicate(self):
        """
        Duplicate(self: GeometryBase) -> GeometryBase
        
            Constructs a deep (full) copy of this object.
            Returns: An object of the same type as this, with the same properties and behavior.
        """
        pass

    def DuplicateShallow(self):
        """
        DuplicateShallow(self: GeometryBase) -> GeometryBase
        
            Constructs a light copy of this object. By "light", it is meant that the same
                    
             underlying data is used until something is done to attempt to change it. For example,
                  
               you could have a shallow copy of a very heavy mesh object and the same underlying
                    
             data will be used when doing things like inspecting the number of faces on the mesh.
                   
              If you modify the location of one of the mesh vertices, the shallow copy will create
                  
               a full duplicate of the underlying mesh data and the shallow copy will become a
                    
             deep copy.
        
            Returns: An object of the same type as this object.
                    This behavior is overridden by 
             implementing classes.
        """
        pass

    def GetBoundingBox(self, *__args):
        """
        GetBoundingBox(self: GeometryBase, plane: Plane) -> BoundingBox
        
            Aligned Boundingbox solver. Gets the plane aligned boundingbox.
        
            plane: Orientation plane for BoundingBox.
            Returns: A BoundingBox in plane coordinates.
        GetBoundingBox(self: GeometryBase, plane: Plane) -> (BoundingBox, Box)
        
            Aligned Boundingbox solver. Gets the plane aligned boundingbox.
        
            plane: Orientation plane for BoundingBox.
            Returns: A BoundingBox in plane coordinates.
        GetBoundingBox(self: GeometryBase, accurate: bool) -> BoundingBox
        
            Boundingbox solver. Gets the world axis aligned boundingbox for the geometry.
        
            accurate: If true, a physically accurate boundingbox will be computed. 
                    If not, a boundingbox 
             estimate will be computed. For some geometry types there is no 
                    difference between 
             the estimate and the accurate boundingbox. Estimated boundingboxes 
                    can be computed 
             much (much) faster than accurate (or "tight") bounding boxes. 
                    Estimated bounding 
             boxes are always similar to or larger than accurate bounding boxes.
        
            Returns: The boundingbox of the geometry in world coordinates or BoundingBox.Empty 
                    if not 
             bounding box could be found.
        
        GetBoundingBox(self: GeometryBase, xform: Transform) -> BoundingBox
        
            Aligned Boundingbox solver. Gets the world axis aligned boundingbox for the transformed geometry.
        
            xform: Transformation to apply to object prior to the BoundingBox computation. 
                    The 
             geometry itself is not modified.
        
            Returns: The accurate boundingbox of the transformed geometry in world coordinates 
                    or 
             BoundingBox.Empty if not bounding box could be found.
        """
        pass

    def GetUserString(self, key):
        """
        GetUserString(self: GeometryBase, key: str) -> str
        
            Gets user string from this geometry.
        
            key: id used to retrieve the string.
            Returns: string associated with the key if successful. null if no key was found.
        """
        pass

    def GetUserStrings(self):
        """
        GetUserStrings(self: GeometryBase) -> NameValueCollection
        
            Gets a copy of all (user key string, user value string) pairs attached to this geometry.
            Returns: A new collection.
        """
        pass

    def MakeDeformable(self):
        """
        MakeDeformable(self: GeometryBase) -> bool
        
            If possible, converts the object into a form that can be accurately modified
                    with 
             "squishy" transformations like projections, shears, an non-uniform scaling.
        
            Returns: false if object cannot be converted to a deformable object. true if object was
                    
             already deformable or was converted into a deformable object.
        """
        pass

    def MemoryEstimate(self):
        """
        MemoryEstimate(self: GeometryBase) -> UInt32
        
            Computes an estimate of the number of bytes that this object is using in memory.
            Returns: An estimated memory footprint.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def Rotate(self, angleRadians, rotationAxis, rotationCenter):
        """
        Rotate(self: GeometryBase, angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> bool
        
            Rotates the object about the specified axis. A positive rotation 
                    angle results in 
             a counter-clockwise rotation about the axis (right hand rule).
        
        
            angleRadians: Angle of rotation in radians.
            rotationAxis: Direction of the axis of rotation.
            rotationCenter: Point on the axis of rotation.
            Returns: true if geometry successfully rotated.
        """
        pass

    def Scale(self, scaleFactor):
        """
        Scale(self: GeometryBase, scaleFactor: float) -> bool
        
            Scales the object by the specified factor. The scale is centered at the origin.
        
            scaleFactor: The uniform scaling factor.
            Returns: true if geometry successfully scaled.
        """
        pass

    def SetUserString(self, key, value):
        """
        SetUserString(self: GeometryBase, key: str, value: str) -> bool
        
            Attach a user string (key,value combination) to this geometry.
        
            key: id used to retrieve this string.
            value: string associated with key.
            Returns: true on success.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: GeometryBase, xform: Transform) -> bool
        
            Transforms the geometry. If the input Transform has a SimilarityType of
                    
             OrientationReversing, you may want to consider flipping the transformed
                    geometry 
             after calling this function when it makes sense. For example,
                    you may want to call 
             Flip() on a Brep after transforming it.
        
        
            xform: Transformation to apply to geometry.
            Returns: true if geometry successfully transformed.
        """
        pass

    def Translate(self, *__args):
        """
        Translate(self: GeometryBase, x: float, y: float, z: float) -> bool
        
            Translates the object along the specified vector.
        
            x: The X component.
            y: The Y component.
            z: The Z component.
            Returns: true if geometry successfully translated.
        Translate(self: GeometryBase, translationVector: Vector3d) -> bool
        
            Translates the object along the specified vector.
        
            translationVector: A moving vector.
            Returns: true if geometry successfully translated.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasBrepForm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Brep.TryConvertBrep function will be successful for this object

Get: HasBrepForm(self: GeometryBase) -> bool

"""

    IsDeformable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if object can be accurately modified with "squishy" transformations like
            projections, shears, and non-uniform scaling.

Get: IsDeformable(self: GeometryBase) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true this object may not be modified. Any properties or functions that attempt
            to modify this object when it is set to "IsReadOnly" will throw a NotSupportedException.

Get: IsDocumentControlled(self: GeometryBase) -> bool

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Useful for switch statements that need to differentiate between
            basic object types like points, curves, surfaces, and so on.

Get: ObjectType(self: GeometryBase) -> ObjectType

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of user strings.

Get: UserStringCount(self: GeometryBase) -> int

"""



class AnnotationBase(GeometryBase, IDisposable, ISerializable):
    """
    Provides a common base class to all annotation geometry.
                This class refers to the geometric element that is independent from the document.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of DimensionStyle in document DimStyle table used by the dimension.

Get: Index(self: AnnotationBase) -> int

Set: Index(self: AnnotationBase) = value
"""

    NumericValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the numeric value, depending on geometry type.
            LinearDimension: distance between arrow tipsRadialDimension: radius or diamater depending on typeAngularDimension: angle in degreesLeader or Text: UnsetValue

Get: NumericValue(self: AnnotationBase) -> float

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the plane containing the annotation.

Get: Plane(self: AnnotationBase) -> Plane

Set: Plane(self: AnnotationBase) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text for this annotation.

Get: Text(self: AnnotationBase) -> str

Set: Text(self: AnnotationBase) = value
"""

    TextFormula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a formula for this annotation.

Get: TextFormula(self: AnnotationBase) -> str

Set: TextFormula(self: AnnotationBase) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text height in model units.

Get: TextHeight(self: AnnotationBase) -> float

Set: TextHeight(self: AnnotationBase) = value
"""



class AngularDimension(AnnotationBase, IDisposable, ISerializable):
    """
    Represents a dimension of an entity that can be measured with an angle.
                This entity refers to the geometric element that is independent from the document.
    
    AngularDimension(arc: Arc, offset: float)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, arc, offset):
        """
        __new__(cls: type, arc: Arc, offset: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Arc(object, IEquatable[Arc], IEpsilonComparable[Arc]):
    """
    Represents the value of a plane, two angles and a radius in
                a subcurve of a three-dimensional circle.
                
                The curve is parameterized by an angle expressed in radians. For an IsValid arc
                the total subtended angle AngleRadians() = Domain()(1) - Domain()(0) must satisfy
                0 < AngleRadians() < 2*PiThe parameterization of the Arc is inherited from the Circle it is derived from.
                In particulart -> center + cos(t)*radius*xaxis + sin(t)*radius*yaxiswhere xaxis and yaxis, (part of Circle.Plane) form an othonormal frame of the plane
                containing the circle.
    
    Arc(circle: Circle, angleRadians: float)
    Arc(circle: Circle, angleIntervalRadians: Interval)
    Arc(plane: Plane, radius: float, angleRadians: float)
    Arc(center: Point3d, radius: float, angleRadians: float)
    Arc(plane: Plane, center: Point3d, radius: float, angleRadians: float)
    Arc(startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
    Arc(pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
    """
    def BoundingBox(self):
        """
        BoundingBox(self: Arc) -> BoundingBox
        
            Computes the 3D axis aligned bounding box for this arc.
            Returns: Bounding box of arc.
        """
        pass

    def ClosestParameter(self, testPoint):
        """
        ClosestParameter(self: Arc, testPoint: Point3d) -> float
        
            Gets parameter on the arc closest to a test point.
        
            testPoint: Point to get close to.
            Returns: Parameter (in radians) of the point on the arc that
                    is closest to the test point. 
             If testPoint is the center
                    of the arc, then the starting point of the arc is
              
                   (arc.Domain()[0]) returned. If no parameter could be found, 
                    
             RhinoMath.UnsetValue is returned.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: Arc, testPoint: Point3d) -> Point3d
        
            Computes the point on an arc that is closest to a test point.
        
            testPoint: Point to get close to.
            Returns: The point on the arc that is closest to testPoint. If testPoint is
                    the center of 
             the arc, then the starting point of the arc is returned.
                    UnsetPoint on failure.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Arc, other: Arc, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Arc, other: Arc) -> bool
        
            Determines whether another arc has the same value as this arc.
        
            other: An arc.
            Returns: true if obj is equal to this arc; otherwise false.
        Equals(self: Arc, obj: object) -> bool
        
            Determines whether another object is an arc and has the same value as this arc.
        
            obj: An object.
            Returns: true if obj is an arc and is exactly equal to this arc; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Arc) -> int
        
            Computes a hash code for the present arc.
            Returns: A non-unique integer that represents this arc.
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Arc, t: float) -> Point3d
        
            Gets the point at the given arc parameter.
        
            t: Arc parameter to evaluate.
            Returns: The point at the given parameter.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Arc)
            Reverses the orientation of the arc. Changes the domain from [a,b]
                    to [-b,-a].
        """
        pass

    def TangentAt(self, t):
        """
        TangentAt(self: Arc, t: float) -> Vector3d
        
            Gets the tangent at the given parameter.
        
            t: Parameter of tangent to evaluate.
            Returns: The tangent at the arc at the given parameter.
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Arc) -> NurbsCurve
        
            Initializes a nurbs curve representation of this arc. 
                    This amounts to the same as 
             calling NurbsCurve.CreateFromArc().
        
            Returns: A nurbs curve representation of this arc or null if no such representation could be made.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Arc, xform: Transform) -> bool
        
            Transforms the arc using a Transformation matrix.
        
            xform: Transformations to apply. 
                    Note that arcs cannot handle non-euclidian 
             transformations.
        
            Returns: true on success, false on failure.
        """
        pass

    def Trim(self, domain):
        """
        Trim(self: Arc, domain: Interval) -> bool
        
            Sets arc's angle domain (in radians) as a subdomain of the circle.
        
            domain: 0 < domain[1] - domain[0] <= 2.0 * RhinoMath.Pi.
            Returns: true on success, false on failure.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Arc]() -> Arc
        
        __new__(cls: type, circle: Circle, angleRadians: float)
        __new__(cls: type, circle: Circle, angleIntervalRadians: Interval)
        __new__(cls: type, plane: Plane, radius: float, angleRadians: float)
        __new__(cls: type, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, plane: Plane, center: Point3d, radius: float, angleRadians: float)
        __new__(cls: type, startPoint: Point3d, pointOnInterior: Point3d, endPoint: Point3d)
        __new__(cls: type, pointA: Point3d, tangentA: Vector3d, pointB: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sweep -or subtended- angle (in Radians) for this arc segment.

Get: Angle(self: Arc) -> float

Set: Angle(self: Arc) = value
"""

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sweep -or subtended- angle (in Radians) for this arc segment.

Get: AngleDegrees(self: Arc) -> float

Set: AngleDegrees(self: Arc) = value
"""

    AngleDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the angle domain (in Radians) of this arc.

Get: AngleDomain(self: Arc) -> Interval

Set: AngleDomain(self: Arc) = value
"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center point for this arc.

Get: Center(self: Arc) -> Point3d

Set: Center(self: Arc) = value
"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the circumference of the circle that is coincident with this arc.

Get: Circumference(self: Arc) -> float

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Diameter of this arc.

Get: Diameter(self: Arc) -> float

Set: Diameter(self: Arc) = value
"""

    EndAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the end angle (in Radians) for this arc segment.

Get: EndAngle(self: Arc) -> float

Set: EndAngle(self: Arc) = value
"""

    EndAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the end angle (in Radians) for this arc segment.

Get: EndAngleDegrees(self: Arc) -> float

Set: EndAngleDegrees(self: Arc) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end point of the arc.

Get: EndPoint(self: Arc) -> Point3d

"""

    IsCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this arc is a complete circle.

Get: IsCircle(self: Arc) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this arc is valid.
            Detail:
             Radius>0 and 0<AngleRadians()<=2*Math.Pi.

Get: IsValid(self: Arc) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the arc. (Length = Radius * (subtended angle in radians)).

Get: Length(self: Arc) -> float

"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mid-point of the arc.

Get: MidPoint(self: Arc) -> Point3d

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the plane in which this arc lies.

Get: Plane(self: Arc) -> Plane

Set: Plane(self: Arc) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of this arc.

Get: Radius(self: Arc) -> float

Set: Radius(self: Arc) = value
"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the start angle (in Radians) for this arc segment.

Get: StartAngle(self: Arc) -> float

Set: StartAngle(self: Arc) = value
"""

    StartAngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the start angle (in Radians) for this arc segment.

Get: StartAngleDegrees(self: Arc) -> float

Set: StartAngleDegrees(self: Arc) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start point of the arc.

Get: StartPoint(self: Arc) -> Point3d

"""



class Curve(GeometryBase, IDisposable, ISerializable):
    """
    Represents a base class that is common to most RhinoCommon curve types.
                A curve represents an entity that can be all visited by providing
                a single parameter, usually called t.
    """
    def ChangeClosedCurveSeam(self, t):
        """
        ChangeClosedCurveSeam(self: Curve, t: float) -> bool
        
            If this curve is closed, then modify it so that the start/end point is at curve parameter t.
        
            t: Curve parameter of new start/end point. The returned curves domain will start at t.
            Returns: true on success, false on failure.
        """
        pass

    def ChangeDimension(self, desiredDimension):
        """
        ChangeDimension(self: Curve, desiredDimension: int) -> bool
        
            Changes the dimension of a curve.
        
            desiredDimension: The desired dimension.
            Returns: true if the curve's dimension was already desiredDimension
                    or if the curve's 
             dimension was successfully changed to desiredDimension;
                    otherwise false.
        """
        pass

    def ClosedCurveOrientation(self, *__args):
        """
        ClosedCurveOrientation(self: Curve, xform: Transform) -> CurveOrientation
        
            Determines the orientation (counterclockwise or clockwise) of a closed planar curve.
                   
              Only works with simple (no self intersections) closed planar curves.
        
        
            xform: Transformation to map the curve to the xy plane. If the curve is parallel
                    to the xy 
             plane, you may pass Identity matrix.
        
            Returns: The orientation of this curve in the world xy-plane.
        ClosedCurveOrientation(self: Curve, plane: Plane) -> CurveOrientation
        
            Determines the orientation (counterclockwise or clockwise) of a closed planar curve in a given 
             plane.
                    Only works with simple (no self intersections) closed planar curves.
        
        
            plane: The plane in which to solve the orientation.
            Returns: The orientation of this curve in the given plane.
        ClosedCurveOrientation(self: Curve, upDirection: Vector3d) -> CurveOrientation
        
            Determines the orientation (counterclockwise or clockwise) of a closed planar curve in a given 
             plane.
                    Only works with simple (no self intersections) closed planar curves.
        
        
            upDirection: A vector that is considered "up".
            Returns: The orientation of this curve with respect to a defined up direction.
        """
        pass

    def ClosestPoint(self, testPoint, t, maximumDistance=None):
        """
        ClosestPoint(self: Curve, testPoint: Point3d, maximumDistance: float) -> (bool, float)
        
            Finds the parameter of the point on a curve that is closest to testPoint.
                    If the 
             maximumDistance parameter is > 0, then only points whose distance
                    to the given 
             point is <= maximumDistance will be returned.  Using a 
                    positive value of 
             maximumDistance can substantially speed up the search.
        
        
            testPoint: Point to project.
            maximumDistance: The maximum allowed distance.
                    Past this distance, the search is given up and false 
             is returned.Use 0 to turn off this parameter.
        
            Returns: true on success, false on failure.
        ClosestPoint(self: Curve, testPoint: Point3d) -> (bool, float)
        
            Finds parameter of the point on a curve that is closest to testPoint.
                    If the 
             maximumDistance parameter is > 0, then only points whose distance
                    to the given 
             point is <= maximumDistance will be returned.  Using a 
                    positive value of 
             maximumDistance can substantially speed up the search.
        
        
            testPoint: Point to search from.
            Returns: true on success, false on failure.
        """
        pass

    def ClosestPoints(self, *__args):
        """
        ClosestPoints(self: Curve, otherCurve: Curve) -> (bool, Point3d, Point3d)
        
            Gets closest points between this and another curves.
        
            otherCurve: The other curve.
            Returns: true on success; false on error.
        ClosestPoints(self: Curve, geometry: IEnumerable[GeometryBase]) -> (bool, Point3d, Point3d, int)
        ClosestPoints(self: Curve, geometry: IEnumerable[GeometryBase], maximumDistance: float) -> (bool, Point3d, Point3d, int)
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Contains(self, testPoint, plane=None, tolerance=None):
        """
        Contains(self: Curve, testPoint: Point3d, plane: Plane, tolerance: float) -> PointContainment
        
            Computes the relationship between a point and a closed curve region. 
                    This curve 
             must be closed or the return value will be Unset.
        
        
            testPoint: Point to test.
            plane: Plane in in which to compare point and region.
            tolerance: Tolerance to use during comparison.
            Returns: Relationship between point and curve region.
        Contains(self: Curve, testPoint: Point3d, plane: Plane) -> PointContainment
        
            Computes the relationship between a point and a closed curve region. 
                    This curve 
             must be closed or the return value will be Unset.
        
        
            testPoint: Point to test.
            plane: Plane in in which to compare point and region.
            Returns: Relationship between point and curve region.
        Contains(self: Curve, testPoint: Point3d) -> PointContainment
        
            Computes the relationship between a point and a closed curve region. 
                    This curve 
             must be closed or the return value will be Unset.
                    Both curve and point are 
             projected to the World XY plane.
        
        
            testPoint: Point to test.
            Returns: Relationship between point and curve region.
        """
        pass

    @staticmethod
    def CreateBlendCurve(*__args):
        """
        CreateBlendCurve(curve0: Curve, t0: float, reverse0: bool, continuity0: BlendContinuity, curve1: Curve, t1: float, reverse1: bool, continuity1: BlendContinuity) -> Curve
        
            Makes a curve blend between 2 curves at the parameters specified
                    with the 
             directions and continuities specified
        
        
            curve0: First curve to blend from
            t0: Parameter on first curve for blend endpoint
            reverse0: If false, the blend will go in the natural direction of the curve.
                    If true, the 
             blend will go in the opposite direction to the curve
        
            continuity0: continuity for the blend at the start
            curve1: Second curve to blend from
            t1: Parameter on second curve for blend endpoint
            reverse1: If false, the blend will go in the natural direction of the curve.
                    If true, the 
             blend will go in the opposite direction to the curve
        
            continuity1: continuity for the blend at the end
            Returns: the blend curve on success. null on failure
        CreateBlendCurve(curveA: Curve, curveB: Curve, continuity: BlendContinuity, bulgeA: float, bulgeB: float) -> Curve
        
            Create a Blend curve between two existing curves.
        
            curveA: Curve to blend from (blending will occur at curve end point).
            curveB: Curve to blend to (blending will occur at curve start point).
            continuity: Continuity of blend.
            bulgeA: Bulge factor at curveA end of blend. Values near 1.0 work best.
            bulgeB: Bulge factor at curveB end of blend. Values near 1.0 work best.
            Returns: A curve representing the blend between A and B or null on failure.
        CreateBlendCurve(curveA: Curve, curveB: Curve, continuity: BlendContinuity) -> Curve
        
            Create a Blend curve between two existing curves.
        
            curveA: Curve to blend from (blending will occur at curve end point).
            curveB: Curve to blend to (blending will occur at curve start point).
            continuity: Continuity of blend.
            Returns: A curve representing the blend between A and B or null on failure.
        """
        pass

    @staticmethod
    def CreateBooleanDifference(curveA, *__args):
        """
        CreateBooleanDifference(curveA: Curve, subtractors: IEnumerable[Curve]) -> Array[Curve]
        CreateBooleanDifference(curveA: Curve, curveB: Curve) -> Array[Curve]
        
            Calculates the boolean difference between two closed, planar curves. 
                    Note, curves 
             must be co-planar.
        
        
            curveA: The first closed, planar curve.
            curveB: The second closed, planar curve.
            Returns: Result curves on success, empty array if no difference could be calculated.
        """
        pass

    @staticmethod
    def CreateBooleanIntersection(curveA, curveB):
        """
        CreateBooleanIntersection(curveA: Curve, curveB: Curve) -> Array[Curve]
        
            Calculates the boolean intersection of two closed, planar curves. 
                    Note, curves 
             must be co-planar.
        
        
            curveA: The first closed, planar curve.
            curveB: The second closed, planar curve.
            Returns: Result curves on success, empty array if no intersection could be calculated.
        """
        pass

    @staticmethod
    def CreateBooleanUnion(curves):
        """ CreateBooleanUnion(curves: IEnumerable[Curve]) -> Array[Curve] """
        pass

    @staticmethod
    def CreateControlPointCurve(points, degree=None):
        """
        CreateControlPointCurve(points: IEnumerable[Point3d]) -> Curve
        CreateControlPointCurve(points: IEnumerable[Point3d], degree: int) -> Curve
        """
        pass

    @staticmethod
    def CreateFillet(curve0, curve1, radius, t0Base, t1Base):
        """
        CreateFillet(curve0: Curve, curve1: Curve, radius: float, t0Base: float, t1Base: float) -> Arc
        
            Computes the fillet arc for a curve filleting operation.
        
            curve0: First curve to fillet.
            curve1: Second curve to fillet.
            radius: Fillet radius.
            t0Base: Parameter on curve0 where the fillet ought to start (approximately).
            t1Base: Parameter on curve1 where the fillet ought to end (approximately).
            Returns: The fillet arc on success, or Arc.Unset on failure.
        """
        pass

    @staticmethod
    def CreateFilletCurves(curve0, point0, curve1, point1, radius, join, trim, arcExtension, tolerance, angleTolerance):
        """
        CreateFilletCurves(curve0: Curve, point0: Point3d, curve1: Curve, point1: Point3d, radius: float, join: bool, trim: bool, arcExtension: bool, tolerance: float, angleTolerance: float) -> Array[Curve]
        
            Creates a tangent arc between two curves and trims or extends the curves to the arc.
        
            curve0: The first curve to fillet.
            point0: A point on the first curve that is near the end where the fillet will
                    be created.
            curve1: The second curve to fillet.
            point1: A point on the second curve that is near the end where the fillet will
                    be created.
            radius: The radius of the fillet.
            join: Join the output curves.
            trim: Trim copies of the input curves to the output fillet curve.
            arcExtension: Applies when arcs are filleted but need to be extended to meet the
                    fillet curve or 
             chamfer line. If true, then the arc is extended
                    maintaining its validity. If false, 
             then the arc is extended with a
                    line segment, which is joined to the arc converting 
             it to a polycurve.
        
            tolerance: The tolerance, generally the document's absolute tolerance.
            Returns: The results of the fillet operation. The number of output curves depends
                    on the 
             input curves and the values of the parameters that were used
                    during the fillet 
             operation. In most cases, the output array will contain
                    either one or three curves, 
             although two curves can be returned if the
                    radius is zero and join = false.
               
                  For example, if both join and trim = true, then the output curve
                    will be a 
             polycurve containing the fillet curve joined with trimmed copies
                    of the input 
             curves. If join = false and trim = true, then three curves,
                    the fillet curve and 
             trimmed copies of the input curves, will be returned.
                    If both join and trim = 
             false, then just the fillet curve is returned.
        """
        pass

    @staticmethod
    def CreateInterpolatedCurve(points, degree, knots=None, startTangent=None, endTangent=None):
        """
        CreateInterpolatedCurve(points: IEnumerable[Point3d], degree: int, knots: CurveKnotStyle, startTangent: Vector3d, endTangent: Vector3d) -> Curve
        CreateInterpolatedCurve(points: IEnumerable[Point3d], degree: int, knots: CurveKnotStyle) -> Curve
        CreateInterpolatedCurve(points: IEnumerable[Point3d], degree: int) -> Curve
        """
        pass

    @staticmethod
    def CreateMeanCurve(curveA, curveB, angleToleranceRadians=None):
        """
        CreateMeanCurve(curveA: Curve, curveB: Curve) -> Curve
        
            Constructs a mean, or average, curve from two curves.
        
            curveA: A first curve.
            curveB: A second curve.
            Returns: The average curve, or null on error.
        CreateMeanCurve(curveA: Curve, curveB: Curve, angleToleranceRadians: float) -> Curve
        
            Constructs a mean, or average, curve from two curves.
        
            curveA: A first curve.
            curveB: A second curve.
            angleToleranceRadians: The angle tolerance, in radians, used to match kinks between curves.
                    If you are 
             unsure how to set this parameter, then either use the
                    document's angle tolerance 
             RhinoDoc.AngleToleranceRadians,
                    or the default value (RhinoMath.UnsetValue)
        
            Returns: The average curve, or null on error.
        """
        pass

    @staticmethod
    def CreateTweenCurves(curve0, curve1, numCurves):
        """
        CreateTweenCurves(curve0: Curve, curve1: Curve, numCurves: int) -> Array[Curve]
        
            Creates curves between two open or closed input curves. Uses the control points of the curves 
             for finding tween curves.
                    That means the first control point of first curve is 
             matched to first control point of the second curve and so on.
                    There is no matching 
             of curves direction. Caller must match input curves direction before calling the function.
        
        
            curve0: The first, or starting, curve.
            curve1: The second, or ending, curve.
            numCurves: Number of tween curves to create.
            Returns: An array of joint curves. This array can be empty.
        """
        pass

    @staticmethod
    def CreateTweenCurvesWithMatching(curve0, curve1, numCurves):
        """
        CreateTweenCurvesWithMatching(curve0: Curve, curve1: Curve, numCurves: int) -> Array[Curve]
        
            Creates curves between two open or closed input curves. Make the structure of input curves 
             compatible if needed.
                    Refits the input curves to have the same structure. The 
             resulting curves are usually more complex than input unless
                    input curves are 
             compatible and no refit is needed. There is no matching of curves direction.
                    Caller 
             must match input curves direction before calling the function.
        
        
            curve0: The first, or starting, curve.
            curve1: The second, or ending, curve.
            numCurves: Number of tween curves to create.
            Returns: An array of joint curves. This array can be empty.
        """
        pass

    @staticmethod
    def CreateTweenCurvesWithSampling(curve0, curve1, numCurves, numSamples):
        """
        CreateTweenCurvesWithSampling(curve0: Curve, curve1: Curve, numCurves: int, numSamples: int) -> Array[Curve]
        
            Creates curves between two open or closed input curves. Use sample points method to make curves 
             compatible.
                    This is how the algorithm workd: Divides the two curves into an equal 
             number of points, finds the midpoint between the 
                    corresponding points on the 
             curves and interpolates the tween curve through those points. There is no matching of curves
           
                      direction. Caller must match input curves direction before calling the function.
        
        
            curve0: The first, or starting, curve.
            curve1: The second, or ending, curve.
            numCurves: Number of tween curves to create.
            numSamples: Number of sample points along input curves.
            Returns: >An array of joint curves. This array can be empty.
        """
        pass

    def CurvatureAt(self, t):
        """
        CurvatureAt(self: Curve, t: float) -> Vector3d
        
            Evaluate the curvature vector at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Curvature vector of the curve at the parameter t.
        """
        pass

    def DerivativeAt(self, t, derivativeCount, side=None):
        """
        DerivativeAt(self: Curve, t: float, derivativeCount: int, side: CurveEvaluationSide) -> Array[Vector3d]
        
            Evaluate the derivatives at the specified curve parameter.
        
            t: Curve parameter to evaluate.
            derivativeCount: Number of derivatives to evaluate, must be at least 0.
            side: Side of parameter to evaluate. If the parameter is at a kink, 
                    it makes a big 
             difference whether the evaluation is from below or above.
        
            Returns: An array of vectors that represents all the derivatives starting at zero.
        DerivativeAt(self: Curve, t: float, derivativeCount: int) -> Array[Vector3d]
        
            Evaluate the derivatives at the specified curve parameter.
        
            t: Curve parameter to evaluate.
            derivativeCount: Number of derivatives to evaluate, must be at least 0.
            Returns: An array of vectors that represents all the derivatives starting at zero.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def DivideAsContour(self, contourStart, contourEnd, interval):
        """
        DivideAsContour(self: Curve, contourStart: Point3d, contourEnd: Point3d, interval: float) -> Array[Point3d]
        
            Divides this curve at fixed steps along a defined contour line.
        
            contourStart: The start of the contouring line.
            contourEnd: The end of the contouring line.
            interval: A distance to measure on the contouring axis.
            Returns: An array of points; or null on error.
        """
        pass

    def DivideByCount(self, segmentCount, includeEnds, points=None):
        """
        DivideByCount(self: Curve, segmentCount: int, includeEnds: bool) -> (Array[float], Array[Point3d])
        
            Divide the curve into a number of equal-length segments.
        
            segmentCount: Segment count. Note that the number of division points may differ from the segment count.
            includeEnds: If true, then the points at the start and end of the curve are included.
            Returns: Array containing division curve parameters on success, null on failure.
        DivideByCount(self: Curve, segmentCount: int, includeEnds: bool) -> Array[float]
        
            Divide the curve into a number of equal-length segments.
        
            segmentCount: Segment count. Note that the number of division points may differ from the segment count.
            includeEnds: If true, then the points at the start and end of the curve are included.
            Returns: List of curve parameters at the division points on success, null on failure.
        """
        pass

    def DivideByLength(self, segmentLength, includeStart, points=None):
        """
        DivideByLength(self: Curve, segmentLength: float, includeStart: bool) -> (Array[float], Array[Point3d])
        
            Divide the curve into specific length segments.
        
            segmentLength: The length of each and every segment (except potentially the last one).
            includeStart: If true, then the point at the start of the curve is included.
            Returns: Array containing division curve parameters if successful, null on failure.
        DivideByLength(self: Curve, segmentLength: float, includeStart: bool) -> Array[float]
        
            Divide the curve into specific length segments.
        
            segmentLength: The length of each and every segment (except potentially the last one).
            includeStart: If true, then the points at the start of the curve is included.
            Returns: Array containing division curve parameters if successful, null on failure.
        """
        pass

    def DivideEquidistant(self, distance):
        """
        DivideEquidistant(self: Curve, distance: float) -> Array[Point3d]
        
            Calculates 3d points on a curve where the linear distance between the points is equal.
        
            distance: The distance betwen division points.
            Returns: An array of equidistant points, or null on error.
        """
        pass

    @staticmethod
    def DoDirectionsMatch(curveA, curveB):
        """
        DoDirectionsMatch(curveA: Curve, curveB: Curve) -> bool
        
            Determines whether two curves travel more or less in the same direction.
        
            curveA: First curve to test.
            curveB: Second curve to test.
            Returns: true if both curves more or less point in the same direction, 
                    false if they point 
             in the opposite directions.
        """
        pass

    def Duplicate(self):
        """
        Duplicate(self: Curve) -> GeometryBase
        
            Constructs an exact duplicate of this Curve.
        """
        pass

    def DuplicateCurve(self):
        """
        DuplicateCurve(self: Curve) -> Curve
        
            Constructs an exact duplicate of this curve.
            Returns: An exact copy of this curve.
        """
        pass

    def DuplicateSegments(self):
        """
        DuplicateSegments(self: Curve) -> Array[Curve]
        
            Polylines will be exploded into line segments. ExplodeCurves will
                    return the curves 
             in topological order.
        
            Returns: An array of all the segments that make up this curve.
        """
        pass

    def Extend(self, *__args):
        """
        Extend(self: Curve, side: CurveEnd, style: CurveExtensionStyle, geometry: IEnumerable[GeometryBase]) -> Curve
        Extend(self: Curve, side: CurveEnd, style: CurveExtensionStyle, endPoint: Point3d) -> Curve
        
            Extends a curve to a point.
        
            side: The end of the curve to extend.
            style: The style or type of extension to use.
            endPoint: A new end point.
            Returns: New extended curve result on success, null on failure.
        Extend(self: Curve, side: CurveEnd, length: float, style: CurveExtensionStyle) -> Curve
        
            Extends a curve by a specific length.
        
            side: Curve end to extend.
            length: Length to add to the curve end.
            style: Extension style.
            Returns: A curve with extended ends or null on failure.
        Extend(self: Curve, t0: float, t1: float) -> Curve
        
            Where possible, analytically extends curve to include the given domain. 
                    This will 
             not work on closed curves. The original curve will be identical to the 
                    restriction 
             of the resulting curve to the original curve domain.
        
        
            t0: Start of extension domain, if the start is not inside the 
                    Domain of this curve, an 
             attempt will be made to extend the curve.
        
            t1: End of extension domain, if the end is not inside the 
                    Domain of this curve, an 
             attempt will be made to extend the curve.
        
            Returns: Extended curve on success, null on failure.
        Extend(self: Curve, domain: Interval) -> Curve
        
            Where possible, analytically extends curve to include the given domain. 
                    This will 
             not work on closed curves. The original curve will be identical to the 
                    restriction 
             of the resulting curve to the original curve domain.
        
        
            domain: Extension domain.
            Returns: Extended curve on success, null on failure.
        """
        pass

    def ExtendByArc(self, side, geometry):
        """ ExtendByArc(self: Curve, side: CurveEnd, geometry: IEnumerable[GeometryBase]) -> Curve """
        pass

    def ExtendByLine(self, side, geometry):
        """ ExtendByLine(self: Curve, side: CurveEnd, geometry: IEnumerable[GeometryBase]) -> Curve """
        pass

    def ExtendOnSurface(self, side, *__args):
        """
        ExtendOnSurface(self: Curve, side: CurveEnd, face: BrepFace) -> Curve
        
            Extends a curve on a surface.
        
            side: The end of the curve to extend.
            face: BrepFace that contains the curve.
            Returns: New extended curve result on success, null on failure.
        ExtendOnSurface(self: Curve, side: CurveEnd, surface: Surface) -> Curve
        
            Extends a curve on a surface.
        
            side: The end of the curve to extend.
            surface: Surface that contains the curve.
            Returns: New extended curve result on success, null on failure.
        """
        pass

    def Fair(self, distanceTolerance, angleTolerance, clampStart, clampEnd, iterations):
        """
        Fair(self: Curve, distanceTolerance: float, angleTolerance: float, clampStart: int, clampEnd: int, iterations: int) -> Curve
        
            Fairs a curve object. Fair works best on degree 3 (cubic) curves. Attempts to 
                    
             remove large curvature variations while limiting the geometry changes to be no 
                    
             more than the specified tolerance.
        
        
            distanceTolerance: Maximum allowed distance the faired curve is allowed to deviate from the input.
            angleTolerance: (in radians) kinks with angles <= angleTolerance are smoothed out 0.05 is a good default.
            clampStart: The number of (control vertices-1) to preserve at start. 
                    0 = preserve start point1 
             = preserve start point and 1st derivative2 = preserve start point, 1st and 2nd derivative
        
            clampEnd: Same as clampStart.
            iterations: The number of iteratoins to use in adjusting the curve.
            Returns: Returns new faired Curve on success, null on failure.
        """
        pass

    def Fit(self, degree, fitTolerance, angleTolerance):
        """
        Fit(self: Curve, degree: int, fitTolerance: float, angleTolerance: float) -> Curve
        
            Fits a new curve through an existing curve.
        
            degree: The degree of the returned Curve. Must be bigger than 1.
            fitTolerance: The fitting tolerance. If fitTolerance is RhinoMath.UnsetValue or <=0.0,
                    the 
             document absolute tolerance is used.
        
            angleTolerance: The kink smoothing tolerance in radians.
                    If angleTolerance is 0.0, all kinks are 
             smoothedIf angleTolerance is >0.0, kinks smaller than angleTolerance are smoothedIf 
             angleTolerance is RhinoMath.UnsetValue or <0.0, the document angle tolerance is used for the 
             kink smoothing
        
            Returns: Returns a new fitted Curve if successful, null on failure.
        """
        pass

    def FrameAt(self, t, plane):
        """
        FrameAt(self: Curve, t: float) -> (bool, Plane)
        
            Returns a 3d frame at a parameter.
        
            t: Evaluation parameter.
            Returns: true on success, false on failure.
        """
        pass

    def GetCurveParameterFromNurbsFormParameter(self, nurbsParameter, curveParameter):
        """
        GetCurveParameterFromNurbsFormParameter(self: Curve, nurbsParameter: float) -> (bool, float)
        
            Convert a NURBS curve parameter to a curve parameter.
        
            nurbsParameter: Nurbs form parameter.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def GetDistancesBetweenCurves(curveA, curveB, tolerance, maxDistance, maxDistanceParameterA, maxDistanceParameterB, minDistance, minDistanceParameterA, minDistanceParameterB):
        """
        GetDistancesBetweenCurves(curveA: Curve, curveB: Curve, tolerance: float) -> (bool, float, float, float, float, float, float)
        
            Computes the distances between two arbitrary curves that overlap.
        
            curveA: A curve.
            curveB: Another curve.
            tolerance: A tolerance value.
            Returns: true if the operation succeeded; otherwise false.
        """
        pass

    @staticmethod
    def GetFilletPoints(curve0, curve1, radius, t0Base, t1Base, t0, t1, filletPlane):
        """
        GetFilletPoints(curve0: Curve, curve1: Curve, radius: float, t0Base: float, t1Base: float) -> (bool, float, float, Plane)
        
            Finds points at which to cut a pair of curves so that a fillet of given radius can be inserted.
        
            curve0: First curve to fillet.
            curve1: Second curve to fillet.
            radius: Fillet radius.
            t0Base: Parameter value for base point on curve0.
            t1Base: Parameter value for base point on curve1.
            Returns: true on success, false on failure.
        """
        pass

    def GetLength(self, *__args):
        """
        GetLength(self: Curve, subdomain: Interval) -> float
        
            Get the length of a sub-section of the curve with a fractional tolerance of 1e-8.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve (must be non-decreasing).
            Returns: The length of the sub-curve on success, or zero on failure.
        GetLength(self: Curve, fractionalTolerance: float, subdomain: Interval) -> float
        
            Get the length of a sub-section of the curve.
        
            fractionalTolerance: Desired fractional precision. 
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve (must be non-decreasing).
            Returns: The length of the sub-curve on success, or zero on failure.
        GetLength(self: Curve) -> float
        
            Gets the length of the curve with a fractional tolerance of 1.0e-8.
            Returns: The length of the curve on success, or zero on failure.
        GetLength(self: Curve, fractionalTolerance: float) -> float
        
            Get the length of the curve.
        
            fractionalTolerance: Desired fractional precision. 
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            Returns: The length of the curve on success, or zero on failure.
        """
        pass

    def GetNextDiscontinuity(self, continuityType, t0, t1, t):
        """
        GetNextDiscontinuity(self: Curve, continuityType: Continuity, t0: float, t1: float) -> (bool, float)
        
            Searches for a derivative, tangent, or curvature discontinuity.
        
            continuityType: Type of continuity to search for.
            t0: Search begins at t0. If there is a discontinuity at t0, it will be ignored. This makes it
              
                   possible to repeatedly call GetNextDiscontinuity() and step through the discontinuities.
        
            t1: (t0 != t1)  If there is a discontinuity at t1 it will be ignored unless continuityType is
              
                   a locus discontinuity type and t1 is at the start or end of the curve.
        
            Returns: Parametric continuity tests c = (C0_continuous, ..., G2_continuous):
                     true if a 
             parametric discontinuity was found strictly between t0 and t1. Note well that
                     all 
             curves are parametrically continuous at the ends of their domains.
                    
                    
             Locus continuity tests c = (C0_locus_continuous, ...,G2_locus_continuous):
                     true if 
             a locus discontinuity was found strictly between t0 and t1 or at t1 is the at the end
                  
                of a curve. Note well that all open curves (IsClosed()=false) are locus discontinuous at the
        
                          ends of their domains.  All closed curves (IsClosed()=true) are at least 
             C0_locus_continuous at 
                     the ends of their domains.
        """
        pass

    def GetNurbsFormParameterFromCurveParameter(self, curveParameter, nurbsParameter):
        """
        GetNurbsFormParameterFromCurveParameter(self: Curve, curveParameter: float) -> (bool, float)
        
            Convert a curve parameter to a NURBS curve parameter.
        
            curveParameter: Curve parameter.
            Returns: true on success, false on failure.
        """
        pass

    def GetPerpendicularFrames(self, parameters):
        """ GetPerpendicularFrames(self: Curve, parameters: IEnumerable[float]) -> Array[Plane] """
        pass

    def HasNurbsForm(self):
        """
        HasNurbsForm(self: Curve) -> int
        
            Does a NURBS curve representation of this curve exist?
            Returns: 0   unable to create NURBS representation with desired accuracy.
                    1   success - 
             NURBS parameterization matches the curve's to the desired accuracy
                    2   success - 
             NURBS point locus matches the curve's and the domain of the NURBS
                                  
             curve is correct. However, This curve's parameterization and the
                                  
             NURBS curve parameterization may not match. This situation happens
                                  
             when getting NURBS representations of curves that have a
                                  
             transendental parameterization like circles.
        """
        pass

    def IsArc(self, tolerance=None):
        """
        IsArc(self: Curve, tolerance: float) -> bool
        
            Test a curve to see if it can be represented by an arc or circle within the given tolerance.
        
            tolerance: Tolerance to use when checking.
            Returns: true if the curve can be represented by an arc or a circle within tolerance.
        IsArc(self: Curve) -> bool
        
            Test a curve to see if it can be represented by an arc or circle within RhinoMath.ZeroTolerance.
            Returns: true if the curve can be represented by an arc or a circle within tolerance.
        """
        pass

    def IsCircle(self, tolerance=None):
        """
        IsCircle(self: Curve, tolerance: float) -> bool
        
            Test a curve to see if it can be represented by a circle within the given tolerance.
        
            tolerance: Tolerance to use when checking.
            Returns: true if the curve can be represented by a circle to within tolerance.
        IsCircle(self: Curve) -> bool
        
            Test a curve to see if it can be represented by a circle within RhinoMath.ZeroTolerance.
            Returns: true if the Curve can be represented by a circle within tolerance.
        """
        pass

    def IsClosable(self, tolerance, minimumAbsoluteSize=None, minimumRelativeSize=None):
        """
        IsClosable(self: Curve, tolerance: float) -> bool
        
            Decide if it makes sense to close off this curve by moving the endpoint 
                    to the 
             start based on start-end gap size and length of curve as 
                    approximated by chord 
             defined by 6 points.
        
        
            tolerance: Maximum allowable distance between start and end. 
                    If start - end gap is greater 
             than tolerance, this function will return false.
        
            Returns: true if start and end points are close enough based on above conditions.
        IsClosable(self: Curve, tolerance: float, minimumAbsoluteSize: float, minimumRelativeSize: float) -> bool
        
            Decide if it makes sense to close off this curve by moving the endpoint
                    to the 
             start based on start-end gap size and length of curve as
                    approximated by chord 
             defined by 6 points.
        
        
            tolerance: Maximum allowable distance between start and end. 
                    If start - end gap is greater 
             than tolerance, this function will return false.
        
            minimumAbsoluteSize: If greater than 0.0 and none of the interior sampled points are at
                    least 
             minimumAbsoluteSize from start, this function will return false.
        
            minimumRelativeSize: If greater than 1.0 and chord length is less than 
                    minimumRelativeSize*gap, this 
             function will return false.
        
            Returns: true if start and end points are close enough based on above conditions.
        """
        pass

    def IsContinuous(self, continuityType, t):
        """
        IsContinuous(self: Curve, continuityType: Continuity, t: float) -> bool
        
            Test continuity at a curve parameter value.
        
            continuityType: Type of continuity to test for.
            t: Parameter to test.
            Returns: true if the curve has at least the c type continuity at the parameter t.
        """
        pass

    def IsEllipse(self, tolerance=None):
        """
        IsEllipse(self: Curve, tolerance: float) -> bool
        
            Test a curve to see if it can be represented by an ellipse within a given tolerance.
        
            tolerance: Tolerance to use for checking.
            Returns: true if the Curve can be represented by an ellipse within tolerance.
        IsEllipse(self: Curve) -> bool
        
            Test a curve to see if it can be represented by an ellipse within RhinoMath.ZeroTolerance.
            Returns: true if the Curve can be represented by an ellipse within tolerance.
        """
        pass

    def IsInPlane(self, testPlane, tolerance=None):
        """
        IsInPlane(self: Curve, testPlane: Plane, tolerance: float) -> bool
        
            Test a curve to see if it lies in a specific plane.
        
            testPlane: Plane to test for.
            tolerance: Tolerance to use when checking.
            Returns: true if the maximum distance from the curve to the testPlane is <= tolerance.
        IsInPlane(self: Curve, testPlane: Plane) -> bool
        
            Test a curve to see if it lies in a specific plane.
        
            testPlane: Plane to test for.
            Returns: true if the maximum distance from the curve to the testPlane is <= RhinoMath.ZeroTolerance.
        """
        pass

    def IsLinear(self, tolerance=None):
        """
        IsLinear(self: Curve, tolerance: float) -> bool
        
            Test a curve to see if it is linear to within the custom tolerance.
        
            tolerance: Tolerance to use when checking linearity.
            Returns: true if the ends of the curve are farther than tolerance apart
                    and the maximum 
             distance from any point on the curve to
                    the line segment connecting the curve ends 
             is <= tolerance.
        
        IsLinear(self: Curve) -> bool
        
            Test a curve to see if it is linear to within RhinoMath.ZeroTolerance units (1e-12).
            Returns: true if the curve is linear.
        """
        pass

    def IsPlanar(self, tolerance=None):
        """
        IsPlanar(self: Curve, tolerance: float) -> bool
        
            Test a curve for planarity.
        
            tolerance: Tolerance to use when checking.
            Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 
             tolerance.
        
        IsPlanar(self: Curve) -> bool
        
            Test a curve for planarity.
            Returns: true if the curve is planar (flat) to within RhinoMath.ZeroTolerance units (1e-12).
        """
        pass

    def IsPolyline(self):
        """
        IsPolyline(self: Curve) -> bool
        
            Several types of Curve can have the form of a polyline
                    including a degree 1 
             NurbsCurve, a PolylineCurve,
                    and a PolyCurve all of whose segments are some form of
             
                    polyline. IsPolyline tests a curve to see if it can be
                    represented as 
             a polyline.
        
            Returns: true if this curve can be represented as a polyline; otherwise, false.
        """
        pass

    def IsShort(self, tolerance, subdomain=None):
        """
        IsShort(self: Curve, tolerance: float, subdomain: Interval) -> bool
        
            Used to quickly find short curves.
        
            tolerance: Length threshold value for "shortness".
            subdomain: The test is performed on the interval that is the intersection of subdomain with Domain()
            Returns: true if the length of the curve is <= tolerance.
        IsShort(self: Curve, tolerance: float) -> bool
        
            Used to quickly find short curves.
        
            tolerance: Length threshold value for "shortness".
            Returns: true if the length of the curve is <= tolerance.
        """
        pass

    @staticmethod
    def JoinCurves(inputCurves, joinTolerance=None, preserveDirection=None):
        """
        JoinCurves(inputCurves: IEnumerable[Curve], joinTolerance: float, preserveDirection: bool) -> Array[Curve]
        JoinCurves(inputCurves: IEnumerable[Curve], joinTolerance: float) -> Array[Curve]
        JoinCurves(inputCurves: IEnumerable[Curve]) -> Array[Curve]
        """
        pass

    def LengthParameter(self, segmentLength, t, *__args):
        """
        LengthParameter(self: Curve, segmentLength: float, subdomain: Interval) -> (bool, float)
        
            Gets the parameter along the curve which coincides with a given length along the curve. 
               
                  A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            segmentLength: Length of segment to measure. Must be less than or equal to the length of the subdomain.
            subdomain: The calculation is performed on the specified sub-domain of the curve rather than the whole 
             curve.
        
            Returns: true on success, false on failure.
        LengthParameter(self: Curve, segmentLength: float, fractionalTolerance: float, subdomain: Interval) -> (bool, float)
        
            Gets the parameter along the curve which coincides with a given length along the curve.
        
            segmentLength: Length of segment to measure. Must be less than or equal to the length of the subdomain.
            fractionalTolerance: Desired fractional precision. 
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve rather than the whole 
             curve.
        
            Returns: true on success, false on failure.
        LengthParameter(self: Curve, segmentLength: float) -> (bool, float)
        
            Gets the parameter along the curve which coincides with a given length along the curve. 
               
                  A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            segmentLength: Length of segment to measure. Must be less than or equal to the length of the curve.
            Returns: true on success, false on failure.
        LengthParameter(self: Curve, segmentLength: float, fractionalTolerance: float) -> (bool, float)
        
            Gets the parameter along the curve which coincides with a given length along the curve.
        
            segmentLength: Length of segment to measure. Must be less than or equal to the length of the curve.
            fractionalTolerance: Desired fractional precision.
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            Returns: true on success, false on failure.
        """
        pass

    def MakeClosed(self, tolerance):
        """
        MakeClosed(self: Curve, tolerance: float) -> bool
        
            If IsClosed, just return true. Otherwise, decide if curve can be closed as 
                    
             follows: Linear curves polylinear curves with 2 segments, Nurbs with 3 or less 
                    
             control points cannot be made closed. Also, if tolerance > 0 and the gap between 
                    
             start and end is larger than tolerance, curve cannot be made closed. 
                    Adjust the 
             curve's endpoint to match its start point.
        
        
            tolerance: If nonzero, and the gap is more than tolerance, curve cannot be made closed.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def MakeEndsMeet(curveA, adjustStartCurveA, curveB, adjustStartCurveB):
        """
        MakeEndsMeet(curveA: Curve, adjustStartCurveA: bool, curveB: Curve, adjustStartCurveB: bool) -> bool
        
            Makes adjustments to the ends of one or both input curves so that they meet at a point.
        
            curveA: 1st curve to adjust.
            adjustStartCurveA: Which end of the 1st curve to adjust: true is start, false is end.
            curveB: 2nd curve to adjust.
            adjustStartCurveB: which end of the 2nd curve to adjust true==start, false==end.
            Returns: true on success.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def NormalizedLengthParameter(self, s, t, *__args):
        """
        NormalizedLengthParameter(self: Curve, s: float, subdomain: Interval) -> (bool, float)
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve. 
                    A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            s: Normalized arc length parameter. 
                    E.g., 0 = start of curve, 1/2 = midpoint of 
             curve, 1 = end of curve.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve.
            Returns: true on success, false on failure.
        NormalizedLengthParameter(self: Curve, s: float, fractionalTolerance: float, subdomain: Interval) -> (bool, float)
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve.
        
        
            s: Normalized arc length parameter. 
                    E.g., 0 = start of curve, 1/2 = midpoint of 
             curve, 1 = end of curve.
        
            fractionalTolerance: Desired fractional precision. 
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve.
            Returns: true on success, false on failure.
        NormalizedLengthParameter(self: Curve, s: float) -> (bool, float)
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve. 
                    A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            s: Normalized arc length parameter. 
                    E.g., 0 = start of curve, 1/2 = midpoint of 
             curve, 1 = end of curve.
        
            Returns: true on success, false on failure.
        NormalizedLengthParameter(self: Curve, s: float, fractionalTolerance: float) -> (bool, float)
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve.
        
        
            s: Normalized arc length parameter. 
                    E.g., 0 = start of curve, 1/2 = midpoint of 
             curve, 1 = end of curve.
        
            fractionalTolerance: Desired fractional precision. 
                    fabs(("exact" length from start to t) - 
             arc_length)/arc_length <= fractionalTolerance.
        
            Returns: true on success, false on failure.
        """
        pass

    def NormalizedLengthParameters(self, s, absoluteTolerance, *__args):
        """
        NormalizedLengthParameters(self: Curve, s: Array[float], absoluteTolerance: float, subdomain: Interval) -> Array[float]
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve. 
                    A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            s: Array of normalized arc length parameters. 
                    E.g., 0 = start of curve, 1/2 = 
             midpoint of curve, 1 = end of curve.
        
            absoluteTolerance: If absoluteTolerance > 0, then the difference between (s[i+1]-s[i])*curve_length 
                    
             and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve. 
                    A 0.0 s 
             value corresponds to subdomain->Min() and a 1.0 s value corresponds to subdomain->Max().
        
            Returns: If successful, array of curve parameters such that the length of the curve from its start to 
             t[i] is s[i]*curve_length. 
                    Null on failure.
        
        NormalizedLengthParameters(self: Curve, s: Array[float], absoluteTolerance: float, fractionalTolerance: float, subdomain: Interval) -> Array[float]
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve.
        
        
            s: Array of normalized arc length parameters. 
                    E.g., 0 = start of curve, 1/2 = 
             midpoint of curve, 1 = end of curve.
        
            absoluteTolerance: If absoluteTolerance > 0, then the difference between (s[i+1]-s[i])*curve_length 
                    
             and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.
        
            fractionalTolerance: Desired fractional precision for each segment. 
                    fabs("true" length - actual 
             length)/(actual length) <= fractionalTolerance.
        
            subdomain: The calculation is performed on the specified sub-domain of the curve. 
                    A 0.0 s 
             value corresponds to subdomain->Min() and a 1.0 s value corresponds to subdomain->Max().
        
            Returns: If successful, array of curve parameters such that the length of the curve from its start to 
             t[i] is s[i]*curve_length. 
                    Null on failure.
        
        NormalizedLengthParameters(self: Curve, s: Array[float], absoluteTolerance: float) -> Array[float]
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve. 
                    A fractional tolerance of 1e-8 is used in this version of the function.
        
        
            s: Array of normalized arc length parameters. 
                    E.g., 0 = start of curve, 1/2 = 
             midpoint of curve, 1 = end of curve.
        
            absoluteTolerance: If absoluteTolerance > 0, then the difference between (s[i+1]-s[i])*curve_length 
                    
             and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.
        
            Returns: If successful, array of curve parameters such that the length of the curve from its start to 
             t[i] is s[i]*curve_length. 
                    Null on failure.
        
        NormalizedLengthParameters(self: Curve, s: Array[float], absoluteTolerance: float, fractionalTolerance: float) -> Array[float]
        
            Input the parameter of the point on the curve that is a prescribed arc length from the start of 
             the curve.
        
        
            s: Array of normalized arc length parameters. 
                    E.g., 0 = start of curve, 1/2 = 
             midpoint of curve, 1 = end of curve.
        
            absoluteTolerance: If absoluteTolerance > 0, then the difference between (s[i+1]-s[i])*curve_length 
                    
             and the length of the curve segment from t[i] to t[i+1] will be <= absoluteTolerance.
        
            fractionalTolerance: Desired fractional precision for each segment. 
                    fabs("true" length - actual 
             length)/(actual length) <= fractionalTolerance.
        
            Returns: If successful, array of curve parameters such that the length of the curve from its start to 
             t[i] is s[i]*curve_length. 
                    Null on failure.
        """
        pass

    def Offset(self, *__args):
        """
        Offset(self: Curve, directionPoint: Point3d, normal: Vector3d, distance: float, tolerance: float, cornerStyle: CurveOffsetCornerStyle) -> Array[Curve]
        
            Offsets this curve. If you have a nice offset, then there will be one entry in 
                    the 
             array. If the original curve had kinks or the offset curve had self 
                    intersections, 
             you will get multiple segments in the offset_curves[] array.
        
        
            directionPoint: A point that indicates the direction of the offset.
            normal: The normal to the offset plane.
            distance: The positive or negative distance to offset.
            tolerance: The offset or fitting tolerance.
            cornerStyle: Corner style for offset kinks.
            Returns: Offset curves on success, null on failure.
        Offset(self: Curve, plane: Plane, distance: float, tolerance: float, cornerStyle: CurveOffsetCornerStyle) -> Array[Curve]
        
            Offsets this curve. If you have a nice offset, then there will be one entry in 
                    the 
             array. If the original curve had kinks or the offset curve had self 
                    intersections, 
             you will get multiple segments in the offset_curves[] array.
        
        
            plane: Offset solution plane.
            distance: The positive or negative distance to offset.
            tolerance: The offset or fitting tolerance.
            cornerStyle: Corner style for offset kinks.
            Returns: Offset curves on success, null on failure.
        """
        pass

    def OffsetNormalToSurface(self, surface, height):
        """
        OffsetNormalToSurface(self: Curve, surface: Surface, height: float) -> Curve
        
            Finds a curve by offsetting an existing curve normal to a surface.
                    The caller is 
             responsible for ensuring that the curve lies on the input surface.
        
        
            surface: Surface from which normals are calculated.
            height: offset distance (distance from surface to result curve)
            Returns: Offset curve at distance height from the surface.  The offset curve is
                    interpolated 
             through a small number of points so if the surface is irregular
                    or complicated, the 
             result will not be a very accurate offset.
        """
        pass

    def OffsetOnSurface(self, *__args):
        """
        OffsetOnSurface(self: Curve, surface: Surface, distance: float, fittingTolerance: float) -> Array[Curve]
        
            Offset a curve on a surface. This curve must lie on the surface.
        
            surface: A surface on which to offset.
            distance: A distance to offset (+)left, (-)right.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        OffsetOnSurface(self: Curve, surface: Surface, throughPoint: Point2d, fittingTolerance: float) -> Array[Curve]
        
            Offset a curve on a surface. This curve must lie on the surface.
                    This overload 
             allows to specify a surface point at which the offset will pass.
        
        
            surface: A surface on which to offset.
            throughPoint: 2d point on the brep face to offset through.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        OffsetOnSurface(self: Curve, surface: Surface, curveParameters: Array[float], offsetDistances: Array[float], fittingTolerance: float) -> Array[Curve]
        
            Offset this curve on a surface. This curve must lie on the surface.
                    This overload 
             allows to specify different offsets for different curve parameters.
        
        
            surface: A surface on which to offset.
            curveParameters: Curve parameters corresponding to the offset distances.
            offsetDistances: Distances to offset (+)left, (-)right.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        OffsetOnSurface(self: Curve, face: BrepFace, distance: float, fittingTolerance: float) -> Array[Curve]
        
            Offset this curve on a brep face surface. This curve must lie on the surface.
        
            face: The brep face on which to offset.
            distance: A distance to offset (+)left, (-)right.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        OffsetOnSurface(self: Curve, face: BrepFace, throughPoint: Point2d, fittingTolerance: float) -> Array[Curve]
        
            Offset a curve on a brep face surface. This curve must lie on the surface.
                    This 
             overload allows to specify a surface point at which the offset will pass.
        
        
            face: The brep face on which to offset.
            throughPoint: 2d point on the brep face to offset through.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        OffsetOnSurface(self: Curve, face: BrepFace, curveParameters: Array[float], offsetDistances: Array[float], fittingTolerance: float) -> Array[Curve]
        
            Offset a curve on a brep face surface. This curve must lie on the surface.
                    This 
             overload allows to specify different offsets for different curve parameters.
        
        
            face: The brep face on which to offset.
            curveParameters: Curve parameters corresponding to the offset distances.
            offsetDistances: distances to offset (+)left, (-)right.
            fittingTolerance: A fitting tolerance.
            Returns: Offset curves on success, or null on failure.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def PerpendicularFrameAt(self, t, plane):
        """
        PerpendicularFrameAt(self: Curve, t: float) -> (bool, Plane)
        
            Return a 3d frame at a parameter. This is slightly different than FrameAt in
                    that 
             the frame is computed in a way so there is minimal rotation from one
                    frame to the 
             next.
        
        
            t: Evaluation parameter.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def PlanarClosedCurveRelationship(curveA, curveB, testPlane, tolerance):
        """
        PlanarClosedCurveRelationship(curveA: Curve, curveB: Curve, testPlane: Plane, tolerance: float) -> RegionContainment
        
            Determines whether two coplanar simple closed curves are disjoint or intersect;
                    
             otherwise, if the regions have a containment relationship, discovers
                    which curve 
             encloses the other.
        
        
            curveA: A first curve.
            curveB: A second curve.
            testPlane: A plane.
            tolerance: A tolerance value.
            Returns: A value indicating the relationship between the first and the second curve.
        """
        pass

    @staticmethod
    def PlanarCurveCollision(curveA, curveB, testPlane, tolerance):
        """
        PlanarCurveCollision(curveA: Curve, curveB: Curve, testPlane: Plane, tolerance: float) -> bool
        
            Determines if two coplanar curves collide (intersect).
        
            curveA: A curve.
            curveB: Another curve.
            testPlane: A valid plane containing the curves.
            tolerance: A tolerance value for intersection.
            Returns: true if the curves intersect, otherwise false
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Curve, t: float) -> Point3d
        
            Evaluates point at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Point (location of curve at the parameter t).
        """
        pass

    def PointAtLength(self, length):
        """
        PointAtLength(self: Curve, length: float) -> Point3d
        
            Gets a point at a certain length along the curve. The length must be 
                    non-negative 
             and less than or equal to the length of the curve. 
                    Lengths will not be wrapped 
             when the curve is closed or periodic.
        
        
            length: Length along the curve between the start point and the returned point.
            Returns: Point on the curve at the specified length from the start point or Poin3d.Unset on failure.
        """
        pass

    def PointAtNormalizedLength(self, length):
        """
        PointAtNormalizedLength(self: Curve, length: float) -> Point3d
        
            Gets a point at a certain normalized length along the curve. The length must be 
                    
             between or including 0.0 and 1.0, where 0.0 equals the start of the curve and 
                    1.0 
             equals the end of the curve.
        
        
            length: Normalized length along the curve between the start point and the returned point.
            Returns: Point on the curve at the specified normalized length from the start point or Poin3d.Unset on 
             failure.
        """
        pass

    @staticmethod
    def ProjectToBrep(*__args):
        """
        ProjectToBrep(curves: IEnumerable[Curve], breps: IEnumerable[Brep], direction: Vector3d, tolerance: float) -> Array[Curve]
        ProjectToBrep(curves: IEnumerable[Curve], breps: IEnumerable[Brep], direction: Vector3d, tolerance: float) -> (Array[Curve], Array[int], Array[int])
        ProjectToBrep(curve: Curve, breps: IEnumerable[Brep], direction: Vector3d, tolerance: float) -> (Array[Curve], Array[int])
        ProjectToBrep(curve: Curve, brep: Brep, direction: Vector3d, tolerance: float) -> Array[Curve]
        
            Projects a Curve onto a Brep along a given direction.
        
            curve: Curve to project.
            brep: Brep to project onto.
            direction: Direction of projection.
            tolerance: Tolerance to use for projection.
            Returns: An array of projected curves or empty array if the projection set is empty.
        ProjectToBrep(curve: Curve, breps: IEnumerable[Brep], direction: Vector3d, tolerance: float) -> Array[Curve]
        """
        pass

    @staticmethod
    def ProjectToMesh(*__args):
        """
        ProjectToMesh(curves: IEnumerable[Curve], meshes: IEnumerable[Mesh], direction: Vector3d, tolerance: float) -> Array[Curve]
        ProjectToMesh(curve: Curve, meshes: IEnumerable[Mesh], direction: Vector3d, tolerance: float) -> Array[Curve]
        ProjectToMesh(curve: Curve, mesh: Mesh, direction: Vector3d, tolerance: float) -> Array[Curve]
        
            Projects a curve to a mesh using a direction and tolerance.
        
            curve: A curve.
            mesh: A mesh.
            direction: A direction vector.
            tolerance: A tolerance value.
            Returns: A curve array.
        """
        pass

    @staticmethod
    def ProjectToPlane(curve, plane):
        """
        ProjectToPlane(curve: Curve, plane: Plane) -> Curve
        
            Constructs a curve by projecting an existing curve to a plane.
        
            curve: A curve.
            plane: A plane.
            Returns: The projected curve on success; null on failure.
        """
        pass

    def PullToBrepFace(self, *__args):
        """
        PullToBrepFace(curve: Curve, face: BrepFace, tolerance: float) -> Array[Curve]
        
            Pull a curve to a BrepFace using closest point projection.
        
            curve: Curve to pull.
            face: Brepface that pulls.
            tolerance: Tolerance to use for pulling.
            Returns: An array of pulled curves, or an empty array on failure.
        PullToBrepFace(self: Curve, face: BrepFace, tolerance: float) -> Array[Curve]
        
            Pulls this curve to a brep face and returns the result of that operation.
        
            face: A brep face.
            tolerance: A tolerance value.
            Returns: An array containing the resulting curves after pulling. This array could be empty.
        """
        pass

    def PullToMesh(self, mesh, tolerance):
        """
        PullToMesh(self: Curve, mesh: Mesh, tolerance: float) -> PolylineCurve
        
            Makes a polyline approximation of the curve and gets the closest point on the mesh for each 
             point on the curve. 
                    Then it "connects the points" so that you have a polyline on 
             the mesh.
        
        
            mesh: Mesh to project onto.
            tolerance: Input tolerance (RhinoDoc.ModelAbsoluteTolerance is a good default)
            Returns: A polyline curve on success, null on failure.
        """
        pass

    def Rebuild(self, pointCount, degree, preserveTangents):
        """
        Rebuild(self: Curve, pointCount: int, degree: int, preserveTangents: bool) -> NurbsCurve
        
            Rebuild a curve with a specific point count.
        
            pointCount: Number of control points in the rebuild curve.
            degree: Degree of curve. Valid values are between and including 1 and 11.
            preserveTangents: If true, the end tangents of the input curve will be preserved.
            Returns: A Nurbs curve on success or null on failure.
        """
        pass

    def RemoveShortSegments(self, tolerance):
        """
        RemoveShortSegments(self: Curve, tolerance: float) -> bool
        
            Looks for segments that are shorter than tolerance that can be removed. 
                    Does not 
             change the domain, but it will change the relative parameterization.
        
        
            tolerance: Tolerance which defines "short" segments.
            Returns: true if removable short segments were found. 
                    false if no removable short segments 
             were found.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Curve) -> bool
        
            Reverses the direction of the curve.
            Returns: true on success, false on failure.
        """
        pass

    def SetEndPoint(self, point):
        """
        SetEndPoint(self: Curve, point: Point3d) -> bool
        
            Forces the curve to end at a specified point. 
                    Not all curve types support this 
             operation.
        
        
            point: New end point of curve.
            Returns: true on success, false on failure.
        """
        pass

    def SetStartPoint(self, point):
        """
        SetStartPoint(self: Curve, point: Point3d) -> bool
        
            Forces the curve to start at a specified point. 
                    Not all curve types support this 
             operation.
        
        
            point: New start point of curve.
            Returns: true on success, false on failure.
        """
        pass

    def Simplify(self, options, distanceTolerance, angleToleranceRadians):
        """
        Simplify(self: Curve, options: CurveSimplifyOptions, distanceTolerance: float, angleToleranceRadians: float) -> Curve
        
            Returns a geometrically equivalent PolyCurve.
                    The PolyCurve has the following 
             properties
                    1. All the PolyCurve segments are LineCurve, PolylineCurve, ArcCurve, or 
             NurbsCurve.
                    
                    2. The Nurbs Curves segments do not have fully multiple 
             interior knots.
                    
                    3. Rational Nurbs curves do not have constant 
             weights.
                    
                    4. Any segment for which IsLinear() or IsArc() is true is a 
             Line, 
                       Polyline segment, or an Arc.
                    
                    5. Adjacent 
             Colinear or Cocircular segments are combined.
                    
                    6. Segments that meet 
             with G1-continuity have there ends tuned up so
                       that they meet with G1-continuity 
             to within machine precision.
        
        
            options: Simplification options.
            distanceTolerance: A distance tolerance for the simplification.
            angleToleranceRadians: An angle tolerance for the simplification.
            Returns: New simplified curve on success, null on failure.
        """
        pass

    def SimplifyEnd(self, end, options, distanceTolerance, angleToleranceRadians):
        """
        SimplifyEnd(self: Curve, end: CurveEnd, options: CurveSimplifyOptions, distanceTolerance: float, angleToleranceRadians: float) -> Curve
        
            Same as SimplifyCurve, but simplifies only the last two segments at "side" end.
        
            end: If CurveEnd.Start the function simplifies the last two start 
                    side segments, 
             otherwise if CurveEnd.End the last two end side segments are simplified.
        
            options: Simplification options.
            distanceTolerance: A distance tolerance for the simplification.
            angleToleranceRadians: An angle tolerance for the simplification.
            Returns: New simplified curve on success, null on failure.
        """
        pass

    def SpanDomain(self, spanIndex):
        """
        SpanDomain(self: Curve, spanIndex: int) -> Interval
        
            Get the domain of the curve span with the given index. 
                    Use the SpanCount property 
             to test how many spans there are.
        
        
            spanIndex: Index of span.
            Returns: Interval of the span with the given index.
        """
        pass

    def Split(self, *__args):
        """
        Split(self: Curve, cutter: Brep, tolerance: float) -> Array[Curve]
        
            Splits a curve into pieces using a polysurface.
        
            cutter: A cutting surface or polysurface.
            tolerance: A tolerance for computing intersections.
            Returns: An array of curves. This array can be empty.
        Split(self: Curve, cutter: Surface, tolerance: float) -> Array[Curve]
        
            Splits a curve into pieces using a surface.
        
            cutter: A cutting surface or polysurface.
            tolerance: A tolerance for computing intersections.
            Returns: An array of curves. This array can be empty.
        Split(self: Curve, t: float) -> Array[Curve]
        
            Splits (divides) the curve at the specified parameter. 
                    The parameter must be in 
             the interior of the curve's domain.
        
        
            t: Parameter to split the curve at in the interval returned by Domain().
            Returns: Two curves on success, null on failure.
        Split(self: Curve, t: IEnumerable[float]) -> Array[Curve]
        """
        pass

    def TangentAt(self, t):
        """
        TangentAt(self: Curve, t: float) -> Vector3d
        
            Evaluates the unit tangent vector at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Unit tangent vector of the curve at the parameter t.
        """
        pass

    def ToNurbsCurve(self, subdomain=None):
        """
        ToNurbsCurve(self: Curve) -> NurbsCurve
        
            Constructs a NURBS curve representation of this curve.
            Returns: NURBS representation of the curve on success, null on failure.
        ToNurbsCurve(self: Curve, subdomain: Interval) -> NurbsCurve
        
            Constructs a NURBS curve representation of this curve.
        
            subdomain: The NURBS representation for this portion of the curve is returned.
            Returns: NURBS representation of the curve on success, null on failure.
        """
        pass

    def ToPolyline(self, mainSegmentCount, subSegmentCount, maxAngleRadians, maxChordLengthRatio, maxAspectRatio, tolerance, minEdgeLength, maxEdgeLength, keepStartPoint, curveDomain=None):
        """
        ToPolyline(self: Curve, mainSegmentCount: int, subSegmentCount: int, maxAngleRadians: float, maxChordLengthRatio: float, maxAspectRatio: float, tolerance: float, minEdgeLength: float, maxEdgeLength: float, keepStartPoint: bool, curveDomain: Interval) -> PolylineCurve
        
            Gets a polyline approximation of a curve.
        
            mainSegmentCount: If mainSegmentCount <= 0, then both subSegmentCount and mainSegmentCount are ignored. 
                 
                If mainSegmentCount > 0, then subSegmentCount must be >= 1. In this 
                    case the 
             nurb will be broken into mainSegmentCount equally spaced 
                    chords. If needed, each 
             of these chords can be split into as many 
                    subSegmentCount sub-parts if the 
             subdivision is necessary for the 
                    mesh to meet the other meshing constraints. In 
             particular, if 
                    subSegmentCount = 0, then the curve is broken into mainSegmentCount 
             
                    pieces and no further testing is performed.
        
            subSegmentCount: An amount of subsegments.
            maxAngleRadians: ( 0 to pi ) Maximum angle (in radians) between unit tangents at 
                    adjacent vertices.
            maxChordLengthRatio: Maximum permitted value of 
                    (distance chord midpoint to curve) / (length of chord).
            maxAspectRatio: If maxAspectRatio < 1.0, the parameter is ignored. 
                    If 1 <= maxAspectRatio < 
             sqrt(2), it is treated as if maxAspectRatio = sqrt(2). 
                    This parameter controls the 
             maximum permitted value of 
                    (length of longest chord) / (length of shortest chord).
        
            tolerance: If tolerance = 0, the parameter is ignored. 
                    This parameter controls the maximum 
             permitted value of the 
                    distance from the curve to the polyline.
        
            minEdgeLength: The minimum permitted edge length.
            maxEdgeLength: If maxEdgeLength = 0, the parameter 
                    is ignored. This parameter controls the 
             maximum permitted edge length.
        
            keepStartPoint: If true the starting point of the curve 
                    is added to the polyline. If false the 
             starting point of the curve is 
                    not added to the polyline.
        
            curveDomain: This subdomain of the NURBS curve is approximated.
            Returns: PolylineCurve on success, null on error.
        ToPolyline(self: Curve, mainSegmentCount: int, subSegmentCount: int, maxAngleRadians: float, maxChordLengthRatio: float, maxAspectRatio: float, tolerance: float, minEdgeLength: float, maxEdgeLength: float, keepStartPoint: bool) -> PolylineCurve
        
            Gets a polyline approximation of a curve.
        
            mainSegmentCount: If mainSegmentCount <= 0, then both subSegmentCount and mainSegmentCount are ignored. 
                 
                If mainSegmentCount > 0, then subSegmentCount must be >= 1. In this 
                    case the 
             nurb will be broken into mainSegmentCount equally spaced 
                    chords. If needed, each 
             of these chords can be split into as many 
                    subSegmentCount sub-parts if the 
             subdivision is necessary for the 
                    mesh to meet the other meshing constraints. In 
             particular, if 
                    subSegmentCount = 0, then the curve is broken into mainSegmentCount 
             
                    pieces and no further testing is performed.
        
            subSegmentCount: An amount of subsegments.
            maxAngleRadians: ( 0 to pi ) Maximum angle (in radians) between unit tangents at 
                    adjacent vertices.
            maxChordLengthRatio: Maximum permitted value of 
                    (distance chord midpoint to curve) / (length of chord).
            maxAspectRatio: If maxAspectRatio < 1.0, the parameter is ignored. 
                    If 1 <= maxAspectRatio < 
             sqrt(2), it is treated as if maxAspectRatio = sqrt(2). 
                    This parameter controls the 
             maximum permitted value of 
                    (length of longest chord) / (length of shortest chord).
        
            tolerance: If tolerance = 0, the parameter is ignored. 
                    This parameter controls the maximum 
             permitted value of the 
                    distance from the curve to the polyline.
        
            minEdgeLength: The minimum permitted edge length.
            maxEdgeLength: If maxEdgeLength = 0, the parameter 
                    is ignored. This parameter controls the 
             maximum permitted edge length.
        
            keepStartPoint: If true the starting point of the curve 
                    is added to the polyline. If false the 
             starting point of the curve is 
                    not added to the polyline.
        
            Returns: PolylineCurve on success, null on error.
        """
        pass

    def Trim(self, *__args):
        """
        Trim(self: Curve, side: CurveEnd, length: float) -> Curve
        
            Shortens a curve by a given length
            Returns: Trimmed curve if successful, null on failure.
        Trim(self: Curve, domain: Interval) -> Curve
        
            Removes portions of the curve outside the specified interval.
        
            domain: Trimming interval. Portions of the curve before curve(domain[0])
                    and after 
             curve(domain[1]) are removed.
        
            Returns: Trimmed curve if successful, null on failure.
        Trim(self: Curve, t0: float, t1: float) -> Curve
        
            Removes portions of the curve outside the specified interval.
        
            t0: Start of the trimming interval. Portions of the curve before curve(t0) are removed.
            t1: End of the trimming interval. Portions of the curve after curve(t1) are removed.
            Returns: Trimmed portion of this curve is successfull, null on failure.
        """
        pass

    def TryGetArc(self, *__args):
        """
        TryGetArc(self: Curve, plane: Plane) -> (bool, Arc)
        
            Try to convert this curve into an Arc using RhinoMath.ZeroTolerance.
        
            plane: Plane in which the comparison is performed.
            Returns: true if the curve could be converted into an arc within the given plane.
        TryGetArc(self: Curve, plane: Plane, tolerance: float) -> (bool, Arc)
        
            Try to convert this curve into an Arc using a custom tolerance.
        
            plane: Plane in which the comparison is performed.
            tolerance: Tolerance to use when checking.
            Returns: true if the curve could be converted into an arc within the given plane.
        TryGetArc(self: Curve) -> (bool, Arc)
        
            Try to convert this curve into an Arc using RhinoMath.ZeroTolerance.
            Returns: true if the curve could be converted into an arc.
        TryGetArc(self: Curve, tolerance: float) -> (bool, Arc)
        
            Try to convert this curve into an Arc using a custom tolerance.
        
            tolerance: Tolerance to use when checking.
            Returns: true if the curve could be converted into an arc.
        """
        pass

    def TryGetCircle(self, circle, tolerance=None):
        """
        TryGetCircle(self: Curve, tolerance: float) -> (bool, Circle)
        
            Try to convert this curve into a Circle using a custom tolerance.
        
            tolerance: Tolerance to use when checking.
            Returns: true if the curve could be converted into a Circle within tolerance.
        TryGetCircle(self: Curve) -> (bool, Circle)
        
            Try to convert this curve into a circle using RhinoMath.ZeroTolerance.
            Returns: true if the curve could be converted into a Circle.
        """
        pass

    def TryGetEllipse(self, *__args):
        """
        TryGetEllipse(self: Curve, plane: Plane) -> (bool, Ellipse)
        
            Try to convert this curve into an Ellipse within RhinoMath.ZeroTolerance.
        
            plane: Plane in which the comparison is performed.
            Returns: true if the curve could be converted into an Ellipse within the given plane.
        TryGetEllipse(self: Curve, plane: Plane, tolerance: float) -> (bool, Ellipse)
        
            Try to convert this curve into an Ellipse using a custom tolerance.
        
            plane: Plane in which the comparison is performed.
            tolerance: Tolerance to use when checking.
            Returns: true if the curve could be converted into an Ellipse within the given plane.
        TryGetEllipse(self: Curve) -> (bool, Ellipse)
        
            Try to convert this curve into an Ellipse within RhinoMath.ZeroTolerance.
            Returns: true if the curve could be converted into an Ellipse.
        TryGetEllipse(self: Curve, tolerance: float) -> (bool, Ellipse)
        
            Try to convert this curve into an Ellipse using a custom tolerance.
        
            tolerance: Tolerance to use when checking.
            Returns: true if the curve could be converted into an Ellipse.
        """
        pass

    def TryGetPlane(self, plane, tolerance=None):
        """
        TryGetPlane(self: Curve, tolerance: float) -> (bool, Plane)
        
            Test a curve for planarity and return the plane.
        
            tolerance: Tolerance to use when checking.
            Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 
             tolerance.
        
        TryGetPlane(self: Curve) -> (bool, Plane)
        
            Test a curve for planarity and return the plane.
            Returns: true if there is a plane such that the maximum distance from the curve to the plane is <= 
             RhinoMath.ZeroTolerance.
        """
        pass

    def TryGetPolyline(self, polyline, parameters=None):
        """
        TryGetPolyline(self: Curve) -> (bool, Polyline, Array[float])
        
            Several types of Curve can have the form of a polyline 
                    including a degree 1 
             NurbsCurve, a PolylineCurve, 
                    and a PolyCurve all of whose segments are some form 
             of 
                    polyline. IsPolyline tests a curve to see if it can be 
                    
             represented as a polyline.
        
            Returns: true if this curve can be represented as a polyline; otherwise, false.
        TryGetPolyline(self: Curve) -> (bool, Polyline)
        
            Several types of Curve can have the form of a polyline 
                    including a degree 1 
             NurbsCurve, a PolylineCurve, 
                    and a PolyCurve all of whose segments are some form 
             of 
                    polyline. IsPolyline tests a curve to see if it can be 
                    
             represented as a polyline.
        
            Returns: true if this curve can be represented as a polyline; otherwise, false.
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
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum algebraic degree of any span
            or a good estimate if curve spans are not algebraic.

Get: Degree(self: Curve) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the dimension of the object.
            The dimension is typically three. For parameter space trimming
            curves the dimension is two. In rare cases the dimension can
            be one or greater than three.

Get: Dimension(self: Curve) -> int

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the domain of the curve.

Get: Domain(self: Curve) -> Interval

Set: Domain(self: Curve) = value
"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this curve is a closed curve.

Get: IsClosed(self: Curve) -> bool

"""

    IsPeriodic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this curve is considered to be Periodic.

Get: IsPeriodic(self: Curve) -> bool

"""

    PointAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Evaluates point at the end of the curve.

Get: PointAtEnd(self: Curve) -> Point3d

"""

    PointAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Evaluates point at the start of the curve.

Get: PointAtStart(self: Curve) -> Point3d

"""

    SpanCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of non-empty smooth (c-infinity) spans in the curve.

Get: SpanCount(self: Curve) -> int

"""

    TangentAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Evaluate unit tangent vector at the end of the curve.

Get: TangentAtEnd(self: Curve) -> Vector3d

"""

    TangentAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Evaluates the unit tangent vector at the start of the curve.

Get: TangentAtStart(self: Curve) -> Vector3d

"""



class ArcCurve(Curve, IDisposable, ISerializable):
    """
    Represent arcs and circles.
                ArcCurve.IsCircle returns true if the curve is a complete circle.
    
    ArcCurve()
    ArcCurve(other: ArcCurve)
    ArcCurve(arc: Arc)
    ArcCurve(arc: Arc, t0: float, t1: float)
    ArcCurve(circle: Circle)
    ArcCurve(circle: Circle, t0: float, t1: float)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: ArcCurve)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, arc: Arc, t0: float, t1: float)
        __new__(cls: type, circle: Circle)
        __new__(cls: type, circle: Circle, t0: float, t1: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the angles of this arc in degrees.

Get: AngleDegrees(self: ArcCurve) -> float

"""

    AngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the angles of this arc in radians.

Get: AngleRadians(self: ArcCurve) -> float

"""

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the arc that is contained within this ArcCurve.

Get: Arc(self: ArcCurve) -> Arc

"""

    IsCompleteCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this curve can be represented by a complete circle.

Get: IsCompleteCircle(self: ArcCurve) -> bool

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the radius of this ArcCurve.

Get: Radius(self: ArcCurve) -> float

"""



class AreaMassProperties(object, IDisposable):
    """
    Contains static initialization methods and allows access to the computed
                metrics of area, area centroid and area moments in closed
                planar curves, in meshes, in surfaces, in hatches and in boundary representations.
    """
    @staticmethod
    def Compute(*__args):
        """
        Compute(brep: Brep) -> AreaMassProperties
        
            Computes an AreaMassProperties for a brep.
        
            brep: Brep to measure.
            Returns: The AreaMassProperties for the given Brep or null on failure.
        Compute(surface: Surface) -> AreaMassProperties
        
            Computes an AreaMassProperties for a surface.
        
            surface: Surface to measure.
            Returns: The AreaMassProperties for the given Surface or null on failure.
        Compute(geometry: IEnumerable[GeometryBase]) -> AreaMassProperties
        Compute(mesh: Mesh) -> AreaMassProperties
        
            Computes an AreaMassProperties for a mesh.
        
            mesh: Mesh to measure.
            Returns: The AreaMassProperties for the given Mesh or null on failure.
        Compute(closedPlanarCurve: Curve) -> AreaMassProperties
        
            Computes an AreaMassProperties for a closed planar curve.
        
            closedPlanarCurve: Curve to measure.
            Returns: The AreaMassProperties for the given curve or null on failure.
        Compute(closedPlanarCurve: Curve, planarTolerance: float) -> AreaMassProperties
        
            Computes an AreaMassProperties for a closed planar curve.
        
            closedPlanarCurve: Curve to measure.
            planarTolerance: absolute tolerance used to insure the closed curve is planar
            Returns: The AreaMassProperties for the given curve or null on failure.
        Compute(hatch: Hatch) -> AreaMassProperties
        
            Computes an AreaMassProperties for a hatch.
        
            hatch: Hatch to measure.
            Returns: The AreaMassProperties for the given hatch or null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AreaMassProperties)
            Actively reclaims unmanaged resources that this instance uses.
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the area solution.

Get: Area(self: AreaMassProperties) -> float

"""

    AreaError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uncertainty in the area calculation.

Get: AreaError(self: AreaMassProperties) -> float

"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the area centroid in the world coordinate system.

Get: Centroid(self: AreaMassProperties) -> Point3d

"""

    CentroidCoordinatesMomentsOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moments of inertia with respect to centroid coordinate system.
            X = integral of ((y-y0)^2 + (z-z0)^2) dm
            Y = integral of ((z-z0)^2 + (x-x0)^2) dm
            Z = integral of ((z-z0)^2 + (y-y0)^2) dm
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesMomentsOfInertia(self: AreaMassProperties) -> Vector3d

"""

    CentroidCoordinatesMomentsOfInertiaError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in centroid coordinates moments of inertia calculation.

Get: CentroidCoordinatesMomentsOfInertiaError(self: AreaMassProperties) -> Vector3d

"""

    CentroidCoordinatesRadiiOfGyration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radii of gyration with respect to centroid coordinate system.
            X = sqrt(integral of ((y-y0)^2 + (z-z0)^2) dm/M)
            Y = sqrt(integral of ((z-z0)^2 + (x-x0)^2) dm/M)
            Z = sqrt(integral of ((z-z0)^2 + (y-y0)^2) dm/M)
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesRadiiOfGyration(self: AreaMassProperties) -> Vector3d

"""

    CentroidCoordinatesSecondMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Second moments with respect to centroid coordinate system.
            X = integral of (x-x0)^2 dm
            Y = integral of (y-y0)^2 dm
            Z = integral of (z-z0)^2 dm
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesSecondMoments(self: AreaMassProperties) -> Vector3d

"""

    CentroidCoordinatesSecondMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in centroid coordinates second moments calculation.

Get: CentroidCoordinatesSecondMomentsError(self: AreaMassProperties) -> Vector3d

"""

    CentroidError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uncertainty in the centroid calculation.

Get: CentroidError(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesFirstMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate first moments if they were able to be calculated.
            X is integral of "x dm" over the area
            Y is integral of "y dm" over the area
            Z is integral of "z dm" over the area.

Get: WorldCoordinatesFirstMoments(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesFirstMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates first moments calculation.

Get: WorldCoordinatesFirstMomentsError(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesMomentsOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moments of inertia about the world coordinate axes.
            X = integral of (y^2 + z^2) dm
            Y = integral of (z^2 + x^2) dm
            Z = integral of (z^2 + y^2) dm.

Get: WorldCoordinatesMomentsOfInertia(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesMomentsOfInertiaError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates moments of inertia calculation.

Get: WorldCoordinatesMomentsOfInertiaError(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesProductMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate product moments if they were able to be calculated.
            X is integral of "xy dm" over the area
            Y is integral of "yz dm" over the area
            Z is integral of "zx dm" over the area.

Get: WorldCoordinatesProductMoments(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesProductMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates second moments calculation.

Get: WorldCoordinatesProductMomentsError(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesRadiiOfGyration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radii of gyration with respect to world coordinate system.
            X = sqrt(integral of (y^2 + z^2) dm/M)
            Y = sqrt(integral of (z^2 + x^2) dm/M)
            Z = sqrt(integral of (z^2 + y^2) dm/M)

Get: WorldCoordinatesRadiiOfGyration(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesSecondMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate first moments if they were able to be calculated.
            X is integral of "xx dm" over the area
            Y is integral of "yy dm" over the area
            Z is integral of "zz dm" over the area.

Get: WorldCoordinatesSecondMoments(self: AreaMassProperties) -> Vector3d

"""

    WorldCoordinatesSecondMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates second moments calculation.

Get: WorldCoordinatesSecondMomentsError(self: AreaMassProperties) -> Vector3d

"""



class BezierCurve(object, IDisposable):
    """
    Represents a Bezier curve.
                Note: as an exception, the bezier curve is not derived from Rhino.Geometry.Curve.
    
    BezierCurve(controlPoints: IEnumerable[Point2d])
    BezierCurve(controlPoints: IEnumerable[Point3d])
    BezierCurve(controlPoints: IEnumerable[Point4d])
    """
    def ChangeDimension(self, desiredDimension):
        """
        ChangeDimension(self: BezierCurve, desiredDimension: int) -> bool
        
            Change dimension of bezier.
            Returns: true if successful.  false if desired_dimension < 1
        """
        pass

    @staticmethod
    def CreateCubicBeziers(sourceCurve, distanceTolerance, kinkTolerance):
        """
        CreateCubicBeziers(sourceCurve: Curve, distanceTolerance: float, kinkTolerance: float) -> Array[BezierCurve]
        
            Constructs an array of cubic, non-rational beziers that fit a curve to a tolerance.
        
            sourceCurve: A curve to approximate.
            distanceTolerance: The max fitting error. Use RhinoMath.SqrtEpsilon as a minimum.
            kinkTolerance: If the input curve has a g1-discontinuity with angle radian measure
                    greater than 
             kinkTolerance at some point P, the list of beziers will
                    also have a kink at P.
        
            Returns: A new array of bezier curves. The array can be empty and might contain null items.
        """
        pass

    @staticmethod
    def CreateLoftedBezier(points):
        """
        CreateLoftedBezier(points: IEnumerable[Point2d]) -> BezierCurve
        CreateLoftedBezier(points: IEnumerable[Point3d]) -> BezierCurve
        """
        pass

    def CurvatureAt(self, t):
        """
        CurvatureAt(self: BezierCurve, t: float) -> Vector3d
        
            Evaluate the curvature vector at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Curvature vector of the curve at the parameter t.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BezierCurve)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def GetBoundingBox(self, accurate):
        """
        GetBoundingBox(self: BezierCurve, accurate: bool) -> BoundingBox
        
            Boundingbox solver. Gets the world axis aligned boundingbox for the curve.
        
            accurate: If true, a physically accurate boundingbox will be computed. 
                    If not, a boundingbox 
             estimate will be computed. For some geometry types there is no 
                    difference between 
             the estimate and the accurate boundingbox. Estimated boundingboxes 
                    can be computed 
             much (much) faster than accurate (or "tight") bounding boxes. 
                    Estimated bounding 
             boxes are always similar to or larger than accurate bounding boxes.
        
            Returns: The boundingbox of the geometry in world coordinates or BoundingBox.Empty 
                    if not 
             bounding box could be found.
        """
        pass

    def GetControlVertex2d(self, index):
        """
        GetControlVertex2d(self: BezierCurve, index: int) -> Point2d
        
            Get location of a control vertex.
        
            index: Control vertex index (0 <= index < ControlVertexCount)
            Returns: If the bezier is rational, the euclidean location is returned.
        """
        pass

    def GetControlVertex3d(self, index):
        """
        GetControlVertex3d(self: BezierCurve, index: int) -> Point3d
        
            Get location of a control vertex.
        
            index: Control vertex index (0 <= index < ControlVertexCount)
            Returns: If the bezier is rational, the euclidean location is returned.
        """
        pass

    def GetControlVertex4d(self, index):
        """
        GetControlVertex4d(self: BezierCurve, index: int) -> Point4d
        
            Get location of a control vertex.
        
            index: Control vertex index (0 <= index < ControlVertexCount)
            Returns: Homogenous value of control vertex. If the bezier is not
                    rational, the weight is 1.
        """
        pass

    def IncreaseDegree(self, desiredDegree):
        """
        IncreaseDegree(self: BezierCurve, desiredDegree: int) -> bool
        
            Increase degree of bezier
            Returns: true if successful.  false if desiredDegree < current degree.
        """
        pass

    def MakeNonRational(self):
        """
        MakeNonRational(self: BezierCurve) -> bool
        
            Make bezier non-rational
            Returns: treu if successful
        """
        pass

    def MakeRational(self):
        """
        MakeRational(self: BezierCurve) -> bool
        
            Make bezier rational
            Returns: true if successful
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: BezierCurve, t: float) -> Point3d
        
            Evaluates point at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Point (location of curve at the parameter t).
        """
        pass

    def TangentAt(self, t):
        """
        TangentAt(self: BezierCurve, t: float) -> Vector3d
        
            Evaluates the unit tangent vector at a curve parameter.
        
            t: Evaluation parameter.
            Returns: Unit tangent vector of the curve at the parameter t.
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: BezierCurve) -> NurbsCurve
        
            Constructs a NURBS curve representation of this curve.
            Returns: NURBS representation of the curve on success, null on failure.
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
    def __new__(self, controlPoints):
        """
        __new__(cls: type, controlPoints: IEnumerable[Point2d])
        __new__(cls: type, controlPoints: IEnumerable[Point3d])
        __new__(cls: type, controlPoints: IEnumerable[Point4d])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ControlVertexCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of control vertices in this curve

Get: ControlVertexCount(self: BezierCurve) -> int

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the curve is rational. 
            Rational curves have control-points with custom weights.

Get: IsRational(self: BezierCurve) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests an object to see if it is valid.

Get: IsValid(self: BezierCurve) -> bool

"""



class BlendContinuity(Enum, IComparable, IFormattable, IConvertible):
    """
    Used in curve and surface blending functions
    
    enum BlendContinuity, values: Curvature (2), Position (0), Tangency (1)
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

    Curvature = None
    Position = None
    Tangency = None
    value__ = None


class BoundingBox(object):
    """
    Represents the value of two points in a bounding box 
                defined by the two extreme corner points.
                This box is therefore aligned to the world X, Y and Z axes.
    
    BoundingBox(min: Point3d, max: Point3d)
    BoundingBox(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float)
    BoundingBox(points: IEnumerable[Point3d])
    """
    def ClosestPoint(self, point, includeInterior=None):
        """
        ClosestPoint(self: BoundingBox, point: Point3d, includeInterior: bool) -> Point3d
        
            Finds the closest point on or in the boundingbox.
        
            point: Sample point.
            includeInterior: If false, the point is projected onto the boundary faces only, 
                    otherwise the 
             interior of the box is also taken into consideration.
        
            Returns: The point on or in the box that is closest to the sample point.
        ClosestPoint(self: BoundingBox, point: Point3d) -> Point3d
        
            Finds the closest point on or in the boundingbox.
        
            point: Sample point.
            Returns: The point on or in the box that is closest to the sample point.
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: BoundingBox, box: BoundingBox) -> bool
        
            Determines whether this boundingbox contains another boundingbox.
                    This is the same 
             as calling Contains(box,false).
        
        
            box: Box to test.
            Returns: true if the box is on the inside of this boundingbox, or is coincident with the surface of it.
        Contains(self: BoundingBox, box: BoundingBox, strict: bool) -> bool
        
            Determines whether this boundingbox contains another boundingbox.
                    The user can 
             choose how to treat boundingboxes with coincidents surfaces.
        
        
            box: Box to test.
            strict: If true, the box needs to be fully on the inside of the boundingbox. 
                    I.e. 
             coincident boxes will be considered 'outside'.
        
            Returns: true if the box is (strictly) on the inside of this BoundingBox.
        Contains(self: BoundingBox, point: Point3d) -> bool
        
            Tests a point for boundingbox inclusion. This is the same as calling Contains(point, false)
        
            point: Point to test.
            Returns: true if the point is on the inside of or coincident with this boundingbox; otherwise false.
        Contains(self: BoundingBox, point: Point3d, strict: bool) -> bool
        
            Tests a point for BoundingBox inclusion.
        
            point: Point to test.
            strict: If true, the point needs to be fully on the inside of the BoundingBox. 
                    I.e. 
             coincident points will be considered 'outside'.
        
            Returns: If 'strict' is affirmative, true if the point is inside this boundingbox; false if it is on the 
             surface or outside.If 'strict' is negative, true if the point is on the surface or on the inside 
             of the boundingbox; otherwise false.
        """
        pass

    def Corner(self, minX, minY, minZ):
        """
        Corner(self: BoundingBox, minX: bool, minY: bool, minZ: bool) -> Point3d
        
            Gets one of the eight corners of the box.
        
            minX: true for the minimum on the X axis; false for the maximum.
            minY: true for the minimum on the Y axis; false for the maximum.
            minZ: true for the minimum on the Z axis; false for the maximum.
            Returns: The requested point.
        """
        pass

    def FurthestPoint(self, point):
        """
        FurthestPoint(self: BoundingBox, point: Point3d) -> Point3d
        
            Finds the furthest point on the Box.
        
            point: Sample point.
            Returns: The point on the box that is furthest from the sample point.
        """
        pass

    def GetCorners(self):
        """
        GetCorners(self: BoundingBox) -> Array[Point3d]
        
            Gets an array filled with the 8 corner points of this box.
                     See remarks for the 
             return order.
        
            Returns: An array of 8 corners.
        """
        pass

    def GetEdges(self):
        """
        GetEdges(self: BoundingBox) -> Array[Line]
        
            Gets an array of the 12 edges of this box.
            Returns: If the boundingbox IsValid, the 12 edges; otherwise, null.
        """
        pass

    def Inflate(self, *__args):
        """
        Inflate(self: BoundingBox, xAmount: float, yAmount: float, zAmount: float)
            Inflate the box with custom amounts in all directions. 
                    Inflating with negative 
             amounts may result in decreasing boxes. 
                    InValid boxes can not be inflated.
        
        
            xAmount: Amount (in model units) to inflate this box in the x direction.
            yAmount: Amount (in model units) to inflate this box in the y direction.
            zAmount: Amount (in model units) to inflate this box in the z direction.
        Inflate(self: BoundingBox, amount: float)
            Inflates the box with equal amounts in all directions. 
                    Inflating with negative 
             amounts may result in decreasing boxes. 
                    Invalid boxes can not be inflated.
        
        
            amount: Amount (in model units) to inflate this box in all directions.
        """
        pass

    @staticmethod
    def Intersection(a, b):
        """
        Intersection(a: BoundingBox, b: BoundingBox) -> BoundingBox
        
            Computes the intersection of two bounding boxes.
        
            a: A first bounding box.
            b: A second bounding box.
            Returns: The intersection bounding box.
        """
        pass

    def IsDegenerate(self, tolerance):
        """
        IsDegenerate(self: BoundingBox, tolerance: float) -> int
        
            Determines whether a bounding box is degenerate (flat) in one or more directions.
        
            tolerance: Distances <= tolerance will be considered to be zero.  If tolerance
                    is negative 
             (default), then a scale invarient tolerance is used.
        
            Returns: 0 = box is not degenerate
                    1 = box is a rectangle (degenerate in one direction).
           
                      2 = box is a line (degenerate in two directions).
                    3 = box is a point 
             (degenerate in three directions)
                    4 = box is not valid.
        """
        pass

    def MakeValid(self):
        """
        MakeValid(self: BoundingBox) -> bool
        
            Ensures that the box is defined in an increasing fashion along X, Y and Z axes.
                    If 
             the Min or Max points are unset, this function will not change the box.
        
            Returns: true if the box was made valid, false if the box could not be made valid.
        """
        pass

    def PointAt(self, tx, ty, tz):
        """
        PointAt(self: BoundingBox, tx: float, ty: float, tz: float) -> Point3d
        
            Evaluates the boundingbox with normalized parameters.
                    The box has idealized side 
             length of 1x1x1.
        
        
            tx: Normalized (between 0 and 1 is inside the box) parameter along the X direction.
            ty: Normalized (between 0 and 1 is inside the box) parameter along the Y direction.
            tz: Normalized (between 0 and 1 is inside the box) parameter along the Z direction.
            Returns: The point at the {tx, ty, tz} parameters.
        """
        pass

    def ToBrep(self):
        """
        ToBrep(self: BoundingBox) -> Brep
        
            Constructs a Rhino.Geometry.Brep representation of this boundingbox.
            Returns: If this operation is sucessfull, a Brep representation of this box; otherwise null.
        """
        pass

    def ToString(self):
        """
        ToString(self: BoundingBox) -> str
        
            Constructs the string representation of this aligned boundingbox.
            Returns: Text.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: BoundingBox, xform: Transform) -> bool
        
            Updates this boundingbox to be the smallest axis aligned
                    boundingbox that contains 
             the transformed result of its 8 original corner
                    points.
        
        
            xform: A transform.
            Returns: true if this operation is sucessfull; otherwise false.
        """
        pass

    def Union(self, *__args):
        """
        Union(a: BoundingBox, b: BoundingBox) -> BoundingBox
        
            Returns a new BoundingBox that represents the union of boxes a and b.
        
            a: First box to include in union.
            b: Second box to include in union.
            Returns: The BoundingBox that contains both a and b.
        Union(box: BoundingBox, point: Point3d) -> BoundingBox
        
            Returns a new BoundingBox that represents the union of a bounding box and a point.
        
            box: Box to include in the union.
            point: Point to include in the union.
            Returns: The BoundingBox that contains both the box and the point.
        Union(self: BoundingBox, other: BoundingBox)
            Updates this BoundingBox to represent the union of itself and another box.
        
            other: Box to include in this union.
        Union(self: BoundingBox, point: Point3d)
            Updates this BoundingBox to represent the union of itself and a point.
        
            point: Point to include in the union.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[BoundingBox]() -> BoundingBox
        
        __new__(cls: type, min: Point3d, max: Point3d)
        __new__(cls: type, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float)
        __new__(cls: type, points: IEnumerable[Point3d])
        """
        pass

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point in the center of the boundingbox.

Get: Center(self: BoundingBox) -> Point3d

"""

    Diagonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the diagonal vector of this BoundingBox. 
            The diagonal connects the Min and Max points.

Get: Diagonal(self: BoundingBox) -> Vector3d

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not this boundingbox is valid. 
            Empty boxes are not valid, and neither are boxes with unset points.

Get: IsValid(self: BoundingBox) -> bool

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point in the maximal corner.

Get: Max(self: BoundingBox) -> Point3d

Set: Max(self: BoundingBox) = value
"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point in the minimal corner.

Get: Min(self: BoundingBox) -> Point3d

Set: Min(self: BoundingBox) = value
"""


    Empty = None
    Unset = None


class Box(object, IEpsilonComparable[Box]):
    """
    Represents the value of a plane and three intervals in
                an orthogonal, oriented box that is not necessarily parallel to the world Y, X, Z axes.
    
    Box(bbox: BoundingBox)
    Box(basePlane: Plane, xSize: Interval, ySize: Interval, zSize: Interval)
    Box(basePlane: Plane, points: IEnumerable[Point3d])
    Box(basePlane: Plane, geometry: GeometryBase)
    Box(basePlane: Plane, boundingbox: BoundingBox)
    """
    def ClosestPoint(self, point):
        """
        ClosestPoint(self: Box, point: Point3d) -> Point3d
        
            Finds the closest point on or in the Box. The box should be Valid for this to work.
        
            point: Sample point.
            Returns: The point on or in the box that is closest to the sample point.
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Box, box: BoundingBox, strict: bool) -> bool
        
            Test a boundingbox for Box inclusion.
        
            box: Box to test.
            strict: If true, the boundingbox needs to be fully on the inside of this Box. 
                    I.e. 
             coincident boxes will be considered 'outside'.
        
            Returns: true if the box is (strictly) on the inside of this Box.
        Contains(self: Box, box: Box) -> bool
        
            Test a box for Box inclusion. This is the same as calling Contains(box,false)
        
            box: Box to test.
            Returns: true if the box is on the inside of or coincident with this Box.
        Contains(self: Box, box: Box, strict: bool) -> bool
        
            Test a box for Box inclusion.
        
            box: Box to test.
            strict: If true, the box needs to be fully on the inside of this Box. 
                    I.e. coincident 
             boxes will be considered 'outside'.
        
            Returns: true if the box is (strictly) on the inside of this Box.
        Contains(self: Box, point: Point3d) -> bool
        
            Determines whether a point is included in this box. This is the same as calling 
             Contains(point,false)
        
        
            point: Point to test.
            Returns: true if the point is on the inside of or coincident with this Box.
        Contains(self: Box, point: Point3d, strict: bool) -> bool
        
            Determines whether a point is included in this box.
        
            point: Point to test.
            strict: If true, the point needs to be fully on the inside of the Box. 
                    I.e. coincident 
             points will be considered 'outside'.
        
            Returns: true if the point is (strictly) on the inside of this Box.
        Contains(self: Box, box: BoundingBox) -> bool
        
            Test a boundingbox for Box inclusion. This is the same as calling Contains(box,false)
        
            box: Box to test.
            Returns: true if the box is on the inside of or coincident with this Box.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Box, other: Box, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def FurthestPoint(self, point):
        """
        FurthestPoint(self: Box, point: Point3d) -> Point3d
        
            Finds the furthest point on the Box. The Box should be Valid for this to work properly.
        
            point: Sample point.
            Returns: The point on the box that is furthest from the sample point.
        """
        pass

    def GetCorners(self):
        """
        GetCorners(self: Box) -> Array[Point3d]
        
            Gets an array of the 8 corner points of this box.
            Returns: An array of 8 corners.
        """
        pass

    def Inflate(self, *__args):
        """
        Inflate(self: Box, xAmount: float, yAmount: float, zAmount: float)
            Inflates the box by a given offset in each direction.
                    Inflating with negative 
             amounts may result in decreasing boxes.
                    InValid boxes cannot be inflated.
        
        
            xAmount: Amount (in model units) to inflate this box in the x direction.
            yAmount: Amount (in model units) to inflate this box in the y direction.
            zAmount: Amount (in model units) to inflate this box in the z direction.
        Inflate(self: Box, amount: float)
            Inflates the box by a given offset in each direction.
                    Inflating with negative 
             amounts may result in decreasing boxes. 
                    InValid boxes cannot be inflated.
        
        
            amount: Amount (in model units) to inflate this box in all directions.
        """
        pass

    def MakeValid(self):
        """
        MakeValid(self: Box) -> bool
        
            Attempts to make the Box valid. This is not always possible.
            Returns: true if the box was made valid, or if it was valid to begin with. 
                    false if the box 
             remains in a differently abled state.
        """
        pass

    def PointAt(self, x, y, z):
        """
        PointAt(self: Box, x: float, y: float, z: float) -> Point3d
        
            Evaluates the box volume at the given unitized parameters.
                    The box has idealized 
             side length of 1x1x1.
        
        
            x: Unitized parameter (between 0 and 1 is inside the box) along box X direction.
            y: Unitized parameter (between 0 and 1 is inside the box) along box Y direction.
            z: Unitized parameter (between 0 and 1 is inside the box) along box Z direction.
            Returns: The point at (x,y,z).
        """
        pass

    def RepositionBasePlane(self, origin):
        """
        RepositionBasePlane(self: Box, origin: Point3d)
            Repositions the origin of the Base plane for this box without affecting 
                    the 
             physical dimensions.
        
        
            origin: The new base plane origin.
        """
        pass

    def ToBrep(self):
        """
        ToBrep(self: Box) -> Brep
        
            Constructs a brep representation of this box.
            Returns: A Brep representation of this box or null.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Box, xform: Transform) -> bool
        
            Transforms this Box using a Transformation matrix. If the Transform does not preserve 
                 
                Similarity, the dimensions of the resulting box cannot be trusted.
        
        
            xform: Transformation matrix to apply to this Box.
            Returns: true if the Box was successfully transformed, false if otherwise.
        """
        pass

    def Union(self, point):
        """
        Union(self: Box, point: Point3d)
            Constructs a union between this Box and the given point. 
                    This grows the box in 
             directions so it contains the point.
        
        
            point: Point to include.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Box]() -> Box
        
        __new__(cls: type, bbox: BoundingBox)
        __new__(cls: type, basePlane: Plane, xSize: Interval, ySize: Interval, zSize: Interval)
        __new__(cls: type, basePlane: Plane, points: IEnumerable[Point3d])
        __new__(cls: type, basePlane: Plane, geometry: GeometryBase)
        __new__(cls: type, basePlane: Plane, boundingbox: BoundingBox)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total surface area of this box.

Get: Area(self: Box) -> float

"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the world axis aligned Bounding box for this oriented box.

Get: BoundingBox(self: Box) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point that is in the center of the box.

Get: Center(self: Box) -> Point3d

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the validity of this Box. Boxes are invalid when the base plane or any of 
            the dimension intervals are invalid or decreasing.

Get: IsValid(self: Box) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the orientation plane for this Box.

Get: Plane(self: Box) -> Plane

Set: Plane(self: Box) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total volume of this box.

Get: Volume(self: Box) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Interval that describes the dimension of the 
            Box along the orientation plane X-Axis. Otherwise known as the Width of the Box.

Get: X(self: Box) -> Interval

Set: X(self: Box) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Interval that describes the dimension of the 
            Box along the orientation plane Y-Axis. Otherwise known as the Depth of the Box.

Get: Y(self: Box) -> Interval

Set: Y(self: Box) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Interval that describes the dimension of the 
            Box along the orientation plane Z-Axis. Otherwise known as the Height of the Box.

Get: Z(self: Box) -> Interval

Set: Z(self: Box) = value
"""


    Empty = None
    Unset = None


class Brep(GeometryBase, IDisposable, ISerializable):
    """
    Boundary Representation. A surface or polysurface along with trim curve information.
    
    Brep()
    """
    def AddEdgeCurve(self, curve):
        """
        AddEdgeCurve(self: Brep, curve: Curve) -> int
        
            Add a 3d curve used by the brep edges
            Returns: Index used to reference this geometry in the edge curve list
        """
        pass

    def AddSurface(self, surface):
        """
        AddSurface(self: Brep, surface: Surface) -> int
        
            Adds a 3D surface used by BrepFace.
        
            surface: A copy of the surface is added to this brep.
            Returns: Index that should be used to reference the geometry.
                    -1 is returned if the input is 
             not acceptable.
        """
        pass

    def AddTrimCurve(self, curve):
        """
        AddTrimCurve(self: Brep, curve: Curve) -> int
        
            Add a 2d curve used by the brep trims
            Returns: Index used to reference this geometry in the trimming curve list
        """
        pass

    def Append(self, other):
        """
        Append(self: Brep, other: Brep)
            Appends a copy of another brep to this and updates indices of appended
                    brep parts.  
             Duplicates are not removed
        """
        pass

    def CapPlanarHoles(self, tolerance):
        """
        CapPlanarHoles(self: Brep, tolerance: float) -> Brep
        
            Returns a new Brep that is equivalent to this Brep with all planar holes capped.
        
            tolerance: Tolerance to use for capping.
            Returns: New brep on success. null on error.
        """
        pass

    def ClosestPoint(self, testPoint, closestPoint=None, ci=None, s=None, t=None, maximumDistance=None, normal=None):
        """
        ClosestPoint(self: Brep, testPoint: Point3d, maximumDistance: float) -> (bool, Point3d, ComponentIndex, float, float, Vector3d)
        
            Finds a point on a brep that is closest to testPoint.
        
            testPoint: base point to project to surface.
            maximumDistance: If maximumDistance > 0, then only points whose distance
                    is <= maximumDistance will 
             be returned. Using a positive
                    value of maximumDistance can substantially speed up 
             the search.
        
            Returns: true if the operation succeeded; otherwise, false.
        ClosestPoint(self: Brep, testPoint: Point3d) -> Point3d
        
            Finds a point on the brep that is closest to testPoint.
        
            testPoint: Base point to project to brep.
            Returns: The point on the Brep closest to testPoint or Point3d.Unset if the operation failed.
        """
        pass

    def Compact(self):
        """
        Compact(self: Brep)
            Deletes any unreferenced objects from arrays, reindexes as needed, and
                    shrinks 
             arrays to minimum required size. Uses CUllUnused* members to
                    delete any 
             unreferenced objects from arrays.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def CopyTrimCurves(trimSource, surfaceSource, tolerance):
        """
        CopyTrimCurves(trimSource: BrepFace, surfaceSource: Surface, tolerance: float) -> Brep
        
            Copy all trims from a Brep face onto a surface.
        
            trimSource: Brep face which defines the trimming curves.
            surfaceSource: The surface to trim.
            tolerance: Tolerance to use for rebuilding 3D trim curves.
            Returns: A brep with the shape of surfaceSource and the trims of trimSource or null on failure.
        """
        pass

    @staticmethod
    def CreateBooleanDifference(*__args):
        """
        CreateBooleanDifference(firstBrep: Brep, secondBrep: Brep, tolerance: float) -> Array[Brep]
        
            Compute the Solid Difference of two Breps.
        
            firstBrep: First Brep for boolean difference.
            secondBrep: Second Brep for boolean difference.
            tolerance: Tolerance to use for difference operation.
            Returns: An array of Brep results or null on failure.
        CreateBooleanDifference(firstSet: IEnumerable[Brep], secondSet: IEnumerable[Brep], tolerance: float) -> Array[Brep]
        """
        pass

    @staticmethod
    def CreateBooleanIntersection(*__args):
        """
        CreateBooleanIntersection(firstBrep: Brep, secondBrep: Brep, tolerance: float) -> Array[Brep]
        
            Compute the Solid Intersection of two Breps.
        
            firstBrep: First Brep for boolean intersection.
            secondBrep: Second Brep for boolean intersection.
            tolerance: Tolerance to use for intersection operation.
            Returns: An array of Brep results or null on failure.
        CreateBooleanIntersection(firstSet: IEnumerable[Brep], secondSet: IEnumerable[Brep], tolerance: float) -> Array[Brep]
        """
        pass

    @staticmethod
    def CreateBooleanUnion(breps, tolerance):
        """ CreateBooleanUnion(breps: IEnumerable[Brep], tolerance: float) -> Array[Brep] """
        pass

    @staticmethod
    def CreateContourCurves(brepToContour, *__args):
        """
        CreateContourCurves(brepToContour: Brep, sectionPlane: Plane) -> Array[Curve]
        
            Constructs the contour curves for a brep, using a slicing plane.
        
            brepToContour: A brep or polysurface.
            sectionPlane: A plane.
            Returns: An array with intersected curves. This array can be empty.
        CreateContourCurves(brepToContour: Brep, contourStart: Point3d, contourEnd: Point3d, interval: float) -> Array[Curve]
        
            Constructs the contour curves for a brep at a specified interval.
        
            brepToContour: A brep or polysurface.
            contourStart: A point to start.
            contourEnd: A point to use as the end.
            interval: The interaxial offset in world units.
            Returns: An array with intersected curves. This array can be empty.
        """
        pass

    @staticmethod
    def CreateEdgeSurface(curves):
        """ CreateEdgeSurface(curves: IEnumerable[Curve]) -> Brep """
        pass

    @staticmethod
    def CreateFromBox(*__args):
        """
        CreateFromBox(corners: IEnumerable[Point3d]) -> Brep
        CreateFromBox(box: Box) -> Brep
        
            Constructs new brep that matches an aligned box.
        
            box: Box to match.
            Returns: A Brep with 6 faces that is similar to the Box.
        CreateFromBox(box: BoundingBox) -> Brep
        
            Constructs new brep that matches a bounding box.
        
            box: A box to use for creation.
            Returns: A new brep; or null on failure.
        """
        pass

    @staticmethod
    def CreateFromCone(cone, capBottom):
        """
        CreateFromCone(cone: Cone, capBottom: bool) -> Brep
        
            Constructs a Brep representation of the cone with a single
                    face for the cone, an 
             edge along the cone seam, 
                    and vertices at the base and apex ends of this seam 
             edge.
                    The optional cap is a single face with one circular edge 
                    
             starting and ending at the base vertex.
        
        
            cone: A cone value.
            capBottom: if true the base of the cone should be capped.
            Returns: A new brep, on null on error.
        """
        pass

    @staticmethod
    def CreateFromCornerPoints(corner1, corner2, corner3, *__args):
        """
        CreateFromCornerPoints(corner1: Point3d, corner2: Point3d, corner3: Point3d, corner4: Point3d, tolerance: float) -> Brep
        
            make a Brep with one face.
        
            corner1: A first corner.
            corner2: A second corner.
            corner3: A third corner.
            corner4: A fourth corner.
            tolerance: Minimum edge length allowed before collapsing the side into a singularity.
            Returns: A boundary representation, or null on error.
        CreateFromCornerPoints(corner1: Point3d, corner2: Point3d, corner3: Point3d, tolerance: float) -> Brep
        
            Makes a brep with one face.
        
            corner1: A first corner.
            corner2: A second corner.
            corner3: A third corner.
            tolerance: Minimum edge length without collapsing to a singularity.
            Returns: A boundary representation, or null on error.
        """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder, capBottom, capTop):
        """
        CreateFromCylinder(cylinder: Cylinder, capBottom: bool, capTop: bool) -> Brep
        
            Constructs a Brep definition of a cylinder.
        
            cylinder: cylinder.IsFinite() must be true.
            capBottom: if true end at cylinder.m_height[0] should be capped.
            capTop: if true end at cylinder.m_height[1] should be capped.
            Returns: A Brep representation of the cylinder with a single face for the cylinder,
                    an edge 
             along the cylinder seam, and vertices at the bottom and top ends of this
                    seam edge. 
             The optional bottom/top caps are single faces with one circular edge
                    starting and 
             ending at the bottom/top vertex.
        """
        pass

    @staticmethod
    def CreateFromLoft(curves, start, end, loftType, closed):
        """ CreateFromLoft(curves: IEnumerable[Curve], start: Point3d, end: Point3d, loftType: LoftType, closed: bool) -> Array[Brep] """
        pass

    @staticmethod
    def CreateFromLoftRebuild(curves, start, end, loftType, closed, rebuildPointCount):
        """ CreateFromLoftRebuild(curves: IEnumerable[Curve], start: Point3d, end: Point3d, loftType: LoftType, closed: bool, rebuildPointCount: int) -> Array[Brep] """
        pass

    @staticmethod
    def CreateFromLoftRefit(curves, start, end, loftType, closed, refitTolerance):
        """ CreateFromLoftRefit(curves: IEnumerable[Curve], start: Point3d, end: Point3d, loftType: LoftType, closed: bool, refitTolerance: float) -> Array[Brep] """
        pass

    @staticmethod
    def CreateFromMesh(mesh, trimmedTriangles):
        """
        CreateFromMesh(mesh: Mesh, trimmedTriangles: bool) -> Brep
        
            Create a brep representation of a mesh
        
            trimmedTriangles: if true, triangles in the mesh will be represented by trimmed planes in
                    the brep. 
             If false, triangles in the mesh will be represented by
                    untrimmed singular bilinear 
             NURBS surfaces in the brep.
        """
        pass

    @staticmethod
    def CreateFromOffsetFace(face, offsetDistance, offsetTolerance, bothSides, createSolid):
        """
        CreateFromOffsetFace(face: BrepFace, offsetDistance: float, offsetTolerance: float, bothSides: bool, createSolid: bool) -> Brep
        
            Offsets a face including trim information to create a new brep.
        
            face: the face to offset.
            offsetDistance: An offset distance.
            offsetTolerance: Use 0.0 to make a loose offset. Otherwise, the document's absolute tolerance is usually 
             sufficient.
        
            bothSides: When true, offset to both sides of the input face.
            createSolid: When true, make a solid object.
            Returns: A new brep if successful. The brep can be disjoint if bothSides is true and createSolid is 
             false,
                    or if createSolid is true and connecting the offsets with side surfaces 
             fails.
                    null if unsuccessful.
        """
        pass

    @staticmethod
    def CreateFromRevSurface(surface, capStart, capEnd):
        """
        CreateFromRevSurface(surface: RevSurface, capStart: bool, capEnd: bool) -> Brep
        
            Constructs a brep form of a surface of revolution.
        
            surface: The surface of revolution.
            capStart: if true, the start of the revolute is not on the axis of revolution,
                    and the 
             surface of revolution is closed, then a circular cap will be
                    added to close of the 
             hole at the start of the revolute.
        
            capEnd: if true, the end of the revolute is not on the axis of revolution,
                    and the surface 
             of revolution is closed, then a circular cap will be
                    added to close of the hole at 
             the end of the revolute.
        
            Returns: A new brep, on null on error.
        """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """
        CreateFromSphere(sphere: Sphere) -> Brep
        
            Constructs a Brep definition of a sphere.
        """
        pass

    @staticmethod
    def CreateFromSurface(surface):
        """
        CreateFromSurface(surface: Surface) -> Brep
        
            Constructs a Brep from a surface. The resulting Brep has an outer boundary made
                    
             from four trims. The trims are ordered so that they run along the south, east,
                    
             north, and then west side of the surface's parameter space.
        
        
            surface: A surface to convert.
            Returns: Resulting brep or null on failure.
        """
        pass

    @staticmethod
    def CreateFromSweep(*__args):
        """
        CreateFromSweep(rail1: Curve, rail2: Curve, shape: Curve, closed: bool, tolerance: float) -> Array[Brep]
        
            General 2 rail sweep. If you are not producing the sweep results that you are after, then
              
                   use the SweepTwoRail class with options to generate the swept geometry
        
        
            rail1: Rail to sweep shapes along
            rail2: Rail to sweep shapes along
            shape: Shape curve
            closed: Only matters if shape is closed
            tolerance: Tolerance for fitting surface and rails
            Returns: Array of Brep sweep results
        CreateFromSweep(rail1: Curve, rail2: Curve, shapes: IEnumerable[Curve], closed: bool, tolerance: float) -> Array[Brep]
        CreateFromSweep(rail: Curve, shape: Curve, closed: bool, tolerance: float) -> Array[Brep]
        
            General 1 rail sweep. If you are not producing the sweep results that you are after, then
              
                   use the SweepOneRail class with options to generate the swept geometry
        
        
            rail: Rail to sweep shapes along
            shape: Shape curve
            closed: Only matters if shape is closed
            tolerance: Tolerance for fitting surface and rails
            Returns: Array of Brep sweep results
        CreateFromSweep(rail: Curve, shapes: IEnumerable[Curve], closed: bool, tolerance: float) -> Array[Brep]
        """
        pass

    @staticmethod
    def CreateFromTaperedExtrude(curveToExtrude, distance, direction, basePoint, draftAngleRadians, cornerType):
        """
        CreateFromTaperedExtrude(curveToExtrude: Curve, distance: float, direction: Vector3d, basePoint: Point3d, draftAngleRadians: float, cornerType: ExtrudeCornerType) -> Array[Brep]
        
            Extrude a curve to a taper making a brep (potentially more than 1)
        
            curveToExtrude: the curve to extrude
            distance: the distance to extrude
            direction: the direction of the extrusion
            basePoint: the basepoint of the extrusion
            draftAngleRadians: angle of the extrusion
            Returns: array of breps on success
        """
        pass

    @staticmethod
    def CreatePatch(geometry, *__args):
        """
        CreatePatch(geometry: IEnumerable[GeometryBase], startingSurface: Surface, uSpans: int, vSpans: int, trim: bool, tangency: bool, pointSpacing: float, flexibility: float, surfacePull: float, fixEdges: Array[bool], tolerance: float) -> Brep
        CreatePatch(geometry: IEnumerable[GeometryBase], uSpans: int, vSpans: int, tolerance: float) -> Brep
        CreatePatch(geometry: IEnumerable[GeometryBase], startingSurface: Surface, tolerance: float) -> Brep
        """
        pass

    @staticmethod
    def CreatePipe(rail, *__args):
        """
        CreatePipe(rail: Curve, railRadiiParameters: IEnumerable[float], radii: IEnumerable[float], localBlending: bool, cap: PipeCapMode, fitRail: bool, absoluteTolerance: float, angleToleranceRadians: float) -> Array[Brep]
        CreatePipe(rail: Curve, radius: float, localBlending: bool, cap: PipeCapMode, fitRail: bool, absoluteTolerance: float, angleToleranceRadians: float) -> Array[Brep]
        
            Creates a single walled pipe
        
            rail: the path curve for the pipe
            radius: radius of the pipe
            localBlending: If True, Local (pipe radius stays constant at the ends and changes more rapidly in the middle) 
             is applied.
                    If False, Global (radius is linearly blended from one end to the other, 
             creating pipes that taper from one radius to the other) is applied
        
            cap: end cap mode
            fitRail: If the curve is a polycurve of lines and arcs, the curve is fit and a single surface is created;
             
                    otherwise the result is a polysurface with joined surfaces created from the 
             polycurve segments.
        
            absoluteTolerance: The sweeping and fitting tolerance. If you are unsure what to use, then use the document's 
             absolute tolerance
        
            angleToleranceRadians: The angle tolerance. If you are unsure what to use, then either use the document's angle 
             tolerance in radians
        
            Returns: Array of created pipes on success
        """
        pass

    @staticmethod
    def CreatePlanarBreps(*__args):
        """
        CreatePlanarBreps(inputLoops: CurveList) -> Array[Brep]
        
            Constructs a set of planar Breps as outlines by the loops.
        
            inputLoops: Curve loops that delineate the planar boundaries.
            Returns: An array of Planar Breps or null on error.
        CreatePlanarBreps(inputLoop: Curve) -> Array[Brep]
        
            Constructs a set of planar breps as outlines by the loops.
        
            inputLoop: A curve that should form the boundaries of the surfaces or polysurfaces.
            Returns: An array of Planar Breps.
        CreatePlanarBreps(inputLoops: IEnumerable[Curve]) -> Array[Brep]
        """
        pass

    @staticmethod
    def CreateShell(brep, facesToRemove, distance, tolerance):
        """ CreateShell(brep: Brep, facesToRemove: IEnumerable[int], distance: float, tolerance: float) -> Array[Brep] """
        pass

    @staticmethod
    def CreateSolid(breps, tolerance):
        """ CreateSolid(breps: IEnumerable[Brep], tolerance: float) -> Array[Brep] """
        pass

    @staticmethod
    def CreateTrimmedSurface(trimSource, surfaceSource):
        """
        CreateTrimmedSurface(trimSource: BrepFace, surfaceSource: Surface) -> Brep
        
            Constructs a Brep using the trimming information of a brep face and a surface. 
                    
             Surface must be roughly the same shape and in the same location as the trimming brep face.
        
        
            trimSource: BrepFace which contains trimmingSource brep.
            surfaceSource: Surface that trims of BrepFace will be applied to.
            Returns: A brep with the shape of surfaceSource and the trims of trimSource or null on failure.
        """
        pass

    def CullUnused2dCurves(self):
        """
        CullUnused2dCurves(self: Brep) -> bool
        
            Culls 3d curves not referenced by an edge.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnused3dCurves(self):
        """
        CullUnused3dCurves(self: Brep) -> bool
        
            Culls 2d curves not referenced by a trim.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedEdges(self):
        """
        CullUnusedEdges(self: Brep) -> bool
        
            Culls edges with m_edge_index == -1.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedFaces(self):
        """
        CullUnusedFaces(self: Brep) -> bool
        
            Culls faces with m_face_index == -1.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedLoops(self):
        """
        CullUnusedLoops(self: Brep) -> bool
        
            Culls loops with m_loop_index == -1.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedSurfaces(self):
        """
        CullUnusedSurfaces(self: Brep) -> bool
        
            Culls surfaces not referenced by a face.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedTrims(self):
        """
        CullUnusedTrims(self: Brep) -> bool
        
            Culls trims with m_trim_index == -1.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def CullUnusedVertices(self):
        """
        CullUnusedVertices(self: Brep) -> bool
        
            Culls vertices with m_vertex_index == -1.
            Returns: true if operation succeeded; false otherwise.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Duplicate(self):
        """
        Duplicate(self: Brep) -> GeometryBase
        
            Copies this brep.
            Returns: A brep.
        """
        pass

    def DuplicateBrep(self):
        """
        DuplicateBrep(self: Brep) -> Brep
        
            Same as Rhino.Geometry.Brep.Duplicate, but already performs a cast to a brep.
                    This 
             cast always succeeds.
        
            Returns: A brep.
        """
        pass

    def DuplicateEdgeCurves(self, nakedOnly=None):
        """
        DuplicateEdgeCurves(self: Brep, nakedOnly: bool) -> Array[Curve]
        
            Duplicate edges of this Brep.
        
            nakedOnly: If true, then only the "naked" edges are duplicated.
                    If false, then all edges are 
             duplicated.
        
            Returns: Array of edge curves on success.
        DuplicateEdgeCurves(self: Brep) -> Array[Curve]
        
            Duplicate all the edges of this Brep.
            Returns: An array of edge curves.
        """
        pass

    def DuplicateNakedEdgeCurves(self, outer, inner):
        """
        DuplicateNakedEdgeCurves(self: Brep, outer: bool, inner: bool) -> Array[Curve]
        
            Duplicate naked edges of this Brep
        """
        pass

    def DuplicateSubBrep(self, faceIndices):
        """ DuplicateSubBrep(self: Brep, faceIndices: IEnumerable[int]) -> Brep """
        pass

    def DuplicateVertices(self):
        """
        DuplicateVertices(self: Brep) -> Array[Point3d]
        
            Duplicate all the corner vertices of this Brep.
            Returns: An array or corner vertices.
        """
        pass

    def Flip(self):
        """
        Flip(self: Brep)
            Reverses entire brep orientation of all faces.
        """
        pass

    def GetArea(self, relativeTolerance=None, absoluteTolerance=None):
        """
        GetArea(self: Brep) -> float
        
            Compute the Area of the Brep. If you want proper Area data with moments 
                    and error 
             information, use the AreaMassProperties class.
        
            Returns: The area of the Brep.
        GetArea(self: Brep, relativeTolerance: float, absoluteTolerance: float) -> float
        
            Compute the Area of the Brep. If you want proper Area data with moments 
                    and error 
             information, use the AreaMassProperties class.
        
        
            relativeTolerance: Relative tolerance to use for area calculation.
            absoluteTolerance: Absolute tolerance to use for area calculation.
            Returns: The area of the Brep.
        """
        pass

    def GetRegions(self):
        """
        GetRegions(self: Brep) -> Array[BrepRegion]
        
            Gets an array containing all regions in this brep.
            Returns: An array of regions in this brep. This array can be empty, but not null.
        """
        pass

    def GetVolume(self, relativeTolerance=None, absoluteTolerance=None):
        """
        GetVolume(self: Brep, relativeTolerance: float, absoluteTolerance: float) -> float
        
            Compute the Volume of the Brep. If you want proper Volume data with moments 
                    and 
             error information, use the VolumeMassProperties class.
        
        
            relativeTolerance: Relative tolerance to use for area calculation.
            absoluteTolerance: Absolute tolerance to use for area calculation.
            Returns: The volume of the Brep.
        GetVolume(self: Brep) -> float
        
            Compute the Volume of the Brep. If you want proper Volume data with moments 
                    and 
             error information, use the VolumeMassProperties class.
        
            Returns: The volume of the Brep.
        """
        pass

    def GetWireframe(self, density):
        """
        GetWireframe(self: Brep, density: int) -> Array[Curve]
        
            Constructs all the Wireframe curves for this Brep.
        
            density: Wireframe density. Valid values range between -1 and 99.
            Returns: An array of Wireframe curves or null on failure.
        """
        pass

    def IsDuplicate(self, other, tolerance):
        """
        IsDuplicate(self: Brep, other: Brep, tolerance: float) -> bool
        
            See if this and other are same brep geometry.
        
            other: other brep.
            tolerance: tolerance to use when comparing control points.
            Returns: true if breps are the same.
        """
        pass

    def IsPointInside(self, point, tolerance, strictlyIn):
        """
        IsPointInside(self: Brep, point: Point3d, tolerance: float, strictlyIn: bool) -> bool
        
            Determines if point is inside Brep.  This question only makes sense when
                    the brep 
             is a closed manifold.  This function does not not check for
                    closed or manifold, so 
             result is not valid in those cases.  Intersects
                    a line through point with brep, 
             finds the intersection point Q closest
                    to point, and looks at face normal at Q.  If 
             the point Q is on an edge
                    or the intersection is not transverse at Q, then another 
             line is used.
        
        
            point: 3d point to test.
            tolerance: 3d distance tolerance used for intersection and determining strict inclusion.
                    A 
             good default is RhinoMath.SqrtEpsilon.
        
            strictlyIn: if true, point is in if inside brep by at least tolerance.
                    if false, point is in if 
             truly in or within tolerance of boundary.
        
            Returns: true if point is in, false if not.
        """
        pass

    def IsValidGeometry(self, log):
        """
        IsValidGeometry(self: Brep) -> (bool, str)
        
            Expert user function that tests the brep to see if its geometry information is valid.
                  
               The value of brep.IsValidTopology() must be true before brep.IsValidGeometry() can be
                
                 safely called.
        
            Returns: A value that indicates whether the geometry is valid.
        """
        pass

    def IsValidTolerancesAndFlags(self, log):
        """
        IsValidTolerancesAndFlags(self: Brep) -> (bool, str)
        
            Expert user function that tests the brep to see if its tolerances and
                    flags are 
             valid.  The values of brep.IsValidTopology() and
                    brep.IsValidGeometry() must be 
             true before brep.IsValidTolerancesAndFlags()
                    can be safely called.
        
            Returns: A value that indicates
        """
        pass

    def IsValidTopology(self, log):
        """
        IsValidTopology(self: Brep) -> (bool, str)
        
            Tests the brep to see if its topology information is valid.
            Returns: true if the topology is valid; false otherwise.
        """
        pass

    def Join(self, otherBrep, tolerance, compact):
        """
        Join(self: Brep, otherBrep: Brep, tolerance: float, compact: bool) -> bool
        
            If any edges of this brep overlap edges of otherBrep, merge a copy of otherBrep into this
              
                   brep joining all edges that overlap within tolerance.
        
        
            otherBrep: Brep to be added to this brep.
            tolerance: 3d distance tolerance for detecting overlapping edges.
            compact: if true, set brep flags and tolerances, remove unused faces and edges.
            Returns: true if any edges were joined.
        """
        pass

    @staticmethod
    def JoinBreps(brepsToJoin, tolerance):
        """ JoinBreps(brepsToJoin: IEnumerable[Brep], tolerance: float) -> Array[Brep] """
        pass

    def JoinNakedEdges(self, tolerance):
        """
        JoinNakedEdges(self: Brep, tolerance: float) -> int
        
            Joins naked edge pairs within the same brep that overlap within tolerance.
        
            tolerance: The tolerance value.
            Returns: number of joins made.
        """
        pass

    @staticmethod
    def MergeBreps(brepsToMerge, tolerance):
        """ MergeBreps(brepsToMerge: IEnumerable[Brep], tolerance: float) -> Brep """
        pass

    def MergeCoplanarFaces(self, tolerance):
        """
        MergeCoplanarFaces(self: Brep, tolerance: float) -> bool
        
            Merges adjacent coplanar faces into single faces.
        
            tolerance: 3d tolerance for determining when edges are adjacent.
            Returns: true if faces were merged.  false if no faces were merged.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def RebuildTrimsForV2(self, face, nurbsSurface):
        """
        RebuildTrimsForV2(self: Brep, face: BrepFace, nurbsSurface: NurbsSurface)
            No support is available for this function.
                    Expert user function used by 
             MakeValidForV2 to convert trim
                    curves from one surface to its NURBS form. After 
             calling this function,
                    you need to change the surface of the face to a 
             NurbsSurface.
        
        
            face: Face whose underlying surface has a parameterization that is different
                    from its 
             NURBS form.
        
            nurbsSurface: NURBS form of the face's underlying surface.
        """
        pass

    def SetTrimIsoFlags(self):
        """
        SetTrimIsoFlags(self: Brep)
            This function can be used to set the BrepTrim::m_iso
                    flag. It is intended to be 
             used when creating a Brep from
                    a definition that does not include compatible 
             parameter space
                    type information.
        """
        pass

    def SetVertices(self):
        """
        SetVertices(self: Brep)
            This function can be used to compute vertex information for a
                    b-rep when everything 
             but the Vertices array is properly filled in.
                    It is intended to be used when 
             creating a Brep from a 
                    definition that does not include explicit vertex 
             information.
        """
        pass

    def Split(self, splitter, intersectionTolerance, toleranceWasRaised=None):
        """
        Split(self: Brep, splitter: Brep, intersectionTolerance: float) -> (Array[Brep], bool)
        
            Splits a Brep into pieces.
        
            splitter: The splitting polysurface.
            intersectionTolerance: The tolerance with which to compute intersections.
            Returns: A new array of breps. This array can be empty.
        Split(self: Brep, splitter: Brep, intersectionTolerance: float) -> Array[Brep]
        
            Splits a Brep into pieces.
        
            splitter: A splitting surface or polysurface.
            intersectionTolerance: The tolerance with which to compute intersections.
            Returns: A new array of breps. This array can be empty.
        """
        pass

    def Standardize(self):
        """
        Standardize(self: Brep)
            Standardizes all trims, edges, and faces in the brep.
                    After standardizing, there 
             may be unused curves and surfaces in the
                    brep.  Call Brep.Compact to remove these 
             unused curves and surfaces.
        """
        pass

    def Trim(self, cutter, intersectionTolerance):
        """
        Trim(self: Brep, cutter: Plane, intersectionTolerance: float) -> Array[Brep]
        
            Trims a Brep with an oriented cutter.  The parts of Brep that lie inside
                    (opposite 
             the normal) of the cutter are retained while the parts to the
                    outside ( in the 
             direction of the normal ) are discarded. A connected
                    component of Brep that does 
             not intersect the cutter is kept if and only
                    if it is contained in the inside of 
             Cutter.  That is the region bounded by
                    cutter opposite from the normal of cutter, 
             or in the case of a Plane cutter
                    the halfspace opposite from the plane normal.
        
        
            cutter: A cutting plane.
            intersectionTolerance: A tolerance value with which to compute intersections.
            Returns: This Brep is not modified, the trim results are returned in an array.
        Trim(self: Brep, cutter: Brep, intersectionTolerance: float) -> Array[Brep]
        
            Trims a brep with an oriented cutter. The parts of the brep that lie inside
                    
             (opposite the normal) of the cutter are retained while the parts to the
                    outside (in 
             the direction of the normal) are discarded.  If the Cutter is
                    closed, then a 
             connected component of the Brep that does not intersect the
                    cutter is kept if and 
             only if it is contained in the inside of cutter.
                    That is the region bounded by 
             cutter opposite from the normal of cutter,
                    If cutter is not closed all these 
             components are kept.
        
        
            cutter: A cutting brep.
            intersectionTolerance: A tolerance value with which to compute intersections.
            Returns: This Brep is not modified, the trim results are returned in an array.
        """
        pass

    @staticmethod
    def TryConvertBrep(geometry):
        """
        TryConvertBrep(geometry: GeometryBase) -> Brep
        
            Attempts to convert a generic Geometry object into a Brep.
        
            geometry: Geometry to convert, not all types of GeometryBase can be represented by BReps.
            Returns: Brep if a brep form could be created or null if this is not possible. If geometry was of type 
             Brep to 
                    begin with, the same object is returned, i.e. it is not duplicated.
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Curves2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Parameter space trimming curves (used by trims)

Get: Curves2D(self: Brep) -> BrepCurveList

"""

    Curves3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pointers to 3d curves (used by edges)

Get: Curves3D(self: Brep) -> BrepCurveList

"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brep edges list accessor.

Get: Edges(self: Brep) -> BrepEdgeList

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brep faces list accessor.

Get: Faces(self: Brep) -> BrepFaceList

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the Brep is manifold. 
            Non-Manifold breps have at least one edge that is shared among three or more faces.

Get: IsManifold(self: Brep) -> bool

"""

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether this brep is a solid, or a closed oriented manifold.

Get: IsSolid(self: Brep) -> bool

"""

    IsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Brep has a single face and that face is geometrically the same
            as the underlying surface.  I.e., the face has trivial trimming.
            In this case, the surface is the first face surface. The flag
            Brep.Faces[0].OrientationIsReversed records the correspondence between the surface's
            natural parametric orientation and the orientation of the Brep.trivial trimming here means that there is only one loop curve in the brep
            and that loop curve is the same as the underlying surface boundary.

Get: IsSurface(self: Brep) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brep loop list accessor.

Get: Loops(self: Brep) -> BrepLoopList

"""

    SolidOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the solid orientation state of this Brep.

Get: SolidOrientation(self: Brep) -> BrepSolidOrientation

"""

    Surfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Parametric surfaces used by faces

Get: Surfaces(self: Brep) -> BrepSurfaceList

"""

    Trims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brep trims list accessor.

Get: Trims(self: Brep) -> BrepTrimList

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Vertices(self: Brep) -> BrepVertexList

"""



class CurveProxy(Curve, IDisposable, ISerializable):
    """ Provides strongly-typed access to Brep edges. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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

    ProxyCurveIsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if "this" is a curve is reversed from the "real" curve geometry

Get: ProxyCurveIsReversed(self: CurveProxy) -> bool

"""



class BrepEdge(CurveProxy, IDisposable, ISerializable):
    """ Represents a single edge curve in a Brep object. """
    def AdjacentFaces(self):
        """
        AdjacentFaces(self: BrepEdge) -> Array[int]
        
            Gets the indices of all the BrepFaces that use this edge.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def GetEdgeParameter(self, trimIndex, trimParameter, edgeParameter):
        """
        GetEdgeParameter(self: BrepEdge, trimIndex: int, trimParameter: float) -> (bool, float)
        
            Get corresponding edge parameter for given trim at given trim parameter.
            Returns: true on success
        """
        pass

    def IsSmoothManifoldEdge(self, angleToleranceRadians):
        """
        IsSmoothManifoldEdge(self: BrepEdge, angleToleranceRadians: float) -> bool
        
            For a manifold, non-boundary edge, decides whether or not the two surfaces
                    on 
             either side meet smoothly.
        
        
            angleToleranceRadians: used to decide if surface normals on either side are parallel.
            Returns: true if edge is manifold, has exactly 2 trims, and surface normals on either
                    side 
             agree to within angle_tolerance.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def SetEdgeCurve(self, curve3dIndex, subDomain=None):
        """
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int, subDomain: Interval) -> bool
        
            Set 3d curve geometry used by a b-rep edge.
        
            curve3dIndex: index of 3d curve in m_C3[] array
            Returns: true if successful
        SetEdgeCurve(self: BrepEdge, curve3dIndex: int) -> bool
        
            Set 3d curve geometry used by a b-rep edge.
        
            curve3dIndex: index of 3d curve in m_C3[] array
            Returns: true if successful
        """
        pass

    def TrimIndices(self):
        """
        TrimIndices(self: BrepEdge) -> Array[int]
        
            Gets the indices of all trims associated with this edge.
            Returns: Empty array on failure.
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

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Brep that owns this edge.

Get: Brep(self: BrepEdge) -> Brep

"""

    EdgeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this edge in the Brep.Edges collection.

Get: EdgeIndex(self: BrepEdge) -> int

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """BrepVertex at end of edge

Get: EndVertex(self: BrepEdge) -> BrepVertex

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """BrepVertex at start of edge

Get: StartVertex(self: BrepEdge) -> BrepVertex

"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the accuracy of the edge curve (>=0.0 or RhinoMath.UnsetValue)
             A value of UnsetValue indicates that the tolerance should be computed.
            
             The maximum distance from the edge's 3d curve to any surface of a face
             that has this edge as a portion of its boundary must be <= this tolerance.

Get: Tolerance(self: BrepEdge) -> float

Set: Tolerance(self: BrepEdge) = value
"""

    TrimCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of trim-curves that use this edge.

Get: TrimCount(self: BrepEdge) -> int

"""

    Valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the topological valency of this edge. The topological valency 
            is defined by how many adjacent faces share this edge.

Get: Valence(self: BrepEdge) -> EdgeAdjacency

"""



class Surface(GeometryBase, IDisposable, ISerializable):
    """
    Represents a base class that is common to most RhinoCommon surface types.
                A surface represents an entity that can be all visited by providing
                two independent parameters, usually called (u, v), or sometimes (s, t).
    """
    def ClosestPoint(self, testPoint, u, v):
        """
        ClosestPoint(self: Surface, testPoint: Point3d) -> (bool, float, float)
        
            Input the parameters of the point on the surface that is closest to testPoint.
        
            testPoint: A point to test against.
            Returns: true on success, false on failure.
        """
        pass

    def ClosestSide(self, u, v):
        """
        ClosestSide(self: Surface, u: float, v: float) -> IsoStatus
        
            Gets the side that is closest, in terms of 3D-distance, to a U and V parameter.
        
            u: A u parameter.
            v: A v parameter.
            Returns: A side.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def CreateExtrusion(profile, direction):
        """
        CreateExtrusion(profile: Curve, direction: Vector3d) -> Surface
        
            Constructs a surface by extruding a curve along a vector.
        
            profile: Profile curve to extrude.
            direction: Direction and length of extrusion.
            Returns: A surface on success or null on failure.
        """
        pass

    @staticmethod
    def CreateExtrusionToPoint(profile, apexPoint):
        """
        CreateExtrusionToPoint(profile: Curve, apexPoint: Point3d) -> Surface
        
            Constructs a surface by extruding a curve to a point.
        
            profile: Profile curve to extrude.
            apexPoint: Apex point of extrusion.
            Returns: A Surface on success or null on failure.
        """
        pass

    @staticmethod
    def CreatePeriodicSurface(baseSurface, direction):
        """
        CreatePeriodicSurface(baseSurface: Surface, direction: int) -> Surface
        
            Constructs a periodic surface from a base surface and a direction.
        
            baseSurface: A base surface.
            direction: 0 is first parameter, 1 is second parameter.
            Returns: A new surface; or null on error.
        """
        pass

    @staticmethod
    def CreateRollingBallFillet(surfaceA, *__args):
        """
        CreateRollingBallFillet(surfaceA: Surface, uvA: Point2d, surfaceB: Surface, uvB: Point2d, radius: float, tolerance: float) -> Array[Surface]
        
            Constructs a rolling ball fillet between two surfaces.
        
            surfaceA: A first surface.
            uvA: A point in the parameter space of FaceA near where the fillet is expected to hit the surface.
            surfaceB: A second surface.
            uvB: A point in the parameter space of FaceB near where the fillet is expected to hit the surface.
            radius: A radius value.
            tolerance: A tolerance value used for approximating and intersecting offset surfaces.
            Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.
        CreateRollingBallFillet(surfaceA: Surface, flipA: bool, surfaceB: Surface, flipB: bool, radius: float, tolerance: float) -> Array[Surface]
        
            Constructs a rolling ball fillet between two surfaces.
        
            surfaceA: A first surface.
            flipA: A value that indicates whether A should be used in flipped mode.
            surfaceB: A second surface.
            flipB: A value that indicates whether B should be used in flipped mode.
            radius: A radius value.
            tolerance: A tolerance value.
            Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.
        CreateRollingBallFillet(surfaceA: Surface, surfaceB: Surface, radius: float, tolerance: float) -> Array[Surface]
        
            Constructs a rolling ball fillet between two surfaces.
        
            surfaceA: A first surface.
            surfaceB: A second surface.
            radius: A radius value.
            tolerance: A tolerance value.
            Returns: A new array of rolling ball fillet surfaces; this array can be empty on failure.
        """
        pass

    def CurvatureAt(self, u, v):
        """
        CurvatureAt(self: Surface, u: float, v: float) -> SurfaceCurvature
        
            Computes the curvature at the given UV coordinate.
        
            u: U parameter for evaluation.
            v: V parameter for evaluation.
            Returns: Surface Curvature data for the point at uv or null on failure.
        """
        pass

    def Degree(self, direction):
        """
        Degree(self: Surface, direction: int) -> int
        
            Returns the maximum algebraic degree of any span
                    (or a good estimate if curve spans 
             are not algebraic).
        
        
            direction: 0 gets first parameter's domain, 1 gets second parameter's domain.
            Returns: The maximum degree.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Domain(self, direction):
        """
        Domain(self: Surface, direction: int) -> Interval
        
            Gets the domain in a direction.
        
            direction: 0 gets first parameter, 1 gets second parameter.
            Returns: An interval value.
        """
        pass

    def Evaluate(self, u, v, numberDerivatives, point, derivatives):
        """
        Evaluate(self: Surface, u: float, v: float, numberDerivatives: int) -> (bool, Point3d, Array[Vector3d])
        
            Evaluates a surface mathematically.
        
            u: A U parameter.
            v: A V parameter.
            numberDerivatives: The number of derivatives.
            Returns: true if the operation succeeded; false otherwise.
        """
        pass

    def Extend(self, edge, extensionLength, smooth):
        """
        Extend(self: Surface, edge: IsoStatus, extensionLength: float, smooth: bool) -> Surface
        
            Extends an untrimmed surface along one edge.
        
            edge: Edge to extend.  Must be North, South, East, or West.
            extensionLength: distance to extend.
            smooth: true for smooth (C-infinity) extension. 
                    false for a C1- ruled extension.
            Returns: New extended surface on success.
        """
        pass

    def Fit(self, uDegree, vDegree, fitTolerance):
        """
        Fit(self: Surface, uDegree: int, vDegree: int, fitTolerance: float) -> Surface
        
            Fits a new surface through an existing surface.
        
            uDegree: the output surface U degree. Must be bigger than 1.
            vDegree: the output surface V degree. Must be bigger than 1.
            fitTolerance: The fitting tolerance.
            Returns: A surface, or null on error.
        """
        pass

    def FrameAt(self, u, v, frame):
        """
        FrameAt(self: Surface, u: float, v: float) -> (bool, Plane)
        
            Computes the orient plane on a surface given a U and V parameter.
                    This is the 
             simple evaluation call with no error handling.
        
        
            u: A first parameter.
            v: A second parameter.
            Returns: true if this operation succeeded; otherwise false.
        """
        pass

    def GetNextDiscontinuity(self, direction, continuityType, t0, t1, t):
        """
        GetNextDiscontinuity(self: Surface, direction: int, continuityType: Continuity, t0: float, t1: float) -> (bool, float)
        
            Searches for a derivative, tangent, or curvature discontinuity.
        
            direction: If 0, then "u" parameter is checked. If 1, then the "v" parameter is checked.
            continuityType: The desired continuity.
            t0: Search begins at t0. If there is a discontinuity at t0, it will be ignored. 
                    This 
             makes it possible to repeatedly call GetNextDiscontinuity and step through the discontinuities.
        
            t1: (t0 != t1) If there is a discontinuity at t1 is will be ingored unless c is a locus 
             discontinuity
                    type and t1 is at the start or end of the curve.
        
            Returns: Parametric continuity tests c = (C0_continuous, ..., G2_continuous):
                    TRUE if a 
             parametric discontinuity was found strictly between t0 and t1.
                    Note well that all 
             curves are parametrically continuous at the ends of their domains.
                    
                    
             Locus continuity tests c = (C0_locus_continuous, ...,G2_locus_continuous):
                    TRUE if 
             a locus discontinuity was found strictly between t0 and t1 or at t1 is the
                    at the 
             end of a curve. Note well that all open curves (IsClosed()=false) are locus
                    
             discontinuous at the ends of their domains.  All closed curves (IsClosed()=true) are
                   
              at least C0_locus_continuous at the ends of their domains.
        """
        pass

    def GetSpanVector(self, direction):
        """
        GetSpanVector(self: Surface, direction: int) -> Array[float]
        
            Gets array of span "knots".
        
            direction: 0 gets first parameter's domain, 1 gets second parameter's domain.
            Returns: An array with span vectors; or null on error.
        """
        pass

    def GetSurfaceSize(self, width, height):
        """
        GetSurfaceSize(self: Surface) -> (bool, float, float)
        
            Gets an estimate of the size of the rectangle that would be created
                    if the 3d 
             surface where flattened into a rectangle.
        
            Returns: true if successful.
        """
        pass

    def HasNurbsForm(self):
        """
        HasNurbsForm(self: Surface) -> int
        
            Is there a NURBS surface representation of this surface.
            Returns: 0 unable to create NURBS representation with desired accuracy.
                    1 success - NURBS 
             parameterization matches the surface's
                    2 success - NURBS point locus matches the 
             surface's and the
                    domain of the NURBS surface is correct. However, This surface's
         
                        parameterization and the NURBS surface parameterization may not
                    match.  
             This situation happens when getting NURBS representations
                    of surfaces that have a 
             transendental parameterization like spheres,
                    cylinders, and cones.
        """
        pass

    def InterpolatedCurveOnSurface(self, points, tolerance):
        """ InterpolatedCurveOnSurface(self: Surface, points: IEnumerable[Point3d], tolerance: float) -> NurbsCurve """
        pass

    def InterpolatedCurveOnSurfaceUV(self, points, tolerance):
        """ InterpolatedCurveOnSurfaceUV(self: Surface, points: IEnumerable[Point2d], tolerance: float) -> NurbsCurve """
        pass

    def IsAtSeam(self, u, v):
        """
        IsAtSeam(self: Surface, u: float, v: float) -> int
        
            Tests if a surface parameter value is at a seam.
        
            u: Surface u parameter to test.
            v: Surface v parameter to test.
            Returns: 0 if not a seam,
                    1 if u == Domain(0)[i] and srf(u, v) == srf(Domain(0)[1-i], v)
           
                      2 if v == Domain(1)[i] and srf(u, v) == srf(u, Domain(1)[1-i])
                    3 if 1 and 
             2 are true.
        """
        pass

    def IsAtSingularity(self, u, v, exact):
        """
        IsAtSingularity(self: Surface, u: float, v: float, exact: bool) -> bool
        
            Tests if a surface parameter value is at a singularity.
        
            u: Surface u parameter to test.
            v: Surface v parameter to test.
            exact: If true, test if (u,v) is exactly at a singularity.
                    If false, test if close enough 
             to cause numerical problems.
        
            Returns: true if surface is singular at (s,t)
        """
        pass

    def IsClosed(self, direction):
        """
        IsClosed(self: Surface, direction: int) -> bool
        
            Gets a value indicating if the surface is closed in a direction.
        
            direction: 0 = U, 1 = V.
            Returns: The indicating boolean value.
        """
        pass

    def IsCone(self, tolerance=None):
        """
        IsCone(self: Surface, tolerance: float) -> bool
        
            Determines if the surface is a portion of a cone within a given tolerance.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a cone.
        IsCone(self: Surface) -> bool
        
            Determines if the surface is a portion of a cone within RhinoMath.ZeroTolerance.
            Returns: true if the surface is a portion of a cone.
        """
        pass

    def IsContinuous(self, continuityType, u, v):
        """
        IsContinuous(self: Surface, continuityType: Continuity, u: float, v: float) -> bool
        
            Tests continuity at a surface parameter value.
        
            continuityType: The continuity type to sample.
            u: Surface u parameter to test.
            v: Surface v parameter to test.
            Returns: true if the surface has at least the specified continuity at the (u,v) parameter.
        """
        pass

    def IsCylinder(self, tolerance=None):
        """
        IsCylinder(self: Surface, tolerance: float) -> bool
        
            Determines if the surface is a portion of a cylinder within a given tolerance.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a cylinder.
        IsCylinder(self: Surface) -> bool
        
            Determines if the surface is a portion of a cylinder within RhinoMath.ZeroTolerance.
            Returns: true if the surface is a portion of a cylinder.
        """
        pass

    def IsIsoparametric(self, *__args):
        """
        IsIsoparametric(self: Surface, bbox: BoundingBox) -> IsoStatus
        
            Determines if a 2d bounding box is iso-parameteric in the parameter space of this surface.
        
            bbox: Bounding box to test.
            Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the bounding 
             box.
        
        IsIsoparametric(self: Surface, curve: Curve) -> IsoStatus
        
            Determines if a 2d curve is iso-parameteric in the parameter space of this surface.
        
            curve: Curve to test.
            Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the curve.
        IsIsoparametric(self: Surface, curve: Curve, curveDomain: Interval) -> IsoStatus
        
            Determines if a 2D curve is iso-parameteric in the parameter space of this surface.
        
            curve: Curve to test.
            curveDomain: Sub domain of the curve.
            Returns: IsoStatus flag describing the iso-parametric relationship between the surface and the curve.
        """
        pass

    def IsoCurve(self, direction, constantParameter):
        """
        IsoCurve(self: Surface, direction: int, constantParameter: float) -> Curve
        
            Gets isoparametric curve.
        
            direction: 0 first parameter varies and second parameter is constant
                    e.g., point on 
             IsoCurve(0,c) at t is srf(t,c)
                    This is a horizontal line from left to right
               
                  
                    1 first parameter is constant and second parameter varies
                    e.g., 
             point on IsoCurve(1,c) at t is srf(c,t
                    This is a vertical line from bottom to top.
        
            constantParameter: The parameter that was constant on the original surface.
            Returns: An isoparametric curve or null on error.
        """
        pass

    def IsPeriodic(self, direction):
        """
        IsPeriodic(self: Surface, direction: int) -> bool
        
            Gets a value indicating if thr surface is periodic in a direction (default is false).
        
            direction: 0 = U, 1 = V.
            Returns: The indicating boolean value.
        """
        pass

    def IsPlanar(self, tolerance=None):
        """
        IsPlanar(self: Surface, tolerance: float) -> bool
        
            Tests a surface to see if it is planar to a given tolerance.
        
            tolerance: tolerance to use when checking.
            Returns: true if there is a plane such that the maximum distance from
                    the surface to the 
             plane is <= tolerance.
        
        IsPlanar(self: Surface) -> bool
        
            Tests a surface to see if it is planar to zero tolerance.
            Returns: true if the surface is planar (flat) to within RhinoMath.ZeroTolerance units (1e-12).
        """
        pass

    def IsSingular(self, side):
        """
        IsSingular(self: Surface, side: int) -> bool
        
            true if surface side is collapsed to a point.
        
            side: side of parameter space to test
                    0 = south, 1 = east, 2 = north, 3 = west.
            Returns: True if this specific side of the surface is singular; otherwise, false.
        """
        pass

    def IsSphere(self, tolerance=None):
        """
        IsSphere(self: Surface, tolerance: float) -> bool
        
            Determines if the surface is a portion of a sphere within a given tolerance.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a sphere.
        IsSphere(self: Surface) -> bool
        
            Determines if the surface is a portion of a sphere within RhinoMath.ZeroTolerance.
            Returns: true if the surface is a portion of a sphere.
        """
        pass

    def IsTorus(self, tolerance=None):
        """
        IsTorus(self: Surface, tolerance: float) -> bool
        
            Determines if the surface is a portion of a torus within a given tolerance.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a torus.
        IsTorus(self: Surface) -> bool
        
            Determines if the surface is a portion of a torus within RhinoMath.ZeroTolerance.
            Returns: true if the surface is a portion of a torus.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def NormalAt(self, u, v):
        """
        NormalAt(self: Surface, u: float, v: float) -> Vector3d
        
            Computes the surface normal at a point.
                    This is the simple evaluation call - it 
             does not support error handling.
        
        
            u: A U parameter.
            v: A V parameter.
            Returns: The normal.
        """
        pass

    def Offset(self, distance, tolerance):
        """
        Offset(self: Surface, distance: float, tolerance: float) -> Surface
        
            Constructs a new surface which is offset from the current surface.
        
            distance: Distance (along surface normal) to offset.
            tolerance: Offset accuracy.
            Returns: The offsetted surface or null on failure.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def PointAt(self, u, v):
        """
        PointAt(self: Surface, u: float, v: float) -> Point3d
        
            Evaluates a point at a given parameter.
        
            u: evaluation parameters.
            v: evaluation parameters.
            Returns: Point3d.Unset on failure.
        """
        pass

    def Pullback(self, curve3d, tolerance, curve3dSubdomain=None):
        """
        Pullback(self: Surface, curve3d: Curve, tolerance: float, curve3dSubdomain: Interval) -> Curve
        
            Pulls a 3d curve back to the surface's parameter space.
        
            curve3d: A curve.
            tolerance: the maximum acceptable 3d distance between from surface(curve_2d(t))
                    to the locus 
             of points on the surface that are closest to curve_3d.
        
            curve3dSubdomain: A subdomain of the curve to sample.
            Returns: 2d curve.
        Pullback(self: Surface, curve3d: Curve, tolerance: float) -> Curve
        
            Pulls a 3d curve back to the surface's parameter space.
        
            curve3d: The curve to pull.
            tolerance: the maximum acceptable 3d distance between from surface(curve_2d(t))
                    to the locus 
             of points on the surface that are closest to curve_3d.
        
            Returns: 2d curve.
        """
        pass

    def Pushup(self, curve2d, tolerance, curve2dSubdomain=None):
        """
        Pushup(self: Surface, curve2d: Curve, tolerance: float) -> Curve
        
            Computes a 3d curve that is the composite of a 2d curve and the surface map.
        
            curve2d: a 2d curve whose image is in the surface's domain.
            tolerance: the maximum acceptable distance from the returned 3d curve to the image of curve_2d on the 
             surface.
        
            Returns: 3d curve.
        Pushup(self: Surface, curve2d: Curve, tolerance: float, curve2dSubdomain: Interval) -> Curve
        
            Computes a 3d curve that is the composite of a 2d curve and the surface map.
        
            curve2d: a 2d curve whose image is in the surface's domain.
            tolerance: the maximum acceptable distance from the returned 3d curve to the image of curve_2d on the 
             surface.
        
            curve2dSubdomain: The curve interval (a sub-domain of the original curve) to use.
            Returns: 3d curve.
        """
        pass

    def Rebuild(self, uDegree, vDegree, uPointCount, vPointCount):
        """
        Rebuild(self: Surface, uDegree: int, vDegree: int, uPointCount: int, vPointCount: int) -> NurbsSurface
        
            Rebuilds an existing surface to a given degree and point count.
        
            uDegree: the output surface u degree.
            vDegree: the output surface u degree.
            uPointCount: The number of points in the output surface u direction. Must be bigger
                    than uDegree 
             (maximum value is 1000)
        
            vPointCount: The number of points in the output surface v direction. Must be bigger
                    than vDegree 
             (maximum value is 1000)
        
            Returns: new rebuilt surface on success. null on failure.
        """
        pass

    def Reverse(self, direction, inPlace=None):
        """
        Reverse(self: Surface, direction: int, inPlace: bool) -> Surface
        
            Same as Reverse, but if inPlace is set to true this Surface is modified
                    instead of 
             a new copy being created.
        
        
            direction: 0 for first parameter's domain, 1 for second parameter's domain.
            Returns: If inPlace is False, a new reversed surface on success. If inPlace is
                    true, this 
             surface instance is returned on success.
        
        Reverse(self: Surface, direction: int) -> Surface
        
            Reverses parameterization Domain changes from [a,b] to [-b,-a]
        
            direction: 0 for first parameter's domain, 1 for second parameter's domain.
            Returns: a new reversed surface on success.
        """
        pass

    def SetDomain(self, direction, domain):
        """
        SetDomain(self: Surface, direction: int, domain: Interval) -> bool
        
            Sets the domain in a direction.
        
            direction: 0 sets first parameter's domain, 1 sets second parameter's domain.
            domain: A new domain to be assigned.
            Returns: true if setting succeeded, otherwise false.
        """
        pass

    def ShortPath(self, start, end, tolerance):
        """
        ShortPath(self: Surface, start: Point2d, end: Point2d, tolerance: float) -> Curve
        
            Constructs a geodesic between 2 points, used by ShortPath command in Rhino.
        
            start: start point of curve in parameter space. Points must be distinct in the domain of thie surface.
            end: end point of curve in parameter space. Points must be distinct in the domain of thie surface.
            tolerance: tolerance used in fitting discrete solution.
            Returns: a geodesic curve on the surface on success. null on failure.
        """
        pass

    def SpanCount(self, direction):
        """
        SpanCount(self: Surface, direction: int) -> int
        
            Gets number of smooth nonempty spans in the parameter direction.
        
            direction: 0 gets first parameter's domain, 1 gets second parameter's domain.
            Returns: The span count.
        """
        pass

    def Split(self, direction, parameter):
        """
        Split(self: Surface, direction: int, parameter: float) -> Array[Surface]
        
            Splits (divides) the surface into two parts at the specified parameter
        
            direction: 0 = The surface is split vertically. The "west" side is returned as the first
                    
             surface in the array and the "east" side is returned as the second surface in
                    the 
             array.
                    1 = The surface is split horizontally. The "south" side is returned as the 
             first surface in the array and the "north"
                    side is returned as the second surfae in 
             the array
        
            parameter: value of constant parameter in interval returned by Domain(direction)
            Returns: Array of two surfaces on success
        """
        pass

    def ToBrep(self):
        """
        ToBrep(self: Surface) -> Brep
        
            Converts the surface into a Brep.
            Returns: A Brep with a similar shape like this surface or null.
        """
        pass

    def ToNurbsSurface(self, tolerance=None, accuracy=None):
        """
        ToNurbsSurface(self: Surface, tolerance: float) -> (NurbsSurface, int)
        
            Gets a NURBS surface representation of this surface.
        
            tolerance: tolerance to use when creating NURBS representation.
            Returns: NurbsSurface on success, null on failure.
        ToNurbsSurface(self: Surface) -> NurbsSurface
        
            Gets a NURBS surface representation of this surface. Default 
                    tolerance of 0.0 is 
             used.
        
            Returns: NurbsSurface on success, null on failure.
        """
        pass

    def Transpose(self, inPlace=None):
        """
        Transpose(self: Surface, inPlace: bool) -> Surface
        
            Transposes surface parameterization (swap U and V)
            Returns: New transposed surface on success, null on failure.
        Transpose(self: Surface) -> Surface
        
            Transposes surface parameterization (swap U and V)
            Returns: New transposed surface on success, null on failure.
        """
        pass

    def Trim(self, u, v):
        """
        Trim(self: Surface, u: Interval, v: Interval) -> Surface
        
            Constructs a sub-surface that covers the specified UV trimming domain.
        
            u: Domain of surface along U direction to include in the subsurface.
            v: Domain of surface along V direction to include in the subsurface.
            Returns: SubSurface on success, null on failure.
        """
        pass

    def TryGetCone(self, cone, tolerance=None):
        """
        TryGetCone(self: Surface, tolerance: float) -> (bool, Cone)
        
            Tests a surface to see if it is a portion of a cone and returns the cone.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a cone.
        TryGetCone(self: Surface) -> (bool, Cone)
        
            Tests a surface to see if it is a portion of a cone within RhinoMath.ZeroTolerance and return 
             the cone.
        
            Returns: true if the surface is a portion of a cone.
        """
        pass

    def TryGetCylinder(self, cylinder, tolerance=None):
        """
        TryGetCylinder(self: Surface, tolerance: float) -> (bool, Cylinder)
        
            Tests a surface to see if it is a portion of a cylinder and return the cylinder.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a cylinder.
        TryGetCylinder(self: Surface) -> (bool, Cylinder)
        
            Tests a surface to see if it is a portion of a cylinder within RhinoMath.ZeroTolerance and 
             return the cylinder.
        
            Returns: true if the surface is a portion of a cylinder.
        """
        pass

    def TryGetPlane(self, plane, tolerance=None):
        """
        TryGetPlane(self: Surface, tolerance: float) -> (bool, Plane)
        
            Tests a surface for planarity and return the plane.
        
            tolerance: tolerance to use when checking.
            Returns: true if there is a plane such that the maximum distance from the surface to the plane is <= 
             tolerance.
        
        TryGetPlane(self: Surface) -> (bool, Plane)
        
            Tests a surface for planarity and return the plane.
            Returns: true if there is a plane such that the maximum distance from the surface to the plane is <= 
             RhinoMath.ZeroTolerance.
        """
        pass

    def TryGetSphere(self, sphere, tolerance=None):
        """
        TryGetSphere(self: Surface, tolerance: float) -> (bool, Sphere)
        
            Test a surface to see if it is a portion of a sphere and return the sphere.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a sphere.
        TryGetSphere(self: Surface) -> (bool, Sphere)
        
            Test a surface to see if it is a portion of a sphere and return the sphere.
            Returns: true if the surface is a portion of a sphere.
        """
        pass

    def TryGetTorus(self, torus, tolerance=None):
        """
        TryGetTorus(self: Surface, tolerance: float) -> (bool, Torus)
        
            Tests a surface to see if it is a portion of a torus and returns the torus.
        
            tolerance: tolerance to use when checking.
            Returns: true if the surface is a portion of a torus.
        TryGetTorus(self: Surface) -> (bool, Torus)
        
            Tests a surface to see if it is a portion of a torus within RhinoMath.ZeroTolerance and returns 
             the torus.
        
            Returns: true if the surface is a portion of a torus.
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
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a values indicating whether a surface is solid.

Get: IsSolid(self: Surface) -> bool

"""



class SurfaceProxy(Surface, IDisposable, ISerializable):
    """ Provides a base class to brep faces and other surface proxies. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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


class BrepFace(SurfaceProxy, IDisposable, ISerializable):
    """
    Provides strongly-typed access to brep faces.
                A Brep face is composed of one surface and trimming curves.
    """
    def AdjacentEdges(self):
        """
        AdjacentEdges(self: BrepFace) -> Array[int]
        
            Gets the indices of all the BrepEdges that delineate this Face.
        """
        pass

    def AdjacentFaces(self):
        """
        AdjacentFaces(self: BrepFace) -> Array[int]
        
            Gets the indices of all the BrepFaces that surround (are adjacent to) this face.
        """
        pass

    def ChangeSurface(self, surfaceIndex):
        """
        ChangeSurface(self: BrepFace, surfaceIndex: int) -> bool
        
            Expert user tool that replaces the 3d surface geometry use by the face.
        
            surfaceIndex: brep surface index of new surface.
            Returns: true if successful.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def CreateExtrusion(self, pathCurve, cap):
        """
        CreateExtrusion(self: BrepFace, pathCurve: Curve, cap: bool) -> Brep
        
            Extrude a face in a Brep.
        
            pathCurve: The path to extrude along.
            cap: If true, the extrusion is capped with a translation of the face being extruded
            Returns: A Brep on success or null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def DuplicateFace(self, duplicateMeshes):
        """
        DuplicateFace(self: BrepFace, duplicateMeshes: bool) -> Brep
        
            Duplicate a face from the brep to create new single face brep.
        
            duplicateMeshes: If true, shading meshes will be copied as well.
            Returns: A new single-face brep synonymous with the current Face.
        """
        pass

    def DuplicateSurface(self):
        """
        DuplicateSurface(self: BrepFace) -> Surface
        
            Gets a copy to the untrimmed surface that this face is based on.
            Returns: A copy of this face's underlying surface.
        """
        pass

    def GetMesh(self, meshType):
        """
        GetMesh(self: BrepFace, meshType: MeshType) -> Mesh
        
            Obtains a reference to a specified type of mesh for this brep face.
        
            meshType: The mesh type.
            Returns: A mesh.
        """
        pass

    def IsPointOnFace(self, u, v):
        """
        IsPointOnFace(self: BrepFace, u: float, v: float) -> PointFaceRelation
        
            Tests if a parameter space point is on the interior of a trimmed face.
        
            u: Parameter space point u value.
            v: Parameter space point v value.
            Returns: A value describing the spatial relationship between the point and the face.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def PullPointsToFace(self, points, tolerance):
        """ PullPointsToFace(self: BrepFace, points: IEnumerable[Point3d], tolerance: float) -> Array[Point3d] """
        pass

    def RebuildEdges(self, tolerance, rebuildSharedEdges, rebuildVertices):
        """
        RebuildEdges(self: BrepFace, tolerance: float, rebuildSharedEdges: bool, rebuildVertices: bool) -> bool
        
            Rebuild the edges used by a face so they lie on the surface.
        
            tolerance: tolerance for fitting 3d edge curves.
            rebuildSharedEdges: if false and and edge is used by this face and a neighbor, then the edge
                    will be 
             skipped.
        
            rebuildVertices: if true, vertex locations are updated to lie on the surface.
            Returns: true on success.
        """
        pass

    def SetDomain(self, direction, domain):
        """
        SetDomain(self: BrepFace, direction: int, domain: Interval) -> bool
        
            Sets the surface domain of this face.
        
            direction: Direction of face to set (0 = U, 1 = V).
            domain: Domain to apply.
            Returns: true on success, false on failure.
        """
        pass

    def SetMesh(self, meshType, mesh):
        """
        SetMesh(self: BrepFace, meshType: MeshType, mesh: Mesh) -> bool
        
            Sets a reference to a specified type of mesh for this brep face.
        
            meshType: The mesh type.
            mesh: The new mesh.
            Returns: true if the operation succeeded; otherwise false.
        """
        pass

    def Split(self, *__args):
        """ Split(self: BrepFace, curves: IEnumerable[Curve], tolerance: float) -> Brep """
        pass

    def TrimAwareIsoCurve(self, direction, constantParameter):
        """
        TrimAwareIsoCurve(self: BrepFace, direction: int, constantParameter: float) -> Array[Curve]
        
            Similar to IsoCurve function, except this function pays attention to trims on faces 
                   
              and may return multiple curves.
        
        
            direction: Direction of isocurve.
                    0 = Isocurve connects all points with a constant U value.1 = 
             Isocurve connects all points with a constant V value.
        
            constantParameter: Surface parameter that remains identical along the isocurves.
            Returns: Isoparametric curves connecting all points with the constantParameter value.
        """
        pass

    def TrimAwareIsoIntervals(self, direction, constantParameter):
        """
        TrimAwareIsoIntervals(self: BrepFace, direction: int, constantParameter: float) -> Array[Interval]
        
            Gets intervals where the iso curve exists on a BrepFace (trimmed surface)
        
            direction: Direction of isocurve.
                    0 = Isocurve connects all points with a constant U value.1 = 
             Isocurve connects all points with a constant V value.
        
            constantParameter: Surface parameter that remains identical along the isocurves.
            Returns: If direction = 0, the parameter space iso interval connects the 2d points
                    
             (intervals[i][0],iso_constant) and (intervals[i][1],iso_constant).
                    If direction = 
             1, the parameter space iso interval connects the 2d points
                    
             (iso_constant,intervals[i][0]) and (iso_constant,intervals[i][1]).
        """
        pass

    def UnderlyingSurface(self):
        """
        UnderlyingSurface(self: BrepFace) -> Surface
        
            Gets the untrimmed surface that is the base of this face.
            Returns: A surface, or null on error.
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

    FaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of face in Brep.Faces array.

Get: FaceIndex(self: BrepFace) -> int

"""

    IsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the face is synonymous with the underlying surface. 
            If a Face has no trimming curves then it is considered a Surface.

Get: IsSurface(self: BrepFace) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Loops in this face.

Get: Loops(self: BrepFace) -> BrepLoopList

"""

    OrientationIsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if face orientation is opposite of natural surface orientation.

Get: OrientationIsReversed(self: BrepFace) -> bool

Set: OrientationIsReversed(self: BrepFace) = value
"""

    OuterLoop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Every face has a single outer loop.

Get: OuterLoop(self: BrepFace) -> BrepLoop

"""

    SurfaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Surface index of the 3d surface geometry used by this face or -1

Get: SurfaceIndex(self: BrepFace) -> int

"""



class BrepLoop(GeometryBase, IDisposable, ISerializable):
    """
    Represent a single loop in a Brep object. A loop is composed
                of a list of trim curves.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def To2dCurve(self):
        """
        To2dCurve(self: BrepLoop) -> Curve
        
            Create a 2d curve that traces the entire loop
        """
        pass

    def To3dCurve(self):
        """
        To3dCurve(self: BrepLoop) -> Curve
        
            Create a 3D curve that approximates the loop geometry.
            Returns: A 3D curve that approximates the loop or null on failure.
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

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Brep that owns this loop.

Get: Brep(self: BrepLoop) -> Brep

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """BrepFace this loop belongs to.

Get: Face(self: BrepLoop) -> BrepFace

"""

    LoopIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this loop in the Brep.Loops collection.

Get: LoopIndex(self: BrepLoop) -> int

"""

    LoopType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """type of loop.

Get: LoopType(self: BrepLoop) -> BrepLoopType

"""

    Trims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of trims for this loop

Get: Trims(self: BrepLoop) -> BrepTrimList

"""



class BrepLoopType(Enum, IComparable, IFormattable, IConvertible):
    """
    Each brep loop has a defined type, e.g. outer, inner or point on surface.
    
    enum BrepLoopType, values: CurveOnSurface (4), Inner (2), Outer (1), PointOnSurface (5), Slit (3), Unknown (0)
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

    CurveOnSurface = None
    Inner = None
    Outer = None
    PointOnSurface = None
    Slit = None
    Unknown = None
    value__ = None


class BrepRegion(object):
    """ Represents a brep topological region that has sides. """
    def BoundaryBrep(self):
        """
        BoundaryBrep(self: BrepRegion) -> Brep
        
            Gets the boundary of a region as a brep object. If the region is finite,
                    the 
             boundary will be a closed  manifold brep. The boundary may have more than one
                    
             connected component.
        
            Returns: A brep or null on error.
        """
        pass

    def GetFaceSides(self):
        """
        GetFaceSides(self: BrepRegion) -> Array[BrepRegionFaceSide]
        
            Gets an array of Rhino.Geometry.BrepRegionFaceSide entities delimiting this region.
            Returns: An array of region face sides. This array might be empty on failure.
        """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the region bounding box.

Get: BoundingBox(self: BrepRegion) -> BoundingBox

"""

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the Brep this region belongs to.

Get: Brep(self: BrepRegion) -> Brep

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of region in the RegionTopology array.

Get: Index(self: BrepRegion) -> int

"""

    IsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this region is finite.

Get: IsFinite(self: BrepRegion) -> bool

"""



class BrepRegionFaceSide(object):
    """ Represents a side of a Rhino.Geometry.BrepRegion entity. """
    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The brep this side belongs to.

Get: Brep(self: BrepRegionFaceSide) -> Brep

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the face this side belongs to.

Get: Face(self: BrepRegionFaceSide) -> BrepFace

"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The region this side belongs to.

Get: Region(self: BrepRegionFaceSide) -> BrepRegion

"""

    SurfaceNormalPointsIntoRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if BrepFace's surface normal points into region; false otherwise.

Get: SurfaceNormalPointsIntoRegion(self: BrepRegionFaceSide) -> bool

"""



class BrepSolidOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all possible Solid Orientations for a Brep.
    
    enum BrepSolidOrientation, values: Inward (-1), None (0), Outward (1), Unknown (2)
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

    Inward = None
    None = None
    Outward = None
    Unknown = None
    value__ = None


class BrepTrim(CurveProxy, IDisposable, ISerializable):
    """
    Brep trim information is stored in BrepTrim classes. Brep.Trims is an
                array of all the trims in the brep. A BrepTrim is derived from CurveProxy
                so the trim can supply easy to use evaluation tools via the Curve virtual
                member functions.
                Note well that the domains and orientations of the curve m_C2[trim.m_c2i]
                and the trim as a curve may not agree.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def GetTolerances(self, toleranceU, toleranceV):
        """
        GetTolerances(self: BrepTrim) -> (float, float)
        
            The values in tolerance[] record the accuracy of the parameter space
                     trimming 
             curves.
        """
        pass

    def GetTrimParameter(self, edgeParameter, trimParameter):
        """
        GetTrimParameter(self: BrepTrim, edgeParameter: float) -> (bool, float)
        
            Get corresponding trim parameter at given edge parameter.
            Returns: true on success
        """
        pass

    def IsReversed(self):
        """
        IsReversed(self: BrepTrim) -> bool
        
            Get orientation of trim with respect to it's corresponding edge.
            Returns: true if the 2d trim and 3d edge have opposite orientations
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def SetTolerances(self, toleranceU, toleranceV):
        """
        SetTolerances(self: BrepTrim, toleranceU: float, toleranceV: float)
            The values in tolerance[] record the accuracy of the parameter space
                     trimming 
             curves.
        """
        pass

    def SetTrimCurve(self, curve2dIndex, subDomain=None):
        """
        SetTrimCurve(self: BrepTrim, curve2dIndex: int, subDomain: Interval) -> bool
        
            Set 2d curve geometry used by a b-rep trim.
        
            curve2dIndex: index of 2d curve in m_C2[] array
            Returns: true if successful
        SetTrimCurve(self: BrepTrim, curve2dIndex: int) -> bool
        
            Set 2d curve geometry used by a b-rep trim.
        
            curve2dIndex: index of 2d curve in m_C2[] array
            Returns: true if successful
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

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Brep that owns this trim.

Get: Brep(self: BrepTrim) -> Brep

"""

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Brep edge this trim belongs to. This will be null for singular trims

Get: Edge(self: BrepTrim) -> BrepEdge

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Brep face this trim belongs to

Get: Face(self: BrepTrim) -> BrepFace

"""

    IsoStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsoStatus(self: BrepTrim) -> IsoStatus

Set: IsoStatus(self: BrepTrim) = value
"""

    Loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Loop that this trim belongs to

Get: Loop(self: BrepTrim) -> BrepLoop

"""

    TrimIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this trim in the Brep.Trims collection.

Get: TrimIndex(self: BrepTrim) -> int

"""

    TrimType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of trim

Get: TrimType(self: BrepTrim) -> BrepTrimType

Set: TrimType(self: BrepTrim) = value
"""



class BrepTrimType(Enum, IComparable, IFormattable, IConvertible):
    """
    Each brep trim has a defined type.
    
    enum BrepTrimType, values: Boundary (1), CurveOnSurface (5), Mated (2), PointOnSurface (6), Seam (3), Singular (4), Slit (7), Unknown (0)
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

    Boundary = None
    CurveOnSurface = None
    Mated = None
    PointOnSurface = None
    Seam = None
    Singular = None
    Slit = None
    Unknown = None
    value__ = None


class Point(GeometryBase, IDisposable, ISerializable):
    """
    Represents a geometric point.
                This is fundamentally a class that derives from
                Rhino.Geometry.GeometryBase and contains a single Rhino.Geometry.Point3d location.
    
    Point(location: Point3d)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, location):
        """
        __new__(cls: type, location: Point3d)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the location (position) of this point.

Get: Location(self: Point) -> Point3d

Set: Location(self: Point) = value
"""



class BrepVertex(Point, IDisposable, ISerializable):
    """ Brep vertex information """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def EdgeIndices(self):
        """
        EdgeIndices(self: BrepVertex) -> Array[int]
        
            Gets the indices of all edges associated with this vertex.
            Returns: Empty array on failure.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Brep that owns this vertex.

Get: Brep(self: BrepVertex) -> Brep

"""

    VertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this vertex in the Brep.Vertices collection.

Get: VertexIndex(self: BrepVertex) -> int

"""



class Circle(object, IEpsilonComparable[Circle]):
    """
    Represents a circle in 3D.
                The values used are a radius and an orthonormal frame	of the plane containing the circle,
                with origin at the center.The circle is parameterized by radians from 0 to 2 Pi given byt -> center + cos(t)*radius*xaxis + sin(t)*radius*yaxiswhere center, xaxis and yaxis define the orthonormal frame of the circle plane.
    
    Circle(radius: float)
    Circle(plane: Plane, radius: float)
    Circle(center: Point3d, radius: float)
    Circle(arc: Arc)
    Circle(point1: Point3d, point2: Point3d, point3: Point3d)
    Circle(plane: Plane, center: Point3d, radius: float)
    Circle(startPoint: Point3d, tangentAtP: Vector3d, pointOnCircle: Point3d)
    """
    def ClosestParameter(self, testPoint, t):
        """
        ClosestParameter(self: Circle, testPoint: Point3d) -> (bool, float)
        
            Gets the parameter on the circle which is closest to a test point.
        
            testPoint: Point to project onto the circle.
            Returns: true on success, false on failure.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: Circle, testPoint: Point3d) -> Point3d
        
            Gets the point on the circle which is closest to a test point.
        
            testPoint: Point to project onto the circle.
            Returns: The point on the circle that is closest to testPoint or
                    Point3d.Unset on failure.
        """
        pass

    def DerivativeAt(self, derivative, t):
        """
        DerivativeAt(self: Circle, derivative: int, t: float) -> Vector3d
        
            Determines the value of the Nth derivative at a parameter.
        
            derivative: Which order of derivative is wanted.
            t: Parameter to evaluate derivative. Valid values are 0, 1, 2 and 3.
            Returns: The derivative of the circle at the given parameter.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Circle, other: Circle, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def IsInPlane(self, plane, tolerance):
        """
        IsInPlane(self: Circle, plane: Plane, tolerance: float) -> bool
        
            Evaluates whether or not this circle is co-planar with a given plane.
        
            plane: Plane.
            tolerance: Tolerance to use.
            Returns: true if the circle plane is co-planar with the given plane within tolerance.
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Circle, t: float) -> Point3d
        
            Circles use trigonometric parameterization: 
                    t -> center + cos(t)*radius*xaxis + 
             sin(t)*radius*yaxis.
        
        
            t: Parameter of point to evaluate.
            Returns: The point on the circle at the given parameter.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Circle)
            Reverse the orientation of the circle. Changes the domain from [a,b]
                    to [-b,-a].
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Circle, angle: float, axis: Vector3d) -> bool
        
            Rotates the circle through a given angle.
        
            angle: Angle (in radians) of the rotation.
            axis: Rotation axis.
            Returns: true on success, false on failure.
        Rotate(self: Circle, angle: float, axis: Vector3d, point: Point3d) -> bool
        
            Rotates the circle through a given angle.
        
            angle: Angle (in radians) of the rotation.
            axis: Rotation axis.
            point: Rotation anchor point.
            Returns: true on success, false on failure.
        Rotate(self: Circle, sinAngle: float, cosAngle: float, axis: Vector3d) -> bool
        
            Rotates the circle around an axis that starts at the base plane origin.
        
            sinAngle: The value returned by Math.Sin(angle) to compose the rotation.
            cosAngle: The value returned by Math.Cos(angle) to compose the rotation.
            axis: A rotation axis.
            Returns: true on success, false on failure.
        Rotate(self: Circle, sinAngle: float, cosAngle: float, axis: Vector3d, point: Point3d) -> bool
        
            Rotates the circle around an axis that starts at the provided point.
        
            sinAngle: The value returned by Math.Sin(angle) to compose the rotation.
            cosAngle: The value returned by Math.Cos(angle) to compose the rotation.
            axis: A rotation direction.
            point: A rotation base point.
            Returns: true on success, false on failure.
        """
        pass

    def TangentAt(self, t):
        """
        TangentAt(self: Circle, t: float) -> Vector3d
        
            Circles use trigonometric parameterization: 
                    t -> center + cos(t)*radius*xaxis + 
             sin(t)*radius*yaxis.
        
        
            t: Parameter of tangent to evaluate.
            Returns: The tangent at the circle at the given parameter.
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Circle) -> NurbsCurve
        
            Constructs a nurbs curve representation of this circle. 
                    This amounts to the same 
             as calling NurbsCurve.CreateFromCircle().
        
            Returns: A nurbs curve representation of this circle or null if no such representation could be made.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Circle, xform: Transform) -> bool
        
            Transforms this circle using an xform matrix.
        
            xform: Transformation to apply.
            Returns: true on success, false on failure.
        """
        pass

    def Translate(self, delta):
        """
        Translate(self: Circle, delta: Vector3d) -> bool
        
            Moves the circle.
        
            delta: Translation vector.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def TryFitCircleTT(c1, c2, t1, t2):
        """
        TryFitCircleTT(c1: Curve, c2: Curve, t1: float, t2: float) -> Circle
        
            Try to fit a circle to two curves using tangent relationships.
        
            c1: First curve to touch.
            c2: Second curve to touch.
            t1: Parameter on first curve close to desired solution.
            t2: Parameter on second curve closet to desired solution.
            Returns: Valid circle on success, Circle.Unset on failure.
        """
        pass

    @staticmethod
    def TryFitCircleTTT(c1, c2, c3, t1, t2, t3):
        """
        TryFitCircleTTT(c1: Curve, c2: Curve, c3: Curve, t1: float, t2: float, t3: float) -> Circle
        
            Try to fit a circle to three curves using tangent relationships.
        
            c1: First curve to touch.
            c2: Second curve to touch.
            c3: Third curve to touch.
            t1: Parameter on first curve close to desired solution.
            t2: Parameter on second curve closet to desired solution.
            t3: Parameter on third curve close to desired solution.
            Returns: Valid circle on success, Circle.Unset on failure.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Circle]() -> Circle
        
        __new__(cls: type, radius: float)
        __new__(cls: type, plane: Plane, radius: float)
        __new__(cls: type, center: Point3d, radius: float)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, point1: Point3d, point2: Point3d, point3: Point3d)
        __new__(cls: type, plane: Plane, center: Point3d, radius: float)
        __new__(cls: type, startPoint: Point3d, tangentAtP: Vector3d, pointOnCircle: Point3d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the circle's 3d axis aligned bounding box.

Get: BoundingBox(self: Circle) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center point of this circle.

Get: Center(self: Circle) -> Point3d

Set: Center(self: Circle) = value
"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the circumference of this circle.

Get: Circumference(self: Circle) -> float

Set: Circumference(self: Circle) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the diameter (radius * 2.0) of this circle. 
            Diameters should be positive values.

Get: Diameter(self: Circle) -> float

Set: Diameter(self: Circle) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A valid circle has radius larger than 0.0 and a base plane which is must also be valid.

Get: IsValid(self: Circle) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the normal vector for this circle.

Get: Normal(self: Circle) -> Vector3d

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the plane of the circle.

Get: Plane(self: Circle) -> Plane

Set: Plane(self: Circle) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of this circle. 
            Radii should be positive values.

Get: Radius(self: Circle) -> float

Set: Radius(self: Circle) = value
"""


    Unset = None


class PlaneSurface(Surface, IDisposable, ISerializable):
    """
    Represents a plane surface, with plane and two intervals.
    
    PlaneSurface(plane: Plane, xExtents: Interval, yExtents: Interval)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def CreateThroughBox(*__args):
        """
        CreateThroughBox(plane: Plane, box: BoundingBox) -> PlaneSurface
        
            Extends a plane into a plane surface so that the latter goes through a bounding box.
        
            plane: An original plane value.
            box: A box to use for extension boundary.
            Returns: A new plane surface on success, or null on error.
        CreateThroughBox(lineInPlane: Line, vectorInPlane: Vector3d, box: BoundingBox) -> PlaneSurface
        
            Makes a plane that includes a line and a vector and goes through a bounding box.
        
            lineInPlane: A line that will lie on the plane.
            vectorInPlane: A vector the direction of which will be in plane.
            box: A box to cut through.
            Returns: A new plane surface on success, or null on error.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, plane, xExtents, yExtents):
        """
        __new__(cls: type, plane: Plane, xExtents: Interval, yExtents: Interval)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class ClippingPlaneSurface(PlaneSurface, IDisposable, ISerializable):
    """ Represents a planar surface that is used as clipping plane in viewports. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def ViewportIds(self):
        """
        ViewportIds(self: ClippingPlaneSurface) -> Array[Guid]
        
            Returns Ids of viewports that this clipping plane is supposed to clip.
            Returns: An array of globally unique ideantifiers (Guids) to the viewports.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clipping plane.

Get: Plane(self: ClippingPlaneSurface) -> Plane

Set: Plane(self: ClippingPlaneSurface) = value
"""



class ComponentIndex(object):
    """
    Represents an index of an element contained in another object.
    
    ComponentIndex(type: ComponentIndexType, index: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, type, index):
        """
        __new__[ComponentIndex]() -> ComponentIndex
        
        __new__(cls: type, type: ComponentIndexType, index: int)
        """
        pass

    ComponentIndexType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The interpretation of Index depends on the Type value.
            Type             m_index interpretation (0 based indices)
            no_type            used when context makes it clear what array is being index
            brep_vertex        Brep.m_V[] array index
            brep_edge          Brep.m_E[] array index
            brep_face          Brep.m_F[] array index
            brep_trim          Brep.m_T[] array index
            brep_loop          Brep.m_L[] array index
            mesh_vertex        Mesh.m_V[] array index
            meshtop_vertex     MeshTopology.m_topv[] array index
            meshtop_edge       MeshTopology.m_tope[] array index
            mesh_face          Mesh.m_F[] array index
            idef_part          InstanceDefinition.m_object_uuid[] array index
            polycurve_segment  PolyCurve::m_segment[] array index
            dim_linear_point   LinearDimension2::POINT_INDEX
            dim_radial_point   RadialDimension2::POINT_INDEX
            dim_angular_point  AngularDimension2::POINT_INDEX
            dim_ordinate_point OrdinateDimension2::POINT_INDEX
            dim_text_point     TextEntity2 origin point.

Get: ComponentIndexType(self: ComponentIndex) -> ComponentIndexType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The interpretation of m_index depends on the m_type value.
            m_type             m_index interpretation (0 based indices)
            no_type            used when context makes it clear what array is being index
            brep_vertex        Brep.m_V[] array index
            brep_edge          Brep.m_E[] array index
            brep_face          Brep.m_F[] array index
            brep_trim          Brep.m_T[] array index
            brep_loop          Brep.m_L[] array index
            mesh_vertex        Mesh.m_V[] array index
            meshtop_vertex     MeshTopology.m_topv[] array index
            meshtop_edge       MeshTopology.m_tope[] array index
            mesh_face          Mesh.m_F[] array index
            idef_part          InstanceDefinition.m_object_uuid[] array index
            polycurve_segment  PolyCurve::m_segment[] array index
            dim_linear_point   LinearDimension2::POINT_INDEX
            dim_radial_point   RadialDimension2::POINT_INDEX
            dim_angular_point  AngularDimension2::POINT_INDEX
            dim_ordinate_point OrdinateDimension2::POINT_INDEX
            dim_text_point     TextEntity2 origin point.

Get: Index(self: ComponentIndex) -> int

"""


    Unset = None


class ComponentIndexType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values to represent component index types.
    
    enum ComponentIndexType, values: BrepEdge (2), BrepFace (3), BrepLoop (5), BrepTrim (4), BrepVertex (1), DimAngularPoint (102), DimLinearPoint (100), DimOrdinatePoint (103), DimRadialPoint (101), DimTextPoint (104), GroupMember (51), InstanceDefinitionPart (21), InvalidType (0), MeshFace (14), MeshTopologyEdge (13), MeshTopologyVertex (12), MeshVertex (11), NoType (268435455), PointCloudPoint (41), PolycurveSegment (31)
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

    BrepEdge = None
    BrepFace = None
    BrepLoop = None
    BrepTrim = None
    BrepVertex = None
    DimAngularPoint = None
    DimLinearPoint = None
    DimOrdinatePoint = None
    DimRadialPoint = None
    DimTextPoint = None
    GroupMember = None
    InstanceDefinitionPart = None
    InvalidType = None
    MeshFace = None
    MeshTopologyEdge = None
    MeshTopologyVertex = None
    MeshVertex = None
    NoType = None
    PointCloudPoint = None
    PolycurveSegment = None
    value__ = None


class Cone(object, IEpsilonComparable[Cone]):
    """
    Represents the center plane, radius and height values in a right circular cone.
    
    Cone(plane: Plane, height: float, radius: float)
    """
    def AngleInDegrees(self):
        """
        AngleInDegrees(self: Cone) -> float
        
            Computes the angle (in degrees) between the axis and the 
                    side of the cone.
               
                  The angle and the height have the same sign.
        
            Returns: An angle in degrees.
        """
        pass

    def AngleInRadians(self):
        """
        AngleInRadians(self: Cone) -> float
        
            Computes the angle (in radians) between the axis and the 
                    side of the cone.
               
                  The angle and the height have the same sign.
        
            Returns: Math.Atan(Radius / Height) if the height is not 0; 0 if the radius is 0; Math.PI otherwise.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Cone, other: Cone, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def ToBrep(self, capBottom):
        """
        ToBrep(self: Cone, capBottom: bool) -> Brep
        
            Gets a Brep representation of the cone with a single
                    face for the cone, an edge 
             along the cone seam, 
                    and vertices at the base and apex ends of this seam edge.
           
                      The optional cap is a single face with one circular edge 
                    starting and 
             ending at the base vertex.
        
        
            capBottom: true if the bottom should be filled with a surface. false otherwise.
            Returns: A brep (polysurface) representation of this cone values.
        """
        pass

    def ToNurbsSurface(self):
        """
        ToNurbsSurface(self: Cone) -> NurbsSurface
        
            Constructs a Nurbs surface representation of this Cone. 
                    This is synonymous with 
             calling NurbsSurface.CreateFromCone().
        
            Returns: A Nurbs surface representation of the cone or null.
        """
        pass

    def ToRevSurface(self):
        """
        ToRevSurface(self: Cone) -> RevSurface
        
            Constructs a RevSurface representation of this Cone. 
                    This is synonymous with 
             calling RevSurface.CreateFromCone().
        
            Returns: A RevSurface representation of the cone or null.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, height, radius):
        """
        __new__[Cone]() -> Cone
        
        __new__(cls: type, plane: Plane, height: float, radius: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApexPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Point at tip of the cone.

Get: ApexPoint(self: Cone) -> Point3d

"""

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit vector axis of cone.

Get: Axis(self: Cone) -> Vector3d

"""

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Center of base circle.

Get: BasePoint(self: Cone) -> Point3d

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the circular right cone.

Get: Height(self: Cone) -> float

Set: Height(self: Cone) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if plane is valid, height is not zero and radius is not zero.

Get: IsValid(self: Cone) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base plane of the cone.

Get: Plane(self: Cone) -> Plane

Set: Plane(self: Cone) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the cone.

Get: Radius(self: Cone) -> float

Set: Radius(self: Cone) = value
"""


    Unset = None


class Continuity(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides enumerated values for continuity along geometry,
                such as continuous first derivative or continuous unit tangent and curvature.
    
    enum Continuity, values: C0_continuous (1), C0_locus_continuous (6), C1_continuous (2), C1_locus_continuous (7), C2_continuous (3), C2_locus_continuous (8), Cinfinity_continuous (11), G1_continuous (4), G1_locus_continuous (9), G2_continuous (5), G2_locus_continuous (10), None (0)
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

    C0_continuous = None
    C0_locus_continuous = None
    C1_continuous = None
    C1_locus_continuous = None
    C2_continuous = None
    C2_locus_continuous = None
    Cinfinity_continuous = None
    G1_continuous = None
    G1_locus_continuous = None
    G2_continuous = None
    G2_locus_continuous = None
    None = None
    value__ = None


class ControlPoint(object, IEpsilonComparable[ControlPoint]):
    """
    Represents control-point geometry with three-dimensional position and weight.
    
    ControlPoint(x: float, y: float, z: float)
    ControlPoint(x: float, y: float, z: float, weight: float)
    ControlPoint(pt: Point3d)
    ControlPoint(pt: Point3d, weight: float)
    ControlPoint(pt: Point4d)
    """
    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: ControlPoint, other: ControlPoint, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ControlPoint]() -> ControlPoint
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, x: float, y: float, z: float, weight: float)
        __new__(cls: type, pt: Point3d)
        __new__(cls: type, pt: Point3d, weight: float)
        __new__(cls: type, pt: Point4d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the location of the control point. 
            Internally, Rhino stores the location of a weighted control-point 
            as a pre-multiplied coordinate, but RhinoCommon always provides 
            Euclidean coordinates for control-points, regardless of weight.

Get: Location(self: ControlPoint) -> Point3d

Set: Location(self: ControlPoint) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the weight of this control point.

Get: Weight(self: ControlPoint) -> float

Set: Weight(self: ControlPoint) = value
"""


    Unset = None


class CurveEnd(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the extremes of a curve through a flagged enumeration.
    
    enum (flags) CurveEnd, values: Both (3), End (2), None (0), Start (1)
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

    Both = None
    End = None
    None = None
    Start = None
    value__ = None


class CurveEvaluationSide(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for the options that defines a curve evaluation side when evaluating kinks.
    
    enum CurveEvaluationSide, values: Above (1), Below (-1), Default (0)
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

    Above = None
    Below = None
    Default = None
    value__ = None


class CurveExtensionStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for styles to use during curve extension, such as "Line", "Arc" or "Smooth".
    
    enum CurveExtensionStyle, values: Arc (1), Line (0), Smooth (2)
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

    Arc = None
    Line = None
    Smooth = None
    value__ = None


class CurveKnotStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for knot spacing styles in interpolated curves.
    
    enum CurveKnotStyle, values: Chord (1), ChordPeriodic (4), ChordSquareRoot (2), ChordSquareRootPeriodic (5), Uniform (0), UniformPeriodic (3)
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

    Chord = None
    ChordPeriodic = None
    ChordSquareRoot = None
    ChordSquareRootPeriodic = None
    Uniform = None
    UniformPeriodic = None
    value__ = None


class CurveOffsetCornerStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for all implemented corner styles in curve offsets.
    
    enum CurveOffsetCornerStyle, values: Chamfer (4), None (0), Round (2), Sharp (1), Smooth (3)
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

    Chamfer = None
    None = None
    Round = None
    Sharp = None
    Smooth = None
    value__ = None


class CurveOrientation(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for closed curve orientations.
    
    enum CurveOrientation, values: Clockwise (-1), CounterClockwise (1), Undefined (0)
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

    Clockwise = None
    CounterClockwise = None
    Undefined = None
    value__ = None


class CurveSimplifyOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates the options to use when simplifying a curve.
    
    enum (flags) CurveSimplifyOptions, values: AdjustG1 (16), All (63), Merge (32), None (0), RebuildArcs (4), RebuildLines (2), RebuildRationals (8), SplitAtFullyMultipleKnots (1)
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

    AdjustG1 = None
    All = None
    Merge = None
    None = None
    RebuildArcs = None
    RebuildLines = None
    RebuildRationals = None
    SplitAtFullyMultipleKnots = None
    value__ = None


class Cylinder(object, IEpsilonComparable[Cylinder]):
    """
    Represents the values of a plane, a radius and two heights -on top and beneath-
                that define a right circular cylinder.
    
    Cylinder(baseCircle: Circle)
    Cylinder(baseCircle: Circle, height: float)
    """
    def CircleAt(self, linearParameter):
        """
        CircleAt(self: Cylinder, linearParameter: float) -> Circle
        
            Compute the circle at the given elevation parameter.
        
            linearParameter: Height parameter for circle section.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Cylinder, other: Cylinder, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def LineAt(self, angularParameter):
        """
        LineAt(self: Cylinder, angularParameter: float) -> Line
        
            Compute the line at the given angle parameter. This line will be degenerate if the cylinder is 
             infite.
        
        
            angularParameter: Angle parameter for line section.
        """
        pass

    def ToBrep(self, capBottom, capTop):
        """
        ToBrep(self: Cylinder, capBottom: bool, capTop: bool) -> Brep
        
            Constructs a Brep representation of this Cylinder. 
                    This is synonymous with calling 
             NurbsSurface.CreateFromCylinder().
        
        
            capBottom: If true, the bottom of the cylinder will be capped.
            capTop: If true, the top of the cylinder will be capped.
            Returns: A Brep representation of the cylinder or null.
        """
        pass

    def ToNurbsSurface(self):
        """
        ToNurbsSurface(self: Cylinder) -> NurbsSurface
        
            Constructs a Nurbs surface representation of this cylinder. 
                    This is synonymous 
             with calling NurbsSurface.CreateFromCylinder().
        
            Returns: A Nurbs surface representation of the cylinder or null.
        """
        pass

    def ToRevSurface(self):
        """
        ToRevSurface(self: Cylinder) -> RevSurface
        
            Constructs a RevSurface representation of this Cylinder. 
                    This is synonymous with 
             calling RevSurface.CreateFromCylinder().
        
            Returns: A RevSurface representation of the cylinder or null.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, baseCircle, height=None):
        """
        __new__[Cylinder]() -> Cylinder
        
        __new__(cls: type, baseCircle: Circle)
        __new__(cls: type, baseCircle: Circle, height: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the axis direction of the cylinder.

Get: Axis(self: Cylinder) -> Vector3d

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the center point of the defining circle.

Get: Center(self: Cylinder) -> Point3d

"""

    Height1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the start height of the cylinder.

Get: Height1(self: Cylinder) -> float

Set: Height1(self: Cylinder) = value
"""

    Height2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the end height of the cylinder. 
            If the end height equals the start height, the cylinder is 
            presumed to be infinite.

Get: Height2(self: Cylinder) -> float

Set: Height2(self: Cylinder) = value
"""

    IsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the cylinder is finite (Height0 != Height1)
            false if the cylinder is infinite.

Get: IsFinite(self: Cylinder) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a boolean value indicating whether this cylinder is valid.
            A valid cylinder is represented by a valid circle and two valid heights.

Get: IsValid(self: Cylinder) -> bool

"""

    TotalHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the cylinder. 
            Infinite cylinders have a height of zero, not Double.PositiveInfinity.

Get: TotalHeight(self: Cylinder) -> float

"""


    Unset = None


class DetailView(GeometryBase, IDisposable, ISerializable):
    """ Represents a view of the model placed on a page layout. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def SetScale(self, modelLength, modelUnits, pageLength, pageUnits):
        """
        SetScale(self: DetailView, modelLength: float, modelUnits: UnitSystem, pageLength: float, pageUnits: UnitSystem) -> bool
        
            Sets the detail viewport's projection so geometry is displayed at a certain scale.
        
            modelLength: Reference model length.
            modelUnits: Units for model length.
            pageLength: Length on page that the modelLength should equal.
            pageUnits: Units for page length.
            Returns: true on success. false if the DetailView projection is perspective or input values are 
             incongruous.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsParallelProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the view is parallel.

Get: IsParallelProjection(self: DetailView) -> bool

Set: IsParallelProjection(self: DetailView) = value
"""

    IsPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the view is perspective.

Get: IsPerspectiveProjection(self: DetailView) -> bool

Set: IsPerspectiveProjection(self: DetailView) = value
"""

    IsProjectionLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the view projection is locked.

Get: IsProjectionLocked(self: DetailView) -> bool

Set: IsProjectionLocked(self: DetailView) = value
"""

    PageToModelRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page units/model units quotient.

Get: PageToModelRatio(self: DetailView) -> float

"""



class EdgeAdjacency(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all possible Topological Edge adjacency types.
    
    enum EdgeAdjacency, values: Interior (2), Naked (1), None (0), NonManifold (3)
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

    Interior = None
    Naked = None
    None = None
    NonManifold = None
    value__ = None


class Ellipse(object, IEpsilonComparable[Ellipse]):
    """
    Represents the values of a plane and the two semiaxes radii in an ellipse.
    
    Ellipse(plane: Plane, radius1: float, radius2: float)
    Ellipse(center: Point3d, second: Point3d, third: Point3d)
    """
    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Ellipse, other: Ellipse, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Ellipse) -> NurbsCurve
        
            Constructs a nurbs curve representation of this ellipse. 
                    This is equivalent to 
             calling NurbsCurve.CreateFromEllipse().
        
            Returns: A nurbs curve representation of this ellipse or null if no such representation could be made.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Ellipse]() -> Ellipse
        
        __new__(cls: type, plane: Plane, radius1: float, radius2: float)
        __new__(cls: type, center: Point3d, second: Point3d, third: Point3d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base plane of the ellipse.

Get: Plane(self: Ellipse) -> Plane

Set: Plane(self: Ellipse) = value
"""

    Radius1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the ellipse along the base plane X semiaxis.

Get: Radius1(self: Ellipse) -> float

Set: Radius1(self: Ellipse) = value
"""

    Radius2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the ellipse along the base plane Y semiaxis.

Get: Radius2(self: Ellipse) -> float

Set: Radius2(self: Ellipse) = value
"""



class ExtrudeCornerType(Enum, IComparable, IFormattable, IConvertible):
    """
    Corner types used for creating a tapered extrusion
    
    enum ExtrudeCornerType, values: Chamfer (4), None (0), Round (2), Sharp (1), Smooth (3)
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

    Chamfer = None
    None = None
    Round = None
    Sharp = None
    Smooth = None
    value__ = None


class Extrusion(Surface, IDisposable, ISerializable):
    """
    Represents an extrusion, or objects such as beams or linearly extruded elements,
                that can be represented by profile curves and two miter planes at the extremes.
    
    Extrusion()
    """
    def AddInnerProfile(self, innerProfile):
        """
        AddInnerProfile(self: Extrusion, innerProfile: Curve) -> bool
        
            Adds an inner profile.
        
            innerProfile: Closed curve in the XY plane or a 2d curve.
            Returns: true if the profile was set.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def Create(planarCurve, height, cap):
        """
        Create(planarCurve: Curve, height: float, cap: bool) -> Extrusion
        
            Creates an extrusion of a 3d curve (which must be planar) and a height.
        
            planarCurve: Planar curve used as profile
            height: If the height > 0, the bottom of the extrusion will be in plane and
                    the top will be 
             height units above the plane.
                    If the height < 0, the top of the extrusion will be 
             in plane and
                    the bottom will be height units below the plane.
                    The 
             plane used is the one that is returned from the curve's TryGetPlane function.
        
            cap: If the curve is closed and cap is true, then the resulting extrusion is capped.
            Returns: If the input is valid, then a new extrusion is returned. Otherwise null is returned
        """
        pass

    @staticmethod
    def CreateCylinderExtrusion(cylinder, capBottom, capTop):
        """
        CreateCylinderExtrusion(cylinder: Cylinder, capBottom: bool, capTop: bool) -> Extrusion
        
            Gets an extrusion form of a cylinder.
        
            cylinder: IsFinite must be true.
            capBottom: If true, the end at cylinder.Height1 will be capped.
            capTop: If true, the end at cylinder.Height2 will be capped.
            Returns: Extrusion on success. null on failure.
        """
        pass

    @staticmethod
    def CreatePipeExtrusion(cylinder, otherRadius, capTop, capBottom):
        """
        CreatePipeExtrusion(cylinder: Cylinder, otherRadius: float, capTop: bool, capBottom: bool) -> Extrusion
        
            Gets an extrusion form of a pipe.
        
            cylinder: IsFinite must be true.
            otherRadius: If cylinder.Radius is less than other radius, then the cylinder will be the inside
                    
             of the pipe.
        
            capTop: If true, the end at cylinder.Height2 will be capped.
            capBottom: If true, the end at cylinder.Height1 will be capped.
            Returns: Extrusion on success. null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def GetMesh(self, meshType):
        """
        GetMesh(self: Extrusion, meshType: MeshType) -> Mesh
        
            Obtains a reference to a specified type of mesh for this extrusion.
        
            meshType: The mesh type.
            Returns: A mesh.
        """
        pass

    def GetPathPlane(self, s):
        """
        GetPathPlane(self: Extrusion, s: float) -> Plane
        
            Gets the 3D plane perpendicular to the path at a normalized path parameter.
        
            s: 0.0 = starting profile
                    1.0 = ending profile.
            Returns: A plane. The plane is Invalid on failure.
        """
        pass

    def GetProfilePlane(self, s):
        """
        GetProfilePlane(self: Extrusion, s: float) -> Plane
        
            Gets the 3D plane containing the profile curve at a normalized path parameter.
        
            s: 0.0 = starting profile
                    1.0 = ending profile.
            Returns: A plane. The plane is Invalid on failure.
        """
        pass

    def GetProfileTransformation(self, s):
        """
        GetProfileTransformation(self: Extrusion, s: float) -> Transform
        
            Gets the transformation that maps the xy profile curve to its 3d location.
        
            s: 0.0 = starting profile
                    1.0 = ending profile.
            Returns: A Transformation. The transform is Invalid on failure.
        """
        pass

    def GetWireframe(self):
        """
        GetWireframe(self: Extrusion) -> Array[Curve]
        
            Constructs all the Wireframe curves for this Extrusion.
            Returns: An array of Wireframe curves.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def PathLineCurve(self):
        """
        PathLineCurve(self: Extrusion) -> LineCurve
        
            Gets the line-like curve that is the conceptual axis of the extrusion.
            Returns: The path as a line curve.
        """
        pass

    def Profile3d(self, *__args):
        """
        Profile3d(self: Extrusion, ci: ComponentIndex) -> Curve
        
            Gets one of the profiles.
        
            ci: The index of this profile.
            Returns: The profile.
        Profile3d(self: Extrusion, profileIndex: int, s: float) -> Curve
        
            Gets a transversal isocurve of the extruded profile.
        
            profileIndex: 0 <= profileIndex < ProfileCount
                    The outer profile has index 0.
            s: 0.0 <= s <= 1.0
                    A relative parameter controling which profile is returned.
                
                 0 = bottom profile and 1 = top profile.
        
            Returns: The profile.
        """
        pass

    def ProfileIndex(self, profileParameter):
        """
        ProfileIndex(self: Extrusion, profileParameter: float) -> int
        
            Gets the index of the profile curve at a domain related to a parameter.
        
            profileParameter: Parameter on profile curve.
            Returns: -1 if profileParameter does not correspond to a point on the profile curve.
                    When 
             the profileParameter corresponds to the end of one profile and the
                    beginning of the 
             next profile, the index of the next profile is returned.
        """
        pass

    def SetOuterProfile(self, outerProfile, cap):
        """
        SetOuterProfile(self: Extrusion, outerProfile: Curve, cap: bool) -> bool
        
            Sets the outer profile of the extrusion.
        
            outerProfile: curve in the XY plane or a 2D curve.
            cap: If outerProfile is a closed curve, then cap determines if the extrusion
                    has end 
             caps. If outerProfile is an open curve, cap is ignored.
        
            Returns: true if the profile was set. If the outer profile is closed, then the
                    extrusion may 
             also have inner profiles. If the outer profile is open,
                    the extrusion may not have 
             inner profiles. If the extrusion already
                    has a profile, the set will fail.
        """
        pass

    def SetPathAndUp(self, a, b, up):
        """
        SetPathAndUp(self: Extrusion, a: Point3d, b: Point3d, up: Vector3d) -> bool
        
            Allows to set the two points at the extremes and the up vector.
        
            a: The start point.
            b: The end point.
            up: The up vector.
            Returns: true if the operation succeeded; otherwise false.
                    Setting up=a-b will make the 
             operation fail.
        """
        pass

    def ToBrep(self, splitKinkyFaces=None):
        """
        ToBrep(self: Extrusion, splitKinkyFaces: bool) -> Brep
        
            Constructs a brep form of the extrusion. The outer profile is always the first face of the brep.
             
                    If there are inner profiles, additional brep faces are created for each profile. If 
             the
                    outer profile is closed, then end caps are added as the last two faces of the 
             brep.
        
        
            splitKinkyFaces: If true and the profiles have kinks, then the faces corresponding to those profiles are split
          
                       so they will be G1.
        
            Returns: A brep with a similar shape like this extrustion, or null on error.
        """
        pass

    def WallEdge(self, ci):
        """
        WallEdge(self: Extrusion, ci: ComponentIndex) -> Curve
        
            Gets one of the longitudinal curves along the beam or extrusion.
        
            ci: The index of this profile.
            Returns: The profile.
        """
        pass

    def WallSurface(self, ci):
        """
        WallSurface(self: Extrusion, ci: ComponentIndex) -> Surface
        
            Gets one of the longitudinal surfaces of the extrusion.
        
            ci: The index specifying which precise item to retrieve.
            Returns: The surface.
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
    def __new__(self):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CapCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of capping surfaces.

Get: CapCount(self: Extrusion) -> int

"""

    IsCappedAtBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the surface that fills the bottom profile is existing.

Get: IsCappedAtBottom(self: Extrusion) -> bool

"""

    IsCappedAtTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the surface that fills the top profile is existing.

Get: IsCappedAtTop(self: Extrusion) -> bool

"""

    IsMiteredAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a miter plane at the end is defined.

Get: IsMiteredAtEnd(self: Extrusion) -> bool

"""

    IsMiteredAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a value indicating whether a miter plane at start is defined.

Get: IsMiteredAtStart(self: Extrusion) -> bool

"""

    IsSolid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether there is no gap among all surfaces constructing this object.

Get: IsSolid(self: Extrusion) -> bool

"""

    MiterPlaneNormalAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the normal of the miter plane at the end in profile coordinates.
            In profile coordinates, 0,0,1 always maps to the extrusion axis

Get: MiterPlaneNormalAtEnd(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtEnd(self: Extrusion) = value
"""

    MiterPlaneNormalAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the normal of the miter plane at the start in profile coordinates.
            In profile coordinates, 0,0,1 always maps to the extrusion axis

Get: MiterPlaneNormalAtStart(self: Extrusion) -> Vector3d

Set: MiterPlaneNormalAtStart(self: Extrusion) = value
"""

    PathEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end point of the path.

Get: PathEnd(self: Extrusion) -> Point3d

"""

    PathStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start point of the path.

Get: PathStart(self: Extrusion) -> Point3d

"""

    PathTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the up vector of the path.

Get: PathTangent(self: Extrusion) -> Vector3d

"""

    ProfileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of profile curves.

Get: ProfileCount(self: Extrusion) -> int

"""



class Hatch(GeometryBase, IDisposable, ISerializable):
    """
    Represents a hatch in planar boundary loop or loops.
                This is a 2d entity with a plane defining a local coordinate system.
                The loops, patterns, angles, etc are all in this local coordinate system.
                The Hatch object manages the plane and loop array
                Fill definitions are in the HatchPattern or class derived from HatchPattern
                Hatch has an index to get the pattern definition from the pattern table.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(curve: Curve, hatchPatternIndex: int, rotationRadians: float, scale: float) -> Array[Hatch]
        
            Constructs an array of Rhino.Geometry.Hatchhatches from one curve.
        
            curve: A Rhino.Geometry.Curve.
            hatchPatternIndex: The index of the hatch pattern in the document hatch pattern table.
            rotationRadians: The relative rotation of the pattern.
            scale: A scaling factor.
            Returns: An array of hatches. The array might be empty on error.
        Create(curves: IEnumerable[Curve], hatchPatternIndex: int, rotationRadians: float, scale: float) -> Array[Hatch]
        """
        pass

    def CreateDisplayGeometry(self, pattern, patternScale, bounds, lines, solidBrep):
        """
        CreateDisplayGeometry(self: Hatch, pattern: HatchPattern, patternScale: float) -> (Array[Curve], Array[Line], Brep)
        
            Generate geometry that would be used to draw the hatch with a given hatch pattern
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Explode(self):
        """
        Explode(self: Hatch) -> Array[GeometryBase]
        
            Decomposes the hatch pattern into an array of geometry.
            Returns: An array of geometry that formed the appearance of the original elements.
        """
        pass

    def Get3dCurves(self, outer):
        """
        Get3dCurves(self: Hatch, outer: bool) -> Array[Curve]
        
            Gets 3d curves that define the boundaries of the hatch
        
            outer: true to get the outer curves, false to get the inner curves
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    PatternIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of the pattern in the document hatch pattern table.

Get: PatternIndex(self: Hatch) -> int

Set: PatternIndex(self: Hatch) = value
"""

    PatternRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the relative rotation of the pattern.

Get: PatternRotation(self: Hatch) -> float

Set: PatternRotation(self: Hatch) = value
"""

    PatternScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scaling factor of the pattern.

Get: PatternScale(self: Hatch) -> float

Set: PatternScale(self: Hatch) = value
"""



class InstanceDefinitionGeometry(GeometryBase, IDisposable, ISerializable):
    """
    Represents the geometry in a block definition.
    
    InstanceDefinitionGeometry()
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def GetObjectIds(self):
        """
        GetObjectIds(self: InstanceDefinitionGeometry) -> Array[Guid]
        
            list of object ids in the instance geometry table
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    """Gets or sets the description of the definition.

Get: Description(self: InstanceDefinitionGeometry) -> str

Set: Description(self: InstanceDefinitionGeometry) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unique id for this instance definition

Get: Id(self: InstanceDefinitionGeometry) -> Guid

Set: Id(self: InstanceDefinitionGeometry) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the definition.

Get: Name(self: InstanceDefinitionGeometry) -> str

Set: Name(self: InstanceDefinitionGeometry) = value
"""



class InstanceReferenceGeometry(GeometryBase, IDisposable, ISerializable):
    """
    Represents a reference to the geometry in a block definition.
    
    InstanceReferenceGeometry(instanceDefinitionId: Guid, transform: Transform)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, instanceDefinitionId, transform):
        """ __new__(cls: type, instanceDefinitionId: Guid, transform: Transform) """
        pass

    ParentIdefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique id for the parent instance definition of this instance reference.

Get: ParentIdefId(self: InstanceReferenceGeometry) -> Guid

"""

    Xform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transformation for this reference.

Get: Xform(self: InstanceReferenceGeometry) -> Transform

"""



class Interpolator(RhinoList[float], IList[float], ICollection[float], IEnumerable[float], IEnumerable, IList, ICollection):
    """
    Exposes a set of standard numeric interpolation algorithms.
    
    Interpolator()
    Interpolator(initialCapacity: int)
    Interpolator(list: RhinoList[float])
    Interpolator(collection: IEnumerable[float])
    Interpolator(amount: int, defaultValue: float)
    """
    def InterpolateCatmullRom(self, t):
        """
        InterpolateCatmullRom(self: Interpolator, t: float) -> float
        
            Sample the list of numbers with Catmull-Rom interpolation.
        
            t: Parameter to sample at. The integer portion of the parameter 
                    indicates the index 
             of the left-hand value. If this Interpolator is cyclical, 
                    parameters will be 
             wrapped.
        
            Returns: The sampled value at t.
        """
        pass

    def InterpolateCosine(self, t):
        """
        InterpolateCosine(self: Interpolator, t: float) -> float
        
            Sample the list of numbers with cosine interpolation.
        
            t: Parameter to sample at. The integer portion of the parameter 
                    indicates the index 
             of the left-hand value. If this Interpolator is cyclical, 
                    parameters will be 
             wrapped.
        
            Returns: The sampled value at t.
        """
        pass

    def InterpolateCubic(self, t):
        """
        InterpolateCubic(self: Interpolator, t: float) -> float
        
            Sample the list of numbers with cubic interpolation.
        
            t: Parameter to sample at. The integer portion of the parameter 
                    indicates the index 
             of the left-hand value. If this Interpolator is cyclical, 
                    parameters will be 
             wrapped.
        
            Returns: The sampled value at t.
        """
        pass

    def InterpolateLinear(self, t):
        """
        InterpolateLinear(self: Interpolator, t: float) -> float
        
            Sample the list of numbers with linear interpolation.
        
            t: Parameter to sample at. The integer portion of the parameter 
                    indicates the index 
             of the left-hand value. If this Interpolator is cyclical, 
                    parameters will be 
             wrapped.
        
            Returns: The sampled value at t.
        """
        pass

    def InterpolateNearestNeighbour(self, t):
        """
        InterpolateNearestNeighbour(self: Interpolator, t: float) -> float
        
            Sample the list of numbers with Nearest Neighbour interpolation.
        
            t: Parameter to sample at. The integer portion of the parameter 
                    indicates the index 
             of the left-hand value. If this Interpolator is cyclical, 
                    parameters will be 
             wrapped.
        
            Returns: The sampled value at t.
        """
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
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, list: RhinoList[float])
        __new__(cls: type, collection: IEnumerable[float])
        __new__(cls: type, amount: int, defaultValue: float)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Cyclical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether or not the values inside this Interpolator 
            are to be treated as cyclical (i.e. circular).

Get: Cyclical(self: Interpolator) -> bool

Set: Cyclical(self: Interpolator) = value
"""



class Interval(object, ISerializable, IEquatable[Interval], IComparable[Interval], IComparable, IEpsilonComparable[Interval]):
    """
    Represents an interval in one-dimensional space,
                that is defined as two extrema or bounds.
    
    Interval(t0: float, t1: float)
    Interval(other: Interval)
    """
    def CompareTo(self, other):
        """
        CompareTo(self: Interval, other: Interval) -> int
        
            Compares this Rhino.Geometry.Interval with another interval.
                     The lower bound has 
             first evaluation priority.
        
        
            other: The other Rhino.Geometry.Interval to compare with.
            Returns: 0: if this is identical to other-1: if this[0] < other[0]+1: if this[0] > other[0]-1: if this[0] 
             == other[0] and this[1] < other[1]+1: if this[0] == other[0] and this[1] > other[1].
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Interval, other: Interval, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Interval, other: Interval) -> bool
        
            Determines whether the specified Rhino.Geometry.Interval is equal to the current 
             Rhino.Geometry.Interval,
                    comparing by value.
        
        
            other: The other interval to compare with.
            Returns: true if obj is an Rhino.Geometry.Interval and has the same bounds; false otherwise.
        Equals(self: Interval, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current Rhino.Geometry.Interval,
        
                         comparing by value.
        
        
            obj: The other object to compare with.
            Returns: true if obj is an Rhino.Geometry.Interval and has the same bounds; false otherwise.
        """
        pass

    @staticmethod
    def FromIntersection(a, b):
        """
        FromIntersection(a: Interval, b: Interval) -> Interval
        
            Returns a new Interval that is the Intersection of the two input Intervals.
        
            a: The first input interval.
            b: The second input interval.
            Returns: If the intersection is not empty, then 
                    intersection = [max(a.Min(),b.Min()), 
             min(a.Max(),b.Max())]
                    The interval [ON.UnsetValue,ON.UnsetValue] is considered to 
             be
                    the empty set interval.  The result of any intersection involving an
                   
              empty set interval or disjoint intervals is the empty set interval.
        """
        pass

    @staticmethod
    def FromUnion(a, b):
        """
        FromUnion(a: Interval, b: Interval) -> Interval
        
            Returns a new Interval which contains both inputs.
        
            a: The first input interval.
            b: The second input interval.
            Returns: The union of an empty set and an increasing interval is the increasing interval.
                    
             The union of two empty sets is empty.The union of an empty set an a non-empty interval is the 
             non-empty interval.The union of two non-empty intervals is [min(a.Min(),b.Min()), 
             max(a.Max(),b.Max())]
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Interval) -> int
        
            Computes the hash code for this Rhino.Geometry.Interval object.
            Returns: A hash value that might be equal for two different Rhino.Geometry.Interval values.
        """
        pass

    def Grow(self, value):
        """
        Grow(self: Interval, value: float)
            Grows the Rhino.Geometry.Interval to include the given number.
        
            value: Number to include in this interval.
        """
        pass

    def IncludesInterval(self, interval, strict=None):
        """
        IncludesInterval(self: Interval, interval: Interval, strict: bool) -> bool
        
            Tests another interval for Interval inclusion.
        
            interval: Interval to test.
            strict: If true, the other interval must be fully on the inside of the Interval.
            Returns: true if the other interval is contained within the limits of this Interval; otherwise false.
        IncludesInterval(self: Interval, interval: Interval) -> bool
        
            Tests another interval for Interval inclusion.
        
            interval: Interval to test.
            Returns: true if the other interval is contained within or is coincident with the limits of this 
             Interval; otherwise false.
        """
        pass

    def IncludesParameter(self, t, strict=None):
        """
        IncludesParameter(self: Interval, t: float, strict: bool) -> bool
        
            Tests a parameter for Interval inclusion.
        
            t: Parameter to test.
            strict: If true, the parameter must be fully on the inside of the Interval.
            Returns: true if t is contained within the limits of this Interval.
        IncludesParameter(self: Interval, t: float) -> bool
        
            Tests a parameter for Interval inclusion.
        
            t: Parameter to test.
            Returns: true if t is contained within or is coincident with the limits of this Interval.
        """
        pass

    def MakeIncreasing(self):
        """
        MakeIncreasing(self: Interval)
            Ensures this Rhino.Geometry.Interval is either singleton or increasing.
        """
        pass

    def NormalizedIntervalAt(self, intervalParameter):
        """
        NormalizedIntervalAt(self: Interval, intervalParameter: Interval) -> Interval
        
            Converts interval value, or pair of values, to normalized parameter.
            Returns: Normalized parameter x so that min*(1.0-x) + max*x = intervalParameter.
        """
        pass

    def NormalizedParameterAt(self, intervalParameter):
        """
        NormalizedParameterAt(self: Interval, intervalParameter: float) -> float
        
            Converts interval value, or pair of values, to normalized parameter.
            Returns: Normalized parameter x so that min*(1.0-x) + max*x = intervalParameter.
        """
        pass

    def ParameterAt(self, normalizedParameter):
        """
        ParameterAt(self: Interval, normalizedParameter: float) -> float
        
            Converts normalized parameter to interval value, or pair of values.
            Returns: Interval parameter min*(1.0-normalizedParameter) + max*normalizedParameter.
        """
        pass

    def ParameterIntervalAt(self, normalizedInterval):
        """
        ParameterIntervalAt(self: Interval, normalizedInterval: Interval) -> Interval
        
            Converts normalized parameter to interval value, or pair of values.
            Returns: Interval parameter min*(1.0-normalizedParameter) + max*normalized_paramete.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Interval)
            Changes interval to [-T1, -T0].
        """
        pass

    def Swap(self):
        """
        Swap(self: Interval)
            Exchanges T0 and T1.
        """
        pass

    def ToString(self):
        """
        ToString(self: Interval) -> str
        
            Returns a string representation of this Rhino.Geometry.Interval.
            Returns: A string with T0,T1.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Interval]() -> Interval
        
        __new__(cls: type, t0: float, t1: float)
        __new__(cls: type, other: Interval)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(number: float, interval: Interval) -> Interval
        
            Shifts an interval by a specific amount (addition).
        
            number: The shifting value.
            interval: The interval to be used as a base.
            Returns: A new interval where T0 and T1 are summed with number.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(number: float, interval: Interval) -> Interval
        
            Shifts an interval by a specific amount (subtraction).
        
            number: The shifting value to subtract from (minuend).
            interval: The interval to be subtracted from (subtrahend).
            Returns: A new interval with [number-T0, number-T1].
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsDecreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if T[0] > T[1].

Get: IsDecreasing(self: Interval) -> bool

"""

    IsIncreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if T0 < T1.

Get: IsIncreasing(self: Interval) -> bool

"""

    IsSingleton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if T0 == T1 != ON.UnsetValue.

Get: IsSingleton(self: Interval) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this Interval is valid. 
            Valid intervals must contain valid numbers.

Get: IsValid(self: Interval) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signed length of the numeric range. 
            If the interval is decreasing, a negative length will be returned.

Get: Length(self: Interval) -> float

"""

    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the larger of T0 and T1.

Get: Max(self: Interval) -> float

"""

    Mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the average of T0 and T1.

Get: Mid(self: Interval) -> float

"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the smaller of T0 and T1.

Get: Min(self: Interval) -> float

"""

    T0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the lower bound of the Interval.

Get: T0(self: Interval) -> float

Set: T0(self: Interval) = value
"""

    T1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the upper bound of the Interval.

Get: T1(self: Interval) -> float

Set: T1(self: Interval) = value
"""


    Unset = None


class IsoStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for isoparametric curve direction on a surface, such as X or Y,
                and curve sides, such as North or West boundary.
                Note: odd values are all x-constant; even values > 0 are all y-constant.
    
    enum IsoStatus, values: East (5), None (0), North (6), South (4), West (3), X (1), Y (2)
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

    East = None
    None = None
    North = None
    South = None
    value__ = None
    West = None
    X = None
    Y = None


class Leader(AnnotationBase, IDisposable, ISerializable):
    """
    Represents a leader, or an annotation entity with text that resembles an arrow pointing to something.
                This class refers to the geometric element that is independent from the document.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Light(GeometryBase, IDisposable, ISerializable):
    """
    Represents a light that shines in the modeling space.
    
    Light()
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def CreateSunLight(*__args):
        """
        CreateSunLight(sun: Sun) -> Light
        
            Constructs a light which simulates a Rhino.Render.Sun.
        
            sun: A Sun object from the Rhino.Render namespace.
            Returns: A light.
        CreateSunLight(northAngleDegrees: float, when: DateTime, latitudeDegrees: float, longitudeDegrees: float) -> Light
        
            Constructs a light which simulates the Sun based on a given time and location on Earth.
        
            northAngleDegrees: The angle of North in degrees. North is the angle between positive World Y axis and model North, 
             as measured on World XY plane.
        
            when: The time of the measurement. The Kind property of DateTime specifies whether this is in local or 
             universal time.
                    Local and Undefined System.DateTimeKinddaytime kinds in this 
             argument are considered local.
        
            latitudeDegrees: The latitude, in degrees, of the location on Earth.
            longitudeDegrees: The longitude, in degrees, of the location on Earth.
            Returns: A newly constructed light object.
        CreateSunLight(northAngleDegrees: float, azimuthDegrees: float, altitudeDegrees: float) -> Light
        
            Constructs a light that represents the Sun.
        
            northAngleDegrees: The angle of North in degrees. North is the angle between positive World Y axis and model North, 
             as measured on World XY plane.
        
            azimuthDegrees: The Azimut angle value in degrees. Azimuth is the compass angle from North.
            altitudeDegrees: The Altitude angle in degrees. Altitude is the angle above the ground plane.
            Returns: A new sun light.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def GetAttenuation(self, d):
        """
        GetAttenuation(self: Light, d: float) -> float
        
            Gets the attenuation settings (ignored for "directional" and "ambient" lights).
                    
             attenuation = 1/(a0 + d*a1 + d^2*a2) where d = distance to light.
        
        
            d: The distance to evaluate.
            Returns: 0 if a0 + d*a1 + d^2*a2 <= 0.
        """
        pass

    def GetSpotLightRadii(self, innerRadius, outerRadius):
        """
        GetSpotLightRadii(self: Light) -> (bool, float, float)
        
            Gets the spot light radii.
            Returns: true if operation succeeded; otherwise, false.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def SetAttenuation(self, a0, a1, a2):
        """
        SetAttenuation(self: Light, a0: float, a1: float, a2: float)
            Sets the attenuation settings (ignored for "directional" and "ambient" lights).
                    
             attenuation = 1/(a0 + d*a1 + d^2*a2) where d = distance to light.
        
        
            a0: The new constant attenuation divisor term.
            a1: The new reverse linear attenuation divisor term.
            a2: The new reverse quadratic attenuation divisor term.
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ambient color.

Get: Ambient(self: Light) -> Color

Set: Ambient(self: Light) = value
"""

    AttenuationVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or Sets the attenuation vector.

Get: AttenuationVector(self: Light) -> Vector3d

Set: AttenuationVector(self: Light) = value
"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value, determined by LightStyle, that explains whether
            the camera diretions are relative to World or Camera spaces.

Get: CoordinateSystem(self: Light) -> CoordinateSystem

"""

    Diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the diffuse color.

Get: Diffuse(self: Light) -> Color

Set: Diffuse(self: Light) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vector direction of the camera.

Get: Direction(self: Light) -> Vector3d

Set: Direction(self: Light) = value
"""

    HotSpot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hot spot setting runs from 0.0 to 1.0 and is used to
            provides a linear interface for controling the focus or 
            concentration of a spotlight.
            A hot spot setting of 0.0 corresponds to a spot exponent of 128.
            A hot spot setting of 1.0 corresponds to a spot exponent of 0.0.

Get: HotSpot(self: Light) -> float

Set: HotSpot(self: Light) = value
"""

    Intensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the light intensity.

Get: Intensity(self: Light) -> float

Set: Intensity(self: Light) = value
"""

    IsDirectionalLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the light style
            is Rhino.Geometry.Light.LightStyle CameraDirectional or WorldDirectional.

Get: IsDirectionalLight(self: Light) -> bool

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that defines if the light is turned on (true) or off (false).

Get: IsEnabled(self: Light) -> bool

Set: IsEnabled(self: Light) = value
"""

    IsLinearLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the light style
            is Rhino.Geometry.Light.LightStyle WorldLinear.

Get: IsLinearLight(self: Light) -> bool

"""

    IsPointLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the light style
            is Rhino.Geometry.Light.LightStyle CameraPoint or WorldPoint.

Get: IsPointLight(self: Light) -> bool

"""

    IsRectangularLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the light style
            is Rhino.Geometry.Light.LightStyle WorldRectangular.

Get: IsRectangularLight(self: Light) -> bool

"""

    IsSpotLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the light style
            is Rhino.Geometry.Light.LightStyle CameraSpot or WorldSpot.

Get: IsSpotLight(self: Light) -> bool

"""

    IsSunLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this object is a Sun light.

Get: IsSunLight(self: Light) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height in linear and rectangular lights.
            (ignored for non-linear/rectangular lights.)

Get: Length(self: Light) -> Vector3d

Set: Length(self: Light) = value
"""

    LightStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a light style on this camera.

Get: LightStyle(self: Light) -> LightStyle

Set: LightStyle(self: Light) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the light or 3D position or location.

Get: Location(self: Light) -> Point3d

Set: Location(self: Light) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the spot light name.

Get: Name(self: Light) -> str

Set: Name(self: Light) = value
"""

    PerpendicularDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a perpendicular vector to the camera direction.

Get: PerpendicularDirection(self: Light) -> Vector3d

"""

    PowerCandela = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the light power in candelas (cd).

Get: PowerCandela(self: Light) -> float

Set: PowerCandela(self: Light) = value
"""

    PowerLumens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the light power in lumens (lm).

Get: PowerLumens(self: Light) -> float

Set: PowerLumens(self: Light) = value
"""

    PowerWatts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the light power in watts (W).

Get: PowerWatts(self: Light) -> float

Set: PowerWatts(self: Light) = value
"""

    Specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the specular color.

Get: Specular(self: Light) -> Color

Set: Specular(self: Light) = value
"""

    SpotAngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the spot angle in radians.
            Ignored for non-spot lights.angle = 0 to pi/2  (0 to 90 degrees).

Get: SpotAngleRadians(self: Light) -> float

Set: SpotAngleRadians(self: Light) = value
"""

    SpotExponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The spot exponent varies from 0.0 to 128.0 and provides
            an exponential interface for controling the focus or 
            concentration of a spotlight (like the 
            OpenGL GL_SPOT_EXPONENT parameter).  The spot exponent
            and hot spot parameters are linked; changing one will
            change the other.
            A hot spot setting of 0.0 corresponds to a spot exponent of 128.
            A hot spot setting of 1.0 corresponds to a spot exponent of 0.0.

Get: SpotExponent(self: Light) -> float

Set: SpotExponent(self: Light) = value
"""

    SpotLightShadowIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the spot light shadow intensity.
            (ignored for non-spot lights.)

Get: SpotLightShadowIntensity(self: Light) -> float

Set: SpotLightShadowIntensity(self: Light) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width in linear and rectangular lights.
            (ignored for non-linear/rectangular lights.)

Get: Width(self: Light) -> Vector3d

Set: Width(self: Light) = value
"""



class LightStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values to represent light styles or types, such as directional or spotlight.
    
    enum LightStyle, values: Ambient (10), CameraDirectional (4), CameraPoint (5), CameraSpot (6), None (0), WorldDirectional (7), WorldLinear (11), WorldPoint (8), WorldRectangular (12), WorldSpot (9)
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

    Ambient = None
    CameraDirectional = None
    CameraPoint = None
    CameraSpot = None
    None = None
    value__ = None
    WorldDirectional = None
    WorldLinear = None
    WorldPoint = None
    WorldRectangular = None
    WorldSpot = None


class Line(object, IEquatable[Line], IEpsilonComparable[Line]):
    """
    Represents the value of start and end points in a single line segment.
    
    Line(from: Point3d, to: Point3d)
    Line(start: Point3d, span: Vector3d)
    Line(start: Point3d, direction: Vector3d, length: float)
    Line(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
    """
    def ClosestParameter(self, testPoint):
        """
        ClosestParameter(self: Line, testPoint: Point3d) -> float
        
            Finds the parameter on the infinite line segment that is closest to a test point.
        
            testPoint: Point to project onto the line.
            Returns: The parameter on the line that is closest to testPoint.
        """
        pass

    def ClosestPoint(self, testPoint, limitToFiniteSegment):
        """
        ClosestPoint(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> Point3d
        
            Finds the point on the (in)finite line segment that is closest to a test point.
        
            testPoint: Point to project onto the line.
            limitToFiniteSegment: If true, the projection is limited to the finite line segment.
            Returns: The point on the (in)finite line that is closest to testPoint.
        """
        pass

    def DistanceTo(self, testPoint, limitToFiniteSegment):
        """
        DistanceTo(self: Line, testPoint: Point3d, limitToFiniteSegment: bool) -> float
        
            Compute the shortest distance between this line segment and a test point.
        
            testPoint: Point for distance computation.
            limitToFiniteSegment: If true, the distance is limited to the finite line segment.
            Returns: The shortest distance between this line segment and testPoint.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Line, other: Line, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Line, other: Line) -> bool
        
            Determines whether a line has the same value as this line.
        
            other: A line.
            Returns: true if other has the same coordinates as this; otherwise false.
        Equals(self: Line, obj: object) -> bool
        
            Determines whether an object is a line that has the same value as this line.
        
            obj: An object.
            Returns: true if obj is a Line and has the same coordinates as this; otherwise false.
        """
        pass

    def Extend(self, startLength, endLength):
        """
        Extend(self: Line, startLength: float, endLength: float) -> bool
        
            Extend the line by custom distances on both sides.
        
            startLength: Distance to extend the line at the start point. 
                    Positive distance result in longer 
             lines.
        
            endLength: Distance to extend the line at the end point. 
                    Positive distance result in longer 
             lines.
        
            Returns: true on success, false on failure.
        """
        pass

    def ExtendThroughBox(self, box, additionalLength=None):
        """
        ExtendThroughBox(self: Line, box: Box) -> bool
        
            Ensure the line extends all the way through a box. 
                    Note, this does not result in 
             the shortest possible line that overlaps the box.
        
        
            box: Box to extend through.
            Returns: true on success, false on failure.
        ExtendThroughBox(self: Line, box: Box, additionalLength: float) -> bool
        
            Ensure the line extends all the way through a box. 
                    Note, this does not result in 
             the shortest possible line that overlaps the box.
        
        
            box: Box to extend through.
            additionalLength: Additional length to append at both sides of the line.
            Returns: true on success, false on failure.
        ExtendThroughBox(self: Line, box: BoundingBox) -> bool
        
            Ensure the line extends all the way through a box. 
                    Note, this does not result in 
             the shortest possible line 
                    that overlaps the box.
        
        
            box: Box to extend through.
            Returns: true on success, false on failure.
        ExtendThroughBox(self: Line, box: BoundingBox, additionalLength: float) -> bool
        
            Ensure the line extends all the way through a box. 
                    Note, this does not result in 
             the shortest possible line that overlaps the box.
        
        
            box: Box to extend through.
            additionalLength: Additional length to append at both sides of the line.
            Returns: true on success, false on failure.
        """
        pass

    def Flip(self):
        """
        Flip(self: Line)
            Flip the endpoints of the line segment.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Line) -> int
        
            Computes a hash number that represents this line.
            Returns: A number that is not unique to the value of this line.
        """
        pass

    def MaximumDistanceTo(self, *__args):
        """
        MaximumDistanceTo(self: Line, testLine: Line) -> float
        
            Finds the largest distance between this line as a finite segment
                    and another finite 
             segment.
        
        
            testLine: A line to test.
            Returns: The maximum distance.
        MaximumDistanceTo(self: Line, testPoint: Point3d) -> float
        
            Finds the largest distance between this line as a finite segment
                    and a test point.
        
            testPoint: A point to test.
            Returns: The maximum distance.
        """
        pass

    def MinimumDistanceTo(self, *__args):
        """
        MinimumDistanceTo(self: Line, testLine: Line) -> float
        
            Finds the shortest distance between this line as a finite segment
                    and another 
             finite segment.
        
        
            testLine: A line to test.
            Returns: The minimum distance.
        MinimumDistanceTo(self: Line, testPoint: Point3d) -> float
        
            Finds the shortest distance between this line as a finite segment
                    and a test point.
        
            testPoint: A point to test.
            Returns: The minimum distance.
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Line, t: float) -> Point3d
        
            Evaluates the line at the specified parameter.
        
            t: Parameter to evaluate line segment at. Line parameters are normalised parameters.
            Returns: The point at the specified parameter.
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Line) -> NurbsCurve
        
            Constructs a nurbs curve representation of this line. 
                    This amounts to the same as 
             calling NurbsCurve.CreateFromLine().
        
            Returns: A nurbs curve representation of this line or null if no such representation could be made.
        """
        pass

    def ToString(self):
        """
        ToString(self: Line) -> str
        
            Contructs the string representation of this line, in the form "From,To".
            Returns: A text string.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Line, xform: Transform) -> bool
        
            Transform the line using a Transformation matrix.
        
            xform: Transform to apply to this line.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def TryCreateBetweenCurves(curve0, curve1, t0, t1, perpendicular0, perpendicular1, line):
        """
        TryCreateBetweenCurves(curve0: Curve, curve1: Curve, t0: float, t1: float, perpendicular0: bool, perpendicular1: bool) -> (bool, float, float, Line)
        
            Creates a line segment between a pair of curves such that the line segment is either tangent or 
             perpendicular to each of the curves.
        
        
            curve0: The first curve.
            curve1: The second curve.
            t0: Parameter value of point on curve0. Seed value at input and solution at output.
            t1: Parameter value of point on curve 0.  Seed value at input and solution at output.
            perpendicular0: Find line Perpendicuar to (true) or tangent to (false) curve0.
            perpendicular1: Find line Perpendicuar to (true) or tangent to (false) curve1.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def TryFitLineToPoints(points, fitLine):
        """ TryFitLineToPoints(points: IEnumerable[Point3d]) -> (bool, Line) """
        pass

    def TryGetPlane(self, plane):
        """
        TryGetPlane(self: Line) -> (bool, Plane)
        
            Gets a plane that contains the line. The origin of the plane is at the start of the line.
              
                   If possible, a plane parallel to the world xy, yz, or zx plane is returned.
        
            Returns: true on success.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Line]() -> Line
        
        __new__(cls: type, from: Point3d, to: Point3d)
        __new__(cls: type, start: Point3d, span: Vector3d)
        __new__(cls: type, start: Point3d, direction: Vector3d, length: float)
        __new__(cls: type, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line's 3d axis aligned bounding box.

Get: BoundingBox(self: Line) -> BoundingBox

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction of this line segment. 
            The length of the direction vector equals the length of 
            the line segment.

Get: Direction(self: Line) -> Vector3d

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start point of line segment.

Get: From(self: Line) -> Point3d

Set: From(self: Line) = value
"""

    FromX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X coordinate of the line From point.

Get: FromX(self: Line) -> float

Set: FromX(self: Line) = value
"""

    FromY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y coordinate of the line From point.

Get: FromY(self: Line) -> float

Set: FromY(self: Line) = value
"""

    FromZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z coordinate of the line From point.

Get: FromZ(self: Line) -> float

Set: FromZ(self: Line) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this line is valid. 
            Valid lines must have valid start and end points.

Get: IsValid(self: Line) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the length of this line segment. 
            Note that a negative length will invert the line segment without 
            making the actual length negative. The line From point will remain fixed 
            when a new Length is set.

Get: Length(self: Line) -> float

Set: Length(self: Line) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End point of line segment.

Get: To(self: Line) -> Point3d

Set: To(self: Line) = value
"""

    ToX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X coordinate of the line To point.

Get: ToX(self: Line) -> float

Set: ToX(self: Line) = value
"""

    ToY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y coordinate of the line To point.

Get: ToY(self: Line) -> float

Set: ToY(self: Line) = value
"""

    ToZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z coordinate of the line To point.

Get: ToZ(self: Line) -> float

Set: ToZ(self: Line) = value
"""

    UnitTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the tangent of the line segment. 
            Note that tangent vectors are always unit vectors.

Get: UnitTangent(self: Line) -> Vector3d

"""


    Unset = None


class LinearDimension(AnnotationBase, IDisposable, ISerializable):
    """
    Represents a linear dimension.
                This entity refers to the geometric element that is independent from the document.
    
    LinearDimension()
    LinearDimension(dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    @staticmethod
    def FromPoints(extensionLine1End, extensionLine2End, pointOnDimensionLine):
        """
        FromPoints(extensionLine1End: Point3d, extensionLine2End: Point3d, pointOnDimensionLine: Point3d) -> LinearDimension
        
            Initializes a new instance of the Rhino.Geometry.LinearDimension class, based on three points.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def SetLocations(self, extensionLine1End, extensionLine2End, pointOnDimensionLine):
        """
        SetLocations(self: LinearDimension, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
            Sets the three locations of the point, using two-dimensional points that refer to the plane of 
             the annotation.
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
    def __new__(self, dimensionPlane=None, extensionLine1End=None, extensionLine2End=None, pointOnDimensionLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Aligned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this annotation is aligned.

Get: Aligned(self: LinearDimension) -> bool

Set: Aligned(self: LinearDimension) = value
"""

    Arrowhead1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the arrow head end of the first extension line.

Get: Arrowhead1End(self: LinearDimension) -> Point2d

"""

    Arrowhead2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the arrow head end of the second extension line.

Get: Arrowhead2End(self: LinearDimension) -> Point2d

"""

    DimensionStyleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of DimensionStyle in document DimStyle table used by the dimension.

Get: DimensionStyleIndex(self: LinearDimension) -> int

Set: DimensionStyleIndex(self: LinearDimension) = value
"""

    DistanceBetweenArrowTips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance between arrow tips.

Get: DistanceBetweenArrowTips(self: LinearDimension) -> float

"""

    ExtensionLine1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end of the first extension line.

Get: ExtensionLine1End(self: LinearDimension) -> Point2d

"""

    ExtensionLine2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end of the second extension line.

Get: ExtensionLine2End(self: LinearDimension) -> Point2d

"""

    TextPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the position of text on the plane.

Get: TextPosition(self: LinearDimension) -> Point2d

Set: TextPosition(self: LinearDimension) = value
"""



class LineCurve(Curve, IDisposable, ISerializable):
    """
    Represents a linear curve.
    
    LineCurve()
    LineCurve(other: LineCurve)
    LineCurve(from: Point2d, to: Point2d)
    LineCurve(from: Point3d, to: Point3d)
    LineCurve(line: Line)
    LineCurve(line: Line, t0: float, t1: float)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: LineCurve)
        __new__(cls: type, from: Point2d, to: Point2d)
        __new__(cls: type, from: Point3d, to: Point3d)
        __new__(cls: type, line: Line)
        __new__(cls: type, line: Line, t0: float, t1: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Line value inside this curve.

Get: Line(self: LineCurve) -> Line

Set: Line(self: LineCurve) = value
"""



class LoftType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies enumerated constants for all supported loft types.
    
    enum LoftType, values: Developable (4), Loose (1), Normal (0), Straight (3), Tight (2), Uniform (5)
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

    Developable = None
    Loose = None
    Normal = None
    Straight = None
    Tight = None
    Uniform = None
    value__ = None


class Matrix(object, IDisposable):
    """
    Represents an arbitrarily sized matrix of System.Doubledouble-precision
                floating point numbers. If you are working with a 4x4 matrix, then you may want
                to use the Rhino.Geometry.Transform class instead.
    
    Matrix(rowCount: int, columnCount: int)
    Matrix(xform: Transform)
    """
    def BackSolve(self, zeroTolerance, b):
        """
        BackSolve(self: Matrix, zeroTolerance: float, b: Array[float]) -> Array[float]
        
            Solves M*x=b where M is upper triangular with a unit diagonal and
                    b is a column of 
             values.
        
        
            zeroTolerance: (>=0.0) used to test for "zero" values in b
                    in underdetermined systems of equations.
            b: The values in B[RowCount],...,B[B.Length-1] are tested to
                    make sure they are within 
             "zeroTolerance".
        
            Returns: Array of length ColumnCount on success. null on error.
        """
        pass

    def BackSolvePoints(self, zeroTolerance, b):
        """
        BackSolvePoints(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> Array[Point3d]
        
            Solves M*x=b where M is upper triangular with a unit diagonal and
                    b is a column of 
             3d points.
        
        
            zeroTolerance: (>=0.0) used to test for "zero" values in b
                    in underdetermined systems of equations.
            b: The values in B[RowCount],...,B[B.Length-1] are tested to
                    make sure they are "zero".
            Returns: Array of length ColumnCount on success. null on error.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Matrix)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Duplicate(self):
        """
        Duplicate(self: Matrix) -> Matrix
        
            Create a duplicate of this matrix.
            Returns: An exact duplicate of this matrix.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Matrix) -> int
        
            Gets the hash code for this matrix. The hash code will change 
                    when the matrix 
             changes so you cannot change matrices while they are stored in 
                    hash tables.
        
            Returns: Hash code.
        """
        pass

    def Invert(self, zeroTolerance):
        """
        Invert(self: Matrix, zeroTolerance: float) -> bool
        
            Modifies this matrix to become its own inverse.
                    Matrix might be non-invertible 
             (singular) and the return value will be false.
        
        
            zeroTolerance: The admitted tolerance for 0.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def RowReduce(self, zeroTolerance, *__args):
        """
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> (int, float)
        
            Row reduces a matrix as the first step in solving M*X=b where
                    b is a column of 3d 
             points.
        
        
            zeroTolerance: (>=0.0) zero tolerance for pivot test. If the absolute value of a pivot
                    is <= 
             zero_tolerance, then the pivot is assumed to be zero.
        
            b: An array of RowCount 3d points that is row reduced with the matrix.
            Returns: Rank of the matrix.
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[float]) -> (int, float)
        
            Row reduces a matrix as the first step in solving M*X=b where
                    b is a column of 
             values.
        
        
            zeroTolerance: (>=0.0) zero tolerance for pivot test. If the absolute value of a pivot
                    is <= 
             zero_tolerance, then the pivot is assumed to be zero.
        
            b: an array of RowCount values that is row reduced with the matrix.
            Returns: Rank of the matrix.
        RowReduce(self: Matrix, zeroTolerance: float) -> (int, float, float)
        
            Row reduces a matrix to calculate rank and determinant.
        
            zeroTolerance: (>=0.0) zero tolerance for pivot test.  If a the absolute value of
                    a pivot is <= 
             zeroTolerance, then the pivot is assumed to be zero.
        
            Returns: Rank of the matrix.
        """
        pass

    def Scale(self, s):
        """
        Scale(self: Matrix, s: float)
            Modifies the current matrix by multiplying its values by a number.
        
            s: A scale factor.
        """
        pass

    def SetDiagonal(self, d):
        """
        SetDiagonal(self: Matrix, d: float)
            Sets diagonal value and zeros off all non-diagonal values.
        
            d: The new diagonal value.
        """
        pass

    def SwapColumns(self, columnA, columnB):
        """
        SwapColumns(self: Matrix, columnA: int, columnB: int) -> bool
        
            Exchanges two columns.
        
            columnA: A first column.
            columnB: Another column.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def SwapRows(self, rowA, rowB):
        """
        SwapRows(self: Matrix, rowA: int, rowB: int) -> bool
        
            Exchanges two rows.
        
            rowA: A first row.
            rowB: Another row.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def Transpose(self):
        """
        Transpose(self: Matrix) -> bool
        
            Modifies this matrix to be its transpose.
                    This is like swapping rows with 
             columns.http://en.wikipedia.org/wiki/Transpose
        
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def Zero(self):
        """
        Zero(self: Matrix)
            Sets all values inside the matrix to zero.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rowCount: int, columnCount: int)
        __new__(cls: type, xform: Transform)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(a: Matrix, b: Matrix) -> Matrix
        
            Adds two matrices and returns a new sum matrix.
        
            a: A first matrix to use in calculation.
            b: Another matrix to use in calculation.
            Returns: The sum matrix.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(a: Matrix, b: Matrix) -> Matrix
        
            Multiplies two matrices and returns a new product matrix.
        
            a: A first matrix to use in calculation.
            b: Another matrix to use in calculation.
            Returns: The product matrix.
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ColumnCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of columns.

Get: ColumnCount(self: Matrix) -> int

"""

    IsColumnOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the matrix is column orthogonal.

Get: IsColumnOrthogonal(self: Matrix) -> bool

"""

    IsColumnOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the matrix is column orthonormal.

Get: IsColumnOrthoNormal(self: Matrix) -> bool

"""

    IsRowOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the matrix is row orthogonal.

Get: IsRowOrthogonal(self: Matrix) -> bool

"""

    IsRowOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the matrix is row orthonormal.

Get: IsRowOrthoNormal(self: Matrix) -> bool

"""

    IsSquare = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this matrix has the same number of rows
            and columns. 0x0 matrices are not considered square.

Get: IsSquare(self: Matrix) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this matrix is valid.

Get: IsValid(self: Matrix) -> bool

"""

    RowCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of rows.

Get: RowCount(self: Matrix) -> int

"""



class Mesh(GeometryBase, IDisposable, ISerializable):
    """
    Represents a geometry type that is defined by vertices and faces.
                This is often called a face-vertex mesh.
    
    Mesh()
    """
    def Append(self, other):
        """
        Append(self: Mesh, other: Mesh)
            Appends a copy of another mesh to this one and updates indices of appended mesh parts.
        
            other: Mesh to append to this one.
        """
        pass

    def ClearTextureData(self):
        """
        ClearTextureData(self: Mesh)
            Remove all texture coordinate information from this mesh.
        """
        pass

    def ClosestMeshPoint(self, testPoint, maximumDistance):
        """
        ClosestMeshPoint(self: Mesh, testPoint: Point3d, maximumDistance: float) -> MeshPoint
        
            Gets the point on the mesh that is closest to a given test point. Similar to the 
                    
             ClosestPoint function except this returns a MeshPoint class which includes
                    extra 
             information beyond just the location of the closest point.
        
        
            testPoint: The source of the search.
            maximumDistance: Optional upper bound on the distance from test point to the mesh. 
                    If you are only 
             interested in finding a point Q on the mesh when 
                    testPoint.DistanceTo(Q) < 
             maximumDistance, 
                    then set maximumDistance to that value. 
                    This 
             parameter is ignored if you pass 0.0 for a maximumDistance.
        
            Returns: closest point information on success. null on failure.
        """
        pass

    def ClosestPoint(self, testPoint, pointOnMesh=None, *__args):
        """
        ClosestPoint(self: Mesh, testPoint: Point3d, maximumDistance: float) -> (int, Point3d, Vector3d)
        
            Gets the point on the mesh that is closest to a given test point.
        
            testPoint: Point to seach for.
            maximumDistance: Optional upper bound on the distance from test point to the mesh. 
                    If you are only 
             interested in finding a point Q on the mesh when 
                    testPoint.DistanceTo(Q) < 
             maximumDistance, 
                    then set maximumDistance to that value. 
                    This 
             parameter is ignored if you pass 0.0 for a maximumDistance.
        
            Returns: Index of face that the closest point lies on if successful. 
                    -1 if not successful; 
             the value of pointOnMesh is undefined.
        
        ClosestPoint(self: Mesh, testPoint: Point3d, maximumDistance: float) -> (int, Point3d)
        
            Gets the point on the mesh that is closest to a given test point.
        
            testPoint: Point to seach for.
            maximumDistance: Optional upper bound on the distance from test point to the mesh. 
                    If you are only 
             interested in finding a point Q on the mesh when 
                    testPoint.DistanceTo(Q) < 
             maximumDistance, 
                    then set maximumDistance to that value. 
                    This 
             parameter is ignored if you pass 0.0 for a maximumDistance.
        
            Returns: Index of face that the closest point lies on if successful. 
                    -1 if not successful; 
             the value of pointOnMesh is undefined.
        
        ClosestPoint(self: Mesh, testPoint: Point3d) -> Point3d
        
            Gets the point on the mesh that is closest to a given test point.
        
            testPoint: Point to seach for.
            Returns: The point on the mesh closest to testPoint, or Point3d.Unset on failure.
        """
        pass

    def ColorAt(self, *__args):
        """
        ColorAt(self: Mesh, faceIndex: int, t0: float, t1: float, t2: float, t3: float) -> Color
        
            Evaluate a mesh normal at a set of barycentric coordinates. Barycentric coordinates must 
              
                   be assigned in accordance with the rules as defined by MeshPoint.T.
        
        
            faceIndex: Index of triangle or quad to evaluate.
            t0: First barycentric coordinate.
            t1: Second barycentric coordinate.
            t2: Third barycentric coordinate.
            t3: Fourth barycentric coordinate. If the face is a triangle, this coordinate will be ignored.
            Returns: The interpolated vertex color on the mesh or Color.Transparent if the faceIndex is not valid, 
         
                        if the barycentric coordinates could not be evaluated, or if there are no colors 
             defined on the mesh.
        
        ColorAt(self: Mesh, meshPoint: MeshPoint) -> Color
        
            Evaluate a mesh color at a set of barycentric coordinates.
        
            meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.
            Returns: The interpolated vertex color on the mesh or Color.Transparent if the faceIndex is not valid, 
         
                        if the barycentric coordinates could not be evaluated, or if there are no colors 
             defined on the mesh.
        """
        pass

    def Compact(self):
        """
        Compact(self: Mesh) -> bool
        
            Removes any unreferenced objects from arrays, reindexes as needed 
                    and shrinks 
             arrays to minimum required size.
        
            Returns: true on success, false on failure.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def CopyFrom(self, other):
        """
        CopyFrom(self: Mesh, other: Mesh)
            Copies mesh values into this mesh from another mesh.
        
            other: The other mesh to copy from.
        """
        pass

    @staticmethod
    def CreateBooleanDifference(firstSet, secondSet):
        """ CreateBooleanDifference(firstSet: IEnumerable[Mesh], secondSet: IEnumerable[Mesh]) -> Array[Mesh] """
        pass

    @staticmethod
    def CreateBooleanIntersection(firstSet, secondSet):
        """ CreateBooleanIntersection(firstSet: IEnumerable[Mesh], secondSet: IEnumerable[Mesh]) -> Array[Mesh] """
        pass

    @staticmethod
    def CreateBooleanSplit(meshesToSplit, meshSplitters):
        """ CreateBooleanSplit(meshesToSplit: IEnumerable[Mesh], meshSplitters: IEnumerable[Mesh]) -> Array[Mesh] """
        pass

    @staticmethod
    def CreateBooleanUnion(meshes):
        """ CreateBooleanUnion(meshes: IEnumerable[Mesh]) -> Array[Mesh] """
        pass

    @staticmethod
    def CreateContourCurves(meshToContour, *__args):
        """
        CreateContourCurves(meshToContour: Mesh, sectionPlane: Plane) -> Array[Curve]
        
            Constructs contour curves for a mesh, sectioned at a plane.
        
            meshToContour: A mesh to contour.
            sectionPlane: A cutting plane.
            Returns: An array of curves. This array can be empty.
        CreateContourCurves(meshToContour: Mesh, contourStart: Point3d, contourEnd: Point3d, interval: float) -> Array[Curve]
        
            Constructs contour curves for a mesh, sectioned along a linear axis.
        
            meshToContour: A mesh to contour.
            contourStart: A start point of the contouring axis.
            contourEnd: An end point of the contouring axis.
            interval: An interval distance.
            Returns: An array of curves. This array can be empty.
        """
        pass

    @staticmethod
    def CreateFromBox(*__args):
        """
        CreateFromBox(corners: IEnumerable[Point3d], xCount: int, yCount: int, zCount: int) -> Mesh
        CreateFromBox(box: Box, xCount: int, yCount: int, zCount: int) -> Mesh
        
            Constructs new mesh that matches an aligned box.
        
            box: Box to match.
            xCount: Number of faces in x-direction.
            yCount: Number of faces in y-direction.
            zCount: Number of faces in z-direction.
        CreateFromBox(box: BoundingBox, xCount: int, yCount: int, zCount: int) -> Mesh
        
            Constructs new mesh that matches a bounding box.
        
            box: A box to use for creation.
            xCount: Number of faces in x-direction.
            yCount: Number of faces in y-direction.
            zCount: Number of faces in z-direction.
            Returns: A new brep, or null on failure.
        """
        pass

    @staticmethod
    def CreateFromBrep(brep, meshingParameters=None):
        """
        CreateFromBrep(brep: Brep, meshingParameters: MeshingParameters) -> Array[Mesh]
        
            Constructs a mesh from a brep.
        
            brep: Brep to approximate.
            meshingParameters: Parameters to use during meshing.
            Returns: An array of meshes.
        CreateFromBrep(brep: Brep) -> Array[Mesh]
        
            Constructs a mesh from a brep.
        
            brep: Brep to approximate.
            Returns: An array of meshes.
        """
        pass

    @staticmethod
    def CreateFromClosedPolyline(polyline):
        """
        CreateFromClosedPolyline(polyline: Polyline) -> Mesh
        
            Attempts to create a Mesh that is a triangulation of a closed polyline
        
            polyline: must be closed
            Returns: New mesh on success or null on failure.
        """
        pass

    @staticmethod
    def CreateFromCone(cone, vertical, around):
        """
        CreateFromCone(cone: Cone, vertical: int, around: int) -> Mesh
        
            Constructs a mesh cone
        
            vertical: Number of faces in the top-to-bottom direction
            around: Number of faces around the cone
        """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder, vertical, around):
        """
        CreateFromCylinder(cylinder: Cylinder, vertical: int, around: int) -> Mesh
        
            Constructs a mesh cylinder
        
            vertical: Number of faces in the top-to-bottom direction
            around: Number of faces around the cylinder
        """
        pass

    @staticmethod
    def CreateFromPlanarBoundary(boundary, parameters):
        """
        CreateFromPlanarBoundary(boundary: Curve, parameters: MeshingParameters) -> Mesh
        
            Attempts to construct a mesh from a closed planar curve.
        
            boundary: must be a closed planar curve.
            parameters: parameters used for creating the mesh.
            Returns: New mesh on success or null on failure.
        """
        pass

    @staticmethod
    def CreateFromPlane(plane, xInterval, yInterval, xCount, yCount):
        """
        CreateFromPlane(plane: Plane, xInterval: Interval, yInterval: Interval, xCount: int, yCount: int) -> Mesh
        
            Constructs a planar mesh grid.
        
            plane: Plane of mesh.
            xInterval: Interval describing size and extends of mesh along plane x-direction.
            yInterval: Interval describing size and extends of mesh along plane y-direction.
            xCount: Number of faces in x-direction.
            yCount: Number of faces in y-direction.
        """
        pass

    @staticmethod
    def CreateFromSphere(sphere, xCount, yCount):
        """
        CreateFromSphere(sphere: Sphere, xCount: int, yCount: int) -> Mesh
        
            Constructs a mesh sphere.
        
            sphere: Base sphere for mesh.
            xCount: Number of faces in the around direction.
            yCount: Number of faces in the top-to-bottom direction.
        """
        pass

    def CreatePartitions(self, maximumVertexCount, maximumTriangleCount):
        """
        CreatePartitions(self: Mesh, maximumVertexCount: int, maximumTriangleCount: int) -> bool
        
            In ancient times (or modern smartphone times), some rendering engines
                    were only 
             able to process small batches of triangles and the
                    CreatePartitions() function was 
             provided to partition the mesh into
                    subsets of vertices and faces that those 
             rendering engines could handle.
        
            Returns: true on success
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Duplicate(self):
        """
        Duplicate(self: Mesh) -> GeometryBase
        
            Constructs a copy of this mesh.
                    This is the same as 
             Rhino.Geometry.Mesh.DuplicateMesh.
        
            Returns: A mesh.
        """
        pass

    def DuplicateMesh(self):
        """
        DuplicateMesh(self: Mesh) -> Mesh
        
            Constructs a copy of this mesh.
                    This is the same as Rhino.Geometry.Mesh.Duplicate.
        """
        pass

    def EvaluateMeshGeometry(self, surface):
        """
        EvaluateMeshGeometry(self: Mesh, surface: Surface) -> bool
        
            If the mesh has SurfaceParameters, the surface is evaluated at
                    these parameters and 
             the mesh geometry is updated.
        
        
            surface: An input surface.
            Returns: true if the operation succceeded; false otherwise.
        """
        pass

    def ExplodeAtUnweldedEdges(self):
        """
        ExplodeAtUnweldedEdges(self: Mesh) -> Array[Mesh]
        
            Explode the mesh into submeshes where a submesh is a collection of faces that are contained
            
                     within a closed loop of "unwelded" edges. Unwelded edges are edges where the faces that 
             share
                    the edge have unique mesh vertexes (not mesh topology vertexes) at both ends 
             of the edge.
        
            Returns: Array of submeshes on success; null on error. If the count in the returned array is 1, then
            
                     nothing happened and the ouput is essentially a copy of the input.
        """
        pass

    def Flip(self, vertexNormals, faceNormals, faceOrientation):
        """
        Flip(self: Mesh, vertexNormals: bool, faceNormals: bool, faceOrientation: bool)
            Reverses the direction of the mesh.
        
            vertexNormals: If true, vertex normals will be reversed.
            faceNormals: If true, face normals will be reversed.
            faceOrientation: If true, face orientations will be reversed.
        """
        pass

    def GetCachedTextureCoordinates(self, textureMappingId):
        """
        GetCachedTextureCoordinates(self: Mesh, textureMappingId: Guid) -> CachedTextureCoordinates
        
            Call this method to get cached texture coordinates for a texture
                    mapping with the 
             specified Id.
        
        
            textureMappingId: Texture mapping Id
            Returns: Object which allows access to coordinates and other props.
        """
        pass

    def GetNakedEdgePointStatus(self):
        """
        GetNakedEdgePointStatus(self: Mesh) -> Array[bool]
        
            Returns an array of bool values equal in length to the number of vertices in this
                    
             mesh. Each value corresponds to a mesh vertex and is set to true if the vertex is
                    
             not completely surrounded by faces.
        
            Returns: An array of true/false flags that, at each index, reveals if the corresponding
                    
             vertex is completely surrounded by faces.
        """
        pass

    def GetNakedEdges(self):
        """
        GetNakedEdges(self: Mesh) -> Array[Polyline]
        
            Returns all edges of a mesh that are considered "naked" in the
                    sense that the edge 
             only has one face.
        
            Returns: An array of polylines, or null on error.
        """
        pass

    def GetOutlines(self, *__args):
        """
        GetOutlines(self: Mesh, viewport: RhinoViewport) -> Array[Polyline]
        
            Constructs the outlines of a mesh. The projection information in the
                    viewport is 
             used to determine how the outlines are projected.
        
        
            viewport: A viewport to determine projection direction.
            Returns: An array of polylines, or null on error.
        GetOutlines(self: Mesh, plane: Plane) -> Array[Polyline]
        
            Constructs the outlines of a mesh projected against a plane.
        
            plane: A plane to project against.
            Returns: An array of polylines, or null on error.
        """
        pass

    def GetPartition(self, which):
        """
        GetPartition(self: Mesh, which: int) -> MeshPart
        
            Retrieves a partition. See Rhino.Geometry.Mesh.CreatePartitions(System.Int32,System.Int32) for 
             details.
        
        
            which: The partition index.
        """
        pass

    def IsManifold(self, topologicalTest, isOriented, hasBoundary):
        """
        IsManifold(self: Mesh, topologicalTest: bool) -> (bool, bool, bool)
        
            Gets a value indicating whether or not the mesh is manifold. 
                    A manifold mesh does 
             not have any edge that borders more than two faces.
        
        
            topologicalTest: If true, the query treats coincident vertices as the same.
            Returns: true if every mesh "edge" has at most two adjacent faces.
        """
        pass

    def IsPointInside(self, point, tolerance, strictlyIn):
        """
        IsPointInside(self: Mesh, point: Point3d, tolerance: float, strictlyIn: bool) -> bool
        
            Determines if a point is inside a solid mesh.
        
            point: 3d point to test.
            tolerance: (>=0) 3d distance tolerance used for ray-mesh intersection
                    and determining strict 
             inclusion.
        
            strictlyIn: If strictlyIn is true, then point must be inside mesh by at least
                    tolerance in 
             order for this function to return true.
                    If strictlyIn is false, then this function 
             will return true if
                    point is inside or the distance from point to a mesh face is <= 
             tolerance.
        
            Returns: true if point is inside the solid mesh, false if not.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def NormalAt(self, *__args):
        """
        NormalAt(self: Mesh, faceIndex: int, t0: float, t1: float, t2: float, t3: float) -> Vector3d
        
            Evaluate a mesh normal at a set of barycentric coordinates. Barycentric coordinates must 
              
                   be assigned in accordance with the rules as defined by MeshPoint.T.
        
        
            faceIndex: Index of triangle or quad to evaluate.
            t0: First barycentric coordinate.
            t1: Second barycentric coordinate.
            t2: Third barycentric coordinate.
            t3: Fourth barycentric coordinate. If the face is a triangle, this coordinate will be ignored.
            Returns: A Normal vector to the mesh or Vector3d.Unset if the faceIndex is not valid or if the 
             barycentric coordinates could not be evaluated.
        
        NormalAt(self: Mesh, meshPoint: MeshPoint) -> Vector3d
        
            Evaluate a mesh normal at a set of barycentric coordinates.
        
            meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.
            Returns: A Normal vector to the mesh or Vector3d.Unset if the faceIndex is not valid or if the 
             barycentric coordinates could not be evaluated.
        """
        pass

    def Offset(self, distance, solidify=None):
        """
        Offset(self: Mesh, distance: float, solidify: bool) -> Mesh
        
            Makes a new mesh with vertices offset a distance in the opposite direction of the existing 
             vertex normals.
                    Optionally, based on the value of solidify, adds the input mesh and 
             a ribbon of faces along any naked edges.
                    If solidify is false it acts exactly as 
             the Offset(distance) function.
        
        
            distance: A distance value.
            solidify: true if the mesh should be solidified.
            Returns: A new mesh on success, or null on failure.
        Offset(self: Mesh, distance: float) -> Mesh
        
            Makes a new mesh with vertices offset a distance in the opposite direction of the existing 
             vertex normals.
                    Same as Mesh.Offset(distance, false)
        
        
            distance: A distance value to use for offsetting.
            Returns: A new mesh on success, or null on failure.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: Mesh)
            Performs some memory cleanup if necessary
        """
        pass

    def PointAt(self, *__args):
        """
        PointAt(self: Mesh, faceIndex: int, t0: float, t1: float, t2: float, t3: float) -> Point3d
        
            Evaluates a mesh at a set of barycentric coordinates. Barycentric coordinates must 
                    
             be assigned in accordance with the rules as defined by MeshPoint.T.
        
        
            faceIndex: Index of triangle or quad to evaluate.
            t0: First barycentric coordinate.
            t1: Second barycentric coordinate.
            t2: Third barycentric coordinate.
            t3: Fourth barycentric coordinate. If the face is a triangle, this coordinate will be ignored.
            Returns: A Point on the mesh or Point3d.Unset if the faceIndex is not valid or if the barycentric 
             coordinates could not be evaluated.
        
        PointAt(self: Mesh, meshPoint: MeshPoint) -> Point3d
        
            Evaluate a mesh at a set of barycentric coordinates.
        
            meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.
            Returns: A Point on the mesh or Point3d.Unset if the faceIndex is not valid or if the barycentric 
             coordinates could not be evaluated.
        """
        pass

    def PullPointsToMesh(self, points):
        """ PullPointsToMesh(self: Mesh, points: IEnumerable[Point3d]) -> Array[Point3d] """
        pass

    def Reduce(self, desiredPolygonCount, allowDistortion, accuracy, normalizeSize):
        """
        Reduce(self: Mesh, desiredPolygonCount: int, allowDistortion: bool, accuracy: int, normalizeSize: bool) -> bool
        
            Reduce polygon count
        
            desiredPolygonCount: desired or target number of faces
            allowDistortion: If true mesh appearance is not changed even if the target polygon count is not reached
            accuracy: Integer from 1 to 10 telling how accurate reduction algorithm
                     to use. Greater 
             number gives more accurate results
        
            normalizeSize: If true mesh is fitted to an axis aligned unit cube until reduction is complete
            Returns: True if mesh is successfully reduced and false if mesh could not be reduced for some reason.
        """
        pass

    def SetCachedTextureCoordinates(self, tm, xf):
        """
        SetCachedTextureCoordinates(self: Mesh, tm: TextureMapping, xf: Transform) -> Transform
        
            Set cached texture coordinates using the specified mapping.
        """
        pass

    def SolidOrientation(self):
        """
        SolidOrientation(self: Mesh) -> int
        
            Determines orientation of a "solid" mesh.
            Returns: +1 = mesh is solid with outward facing normals.-1 = mesh is solid with inward facing normals.0 = 
             mesh is not solid.
        """
        pass

    def Split(self, *__args):
        """
        Split(self: Mesh, meshes: IEnumerable[Mesh]) -> Array[Mesh]
        Split(self: Mesh, mesh: Mesh) -> Array[Mesh]
        
            Split a mesh with another mesh.
        
            mesh: Mesh to split with.
            Returns: An array of mesh segments representing the split result.
        Split(self: Mesh, plane: Plane) -> Array[Mesh]
        
            Split a mesh by an infinite plane.
        
            plane: The splitting plane.
            Returns: A new mesh array with the split result. This can be null if no result was found.
        """
        pass

    def SplitDisjointPieces(self):
        """
        SplitDisjointPieces(self: Mesh) -> Array[Mesh]
        
            Splits up the mesh into its unconnected pieces.
            Returns: An array containing all the disjoint pieces that make up this Mesh.
        """
        pass

    def UnifyNormals(self):
        """
        UnifyNormals(self: Mesh) -> int
        
            Attempts to fix inconsistencies in the directions of meshfaces for a mesh. This function
               
                  does not modify the vertex normals, but rather rearranges the mesh face winding and face
          
                       normals to make them all consistent. You may want to call 
             Mesh.Normals.ComputeNormals()
                    to recompute vertex normals after calling this 
             functions.
        
            Returns: number of faces that were modified.
        """
        pass

    def Unweld(self, angleToleranceRadians, modifyNormals):
        """
        Unweld(self: Mesh, angleToleranceRadians: float, modifyNormals: bool)
            Makes sure that faces sharing an edge and having a difference of normal greater
                    
             than or equal to angleToleranceRadians have unique vertexes along that edge,
                    adding 
             vertices if necessary.
        
        
            angleToleranceRadians: Angle at which to make unique vertices.
            modifyNormals: Determines whether new vertex normals will have the same vertex normal as the original (false)
         
                        or vertex normals made from the corrsponding face normals (true)
        """
        pass

    def Weld(self, angleToleranceRadians):
        """
        Weld(self: Mesh, angleToleranceRadians: float)
            Makes sure that faces sharing an edge and having a difference of normal greater
                    
             than or equal to angleToleranceRadians share vertexes along that edge, vertex normals
                  
               are averaged.
        
        
            angleToleranceRadians: Angle at which to weld vertices.
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DisjointMeshCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of disjoint (topologically unconnected) pieces in this mesh.

Get: DisjointMeshCount(self: Mesh) -> int

"""

    FaceNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the face normal collection in this mesh.

Get: FaceNormals(self: Mesh) -> MeshFaceNormalList

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the faces collection in this mesh.

Get: Faces(self: Mesh) -> MeshFaceList

"""

    HasCachedTextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Will return true if SetCachedTextureCoordinates has been called;
            otherwise will return false.

Get: HasCachedTextureCoordinates(self: Mesh) -> bool

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a mesh is considered to be closed (solid).
            A mesh is considered solid when every mesh edge borders two or more faces.

Get: IsClosed(self: Mesh) -> bool

"""

    Normals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the vertex normal collection in this mesh.

Get: Normals(self: Mesh) -> MeshVertexNormalList

"""

    PartitionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of partition information chunks stored on this mesh based
            on the last call to CreatePartitions

Get: PartitionCount(self: Mesh) -> int

"""

    TextureCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the vertex texture coordinate collection in this mesh.

Get: TextureCoordinates(self: Mesh) -> MeshTextureCoordinateList

"""

    TopologyEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Rhino.Geometry.Collections.MeshTopologyEdgeList object associated with this mesh.
            This object stores edge connectivity.

Get: TopologyEdges(self: Mesh) -> MeshTopologyEdgeList

"""

    TopologyVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Rhino.Geometry.Collections.MeshTopologyVertexList object associated with this mesh.
            This object stores vertex connectivity and the indices of vertices
            that were unified while computing the edge topology.

Get: TopologyVertices(self: Mesh) -> MeshTopologyVertexList

"""

    VertexColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the (optional) vertex color collection in this mesh.

Get: VertexColors(self: Mesh) -> MeshVertexColorList

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the vertices set of this mesh.

Get: Vertices(self: Mesh) -> MeshVertexList

"""



class MeshFace(object):
    """
    Represents the values of the four indices of a mesh face quad.
                If the third and fourth values are the same, this face represents a
                triangle.
    
    MeshFace(a: int, b: int, c: int)
    MeshFace(a: int, b: int, c: int, d: int)
    """
    def Flip(self):
        """
        Flip(self: MeshFace) -> MeshFace
        
            Reverses the orientation of the face by swapping corners. 
                    The first corner is 
             always maintained.
        """
        pass

    def IsValid(self, vertexCount=None):
        """
        IsValid(self: MeshFace, vertexCount: int) -> bool
        
            Gets a value indicating whether or not this mesh face 
                    is considered to be valid. 
             Unlike the simple IsValid function, 
                    this function takes upper bound indices into 
             account.
        
        
            vertexCount: Number of vertices in the mesh that this face is a part of.
            Returns: true if the face is considered valid, false if not.
        IsValid(self: MeshFace) -> bool
        
            Gets a value indicating whether or not this mesh face 
                    is considered to be valid. 
             Note that even valid mesh faces 
                    could potentially be invalid in the context of a 
             specific Mesh, 
                    if one or more of the corner indices exceeds the number of 
               
                  vertices on the mesh. If you want to perform a complete 
                    validity check, use 
             IsValid(int) instead.
        """
        pass

    def Set(self, a, b, c, d=None):
        """
        Set(self: MeshFace, a: int, b: int, c: int, d: int)
            Sets all the corners for this face as a quad.
        
            a: Index of first corner.
            b: Index of second corner.
            c: Index of third corner.
            d: Index of fourth corner.
        Set(self: MeshFace, a: int, b: int, c: int)
            Sets all the corners for this face as a triangle.
        
            a: Index of first corner.
            b: Index of second corner.
            c: Index of third corner.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, a, b, c, d=None):
        """
        __new__[MeshFace]() -> MeshFace
        
        __new__(cls: type, a: int, b: int, c: int)
        __new__(cls: type, a: int, b: int, c: int, d: int)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first corner index of the mesh face.

Get: A(self: MeshFace) -> int

Set: A(self: MeshFace) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the second corner index of the mesh face.

Get: B(self: MeshFace) -> int

Set: B(self: MeshFace) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the third corner index of the mesh face.

Get: C(self: MeshFace) -> int

Set: C(self: MeshFace) = value
"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the fourth corner index of the mesh face. 
            If D equals C, the mesh face is considered to be a triangle 
            rather than a quad.

Get: D(self: MeshFace) -> int

Set: D(self: MeshFace) = value
"""

    IsQuad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this mesh face is a quad. 
            A mesh face is considered to be a triangle when C does not equal D, 
            thus it is possible for an Invalid mesh face to also be a quad.

Get: IsQuad(self: MeshFace) -> bool

"""

    IsTriangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this mesh face is a triangle. 
            A mesh face is considered to be a triangle when C equals D, thus it is 
            possible for an Invalid mesh face to also be a triangle.

Get: IsTriangle(self: MeshFace) -> bool

"""


    Unset = None


class MeshingParameters(object, IDisposable):
    """
    Represents settings used for creating a mesh representation of a brep or surface.
    
    MeshingParameters()
    """
    def Dispose(self):
        """
        Dispose(self: MeshingParameters)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    @staticmethod
    def DocumentCurrentSetting(doc):
        """
        DocumentCurrentSetting(doc: RhinoDoc) -> MeshingParameters
        
            Gets the MeshingParameters that are currently set for a document.
                    These are the 
             same settings that are shown in the DocumentProperties
                    "mesh settings" user 
             interface.
        
        
            doc: A Rhino document to query.
            Returns: Meshing parameters of the document.
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

    ComputeCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether or not surface curvature 
            data will be embedded in the mesh.

Get: ComputeCurvature(self: MeshingParameters) -> bool

Set: ComputeCurvature(self: MeshingParameters) = value
"""

    GridAmplification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the grid amplification factor. 
            Values lower than 1.0 will decrease the number of initial quads, 
            values higher than 1.0 will increase the number of initial quads.

Get: GridAmplification(self: MeshingParameters) -> float

Set: GridAmplification(self: MeshingParameters) = value
"""

    GridAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed angle difference (in radians) 
            for a single sampling quad. The angle pertains to the surface normals.

Get: GridAngle(self: MeshingParameters) -> float

Set: GridAngle(self: MeshingParameters) = value
"""

    GridAspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed aspect ratio of sampling quads.

Get: GridAspectRatio(self: MeshingParameters) -> float

Set: GridAspectRatio(self: MeshingParameters) = value
"""

    GridMaxCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of grid quads in the initial sampling grid.

Get: GridMaxCount(self: MeshingParameters) -> int

Set: GridMaxCount(self: MeshingParameters) = value
"""

    GridMinCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum number of grid quads in the initial sampling grid.

Get: GridMinCount(self: MeshingParameters) -> int

Set: GridMinCount(self: MeshingParameters) = value
"""

    JaggedSeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether or not the mesh is allowed to have jagged seams. 
            When this flag is set to true, meshes on either side of a Brep Edge will not match up.

Get: JaggedSeams(self: MeshingParameters) -> bool

Set: JaggedSeams(self: MeshingParameters) = value
"""

    MaximumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed mesh edge length.

Get: MaximumEdgeLength(self: MeshingParameters) -> float

Set: MaximumEdgeLength(self: MeshingParameters) = value
"""

    MinimumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum allowed mesh edge length.

Get: MinimumEdgeLength(self: MeshingParameters) -> float

Set: MinimumEdgeLength(self: MeshingParameters) = value
"""

    MinimumTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum tolerance.

Get: MinimumTolerance(self: MeshingParameters) -> float

Set: MinimumTolerance(self: MeshingParameters) = value
"""

    RefineAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the mesh parameter refine angle.

Get: RefineAngle(self: MeshingParameters) -> float

Set: RefineAngle(self: MeshingParameters) = value
"""

    RefineGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether or not the sampling grid can be refined 
            when certain tolerances are not met.

Get: RefineGrid(self: MeshingParameters) -> bool

Set: RefineGrid(self: MeshingParameters) = value
"""

    RelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the relative tolerance.

Get: RelativeTolerance(self: MeshingParameters) -> float

Set: RelativeTolerance(self: MeshingParameters) = value
"""

    SimplePlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether or not planar areas are allowed 
            to be meshed in a simplified manner.

Get: SimplePlanes(self: MeshingParameters) -> bool

Set: SimplePlanes(self: MeshingParameters) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed edge deviation. 
            This tolerance is measured between the center of the mesh edge and the surface.

Get: Tolerance(self: MeshingParameters) -> float

Set: Tolerance(self: MeshingParameters) = value
"""



class MeshingParameterStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of Mesh Parameters used by the RhinoDoc for meshing objects
    
    enum MeshingParameterStyle, values: Custom (9), Fast (1), None (0), PerObject (10), Quality (2)
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

    Custom = None
    Fast = None
    None = None
    PerObject = None
    Quality = None
    value__ = None


class MeshPart(object):
    """ Represents a portion of a mesh for partitioning """
    EndFaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End of subinterval of parent mesh face array

Get: EndFaceIndex(self: MeshPart) -> int

"""

    EndVertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End of subinterval of parent mesh vertex array

Get: EndVertexIndex(self: MeshPart) -> int

"""

    StartFaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start of subinterval of parent mesh face array

Get: StartFaceIndex(self: MeshPart) -> int

"""

    StartVertexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start of subinterval of parent mesh vertex array

Get: StartVertexIndex(self: MeshPart) -> int

"""

    TriangleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TriangleCount(self: MeshPart) -> int

"""

    VertexCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EndVertexIndex - StartVertexIndex

Get: VertexCount(self: MeshPart) -> int

"""



class MeshPoint(object):
    """ Represents a point that is found on a mesh. """
    def GetTriangle(self, a, b, c):
        """
        GetTriangle(self: MeshPoint) -> (bool, int, int, int)
        
            Gets the mesh face indices of the triangle where the
                    intersection is on the face 
             takes into consideration
                    the way the quad was split during the intersection.
        """
        pass

    ComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component index of the intersecting element in the mesh.

Get: ComponentIndex(self: MeshPoint) -> ComponentIndex

"""

    EdgeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When set, EdgeIndex is an index of an edge in the mesh's edge list.

Get: EdgeIndex(self: MeshPoint) -> int

"""

    EdgeParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Edge parameter when found.

Get: EdgeParameter(self: MeshPoint) -> float

"""

    FaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FaceIndex is an index of a face in mesh.Faces.
            When ComponentIndex refers to a vertex, any face that uses the vertex
            may appear as FaceIndex.  When ComponenctIndex refers to an Edge or
            EdgeIndex is set, then any face that uses that edge may appear as FaceIndex.

Get: FaceIndex(self: MeshPoint) -> int

"""

    Mesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mesh that is ralated to this point.

Get: Mesh(self: MeshPoint) -> Mesh

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location (position) of this point.

Get: Point(self: MeshPoint) -> Point3d

"""

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Barycentric quad coordinates for the point on the mesh
            face mesh.Faces[FaceIndex].  If the face is a triangle
            disregard T[3] (it should be set to 0.0). If the face is
            a quad and is split between vertexes 0 and 2, then T[3]
            will be 0.0 when point is on the triangle defined by vi[0],
            vi[1], vi[2] and T[1] will be 0.0 when point is on the
            triangle defined by vi[0], vi[2], vi[3]. If the face is a
            quad and is split between vertexes 1 and 3, then T[2] will
            be -1 when point is on the triangle defined by vi[0],
            vi[1], vi[3] and m_t[0] will be -1 when point is on the
            triangle defined by vi[1], vi[2], vi[3].

Get: T(self: MeshPoint) -> Array[float]

"""

    Triangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Face triangle where the intersection takes place:
            0 is unsetA is 0,1,2B is 0,2,3C is 0,1,3D is 1,2,3

Get: Triangle(self: MeshPoint) -> Char

"""



class MeshType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for various mesh types.
    
    enum MeshType, values: Analysis (2), Any (4), Default (0), Preview (3), Render (1)
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

    Analysis = None
    Any = None
    Default = None
    Preview = None
    Render = None
    value__ = None


class MorphControl(GeometryBase, IDisposable, ISerializable):
    """
    Represents a geometry that is able to control the morphing behaviour of some other geometry.
    
    MorphControl(originCurve: NurbsCurve, targetCurve: NurbsCurve)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Morph(self, geometry):
        """
        Morph(self: MorphControl, geometry: GeometryBase) -> bool
        
            Applies the space morph to geometry.
        
            geometry: The geometry to be morphed.
            Returns: true on success, false on failure.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, originCurve, targetCurve):
        """
        __new__(cls: type, originCurve: NurbsCurve, targetCurve: NurbsCurve)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    PreserveStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the morph should be done in a way that preserves the structure
            of the geometry.  In particular, for NURBS objects, true  eans that
            only the control points are moved.  The PreserveStructure value does not
            affect the way meshes and points are morphed. The default is false.

Get: PreserveStructure(self: MorphControl) -> bool

Set: PreserveStructure(self: MorphControl) = value
"""

    QuickPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the morph should be done as quickly as possible because the
            result is being used for some type of dynamic preview.  If QuickPreview
            is true, the tolerance may be ignored. The QuickPreview value does not
            affect the way meshes and points are morphed. The default is false.

Get: QuickPreview(self: MorphControl) -> bool

Set: QuickPreview(self: MorphControl) = value
"""

    SpaceMorphTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 3d fitting tolerance used when morphing surfaces and breps.
            The default is 0.0 and any value <= 0.0 is ignored by morphing functions.
            The value returned by Tolerance does not affect the way meshes and points are morphed.

Get: SpaceMorphTolerance(self: MorphControl) -> float

Set: SpaceMorphTolerance(self: MorphControl) = value
"""



class NurbsCurve(Curve, IDisposable, ISerializable, IEpsilonComparable[NurbsCurve]):
    """
    Represents a Non Uniform Rational B-Splines (NURBS) curve.
    
    NurbsCurve(other: NurbsCurve)
    NurbsCurve(degree: int, pointCount: int)
    NurbsCurve(dimension: int, rational: bool, order: int, pointCount: int)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def Create(periodic, degree, points):
        """ Create(periodic: bool, degree: int, points: IEnumerable[Point3d]) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromArc(arc):
        """
        CreateFromArc(arc: Arc) -> NurbsCurve
        
            Gets a rational degree 2 NURBS curve representation
                    of the arc. Note that the 
             parameterization of NURBS curve
                    does not match arc's transcendental 
             paramaterization.
        
            Returns: Curve on success, null on failure.
        """
        pass

    @staticmethod
    def CreateFromCircle(circle):
        """
        CreateFromCircle(circle: Circle) -> NurbsCurve
        
            Gets a rational degree 2 NURBS curve representation
                    of the circle. Note that the 
             parameterization of NURBS curve
                    does not match circle's transcendental 
             paramaterization.  
                    Use GetRadianFromNurbFormParameter() and
                    
             GetParameterFromRadian() to convert between the NURBS curve 
                    parameter and the 
             transcendental parameter.
        
            Returns: Curve on success, null on failure.
        """
        pass

    @staticmethod
    def CreateFromEllipse(ellipse):
        """
        CreateFromEllipse(ellipse: Ellipse) -> NurbsCurve
        
            Gets a rational degree 2 NURBS curve representation of the ellipse.
                    Note that the 
             parameterization of the NURBS curve does not match
                    with the transcendental 
             paramaterization of the ellipsis.
        
            Returns: A nurbs curve representation of this ellipse or null if no such representation could be made.
        """
        pass

    @staticmethod
    def CreateFromLine(line):
        """
        CreateFromLine(line: Line) -> NurbsCurve
        
            Gets a non-rational, degree 1 Nurbs curve representation of the line.
            Returns: Curve on success, null on failure.
        """
        pass

    @staticmethod
    def CreateSpiral(*__args):
        """
        CreateSpiral(railCurve: Curve, t0: float, t1: float, radiusPoint: Point3d, pitch: float, turnCount: float, radius0: float, radius1: float, pointsPerTurn: int) -> NurbsCurve
        
            Create a C2 non-rational uniform cubic NURBS approximation of a swept helix or spiral.
        
            railCurve: The rail curve.
            t0: Starting portion of rail curve's domain to sweep along.
            t1: Ending portion of rail curve's domain to sweep along.
            radiusPoint: Point used only to get a vector that is perpedicular to the axis. In
                    particular, 
             this vector must not be (anti)parallel to the axis vector.
        
            pitch: The pitch. Positive values produce counter-clockwise orientation,
                    negative values 
             produce clockwise orientation.
        
            turnCount: The turn count. If != 0, then the resulting helix will have this many
                    turns. If = 
             0, then pitch must be != 0 and the approximate distance
                    between turns will be set 
             to pitch. Positive values produce counter-clockwise
                    orientation, negitive values 
             produce clockwise orientation.
        
            radius0: The starting radius. At least one radii must benonzero. Negative values
                    are allowed.
            radius1: The ending radius. At least ont radii must be nonzero. Negative values
                    are allowed.
            pointsPerTurn: Number of points to intepolate per turn. Must be greater than 4.
                    When in doubt, use 
             12.
        
            Returns: NurbsCurve on success, null on failure.
        CreateSpiral(axisStart: Point3d, axisDir: Vector3d, radiusPoint: Point3d, pitch: float, turnCount: float, radius0: float, radius1: float) -> NurbsCurve
        
            Creates a C1 cubic NURBS approximation of a helix or spiral. For a helix,
                    you may 
             have radius0 == radius1. For a spiral radius0 == radius0 produces
                    a circle. Zero 
             and negative radii are permissible.
        
        
            axisStart: Helix's axis starting point or center of spiral.
            axisDir: Helix's axis vector or normal to spiral's plane.
            radiusPoint: Point used only to get a vector that is perpedicular to the axis. In
                    particular, 
             this vector must not be (anti)parallel to the axis vector.
        
            pitch: The pitch, where a spiral has a pitch = 0, and pitch > 0 is the distance
                    between 
             the helix's "threads".
        
            turnCount: The number of turns in spiral or helix. Positive
                    values produce counter-clockwise 
             orientation, negitive values produce
                    clockwise orientation. Note, for a helix, 
             turnCount * pitch = length of
                    the helix's axis.
        
            radius0: The starting radius.
            radius1: The ending radius.
            Returns: NurbsCurve on success, null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsCurve, other: NurbsCurve, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def GrevilleParameter(self, index):
        """
        GrevilleParameter(self: NurbsCurve, index: int) -> float
        
            Gets the greville (edit point) parameter that belongs 
                    to the control point at the 
             specified index.
        
        
            index: Index of Greville (Edit) point.
        """
        pass

    def GrevilleParameters(self):
        """
        GrevilleParameters(self: NurbsCurve) -> Array[float]
        
            Gets all Greville (Edit point) parameters for this curve.
        """
        pass

    def GrevillePoint(self, index):
        """
        GrevillePoint(self: NurbsCurve, index: int) -> Point3d
        
            Gets the greville (edit point) parameter that belongs 
                    to the control point at the 
             specified index.
        
        
            index: Index of Greville (Edit) point.
        """
        pass

    def GrevillePoints(self):
        """
        GrevillePoints(self: NurbsCurve) -> Point3dList
        
            Gets all Greville (Edit) points for this curve.
        """
        pass

    def IncreaseDegree(self, desiredDegree):
        """
        IncreaseDegree(self: NurbsCurve, desiredDegree: int) -> bool
        
            Increase the degree of this curve.
        
            desiredDegree: The desired degree. 
                    Degrees should be number between and including 1 and 11.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def IsDuplicate(curveA, curveB, ignoreParameterization, tolerance):
        """
        IsDuplicate(curveA: NurbsCurve, curveB: NurbsCurve, ignoreParameterization: bool, tolerance: float) -> bool
        
            Determines if two curves are similar.
        
            curveA: First curve used in comparison.
            curveB: Second curve used in comparison.
            ignoreParameterization: if true, parameterization and orientaion are ignored.
            tolerance: tolerance to use when comparing control points.
            Returns: true if curves are similar within tolerance.
        """
        pass

    def MakePiecewiseBezier(self, setEndWeightsToOne):
        """
        MakePiecewiseBezier(self: NurbsCurve, setEndWeightsToOne: bool) -> bool
        
            Clamps ends and adds knots so the NURBS curve has bezier spans 
                    (all distinct knots 
             have multiplitity = degree).
        
        
            setEndWeightsToOne: If true and the first or last weight is not one, then the first and
                    last spans are 
             reparameterized so that the end weights are one.
        
            Returns: true on success, false on failure.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def Reparameterize(self, c):
        """
        Reparameterize(self: NurbsCurve, c: float) -> bool
        
            Use a linear fractional transformation to reparameterize the NURBS curve.
                    This does 
             not change the curve's domain.
        
        
            c: reparameterization constant (generally speaking, c should be > 0). The
                    control 
             points and knots are adjusted so that
                    output_nurbs(t) = input_nurbs(lambda(t)), 
             where lambda(t) = c*t/( (c-1)*t + 1 ).
                    Note that lambda(0) = 0, lambda(1) = 1, 
             lambda'(t) > 0, 
                    lambda'(0) = c and lambda'(1) = 1/c.
        
            Returns: true if successful.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, other: NurbsCurve)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, degree: int, pointCount: int)
        __new__(cls: type, dimension: int, rational: bool, order: int, pointCount: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasBezierSpans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the NURBS curve has bezier spans (all distinct knots have multiplitity = degree)

Get: HasBezierSpans(self: NurbsCurve) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the curve is rational. 
            Rational curves have control-points with custom weights.

Get: IsRational(self: NurbsCurve) -> bool

"""

    Knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the knots (or "knot vector") of this nurbs curve.

Get: Knots(self: NurbsCurve) -> NurbsCurveKnotList

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order of the curve. Order = Degree + 1.

Get: Order(self: NurbsCurve) -> int

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the control points of this nurbs curve.

Get: Points(self: NurbsCurve) -> NurbsCurvePointList

"""



class NurbsSurface(Surface, IDisposable, ISerializable, IEpsilonComparable[NurbsSurface]):
    """
    Represents a Non Uniform Rational B-Splines (NURBS) surface.
    
    NurbsSurface(other: NurbsSurface)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def CopyFrom(self, other):
        """
        CopyFrom(self: NurbsSurface, other: NurbsSurface)
            Copies this NURBS surface from another NURBS surface.
        
            other: The other NURBS surface to use as source.
        """
        pass

    @staticmethod
    def Create(dimension, isRational, order0, order1, controlPointCount0, controlPointCount1):
        """
        Create(dimension: int, isRational: bool, order0: int, order1: int, controlPointCount0: int, controlPointCount1: int) -> NurbsSurface
        
            Constructs a new NURBS surface with internal uninitialized arrays.
        
            dimension: The number of dimensions.>= 1. This value is usually 3.
            isRational: true to make a rational NURBS.
            order0: The order in U direction.>= 2.
            order1: The order in V direction.>= 2.
            controlPointCount0: Control point count in U direction.>= order0.
            controlPointCount1: Control point count in V direction.>= order1.
            Returns: A new NURBS surface, or null on error.
        """
        pass

    @staticmethod
    def CreateFromCone(cone):
        """
        CreateFromCone(cone: Cone) -> NurbsSurface
        
            Constructs a new NURBS surfaces from cone data.
        
            cone: A cone value.
            Returns: A new NURBS surface, or null on error.
        """
        pass

    @staticmethod
    def CreateFromCorners(corner1, corner2, corner3, corner4=None, tolerance=None):
        """
        CreateFromCorners(corner1: Point3d, corner2: Point3d, corner3: Point3d) -> NurbsSurface
        
            Makes a surface from 3 corner points.
        
            corner1: The first corner.
            corner2: The second corner.
            corner3: The third corner.
            Returns: The resulting surface or null on error.
        CreateFromCorners(corner1: Point3d, corner2: Point3d, corner3: Point3d, corner4: Point3d, tolerance: float) -> NurbsSurface
        
            Makes a surface from 4 corner points.
        
            corner1: The first corner.
            corner2: The second corner.
            corner3: The third corner.
            corner4: The fourth corner.
            tolerance: Minimum edge length without collapsing to a singularity.
            Returns: The resulting surface or null on error.
        CreateFromCorners(corner1: Point3d, corner2: Point3d, corner3: Point3d, corner4: Point3d) -> NurbsSurface
        
            Makes a surface from 4 corner points.
                    This is the same as calling 
             Rhino.Geometry.NurbsSurface.CreateFromCorners(Rhino.Geometry.Point3d,Rhino.Geometry.Point3d,Rhino
             .Geometry.Point3d,Rhino.Geometry.Point3d,System.Double) with tolerance 0.
        
        
            corner1: The first corner.
            corner2: The second corner.
            corner3: The third corner.
            corner4: The fourth corner.
            Returns: the resulting surface or null on error.
        """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder):
        """
        CreateFromCylinder(cylinder: Cylinder) -> NurbsSurface
        
            Constructs a new NURBS surfaces from cylinder data.
        
            cylinder: A cylinder value.
            Returns: A new NURBS surface, or null on error.
        """
        pass

    @staticmethod
    def CreateFromPoints(points, uCount, vCount, uDegree, vDegree):
        """ CreateFromPoints(points: IEnumerable[Point3d], uCount: int, vCount: int, uDegree: int, vDegree: int) -> NurbsSurface """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """
        CreateFromSphere(sphere: Sphere) -> NurbsSurface
        
            Constructs a new NURBS surfaces from sphere data.
        
            sphere: A sphere value.
            Returns: A new NURBS surface, or null on error.
        """
        pass

    @staticmethod
    def CreateFromTorus(torus):
        """
        CreateFromTorus(torus: Torus) -> NurbsSurface
        
            Constructs a new NURBS surfaces from torus data.
        
            torus: A torus value.
            Returns: A new NURBS surface, or null on error.
        """
        pass

    @staticmethod
    def CreateNetworkSurface(*__args):
        """
        CreateNetworkSurface(curves: IEnumerable[Curve], continuity: int, edgeTolerance: float, interiorTolerance: float, angleTolerance: float) -> (NurbsSurface, int)
        CreateNetworkSurface(uCurves: IEnumerable[Curve], uContinuityStart: int, uContinuityEnd: int, vCurves: IEnumerable[Curve], vContinuityStart: int, vContinuityEnd: int, edgeTolerance: float, interiorTolerance: float, angleTolerance: float) -> (NurbsSurface, int)
        """
        pass

    @staticmethod
    def CreateRailRevolvedSurface(profile, rail, axis, scaleHeight):
        """
        CreateRailRevolvedSurface(profile: Curve, rail: Curve, axis: Line, scaleHeight: bool) -> NurbsSurface
        
            Constructs a railed Surface-of-Revolution.
        
            profile: Profile curve for revolution.
            rail: Rail curve for revolution.
            axis: Axis of revolution.
            scaleHeight: If true, surface will be locally scaled.
            Returns: A NurbsSurface or null on failure.
        """
        pass

    @staticmethod
    def CreateRuledSurface(curveA, curveB):
        """
        CreateRuledSurface(curveA: Curve, curveB: Curve) -> NurbsSurface
        
            Constructs a ruled surface between two curves. Curves must share the same knot-vector.
        
            curveA: First curve.
            curveB: Second curve.
            Returns: A ruled surface on success or null on failure.
        """
        pass

    @staticmethod
    def CreateThroughPoints(points, uCount, vCount, uDegree, vDegree, uClosed, vClosed):
        """ CreateThroughPoints(points: IEnumerable[Point3d], uCount: int, vCount: int, uDegree: int, vDegree: int, uClosed: bool, vClosed: bool) -> NurbsSurface """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsSurface, other: NurbsSurface, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def IncreaseDegreeU(self, desiredDegree):
        """
        IncreaseDegreeU(self: NurbsSurface, desiredDegree: int) -> bool
        
            Increase the degree of this surface in U direction.
        
            desiredDegree: The desired degree. 
                    Degrees should be number between and including 1 and 11.
            Returns: true on success, false on failure.
        """
        pass

    def IncreaseDegreeV(self, desiredDegree):
        """
        IncreaseDegreeV(self: NurbsSurface, desiredDegree: int) -> bool
        
            Increase the degree of this surface in V direction.
        
            desiredDegree: The desired degree. 
                    Degrees should be number between and including 1 and 11.
            Returns: true on success, false on failure.
        """
        pass

    def MakeNonRational(self):
        """
        MakeNonRational(self: NurbsSurface) -> bool
        
            Makes this surface non-rational.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def MakeRational(self):
        """
        MakeRational(self: NurbsSurface) -> bool
        
            Makes this surface rational.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, other):
        """
        __new__(cls: type, other: NurbsSurface)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the nurbs surface is rational.

Get: IsRational(self: NurbsSurface) -> bool

"""

    KnotsU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The U direction knot vector.

Get: KnotsU(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

    KnotsV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The V direction knot vector.

Get: KnotsV(self: NurbsSurface) -> NurbsSurfaceKnotList

"""

    OrderU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order in the U direction.

Get: OrderU(self: NurbsSurface) -> int

"""

    OrderV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order in the V direction.

Get: OrderV(self: NurbsSurface) -> int

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of surface control points that form this surface.

Get: Points(self: NurbsSurface) -> NurbsSurfacePointList

"""



class OrdinateDimension(AnnotationBase, IDisposable, ISerializable):
    """
    Represents the geometry of a dimension that displays a coordinate of a point.
                This class refers to the geometric element that is independent from the document.
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Particle(object):
    """
    Represents a simple particle.
                This base class only defines position and display properties (size, color, bitmap id).
                You will most likely create a class that derives from this particle class to perform some
                sort of physical simulation (movement over time or frames).
    
    Particle()
    """
    def Update(self):
        """
        Update(self: Particle)
            Base class implementation does nothing.
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Particle) -> Color

Set: Color(self: Particle) = value
"""

    DisplayBitmapIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayBitmapIndex(self: Particle) -> int

Set: DisplayBitmapIndex(self: Particle) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index in ParentSystem for this Particle. Can change when the particle
            system is modified.

Get: Index(self: Particle) -> int

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """3d Location of the Particle.

Get: Location(self: Particle) -> Point3d

Set: Location(self: Particle) = value
"""

    ParentSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent particle system of this particle.

Get: ParentSystem(self: Particle) -> ParticleSystem

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: Particle) -> Single

Set: Size(self: Particle) = value
"""



class ParticleSystem(object, IEnumerable[Particle], IEnumerable):
    """ ParticleSystem() """
    def Add(self, particle):
        """
        Add(self: ParticleSystem, particle: Particle) -> bool
        
            Adds a particle to this ParticleSystem. A Particle can only be in one system
                    at a 
             time.  If the Particle already exists in a different system, this function
                    will 
             return false. You should remove the particle from the other system first
                    before 
             adding it.
        
        
            particle: A particle to be added.
            Returns: true if this particle was added to the system or if is already in the system.
                    false 
             if the particle already exists in a different system.
        """
        pass

    def Clear(self):
        """
        Clear(self: ParticleSystem)
            Remove all Particles from this system.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ParticleSystem) -> IEnumerator[Particle] """
        pass

    def Remove(self, particle):
        """
        Remove(self: ParticleSystem, particle: Particle)
            Removes a single particle from this system.
        
            particle: The particle to be removed.
        """
        pass

    def Update(self):
        """
        Update(self: ParticleSystem)
            Calls Update on every particle in the system.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Particle](enumerable: IEnumerable[Particle], value: Particle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: ParticleSystem) -> BoundingBox

"""

    DisplaySizesInWorldUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplaySizesInWorldUnits(self: ParticleSystem) -> bool

Set: DisplaySizesInWorldUnits(self: ParticleSystem) = value
"""

    DrawRequiresDepthSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawRequiresDepthSorting(self: ParticleSystem) -> bool

Set: DrawRequiresDepthSorting(self: ParticleSystem) = value
"""



class PipeCapMode(Enum, IComparable, IFormattable, IConvertible):
    """
    constansts used for CreatePipe functions
    
    enum PipeCapMode, values: Flat (1), None (0), Round (2)
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

    Flat = None
    None = None
    Round = None
    value__ = None


class Plane(object, IEquatable[Plane], IEpsilonComparable[Plane]):
    """
    Represents the value of a center point and two axes in a plane in three dimensions.
    
    Plane(other: Plane)
    Plane(origin: Point3d, normal: Vector3d)
    Plane(origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
    Plane(origin: Point3d, xPoint: Point3d, yPoint: Point3d)
    Plane(a: float, b: float, c: float, d: float)
    """
    def ClosestParameter(self, testPoint, s, t):
        """
        ClosestParameter(self: Plane, testPoint: Point3d) -> (bool, float, float)
        
            Gets the parameters of the point on the plane closest to a test point.
        
            testPoint: Point to get close to.
            Returns: true if a parameter could be found, 
                    false if the point could not be projected 
             successfully.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: Plane, testPoint: Point3d) -> Point3d
        
            Gets the point on the plane closest to a test point.
        
            testPoint: Point to get close to.
            Returns: The point on the plane that is closest to testPoint, 
                    or Point3d.Unset on failure.
        """
        pass

    def DistanceTo(self, testPoint):
        """
        DistanceTo(self: Plane, testPoint: Point3d) -> float
        
            Returns the signed distance from testPoint to its projection onto this plane. 
                    If 
             the point is below the plane, a negative distance is returned.
        
        
            testPoint: Point to test.
            Returns: Signed distance from this plane to testPoint.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Plane, other: Plane, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Plane, plane: Plane) -> bool
        
            Determines if another plane has the same components as this plane.
        
            plane: A plane.
            Returns: true if plane has the same components as this plane; false otherwise.
        Equals(self: Plane, obj: object) -> bool
        
            Determines if an object is a plane and has the same components as this plane.
        
            obj: An object.
            Returns: true if obj is a plane and has the same components as this plane; false otherwise.
        """
        pass

    def ExtendThroughBox(self, box, s, t):
        """
        ExtendThroughBox(self: Plane, box: Box) -> (bool, Interval, Interval)
        
            Extend this plane through a Box.
        
            box: A box to use for extension.
            Returns: true on success, false on failure.
        ExtendThroughBox(self: Plane, box: BoundingBox) -> (bool, Interval, Interval)
        
            Extends this plane through a bounding box.
        
            box: A box to use as minimal extension boundary.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def FitPlaneToPoints(points, plane, maximumDeviation=None):
        """
        FitPlaneToPoints(points: IEnumerable[Point3d]) -> (PlaneFitResult, Plane, float)
        FitPlaneToPoints(points: IEnumerable[Point3d]) -> (PlaneFitResult, Plane)
        """
        pass

    def Flip(self):
        """
        Flip(self: Plane)
            Flip this plane by swapping out the X and Y axes and inverting the Z axis.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Plane) -> int
        
            Gets a non-unique hashing code for this entity.
            Returns: A particular number for a specific instance of plane.
        """
        pass

    def GetPlaneEquation(self):
        """
        GetPlaneEquation(self: Plane) -> Array[float]
        
            Gets the plane equation for this plane in the format of Ax+By+Cz+D=0.
            Returns: Array of four values.
        """
        pass

    def PointAt(self, u, v, w=None):
        """
        PointAt(self: Plane, u: float, v: float, w: float) -> Point3d
        
            Evaluate a point on the plane.
        
            u: evaulation parameter.
            v: evaulation parameter.
            w: evaulation parameter.
            Returns: plane.origin + u*plane.xaxis + v*plane.yaxis + z*plane.zaxis.
        PointAt(self: Plane, u: float, v: float) -> Point3d
        
            Evaluate a point on the plane.
        
            u: evaulation parameter.
            v: evaulation parameter.
            Returns: plane.origin + u*plane.xaxis + v*plane.yaxis.
        """
        pass

    def RemapToPlaneSpace(self, ptSample, ptPlane):
        """
        RemapToPlaneSpace(self: Plane, ptSample: Point3d) -> (bool, Point3d)
        
            Convert a point from World space coordinates into Plane space coordinates.
        
            ptSample: World point to remap.
            Returns: true on success, false on failure.
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Plane, angle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        
            Rotate the plane about a custom anchor point.
        
            angle: Angle in radians.
            axis: Axis of rotation.
            centerOfRotation: Center of rotation.
            Returns: true on success, false on failure.
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d, centerOfRotation: Point3d) -> bool
        
            Rotate the plane about a custom anchor point.
        
            sinAngle: Sin(angle)
            cosAngle: Cos(angle)
            axis: Axis of rotation.
            centerOfRotation: Center of rotation.
            Returns: true on success, false on failure.
        Rotate(self: Plane, sinAngle: float, cosAngle: float, axis: Vector3d) -> bool
        
            Rotate the plane about its origin point.
        
            sinAngle: Sin(angle).
            cosAngle: Cos(angle).
            axis: Axis of rotation.
            Returns: true on success, false on failure.
        Rotate(self: Plane, angle: float, axis: Vector3d) -> bool
        
            Rotate the plane about its origin point.
        
            angle: Angle in radians.
            axis: Axis of rotation.
            Returns: true on success, false on failure.
        """
        pass

    def ToString(self):
        """
        ToString(self: Plane) -> str
        
            Constructs the string representation of this plane.
            Returns: Text.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Plane, xform: Transform) -> bool
        
            Transform the plane with a Transformation matrix.
        
            xform: Transformation to apply to plane.
            Returns: true on success, false on failure.
        """
        pass

    def Translate(self, delta):
        """
        Translate(self: Plane, delta: Vector3d) -> bool
        
            Translate (move) the plane along a vector.
        
            delta: Translation (motion) vector.
            Returns: true on success, false on failure.
        """
        pass

    def ValueAt(self, p):
        """
        ValueAt(self: Plane, p: Point3d) -> float
        
            Get the value of the plane equation at the point.
        
            p: evaulation point.
            Returns: returns pe[0]*p.X + pe[1]*p.Y + pe[2]*p.Z + pe[3] where
                    pe[0], pe[1], pe[2] and 
             pe[3] are the coeeficients of the plane equation.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Plane]() -> Plane
        
        __new__(cls: type, other: Plane)
        __new__(cls: type, origin: Point3d, normal: Vector3d)
        __new__(cls: type, origin: Point3d, xDirection: Vector3d, yDirection: Vector3d)
        __new__(cls: type, origin: Point3d, xPoint: Point3d, yPoint: Point3d)
        __new__(cls: type, a: float, b: float, c: float, d: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this is a valid plane. 
            A plane is considered to be valid when all fields contain reasonable 
            information and the equation jibes with point and zaxis.

Get: IsValid(self: Plane) -> bool

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the normal of this plane. This is essentially the ZAxis of the plane.

Get: Normal(self: Plane) -> Vector3d

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the origin point of this plane.

Get: Origin(self: Plane) -> Point3d

Set: Origin(self: Plane) = value
"""

    OriginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X coordinate of the origin of this plane.

Get: OriginX(self: Plane) -> float

Set: OriginX(self: Plane) = value
"""

    OriginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y coordinate of the origin of this plane.

Get: OriginY(self: Plane) -> float

Set: OriginY(self: Plane) = value
"""

    OriginZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z coordinate of the origin of this plane.

Get: OriginZ(self: Plane) -> float

Set: OriginZ(self: Plane) = value
"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X axis vector of this plane.

Get: XAxis(self: Plane) -> Vector3d

Set: XAxis(self: Plane) = value
"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y axis vector of this plane.

Get: YAxis(self: Plane) -> Vector3d

Set: YAxis(self: Plane) = value
"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z axis vector of this plane.

Get: ZAxis(self: Plane) -> Vector3d

Set: ZAxis(self: Plane) = value
"""


    Unset = None
    WorldXY = None
    WorldYZ = None
    WorldZX = None


class PlaneFitResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all possible outcomes of a Least-Squares plane fitting operation.
    
    enum PlaneFitResult, values: Failure (-1), Inconclusive (1), Success (0)
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

    Failure = None
    Inconclusive = None
    Success = None
    value__ = None


class Point2d(object, ISerializable, IEquatable[Point2d], IComparable[Point2d], IComparable, IEpsilonComparable[Point2d]):
    """
    Represents the two coordinates of a point in two-dimensional space,
                using System.Double-precision floating point numbers.
    
    Point2d(x: float, y: float)
    Point2d(vector: Vector2d)
    Point2d(point: Point2d)
    Point2d(point: Point3d)
    """
    @staticmethod
    def Add(*__args):
        """
        Add(point1: Point2d, point2: Point2d) -> Point2d
        
            Adds a point with a point.
                    (Provided for languages that do not support operator 
             overloading. You can use the + operator otherwise)
        
        
            point1: A point.
            point2: A point.
            Returns: A new point that is coordinatewise summed with the other point.
        Add(vector: Vector2d, point: Point2d) -> Point2d
        
            Adds a vector with a point.
                    (Provided for languages that do not support operator 
             overloading. You can use the + operator otherwise)
        
        
            vector: A vector.
            point: A point.
            Returns: A new point that is coordinatewise summed with the vector.
        Add(point: Point2d, vector: Vector2d) -> Point2d
        
            Adds a point with a vector.
                    (Provided for languages that do not support operator 
             overloading. You can use the + operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that is coordinatewise summed with the vector.
        """
        pass

    def CompareTo(self, other):
        """
        CompareTo(self: Point2d, other: Point2d) -> int
        
            Compares this Rhino.Geometry.Point2d with another Rhino.Geometry.Point2d.
                    
             Coordinates evaluation priority is first X, then Y.
        
        
            other: The other Rhino.Geometry.Point2d to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y+1: otherwise.
        """
        pass

    def DistanceTo(self, other):
        """
        DistanceTo(self: Point2d, other: Point2d) -> float
        
            Computes the distance between two points.
        
            other: Another point.
            Returns: The length of the line between the two points, or 0 if either point is invalid.
        """
        pass

    @staticmethod
    def Divide(point, t):
        """
        Divide(point: Point2d, t: float) -> Point2d
        
            Divides a Rhino.Geometry.Point2d by a number.
                    (Provided for languages that do not 
             support operator overloading. You can use the / operator otherwise)
        
        
            point: A point.
            t: A number.
            Returns: A new point that is coordinatewise divided by t.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Point2d, other: Point2d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point2d, point: Point2d) -> bool
        
            Determines whether the specified Point2d has the same values as the present point.
        
            point: The specified point.
            Returns: true if point has the same coordinates as this; otherwise false.
        Equals(self: Point2d, obj: object) -> bool
        
            Determines whether the specified System.Object is a Point2d and has the same values as the 
             present point.
        
        
            obj: The specified object.
            Returns: true if obj is a Point2d and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point2d) -> int
        
            Computes a hash number that represents the current point.
            Returns: A hash code that is not unique for each point.
        """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: float, point: Point2d) -> Point2d
        
            Multiplies a Rhino.Geometry.Point2d by a number.
                    (Provided for languages that do 
             not support operator overloading. You can use the * operator otherwise)
        
        
            t: A number.
            point: A point.
            Returns: A new point that is coordinatewise multiplied by t.
        Multiply(point: Point2d, t: float) -> Point2d
        
            Multiplies a Rhino.Geometry.Point2d by a number.
                    (Provided for languages that do 
             not support operator overloading. You can use the * operator otherwise)
        
        
            point: A point.
            t: A number.
            Returns: A new point that is coordinatewise multiplied by t.
        """
        pass

    @staticmethod
    def Subtract(*__args):
        """
        Subtract(point1: Point2d, point2: Point2d) -> Vector2d
        
            Subtracts the second point from the first point.
                    (Provided for languages that do 
             not support operator overloading. You can use the - operator otherwise)
        
        
            point1: A point (minuend).
            point2: A point (subtrahend).
            Returns: A new vector that is point1 coordinatewise subtracted by point2.
        Subtract(point: Point2d, vector: Vector2d) -> Point2d
        
            Subtracts a vector from a point.
                    (Provided for languages that do not support 
             operator overloading. You can use the - operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that is coordinatewise subtracted by vector.
        """
        pass

    def ToString(self):
        """
        ToString(self: Point2d) -> str
        
            Constructs the string representation for the current point.
            Returns: The point representation in the form X,Y.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Point2d, xform: Transform)
            Transforms the present point in place. The transformation matrix acts on the left of the point. 
             i.e.,
                    result = transformation*point
        
        
            xform: Transformation to apply.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point2d]() -> Point2d
        
        __new__(cls: type, x: float, y: float)
        __new__(cls: type, vector: Vector2d)
        __new__(cls: type, point: Point2d)
        __new__(cls: type, point: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(point1: Point2d, point2: Point2d) -> Point2d
        
            Adds a point with a point.
        
            point1: A point.
            point2: A point.
            Returns: A new point that is coordinatewise summed with the other point.
        __radd__(vector: Vector2d, point: Point2d) -> Point2d
        
            Adds a vector with a point.
        
            vector: A vector.
            point: A point.
            Returns: A new point that is coordinatewise summed with the vector.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(t: float, point: Point2d) -> Point2d
        
            Multiplies a Rhino.Geometry.Point2d by a number.
        
            t: A number.
            point: A point.
            Returns: A new point that is coordinatewise multiplied by t.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(point1: Point2d, point2: Point2d) -> Vector2d
        
            Subtracts point2 from point1.
        
            point1: A point (minuend).
            point2: A point (subtrahend).
            Returns: A new vector that is point1 coordinatewise subtracted by point2.
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If any coordinate of a point is UnsetValue, then the point is not valid.

Get: IsValid(self: Point2d) -> bool

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the largest valid coordinate, or RhinoMath.UnsetValue if no coordinate is valid.

Get: MaximumCoordinate(self: Point2d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the smallest (both positive and negative) valid coordinate, or RhinoMath.UnsetValue if no coordinate is valid.

Get: MinimumCoordinate(self: Point2d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) coordinate of the point.

Get: X(self: Point2d) -> float

Set: X(self: Point2d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) coordinate of the point.

Get: Y(self: Point2d) -> float

Set: Y(self: Point2d) = value
"""


    Origin = None
    Unset = None


class Point2f(object, IEquatable[Point2f], IComparable[Point2f], IComparable, IEpsilonFComparable[Point2f]):
    """
    Represents the two coordinates of a point in two-dimensional space,
                using System.Single-precision floating point numbers.
    
    Point2f(x: Single, y: Single)
    Point2f(x: float, y: float)
    """
    def CompareTo(self, other):
        """
        CompareTo(self: Point2f, other: Point2f) -> int
        
            Compares this Rhino.Geometry.Point2f with another Rhino.Geometry.Point2f.
                    
             Coordinates evaluation priority is first X, then Y.
        
        
            other: The other Rhino.Geometry.Point2f to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y+1: otherwise.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Point2f, other: Point2f, epsilon: Single) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point2f, point: Point2f) -> bool
        
            Determines whether the specified Rhino.Geometry.Point2f has the same values as the present point.
        
            point: The specified point.
            Returns: true if point has the same coordinates as this; otherwise false.
        Equals(self: Point2f, obj: object) -> bool
        
            Determines whether the specified System.Object is a Rhino.Geometry.Point2f and has the same 
             values as the present point.
        
        
            obj: The specified object.
            Returns: true if obj is Point2f and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point2f) -> int
        
            Computes a hash number that represents the current point.
            Returns: A hash code that is not unique for each point.
        """
        pass

    def ToString(self):
        """
        ToString(self: Point2f) -> str
        
            Constructs the string representation for the current point.
            Returns: The point representation in the form X,Y.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__[Point2f]() -> Point2f
        
        __new__(cls: type, x: Single, y: Single)
        __new__(cls: type, x: float, y: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this point is considered valid.

Get: IsValid(self: Point2f) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of the vector.

Get: X(self: Point2f) -> Single

Set: X(self: Point2f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of the vector.

Get: Y(self: Point2f) -> Single

Set: Y(self: Point2f) = value
"""


    Unset = None


class Point3d(object, ISerializable, IEquatable[Point3d], IComparable[Point3d], IComparable, IEpsilonComparable[Point3d]):
    """
    Represents the three coordinates of a point in three-dimensional space,
                using System.Double-precision floating point values.
    
    Point3d(x: float, y: float, z: float)
    Point3d(vector: Vector3d)
    Point3d(point: Point3f)
    Point3d(point: Point3d)
    Point3d(point: Point4d)
    """
    @staticmethod
    def Add(*__args):
        """
        Add(point: Point3d, vector: Vector3f) -> Point3d
        
            Sums up a point and a vector, and returns a new point.
                    (Provided for languages that 
             do not support operator overloading. You can use the + operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that results from the addition of point and vector.
        Add(vector: Vector3d, point: Point3d) -> Point3d
        
            Sums up a point and a vector, and returns a new point.
                    (Provided for languages that 
             do not support operator overloading. You can use the + operator otherwise)
        
        
            vector: A vector.
            point: A point.
            Returns: A new point that results from the addition of point and vector.
        Add(point1: Point3d, point2: Point3d) -> Point3d
        
            Sums two Rhino.Geometry.Point3d instances.
                    (Provided for languages that do not 
             support operator overloading. You can use the + operator otherwise)
        
        
            point1: A point.
            point2: A point.
            Returns: A new point that results from the addition of point1 and point2.
        Add(point: Point3d, vector: Vector3d) -> Point3d
        
            Sums up a point and a vector, and returns a new point.
                    (Provided for languages that 
             do not support operator overloading. You can use the + operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that results from the addition of point and vector.
        """
        pass

    @staticmethod
    def ArePointsCoplanar(points, tolerance):
        """ ArePointsCoplanar(points: IEnumerable[Point3d], tolerance: float) -> bool """
        pass

    def CompareTo(self, other):
        """
        CompareTo(self: Point3d, other: Point3d) -> int
        
            Compares this Rhino.Geometry.Point3d with another Rhino.Geometry.Point3d.
                    Component 
             evaluation priority is first X, then Y, then Z.
        
        
            other: The other Rhino.Geometry.Point3d to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
        """
        pass

    @staticmethod
    def CullDuplicates(points, tolerance):
        """ CullDuplicates(points: IEnumerable[Point3d], tolerance: float) -> Array[Point3d] """
        pass

    def DistanceTo(self, other):
        """
        DistanceTo(self: Point3d, other: Point3d) -> float
        
            Computes the distance between two points.
        
            other: Other point for distance measurement.
            Returns: The length of the line between this and the other point; or 0 if any of the points is not valid.
        """
        pass

    @staticmethod
    def Divide(point, t):
        """
        Divide(point: Point3d, t: float) -> Point3d
        
            Divides a Rhino.Geometry.Point3d by a number.
                    (Provided for languages that do not 
             support operator overloading. You can use the / operator otherwise)
        
        
            point: A point.
            t: A number.
            Returns: A new point that is coordinatewise divided by t.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Point3d, other: Point3d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point3d, point: Point3d) -> bool
        
            Determines whether the specified Rhino.Geometry.Point3d has the same values as the present point.
        
            point: The specified point.
            Returns: true if point has the same coordinates as this; otherwise false.
        Equals(self: Point3d, obj: object) -> bool
        
            Determines whether the specified System.Object is a Rhino.Geometry.Point3d and has the same 
             values as the present point.
        
        
            obj: The specified object.
            Returns: true if obj is a Point3d and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point3d) -> int
        
            Computes a hash code for the present point.
            Returns: A non-unique integer that represents this point.
        """
        pass

    def Interpolate(self, pA, pB, t):
        """
        Interpolate(self: Point3d, pA: Point3d, pB: Point3d, t: float)
            Interpolate between two points.
        
            pA: First point.
            pB: Second point.
            t: Interpolation parameter. 
                    If t=0 then this point is set to pA. 
                    If t=1 
             then this point is set to pB. 
                    Values of t in between 0.0 and 1.0 result in points 
             between pA and pB.
        """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: float, point: Point3d) -> Point3d
        
            Multiplies a Rhino.Geometry.Point3d by a number.
                    (Provided for languages that do 
             not support operator overloading. You can use the * operator otherwise)
        
        
            t: A number.
            point: A point.
            Returns: A new point that is coordinatewise multiplied by t.
        Multiply(point: Point3d, t: float) -> Point3d
        
            Multiplies a Rhino.Geometry.Point3d by a number.
                    (Provided for languages that do 
             not support operator overloading. You can use the * operator otherwise)
        
        
            point: A point.
            t: A number.
            Returns: A new point that is coordinatewise multiplied by t.
        """
        pass

    @staticmethod
    def SortAndCullPointList(points, minimumDistance):
        """ SortAndCullPointList(points: IEnumerable[Point3d], minimumDistance: float) -> Array[Point3d] """
        pass

    @staticmethod
    def Subtract(*__args):
        """
        Subtract(point1: Point3d, point2: Point3d) -> Vector3d
        
            Subtracts a point from another point.
                    (Provided for languages that do not support 
             operator overloading. You can use the - operator otherwise)
        
        
            point1: A point.
            point2: Another point.
            Returns: A new vector that is the difference of point minus vector.
        Subtract(point: Point3d, vector: Vector3d) -> Point3d
        
            Subtracts a vector from a point.
                    (Provided for languages that do not support 
             operator overloading. You can use the - operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that is the difference of point minus vector.
        """
        pass

    def ToString(self):
        """
        ToString(self: Point3d) -> str
        
            Constructs the string representation for the current point.
            Returns: The point representation in the form X,Y,Z.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Point3d, xform: Transform)
            Transforms the present point in place. The transformation matrix acts on the left of the point. 
             i.e.,
                    result = transformation*point
        
        
            xform: Transformation to apply.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point3d]() -> Point3d
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, vector: Vector3d)
        __new__(cls: type, point: Point3f)
        __new__(cls: type, point: Point3d)
        __new__(cls: type, point: Point4d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(vector: Vector3d, point: Point3d) -> Point3d
        
            Sums up a point and a vector, and returns a new point.
        
            vector: A vector.
            point: A point.
            Returns: A new point that results from the addition of point and vector.
        __radd__(point1: Point3d, point2: Point3d) -> Point3d
        
            Sums two Rhino.Geometry.Point3d instances.
        
            point1: A point.
            point2: A point.
            Returns: A new point that results from the addition of point1 and point2.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(t: float, point: Point3d) -> Point3d
        
            Multiplies a Rhino.Geometry.Point3d by a number.
        
            t: A number.
            point: A point.
            Returns: A new point that is coordinatewise multiplied by t.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(point1: Point3d, point2: Point3d) -> Vector3d
        
            Subtracts a point from another point.
        
            point1: A point.
            point2: Another point.
            Returns: A new vector that is the difference of point minus vector.
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Each coordinate of the point must pass the Rhino.RhinoMath.IsValidDouble(System.Double) test.

Get: IsValid(self: Point3d) -> bool

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the largest (both positive and negative) valid coordinate in this point,
            or RhinoMath.UnsetValue if no coordinate is valid.

Get: MaximumCoordinate(self: Point3d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the smallest (both positive and negative) coordinate value in this point.

Get: MinimumCoordinate(self: Point3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) coordinate of this point.

Get: X(self: Point3d) -> float

Set: X(self: Point3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) coordinate of this point.

Get: Y(self: Point3d) -> float

Set: Y(self: Point3d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z (third) coordinate of this point.

Get: Z(self: Point3d) -> float

Set: Z(self: Point3d) = value
"""


    Origin = None
    Unset = None


class Point3dGrid(GeometryBase, IDisposable, ISerializable):
    """
    Represents a rectangular grid of 3D points.
    
    Point3dGrid()
    Point3dGrid(rows: int, columns: int)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, rows=None, columns=None):
        """
        __new__(cls: type)
        __new__(cls: type, rows: int, columns: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Point3f(object, IEquatable[Point3f], IComparable[Point3f], IComparable, IEpsilonFComparable[Point3f]):
    """
    Represents the three coordinates of a point in three-dimensional space,
                using System.Single-precision floating point numbers.
    
    Point3f(x: Single, y: Single, z: Single)
    """
    def CompareTo(self, other):
        """
        CompareTo(self: Point3f, other: Point3f) -> int
        
            Compares this Rhino.Geometry.Point3f with another Rhino.Geometry.Point3f.
                    Component 
             evaluation priority is first X, then Y, then Z.
        
        
            other: The other Rhino.Geometry.Point3d to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
        """
        pass

    def DistanceTo(self, other):
        """
        DistanceTo(self: Point3f, other: Point3f) -> float
        
            Computes the distance between two points.
        
            other: Other point for distance measurement.
            Returns: The length of the line between this and the other point; or 0 if any of the points is not valid.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Point3f, other: Point3f, epsilon: Single) -> bool
        
            Check that all values in other are withing epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point3f, point: Point3f) -> bool
        
            Determines whether the specified Point3f has the same values as the present point.
        
            point: The specified point.
            Returns: true if point has the same coordinates as this; otherwise false.
        Equals(self: Point3f, obj: object) -> bool
        
            Determines whether the specified System.Object is a Point3f and has the same values as the 
             present point.
        
        
            obj: The specified object.
            Returns: true if obj is Point3f and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point3f) -> int
        
            Computes a hash code for the present point.
            Returns: A non-unique integer that represents this point.
        """
        pass

    @staticmethod
    def Subtract(point1, point2):
        """
        Subtract(point1: Point3f, point2: Point3f) -> Vector3f
        
            Subtracts a point from another point.
                    (Provided for languages that do not support 
             operator overloading. You can use the - operator otherwise)
        
        
            point1: A point.
            point2: Another point.
            Returns: A new vector that is the difference of point minus vector.
        """
        pass

    def ToString(self):
        """
        ToString(self: Point3f) -> str
        
            Constructs the string representation for the current point.
            Returns: The point representation in the form X,Y,Z.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Point3f, xform: Transform)
            Transforms the present point in place. The transformation matrix acts on the left of the point. 
             i.e.,
                    result = transformation*point
        
        
            xform: Transformation to apply.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, x, y, z):
        """
        __new__[Point3f]() -> Point3f
        
        __new__(cls: type, x: Single, y: Single, z: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(point1: Point3f, point2: Point3f) -> Vector3f
        
            Subtracts a point from another point.
        
            point1: A point.
            point2: Another point.
            Returns: A new vector that is the difference of point minus vector.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Each coordinate of the point must pass the Rhino.RhinoMath.IsValidSingle(System.Single) test.

Get: IsValid(self: Point3f) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of the vector.

Get: X(self: Point3f) -> Single

Set: X(self: Point3f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of the vector.

Get: Y(self: Point3f) -> Single

Set: Y(self: Point3f) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z (third) component of the vector.

Get: Z(self: Point3f) -> Single

Set: Z(self: Point3f) = value
"""


    Origin = None
    Unset = None


class Point4d(object, ISerializable, IEquatable[Point4d], IEpsilonComparable[Point4d]):
    """
    Represents the four coordinates of a point in four-dimensional space.
                The W (fourth) dimension is often considered the weight of the point as seen in 3D space.
    
    Point4d(x: float, y: float, z: float, w: float)
    Point4d(point: Point3d)
    """
    @staticmethod
    def Add(point1, point2):
        """
        Add(point1: Point4d, point2: Point4d) -> Point4d
        
            Sums two Rhino.Geometry.Point4d together.
                    (Provided for languages that do not 
             support operator overloading. You can use the + operator otherwise)
        
        
            point1: First point.
            point2: Second point.
            Returns: A new point that results from the weighted addition of point1 and point2.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Point4d, other: Point4d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Point4d, point: Point4d) -> bool
        
            Determines whether the specified point has same value as the present point.
        
            point: The specified point.
            Returns: true if point has the same value as this; otherwise false.
        Equals(self: Point4d, obj: object) -> bool
        
            Determines whether the specified System.Object is Point4d and has same coordinates as the 
             present point.
        
        
            obj: The specified object.
            Returns: true if obj is Point4d and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point4d) -> int
        
            Computes the hash code for the present point.
            Returns: A non-unique hash code, which uses all coordiantes of this object.
        """
        pass

    @staticmethod
    def Multiply(point, d):
        """
        Multiply(point: Point4d, d: float) -> Point4d
        
            Multiplies a point by a number.
                    (Provided for languages that do not support 
             operator overloading. You can use the * operator otherwise)
        
        
            point: A point.
            d: A number.
            Returns: A new point that results from the coordinatewise multiplication of point with d.
        """
        pass

    @staticmethod
    def Subtract(point1, point2):
        """
        Subtract(point1: Point4d, point2: Point4d) -> Point4d
        
            Subtracts the second point from the first point.
                    (Provided for languages that do 
             not support operator overloading. You can use the - operator otherwise)
        
        
            point1: First point.
            point2: Second point.
            Returns: A new point that results from the weighted subtraction of point2 from point1.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point4d]() -> Point4d
        
        __new__(cls: type, x: float, y: float, z: float, w: float)
        __new__(cls: type, point: Point3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(point1: Point4d, point2: Point4d) -> Point4d
        
            Sums two Rhino.Geometry.Point4d together.
        
            point1: First point.
            point2: Second point.
            Returns: A new point that results from the weighted addition of point1 and point2.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(point1: Point4d, point2: Point4d) -> float
        
            Multiplies two Rhino.Geometry.Point4d together, returning the dot (internal) product of the two.
             
                    This is not the cross product.
        
        
            point1: The first point.
            point2: The second point.
            Returns: A value that results from the coordinatewise multiplication of point1 and point2.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(point1: Point4d, point2: Point4d) -> Point4d
        
            Subtracts the second point from the first point.
        
            point1: First point.
            point2: Second point.
            Returns: A new point that results from the weighted subtraction of point2 from point1.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    W = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the W (fourth) coordinate -or weight- of this point.

Get: W(self: Point4d) -> float

Set: W(self: Point4d) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) coordinate of this point.

Get: X(self: Point4d) -> float

Set: X(self: Point4d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) coordinate of this point.

Get: Y(self: Point4d) -> float

Set: Y(self: Point4d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z (third) coordinate of this point.

Get: Z(self: Point4d) -> float

Set: Z(self: Point4d) = value
"""


    Unset = None


class PointCloud(GeometryBase, IDisposable, ISerializable, IEnumerable[PointCloudItem], IEnumerable):
    """
    Represents a collection of coordinates with optional normal vectors and colors.
    
    PointCloud()
    PointCloud(other: PointCloud)
    PointCloud(points: IEnumerable[Point3d])
    """
    def Add(self, point, *__args):
        """
        Add(self: PointCloud, point: Point3d, color: Color)
            Append a new point to the end of the list.
        
            point: Point to append.
            color: Color of new point.
        Add(self: PointCloud, point: Point3d, normal: Vector3d, color: Color)
            Append a new point to the end of the list.
        
            point: Point to append.
            normal: Normal vector of new point.
            color: Color of new point.
        Add(self: PointCloud, point: Point3d)
            Append a new point to the end of the list.
        
            point: Point to append.
        Add(self: PointCloud, point: Point3d, normal: Vector3d)
            Append a new point to the end of the list.
        
            point: Point to append.
            normal: Normal vector of new point.
        """
        pass

    def AddRange(self, points):
        """ AddRange(self: PointCloud, points: IEnumerable[Point3d]) """
        pass

    def AppendNew(self):
        """
        AppendNew(self: PointCloud) -> PointCloudItem
        
            Appends a new PointCloudItem to the end of this point cloud.
            Returns: The newly appended item.
        """
        pass

    def ClearColors(self):
        """
        ClearColors(self: PointCloud)
            Destroys the color information in this point cloud.
        """
        pass

    def ClearHiddenFlags(self):
        """
        ClearHiddenFlags(self: PointCloud)
            Destroys the hidden flag information in this point cloud.
        """
        pass

    def ClearNormals(self):
        """
        ClearNormals(self: PointCloud)
            Destroys the normal vector information in this point cloud.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: PointCloud, testPoint: Point3d) -> int
        
            Returns index of the closest point in the point cloud to a given test point.
        
            testPoint: .
            Returns: Index of point in the point cloud on success. -1 on failure.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def GetColors(self):
        """
        GetColors(self: PointCloud) -> Array[Color]
        
            Copy all the point colors in this point cloud to an array.
            Returns: An array containing all the colors in this point cloud.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PointCloud) -> IEnumerator[PointCloudItem]
        
            Gets an enumerator that allows to modify each pointcloud point.
            Returns: A instance of System.Collections.Generic.IEnumerator.
        """
        pass

    def GetNormals(self):
        """
        GetNormals(self: PointCloud) -> Array[Vector3d]
        
            Copy all the normal vectors in this point cloud to an array.
            Returns: An array containing all the normals in this point cloud.
        """
        pass

    def GetPoints(self):
        """
        GetPoints(self: PointCloud) -> Array[Point3d]
        
            Copy all the point coordinates in this point cloud to an array.
            Returns: An array containing all the points in this point cloud.
        """
        pass

    def Insert(self, index, point, *__args):
        """
        Insert(self: PointCloud, index: int, point: Point3d, color: Color)
            Inserts a new point into the point list.
        
            index: Insertion index.
            point: Point to append.
            color: Color of new point.
        Insert(self: PointCloud, index: int, point: Point3d, normal: Vector3d, color: Color)
            Inserts a new point into the point list.
        
            index: Insertion index.
            point: Point to append.
            normal: Normal vector of new point.
            color: Color of new point.
        Insert(self: PointCloud, index: int, point: Point3d)
            Inserts a new point into the point list.
        
            index: Insertion index.
            point: Point to append.
        Insert(self: PointCloud, index: int, point: Point3d, normal: Vector3d)
            Inserts a new point into the point list.
        
            index: Insertion index.
            point: Point to append.
            normal: Normal vector of new point.
        """
        pass

    def InsertNew(self, index):
        """
        InsertNew(self: PointCloud, index: int) -> PointCloudItem
        
            Inserts a new Rhino.Geometry.PointCloudItem at a specific position of the point cloud.
        
            index: Index of new item.
            Returns: The newly inserted item.
        """
        pass

    def InsertRange(self, index, points):
        """ InsertRange(self: PointCloud, index: int, points: IEnumerable[Point3d]) """
        pass

    def Merge(self, other):
        """
        Merge(self: PointCloud, other: PointCloud)
            Copies the point values of another pointcloud into this one.
        
            other: PointCloud to merge with this one.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: PointCloud, index: int)
            Remove the point at the given index.
        
            index: Index of point to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PointCloudItem](enumerable: IEnumerable[PointCloudItem], value: PointCloudItem) -> bool """
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
        __new__(cls: type, other: PointCloud)
        __new__(cls: type, points: IEnumerable[Point3d])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ContainsColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the points in this 
            pointcloud have colors assigned to them.

Get: ContainsColors(self: PointCloud) -> bool

"""

    ContainsHiddenFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the points in this 
            pointcloud have hidden flags assigned to them.

Get: ContainsHiddenFlags(self: PointCloud) -> bool

"""

    ContainsNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the points in this 
            pointcloud have normals assigned to them.

Get: ContainsNormals(self: PointCloud) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of points in this pointcloud.

Get: Count(self: PointCloud) -> int

"""

    HiddenPointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of points that have their Hidden flag set.

Get: HiddenPointCount(self: PointCloud) -> int

"""



class PointCloudItem(object):
    """
    Represents a single item in a pointcloud. A PointCloud item 
                always has a location, but it has an optional normal vector and color.
    """
    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of this point cloud item.

Get: Color(self: PointCloudItem) -> Color

Set: Color(self: PointCloudItem) = value
"""

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the hidden flag of this point cloud item.

Get: Hidden(self: PointCloudItem) -> bool

Set: Hidden(self: PointCloudItem) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this point cloud item.

Get: Index(self: PointCloudItem) -> int

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the location of this point cloud item.

Get: Location(self: PointCloudItem) -> Point3d

Set: Location(self: PointCloudItem) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the normal vector for this point cloud item.

Get: Normal(self: PointCloudItem) -> Vector3d

Set: Normal(self: PointCloudItem) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X component of this point cloud item location.

Get: X(self: PointCloudItem) -> float

Set: X(self: PointCloudItem) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y component of this point cloud item location.

Get: Y(self: PointCloudItem) -> float

Set: Y(self: PointCloudItem) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z component of this point cloud item location.

Get: Z(self: PointCloudItem) -> float

Set: Z(self: PointCloudItem) = value
"""



class PointContainment(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for closed curve/point spatial relationships.
    
    enum PointContainment, values: Coincident (3), Inside (1), Outside (2), Unset (0)
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

    Coincident = None
    Inside = None
    Outside = None
    Unset = None
    value__ = None


class PointFaceRelation(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates the possible point/BrepFace spatial relationships.
    
    enum PointFaceRelation, values: Boundary (2), Exterior (0), Interior (1)
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

    Boundary = None
    Exterior = None
    Interior = None
    value__ = None


class PolyCurve(Curve, IDisposable, ISerializable):
    """
    Represents a curve that is the result of joining several (possibly different)
                types of curves.
    
    PolyCurve()
    """
    def Append(self, *__args):
        """
        Append(self: PolyCurve, curve: Curve) -> bool
        
            Appends and matches the start of the curve to the end of polycurve. 
                    This function 
             will fail if the PolyCurve is closed or if SegmentCount > 0 and the new segment is closed.
        
        
            curve: Segment to append.
            Returns: true on success, false on failure.
        Append(self: PolyCurve, arc: Arc) -> bool
        
            Appends and matches the start of the arc to the end of polycurve. 
                    This function 
             will fail if the polycurve is closed or if SegmentCount > 0 and the arc is closed.
        
        
            arc: Arc segment to append.
            Returns: true on success, false on failure.
        Append(self: PolyCurve, line: Line) -> bool
        
            Appends and matches the start of the line to the end of polycurve. 
                    This function 
             will fail if the polycurve is closed.
        
        
            line: Line segment to append.
            Returns: true on success, false on failure.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def Duplicate(self):
        """
        Duplicate(self: PolyCurve) -> GeometryBase
        
            Duplicates this polycurve.
                    When not overridden in a derived class, this calls 
             Rhino.Geometry.PolyCurve.DuplicatePolyCurve.
        
            Returns: An exact duplicate of this curve.
        """
        pass

    def DuplicatePolyCurve(self):
        """
        DuplicatePolyCurve(self: PolyCurve) -> PolyCurve
        
            Duplicates this polycurve.
                    This is the same as Rhino.Geometry.PolyCurve.Duplicate.
            Returns: An exact duplicate of this curve.
        """
        pass

    def Explode(self):
        """
        Explode(self: PolyCurve) -> Array[Curve]
        
            Explodes this PolyCurve into a list of Curve segments. This will not explode nested polycurves. 
             
                    Call Rhino.Geometry.PolyCurve.RemoveNesting first if you need all individual 
             segments.
        
            Returns: An array of polycurve segments.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def PolyCurveParameter(self, segmentIndex, segmentCurveParameter):
        """
        PolyCurveParameter(self: PolyCurve, segmentIndex: int, segmentCurveParameter: float) -> float
        
            Converts a segment curve parameter to a polycurve parameter.
        
            segmentIndex: Index of segment.
            segmentCurveParameter: Parameter on segment.
            Returns: Polycurve evaluation parameter or UnsetValue if the polycurve curve parameter could not be 
             computed.
        """
        pass

    def RemoveNesting(self):
        """
        RemoveNesting(self: PolyCurve) -> bool
        
            Explodes nested polycurve segments and reconstructs this curve from the shattered remains. 
            
                     The result will have not have any PolyCurves as segments but it will have identical 
           
                      locus and parameterization.
        
            Returns: true if any nested PolyCurve was found and absorbed, false if no PolyCurve segments could be 
             found.
        """
        pass

    def SegmentCurve(self, index):
        """
        SegmentCurve(self: PolyCurve, index: int) -> Curve
        
            Gets the segment curve at the given index.
        
            index: Index of segment to retrieve.
            Returns: The segment at the given index or null on failure.
        """
        pass

    def SegmentCurveParameter(self, polycurveParameter):
        """
        SegmentCurveParameter(self: PolyCurve, polycurveParameter: float) -> float
        
            Converts a polycurve parameter to a segment curve parameter.
        
            polycurveParameter: Parameter on PolyCurve to convert.
            Returns: Segment curve evaluation parameter or UnsetValue if the 
                    segment curve parameter 
             could not be computed.
        """
        pass

    def SegmentDomain(self, segmentIndex):
        """
        SegmentDomain(self: PolyCurve, segmentIndex: int) -> Interval
        
            Returns the polycurve subdomain assigned to a segment curve.
        
            segmentIndex: Index of segment.
            Returns: The polycurve subdomain assigned to a segment curve. 
                    Returns Interval.Unset if 
             segment_index < 0 or segment_index >= Count().
        """
        pass

    def SegmentIndex(self, polycurveParameter):
        """
        SegmentIndex(self: PolyCurve, polycurveParameter: float) -> int
        
            Finds the segment used for evaluation at polycurve_parameter.
        
            polycurveParameter: Parameter on polycurve for segment lookup.
            Returns: Index of the segment used for evaluation at polycurve_parameter. 
                    If 
             polycurve_parameter < Domain.Min(), then 0 is returned. 
                    If polycurve_parameter > 
             Domain.Max(), then Count()-1 is returned.
        """
        pass

    def SegmentIndexes(self, subdomain, segmentIndex0, segmentIndex1):
        """
        SegmentIndexes(self: PolyCurve, subdomain: Interval) -> (int, int, int)
        
            Finds the segments that overlap the Polycurve sub domain.
        
            subdomain: Domain on this PolyCurve.
            Returns: Number of segments that overlap the subdomain.
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
    def __new__(self):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is a quick way to see if the curve has gaps between the sub curve segments.

Get: HasGap(self: PolyCurve) -> bool

"""

    IsNested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not a PolyCurve contains nested PolyCurves.

Get: IsNested(self: PolyCurve) -> bool

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of segments that make up this Polycurve.

Get: SegmentCount(self: PolyCurve) -> int

"""



class Polyline(Point3dList, IList[Point3d], ICollection[Point3d], IEnumerable[Point3d], IEnumerable, IList, ICollection):
    """
    Represents an ordered set of points connected by linear segments.
                Polylines are closed if start and end points coincide.
    
    Polyline()
    Polyline(initialCapacity: int)
    Polyline(collection: IEnumerable[Point3d])
    """
    def BreakAtAngles(self, angle):
        """
        BreakAtAngles(self: Polyline, angle: float) -> Array[Polyline]
        
            Breaks this polyline into sections at sharp kinks. 
                    Closed polylines will also be 
             broken at the first and last vertex.
        
        
            angle: Angle (in radians) between adjacent segments for a break to occur.
            Returns: An array of polyline segments, or null on error.
        """
        pass

    def CenterPoint(self):
        """
        CenterPoint(self: Polyline) -> Point3d
        
            Compute the center point of the polyline as the weighted average of all segments.
            Returns: The weighted average of all segments.
        """
        pass

    def ClosestParameter(self, testPoint):
        """
        ClosestParameter(self: Polyline, testPoint: Point3d) -> float
        
            Gets the parameter along the polyline which is closest to a test-point.
        
            testPoint: Point to approximate.
            Returns: The parameter along the polyline closest to testPoint.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: Polyline, testPoint: Point3d) -> Point3d
        
            Gets the point on the polyline which is closest to a test-point.
        
            testPoint: Point to approximate.
            Returns: The point on the polyline closest to testPoint.
        """
        pass

    def CollapseShortSegments(self, tolerance):
        """
        CollapseShortSegments(self: Polyline, tolerance: float) -> int
        
            Collapses all segments until none are shorter than tolerance. 
                    This function is 
             significantly slower than DeleteShortSegments, 
                    since it recursively operates on 
             the shortest segment. 
                    When a segment is collapsed the end-points are placed in the 
             center of the segment.
        
        
            tolerance: Tolerance to use during collapsing.
            Returns: The number of segments that were collapsed.
        """
        pass

    def DeleteShortSegments(self, tolerance):
        """
        DeleteShortSegments(self: Polyline, tolerance: float) -> int
        
            Removes all points that are closer than tolerance to the previous point. 
                    Start and 
             end points are left intact.
        
        
            tolerance: Vertices closer together than tolerance will be removed.
            Returns: Number of points (and segments) removed.
        """
        pass

    def GetSegments(self):
        """
        GetSegments(self: Polyline) -> Array[Line]
        
            Constructs an array of line segments that make up the entire polyline.
            Returns: An array of line segments or null if the polyline contains fewer than 2 points.
        """
        pass

    def IsClosedWithinTolerance(self, tolerance):
        """
        IsClosedWithinTolerance(self: Polyline, tolerance: float) -> bool
        
            Determines whether the polyline is closed, provided a tolerance value.
        
            tolerance: If the distance between the start and end point of the polyline 
                    is less than 
             tolerance, the polyline is considered to be closed.
        
            Returns: true if the polyline is closed to within tolerance, false otherwise.
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Polyline, t: float) -> Point3d
        
            Gets the point on the polyline at the given parameter. 
                    The integer part of the 
             parameter indicates the index of the segment.
        
        
            t: Polyline parameter.
            Returns: The point on the polyline at t.
        """
        pass

    def ReduceSegments(self, tolerance):
        """
        ReduceSegments(self: Polyline, tolerance: float) -> int
        
            Constructs a reduction of this polyline by recursively removing the least significant segments.
        
            tolerance: Tolerance for reduction. Whenever a vertex of the polyline is more 
                    significant 
             than tolerance, it will be included in the reduction.
        
            Returns: The number of vertices that disappeared due to reduction.
        """
        pass

    def SegmentAt(self, index):
        """
        SegmentAt(self: Polyline, index: int) -> Line
        
            Gets the line segment at the given index.
        
            index: Index of segment to retrieve.
            Returns: Line segment at index or Line.Unset on failure.
        """
        pass

    def Smooth(self, amount):
        """
        Smooth(self: Polyline, amount: float) -> bool
        
            Smoothens the polyline segments by averaging adjacent vertices. 
                    Smoothing requires 
             a polyline with exclusively valid vertices.
        
        
            amount: Amount to smooth. Zero equals no smoothing, one equals complete smoothing.
            Returns: true on success, false on failure.
        """
        pass

    def TangentAt(self, t):
        """
        TangentAt(self: Polyline, t: float) -> Vector3d
        
            Gets the unit tangent vector along the polyline at the given parameter. 
                    The 
             integer part of the parameter indicates the index of the segment.
        
        
            t: Polyline parameter.
            Returns: The tangent along the polyline at t.
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Polyline) -> NurbsCurve
        
            Constructs a nurbs curve representation of this polyline.
            Returns: A Nurbs curve shaped like this polyline or null on failure.
        """
        pass

    def TriangulateClosedPolyline(self):
        """
        TriangulateClosedPolyline(self: Polyline) -> Array[MeshFace]
        
            Attempts to create a list of triangles which represent a
                    triangulation of a closed 
             polyline
        """
        pass

    def Trim(self, domain):
        """
        Trim(self: Polyline, domain: Interval) -> Polyline
        
            Constructs a polyline out of a parameter subdomain in this curve.
        
            domain: The subdomain of the polyline. 
                    The integer part of the domain parameters indicate 
             the index of the segment.
        
            Returns: The polyline as defined by the subdomain, or null on failure.
        """
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
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, collection: IEnumerable[Point3d])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this polyline is closed. 
            The polyline is considered to be closed if its start is 
            identical to its endpoint.

Get: IsClosed(self: Polyline) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this polyline is valid. 
            Valid polylines have at least one segment, no Invalid points and no zero length segments.Closed polylines with only two segments are also not considered valid.

Get: IsValid(self: Polyline) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total length of the polyline.

Get: Length(self: Polyline) -> float

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of segments for this polyline.

Get: SegmentCount(self: Polyline) -> int

"""



class PolylineCurve(Curve, IDisposable, ISerializable):
    """
    Represents the geometry of a set of linked line segments.
                This is fundamentally a class that derives from Rhino.Geometry.Curve
                and internally contains a Rhino.Geometry.Polyline.
    
    PolylineCurve()
    PolylineCurve(other: PolylineCurve)
    PolylineCurve(points: IEnumerable[Point3d])
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Curve, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: Curve)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
        """
        pass

    def Point(self, index):
        """
        Point(self: PolylineCurve, index: int) -> Point3d
        
            Gets a point at a specified index in the polyline curve.
        
            index: An index.
            Returns: A point.
        """
        pass

    def SetPoint(self, index, point):
        """
        SetPoint(self: PolylineCurve, index: int, point: Point3d)
            Sets a point at a specified index in the polyline curve.
        
            index: An index.
            point: A point location to set.
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: PolylineCurve)
        __new__(cls: type, points: IEnumerable[Point3d])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    PointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of points in this polyline.

Get: PointCount(self: PolylineCurve) -> int

"""



class Quaternion(object, IEquatable[Quaternion], IEpsilonComparable[Quaternion]):
    """
    Represents the four coefficient values in a quaternion.
                The first value a is the real part,
                while the rest multipies i, j and k, that are imaginary.quaternion = a + bi + cj + dk
    
    Quaternion(a: float, b: float, c: float, d: float)
    """
    @staticmethod
    def CrossProduct(p, q):
        """
        CrossProduct(p: Quaternion, q: Quaternion) -> Quaternion
        
            Computes the vector cross product of p and q = (0,x,y,z),
                    where (x,y,z) = 
             Rhino.Geometry.Vector3d.CrossProduct(Rhino.Geometry.Vector3d,Rhino.Geometry.Vector3d)CrossProduct
             (p.Rhino.Geometry.Quaternion.VectorVector,q.Rhino.Geometry.Quaternion.VectorVector).This is not 
             the same as the quaternion product p*q.
        
        
            p: A quaternion.
            q: Another quaternion.
            Returns: A new quaternion.
        """
        pass

    @staticmethod
    def Distance(p, q):
        """
        Distance(p: Quaternion, q: Quaternion) -> float
        
            Returns the distance or norm of the difference between two quaternions.
        
            p: A quaternion.
            q: Another quaternion.
            Returns: (p - q).Length()
        """
        pass

    def DistanceTo(self, q):
        """
        DistanceTo(self: Quaternion, q: Quaternion) -> float
        
            Computes the distance or norm of the difference between this and another quaternion.
        
            q: Another quaternion.
            Returns: (this - q).Length.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Quaternion, other: Quaternion, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Quaternion, obj: object) -> bool
        
            Determines whether an object is a quaternion and has the same value of this quaternion.
        
            obj: Another object to compare.
            Returns: true if obj is a quaternion and has exactly equal coefficients; otherwise false.
        Equals(self: Quaternion, other: Quaternion) -> bool
        
            Determines whether this quaternion has the same value of another quaternion.
        
            other: Another quaternion to compare.
            Returns: true if the quaternions have exactly equal coefficients; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Quaternion) -> int
        
            Gets a non-unique but repeatable hashing code for this quaternion.
            Returns: A signed number.
        """
        pass

    def GetRotation(self, *__args):
        """
        GetRotation(self: Quaternion) -> (bool, Plane)
        
            Returns the frame created by applying the quaternion's rotation
                    to the canonical 
             world frame (1,0,0),(0,1,0),(0,0,1).
        
            Returns: true if the operation succeeded; otherwise, false.
        GetRotation(self: Quaternion) -> (bool, float, Vector3d)
        
            Returns the rotation defined by the quaternion.
            Returns: True if the operation succeeded; otherwise, false.
        """
        pass

    def Invert(self):
        """
        Invert(self: Quaternion) -> bool
        
            Modifies this quaternion to become
                    (a/L2, -b/L2, -c/L2, -d/L2),where L2 = length 
             squared = (a*a + b*b + c*c + d*d).This is the multiplicative inverse, i.e.,
                    
             (a,b,c,d)*(a/L2, -b/L2, -c/L2, -d/L2) = (1,0,0,0).
        
            Returns: true if successful. false if the quaternion is zero and cannot be inverted.
        """
        pass

    def MatrixForm(self):
        """
        MatrixForm(self: Quaternion) -> Transform
        
            Returns 4x4 real valued matrix form of the quaternion
                    a  b  c  d
                    -b  a 
             -d  c
                    -c  d  a -b
                    -d -c  b  a
                    which has the same 
             arithmetic properties as the quaternion.
        
            Returns: A transform value.
        """
        pass

    @staticmethod
    def Product(p, q):
        """
        Product(p: Quaternion, q: Quaternion) -> Quaternion
        
            The quaternion product of p and q.  This is the same value as p*q.
        
            p: The first trasform.
            q: The second trasform.
            Returns: A transform value.
        """
        pass

    def Rotate(self, v):
        """
        Rotate(self: Quaternion, v: Vector3d) -> Vector3d
        
            Rotates a 3d vector. This operation is also called conjugation,
                    because the result 
             is the same as
                    (q.Conjugate()*(0,x,y,x)*q/q.LengthSquared).Vector.
        
        
            v: The vector to be rotated.
            Returns: R*v, where R is the rotation defined by the unit quaternion.
                    This is mathematically 
             the same as the values
                    (Inverse(q)*(0,x,y,z)*q).Vector
                    and
                   
              (q.Conjugate()*(0,x,y,x)*q/q.LengthSquared).Vector.
        """
        pass

    @staticmethod
    def Rotation(*__args):
        """
        Rotation(plane0: Plane, plane1: Plane) -> Quaternion
        
            Returns the unit quaternion that represents the the rotation that maps
                    plane0.xaxis 
             to plane1.xaxis, plane0.yaxis to plane1.yaxis, and 
                    plane0.zaxis to plane1.zaxis.
        
        
            plane0: The first plane.
            plane1: The second plane.
            Returns: A quaternion value.
        Rotation(angle: float, axisOfRotation: Vector3d) -> Quaternion
        
            Returns the unit quaternion
                    cos(angle/2), sin(angle/2)*x, sin(angle/2)*y, 
             sin(angle/2)*z
                    where (x,y,z) is the unit vector parallel to axis.  This is the
            
                     unit quaternion that represents the rotation of angle about axis.
        
        
            angle: An angle in radians.
            axisOfRotation: The axis of rotation.
            Returns: A new quaternion.
        """
        pass

    def Set(self, a, b, c, d):
        """
        Set(self: Quaternion, a: float, b: float, c: float, d: float)
            Sets all coefficients of the quaternion.
        """
        pass

    def SetRotation(self, *__args):
        """
        SetRotation(self: Quaternion, plane0: Plane, plane1: Plane)
            Sets the quaternion to the unit quaternion which rotates
                    plane0.xaxis to 
             plane1.xaxis, plane0.yaxis to plane1.yaxis,
                    and plane0.zaxis to plane1.zaxis.
        
        
            plane0: The "from" rotation plane. Origin point is ignored.
            plane1: The "to" rotation plane. Origin point is ignored.
        SetRotation(self: Quaternion, angle: float, axisOfRotation: Vector3d)
            Sets the quaternion to cos(angle/2), sin(angle/2)*x, sin(angle/2)*y, sin(angle/2)*z
                    
             where (x,y,z) is the unit vector parallel to axis.  This is the unit quaternion
                    
             that represents the rotation of angle about axis.
        
        
            angle: in radians.
            axisOfRotation: The direction of the axis of rotation.
        """
        pass

    def Unitize(self):
        """
        Unitize(self: Quaternion) -> bool
        
            Scales the quaternion's coordinates so that a*a + b*b + c*c + d*d = 1.
            Returns: true if successful.  false if the quaternion is zero and cannot be unitized.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, a, b, c, d):
        """
        __new__[Quaternion]() -> Quaternion
        
        __new__(cls: type, a: float, b: float, c: float, d: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(a: Quaternion, b: Quaternion) -> Quaternion
        
            Adds two quaternions.
                    This sums each quaternion coefficient with its correspondant 
             and returns
                    a new result quaternion.
        
        
            a: A quaternion.
            b: Another quaternion.
            Returns: A new quaternion.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(a: Quaternion, b: Quaternion) -> Quaternion
        
            Multiplies a quaternion with another one.
                    Quaternion multiplication (Hamilton 
             product) is not commutative.
        
        
            a: The first term.
            b: The second term.
            Returns: A new quaternion.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(a: Quaternion, b: Quaternion) -> Quaternion
        
            Subtracts a quaternion from another one.
                    This computes the difference of each 
             quaternion coefficient with its
                    correspondant and returns a new result quaternion.
        
        
            a: A quaternion.
            b: Another quaternion.
            Returns: A new quaternion.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the real part of the quaternion.

Get: A(self: Quaternion) -> float

Set: A(self: Quaternion) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first imaginary coefficient of the quaternion.

Get: B(self: Quaternion) -> float

Set: B(self: Quaternion) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the second imaginary coefficient of the quaternion.

Get: C(self: Quaternion) -> float

Set: C(self: Quaternion) = value
"""

    Conjugate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a new quaternion that is the conjugate of this quaternion.
            This is (a,-b,-c,-d)

Get: Conjugate(self: Quaternion) -> Quaternion

"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the third imaginary coefficient of the quaternion.

Get: D(self: Quaternion) -> float

Set: D(self: Quaternion) = value
"""

    Inverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Computes a new inverted quaternion,
            (a/L2, -b/L2, -c/L2, -d/L2),where L2 = length squared = (a*a + b*b + c*c + d*d).
            This is the multiplicative inverse, i.e.,
            (a,b,c,d)*(a/L2, -b/L2, -c/L2, -d/L2) = (1,0,0,0).
            If this is the zero quaternion, then the zero quaternion is returned.

Get: Inverse(self: Quaternion) -> Quaternion

"""

    IsScalar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if b, c, and d are all zero.

Get: IsScalar(self: Quaternion) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the four coefficients are valid numbers within RhinoCommon.
            See Rhino.RhinoMath.IsValidDouble(System.Double).

Get: IsValid(self: Quaternion) -> bool

"""

    IsVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if a = 0 and at least one of b, c, or d is not zero.

Get: IsVector(self: Quaternion) -> bool

"""

    IsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if a, b, c, and d are all zero.

Get: IsZero(self: Quaternion) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the length or norm of the quaternion.

Get: Length(self: Quaternion) -> float

"""

    LengthSquared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the result of (a^2 + b^2 + c^2 + d^2).

Get: LengthSquared(self: Quaternion) -> float

"""

    Scalar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The real (scalar) part of the quaternion
            This is Rhino.Geometry.Quaternion.A.

Get: Scalar(self: Quaternion) -> float

"""

    Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The imaginary part of the quaternion
            (B,C,D)

Get: Vector(self: Quaternion) -> Vector3d

"""


    I = None
    Identity = None
    J = None
    K = None
    Zero = None


class RadialDimension(AnnotationBase, IDisposable, ISerializable):
    """
    Represents a dimension of a circular entity that can be measured with radius or diameter.
                This entity refers to the geometric element that is independent from the document.
    
    RadialDimension(center: Point3d, arrowTip: Point3d, xAxis: Vector3d, normal: Vector3d, offsetDistance: float)
    RadialDimension(circle: Circle, arrowTip: Point3d, offsetDistance: float)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, center: Point3d, arrowTip: Point3d, xAxis: Vector3d, normal: Vector3d, offsetDistance: float)
        __new__(cls: type, circle: Circle, arrowTip: Point3d, offsetDistance: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsDiameterDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the value refers to the diameter, rather than the radius.

Get: IsDiameterDimension(self: RadialDimension) -> bool

"""



class Ray3d(object, ISerializable, IEquatable[Ray3d], IEpsilonComparable[Ray3d]):
    """
    Represents an immutable ray in three dimensions, using position and direction.
    
    Ray3d(position: Point3d, direction: Vector3d)
    """
    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Ray3d, other: Ray3d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Ray3d, ray: Ray3d) -> bool
        
            Determines whether the specified Ray3d has the same value as the present ray.
        
            ray: The specified ray.
            Returns: true if ray has the same position and direction as this; otherwise false.
        Equals(self: Ray3d, obj: object) -> bool
        
            Determines whether the specified System.Object is a Ray3d and has the same values as the present 
             ray.
        
        
            obj: The specified object.
            Returns: true if obj is a Ray3d and has the same position and direction as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Ray3d) -> int
        
            Computes a hashing number that represents the current ray.
            Returns: A signed integer that represents both postion and direction, but is not unique.
        """
        pass

    def PointAt(self, t):
        """
        PointAt(self: Ray3d, t: float) -> Point3d
        
            Evaluates a point along the ray.
        
            t: The t parameter.
            Returns: A point at (Direction*t + Position).
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, position, direction):
        """
        __new__[Ray3d]() -> Ray3d
        
        __new__(cls: type, position: Point3d, direction: Vector3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction vector of this ray.

Get: Direction(self: Ray3d) -> Vector3d

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the starting position of this ray.

Get: Position(self: Ray3d) -> Point3d

"""



class Rectangle3d(object, IEpsilonComparable[Rectangle3d]):
    """
    Represents the values of a plane and two intervals
                that form an oriented rectangle in three dimensions.
    
    Rectangle3d(plane: Plane, width: float, height: float)
    Rectangle3d(plane: Plane, width: Interval, height: Interval)
    Rectangle3d(plane: Plane, cornerA: Point3d, cornerB: Point3d)
    """
    def ClosestPoint(self, point, includeInterior=None):
        """
        ClosestPoint(self: Rectangle3d, point: Point3d, includeInterior: bool) -> Point3d
        
            Gets the point on the rectangle that is closest to a test-point.
        
            point: Point to project.
            includeInterior: If false, the point is projected onto the boundary edge only, 
                    otherwise the 
             interior of the rectangle is also taken into consideration.
        
            Returns: The point on the rectangle closest to the test point or Point3d.Unset on failure.
        ClosestPoint(self: Rectangle3d, point: Point3d) -> Point3d
        
            Gets the point on the rectangle that is closest to a test-point.
        
            point: Point to project.
            Returns: The point on or in the rectangle closest to the test point or Point3d.Unset on failure.
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Rectangle3d, x: float, y: float) -> PointContainment
        
            Determines if two plane parameters are included in this rectangle.
        
            x: Parameter along base plane X direction.
            y: Parameter along base plane Y direction.
            Returns: Parameter Rectangle relationship.
        Contains(self: Rectangle3d, pt: Point3d) -> PointContainment
        
            Determines if a point is included in this rectangle.
        
            pt: Point to test. The point will be projected onto the Rectangle plane before inclusion is 
             determined.
        
            Returns: Point Rectangle relationship.
        """
        pass

    def Corner(self, index):
        """
        Corner(self: Rectangle3d, index: int) -> Point3d
        
            Gets the corner at the given index.
        
            index: Index of corner, valid values are:
                    0 = lower left (min-x, min-y)1 = lower right 
             (max-x, min-y)2 = upper right (max-x, max-y)3 = upper left (min-x, max-y)
        
            Returns: The point at the given corner index.
        """
        pass

    @staticmethod
    def CreateFromPolyline(polyline, deviation=None, angleDeviation=None):
        """
        CreateFromPolyline(polyline: IEnumerable[Point3d]) -> (Rectangle3d, float, float)
        CreateFromPolyline(polyline: IEnumerable[Point3d]) -> Rectangle3d
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Rectangle3d, other: Rectangle3d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def MakeIncreasing(self):
        """
        MakeIncreasing(self: Rectangle3d)
            Ensures the X and Y dimensions are increasing or singleton intervals.
        """
        pass

    def PointAt(self, *__args):
        """
        PointAt(self: Rectangle3d, t: float) -> Point3d
        
            Gets a point along the rectangle boundary.
        
            t: Parameter along rectangle boundary. Valid values range from 0.0 to 4.0, 
                    where each 
             integer domain represents a single boundary edge.
        
            Returns: The point at the given boundary parameter.
        PointAt(self: Rectangle3d, x: float, y: float) -> Point3d
        
            Gets a point in Rectangle space.
        
            x: Normalized parameter along Rectangle width.
            y: Normalized parameter along Rectangle height.
            Returns: The point at the given x,y parameter.
        """
        pass

    def RecenterPlane(self, *__args):
        """
        RecenterPlane(self: Rectangle3d, origin: Point3d)
            Recenters the base plane on a new origin.
        
            origin: New origin for plane.
        RecenterPlane(self: Rectangle3d, index: int)
            Recenters the base plane on one of the corners.
        
            index: Index of corner, valid values are:
                    0 = lower left (min-x, min-y)1 = lower right 
             (max-x, min-y)2 = upper right (max-x, max-y)3 = upper left (min-x, max-y)
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Rectangle3d) -> NurbsCurve
        
            Constructs a nurbs curve representation of this rectangle.
            Returns: A nurbs curve with the same shape as this rectangle.
        """
        pass

    def ToPolyline(self):
        """
        ToPolyline(self: Rectangle3d) -> Polyline
        
            Constructs a polyline from this rectangle.
            Returns: A polyline with the same shape as this rectangle.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Rectangle3d, xform: Transform) -> bool
        
            Transforms this rectangle. Note that rectangles cannot be skewed or tapered.
        
            xform: Transformation to apply.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane, *__args):
        """
        __new__[Rectangle3d]() -> Rectangle3d
        
        __new__(cls: type, plane: Plane, width: float, height: float)
        __new__(cls: type, plane: Plane, width: Interval, height: Interval)
        __new__(cls: type, plane: Plane, cornerA: Point3d, cornerB: Point3d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unsigned Area of the rectangle.

Get: Area(self: Rectangle3d) -> float

"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the world aligned boundingbox for this rectangle.

Get: BoundingBox(self: Rectangle3d) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point in the center of the rectangle.

Get: Center(self: Rectangle3d) -> Point3d

"""

    Circumference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the circumference of the rectangle.

Get: Circumference(self: Rectangle3d) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signed height of the rectangle. If the Y dimension is decreasing, the height will be negative.

Get: Height(self: Rectangle3d) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this is a valid rectangle. 
            A rectangle is considered to be valid when the base plane and both dimensions are valid.

Get: IsValid(self: Rectangle3d) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base plane of the rectangle.

Get: Plane(self: Rectangle3d) -> Plane

Set: Plane(self: Rectangle3d) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signed width of the rectangle. If the X dimension is decreasing, the width will be negative.

Get: Width(self: Rectangle3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the dimensions of the rectangle along the base plane X-Axis (i.e. the width).

Get: X(self: Rectangle3d) -> Interval

Set: X(self: Rectangle3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the dimensions of the rectangle along the base plane Y-Axis (i.e. the height).

Get: Y(self: Rectangle3d) -> Interval

Set: Y(self: Rectangle3d) = value
"""


    Unset = None


class RegionContainment(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for closed curve/closed curve relationships.
    
    enum RegionContainment, values: AInsideB (2), BInsideA (3), Disjoint (0), MutualIntersection (1)
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

    AInsideB = None
    BInsideA = None
    Disjoint = None
    MutualIntersection = None
    value__ = None


class RevSurface(Surface, IDisposable, ISerializable):
    """
    Represents a surface of revolution.
                Revolutions can be incomplete (they can form arcs).
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(revoluteLine: Line, axisOfRevolution: Line) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix line and an axis.
                    If the 
             operation succeeds, results can be (truncated) cones, cylinders and circular hyperboloids.
        
        
            revoluteLine: A generatrix.
            axisOfRevolution: An axis.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        Create(revolutePolyline: Polyline, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix polyline and an axis.
                    This 
             overload accepts a slice start and end angles.
        
        
            revolutePolyline: A generatrix.
            axisOfRevolution: An axis.
            startAngleRadians: An angle in radias for the start.
            endAngleRadians: An angle in radias for the end.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        Create(revolutePolyline: Polyline, axisOfRevolution: Line) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix polyline and an axis.
        
            revolutePolyline: A generatrix.
            axisOfRevolution: An axis.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        Create(revoluteCurve: Curve, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix curve and an axis.
                    This 
             overload accepts a slice start and end angles.
        
        
            revoluteCurve: A generatrix.
            axisOfRevolution: An axis.
            startAngleRadians: An angle in radias for the start.
            endAngleRadians: An angle in radias for the end.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        Create(revoluteCurve: Curve, axisOfRevolution: Line) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix curve and an axis.
        
            revoluteCurve: A generatrix.
            axisOfRevolution: An axis.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        Create(revoluteLine: Line, axisOfRevolution: Line, startAngleRadians: float, endAngleRadians: float) -> RevSurface
        
            Constructs a new surface of revolution from a generatrix line and an axis.
                    This 
             overload accepts a slice start and end angles.Results can be (truncated) cones, cylinders and 
             circular hyperboloids, or can fail.
        
        
            revoluteLine: A generatrix.
            axisOfRevolution: An axis.
            startAngleRadians: An angle in radias for the start.
            endAngleRadians: An angle in radias for the end.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        """
        pass

    @staticmethod
    def CreateFromCone(cone):
        """
        CreateFromCone(cone: Cone) -> RevSurface
        
            Constructs a new surface of revolution from the values of a cone.
        
            cone: A cone.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        """
        pass

    @staticmethod
    def CreateFromCylinder(cylinder):
        """
        CreateFromCylinder(cylinder: Cylinder) -> RevSurface
        
            Constructs a new surface of revolution from the values of a cylinder.
        
            cylinder: A cylinder.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        """
        pass

    @staticmethod
    def CreateFromSphere(sphere):
        """
        CreateFromSphere(sphere: Sphere) -> RevSurface
        
            Constructs a new surface of revolution from the values of a sphere.
        
            sphere: A sphere.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        """
        pass

    @staticmethod
    def CreateFromTorus(torus):
        """
        CreateFromTorus(torus: Torus) -> RevSurface
        
            Constructs a new surface of revolution from the values of a torus.
        
            torus: A torus.
            Returns: A new surface of revolution, or null if any of the inputs is invalid or on error.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class RTree(object, IDisposable):
    """
    Represents a spatial search structure based on implementations of the
                R-tree algorithm by Toni Gutman.
    
    RTree()
    """
    def Clear(self):
        """
        Clear(self: RTree)
            Removes all elements.
        """
        pass

    @staticmethod
    def CreateMeshFaceTree(mesh):
        """
        CreateMeshFaceTree(mesh: Mesh) -> RTree
        
            Constructs a new tree with an element for each face in the mesh.
                    The element id is 
             set to the index of the face.
        
        
            mesh: A mesh.
            Returns: A new tree, or null on error.
        """
        pass

    @staticmethod
    def CreatePointCloudTree(cloud):
        """
        CreatePointCloudTree(cloud: PointCloud) -> RTree
        
            Constructs a new tree with an element for each pointcloud point.
        
            cloud: A pointcloud.
            Returns: A new tree, or null on error.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: RTree)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Insert(self, *__args):
        """
        Insert(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        
            Inserts an element into the tree.
        
            box: A bounding box.
            elementId: A pointer.
            Returns: true if element was successfully inserted.
        Insert(self: RTree, point: Point2d, elementId: int) -> bool
        
            Inserts an element into the tree.
        
            point: A point.
            elementId: A number.
            Returns: true if element was successfully inserted.
        Insert(self: RTree, point: Point2d, elementId: IntPtr) -> bool
        
            Inserts an element into the tree.
        
            point: A point.
            elementId: A pointer.
            Returns: true if element was successfully inserted.
        Insert(self: RTree, point: Point3d, elementId: int) -> bool
        
            Inserts an element into the tree.
        
            point: A point.
            elementId: A number.
            Returns: true if element was successfully inserted.
        Insert(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        
            Inserts an element into the tree.
        
            point: A point.
            elementId: A pointer.
            Returns: true if element was successfully inserted.
        Insert(self: RTree, box: BoundingBox, elementId: int) -> bool
        
            Inserts an element into the tree.
        
            box: A bounding box.
            elementId: A number.
            Returns: true if element was successfully inserted.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: RTree, box: BoundingBox, elementId: IntPtr) -> bool
        
            Removes an element from the tree.
        
            box: A bounding box.
            elementId: A pointer.
            Returns: true if element was successfully removed.
        Remove(self: RTree, point: Point2d, elementId: int) -> bool
        
            Removes an element from the tree.
        
            point: A point.
            elementId: A number.
            Returns: true if element was successfully removed.
        Remove(self: RTree, box: BoundingBox, elementId: int) -> bool
        
            Removes an element from the tree.
        
            box: A bounding box.
            elementId: A number.
            Returns: true if element was successfully removed.
        Remove(self: RTree, point: Point3d, elementId: int) -> bool
        
            Removes an element from the tree.
        
            point: A point.
            elementId: A number.
            Returns: true if element was successfully removed.
        Remove(self: RTree, point: Point3d, elementId: IntPtr) -> bool
        
            Removes an element from the tree.
        
            point: A point.
            elementId: A pointer.
            Returns: true if element was successfully removed.
        """
        pass

    def Search(self, *__args):
        """
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, sphere: Sphere, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs]) -> bool
        Search(self: RTree, box: BoundingBox, callback: EventHandler[RTreeEventArgs], tag: object) -> bool
        """
        pass

    @staticmethod
    def SearchOverlaps(treeA, treeB, tolerance, callback):
        """ SearchOverlaps(treeA: RTree, treeB: RTree, tolerance: float, callback: EventHandler[RTreeEventArgs]) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in this tree.

Get: Count(self: RTree) -> int

"""



class RTreeEventArgs(EventArgs):
    """
    Represents event data that is passed when when an item that meets certain 
                criteria is found and the passed RTree event is raised.
    """
    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if the search should be conducted farther.

Get: Cancel(self: RTreeEventArgs) -> bool

Set: Cancel(self: RTreeEventArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of the found item.

Get: Id(self: RTreeEventArgs) -> int

"""

    IdB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If search is using two r-trees, IdB is element b in the search.

Get: IdB(self: RTreeEventArgs) -> int

"""

    IdBPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If search is using two r-trees, IdB is the element b pointer in the search.

Get: IdBPtr(self: RTreeEventArgs) -> IntPtr

"""

    IdPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier pointer of the found item.

Get: IdPtr(self: RTreeEventArgs) -> IntPtr

"""

    SearchBoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bounding box bounds used during a search. You may modify the box in a search callback
            to help reduce the bounds to search.

Get: SearchBoundingBox(self: RTreeEventArgs) -> BoundingBox

Set: SearchBoundingBox(self: RTreeEventArgs) = value
"""

    SearchSphere = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sphere bounds used during a search. You can modify the sphere in a search callback to
            help reduce the bounds to search.

Get: SearchSphere(self: RTreeEventArgs) -> Sphere

Set: SearchSphere(self: RTreeEventArgs) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an arbitrary object that can be attached to this event args.
            This object will "stick" through a single search and can represent user-defined state.

Get: Tag(self: RTreeEventArgs) -> object

Set: Tag(self: RTreeEventArgs) = value
"""



class SpaceMorph(object):
    """ Represents a spacial, Euclidean morph. """
    @staticmethod
    def IsMorphable(geometry):
        """
        IsMorphable(geometry: GeometryBase) -> bool
        
            true if the geometry can be morphed by calling SpaceMorph.Morph(geometry)
        """
        pass

    def Morph(self, geometry):
        """
        Morph(self: SpaceMorph, geometry: GeometryBase) -> bool
        
            Apply the space morph to geometry.
        
            geometry: Geometry to morph.
            Returns: true on success, false on failure.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: SpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point. This method is abstract.
        
            point: A point that will be morphed by this function.
            Returns: Resulting morphed point.
        """
        pass

    PreserveStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the morph should be done in a way that preserves the structure of the geometry.
            In particular, for NURBS objects, true means that only the control points are moved.
            The PreserveStructure value does not affect the way meshes and points are morphed.
            The default is false.

Get: PreserveStructure(self: SpaceMorph) -> bool

Set: PreserveStructure(self: SpaceMorph) = value
"""

    QuickPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the morph should be done as quickly as possible because the result
            is being used for some type of dynamic preview. If QuickPreview is true,
            the tolerance may be ignored.
            The QuickPreview value does not affect the way meshes and points are morphed.
            The default is false.

Get: QuickPreview(self: SpaceMorph) -> bool

Set: QuickPreview(self: SpaceMorph) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The desired accuracy of the morph. This value is primarily used for deforming
            surfaces and breps. The default is 0.0 and any value <= 0.0 is ignored by
            morphing functions. The Tolerance value does not affect the way meshes and points
            are morphed.

Get: Tolerance(self: SpaceMorph) -> float

Set: Tolerance(self: SpaceMorph) = value
"""



class Sphere(object, IEpsilonComparable[Sphere]):
    """
    Represents the plane and radius values of a sphere.
    
    Sphere(center: Point3d, radius: float)
    Sphere(equatorialPlane: Plane, radius: float)
    """
    def ClosestParameter(self, testPoint, longitudeRadians, latitudeRadians):
        """
        ClosestParameter(self: Sphere, testPoint: Point3d) -> (bool, float, float)
        
            Finds the angle parameters on this sphere that are closest to a test point.
        
            testPoint: Point to project onto the sphere.
            Returns: true on success, false on failure. This function will fail if the point it coincident with the 
             sphere center.
        """
        pass

    def ClosestPoint(self, testPoint):
        """
        ClosestPoint(self: Sphere, testPoint: Point3d) -> Point3d
        
            Returns point on sphere that is closest to given point.
        
            testPoint: Point to project onto Sphere.
            Returns: Point on sphere surface closest to testPoint.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Sphere, other: Sphere, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    @staticmethod
    def FitSphereToPoints(points):
        """ FitSphereToPoints(points: IEnumerable[Point3d]) -> Sphere """
        pass

    def LatitudeDegrees(self, degrees):
        """
        LatitudeDegrees(self: Sphere, degrees: float) -> Circle
        
            Computes the parallel at a specific latitude angle.
                    The angle is specified in 
             degrees.
        
        
            degrees: An angle in degrees for the meridian.
            Returns: A circle.
        """
        pass

    def LatitudeRadians(self, radians):
        """
        LatitudeRadians(self: Sphere, radians: float) -> Circle
        
            Computes the parallel at a specific latitude angle.
                    The angle is specified in 
             radians.
        
        
            radians: An angle in radians for the parallel.
            Returns: A circle.
        """
        pass

    def LongitudeDegrees(self, degrees):
        """
        LongitudeDegrees(self: Sphere, degrees: float) -> Circle
        
            Computes the meridian at a specific longitude angle.
                    The angle is specified in 
             degrees.
        
        
            degrees: An angle in degrees.
            Returns: A circle.
        """
        pass

    def LongitudeRadians(self, radians):
        """
        LongitudeRadians(self: Sphere, radians: float) -> Circle
        
            Computes the meridian at a specific longitude angle.
                    The angle is specified in 
             radians.
        
        
            radians: An angle in radians.
            Returns: A circle.
        """
        pass

    def NormalAt(self, longitudeRadians, latitudeRadians):
        """
        NormalAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Vector3d
        
            Computes the normal at a specific angular location on the sphere.
        
            longitudeRadians: A number within the interval [0, 2pi].
            latitudeRadians: A number within the interval [-pi/2, pi/2].
            Returns: A vector.
        """
        pass

    def PointAt(self, longitudeRadians, latitudeRadians):
        """
        PointAt(self: Sphere, longitudeRadians: float, latitudeRadians: float) -> Point3d
        
            Evaluates the sphere at specific longitude and latitude angles.
        
            longitudeRadians: A number within the interval [0, 2pi].
            latitudeRadians: A number within the interval [-pi/2,pi/2].
            Returns: A point value.
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        
            Rotates this sphere about a point and an axis.
        
            sinAngle: sin(angle)
            cosAngle: cod(angle)
            axisOfRotation: Axis of rotation.
            centerOfRotation: Center of rotation.
            Returns: true on success; false on failure.
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d, centerOfRotation: Point3d) -> bool
        
            Rotates this sphere about a point and an axis.
        
            angleRadians: Rotation angle (in Radians)
            axisOfRotation: Axis of rotation.
            centerOfRotation: Center of rotation.
            Returns: true on success; false on failure.
        Rotate(self: Sphere, sinAngle: float, cosAngle: float, axisOfRotation: Vector3d) -> bool
        
            Rotates this sphere about the center point.
        
            sinAngle: sin(angle)
            cosAngle: cos(angle)
            axisOfRotation: The direction of the axis of rotation.
            Returns: true on success; false on failure.
        Rotate(self: Sphere, angleRadians: float, axisOfRotation: Vector3d) -> bool
        
            Rotates the sphere about the center point.
        
            angleRadians: Angle of rotation (in radians)
            axisOfRotation: Rotation axis.
            Returns: true on success; false on failure.
        """
        pass

    def ToBrep(self):
        """
        ToBrep(self: Sphere) -> Brep
        
            Converts this sphere is it Brep representation
        """
        pass

    def ToNurbsSurface(self):
        """
        ToNurbsSurface(self: Sphere) -> NurbsSurface
        
            Converts this sphere to its NurbsSurface representation. 
                    This is synonymous with 
             calling NurbsSurface.CreateFromSphere().
        
            Returns: A nurbs surface representation of this sphere or null.
        """
        pass

    def ToRevSurface(self):
        """
        ToRevSurface(self: Sphere) -> RevSurface
        
            Converts this Sphere to a RevSurface representation. 
                    This is synonymous with 
             calling RevSurface.CreateFromSphere().
        
            Returns: A surface of revolution representation of this sphere or null.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Sphere, xform: Transform) -> bool
        
            Transforms this sphere. Note that non-similarity preserving transformations 
                    cannot 
             be applied to a sphere as that would result in an ellipsoid.
        
        
            xform: Transformation matrix to apply.
            Returns: true on success, false on failure.
        """
        pass

    def Translate(self, delta):
        """
        Translate(self: Sphere, delta: Vector3d) -> bool
        
            Moves this sphere along a motion vector.
        
            delta: Motion vector.
            Returns: true on success; false on failure.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Sphere]() -> Sphere
        
        __new__(cls: type, center: Point3d, radius: float)
        __new__(cls: type, equatorialPlane: Plane, radius: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the world aligned boundingbox for this Sphere. 
            If the Sphere is Invalid, an empty box is returned.

Get: BoundingBox(self: Sphere) -> BoundingBox

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center point of the sphere.

Get: Center(self: Sphere) -> Point3d

Set: Center(self: Sphere) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the diameter for this sphere.

Get: Diameter(self: Sphere) -> float

Set: Diameter(self: Sphere) = value
"""

    EquitorialPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Equatorial plane for this sphere.

Get: EquitorialPlane(self: Sphere) -> Plane

Set: EquitorialPlane(self: Sphere) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the sphere is valid.

Get: IsValid(self: Sphere) -> bool

"""

    NorthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point at the North Pole of the sphere.
            This is the parameterization singularity that can be obtained,
            at V value +Math.Pi/2.

Get: NorthPole(self: Sphere) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Radius for this sphere.

Get: Radius(self: Sphere) -> float

Set: Radius(self: Sphere) = value
"""

    SouthPole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point at the South Pole of the sphere.
            This is the parameterization singularity that can be obtained,
            at V value -Math.Pi/2.

Get: SouthPole(self: Sphere) -> Point3d

"""


    Unset = None


class SumSurface(Surface, IDisposable, ISerializable):
    """ Represents a sum surface, or an extrusion of a curve along a curved path. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def Create(curveA, curveB):
        """
        Create(curveA: Curve, curveB: Curve) -> SumSurface
        
            Constructs a new sum surface by extruding a curve A along a path B.
        
            curveA: The curve used as extrusion profile.
            curveB: The curve used as path.
            Returns: A new sum surface on success; null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SurfaceCurvature(object):
    """ Maintains computed information for surface curvature evaluation. """
    def Direction(self, direction):
        """
        Direction(self: SurfaceCurvature, direction: int) -> Vector3d
        
            Gets the principal curvature direction vector.
        
            direction: Direction index, valid values are 0 and 1.
            Returns: The specified direction vector.
        """
        pass

    def Kappa(self, direction):
        """
        Kappa(self: SurfaceCurvature, direction: int) -> float
        
            Gets the Kappa curvature value.
        
            direction: Kappa index, valid values are 0 and 1.
            Returns: The specified kappa value.
        """
        pass

    def OsculatingCircle(self, direction):
        """
        OsculatingCircle(self: SurfaceCurvature, direction: int) -> Circle
        
            Computes the osculating circle along the given direction.
        
            direction: Direction index, valid values are 0 and 1.
            Returns: The osculating circle in the given direction or Circle.Unset on failure.
        """
        pass

    Gaussian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Gaussian curvature value at UV.

Get: Gaussian(self: SurfaceCurvature) -> float

"""

    Mean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Mean curvature value at UV.

Get: Mean(self: SurfaceCurvature) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the surface normal at UV.

Get: Normal(self: SurfaceCurvature) -> Vector3d

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the surface point at UV.

Get: Point(self: SurfaceCurvature) -> Point3d

"""

    UVPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the UV location where the curvature was computed.

Get: UVPoint(self: SurfaceCurvature) -> Point2d

"""



class SweepOneRail(object):
    """
    Utility class for generating breps by sweeping cross section curves over
                a single rail curve.
    
    SweepOneRail()
    """
    def PerformSweep(self, rail, *__args):
        """
        PerformSweep(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve]) -> Array[Brep]
        PerformSweep(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve], crossSectionParameters: IEnumerable[float]) -> Array[Brep]
        PerformSweep(self: SweepOneRail, rail: Curve, crossSection: Curve) -> Array[Brep]
        PerformSweep(self: SweepOneRail, rail: Curve, crossSection: Curve, crossSectionParameter: float) -> Array[Brep]
        """
        pass

    def PerformSweepRebuild(self, rail, *__args):
        """
        PerformSweepRebuild(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve], rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve], crossSectionParameters: IEnumerable[float], rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepOneRail, rail: Curve, crossSection: Curve, rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepOneRail, rail: Curve, crossSection: Curve, crossSectionParameter: float, rebuildCount: int) -> Array[Brep]
        """
        pass

    def PerformSweepRefit(self, rail, *__args):
        """
        PerformSweepRefit(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve], refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepOneRail, rail: Curve, crossSections: IEnumerable[Curve], crossSectionParameters: IEnumerable[float], refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepOneRail, rail: Curve, crossSection: Curve, refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepOneRail, rail: Curve, crossSection: Curve, crossSectionParameter: float, refitTolerance: float) -> Array[Brep]
        """
        pass

    def SetRoadlikeUpDirection(self, up):
        """ SetRoadlikeUpDirection(self: SweepOneRail, up: Vector3d) """
        pass

    def SetToRoadlikeFront(self):
        """ SetToRoadlikeFront(self: SweepOneRail) """
        pass

    def SetToRoadlikeRight(self):
        """ SetToRoadlikeRight(self: SweepOneRail) """
        pass

    def SetToRoadlikeTop(self):
        """ SetToRoadlikeTop(self: SweepOneRail) """
        pass

    AngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleToleranceRadians(self: SweepOneRail) -> float

Set: AngleToleranceRadians(self: SweepOneRail) = value
"""

    ClosedSweep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the input rail is closed, ClosedSweep determines if the swept breps will also
            be closed.

Get: ClosedSweep(self: SweepOneRail) -> bool

Set: ClosedSweep(self: SweepOneRail) = value
"""

    GlobalShapeBlending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the sweep is linearly blended from one end to the other,
            creating sweeps that taper from one cross-section curve to the other.
            If false, the sweep stays constant at the ends and changes more
            rapidly in the middle.

Get: GlobalShapeBlending(self: SweepOneRail) -> bool

Set: GlobalShapeBlending(self: SweepOneRail) = value
"""

    IsFreeform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFreeform(self: SweepOneRail) -> bool

"""

    IsRoadlike = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoadlike(self: SweepOneRail) -> bool

"""

    IsRoadlikeFront = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoadlikeFront(self: SweepOneRail) -> bool

"""

    IsRoadlikeTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoadlikeTop(self: SweepOneRail) -> bool

"""

    IsRoadlineRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoadlineRight(self: SweepOneRail) -> bool

"""

    MiterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """0: don't miter,  1: intersect surfaces and trim sweeps,  2: rotate shapes at kinks and don't trim.

Get: MiterType(self: SweepOneRail) -> int

Set: MiterType(self: SweepOneRail) = value
"""

    SweepTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweepTolerance(self: SweepOneRail) -> float

Set: SweepTolerance(self: SweepOneRail) = value
"""



class SweepTwoRail(object):
    """
    Utility class for generating breps by sweeping cross section curves over
                two rail curves.
    
    SweepTwoRail()
    """
    def PerformSweep(self, rail1, rail2, *__args):
        """
        PerformSweep(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve]) -> Array[Brep]
        PerformSweep(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve], crossSectionParameters1: IEnumerable[float], crossSectionParameters2: IEnumerable[float]) -> Array[Brep]
        PerformSweep(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve) -> Array[Brep]
        PerformSweep(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve, crossSectionParameterRail1: float, crossSectionParameterRail2: float) -> Array[Brep]
        """
        pass

    def PerformSweepRebuild(self, rail1, rail2, *__args):
        """
        PerformSweepRebuild(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve], rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve], crossSectionParametersRail1: IEnumerable[float], crossSectionParametersRail2: IEnumerable[float], rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve, rebuildCount: int) -> Array[Brep]
        PerformSweepRebuild(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve, crossSectionParameterRail1: float, crossSectionParameterRail2: float, rebuildCount: int) -> Array[Brep]
        """
        pass

    def PerformSweepRefit(self, rail1, rail2, *__args):
        """
        PerformSweepRefit(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve], refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSections: IEnumerable[Curve], crossSectionParametersRail1: IEnumerable[float], crossSectionParametersRail2: IEnumerable[float], refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve, refitTolerance: float) -> Array[Brep]
        PerformSweepRefit(self: SweepTwoRail, rail1: Curve, rail2: Curve, crossSection: Curve, crossSectionParameterRail1: float, crossSectionParameterRail2: float, refitTolerance: float) -> Array[Brep]
        """
        pass

    AngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleToleranceRadians(self: SweepTwoRail) -> float

Set: AngleToleranceRadians(self: SweepTwoRail) = value
"""

    ClosedSweep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the input rails are closed, ClosedSweep determines if the swept breps
            will also be closed.

Get: ClosedSweep(self: SweepTwoRail) -> bool

Set: ClosedSweep(self: SweepTwoRail) = value
"""

    MaintainHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaintainHeight(self: SweepTwoRail) -> bool

Set: MaintainHeight(self: SweepTwoRail) = value
"""

    SweepTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweepTolerance(self: SweepTwoRail) -> float

Set: SweepTolerance(self: SweepTwoRail) = value
"""



class TextDot(GeometryBase, IDisposable, ISerializable):
    """
    Represents a text dot, or an annotation entity with text that always faces the camera and always has the same size.
                This class refers to the geometric element that is independent from the document.
    
    TextDot(text: str, location: Point3d)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self, text, location):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, text: str, location: Point3d)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    FontFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Font face used for displaying the dot

Get: FontFace(self: TextDot) -> str

Set: FontFace(self: TextDot) = value
"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height of font used for displaying the dot

Get: FontHeight(self: TextDot) -> int

Set: FontHeight(self: TextDot) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the textdot.

Get: Point(self: TextDot) -> Point3d

Set: Point(self: TextDot) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text of the textdot.

Get: Text(self: TextDot) -> str

Set: Text(self: TextDot) = value
"""



class TextEntity(AnnotationBase, IDisposable, ISerializable):
    """
    Represents text geometry.
                This class refers to the geometric element that is independent from the document.
    
    TextEntity()
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
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

    def Explode(self):
        """
        Explode(self: TextEntity) -> Array[Curve]
        
            Explodes this text entity into an array of curves.
            Returns: An array of curves that forms the outline or content of this text entity.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: GeometryBase)
            Is called when a non-const operation occurs.
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AnnotativeScalingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scale annotation according to detail scale factor in paperspace
            or by 1.0 in paperspace and not in a detail
            Otherwise, dimscale or text scale is used

Get: AnnotativeScalingEnabled(self: TextEntity) -> bool

Set: AnnotativeScalingEnabled(self: TextEntity) = value
"""

    FontIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of font in document font table used by the text.

Get: FontIndex(self: TextEntity) -> int

Set: FontIndex(self: TextEntity) = value
"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the justification of text in relation to its base point.

Get: Justification(self: TextEntity) -> TextJustification

Set: Justification(self: TextEntity) = value
"""

    MaskColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color to use for drawing a text mask when it is enabled. If the mask is
            enabled and MaskColor is System.Drawing.Color.Transparent, then the
            viewport's color will be used for the MaskColor

Get: MaskColor(self: TextEntity) -> Color

Set: MaskColor(self: TextEntity) = value
"""

    MaskEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether or not to draw a Text Mask

Get: MaskEnabled(self: TextEntity) -> bool

Set: MaskEnabled(self: TextEntity) = value
"""

    MaskOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """distance around text to display mask

Get: MaskOffset(self: TextEntity) -> float

Set: MaskOffset(self: TextEntity) = value
"""

    MaskUsesViewportColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the viewport's color is used for the mask color. If
            false, the color defined by MaskColor is used

Get: MaskUsesViewportColor(self: TextEntity) -> bool

Set: MaskUsesViewportColor(self: TextEntity) = value
"""



class TextJustification(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies enumerated constants used to indicate the internal alignment and justification of text.
    
    enum (flags) TextJustification, values: Bottom (65536), BottomCenter (65538), BottomLeft (65537), BottomRight (65540), Center (2), Left (1), Middle (131072), MiddleCenter (131074), MiddleLeft (131073), MiddleRight (131076), None (0), Right (4), Top (262144), TopCenter (262146), TopLeft (262145), TopRight (262148)
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

    Bottom = None
    BottomCenter = None
    BottomLeft = None
    BottomRight = None
    Center = None
    Left = None
    Middle = None
    MiddleCenter = None
    MiddleLeft = None
    MiddleRight = None
    None = None
    Right = None
    Top = None
    TopCenter = None
    TopLeft = None
    TopRight = None
    value__ = None


class Torus(object, IEpsilonComparable[Torus]):
    """
    Represents the value of a plane and two radii in a torus that is oriented in three-dimensional space.
    
    Torus(basePlane: Plane, majorRadius: float, minorRadius: float)
    """
    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Torus, other: Torus, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def ToNurbsSurface(self):
        """
        ToNurbsSurface(self: Torus) -> NurbsSurface
        
            Converts this torus to its nurbs surface representation. 
                    This is synonymous with 
             calling NurbsSurface.CreateFromTorus().
        
            Returns: A nurbs surface representation of this torus, or null on error.
        """
        pass

    def ToRevSurface(self):
        """
        ToRevSurface(self: Torus) -> RevSurface
        
            Convert this torus to a surface of revolution representation. 
                    This is synonymous 
             with calling RevSurface.CreateFromTorus().
        
            Returns: A surface of revolution representation of this torus, or null on error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, basePlane, majorRadius, minorRadius):
        """
        __new__[Torus]() -> Torus
        
        __new__(cls: type, basePlane: Plane, majorRadius: float, minorRadius: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this torus is valid.

Get: IsValid(self: Torus) -> bool

"""

    MajorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the circle that lies at the heart of the torus.

Get: MajorRadius(self: Torus) -> float

Set: MajorRadius(self: Torus) = value
"""

    MinorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the torus section.

Get: MinorRadius(self: Torus) -> float

Set: MinorRadius(self: Torus) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the plane for the torus large circle.

Get: Plane(self: Torus) -> Plane

Set: Plane(self: Torus) = value
"""


    Unset = None


class Transform(object, IComparable[Transform], IEquatable[Transform]):
    """
    Represents the values in a 4x4 transform matrix.
                This is parallel to C++ ON_Xform.
    
    Transform(diagonalValue: float)
    """
    @staticmethod
    def ChangeBasis(*__args):
        """
        ChangeBasis(initialBasisX: Vector3d, initialBasisY: Vector3d, initialBasisZ: Vector3d, finalBasisX: Vector3d, finalBasisY: Vector3d, finalBasisZ: Vector3d) -> Transform
        
            Computes a change of basis transformation. A basis change is essentially a remapping 
                  
               of geometry from one coordinate system to another.
        
        
            initialBasisX: can be any 3d basis.
            initialBasisY: can be any 3d basis.
            initialBasisZ: can be any 3d basis.
            finalBasisX: can be any 3d basis.
            finalBasisY: can be any 3d basis.
            finalBasisZ: can be any 3d basis.
            Returns: A transformation matrix which orients geometry from one coordinate system to another on success.
             
                    Transform.Unset on failure.
        
        ChangeBasis(plane0: Plane, plane1: Plane) -> Transform
        
            Computes a change of basis transformation. A basis change is essentially a remapping 
                  
               of geometry from one coordinate system to another.
        
        
            plane0: Coordinate system in which the geometry is currently described.
            plane1: Target coordinate system in which we want the geometry to be described.
            Returns: A transformation matrix which orients geometry from one coordinate system to another on success.
             
                    Transform.Unset on failure.
        """
        pass

    def CompareTo(self, other):
        """
        CompareTo(self: Transform, other: Transform) -> int
        
            Compares this transform with another transform.
                    M33 has highest value, then M32, 
             etc..
        
        
            other: Another transform.
            Returns: -1 if this < other; 0 if both are equal; 1 otherwise.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Transform, other: Transform) -> bool
        
            Determines if another transform equals this transform value.
        
            other: Another transform.
            Returns: true if other has the same value as this transform; otherwise, false.
        Equals(self: Transform, obj: object) -> bool
        
            Determines if another object is a transform and its value equals this transform value.
        
            obj: Another object.
            Returns: true if obj is a transform and has the same value as this transform; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Transform) -> int
        
            Gets a non-unique hashing code for this transform.
            Returns: A number that can be used to hash this transform in a dictionary.
        """
        pass

    @staticmethod
    def Mirror(*__args):
        """
        Mirror(mirrorPlane: Plane) -> Transform
        
            Constructs a new Mirror transformation.
        
            mirrorPlane: Plane that defines the mirror orientation and position.
            Returns: A transformation matrix which mirrors geometry in a specified plane.
        Mirror(pointOnMirrorPlane: Point3d, normalToMirrorPlane: Vector3d) -> Transform
        
            Create mirror transformation matrix
                    The mirror transform maps a point Q to 
               
                  Q - (2*(Q-P)oN)*N, where
                    P = pointOnMirrorPlane and N = normalToMirrorPlane.
        
        
            pointOnMirrorPlane: Point on the mirror plane.
            normalToMirrorPlane: Normal vector to the mirror plane.
            Returns: A transformation matrix which mirrors geometry in a specified plane.
        """
        pass

    @staticmethod
    def Multiply(a, b):
        """
        Multiply(a: Transform, b: Transform) -> Transform
        
            Multiplies (combines) two transformations.
                    This is the same as the * operator 
             between two transformations.
        
        
            a: First transformation.
            b: Second transformation.
            Returns: A transformation matrix that combines the effect of both input transformations. 
                    
             The resulting Transform gives the same result as though you'd first apply A then B.
        """
        pass

    @staticmethod
    def PlanarProjection(plane):
        """
        PlanarProjection(plane: Plane) -> Transform
        
            Constructs a projection transformation.
        
            plane: Plane onto which everything will be perpendicularly projected.
            Returns: A transformation matrix which projects geometry onto a specified plane.
        """
        pass

    @staticmethod
    def PlaneToPlane(plane0, plane1):
        """ PlaneToPlane(plane0: Plane, plane1: Plane) -> Transform """
        pass

    @staticmethod
    def Rotation(*__args):
        """
        Rotation(startDirection: Vector3d, endDirection: Vector3d, rotationCenter: Point3d) -> Transform
        
            Constructs a new rotation transformation with start and end directions and rotation center.
        
            startDirection: A start direction.
            endDirection: An end direction.
            rotationCenter: A rotation center.
            Returns: A transformation matrix which rotates geometry around an anchor point.
        Rotation(x0: Vector3d, y0: Vector3d, z0: Vector3d, x1: Vector3d, y1: Vector3d, z1: Vector3d) -> Transform
        
            Constructs a transformation that maps X0 to X1, Y0 to Y1, Z0 to Z1.
        
            x0: First "from" vector.
            y0: Second "from" vector.
            z0: Third "from" vector.
            x1: First "to" vector.
            y1: Second "to" vector.
            z1: Third "to" vector.
            Returns: A rotation transformation value.
        Rotation(angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> Transform
        
            Constructs a new rotation transformation with specified angle, rotation center and rotation axis.
        
            angleRadians: Angle (in Radians) of the rotation.
            rotationAxis: Axis direction of rotation operation.
            rotationCenter: Center point of rotation. Rotation axis is vertical.
            Returns: A transformation matrix which rotates geometry around an anchor point.
        Rotation(sinAngle: float, cosAngle: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> Transform
        
            Constructs a new rotation transformation with specified angle, rotation center and rotation axis.
        
            sinAngle: Sin of the rotation angle.
            cosAngle: Cos of the rotation angle.
            rotationAxis: Axis direction of rotation.
            rotationCenter: Center point of rotation.
            Returns: A transformation matrix which rotates geometry around an anchor point.
        Rotation(angleRadians: float, rotationCenter: Point3d) -> Transform
        
            Constructs a new rotation transformation with specified angle and rotation center.
        
            angleRadians: Angle (in Radians) of the rotation.
            rotationCenter: Center point of rotation. Rotation axis is vertical.
            Returns: A transformation matrix which rotates geometry around an anchor point.
        """
        pass

    @staticmethod
    def Scale(*__args):
        """
        Scale(plane: Plane, xScaleFactor: float, yScaleFactor: float, zScaleFactor: float) -> Transform
        
            Constructs a new non-uniform scaling transformation with a specified scaling anchor point.
        
            plane: Defines the center and orientation of the scaling operation.
            xScaleFactor: Scaling factor along the anchor plane X-Axis direction.
            yScaleFactor: Scaling factor along the anchor plane Y-Axis direction.
            zScaleFactor: Scaling factor along the anchor plane Z-Axis direction.
            Returns: A transformation matrix which scales geometry non-uniformly.
        Scale(anchor: Point3d, scaleFactor: float) -> Transform
        
            Constructs a new uniform scaling transformation with a specified scaling anchor point.
        
            anchor: Defines the anchor point of the scaling operation.
            scaleFactor: Scaling factor in all directions.
            Returns: A transform matrix which scales geometry uniformly around the anchor point.
        """
        pass

    @staticmethod
    def Shear(plane, x, y, z):
        """
        Shear(plane: Plane, x: Vector3d, y: Vector3d, z: Vector3d) -> Transform
        
            Constructs a Shear transformation.
        
            plane: Base plane for shear.
            x: Shearing vector along plane x-axis.
            y: Shearing vector along plane y-axis.
            z: Shearing vector along plane z-axis.
            Returns: A transformation matrix which shear geometry.
        """
        pass

    def ToFloatArray(self, rowDominant):
        """
        ToFloatArray(self: Transform, rowDominant: bool) -> Array[Single]
        
            Return the matrix as a linear array of 16 float values
        """
        pass

    def ToString(self):
        """
        ToString(self: Transform) -> str
        
            Returns a string representation of this transform.
            Returns: A textual representation.
        """
        pass

    def TransformBoundingBox(self, bbox):
        """
        TransformBoundingBox(self: Transform, bbox: BoundingBox) -> BoundingBox
        
            Computes a new boundingbox that is the smallest axis aligned
                    boundingbox that 
             contains the transformed result of its 8 original corner
                    points.
        
            Returns: A new bounding box.
        """
        pass

    def TransformList(self, points):
        """ TransformList(self: Transform, points: IEnumerable[Point3d]) -> Array[Point3d] """
        pass

    @staticmethod
    def Translation(*__args):
        """
        Translation(dx: float, dy: float, dz: float) -> Transform
        
            Constructs a new translation (move) tranformation. 
                    Right column is (dx, dy, dz, 
             1.0).
        
        
            dx: Distance to translate (move) geometry along the world X axis.
            dy: Distance to translate (move) geometry along the world Y axis.
            dz: Distance to translate (move) geometry along the world Z axis.
            Returns: A transform matrix which moves geometry with the specified distances.
        Translation(motion: Vector3d) -> Transform
        
            Constructs a new translation (move) transformation.
        
            motion: Translation (motion) vector.
            Returns: A transform matrix which moves geometry along the motion vector.
        """
        pass

    def Transpose(self):
        """
        Transpose(self: Transform) -> Transform
        
            Flip row/column values
        """
        pass

    def TryGetInverse(self, inverseTransform):
        """
        TryGetInverse(self: Transform) -> (bool, Transform)
        
            Attempts to get the inverse transform of this transform.
            Returns: true on success. 
                    If false is returned and this Transform is Invalid, 
             inserveTransform will be set to this Transform. 
                    If false is returned and this 
             Transform is Valid, inverseTransform will be set to a pseudo inverse.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diagonalValue):
        """
        __new__[Transform]() -> Transform
        
        __new__(cls: type, diagonalValue: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(a: Transform, b: Transform) -> Transform
        
            Multiplies (combines) two transformations.
        
            a: First transformation.
            b: Second transformation.
            Returns: A transformation matrix that combines the effect of both input transformations. 
                    
             The resulting Transform gives the same result as though you'd first apply A then B.
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The determinant of this 4x4 matrix.

Get: Determinant(self: Transform) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this Transform is a valid matrix. 
            A valid transform matrix is not allowed to have any invalid numbers.

Get: IsValid(self: Transform) -> bool

"""

    M00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[0,0].

Get: M00(self: Transform) -> float

Set: M00(self: Transform) = value
"""

    M01 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[0,1].

Get: M01(self: Transform) -> float

Set: M01(self: Transform) = value
"""

    M02 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[0,2].

Get: M02(self: Transform) -> float

Set: M02(self: Transform) = value
"""

    M03 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[0,3].

Get: M03(self: Transform) -> float

Set: M03(self: Transform) = value
"""

    M10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[1,0].

Get: M10(self: Transform) -> float

Set: M10(self: Transform) = value
"""

    M11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[1,1].

Get: M11(self: Transform) -> float

Set: M11(self: Transform) = value
"""

    M12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[1,2].

Get: M12(self: Transform) -> float

Set: M12(self: Transform) = value
"""

    M13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[1,3].

Get: M13(self: Transform) -> float

Set: M13(self: Transform) = value
"""

    M20 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[2,0].

Get: M20(self: Transform) -> float

Set: M20(self: Transform) = value
"""

    M21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[2,1].

Get: M21(self: Transform) -> float

Set: M21(self: Transform) = value
"""

    M22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[2,2].

Get: M22(self: Transform) -> float

Set: M22(self: Transform) = value
"""

    M23 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[2,3].

Get: M23(self: Transform) -> float

Set: M23(self: Transform) = value
"""

    M30 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[3,0].

Get: M30(self: Transform) -> float

Set: M30(self: Transform) = value
"""

    M31 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[3,1].

Get: M31(self: Transform) -> float

Set: M31(self: Transform) = value
"""

    M32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[3,2].

Get: M32(self: Transform) -> float

Set: M32(self: Transform) = value
"""

    M33 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets this[3,3].

Get: M33(self: Transform) -> float

Set: M33(self: Transform) = value
"""

    SimilarityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the Transform maintains similarity. 
            The easiest way to think of Similarity is that any circle, when transformed, 
            remains a circle. Whereas a non-similarity Transform deforms circles into ellipses.

Get: SimilarityType(self: Transform) -> TransformSimilarityType

"""


    Identity = None
    Unset = None


class TransformSimilarityType(Enum, IComparable, IFormattable, IConvertible):
    """
    Lists all possible outcomes for transform similarity.
    
    enum TransformSimilarityType, values: NotSimilarity (0), OrientationPreserving (1), OrientationReversing (-1)
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

    NotSimilarity = None
    OrientationPreserving = None
    OrientationReversing = None
    value__ = None


class Unroller(object):
    """
    Represents the operation of unrolling a single surface.
    
    Unroller(surface: Surface)
    Unroller(brep: Brep)
    """
    def AddFollowingGeometry(self, *__args):
        """
        AddFollowingGeometry(self: Unroller, dot: TextDot)
            Adds a text dot that should be unrolled along with the surface/brep.
        
            dot: A text dot.
        AddFollowingGeometry(self: Unroller, dots: IEnumerable[TextDot])AddFollowingGeometry(self: Unroller, dotLocation: Point3d, dotText: str)
            Adds a text dot that should be unrolled along with the surface/brep.
        
            dotLocation: A dot point.
            dotText: A dot text.
        AddFollowingGeometry(self: Unroller, dotLocations: IEnumerable[Point3d], dotText: IEnumerable[str])AddFollowingGeometry(self: Unroller, point: Point)
            Adds a point that should be unrolled along with the surface/brep.
        
            point: A point.
        AddFollowingGeometry(self: Unroller, curve: Curve)
            Adds a curve that should be unrolled along with the surface/brep.
        
            curve: The curve.
        AddFollowingGeometry(self: Unroller, curves: IEnumerable[Curve])AddFollowingGeometry(self: Unroller, point: Point3d)
            Adds a point that should be unrolled along with the surface/brep.
        
            point: A point.
        AddFollowingGeometry(self: Unroller, points: IEnumerable[Point3d])
        """
        pass

    def PerformUnroll(self, unrolledCurves, unrolledPoints, unrolledDots):
        """
        PerformUnroll(self: Unroller) -> (Array[Brep], Array[Curve], Array[Point3d], Array[TextDot])
        
            Executes unrolling operations.
            Returns: An array of breps. This array can be empty.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, surface: Surface)
        __new__(cls: type, brep: Brep)
        """
        pass

    AbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the absolute tolerance for the unrolling operation.
            Absolute tolerance is used in the evaluation of new entities,
            such as intersections, reprojections and splits.In the current implementation, absolute tolerance is used 
            in tessellating rails, fitting curves and pulling back trims.

Get: AbsoluteTolerance(self: Unroller) -> float

Set: AbsoluteTolerance(self: Unroller) = value
"""

    ExplodeOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value determining whether geometry should be exploded.

Get: ExplodeOutput(self: Unroller) -> bool

Set: ExplodeOutput(self: Unroller) = value
"""

    ExplodeSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value determining whether spacing should be exploded.

Get: ExplodeSpacing(self: Unroller) -> float

Set: ExplodeSpacing(self: Unroller) = value
"""

    RelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the relative tolerance for the unrolling operation.
            Relative tolerance is used in the evaluation of intrinsic properties,
            such as computations "along" the surface or brep.In the current implementation, relative tolerance is used to decide
            if a surface is flat enough to try to unroll. That helps ease the scale dependency.
            The surface has to be linear in one direction within (length * RelativeTolerance)
            to be considered linear for that purpose. Otherwise smash will ignore that tolerance and
            unroll anything.

Get: RelativeTolerance(self: Unroller) -> float

Set: RelativeTolerance(self: Unroller) = value
"""



class Vector2d(object, ISerializable, IEquatable[Vector2d], IComparable[Vector2d], IComparable, IEpsilonComparable[Vector2d]):
    """
    Represents the two components of a vector in two-dimensional space,
                using System.Double-precision floating point numbers.
    
    Vector2d(x: float, y: float)
    """
    def CompareTo(self, other):
        """
        CompareTo(self: Vector2d, other: Vector2d) -> int
        
            Compares this Rhino.Geometry.Vector2d with another Rhino.Geometry.Vector2d.
                    
             Components evaluation priority is first X, then Y.
        
        
            other: The other Rhino.Geometry.Vector2d to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y+1: otherwise.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Vector2d, other: Vector2d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector2d, vector: Vector2d) -> bool
        
            Determines whether the specified vector has the same value as the present vector.
        
            vector: The specified vector.
            Returns: true if vector has the same components as this; otherwise false.
        Equals(self: Vector2d, obj: object) -> bool
        
            Determines whether the specified System.Object is a Vector2d and has the same value as the 
             present vector.
        
        
            obj: The specified object.
            Returns: true if obj is Vector2d and has the same components as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector2d) -> int
        
            Provides a hashing value for the present vector.
            Returns: A non-unique number based on vector components.
        """
        pass

    def ToString(self):
        """
        ToString(self: Vector2d) -> str
        
            Constructs a string representation of the current vector.
            Returns: A string in the form X,Y.
        """
        pass

    def Unitize(self):
        """
        Unitize(self: Vector2d) -> bool
        
            Unitizes the vector in place. A unit vector has length 1 unit. 
                    An invalid or zero 
             length vector cannot be unitized.
        
            Returns: true on success or false on failure.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__[Vector2d]() -> Vector2d
        
        __new__(cls: type, x: float, y: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this vector is valid. 
            A valid vector must be formed of valid component values for x, y and z.

Get: IsValid(self: Vector2d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Computes the length (or magnitude, or size) of this vector.
            This is an application of Pythagoras' theorem.

Get: Length(self: Vector2d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of this vector.

Get: X(self: Vector2d) -> float

Set: X(self: Vector2d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of this vector.

Get: Y(self: Vector2d) -> float

Set: Y(self: Vector2d) = value
"""


    Unset = None
    Zero = None


class Vector2f(object, IEquatable[Vector2f], IComparable[Vector2f], IComparable, IEpsilonFComparable[Vector2f]):
    """
    Represents the two components of a vector in two-dimensional space,
                using System.Single-precision floating point numbers.
    """
    def CompareTo(self, other):
        """
        CompareTo(self: Vector2f, other: Vector2f) -> int
        
            Compares this Rhino.Geometry.Vector2f with another Rhino.Geometry.Vector2f.
                    
             Components evaluation priority is first X, then Y.
        
        
            other: The other Rhino.Geometry.Vector2f to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y+1: otherwise.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Vector2f, other: Vector2f, epsilon: Single) -> bool
        
            Check that all values in other are withing epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector2f, vector: Vector2f) -> bool
        
            Determines whether the specified vector has the same values as the present vector.
        
            vector: The specified vector.
            Returns: true if obj is Vector2f and has the same coordinates as this; otherwise false.
        Equals(self: Vector2f, obj: object) -> bool
        
            Determines whether the specified System.Object is a Vector2f and has the same values as the 
             present vector.
        
        
            obj: The specified object.
            Returns: true if obj is Vector2f and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector2f) -> int
        
            Computes a hash number that represents the current vector.
            Returns: A hash code that is not unique for each vector.
        """
        pass

    def ToString(self):
        """
        ToString(self: Vector2f) -> str
        
            Constructs the string representation of the current vector.
            Returns: The vector representation in the form X,Y,Z.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of this vector.

Get: X(self: Vector2f) -> Single

Set: X(self: Vector2f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of this vector.

Get: Y(self: Vector2f) -> Single

Set: Y(self: Vector2f) = value
"""



class Vector3d(object, ISerializable, IEquatable[Vector3d], IComparable[Vector3d], IComparable, IEpsilonComparable[Vector3d]):
    """
    Represents the three components of a vector in three-dimensional space,
                using System.Double-precision floating point numbers.
    
    Vector3d(x: float, y: float, z: float)
    Vector3d(point: Point3d)
    Vector3d(vector: Vector3f)
    Vector3d(vector: Vector3d)
    """
    @staticmethod
    def Add(vector1, vector2):
        """
        Add(vector1: Vector3d, vector2: Vector3d) -> Vector3d
        
            Sums up two vectors.
                    (Provided for languages that do not support operator 
             overloading. You can use the + operator otherwise)
        
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A new vector that results from the componentwise addition of the two vectors.
        """
        pass

    def CompareTo(self, other):
        """
        CompareTo(self: Vector3d, other: Vector3d) -> int
        
            Compares this Rhino.Geometry.Vector3d with another Rhino.Geometry.Vector3d.
                    
             Component evaluation priority is first X, then Y, then Z.
        
        
            other: The other Rhino.Geometry.Vector3d to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
        """
        pass

    @staticmethod
    def CrossProduct(a, b):
        """
        CrossProduct(a: Vector3d, b: Vector3d) -> Vector3d
        
            Computes the cross product (or vector product, or exterior product) of two vectors.
                    
             This operation is not commutative.
        
        
            a: First vector.
            b: Second vector.
            Returns: A new vector that is perpendicular to both a and b,
                    has Length == a.Length * 
             b.Length andwith a result that is oriented following the right hand rule.
        """
        pass

    @staticmethod
    def Divide(vector, t):
        """
        Divide(vector: Vector3d, t: float) -> Vector3d
        
            Divides a Rhino.Geometry.Vector3d by a number, having the effect of shrinking it.
                    
             (Provided for languages that do not support operator overloading. You can use the / operator 
             otherwise)
        
        
            vector: A vector.
            t: A number.
            Returns: A new vector that is componentwise divided by t.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Vector3d, other: Vector3d, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector3d, vector: Vector3d) -> bool
        
            Determines whether the specified vector has the same value as the present vector.
        
            vector: The specified vector.
            Returns: true if vector has the same coordinates as this; otherwise false.
        Equals(self: Vector3d, obj: object) -> bool
        
            Determines whether the specified System.Object is a Vector3d and has the same values as the 
             present vector.
        
        
            obj: The specified object.
            Returns: true if obj is a Vector3d and has the same coordinates as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector3d) -> int
        
            Computes the hash code for the current vector.
            Returns: A non-unique number that represents the components of this vector.
        """
        pass

    def IsParallelTo(self, other, angleTolerance=None):
        """
        IsParallelTo(self: Vector3d, other: Vector3d, angleTolerance: float) -> int
        
            Determines whether this vector is parallel to another vector, within a provided tolerance.
        
            other: Vector to use for comparison.
            angleTolerance: Angle tolerance (in radians).
            Returns: Parallel indicator:
                    +1 = both vectors are parallel.0 = vectors are not parallel or 
             at least one of the vectors is zero.-1 = vectors are anti-parallel.
        
        IsParallelTo(self: Vector3d, other: Vector3d) -> int
        
            Determines whether this vector is parallel to another vector, within one degree (within Pi / 
             180).
        
        
            other: Vector to use for comparison.
            Returns: Parallel indicator:
                    +1 = both vectors are parallel 0 = vectors are not parallel, or 
             at least one of the vectors is zero-1 = vectors are anti-parallel.
        """
        pass

    def IsPerpendicularTo(self, other, angleTolerance=None):
        """
        IsPerpendicularTo(self: Vector3d, other: Vector3d, angleTolerance: float) -> bool
        
            Determines whether this vector is perpendicular to another vector, within a provided angle 
             tolerance.
        
        
            other: Vector to use for comparison.
            angleTolerance: Angle tolerance (in radians).
            Returns: true if vectors form Pi-radians (90-degree) angles with each other; otherwise false.
        IsPerpendicularTo(self: Vector3d, other: Vector3d) -> bool
        
            Test to see whether this vector is perpendicular to within one degree of another one.
        
            other: Vector to compare to.
            Returns: true if both vectors are perpendicular, false if otherwise.
        """
        pass

    def IsTiny(self, tolerance=None):
        """
        IsTiny(self: Vector3d) -> bool
        
            Uses RhinoMath.ZeroTolerance for IsTiny calculation.
            Returns: true if vector is very small, otherwise false.
        IsTiny(self: Vector3d, tolerance: float) -> bool
        
            Determines whether a vector is very short.
        
            tolerance: A nonzero value used as the coordinate zero tolerance.
                    .
            Returns: (Math.Abs(X) <= tiny_tol) AND (Math.Abs(Y) <= tiny_tol) AND (Math.Abs(Z) <= tiny_tol).
        """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(vector1: Vector3d, vector2: Vector3d) -> float
        
            Multiplies two vectors together, returning the dot product (or inner product).
                    This 
             differs from the cross product.
                    (Provided for languages that do not support 
             operator overloading. You can use the * operator otherwise)
        
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A value that results from the evaluation of v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z.
                    This 
             value equals v1.Length * v2.Length * cos(alpha), where alpha is the angle between vectors.
        
        Multiply(t: float, vector: Vector3d) -> Vector3d
        
            Multiplies a vector by a number, having the effect of scaling it.
                    (Provided for 
             languages that do not support operator overloading. You can use the * operator otherwise)
        
        
            t: A number.
            vector: A vector.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        Multiply(vector: Vector3d, t: float) -> Vector3d
        
            Multiplies a vector by a number, having the effect of scaling it.
                    (Provided for 
             languages that do not support operator overloading. You can use the * operator otherwise)
        
        
            vector: A vector.
            t: A number.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        """
        pass

    @staticmethod
    def Negate(vector):
        """
        Negate(vector: Vector3d) -> Vector3d
        
            Computes the opposite vector.
                    (Provided for languages that do not support operator 
             overloading. You can use the - unary operator otherwise)
        
        
            vector: A vector to negate.
            Returns: A new vector where all components were multiplied by -1.
        """
        pass

    def PerpendicularTo(self, other):
        """
        PerpendicularTo(self: Vector3d, other: Vector3d) -> bool
        
            Sets this vector to be perpendicular to another vector. 
                     Result is not unitized.
        
            other: Vector to use as guide.
            Returns: true on success, false if input vector is zero or invalid.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Vector3d) -> bool
        
            Reverses (inverts) this vector in place.
                     If this vector is Invalid, no changes 
             will occur and false will be returned.
        
            Returns: true on success or false if the vector is invalid.
        """
        pass

    def Rotate(self, angleRadians, rotationAxis):
        """
        Rotate(self: Vector3d, angleRadians: float, rotationAxis: Vector3d) -> bool
        
            Rotates this vector around a given axis.
        
            angleRadians: Angle of rotation (in radians).
            rotationAxis: Axis of rotation.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def Subtract(vector1, vector2):
        """
        Subtract(vector1: Vector3d, vector2: Vector3d) -> Vector3d
        
            Subtracts the second vector from the first one.
                    (Provided for languages that do not 
             support operator overloading. You can use the - operator otherwise)
        
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A new vector that results from the componentwise difference of vector1 - vector2.
        """
        pass

    def ToString(self):
        """
        ToString(self: Vector3d) -> str
        
            Returns the string representation of the current vector, in the form X,Y,Z.
            Returns: A string with the current location of the point.
        """
        pass

    def Transform(self, transformation):
        """
        Transform(self: Vector3d, transformation: Transform)
            Transforms the vector in place.
                    The transformation matrix acts on the left of the 
             vector; i.e.,result = transformation*vector
        
        
            transformation: Transformation matrix to apply.
        """
        pass

    def Unitize(self):
        """
        Unitize(self: Vector3d) -> bool
        
            Unitizes the vector in place. A unit vector has length 1 unit. 
                    An invalid or zero 
             length vector cannot be unitized.
        
            Returns: true on success or false on failure.
        """
        pass

    @staticmethod
    def VectorAngle(a, b, plane=None):
        """
        VectorAngle(a: Vector3d, b: Vector3d, plane: Plane) -> float
        
            Computes the angle on a plane between two vectors.
        
            a: First vector.
            b: Second vector.
            plane: Two-dimensional plane on which to perform the angle measurement.
            Returns: On success, the angle (in radians) between a and b as projected onto the plane; 
             RhinoMath.UnsetValue on failure.
        
        VectorAngle(a: Vector3d, b: Vector3d) -> float
        
            Compute the angle between two vectors.
                    This operation is commutative.
        
            a: First vector for angle.
            b: Second vector for angle.
            Returns: If the input is valid, the angle (in radians) between a and b; RhinoMath.UnsetValue otherwise.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Vector3d]() -> Vector3d
        
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, point: Point3d)
        __new__(cls: type, vector: Vector3f)
        __new__(cls: type, vector: Vector3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(vector1: Vector3d, vector2: Vector3d) -> Vector3d
        
            Sums up two vectors.
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A new vector that results from the componentwise addition of the two vectors.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(vector1: Vector3d, vector2: Vector3d) -> float
        
            Multiplies two vectors together, returning the dot product (or inner product).
                    This 
             differs from the cross product.
        
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A value that results from the evaluation of v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z.
                    This 
             value equals v1.Length * v2.Length * cos(alpha), where alpha is the angle between vectors.
        
        __rmul__(t: float, vector: Vector3d) -> Vector3d
        
            Multiplies a vector by a number, having the effect of scaling it.
        
            t: A number.
            vector: A vector.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(vector1: Vector3d, vector2: Vector3d) -> Vector3d
        
            Subtracts the second vector from the first one.
        
            vector1: A vector.
            vector2: A second vector.
            Returns: A new vector that results from the componentwise difference of vector1 - vector2.
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsUnitVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this is a unit vector. 
            A unit vector has length 1.

Get: IsUnitVector(self: Vector3d) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this vector is valid. 
            A valid vector must be formed of valid component values for x, y and z.

Get: IsValid(self: Vector3d) -> bool

"""

    IsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the X, Y, and Z values are all equal to 0.0.

Get: IsZero(self: Vector3d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Computes the length (or magnitude, or size) of this vector.
            This is an application of Pythagoras' theorem.
            If this vector is invalid, its length is considered 0.

Get: Length(self: Vector3d) -> float

"""

    MaximumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the largest (both positive and negative) component value in this vector.

Get: MaximumCoordinate(self: Vector3d) -> float

"""

    MinimumCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the smallest (both positive and negative) component value in this vector.

Get: MinimumCoordinate(self: Vector3d) -> float

"""

    SquareLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Computes the squared length (or magnitude, or size) of this vector.
            This is an application of Pythagoras' theorem.
            While the Length property checks for input validity,
            this property does not. You should check validity in advance,
            if this vector can be invalid.

Get: SquareLength(self: Vector3d) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of the vector.

Get: X(self: Vector3d) -> float

Set: X(self: Vector3d) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of the vector.

Get: Y(self: Vector3d) -> float

Set: Y(self: Vector3d) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z (third) component of the vector.

Get: Z(self: Vector3d) -> float

Set: Z(self: Vector3d) = value
"""


    Unset = None
    XAxis = None
    YAxis = None
    ZAxis = None
    Zero = None


class Vector3f(object, IEquatable[Vector3f], IComparable[Vector3f], IComparable, IEpsilonFComparable[Vector3f]):
    """
    Represents the three components of a vector in three-dimensional space,
                using System.Single-precision floating point numbers.
    
    Vector3f(x: Single, y: Single, z: Single)
    """
    @staticmethod
    def Add(point, vector):
        """
        Add(point: Point3f, vector: Vector3f) -> Point3f
        
            Sums up a point and a vector, and returns a new point.
                    (Provided for languages that 
             do not support operator overloading. You can use the + operator otherwise)
        
        
            point: A point.
            vector: A vector.
            Returns: A new point that results from the addition of point and vector.
        """
        pass

    def CompareTo(self, other):
        """
        CompareTo(self: Vector3f, other: Vector3f) -> int
        
            Compares this Rhino.Geometry.Vector3f with another Rhino.Geometry.Vector3f.
                    
             Component evaluation priority is first X, then Y, then Z.
        
        
            other: The other Rhino.Geometry.Vector3f to use in comparison.
            Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 
             other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
        """
        pass

    @staticmethod
    def CrossProduct(a, b):
        """
        CrossProduct(a: Vector3f, b: Vector3f) -> Vector3f
        
            Computes the cross product (or vector product, or exterior product) of two vectors.
                    
             This operation is not commutative.
        
        
            a: First vector.
            b: Second vector.
            Returns: A new vector that is perpendicular to both a and b,
                    has Length == a.Length * 
             b.Length andwith a result that is oriented following the right hand rule.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: Vector3f, other: Vector3f, epsilon: Single) -> bool
        
            Check that all values in other are withing epsilon of the values in this
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector3f, vector: Vector3f) -> bool
        
            Determines whether the specified vector has the same values as the present vector.
        
            vector: The specified vector.
            Returns: true if vector has the same components as this; otherwise false.
        Equals(self: Vector3f, obj: object) -> bool
        
            Determines whether the specified System.Object is a Vector3f and has the same values as the 
             present vector.
        
        
            obj: The specified object.
            Returns: true if obj is Vector3f and has the same components as this; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector3f) -> int
        
            Computes a hash number that represents the current vector.
            Returns: A hash code that is not unique for each vector.
        """
        pass

    @staticmethod
    def Multiply(*__args):
        """
        Multiply(t: Single, vector: Vector3f) -> Vector3f
        
            Multiplies a vector by a number, having the effect of scaling it.
                    (Provided for 
             languages that do not support operator overloading. You can use the * operator otherwise)
        
        
            t: A number.
            vector: A vector.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        Multiply(vector: Vector3f, t: Single) -> Vector3f
        
            Multiplies a vector by a number, having the effect of scaling it.
                    (Provided for 
             languages that do not support operator overloading. You can use the * operator otherwise)
        
        
            vector: A vector.
            t: A number.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        """
        pass

    def PerpendicularTo(self, other):
        """
        PerpendicularTo(self: Vector3f, other: Vector3f) -> bool
        
            Sets this vector to be perpendicular to another vector. 
                     Result is not unitized.
        
            other: Vector to use as guide.
            Returns: true on success, false if input vector is zero or invalid.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Vector3f) -> bool
        
            Reverses (inverts) this vector in place.
                     If this vector contains 
             RhinoMath.UnsetValue, the 
                     reverse will also be invalid and false will be 
             returned.
        
            Returns: true on success or false if the vector is invalid.
        """
        pass

    def Rotate(self, angleRadians, rotationAxis):
        """
        Rotate(self: Vector3f, angleRadians: float, rotationAxis: Vector3f) -> bool
        
            Rotates this vector around a given axis.
        
            angleRadians: Angle of rotation (in radians).
            rotationAxis: Axis of rotation.
            Returns: true on success, false on failure.
        """
        pass

    def ToString(self):
        """
        ToString(self: Vector3f) -> str
        
            Constructs the string representation of the current vector.
            Returns: The vector representation in the form X,Y,Z.
        """
        pass

    def Transform(self, transformation):
        """
        Transform(self: Vector3f, transformation: Transform)
            Transforms the vector in place.
                    The transformation matrix acts on the left of the 
             vector; i.e.,result = transformation*vector
        
        
            transformation: Transformation matrix to apply.
        """
        pass

    def Unitize(self):
        """
        Unitize(self: Vector3f) -> bool
        
            Unitizes the vector in place. A unit vector has length 1 unit. 
                    An invalid or zero 
             length vector cannot be unitized.
        
            Returns: true on success or false on failure.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y, z):
        """
        __new__[Vector3f]() -> Vector3f
        
        __new__(cls: type, x: Single, y: Single, z: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(point: Point3f, vector: Vector3f) -> Point3f
        
            Sums up a point and a vector, and returns a new point.
        
            point: A point.
            vector: A vector.
            Returns: A new point that results from the addition of point and vector.
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(t: Single, vector: Vector3f) -> Vector3f
        
            Multiplies a vector by a number, having the effect of scaling it.
        
            t: A number.
            vector: A vector.
            Returns: A new vector that is the original vector coordinatewise multiplied by t.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Computes the length (or magnitude, or size) of this vector.
            This is an application of Pythagoras' theorem.
            If this vector is invalid, its length is considered 0.

Get: Length(self: Vector3f) -> Single

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the X (first) component of this vector.

Get: X(self: Vector3f) -> Single

Set: X(self: Vector3f) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Y (second) component of this vector.

Get: Y(self: Vector3f) -> Single

Set: Y(self: Vector3f) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Z (third) component of this vector.

Get: Z(self: Vector3f) -> Single

Set: Z(self: Vector3f) = value
"""


    Unset = None
    XAxis = None
    YAxis = None
    ZAxis = None
    Zero = None


class VolumeMassProperties(object, IDisposable):
    """
    Contains static initialization methods and allows access to the computed
                metrics of volume, volume centroid and volume moments in 
                in solid meshes, in solid surfaces and in solid (closed) boundary representations.
    """
    @staticmethod
    def Compute(*__args):
        """
        Compute(surface: Surface) -> VolumeMassProperties
        
            Compute the VolumeMassProperties for a single Surface.
        
            surface: Surface to measure.
            Returns: The VolumeMassProperties for the given Surface or null on failure.
        Compute(brep: Brep) -> VolumeMassProperties
        
            Compute the VolumeMassProperties for a single Brep.
        
            brep: Brep to measure.
            Returns: The VolumeMassProperties for the given Brep or null on failure.
        Compute(mesh: Mesh) -> VolumeMassProperties
        
            Compute the VolumeMassProperties for a single Mesh.
        
            mesh: Mesh to measure.
            Returns: The VolumeMassProperties for the given Mesh or null on failure.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: VolumeMassProperties)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Sum(self, summand):
        """
        Sum(self: VolumeMassProperties, summand: VolumeMassProperties) -> bool
        
            Sum mass properties together to get an aggregate mass.
        
            summand: mass properties to add.
            Returns: true if successful.
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

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volume centroid in the world coordinate system.

Get: Centroid(self: VolumeMassProperties) -> Point3d

"""

    CentroidCoordinatesMomentsOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moments of inertia with respect to centroid coordinate system.
            X = integral of ((y-y0)^2 + (z-z0)^2) dm
            Y = integral of ((z-z0)^2 + (x-x0)^2) dm
            Z = integral of ((z-z0)^2 + (y-y0)^2) dm
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesMomentsOfInertia(self: VolumeMassProperties) -> Vector3d

"""

    CentroidCoordinatesMomentsOfInertiaError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in centroid coordinates moments of inertia calculation.

Get: CentroidCoordinatesMomentsOfInertiaError(self: VolumeMassProperties) -> Vector3d

"""

    CentroidCoordinatesRadiiOfGyration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radii of gyration with respect to centroid coordinate system.
            X = sqrt(integral of ((y-y0)^2 + (z-z0)^2) dm/M)
            Y = sqrt(integral of ((z-z0)^2 + (x-x0)^2) dm/M)
            Z = sqrt(integral of ((z-z0)^2 + (y-y0)^2) dm/M)
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesRadiiOfGyration(self: VolumeMassProperties) -> Vector3d

"""

    CentroidCoordinatesSecondMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Second moments with respect to centroid coordinate system.
            X = integral of (x-x0)^2 dm
            Y = integral of (y-y0)^2 dm
            Z = integral of (z-z0)^2 dm
            where (x0,y0,z0) = centroid.

Get: CentroidCoordinatesSecondMoments(self: VolumeMassProperties) -> Vector3d

"""

    CentroidCoordinatesSecondMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in centroid coordinates second moments calculation.

Get: CentroidCoordinatesSecondMomentsError(self: VolumeMassProperties) -> Vector3d

"""

    CentroidError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uncertainty in the Centroid calculation.

Get: CentroidError(self: VolumeMassProperties) -> Vector3d

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volume solution.

Get: Volume(self: VolumeMassProperties) -> float

"""

    VolumeError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uncertainty in the volume calculation.

Get: VolumeError(self: VolumeMassProperties) -> float

"""

    WorldCoordinatesFirstMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate first moments if they were able to be calculated.
            X is integral of "x dm" over the volume
            Y is integral of "y dm" over the volume
            Z is integral of "z dm" over the volume.

Get: WorldCoordinatesFirstMoments(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesFirstMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates first moments calculation.

Get: WorldCoordinatesFirstMomentsError(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesMomentsOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The moments of inertia about the world coordinate axes.
            X = integral of (y^2 + z^2) dm
            Y = integral of (z^2 + x^2) dm
            Z = integral of (z^2 + y^2) dm.

Get: WorldCoordinatesMomentsOfInertia(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesMomentsOfInertiaError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates moments of inertia calculation.

Get: WorldCoordinatesMomentsOfInertiaError(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesProductMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate product moments if they were able to be calculated.
            X is integral of "xy dm" over the area
            Y is integral of "yz dm" over the area
            Z is integral of "zx dm" over the area.

Get: WorldCoordinatesProductMoments(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesProductMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates second moments calculation.

Get: WorldCoordinatesProductMomentsError(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesRadiiOfGyration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Radii of gyration with respect to world coordinate system.
            X = sqrt(integral of (y^2 + z^2) dm/M)
            Y = sqrt(integral of (z^2 + x^2) dm/M)
            Z = sqrt(integral of (z^2 + y^2) dm/M)

Get: WorldCoordinatesRadiiOfGyration(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesSecondMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the world coordinate first moments if they were able to be calculated.
            X is integral of "xx dm" over the area
            Y is integral of "yy dm" over the area
            Z is integral of "zz dm" over the area.

Get: WorldCoordinatesSecondMoments(self: VolumeMassProperties) -> Vector3d

"""

    WorldCoordinatesSecondMomentsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncertainty in world coordinates second moments calculation.

Get: WorldCoordinatesSecondMomentsError(self: VolumeMassProperties) -> Vector3d

"""



# variables with complex values

