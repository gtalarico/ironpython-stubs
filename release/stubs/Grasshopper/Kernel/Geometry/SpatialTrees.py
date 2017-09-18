# encoding: utf-8
# module Grasshopper.Kernel.Geometry.SpatialTrees calls itself SpatialTrees
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Coordinates3d(MulticastDelegate, ICloneable, ISerializable):
    """ Coordinates3d[T](TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, element, x, y, z, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: Coordinates3d[T], element: T, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> (IAsyncResult, float, float, float) """
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

    def EndInvoke(self, x, y, z, DelegateAsyncResult):
        """ EndInvoke(self: Coordinates3d[T], DelegateAsyncResult: IAsyncResult) -> (float, float, float) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, element, x, y, z):
        """ Invoke(self: Coordinates3d[T], element: T) -> (float, float, float) """
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
    def __new__(self, TargetObject, TargetMethod):
        """ __new__(cls: type, TargetObject: object, TargetMethod: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Index3d(object, IComparable[Index3d[T]]):
    """ Index3d[T](node: Node3d[T], nodeIndex: int) """
    def CompareTo(self, other):
        """ CompareTo(self: Index3d[T], other: Index3d[T]) -> int """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, node, nodeIndex):
        """ __new__(cls: type, node: Node3d[T], nodeIndex: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GlobalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalIndex(self: Index3d[T]) -> int

"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: Index3d[T]) -> T

"""

    LocalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalIndex(self: Index3d[T]) -> int

"""

    Node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Node(self: Index3d[T]) -> Node3d[T]

"""



class Node3d(object):
    """
    Node3d[T](converter: Coordinates3d[T], region: BoundingBox)
    Node3d[T](converter: Coordinates3d[T], region: BoundingBox, limit: int)
    """
    def Add(self, item):
        """ Add(self: Node3d[T], item: T) """
        pass

    def AddRange(self, items):
        """ AddRange(self: Node3d[T], items: IEnumerable[T]) """
        pass

    def AddToRhinoDocument(self, doc):
        """ AddToRhinoDocument(self: Node3d[T], doc: RhinoDoc) """
        pass

    def ChildIndex(self, *args): #cannot find CLR method
        """ ChildIndex(self: Node3d[T], x: float, y: float, z: float) -> int """
        pass

    def ChildRegion(self, *args): #cannot find CLR method
        """ ChildRegion(self: Node3d[T], index: int) -> BoundingBox """
        pass

    def CollapseNodes(self):
        """ CollapseNodes(self: Node3d[T]) -> Node3d[T] """
        pass

    def FurthestItem(self, *__args):
        """
        FurthestItem(self: Node3d[T], locus: T, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        FurthestItem(self: Node3d[T], locus: Point3d, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        FurthestItem(self: Node3d[T], x: float, y: float, z: float, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        FurthestItem(self: Node3d[T], locus: T) -> Index3d[T]
        FurthestItem(self: Node3d[T], locus: Point3d) -> Index3d[T]
        FurthestItem(self: Node3d[T], x: float, y: float, z: float) -> Index3d[T]
        """
        pass

    def InsertIndexRecursive(self, *args): #cannot find CLR method
        """ InsertIndexRecursive(self: Node3d[T], index: int) """
        pass

    def NearestItem(self, *__args):
        """
        NearestItem(self: Node3d[T], locus: Point3d, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        NearestItem(self: Node3d[T], x: float, y: float, z: float, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        NearestItem(self: Node3d[T], x: float, y: float, z: float, validationDelegate: Validation3d[T]) -> Index3d[T]
        NearestItem(self: Node3d[T], locus: T, minimumDistance: float, maximumDistance: float) -> Index3d[T]
        NearestItem(self: Node3d[T], locus: T) -> Index3d[T]
        NearestItem(self: Node3d[T], locus: Point3d) -> Index3d[T]
        NearestItem(self: Node3d[T], x: float, y: float, z: float) -> Index3d[T]
        """
        pass

    def NearestItems(self, *__args):
        """
        NearestItems(self: Node3d[T], x: float, y: float, z: float, groupSize: int) -> List[Index3d[T]]
        NearestItems(self: Node3d[T], x: float, y: float, z: float, groupSize: int, minimumDistance: float, maximumDistance: float) -> List[Index3d[T]]
        NearestItems(self: Node3d[T], locus: T, groupSize: int) -> List[Index3d[T]]
        NearestItems(self: Node3d[T], locus: T, groupSize: int, minimumDistance: float, maximumDistance: float) -> List[Index3d[T]]
        """
        pass

    def OptimizeTree(self):
        """ OptimizeTree(self: Node3d[T]) -> Node3d[T] """
        pass

    def Rebuild(self, *args): #cannot find CLR method
        """ Rebuild(self: Node3d[T]) """
        pass

    def Remove(self, index):
        """ Remove(self: Node3d[T], index: Index3d[T])Remove(self: Node3d[T], index: int) """
        pass

    def RemoveIndexRecursive(self, *args): #cannot find CLR method
        """ RemoveIndexRecursive(self: Node3d[T], index: int) """
        pass

    def ShrinkRegions(self):
        """ ShrinkRegions(self: Node3d[T]) """
        pass

    def SubTree(self, omitStructuralNodes):
        """ SubTree(self: Node3d[T], omitStructuralNodes: bool) -> IEnumerator[Node3d[T]] """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: Node3d[T]) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, converter, region, limit=None):
        """
        __new__(cls: type, converter: Coordinates3d[T], region: BoundingBox)
        __new__(cls: type, converter: Coordinates3d[T], region: BoundingBox, limit: int)
        """
        pass

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Node3d[T]) -> Point3d

"""

    ChildCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChildCount(self: Node3d[T]) -> int

"""

    ContentAverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentAverage(self: Node3d[T]) -> Point3d

"""

    ContentBoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentBoundingBox(self: Node3d[T]) -> BoundingBox

"""

    IndicesLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndicesLocal(self: Node3d[T]) -> List[int]

"""

    IndicesRecursive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndicesRecursive(self: Node3d[T]) -> List[int]

"""

    IsLeaf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLeaf(self: Node3d[T]) -> bool

"""

    IsMutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMutable(self: Node3d[T]) -> bool

"""

    IsRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoot(self: Node3d[T]) -> bool

"""

    IsTwig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTwig(self: Node3d[T]) -> bool

"""

    ItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCount(self: Node3d[T]) -> int

"""

    ItemsGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsGlobal(self: Node3d[T]) -> List[T]

"""

    ItemsLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsLocal(self: Node3d[T]) -> List[T]

"""

    Limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limit(self: Node3d[T]) -> int

"""

    MemoryConsumption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemoryConsumption(self: Node3d[T]) -> Int64

"""

    NextNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextNode(self: Node3d[T]) -> Node3d[T]

"""

    NodeDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeDepth(self: Node3d[T]) -> int

"""

    ParentNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentNode(self: Node3d[T]) -> Node3d[T]

"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region(self: Node3d[T]) -> BoundingBox

"""

    RootNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootNode(self: Node3d[T]) -> Node3d[T]

"""

    WeightedSubdivision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeightedSubdivision(self: Node3d[T]) -> bool

Set: WeightedSubdivision(self: Node3d[T]) = value
"""



class TreeDelegates(object):
    # no doc
    @staticmethod
    def Node2Coordinates(pt, x, y, z):
        """ Node2Coordinates(pt: Node2, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def Node3Coordinates(pt, x, y, z):
        """ Node3Coordinates(pt: Node3, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def Point2dCoordinates(pt, x, y, z):
        """ Point2dCoordinates(pt: Point2d, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def Point2fCoordinates(pt, x, y, z):
        """ Point2fCoordinates(pt: Point2d, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def Point3dCoordinates(pt, x, y, z):
        """ Point3dCoordinates(pt: Point3d, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def Point3fCoordinates(pt, x, y, z):
        """ Point3fCoordinates(pt: Point3d, x: float, y: float, z: float) -> (float, float, float) """
        pass

    @staticmethod
    def PointCoordinates(pt, x, y, z):
        """ PointCoordinates(pt: Point, x: float, y: float, z: float) -> (float, float, float) """
        pass


class Validation3d(MulticastDelegate, ICloneable, ISerializable):
    """ Validation3d[T](TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, element, globalIndex, node, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: Validation3d[T], element: T, globalIndex: int, node: Node3d[T], DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
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

    def EndInvoke(self, DelegateAsyncResult):
        """ EndInvoke(self: Validation3d[T], DelegateAsyncResult: IAsyncResult) -> bool """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, element, globalIndex, node):
        """ Invoke(self: Validation3d[T], element: T, globalIndex: int, node: Node3d[T]) -> bool """
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
    def __new__(self, TargetObject, TargetMethod):
        """ __new__(cls: type, TargetObject: object, TargetMethod: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


