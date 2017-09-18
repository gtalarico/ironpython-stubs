# encoding: utf-8
# module Grasshopper.Kernel.Utility calls itself Utility
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_IntervalWrapperDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ GH_IntervalWrapperDelegate(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender, interval, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: GH_IntervalWrapperDelegate, sender: GH_Interval_Wrapper, interval: Interval, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
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
        """ EndInvoke(self: GH_IntervalWrapperDelegate, DelegateAsyncResult: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, interval):
        """ Invoke(self: GH_IntervalWrapperDelegate, sender: GH_Interval_Wrapper, interval: Interval) """
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


class GH_Interval_Wrapper(object):
    """ GH_Interval_Wrapper(interval: Interval, wrapperdelegate: GH_IntervalWrapperDelegate) -> Interval """
    def InternalInterval(self):
        """ InternalInterval(self: GH_Interval_Wrapper) -> Interval """
        pass

    @staticmethod # known case of __new__
    def __new__(self, interval, wrapperdelegate):
        """ __new__(cls: type, interval: Interval, wrapperdelegate: GH_IntervalWrapperDelegate) -> Interval """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: GH_Interval_Wrapper) -> float

Set: A(self: GH_Interval_Wrapper) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: GH_Interval_Wrapper) -> float

Set: B(self: GH_Interval_Wrapper) = value
"""

    Increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increasing(self: GH_Interval_Wrapper) -> str

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GH_Interval_Wrapper) -> str

"""



class GH_Interval_Wrapper_TypeConverter(ExpandableObjectConverter):
    """ GH_Interval_Wrapper_TypeConverter() """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: GH_Interval_Wrapper_TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def CanConvertTo(self, *__args):
        """ CanConvertTo(self: GH_Interval_Wrapper_TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: GH_Interval_Wrapper_TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass


class GH_PlaneModifier(object):
    # no doc
    @staticmethod
    def Set_X(P, x_axis):
        """ Set_X(P: Plane, x_axis: Vector3d) -> Plane """
        pass

    @staticmethod
    def Set_Y(P, y_axis):
        """ Set_Y(P: Plane, y_axis: Vector3d) -> Plane """
        pass

    @staticmethod
    def Set_Z(P, z_axis):
        """ Set_Z(P: Plane, z_axis: Vector3d) -> Plane """
        pass


class GH_Point3dWrapperDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ GH_Point3dWrapperDelegate(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender, point, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: GH_Point3dWrapperDelegate, sender: GH_Point3d_Wrapper, point: Point3d, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
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
        """ EndInvoke(self: GH_Point3dWrapperDelegate, DelegateAsyncResult: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, point):
        """ Invoke(self: GH_Point3dWrapperDelegate, sender: GH_Point3d_Wrapper, point: Point3d) """
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


class GH_Point3d_Wrapper(object):
    """ GH_Point3d_Wrapper(pt: Point3d, wrapperdelegate: GH_Point3dWrapperDelegate) -> Point3d """
    def InternalPoint(self):
        """ InternalPoint(self: GH_Point3d_Wrapper) -> Point3d """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pt, wrapperdelegate):
        """ __new__(cls: type, pt: Point3d, wrapperdelegate: GH_Point3dWrapperDelegate) -> Point3d """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: GH_Point3d_Wrapper) -> float

Set: X(self: GH_Point3d_Wrapper) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: GH_Point3d_Wrapper) -> float

Set: Y(self: GH_Point3d_Wrapper) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: GH_Point3d_Wrapper) -> float

Set: Z(self: GH_Point3d_Wrapper) = value
"""



class GH_Point3d_Wrapper_TypeConverter(ExpandableObjectConverter):
    """ GH_Point3d_Wrapper_TypeConverter() """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: GH_Point3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def CanConvertTo(self, *__args):
        """ CanConvertTo(self: GH_Point3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: GH_Point3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass


class GH_PointRefUVWrapperDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ GH_PointRefUVWrapperDelegate(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender, ref, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: GH_PointRefUVWrapperDelegate, sender: GH_PointRefUV_Wrapper, ref: GH_PointRefData, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
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
        """ EndInvoke(self: GH_PointRefUVWrapperDelegate, DelegateAsyncResult: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, ref):
        """ Invoke(self: GH_PointRefUVWrapperDelegate, sender: GH_PointRefUV_Wrapper, ref: GH_PointRefData) """
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


class GH_PointRefUV_Wrapper(object):
    """ GH_PointRefUV_Wrapper(ref: GH_PointRefData, wrapperdelegate: GH_PointRefUVWrapperDelegate) -> GH_PointRefData """
    def InternalRefence(self):
        """ InternalRefence(self: GH_PointRefUV_Wrapper) -> GH_PointRefData """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ref, wrapperdelegate):
        """ __new__(cls: type, ref: GH_PointRefData, wrapperdelegate: GH_PointRefUVWrapperDelegate) -> GH_PointRefData """
        pass

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U(self: GH_PointRefUV_Wrapper) -> float

Set: U(self: GH_PointRefUV_Wrapper) = value
"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V(self: GH_PointRefUV_Wrapper) -> float

Set: V(self: GH_PointRefUV_Wrapper) = value
"""



class GH_PointRefUV_Wrapper_TypeConverter(ExpandableObjectConverter):
    """ GH_PointRefUV_Wrapper_TypeConverter() """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: GH_PointRefUV_Wrapper_TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def CanConvertTo(self, *__args):
        """ CanConvertTo(self: GH_PointRefUV_Wrapper_TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: GH_PointRefUV_Wrapper_TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass


class GH_Vector3dWrapperDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ GH_Vector3dWrapperDelegate(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender, vector, DelegateCallback, DelegateAsyncState):
        """ BeginInvoke(self: GH_Vector3dWrapperDelegate, sender: GH_Vector3d_Wrapper, vector: Vector3d, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
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
        """ EndInvoke(self: GH_Vector3dWrapperDelegate, DelegateAsyncResult: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, vector):
        """ Invoke(self: GH_Vector3dWrapperDelegate, sender: GH_Vector3d_Wrapper, vector: Vector3d) """
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


class GH_Vector3d_Wrapper(object):
    """ GH_Vector3d_Wrapper(vec: Vector3d, wrapperdelegate: GH_Vector3dWrapperDelegate) -> Vector3d """
    def InternalVector(self):
        """ InternalVector(self: GH_Vector3d_Wrapper) -> Vector3d """
        pass

    @staticmethod # known case of __new__
    def __new__(self, vec, wrapperdelegate):
        """ __new__(cls: type, vec: Vector3d, wrapperdelegate: GH_Vector3dWrapperDelegate) -> Vector3d """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: GH_Vector3d_Wrapper) -> str

"""

    Tiny = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tiny(self: GH_Vector3d_Wrapper) -> str

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: GH_Vector3d_Wrapper) -> float

Set: X(self: GH_Vector3d_Wrapper) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: GH_Vector3d_Wrapper) -> float

Set: Y(self: GH_Vector3d_Wrapper) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: GH_Vector3d_Wrapper) -> float

Set: Z(self: GH_Vector3d_Wrapper) = value
"""



class GH_Vector3d_Wrapper_TypeConverter(ExpandableObjectConverter):
    """ GH_Vector3d_Wrapper_TypeConverter() """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: GH_Vector3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def CanConvertTo(self, *__args):
        """ CanConvertTo(self: GH_Vector3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: GH_Vector3d_Wrapper_TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass


