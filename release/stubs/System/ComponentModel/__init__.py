# encoding: utf-8
# module System.ComponentModel calls itself ComponentModel
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AddingNewEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.BindingSource.AddingNew event.
    
    AddingNewEventArgs()
    AddingNewEventArgs(newObject: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, newObject=None):
        """
        __new__(cls: type)
        __new__(cls: type, newObject: object)
        """
        pass

    NewObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object to be added to the binding list.

Get: NewObject(self: AddingNewEventArgs) -> object

Set: NewObject(self: AddingNewEventArgs) = value
"""



class AddingNewEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Forms.BindingSource.AddingNew event.
    
    AddingNewEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: AddingNewEventHandler, sender: object, e: AddingNewEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: AddingNewEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AddingNewEventHandler, sender: object, e: AddingNewEventArgs) """
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


class AmbientValueAttribute(Attribute, _Attribute):
    """
    Specifies the value to pass to a property to cause the property to get its value from another source. This is known as ambience. This class cannot be inherited.
    
    AmbientValueAttribute(type: Type, value: str)
    AmbientValueAttribute(value: Char)
    AmbientValueAttribute(value: Byte)
    AmbientValueAttribute(value: Int16)
    AmbientValueAttribute(value: int)
    AmbientValueAttribute(value: Int64)
    AmbientValueAttribute(value: Single)
    AmbientValueAttribute(value: float)
    AmbientValueAttribute(value: bool)
    AmbientValueAttribute(value: str)
    AmbientValueAttribute(value: object)
    """
    def Equals(self, obj):
        """
        Equals(self: AmbientValueAttribute, obj: object) -> bool
        
            Determines whether the specified System.ComponentModel.AmbientValueAttribute is equal to the 
             current System.ComponentModel.AmbientValueAttribute.
        
        
            obj: The System.ComponentModel.AmbientValueAttribute to compare with the current 
             System.ComponentModel.AmbientValueAttribute.
        
            Returns: true if the specified System.ComponentModel.AmbientValueAttribute is equal to the current 
             System.ComponentModel.AmbientValueAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: AmbientValueAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.AmbientValueAttribute.
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
        __new__(cls: type, type: Type, value: str)
        __new__(cls: type, value: Char)
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: Int16)
        __new__(cls: type, value: int)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: Single)
        __new__(cls: type, value: float)
        __new__(cls: type, value: bool)
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that is the value of this System.ComponentModel.AmbientValueAttribute.

Get: Value(self: AmbientValueAttribute) -> object

"""



class TypeConverter(object):
    """
    Provides a unified way of converting types of values to other types, as well as for accessing standard values and subproperties.
    
    TypeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of the given type to the type of this 
             converter, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        CanConvertFrom(self: TypeConverter, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of the given type to the type of this 
             converter.
        
        
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type, using the specified 
             context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        CanConvertTo(self: TypeConverter, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type.
        
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the type of this converter, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        ConvertFrom(self: TypeConverter, value: object) -> object
        
            Converts the given value to the type of this converter.
        
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertFromInvariantString(self, *__args):
        """
        ConvertFromInvariantString(self: TypeConverter, context: ITypeDescriptorContext, text: str) -> object
        
            Converts the given string to the type of this converter, using the invariant culture and the 
             specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            text: The System.String to convert.
            Returns: An System.Object that represents the converted text.
        ConvertFromInvariantString(self: TypeConverter, text: str) -> object
        
            Converts the given string to the type of this converter, using the invariant culture.
        
            text: The System.String to convert.
            Returns: An System.Object that represents the converted text.
        """
        pass

    def ConvertFromString(self, *__args):
        """
        ConvertFromString(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, text: str) -> object
        
            Converts the given text to an object, using the specified context and culture information.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo. If null is passed, the current culture is assumed.
            text: The System.String to convert.
            Returns: An System.Object that represents the converted text.
        ConvertFromString(self: TypeConverter, context: ITypeDescriptorContext, text: str) -> object
        
            Converts the given text to an object, using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            text: The System.String to convert.
            Returns: An System.Object that represents the converted text.
        ConvertFromString(self: TypeConverter, text: str) -> object
        
            Converts the specified text to an object.
        
            text: The text representation of the object to convert.
            Returns: An System.Object that represents the converted text.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo. If null is passed, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        ConvertTo(self: TypeConverter, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type, using the arguments.
        
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertToInvariantString(self, *__args):
        """
        ConvertToInvariantString(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> str
        
            Converts the specified value to a culture-invariant string representation, using the specified 
             context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: The System.Object to convert.
            Returns: A System.String that represents the converted value.
        ConvertToInvariantString(self: TypeConverter, value: object) -> str
        
            Converts the specified value to a culture-invariant string representation.
        
            value: The System.Object to convert.
            Returns: A System.String that represents the converted value.
        """
        pass

    def ConvertToString(self, *__args):
        """
        ConvertToString(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> str
        
            Converts the given value to a string representation, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo. If null is passed, the current culture is assumed.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        ConvertToString(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> str
        
            Converts the given value to a string representation, using the given context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        ConvertToString(self: TypeConverter, value: object) -> str
        
            Converts the specified value to a string representation.
        
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: TypeConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an instance of the type that this System.ComponentModel.TypeConverter is associated 
             with, using the specified context, given a set of property values for the object.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            propertyValues: An System.Collections.IDictionary of new property values.
            Returns: An System.Object representing the given System.Collections.IDictionary, or null if the object 
             cannot be created. This method always returns null.
        
        CreateInstance(self: TypeConverter, propertyValues: IDictionary) -> object
        
            Re-creates an System.Object given a set of property values for the object.
        
            propertyValues: An System.Collections.IDictionary that represents a dictionary of new property values.
            Returns: An System.Object representing the given System.Collections.IDictionary, or null if the object 
             cannot be created. This method always returns null.
        """
        pass

    def GetConvertFromException(self, *args): #cannot find CLR method
        """
        GetConvertFromException(self: TypeConverter, value: object) -> Exception
        
            Returns an exception to throw when a conversion cannot be performed.
        
            value: The System.Object to convert, or null if the object is not available.
            Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
        """
        pass

    def GetConvertToException(self, *args): #cannot find CLR method
        """
        GetConvertToException(self: TypeConverter, value: object, destinationType: Type) -> Exception
        
            Returns an exception to throw when a conversion cannot be performed.
        
            value: The System.Object to convert, or null if the object is not available.
            destinationType: A System.Type that represents the type the conversion was trying to convert to.
            Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether changing a value on this object requires a call to 
             System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 
             new value, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if changing a property on this object requires a call to 
             System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 
             new value; otherwise, false.
        
        GetCreateInstanceSupported(self: TypeConverter) -> bool
        
            Returns whether changing a value on this object requires a call to the 
             System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) method to 
             create a new value.
        
            Returns: true if changing a property on this object requires a call to 
             System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 
             new value; otherwise, false.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: TypeConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a collection of properties for the type of array specified by the value parameter, using 
             the specified context and attributes.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of array for which to get properties.
            attributes: An array of type System.Attribute that is used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties.
        
        GetProperties(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> PropertyDescriptorCollection
        
            Returns a collection of properties for the type of array specified by the value parameter, using 
             the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of array for which to get properties.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties.
        
        GetProperties(self: TypeConverter, value: object) -> PropertyDescriptorCollection
        
            Returns a collection of properties for the type of array specified by the value parameter.
        
            value: An System.Object that specifies the type of array for which to get properties.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether this object supports properties, using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 
             find the properties of this object; otherwise, false.
        
        GetPropertiesSupported(self: TypeConverter) -> bool
        
            Returns whether this object supports properties.
            Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 
             find the properties of this object; otherwise, false.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: TypeConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Returns a collection of standard values for the data type this type converter is designed for 
             when provided with a format context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context that can be used 
             to extract additional information about the environment from which this converter is invoked. 
             This parameter or properties of this parameter can be null.
        
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        
        GetStandardValues(self: TypeConverter) -> ICollection
        
            Returns a collection of standard values from the default context for the data type this type 
             converter is designed for.
        
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection containing a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether the collection of standard values returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list of possible values, 
             using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 
             false if other values are possible.
        
        GetStandardValuesExclusive(self: TypeConverter) -> bool
        
            Returns whether the collection of standard values returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list.
        
            Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 
             false if other values are possible.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether this object supports a standard set of values that can be picked from a list, 
             using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 
             set of values the object supports; otherwise, false.
        
        GetStandardValuesSupported(self: TypeConverter) -> bool
        
            Returns whether this object supports a standard set of values that can be picked from a list.
            Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 
             set of values the object supports; otherwise, false.
        """
        pass

    def IsValid(self, *__args):
        """
        IsValid(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> bool
        
            Returns whether the given value object is valid for this type and for the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: The System.Object to test for validity.
            Returns: true if the specified value is valid for this object; otherwise, false.
        IsValid(self: TypeConverter, value: object) -> bool
        
            Returns whether the given value object is valid for this type.
        
            value: The object to test for validity.
            Returns: true if the specified value is valid for this object; otherwise, false.
        """
        pass

    def SortProperties(self, *args): #cannot find CLR method
        """
        SortProperties(self: TypeConverter, props: PropertyDescriptorCollection, names: Array[str]) -> PropertyDescriptorCollection
        
            Sorts a collection of properties.
        
            props: A System.ComponentModel.PropertyDescriptorCollection that has the properties to sort.
            names: An array of names in the order you want the properties to appear in the collection.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the sorted properties.
        """
        pass

    SimplePropertyDescriptor = None
    StandardValuesCollection = None


class CollectionConverter(TypeConverter):
    """
    Provides a type converter to convert collection objects to and from various other representations.
    
    CollectionConverter()
    """
    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The culture to which value will be converted.
            value: The System.Object to convert. This parameter must inherit from System.Collections.ICollection.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: CollectionConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets a collection of properties for the type of array specified by the value parameter using the 
             specified context and attributes.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of array to get the properties for.
            attributes: An array of type System.Attribute that will be used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties. This method always returns null.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: CollectionConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports properties.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: false because 
             System.ComponentModel.CollectionConverter.GetProperties(System.ComponentModel.ITypeDescriptorCont
             ext,System.Object,System.Attribute[]) should not be called to find the properties of this 
             object. This method never returns true.
        """
        pass


class ArrayConverter(CollectionConverter):
    """
    Provides a type converter to convert System.Array objects to and from various other representations.
    
    ArrayConverter()
    """
    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ArrayConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The culture into which value will be converted.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: ArrayConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets a collection of properties for the type of array specified by the value parameter.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of array to get the properties for.
            attributes: An array of type System.Attribute that will be used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for an 
             array, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: ArrayConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports properties.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because 
             System.ComponentModel.ArrayConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,S
             ystem.Object,System.Attribute[]) should be called to find the properties of this object. This 
             method never returns false.
        """
        pass


class AsyncCompletedEventArgs(EventArgs):
    """
    Provides data for the MethodNameCompleted event.
    
    AsyncCompletedEventArgs()
    AsyncCompletedEventArgs(error: Exception, cancelled: bool, userState: object)
    """
    def RaiseExceptionIfNecessary(self, *args): #cannot find CLR method
        """
        RaiseExceptionIfNecessary(self: AsyncCompletedEventArgs)
            Raises a user-supplied exception if an asynchronous operation failed.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, error=None, cancelled=None, userState=None):
        """
        __new__(cls: type)
        __new__(cls: type, error: Exception, cancelled: bool, userState: object)
        """
        pass

    Cancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an asynchronous operation has been canceled.

Get: Cancelled(self: AsyncCompletedEventArgs) -> bool

"""

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating which error occurred during an asynchronous operation.

Get: Error(self: AsyncCompletedEventArgs) -> Exception

"""

    UserState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier for the asynchronous task.

Get: UserState(self: AsyncCompletedEventArgs) -> object

"""



class AsyncCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the MethodNameCompleted event of an asynchronous operation.
    
    AsyncCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: AsyncCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: AsyncCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AsyncCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs) """
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


class AsyncOperation(object):
    """ Tracks the lifetime of an asynchronous operation. """
    def OperationCompleted(self):
        """
        OperationCompleted(self: AsyncOperation)
            Ends the lifetime of an asynchronous operation.
        """
        pass

    def Post(self, d, arg):
        """
        Post(self: AsyncOperation, d: SendOrPostCallback, arg: object)
            Invokes a delegate on the thread or context appropriate for the application model.
        
            d: A System.Threading.SendOrPostCallback object that wraps the delegate to be called when the 
             operation ends.
        
            arg: An argument for the delegate contained in the d parameter.
        """
        pass

    def PostOperationCompleted(self, d, arg):
        """
        PostOperationCompleted(self: AsyncOperation, d: SendOrPostCallback, arg: object)
            Ends the lifetime of an asynchronous operation.
        
            d: A System.Threading.SendOrPostCallback object that wraps the delegate to be called when the 
             operation ends.
        
            arg: An argument for the delegate contained in the d parameter.
        """
        pass

    SynchronizationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Threading.SynchronizationContext object that was passed to the constructor.

Get: SynchronizationContext(self: AsyncOperation) -> SynchronizationContext

"""

    UserSuppliedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object used to uniquely identify an asynchronous operation.

Get: UserSuppliedState(self: AsyncOperation) -> object

"""



class AsyncOperationManager(object):
    """ Provides concurrency management for classes that support asynchronous method calls. This class cannot be inherited. """
    @staticmethod
    def CreateOperation(userSuppliedState):
        """
        CreateOperation(userSuppliedState: object) -> AsyncOperation
        
            Returns an System.ComponentModel.AsyncOperation for tracking the duration of a particular 
             asynchronous operation.
        
        
            userSuppliedState: An object used to associate a piece of client state, such as a task ID, with a particular 
             asynchronous operation.
        
            Returns: An System.ComponentModel.AsyncOperation that you can use to track the duration of an 
             asynchronous method invocation.
        """
        pass

    SynchronizationContext = None
    __all__ = [
        'CreateOperation',
    ]


class AttributeCollection(object, ICollection, IEnumerable):
    """
    Represents a collection of attributes.
    
    AttributeCollection(*attributes: Array[Attribute])
    """
    def Contains(self, *__args):
        """
        Contains(self: AttributeCollection, attributes: Array[Attribute]) -> bool
        
            Determines whether this attribute collection contains all the specified attributes in the 
             attribute array.
        
        
            attributes: An array of type System.Attribute to find in the collection.
            Returns: true if the collection contains all the attributes; otherwise, false.
        Contains(self: AttributeCollection, attribute: Attribute) -> bool
        
            Determines whether this collection of attributes has the specified attribute.
        
            attribute: An System.Attribute to find in the collection.
            Returns: true if the collection contains the attribute or is the default attribute for the type of 
             attribute; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: AttributeCollection, array: Array, index: int)
            Copies the collection to an array, starting at the specified index.
        
            array: The System.Array to copy the collection to.
            index: The index to start from.
        """
        pass

    @staticmethod
    def FromExisting(existing, newAttributes):
        """
        FromExisting(existing: AttributeCollection, *newAttributes: Array[Attribute]) -> AttributeCollection
        
            Creates a new System.ComponentModel.AttributeCollection from an existing 
             System.ComponentModel.AttributeCollection.
        
        
            existing: An System.ComponentModel.AttributeCollection from which to create the copy.
            newAttributes: An array of type System.Attribute that provides the attributes for this collection. Can be null.
            Returns: A new System.ComponentModel.AttributeCollection that is a copy of existing.
        """
        pass

    def GetDefaultAttribute(self, *args): #cannot find CLR method
        """
        GetDefaultAttribute(self: AttributeCollection, attributeType: Type) -> Attribute
        
            Returns the default System.Attribute of a given System.Type.
        
            attributeType: The System.Type of the attribute to retrieve.
            Returns: An System.Attribute.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: AttributeCollection) -> IEnumerator
        
            Gets an enumerator for this collection.
            Returns: An enumerator of type System.Collections.IEnumerator.
        """
        pass

    def Matches(self, *__args):
        """
        Matches(self: AttributeCollection, attributes: Array[Attribute]) -> bool
        
            Determines whether the attributes in the specified array are the same as the attributes in the 
             collection.
        
        
            attributes: An array of System.CodeDom.MemberAttributes to compare with the attributes in this collection.
            Returns: true if all the attributes in the array are contained in the collection and have the same values 
             as the attributes in the collection; otherwise, false.
        
        Matches(self: AttributeCollection, attribute: Attribute) -> bool
        
            Determines whether a specified attribute is the same as an attribute in the collection.
        
            attribute: An instance of System.Attribute to compare with the attributes in this collection.
            Returns: true if the attribute is contained within the collection and has the same value as the attribute 
             in the collection; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, attributes):
        """
        __new__(cls: type, *attributes: Array[Attribute])
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attribute collection.

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of attributes.

Get: Count(self: AttributeCollection) -> int

"""


    Empty = None


class AttributeProviderAttribute(Attribute, _Attribute):
    """
    Enables attribute redirection. This class cannot be inherited.
    
    AttributeProviderAttribute(typeName: str)
    AttributeProviderAttribute(typeName: str, propertyName: str)
    AttributeProviderAttribute(type: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, typeName: str)
        __new__(cls: type, typeName: str, propertyName: str)
        __new__(cls: type, type: Type)
        """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property for which attributes will be retrieved.

Get: PropertyName(self: AttributeProviderAttribute) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the assembly qualified type name passed into the constructor.

Get: TypeName(self: AttributeProviderAttribute) -> str

"""



class Component(MarshalByRefObject, IComponent, IDisposable):
    """
    Provides the base implementation for the System.ComponentModel.IComponent interface and enables object sharing between applications.
    
    Component()
    """
    def Dispose(self):
        """
        Dispose(self: Component)
            Releases all resources used by the System.ComponentModel.Component.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ToString(self):
        """
        ToString(self: Component) -> str
        
            Returns a System.String containing the name of the System.ComponentModel.Component, if any. This 
             method should not be overridden.
        
            Returns: A System.String containing the name of the System.ComponentModel.Component, if any, or null if 
             the System.ComponentModel.Component is unnamed.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    Container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.IContainer that contains the System.ComponentModel.Component.

Get: Container(self: Component) -> IContainer

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.ComponentModel.ISite of the System.ComponentModel.Component.

Get: Site(self: Component) -> ISite

Set: Site(self: Component) = value
"""


    Disposed = None


class BackgroundWorker(Component, IComponent, IDisposable):
    """
    Executes an operation on a separate thread.
    
    BackgroundWorker()
    """
    def CancelAsync(self):
        """
        CancelAsync(self: BackgroundWorker)
            Requests cancellation of a pending background operation.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnDoWork(self, *args): #cannot find CLR method
        """
        OnDoWork(self: BackgroundWorker, e: DoWorkEventArgs)
            Raises the System.ComponentModel.BackgroundWorker.DoWork event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnProgressChanged(self, *args): #cannot find CLR method
        """
        OnProgressChanged(self: BackgroundWorker, e: ProgressChangedEventArgs)
            Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRunWorkerCompleted(self, *args): #cannot find CLR method
        """
        OnRunWorkerCompleted(self: BackgroundWorker, e: RunWorkerCompletedEventArgs)
            Raises the System.ComponentModel.BackgroundWorker.RunWorkerCompleted event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def ReportProgress(self, percentProgress, userState=None):
        """
        ReportProgress(self: BackgroundWorker, percentProgress: int, userState: object)
            Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.
        
            percentProgress: The percentage, from 0 to 100, of the background operation that is complete.
            userState: The state object passed to System.ComponentModel.BackgroundWorker.RunWorkerAsync(System.Object).
        ReportProgress(self: BackgroundWorker, percentProgress: int)
            Raises the System.ComponentModel.BackgroundWorker.ProgressChanged event.
        
            percentProgress: The percentage, from 0 to 100, of the background operation that is complete.
        """
        pass

    def RunWorkerAsync(self, argument=None):
        """
        RunWorkerAsync(self: BackgroundWorker, argument: object)
            Starts execution of a background operation.
        
            argument: A parameter for use by the background operation to be executed in the 
             System.ComponentModel.BackgroundWorker.DoWork event handler.
        
        RunWorkerAsync(self: BackgroundWorker)
            Starts execution of a background operation.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CancellationPending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the application has requested cancellation of a background operation.

Get: CancellationPending(self: BackgroundWorker) -> bool

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.ComponentModel.BackgroundWorker is running an asynchronous operation.

Get: IsBusy(self: BackgroundWorker) -> bool

"""

    WorkerReportsProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.ComponentModel.BackgroundWorker can report progress updates.

Get: WorkerReportsProgress(self: BackgroundWorker) -> bool

Set: WorkerReportsProgress(self: BackgroundWorker) = value
"""

    WorkerSupportsCancellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.ComponentModel.BackgroundWorker supports asynchronous cancellation.

Get: WorkerSupportsCancellation(self: BackgroundWorker) -> bool

Set: WorkerSupportsCancellation(self: BackgroundWorker) = value
"""


    DoWork = None
    ProgressChanged = None
    RunWorkerCompleted = None


class BaseNumberConverter(TypeConverter):
    """ Provides a base type converter for nonfloating-point numerical types. """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: BaseNumberConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines if this converter can convert an object in the given source type to the native type 
             of the converter.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type from which you want to convert.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: BaseNumberConverter, context: ITypeDescriptorContext, t: Type) -> bool
        
            Returns a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            t: A System.Type that represents the type to which you want to convert.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: BaseNumberConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the converter's native type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture to represent the number.
            value: The object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: BaseNumberConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to another type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture to represent the number.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: An System.Object that represents the converted value.
        """
        pass


class BindableAttribute(Attribute, _Attribute):
    """
    Specifies whether a member is typically used for binding. This class cannot be inherited.
    
    BindableAttribute(bindable: bool)
    BindableAttribute(bindable: bool, direction: BindingDirection)
    BindableAttribute(flags: BindableSupport)
    BindableAttribute(flags: BindableSupport, direction: BindingDirection)
    """
    def Equals(self, obj):
        """
        Equals(self: BindableAttribute, obj: object) -> bool
        
            Determines whether two System.ComponentModel.BindableAttribute objects are equal.
        
            obj: The object to compare.
            Returns: true if the specified System.ComponentModel.BindableAttribute is equal to the current 
             System.ComponentModel.BindableAttribute; false if it is not equal.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: BindableAttribute) -> int
        
            Serves as a hash function for the System.ComponentModel.BindableAttribute class.
            Returns: A hash code for the current System.ComponentModel.BindableAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: BindableAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
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
        __new__(cls: type, bindable: bool)
        __new__(cls: type, bindable: bool, direction: BindingDirection)
        __new__(cls: type, flags: BindableSupport)
        __new__(cls: type, flags: BindableSupport, direction: BindingDirection)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Bindable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating that a property is typically used for binding.

Get: Bindable(self: BindableAttribute) -> bool

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the direction or directions of this property's data binding.

Get: Direction(self: BindableAttribute) -> BindingDirection

"""


    Default = None
    No = None
    Yes = None


class BindableSupport(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies values to indicate whether a property can be bound to a data element or another property.
    
    enum BindableSupport, values: Default (2), No (0), Yes (1)
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

    Default = None
    No = None
    value__ = None
    Yes = None


class BindingDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether the template can be bound one way or two ways.
    
    enum BindingDirection, values: OneWay (0), TwoWay (1)
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

    OneWay = None
    TwoWay = None
    value__ = None


class IBindingList(IList, ICollection, IEnumerable):
    """ Provides the features required to support both complex and simple scenarios when binding to a data source. """
    def AddIndex(self, property):
        """
        AddIndex(self: IBindingList, property: PropertyDescriptor)
            Adds the System.ComponentModel.PropertyDescriptor to the indexes used for searching.
        
            property: The System.ComponentModel.PropertyDescriptor to add to the indexes used for searching.
        """
        pass

    def AddNew(self):
        """
        AddNew(self: IBindingList) -> object
        
            Adds a new item to the list.
            Returns: The item added to the list.
        """
        pass

    def ApplySort(self, property, direction):
        """
        ApplySort(self: IBindingList, property: PropertyDescriptor, direction: ListSortDirection)
            Sorts the list based on a System.ComponentModel.PropertyDescriptor and a 
             System.ComponentModel.ListSortDirection.
        
        
            property: The System.ComponentModel.PropertyDescriptor to sort by.
            direction: One of the System.ComponentModel.ListSortDirection values.
        """
        pass

    def Find(self, property, key):
        """
        Find(self: IBindingList, property: PropertyDescriptor, key: object) -> int
        
            Returns the index of the row that has the given System.ComponentModel.PropertyDescriptor.
        
            property: The System.ComponentModel.PropertyDescriptor to search on.
            key: The value of the property parameter to search for.
            Returns: The index of the row that has the given System.ComponentModel.PropertyDescriptor.
        """
        pass

    def RemoveIndex(self, property):
        """
        RemoveIndex(self: IBindingList, property: PropertyDescriptor)
            Removes the System.ComponentModel.PropertyDescriptor from the indexes used for searching.
        
            property: The System.ComponentModel.PropertyDescriptor to remove from the indexes used for searching.
        """
        pass

    def RemoveSort(self):
        """
        RemoveSort(self: IBindingList)
            Removes any sort applied using 
             System.ComponentModel.IBindingList.ApplySort(System.ComponentModel.PropertyDescriptor,System.Comp
             onentModel.ListSortDirection).
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    AllowEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether you can update items in the list.

Get: AllowEdit(self: IBindingList) -> bool

"""

    AllowNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether you can add items to the list using System.ComponentModel.IBindingList.AddNew.

Get: AllowNew(self: IBindingList) -> bool

"""

    AllowRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether you can remove items from the list, using System.Collections.IList.Remove(System.Object) or System.Collections.IList.RemoveAt(System.Int32).

Get: AllowRemove(self: IBindingList) -> bool

"""

    IsSorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the items in the list are sorted.

Get: IsSorted(self: IBindingList) -> bool

"""

    SortDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction of the sort.

Get: SortDirection(self: IBindingList) -> ListSortDirection

"""

    SortProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.PropertyDescriptor that is being used for sorting.

Get: SortProperty(self: IBindingList) -> PropertyDescriptor

"""

    SupportsChangeNotification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether a System.ComponentModel.IBindingList.ListChanged event is raised when the list changes or an item in the list changes.

Get: SupportsChangeNotification(self: IBindingList) -> bool

"""

    SupportsSearching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the list supports searching using the System.ComponentModel.IBindingList.Find(System.ComponentModel.PropertyDescriptor,System.Object) method.

Get: SupportsSearching(self: IBindingList) -> bool

"""

    SupportsSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the list supports sorting.

Get: SupportsSorting(self: IBindingList) -> bool

"""


    ListChanged = None


class ICancelAddNew:
    """ Adds transactional capability when adding a new item to a collection. """
    def CancelNew(self, itemIndex):
        """
        CancelNew(self: ICancelAddNew, itemIndex: int)
            Discards a pending new item from the collection.
        
            itemIndex: The index of the item that was previously added to the collection.
        """
        pass

    def EndNew(self, itemIndex):
        """
        EndNew(self: ICancelAddNew, itemIndex: int)
            Commits a pending new item to the collection.
        
            itemIndex: The index of the item that was previously added to the collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IRaiseItemChangedEvents:
    """ Indicates whether a class converts property change events to System.ComponentModel.IBindingList.ListChanged events. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    RaisesItemChangedEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.ComponentModel.IRaiseItemChangedEvents object raises System.ComponentModel.IBindingList.ListChanged events.

Get: RaisesItemChangedEvents(self: IRaiseItemChangedEvents) -> bool

"""



class BindingList(Collection[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T], IBindingList, ICancelAddNew, IRaiseItemChangedEvents):
    """
    BindingList[T]()
    BindingList[T](list: IList[T])
    """
    def AddNew(self):
        """
        AddNew(self: BindingList[T]) -> T
        
            Adds a new item to the collection.
            Returns: The item added to the list.
        """
        pass

    def AddNewCore(self, *args): #cannot find CLR method
        """
        AddNewCore(self: BindingList[T]) -> object
        
            Adds a new item to the end of the collection.
            Returns: The item that was added to the collection.
        """
        pass

    def ApplySortCore(self, *args): #cannot find CLR method
        """
        ApplySortCore(self: BindingList[T], prop: PropertyDescriptor, direction: ListSortDirection)
            Sorts the items if overridden in a derived class; otherwise, throws a 
             System.NotSupportedException.
        
        
            prop: A System.ComponentModel.PropertyDescriptor that specifies the property to sort on.
            direction: One of the System.ComponentModel.ListSortDirection  values.
        """
        pass

    def CancelNew(self, itemIndex):
        """
        CancelNew(self: BindingList[T], itemIndex: int)
            Discards a pending new item.
        
            itemIndex: The index of the of the new item to be added
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: BindingList[T])
            Removes all elements from the collection.
        """
        pass

    def EndNew(self, itemIndex):
        """
        EndNew(self: BindingList[T], itemIndex: int)
            Commits a pending new item to the collection.
        
            itemIndex: The index of the new item to be added.
        """
        pass

    def FindCore(self, *args): #cannot find CLR method
        """
        FindCore(self: BindingList[T], prop: PropertyDescriptor, key: object) -> int
        
            Searches for the index of the item that has the specified property descriptor with the specified 
             value, if searching is implemented in a derived class; otherwise, a 
             System.NotSupportedException.
        
        
            prop: The System.ComponentModel.PropertyDescriptor to search for.
            key: The value of property to match.
            Returns: The zero-based index of the item that matches the property descriptor and contains the specified 
             value.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: BindingList[T], index: int, item: T)
            Inserts the specified item in the list at the specified index.
        
            index: The zero-based index where the item is to be inserted.
            item: The item to insert in the list.
        """
        pass

    def OnAddingNew(self, *args): #cannot find CLR method
        """
        OnAddingNew(self: BindingList[T], e: AddingNewEventArgs)
            Raises the System.ComponentModel.BindingList event.
        
            e: An System.ComponentModel.AddingNewEventArgs that contains the event data.
        """
        pass

    def OnListChanged(self, *args): #cannot find CLR method
        """
        OnListChanged(self: BindingList[T], e: ListChangedEventArgs)
            Raises the System.ComponentModel.BindingList event.
        
            e: A System.ComponentModel.ListChangedEventArgs that contains the event data.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: BindingList[T], index: int)
            Removes the item at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def RemoveSortCore(self, *args): #cannot find CLR method
        """
        RemoveSortCore(self: BindingList[T])
            Removes any sort applied with System.ComponentModel.BindingList if sorting is implemented in a 
             derived class; otherwise, raises System.NotSupportedException.
        """
        pass

    def ResetBindings(self):
        """
        ResetBindings(self: BindingList[T])
            Raises a System.ComponentModel.BindingList event of type 
             System.ComponentModel.ListChangedType.Reset.
        """
        pass

    def ResetItem(self, position):
        """
        ResetItem(self: BindingList[T], position: int)
            Raises a System.ComponentModel.BindingList event of type 
             System.ComponentModel.ListChangedType.ItemChanged for the item at the specified position.
        
        
            position: A zero-based index of the item to be reset.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: BindingList[T], index: int, item: T)
            Replaces the item at the specified index with the specified item.
        
            index: The zero-based index of the item to replace.
            item: The new value for the item at the specified index. The value can be null for reference types.
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
    def __new__(self, list=None):
        """
        __new__(cls: type)
        __new__(cls: type, list: IList[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    AllowEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether items in the list can be edited.

Get: AllowEdit(self: BindingList[T]) -> bool

Set: AllowEdit(self: BindingList[T]) = value
"""

    AllowNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether you can add items to the list using the System.ComponentModel.BindingList method.

Get: AllowNew(self: BindingList[T]) -> bool

Set: AllowNew(self: BindingList[T]) = value
"""

    AllowRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether you can remove items from the collection.

Get: AllowRemove(self: BindingList[T]) -> bool

Set: AllowRemove(self: BindingList[T]) = value
"""

    IsSortedCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the list is sorted.

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""

    RaiseListChangedEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether adding or removing items within the list raises System.ComponentModel.BindingList events.

Get: RaiseListChangedEvents(self: BindingList[T]) -> bool

Set: RaiseListChangedEvents(self: BindingList[T]) = value
"""

    SortDirectionCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction the list is sorted.

"""

    SortPropertyCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property descriptor that is used for sorting the list if sorting is implemented in a derived class; otherwise, returns null.

"""

    SupportsChangeNotificationCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether System.ComponentModel.BindingList events are enabled.

"""

    SupportsSearchingCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the list supports searching.

"""

    SupportsSortingCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the list supports sorting.

"""


    AddingNew = None
    ListChanged = None


class BooleanConverter(TypeConverter):
    """
    Provides a type converter to convert System.Boolean objects to and from various other representations.
    
    BooleanConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: BooleanConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a Boolean object using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this object can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: BooleanConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given value object to a Boolean object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: BooleanConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard values for the Boolean data type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: BooleanConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether the list of standard values returned from the 
             System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon
             text) method is an exclusive list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon
             text) is an exhaustive list of possible values. This method never returns false.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: BooleanConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports a standard set of values that can be picked 
             from a list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because 
             System.ComponentModel.BooleanConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCon
             text) can be called to find a common set of values the object supports. This method never 
             returns false.
        """
        pass


class BrowsableAttribute(Attribute, _Attribute):
    """
    Specifies whether a property or event should be displayed in a Properties window.
    
    BrowsableAttribute(browsable: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: BrowsableAttribute, obj: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            obj: Another object to compare to.
            Returns: true if obj is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: BrowsableAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: BrowsableAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, browsable):
        """ __new__(cls: type, browsable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Browsable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an object is browsable.

Get: Browsable(self: BrowsableAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class ByteConverter(BaseNumberConverter):
    """
    Provides a type converter to convert 8-bit unsigned integer objects to and from various other representations.
    
    ByteConverter()
    """

class CancelEventArgs(EventArgs):
    """
    Provides data for a cancelable event.
    
    CancelEventArgs()
    CancelEventArgs(cancel: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, cancel=None):
        """
        __new__(cls: type)
        __new__(cls: type, cancel: bool)
        """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the event should be canceled.

Get: Cancel(self: CancelEventArgs) -> bool

Set: Cancel(self: CancelEventArgs) = value
"""



class CancelEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles a cancelable event.
    
    CancelEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: CancelEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: CancelEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CancelEventHandler, sender: object, e: CancelEventArgs) """
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


class CategoryAttribute(Attribute, _Attribute):
    """
    Specifies the name of the category in which to group the property or event when displayed in a System.Windows.Forms.PropertyGrid control set to Categorized mode.
    
    CategoryAttribute()
    CategoryAttribute(category: str)
    """
    def Equals(self, obj):
        """
        Equals(self: CategoryAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.CategoryAttribute..
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CategoryAttribute) -> int
        
            Returns the hash code for this attribute.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def GetLocalizedString(self, *args): #cannot find CLR method
        """
        GetLocalizedString(self: CategoryAttribute, value: str) -> str
        
            Looks up the localized name of the specified category.
        
            value: The identifer for the category to look up.
            Returns: The localized name of the category, or null if a localized name does not exist.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: CategoryAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, category=None):
        """
        __new__(cls: type)
        __new__(cls: type, category: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the category for the property or event that this attribute is applied to.

Get: Category(self: CategoryAttribute) -> str

"""


    Action = None
    Appearance = None
    Asynchronous = None
    Behavior = None
    Data = None
    Default = None
    Design = None
    DragDrop = None
    Focus = None
    Format = None
    Key = None
    Layout = None
    Mouse = None
    WindowStyle = None


class CharConverter(TypeConverter):
    """
    Provides a type converter to convert Unicode character objects to and from various other representations.
    
    CharConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CharConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a Unicode character object using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CharConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to a Unicode character object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The culture into which value will be converted.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CharConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to a Unicode character object using the arguments.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The culture into which value will be converted.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass


class CollectionChangeAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the collection is changed.
    
    enum CollectionChangeAction, values: Add (1), Refresh (3), Remove (2)
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

    Add = None
    Refresh = None
    Remove = None
    value__ = None


class CollectionChangeEventArgs(EventArgs):
    """
    Provides data for the System.Data.DataColumnCollection.CollectionChanged event.
    
    CollectionChangeEventArgs(action: CollectionChangeAction, element: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, action, element):
        """ __new__(cls: type, action: CollectionChangeAction, element: object) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an action that specifies how the collection changed.

Get: Action(self: CollectionChangeEventArgs) -> CollectionChangeAction

"""

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the instance of the collection with the change.

Get: Element(self: CollectionChangeEventArgs) -> object

"""



class CollectionChangeEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Data.DataColumnCollection.CollectionChanged event raised when adding elements to or removing elements from a collection.
    
    CollectionChangeEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: CollectionChangeEventHandler, sender: object, e: CollectionChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: CollectionChangeEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CollectionChangeEventHandler, sender: object, e: CollectionChangeEventArgs) """
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


class ComplexBindingPropertiesAttribute(Attribute, _Attribute):
    """
    Specifies the data source and data member properties for a component that supports complex data binding. This class cannot be inherited.
    
    ComplexBindingPropertiesAttribute()
    ComplexBindingPropertiesAttribute(dataSource: str)
    ComplexBindingPropertiesAttribute(dataSource: str, dataMember: str)
    """
    def Equals(self, obj):
        """
        Equals(self: ComplexBindingPropertiesAttribute, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.ComponentModel.ComplexBindingPropertiesAttribute instance.
        
        
            obj: The System.Object to compare with the current 
             System.ComponentModel.ComplexBindingPropertiesAttribute instance
        
            Returns: true if the object is equal to the current instance; otherwise, false, indicating they are not 
             equal.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ComplexBindingPropertiesAttribute) -> int
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dataSource=None, dataMember=None):
        """
        __new__(cls: type)
        __new__(cls: type, dataSource: str)
        __new__(cls: type, dataSource: str, dataMember: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DataMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the data member property for the component to which the System.ComponentModel.ComplexBindingPropertiesAttribute is bound.

Get: DataMember(self: ComplexBindingPropertiesAttribute) -> str

"""

    DataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the data source property for the component to which the System.ComponentModel.ComplexBindingPropertiesAttribute is bound.

Get: DataSource(self: ComplexBindingPropertiesAttribute) -> str

"""


    Default = None


class ComponentCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    Provides a read-only container for a collection of System.ComponentModel.IComponent objects.
    
    ComponentCollection(components: Array[IComponent])
    """
    def CopyTo(self, array, index):
        """
        CopyTo(self: ComponentCollection, array: Array[IComponent], index: int)
            Copies the entire collection to an array, starting writing at the specified array index.
        
            array: An System.ComponentModel.IComponent array to copy the objects in the collection to.
            index: The index of the array at which copying to should begin.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, components):
        """ __new__(cls: type, components: Array[IComponent]) """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class ReferenceConverter(TypeConverter):
    """
    Provides a type converter to convert object references to and from other representations.
    
    ReferenceConverter(type: Type)
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ReferenceConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a reference object using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this object can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ReferenceConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the reference type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ReferenceConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the reference type using the specified context and arguments.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.
            value: The System.Object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: ReferenceConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard values for the reference data type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: ReferenceConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether the list of standard values returned from 
             System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC
             ontext) is an exclusive list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC
             ontext) is an exhaustive list of possible values. This method never returns false.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: ReferenceConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports a standard set of values that can be picked 
             from a list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because 
             System.ComponentModel.ReferenceConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorC
             ontext) can be called to find a common set of values the object supports. This method never 
             returns false.
        """
        pass

    def IsValueAllowed(self, *args): #cannot find CLR method
        """
        IsValueAllowed(self: ReferenceConverter, context: ITypeDescriptorContext, value: object) -> bool
        
            Returns a value indicating whether a particular value can be added to the standard values 
             collection.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides an additional context.
            value: The value to check.
            Returns: true if the value is allowed and can be added to the standard values collection; false if the 
             value cannot be added to the standard values collection.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass


class ComponentConverter(ReferenceConverter):
    """
    Provides a type converter to convert components to and from various other representations.
    
    ComponentConverter(type: Type)
    """
    def GetProperties(self, *__args):
        """
        GetProperties(self: ComponentConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets a collection of properties for the type of component specified by the value parameter.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of component to get the properties for.
            attributes: An array of type System.Attribute that will be used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             the component, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: ComponentConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports properties using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called 
             to find the properties of this object. This method never returns false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass


class ComponentEditor(object):
    """ Provides the base class for a custom component editor. """
    def EditComponent(self, *__args):
        """
        EditComponent(self: ComponentEditor, context: ITypeDescriptorContext, component: object) -> bool
        
            Edits the component and returns a value indicating whether the component was modified based upon 
             a given context.
        
        
            context: An optional context object that can be used to obtain further information about the edit.
            component: The component to be edited.
            Returns: true if the component was modified; otherwise, false.
        EditComponent(self: ComponentEditor, component: object) -> bool
        
            Edits the component and returns a value indicating whether the component was modified.
        
            component: The component to be edited.
            Returns: true if the component was modified; otherwise, false.
        """
        pass


class ComponentResourceManager(ResourceManager):
    """
    Provides simple functionality for enumerating resources for a component or object. The System.ComponentModel.ComponentResourceManager class is a System.Resources.ResourceManager.
    
    ComponentResourceManager()
    ComponentResourceManager(t: Type)
    """
    def ApplyResources(self, value, objectName, culture=None):
        """
        ApplyResources(self: ComponentResourceManager, value: object, objectName: str, culture: CultureInfo)
            Applies a resource's value to the corresponding property of the object.
        
            value: An System.Object that contains the property value to be applied.
            objectName: A System.String that contains the name of the object to look up in the resources.
            culture: The culture for which to apply resources.
        ApplyResources(self: ComponentResourceManager, value: object, objectName: str)
            Applies a resource's value to the corresponding property of the object.
        
            value: An System.Object that contains the property value to be applied.
            objectName: A System.String that contains the name of the object to look up in the resources.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, t=None):
        """
        __new__(cls: type)
        __new__(cls: type, t: Type)
        """
        pass

    FallbackLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the location from which to retrieve neutral fallback resources.

"""


    BaseNameField = None
    MainAssembly = None
    ResourceSets = None


class Container(object, IContainer, IDisposable):
    """
    Encapsulates zero or more components.
    
    Container()
    """
    def Add(self, component, name=None):
        """
        Add(self: Container, component: IComponent, name: str)
            Adds the specified System.ComponentModel.Component to the System.ComponentModel.Container and 
             assigns it a name.
        
        
            component: The component to add.
            name: The unique, case-insensitive name to assign to the component.-or- null, which leaves the 
             component unnamed.
        
        Add(self: Container, component: IComponent)
            Adds the specified System.ComponentModel.Component to the System.ComponentModel.Container. The 
             component is unnamed.
        
        
            component: The component to add.
        """
        pass

    def CreateSite(self, *args): #cannot find CLR method
        """
        CreateSite(self: Container, component: IComponent, name: str) -> ISite
        
            Creates a site System.ComponentModel.ISite for the given System.ComponentModel.IComponent and 
             assigns the given name to the site.
        
        
            component: The System.ComponentModel.IComponent to create a site for.
            name: The name to assign to component, or null to skip the name assignment.
            Returns: The newly created site.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Container)
            Releases all resources used by the System.ComponentModel.Container.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Container, service: Type) -> object
        
            Gets the service object of the specified type, if it is available.
        
            service: The System.Type of the service to retrieve.
            Returns: An System.Object implementing the requested service, or null if the service cannot be resolved.
        """
        pass

    def Remove(self, component):
        """
        Remove(self: Container, component: IComponent)
            Removes a component from the System.ComponentModel.Container.
        
            component: The component to remove.
        """
        pass

    def RemoveWithoutUnsiting(self, *args): #cannot find CLR method
        """
        RemoveWithoutUnsiting(self: Container, component: IComponent)
            Removes a component from the System.ComponentModel.Container without setting 
             System.ComponentModel.IComponent.Site to null.
        
        
            component: The component to remove.
        """
        pass

    def ValidateName(self, *args): #cannot find CLR method
        """
        ValidateName(self: Container, component: IComponent, name: str)
            Determines whether the component name is unique for this container.
        
            component: The named component.
            name: The component name to validate.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the components in the System.ComponentModel.Container.

Get: Components(self: Container) -> ComponentCollection

"""



class ContainerFilterService(object):
    """ Provides a base class for the container filter service. """
    def FilterComponents(self, components):
        """
        FilterComponents(self: ContainerFilterService, components: ComponentCollection) -> ComponentCollection
        
            Filters the component collection.
        
            components: The component collection to filter.
            Returns: A System.ComponentModel.ComponentCollection that represents a modified collection.
        """
        pass


class CultureInfoConverter(TypeConverter):
    """
    Provides a type converter to convert System.Globalization.CultureInfo objects to and from various other representations.
    
    CultureInfoConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CultureInfoConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a System.Globalization.CultureInfo using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CultureInfoConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CultureInfoConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified value object to a System.Globalization.CultureInfo.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CultureInfoConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture to which to convert.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetCultureName(self, *args): #cannot find CLR method
        """
        GetCultureName(self: CultureInfoConverter, culture: CultureInfo) -> str
        
            Retrieves the name of the specified culture.
        
            culture: A System.Globalization.CultureInfo that specifies the culture to get the name for.
            Returns: The name of the specified culture.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: CultureInfoConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard values for a System.Globalization.CultureInfo object using the 
             specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection containing a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: CultureInfoConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether the list of standard values returned from 
             System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto
             rContext) is an exhaustive list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: false because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto
             rContext) is not an exhaustive list of possible values (that is, other values are possible). 
             This method never returns true.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: CultureInfoConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports a standard set of values that can be picked 
             from a list using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because 
             System.ComponentModel.CultureInfoConverter.GetStandardValues(System.ComponentModel.ITypeDescripto
             rContext) should be called to find a common set of values the object supports. This method never 
             returns false.
        """
        pass


class CustomTypeDescriptor(object, ICustomTypeDescriptor):
    """ Provides a simple default implementation of the System.ComponentModel.ICustomTypeDescriptor interface. """
    def GetAttributes(self):
        """
        GetAttributes(self: CustomTypeDescriptor) -> AttributeCollection
        
            Returns a collection of custom attributes for the type represented by this type descriptor.
            Returns: An System.ComponentModel.AttributeCollection containing the attributes for the type. The default 
             is System.ComponentModel.AttributeCollection.Empty.
        """
        pass

    def GetClassName(self):
        """
        GetClassName(self: CustomTypeDescriptor) -> str
        
            Returns the fully qualified name of the class represented by this type descriptor.
            Returns: A System.String containing the fully qualified class name of the type this type descriptor is 
             describing. The default is null.
        """
        pass

    def GetComponentName(self):
        """
        GetComponentName(self: CustomTypeDescriptor) -> str
        
            Returns the name of the class represented by this type descriptor.
            Returns: A System.String containing the name of the component instance this type descriptor is 
             describing. The default is null.
        """
        pass

    def GetConverter(self):
        """
        GetConverter(self: CustomTypeDescriptor) -> TypeConverter
        
            Returns a type converter for the type represented by this type descriptor.
            Returns: A System.ComponentModel.TypeConverter for the type represented by this type descriptor. The 
             default is a newly created System.ComponentModel.TypeConverter.
        """
        pass

    def GetDefaultEvent(self):
        """
        GetDefaultEvent(self: CustomTypeDescriptor) -> EventDescriptor
        
            Returns the event descriptor for the default event of the object represented by this type 
             descriptor.
        
            Returns: The System.ComponentModel.EventDescriptor for the default event on the object represented by 
             this type descriptor. The default is null.
        """
        pass

    def GetDefaultProperty(self):
        """
        GetDefaultProperty(self: CustomTypeDescriptor) -> PropertyDescriptor
        
            Returns the property descriptor for the default property of the object represented by this type 
             descriptor.
        
            Returns: A System.ComponentModel.PropertyDescriptor for the default property on the object represented by 
             this type descriptor. The default is null.
        """
        pass

    def GetEditor(self, editorBaseType):
        """
        GetEditor(self: CustomTypeDescriptor, editorBaseType: Type) -> object
        
            Returns an editor of the specified type that is to be associated with the class represented by 
             this type descriptor.
        
        
            editorBaseType: The base type of the editor to retrieve.
            Returns: An editor of the given type that is to be associated with the class represented by this type 
             descriptor. The default is null.
        """
        pass

    def GetEvents(self, attributes=None):
        """
        GetEvents(self: CustomTypeDescriptor, attributes: Array[Attribute]) -> EventDescriptorCollection
        
            Returns a filtered collection of event descriptors for the object represented by this type 
             descriptor.
        
        
            attributes: An array of attributes to use as a filter. This can be null.
            Returns: An System.ComponentModel.EventDescriptorCollection containing the event descriptions for the 
             object represented by this type descriptor. The default is 
             System.ComponentModel.EventDescriptorCollection.Empty.
        
        GetEvents(self: CustomTypeDescriptor) -> EventDescriptorCollection
        
            Returns a collection of event descriptors for the object represented by this type descriptor.
            Returns: An System.ComponentModel.EventDescriptorCollection containing the event descriptors for the 
             object represented by this type descriptor. The default is 
             System.ComponentModel.EventDescriptorCollection.Empty.
        """
        pass

    def GetProperties(self, attributes=None):
        """
        GetProperties(self: CustomTypeDescriptor) -> PropertyDescriptorCollection
        
            Returns a collection of property descriptors for the object represented by this type descriptor.
            Returns: A System.ComponentModel.PropertyDescriptorCollection containing the property descriptions for 
             the object represented by this type descriptor. The default is 
             System.ComponentModel.PropertyDescriptorCollection.Empty.
        
        GetProperties(self: CustomTypeDescriptor, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a filtered collection of property descriptors for the object represented by this type 
             descriptor.
        
        
            attributes: An array of attributes to use as a filter. This can be null.
            Returns: A System.ComponentModel.PropertyDescriptorCollection containing the property descriptions for 
             the object represented by this type descriptor. The default is 
             System.ComponentModel.PropertyDescriptorCollection.Empty.
        """
        pass

    def GetPropertyOwner(self, pd):
        """
        GetPropertyOwner(self: CustomTypeDescriptor, pd: PropertyDescriptor) -> object
        
            Returns an object that contains the property described by the specified property descriptor.
        
            pd: The property descriptor for which to retrieve the owning object.
            Returns: An System.Object that owns the given property specified by the type descriptor. The default is 
             null.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, parent: ICustomTypeDescriptor)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DataErrorsChangedEventArgs(EventArgs):
    """ DataErrorsChangedEventArgs(propertyName: str) """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: DataErrorsChangedEventArgs) -> str

"""



class DataObjectAttribute(Attribute, _Attribute):
    """
    Identifies a type as an object suitable for binding to an System.Web.UI.WebControls.ObjectDataSource object. This class cannot be inherited.
    
    DataObjectAttribute()
    DataObjectAttribute(isDataObject: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: DataObjectAttribute, obj: object) -> bool
        
            Determines whether this instance of System.ComponentModel.DataObjectAttribute fits the pattern 
             of another object.
        
        
            obj: An object to compare with this instance of System.ComponentModel.DataObjectAttribute.
            Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise, 
             false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DataObjectAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DataObjectAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isDataObject=None):
        """
        __new__(cls: type)
        __new__(cls: type, isDataObject: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsDataObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an object should be considered suitable for binding to an System.Web.UI.WebControls.ObjectDataSource object at design time.

Get: IsDataObject(self: DataObjectAttribute) -> bool

"""


    DataObject = None
    Default = None
    NonDataObject = None


class DataObjectFieldAttribute(Attribute, _Attribute):
    """
    Provides metadata for a property representing a data field. This class cannot be inherited.
    
    DataObjectFieldAttribute(primaryKey: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
    """
    def Equals(self, obj):
        """
        Equals(self: DataObjectFieldAttribute, obj: object) -> bool
        
            Returns a value indicating whether this instance is equal to a specified object.
        
            obj: An object to compare with this instance of System.ComponentModel.DataObjectFieldAttribute.
            Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise, 
             false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DataObjectFieldAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, primaryKey, isIdentity=None, isNullable=None, length=None):
        """
        __new__(cls: type, primaryKey: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property represents an identity field in the underlying data.

Get: IsIdentity(self: DataObjectFieldAttribute) -> bool

"""

    IsNullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property represents a field that can be null in the underlying data store.

Get: IsNullable(self: DataObjectFieldAttribute) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the property in bytes.

Get: Length(self: DataObjectFieldAttribute) -> int

"""

    PrimaryKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property is in the primary key in the underlying data.

Get: PrimaryKey(self: DataObjectFieldAttribute) -> bool

"""



class DataObjectMethodAttribute(Attribute, _Attribute):
    """
    Identifies a data operation method exposed by a type, what type of operation the method performs, and whether the method is the default data method. This class cannot be inherited.
    
    DataObjectMethodAttribute(methodType: DataObjectMethodType)
    DataObjectMethodAttribute(methodType: DataObjectMethodType, isDefault: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: DataObjectMethodAttribute, obj: object) -> bool
        
            Returns a value indicating whether this instance is equal to a specified object.
        
            obj: An object to compare with this instance of System.ComponentModel.DataObjectMethodAttribute.
            Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise, 
             false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DataObjectMethodAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def Match(self, obj):
        """
        Match(self: DataObjectMethodAttribute, obj: object) -> bool
        
            Gets a value indicating whether this instance shares a common pattern with a specified attribute.
        
            obj: An object to compare with this instance of System.ComponentModel.DataObjectMethodAttribute.
            Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise, 
             false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, methodType, isDefault=None):
        """
        __new__(cls: type, methodType: DataObjectMethodType)
        __new__(cls: type, methodType: DataObjectMethodType, isDefault: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the method that the System.ComponentModel.DataObjectMethodAttribute is applied to is the default data method exposed by the data object for a specific method type.

Get: IsDefault(self: DataObjectMethodAttribute) -> bool

"""

    MethodType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.ComponentModel.DataObjectMethodType value indicating the type of data operation the method performs.

Get: MethodType(self: DataObjectMethodAttribute) -> DataObjectMethodType

"""



class DataObjectMethodType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the type of data operation performed by a method, as specified by the System.ComponentModel.DataObjectMethodAttribute applied to the method.
    
    enum DataObjectMethodType, values: Delete (4), Fill (0), Insert (3), Select (1), Update (2)
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

    Delete = None
    Fill = None
    Insert = None
    Select = None
    Update = None
    value__ = None


class DateTimeConverter(TypeConverter):
    """
    Provides a type converter to convert System.DateTime objects to and from various other representations.
    
    DateTimeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: DateTimeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a System.DateTime using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this object can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DateTimeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: DateTimeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given value object to a System.DateTime.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DateTimeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to a System.DateTime using the arguments.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass


class DateTimeOffsetConverter(TypeConverter):
    """
    Provides a type converter to convert System.DateTimeOffset structures to and from various other representations.
    
    DateTimeOffsetConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: DateTimeOffsetConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns a value that indicates whether an object of the specified source type can be converted 
             to a System.DateTimeOffset.
        
        
            context: The date format context.
            sourceType: The source type to check.
            Returns: true if the specified type can be converted to a System.DateTimeOffset; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DateTimeOffsetConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value that indicates whether a System.DateTimeOffset can be converted to an object of 
             the specified type.
        
        
            context: The date format context.
            destinationType: The destination type to check.
            Returns: true if a System.DateTimeOffset can be converted to the specified type; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: DateTimeOffsetConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to a System.DateTimeOffset.
        
            context: The date format context.
            culture: The date culture.
            value: The object to be converted.
            Returns: A System.DateTimeOffset that represents the specified object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DateTimeOffsetConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a System.DateTimeOffset to an object of the specified type.
        
            context: The date format context.
            culture: The date culture.
            value: The System.DateTimeOffset to be converted.
            destinationType: The type to convert to.
            Returns: An object of the specified type that represents the System.DateTimeOffset.
        """
        pass


class DecimalConverter(BaseNumberConverter):
    """
    Provides a type converter to convert System.Decimal objects to and from various other representations.
    
    DecimalConverter()
    """
    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DecimalConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DecimalConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to a System.Decimal using the arguments.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass


class DefaultBindingPropertyAttribute(Attribute, _Attribute):
    """
    Specifies the default binding property for a component. This class cannot be inherited.
    
    DefaultBindingPropertyAttribute()
    DefaultBindingPropertyAttribute(name: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DefaultBindingPropertyAttribute, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.ComponentModel.DefaultBindingPropertyAttribute instance.
        
        
            obj: The System.Object to compare with the current 
             System.ComponentModel.DefaultBindingPropertyAttribute instance
        
            Returns: true if the object is equal to the current instance; otherwise, false, indicating they are not 
             equal.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DefaultBindingPropertyAttribute) -> int
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the default binding property for the component to which the System.ComponentModel.DefaultBindingPropertyAttribute is bound.

Get: Name(self: DefaultBindingPropertyAttribute) -> str

"""


    Default = None


class DefaultEventAttribute(Attribute, _Attribute):
    """
    Specifies the default event for a component.
    
    DefaultEventAttribute(name: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DefaultEventAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DefaultEventAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DefaultEventAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the default event for the component this attribute is bound to.

Get: Name(self: DefaultEventAttribute) -> str

"""


    Default = None


class DefaultPropertyAttribute(Attribute, _Attribute):
    """
    Specifies the default property for a component.
    
    DefaultPropertyAttribute(name: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DefaultPropertyAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DefaultPropertyAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DefaultPropertyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the default property for the component this attribute is bound to.

Get: Name(self: DefaultPropertyAttribute) -> str

"""


    Default = None


class DefaultValueAttribute(Attribute, _Attribute):
    """
    Specifies the default value for a property.
    
    DefaultValueAttribute(type: Type, value: str)
    DefaultValueAttribute(value: Char)
    DefaultValueAttribute(value: Byte)
    DefaultValueAttribute(value: Int16)
    DefaultValueAttribute(value: int)
    DefaultValueAttribute(value: Int64)
    DefaultValueAttribute(value: Single)
    DefaultValueAttribute(value: float)
    DefaultValueAttribute(value: bool)
    DefaultValueAttribute(value: str)
    DefaultValueAttribute(value: object)
    """
    def Equals(self, obj):
        """
        Equals(self: DefaultValueAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DefaultValueAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DefaultValueAttribute) -> int """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """
        SetValue(self: DefaultValueAttribute, value: object)
            Sets the default value for the property to which this attribute is bound.
        
            value: The default value.
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
        __new__(cls: type, type: Type, value: str)
        __new__(cls: type, value: Char)
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: Int16)
        __new__(cls: type, value: int)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: Single)
        __new__(cls: type, value: float)
        __new__(cls: type, value: bool)
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default value of the property this attribute is bound to.

Get: Value(self: DefaultValueAttribute) -> object

"""



class DescriptionAttribute(Attribute, _Attribute):
    """
    Specifies a description for a property or event.
    
    DescriptionAttribute()
    DescriptionAttribute(description: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DescriptionAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DescriptionAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DescriptionAttribute) -> int """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DescriptionAttribute) -> bool
        
            Returns a value indicating whether this is the default 
             System.ComponentModel.DescriptionAttribute instance.
        
            Returns: true, if this is the default System.ComponentModel.DescriptionAttribute instance; otherwise, 
             false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description stored in this attribute.

Get: Description(self: DescriptionAttribute) -> str

"""

    DescriptionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string stored as the description.

"""


    Default = None


class DesignerAttribute(Attribute, _Attribute):
    """
    Specifies the class used to implement design-time services for a component.
    
    DesignerAttribute(designerTypeName: str)
    DesignerAttribute(designerType: Type)
    DesignerAttribute(designerTypeName: str, designerBaseTypeName: str)
    DesignerAttribute(designerTypeName: str, designerBaseType: Type)
    DesignerAttribute(designerType: Type, designerBaseType: Type)
    """
    def Equals(self, obj):
        """
        Equals(self: DesignerAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DesignerAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DesignerAttribute) -> int """
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
        __new__(cls: type, designerTypeName: str)
        __new__(cls: type, designerType: Type)
        __new__(cls: type, designerTypeName: str, designerBaseTypeName: str)
        __new__(cls: type, designerTypeName: str, designerBaseType: Type)
        __new__(cls: type, designerType: Type, designerBaseType: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DesignerBaseTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the base type of this designer.

Get: DesignerBaseTypeName(self: DesignerAttribute) -> str

"""

    DesignerTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the designer type associated with this designer attribute.

Get: DesignerTypeName(self: DesignerAttribute) -> str

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique ID for this attribute type.

Get: TypeId(self: DesignerAttribute) -> object

"""



class DesignerCategoryAttribute(Attribute, _Attribute):
    """
    Specifies that the designer for a class belongs to a certain category.
    
    DesignerCategoryAttribute()
    DesignerCategoryAttribute(category: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DesignerCategoryAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DesignOnlyAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DesignerCategoryAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DesignerCategoryAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, category=None):
        """
        __new__(cls: type)
        __new__(cls: type, category: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the category.

Get: Category(self: DesignerCategoryAttribute) -> str

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique identifier for this attribute.

Get: TypeId(self: DesignerCategoryAttribute) -> object

"""


    Component = None
    Default = None
    Form = None
    Generic = None


class DesignerSerializationVisibility(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the visibility a property has to the design-time serializer.
    
    enum DesignerSerializationVisibility, values: Content (2), Hidden (0), Visible (1)
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

    Content = None
    Hidden = None
    value__ = None
    Visible = None


class DesignerSerializationVisibilityAttribute(Attribute, _Attribute):
    """
    Specifies the type of persistence to use when serializing a property on a component at design time.
    
    DesignerSerializationVisibilityAttribute(visibility: DesignerSerializationVisibility)
    """
    def Equals(self, obj):
        """
        Equals(self: DesignerSerializationVisibilityAttribute, obj: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            obj: Another object to compare to.
            Returns: true if obj is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DesignerSerializationVisibilityAttribute) -> int
        
            Returns the hash code for this object.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DesignerSerializationVisibilityAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the attribute is set to the default value; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visibility):
        """ __new__(cls: type, visibility: DesignerSerializationVisibility) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the basic serialization mode a serializer should use when determining whether and how to persist the value of a property.

Get: Visibility(self: DesignerSerializationVisibilityAttribute) -> DesignerSerializationVisibility

"""


    Content = None
    Default = None
    Hidden = None
    Visible = None


class DesignOnlyAttribute(Attribute, _Attribute):
    """
    Specifies whether a property can only be set at design time.
    
    DesignOnlyAttribute(isDesignOnly: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: DesignOnlyAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.DesignOnlyAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DesignOnlyAttribute) -> int """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DesignOnlyAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isDesignOnly):
        """ __new__(cls: type, isDesignOnly: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsDesignOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property can be set only at design time.

Get: IsDesignOnly(self: DesignOnlyAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class DesignTimeVisibleAttribute(Attribute, _Attribute):
    """
    System.ComponentModel.DesignTimeVisibleAttribute marks a component's visibility. If System.ComponentModel.DesignTimeVisibleAttribute.Yes is present, a visual designer can show this component on a designer.
    
    DesignTimeVisibleAttribute(visible: bool)
    DesignTimeVisibleAttribute()
    """
    def Equals(self, obj):
        """
        Equals(self: DesignTimeVisibleAttribute, obj: object) -> bool
        
            obj: The object to compare.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DesignTimeVisibleAttribute) -> int """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DesignTimeVisibleAttribute) -> bool
        
            Gets a value indicating if this instance is equal to the 
             System.ComponentModel.DesignTimeVisibleAttribute.Default value.
        
            Returns: true, if this instance is equal to the System.ComponentModel.DesignTimeVisibleAttribute.Default 
             value; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visible=None):
        """
        __new__(cls: type, visible: bool)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the component should be shown at design time.

Get: Visible(self: DesignTimeVisibleAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class DisplayNameAttribute(Attribute, _Attribute):
    """
    Specifies the display name for a property, event, or public void method which takes no arguments.
    
    DisplayNameAttribute()
    DisplayNameAttribute(displayName: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DisplayNameAttribute, obj: object) -> bool
        
            Determines whether two System.ComponentModel.DisplayNameAttribute instances are equal.
        
            obj: The System.ComponentModel.DisplayNameAttribute to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DisplayNameAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.DisplayNameAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: DisplayNameAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayName=None):
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display name for a property, event, or public void method that takes no arguments stored in this attribute.

Get: DisplayName(self: DisplayNameAttribute) -> str

"""

    DisplayNameValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the display name.

"""


    Default = None


class DoubleConverter(BaseNumberConverter):
    """
    Provides a type converter to convert double-precision, floating point number objects to and from various other representations.
    
    DoubleConverter()
    """

class DoWorkEventArgs(CancelEventArgs):
    """
    Provides data for the System.ComponentModel.BackgroundWorker.DoWork event handler.
    
    DoWorkEventArgs(argument: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, argument):
        """ __new__(cls: type, argument: object) """
        pass

    Argument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the argument of an asynchronous operation.

Get: Argument(self: DoWorkEventArgs) -> object

"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the result of an asynchronous operation.

Get: Result(self: DoWorkEventArgs) -> object

Set: Result(self: DoWorkEventArgs) = value
"""



class DoWorkEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.BackgroundWorker.DoWork event. This class cannot be inherited.
    
    DoWorkEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DoWorkEventHandler, sender: object, e: DoWorkEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: DoWorkEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DoWorkEventHandler, sender: object, e: DoWorkEventArgs) """
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


class EditorAttribute(Attribute, _Attribute):
    """
    Specifies the editor to use to change a property. This class cannot be inherited.
    
    EditorAttribute()
    EditorAttribute(typeName: str, baseTypeName: str)
    EditorAttribute(typeName: str, baseType: Type)
    EditorAttribute(type: Type, baseType: Type)
    """
    def Equals(self, obj):
        """
        Equals(self: EditorAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.EditorAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EditorAttribute) -> int """
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
        __new__(cls: type)
        __new__(cls: type, typeName: str, baseTypeName: str)
        __new__(cls: type, typeName: str, baseType: Type)
        __new__(cls: type, type: Type, baseType: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    EditorBaseTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the base class or interface serving as a lookup key for this editor.

Get: EditorBaseTypeName(self: EditorAttribute) -> str

"""

    EditorTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the editor class in the System.Type.AssemblyQualifiedName format.

Get: EditorTypeName(self: EditorAttribute) -> str

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique ID for this attribute type.

Get: TypeId(self: EditorAttribute) -> object

"""



class EditorBrowsableAttribute(Attribute, _Attribute):
    """
    Specifies that a property or method is viewable in an editor. This class cannot be inherited.
    
    EditorBrowsableAttribute(state: EditorBrowsableState)
    EditorBrowsableAttribute()
    """
    def Equals(self, obj):
        """
        Equals(self: EditorBrowsableAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.EditorBrowsableAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EditorBrowsableAttribute) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state=None):
        """
        __new__(cls: type, state: EditorBrowsableState)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the browsable state of the property or method.

Get: State(self: EditorBrowsableAttribute) -> EditorBrowsableState

"""



class EditorBrowsableState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the browsable state of a property or method from within an editor.
    
    enum EditorBrowsableState, values: Advanced (2), Always (0), Never (1)
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

    Advanced = None
    Always = None
    Never = None
    value__ = None


class EnumConverter(TypeConverter):
    """
    Provides a type converter to convert System.Enum objects to and from various other representations.
    
    EnumConverter(type: Type)
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: EnumConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             an enumeration object using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: EnumConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: EnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified value object to an enumeration object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: EnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: EnumConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard values for the data type this validator is designed for.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: EnumConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether the list of standard values returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exclusive list using the specified 
             context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 
             false if other values are possible.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: EnumConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports a standard set of values that can be picked 
             from a list using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because System.ComponentModel.TypeConverter.GetStandardValues should be called to find a 
             common set of values the object supports. This method never returns false.
        """
        pass

    def IsValid(self, *__args):
        """
        IsValid(self: EnumConverter, context: ITypeDescriptorContext, value: object) -> bool
        
            Gets a value indicating whether the given object value is valid for this type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: The System.Object to test.
            Returns: true if the specified value is valid for this object; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IComparer that can be used to sort the values of the enumeration.

"""

    EnumType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the type of the enumerator this converter is associated with.

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.ComponentModel.TypeConverter.StandardValuesCollection that specifies the possible values for the enumeration.

"""



class MemberDescriptor(object):
    """ Represents a class member, such as a property or event. This is an abstract base class. """
    def CreateAttributeCollection(self, *args): #cannot find CLR method
        """
        CreateAttributeCollection(self: MemberDescriptor) -> AttributeCollection
        
            Creates a collection of attributes using the array of attributes passed to the constructor.
            Returns: A new System.ComponentModel.AttributeCollection that contains the 
             System.ComponentModel.MemberDescriptor.AttributeArray attributes.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: MemberDescriptor, obj: object) -> bool
        
            Compares this instance to the given object to see if they are equivalent.
        
            obj: The object to compare to the current instance.
            Returns: true if equivalent; otherwise, false.
        """
        pass

    def FillAttributes(self, *args): #cannot find CLR method
        """
        FillAttributes(self: MemberDescriptor, attributeList: IList)
            When overridden in a derived class, adds the attributes of the inheriting class to the specified 
             list of attributes in the parent class.
        
        
            attributeList: An System.Collections.IList that lists the attributes in the parent class. Initially, this is 
             empty.
        """
        pass

    def FindMethod(self, *args): #cannot find CLR method
        """
        FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type, publicOnly: bool) -> MethodInfo
        
            Finds the given method through reflection, with an option to search only public methods.
        
            componentClass: The component that contains the method.
            name: The name of the method to find.
            args: An array of parameters for the method, used to choose between overloaded methods.
            returnType: The type to return for the method.
            publicOnly: Whether to restrict search to public methods.
            Returns: A System.Reflection.MethodInfo that represents the method, or null if the method is not found.
        FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type) -> MethodInfo
        
            Finds the given method through reflection, searching only for public methods.
        
            componentClass: The component that contains the method.
            name: The name of the method to find.
            args: An array of parameters for the method, used to choose between overloaded methods.
            returnType: The type to return for the method.
            Returns: A System.Reflection.MethodInfo that represents the method, or null if the method is not found.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MemberDescriptor) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.MemberDescriptor.
        """
        pass

    def GetInvocationTarget(self, *args): #cannot find CLR method
        """
        GetInvocationTarget(self: MemberDescriptor, type: Type, instance: object) -> object
        
            Retrieves the object that should be used during invocation of members.
        
            type: The System.Type of the invocation target.
            instance: The potential invocation target.
            Returns: The object to be used during member invocations.
        """
        pass

    def GetInvokee(self, *args): #cannot find CLR method
        """
        GetInvokee(componentClass: Type, component: object) -> object
        
            Gets the component on which to invoke a method.
        
            componentClass: A System.Type representing the type of component this System.ComponentModel.MemberDescriptor is 
             bound to. For example, if this System.ComponentModel.MemberDescriptor describes a property, this 
             parameter should be the class that the property is declared on.
        
            component: An instance of the object to call.
            Returns: An instance of the component to invoke. This method returns a visual designer when the property 
             is attached to a visual designer.
        """
        pass

    def GetSite(self, *args): #cannot find CLR method
        """
        GetSite(component: object) -> ISite
        
            Gets a component site for the given component.
        
            component: The component for which you want to find a site.
            Returns: The site of the component, or null if a site does not exist.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, attributes: Array[Attribute])
        __new__(cls: type, descr: MemberDescriptor)
        __new__(cls: type, oldMemberDescriptor: MemberDescriptor, newAttributes: Array[Attribute])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of attributes.

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of attributes for this member.

Get: Attributes(self: MemberDescriptor) -> AttributeCollection

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the category to which the member belongs, as specified in the System.ComponentModel.CategoryAttribute.

Get: Category(self: MemberDescriptor) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description of the member, as specified in the System.ComponentModel.DescriptionAttribute.

Get: Description(self: MemberDescriptor) -> str

"""

    DesignTimeOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this member should be set only at design time, as specified in the System.ComponentModel.DesignOnlyAttribute.

Get: DesignTimeOnly(self: MemberDescriptor) -> bool

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name that can be displayed in a window, such as a Properties window.

Get: DisplayName(self: MemberDescriptor) -> str

"""

    IsBrowsable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the member is browsable, as specified in the System.ComponentModel.BrowsableAttribute.

Get: IsBrowsable(self: MemberDescriptor) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the member.

Get: Name(self: MemberDescriptor) -> str

"""

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash code for the name of the member, as specified in System.String.GetHashCode.

"""



class EventDescriptor(MemberDescriptor):
    """ Provides information about an event. """
    def AddEventHandler(self, component, value):
        """
        AddEventHandler(self: EventDescriptor, component: object, value: Delegate)
            When overridden in a derived class, binds the event to the component.
        
            component: A component that provides events to the delegate.
            value: A delegate that represents the method that handles the event.
        """
        pass

    def RemoveEventHandler(self, component, value):
        """
        RemoveEventHandler(self: EventDescriptor, component: object, value: Delegate)
            When overridden in a derived class, unbinds the delegate from the component so that the delegate 
             will no longer receive events from the component.
        
        
            component: The component that the delegate is bound to.
            value: The delegate to unbind from the component.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, name: str, attrs: Array[Attribute])
        __new__(cls: type, descr: MemberDescriptor)
        __new__(cls: type, descr: MemberDescriptor, attrs: Array[Attribute])
        """
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of attributes.

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the type of component this event is bound to.

Get: ComponentType(self: EventDescriptor) -> Type

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the type of delegate for the event.

Get: EventType(self: EventDescriptor) -> Type

"""

    IsMulticast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the event delegate is a multicast delegate.

Get: IsMulticast(self: EventDescriptor) -> bool

"""

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash code for the name of the member, as specified in System.String.GetHashCode.

"""



class EventDescriptorCollection(object, ICollection, IEnumerable, IList):
    """
    Represents a collection of System.ComponentModel.EventDescriptor objects.
    
    EventDescriptorCollection(events: Array[EventDescriptor])
    EventDescriptorCollection(events: Array[EventDescriptor], readOnly: bool)
    """
    def Add(self, value):
        """
        Add(self: EventDescriptorCollection, value: EventDescriptor) -> int
        
            Adds an System.ComponentModel.EventDescriptor to the end of the collection.
        
            value: An System.ComponentModel.EventDescriptor to add to the collection.
            Returns: The position of the System.ComponentModel.EventDescriptor within the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: EventDescriptorCollection)
            Removes all objects from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: EventDescriptorCollection, value: EventDescriptor) -> bool
        
            Returns whether the collection contains the given System.ComponentModel.EventDescriptor.
        
            value: The System.ComponentModel.EventDescriptor to find within the collection.
            Returns: true if the collection contains the value parameter given; otherwise, false.
        """
        pass

    def Find(self, name, ignoreCase):
        """
        Find(self: EventDescriptorCollection, name: str, ignoreCase: bool) -> EventDescriptor
        
            Gets the description of the event with the specified name in the collection.
        
            name: The name of the event to get from the collection.
            ignoreCase: true if you want to ignore the case of the event; otherwise, false.
            Returns: The System.ComponentModel.EventDescriptor with the specified name, or null if the event does not 
             exist.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: EventDescriptorCollection) -> IEnumerator
        
            Gets an enumerator for this System.ComponentModel.EventDescriptorCollection.
            Returns: An enumerator that implements System.Collections.IEnumerator.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: EventDescriptorCollection, value: EventDescriptor) -> int
        
            Returns the index of the given System.ComponentModel.EventDescriptor.
        
            value: The System.ComponentModel.EventDescriptor to find within the collection.
            Returns: The index of the given System.ComponentModel.EventDescriptor within the collection.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: EventDescriptorCollection, index: int, value: EventDescriptor)
            Inserts an System.ComponentModel.EventDescriptor to the collection at a specified index.
        
            index: The index within the collection in which to insert the value parameter.
            value: An System.ComponentModel.EventDescriptor to insert into the collection.
        """
        pass

    def InternalSort(self, *args): #cannot find CLR method
        """
        InternalSort(self: EventDescriptorCollection, sorter: IComparer)
            Sorts the members of this System.ComponentModel.EventDescriptorCollection, using the specified 
             System.Collections.IComparer.
        
        
            sorter: A comparer to use to sort the System.ComponentModel.EventDescriptor objects in this collection.
        InternalSort(self: EventDescriptorCollection, names: Array[str])
            Sorts the members of this System.ComponentModel.EventDescriptorCollection. The specified order 
             is applied first, followed by the default sort for this collection, which is usually 
             alphabetical.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.EventDescriptor objects in this collection.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: EventDescriptorCollection, value: EventDescriptor)
            Removes the specified System.ComponentModel.EventDescriptor from the collection.
        
            value: The System.ComponentModel.EventDescriptor to remove from the collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: EventDescriptorCollection, index: int)
            Removes the System.ComponentModel.EventDescriptor at the specified index from the collection.
        
            index: The index of the System.ComponentModel.EventDescriptor to remove.
        """
        pass

    def Sort(self, *__args):
        """
        Sort(self: EventDescriptorCollection, names: Array[str], comparer: IComparer) -> EventDescriptorCollection
        
            Sorts the members of this System.ComponentModel.EventDescriptorCollection, given a specified 
             sort order and an System.Collections.IComparer.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.EventDescriptor objects in the collection.
        
            comparer: An System.Collections.IComparer to use to sort the System.ComponentModel.EventDescriptor objects 
             in this collection.
        
            Returns: The new System.ComponentModel.EventDescriptorCollection.
        Sort(self: EventDescriptorCollection, comparer: IComparer) -> EventDescriptorCollection
        
            Sorts the members of this System.ComponentModel.EventDescriptorCollection, using the specified 
             System.Collections.IComparer.
        
        
            comparer: An System.Collections.IComparer to use to sort the System.ComponentModel.EventDescriptor objects 
             in this collection.
        
            Returns: The new System.ComponentModel.EventDescriptorCollection.
        Sort(self: EventDescriptorCollection) -> EventDescriptorCollection
        
            Sorts the members of this System.ComponentModel.EventDescriptorCollection, using the default 
             sort for this collection, which is usually alphabetical.
        
            Returns: The new System.ComponentModel.EventDescriptorCollection.
        Sort(self: EventDescriptorCollection, names: Array[str]) -> EventDescriptorCollection
        
            Sorts the members of this System.ComponentModel.EventDescriptorCollection, given a specified 
             sort order.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.EventDescriptor objects in the collection.
        
            Returns: The new System.ComponentModel.EventDescriptorCollection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, events, readOnly=None):
        """
        __new__(cls: type, events: Array[EventDescriptor])
        __new__(cls: type, events: Array[EventDescriptor], readOnly: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of event descriptors in the collection.

Get: Count(self: EventDescriptorCollection) -> int

"""


    Empty = None


class EventHandlerList(object, IDisposable):
    """
    Provides a simple list of delegates. This class cannot be inherited.
    
    EventHandlerList()
    """
    def AddHandler(self, key, value):
        """
        AddHandler(self: EventHandlerList, key: object, value: Delegate)
            Adds a delegate to the list.
        
            key: The object that owns the event.
            value: The delegate to add to the list.
        """
        pass

    def AddHandlers(self, listToAddFrom):
        """
        AddHandlers(self: EventHandlerList, listToAddFrom: EventHandlerList)
            Adds a list of delegates to the current list.
        
            listToAddFrom: The list to add.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: EventHandlerList)
            Disposes the delegate list.
        """
        pass

    def RemoveHandler(self, key, value):
        """
        RemoveHandler(self: EventHandlerList, key: object, value: Delegate)
            Removes a delegate from the list.
        
            key: The object that owns the event.
            value: The delegate to remove from the list.
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class ExpandableObjectConverter(TypeConverter):
    """
    Provides a type converter to convert expandable objects to and from various other representations.
    
    ExpandableObjectConverter()
    """
    def GetProperties(self, *__args):
        """
        GetProperties(self: ExpandableObjectConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets a collection of properties for the type of object specified by the value parameter.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of object to get the properties for.
            attributes: An array of type System.Attribute that will be used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             the component, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: ExpandableObjectConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports properties using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called 
             to find the properties of this object. This method never returns false.
        """
        pass


class ExtenderProvidedPropertyAttribute(Attribute, _Attribute):
    """
    Specifies a property that is offered by an extender provider. This class cannot be inherited.
    
    ExtenderProvidedPropertyAttribute()
    """
    def Equals(self, obj):
        """
        Equals(self: ExtenderProvidedPropertyAttribute, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current System.Object.
        
            obj: An System.Object to compare with this instance or null.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ExtenderProvidedPropertyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ExtenderProvidedPropertyAttribute) -> bool
        
            Provides an indication whether the value of this instance is the default value for the derived 
             class.
        
            Returns: true if this instance is the default attribute for the class; otherwise, false.
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

    ExtenderProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property that is being provided.

Get: ExtenderProperty(self: ExtenderProvidedPropertyAttribute) -> PropertyDescriptor

"""

    Provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the extender provider that is providing the property.

Get: Provider(self: ExtenderProvidedPropertyAttribute) -> IExtenderProvider

"""

    ReceiverType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of object that can receive the property.

Get: ReceiverType(self: ExtenderProvidedPropertyAttribute) -> Type

"""



class GuidConverter(TypeConverter):
    """
    Provides a type converter to convert System.Guid objects to and from various other representations.
    
    GuidConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: GuidConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a GUID object using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: GuidConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: GuidConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to a GUID object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: GuidConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given object to another type.
        
            context: A formatter context.
            culture: The culture into which value will be converted.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass


class HandledEventArgs(EventArgs):
    """
    Provides data for events that can be handled completely in an event handler.
    
    HandledEventArgs()
    HandledEventArgs(defaultHandledValue: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, defaultHandledValue=None):
        """
        __new__(cls: type)
        __new__(cls: type, defaultHandledValue: bool)
        """
        pass

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the event handler has completely handled the event or whether the system should continue its own processing.

Get: Handled(self: HandledEventArgs) -> bool

Set: Handled(self: HandledEventArgs) = value
"""



class HandledEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a method that can handle events which may or may not require further processing after the event handler has returned.
    
    HandledEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: HandledEventHandler, sender: object, e: HandledEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: HandledEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: HandledEventHandler, sender: object, e: HandledEventArgs) """
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


class IBindingListView(IBindingList, IList, ICollection, IEnumerable):
    """ Extends the System.ComponentModel.IBindingList interface by providing advanced sorting and filtering capabilities. """
    def ApplySort(self, sorts):
        """
        ApplySort(self: IBindingListView, sorts: ListSortDescriptionCollection)
            Sorts the data source based on the given System.ComponentModel.ListSortDescriptionCollection.
        
            sorts: The System.ComponentModel.ListSortDescriptionCollection containing the sorts to apply to the 
             data source.
        """
        pass

    def RemoveFilter(self):
        """
        RemoveFilter(self: IBindingListView)
            Removes the current filter applied to the data source.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the filter to be used to exclude items from the collection of items returned by the data source

Get: Filter(self: IBindingListView) -> str

Set: Filter(self: IBindingListView) = value
"""

    SortDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of sort descriptions currently applied to the data source.

Get: SortDescriptions(self: IBindingListView) -> ListSortDescriptionCollection

"""

    SupportsAdvancedSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the data source supports advanced sorting.

Get: SupportsAdvancedSorting(self: IBindingListView) -> bool

"""

    SupportsFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the data source supports filtering.

Get: SupportsFiltering(self: IBindingListView) -> bool

"""



class IChangeTracking:
    """ Defines the mechanism for querying the object for changes and resetting of the changed status. """
    def AcceptChanges(self):
        """
        AcceptChanges(self: IChangeTracking)
                """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object's changed status.

Get: IsChanged(self: IChangeTracking) -> bool

"""



class IComNativeDescriptorHandler:
    """ Provides a top-level mapping layer between a COM object and a System.ComponentModel.TypeDescriptor. """
    def GetAttributes(self, component):
        """
        GetAttributes(self: IComNativeDescriptorHandler, component: object) -> AttributeCollection
        
            Gets the attributes for the specified component.
        
            component: The component to get attributes for.
            Returns: A collection of attributes for component.
        """
        pass

    def GetClassName(self, component):
        """
        GetClassName(self: IComNativeDescriptorHandler, component: object) -> str
        
            Gets the class name for the specified component.
        
            component: The component to get the class name for.
            Returns: The name of the class that corresponds with component.
        """
        pass

    def GetConverter(self, component):
        """
        GetConverter(self: IComNativeDescriptorHandler, component: object) -> TypeConverter
        
            Gets the type converter for the specified component.
        
            component: The component to get the System.ComponentModel.TypeConverter for.
            Returns: The System.ComponentModel.TypeConverter for component.
        """
        pass

    def GetDefaultEvent(self, component):
        """
        GetDefaultEvent(self: IComNativeDescriptorHandler, component: object) -> EventDescriptor
        
            Gets the default event for the specified component.
        
            component: The component to get the default event for.
            Returns: An System.ComponentModel.EventDescriptor that represents component's default event.
        """
        pass

    def GetDefaultProperty(self, component):
        """
        GetDefaultProperty(self: IComNativeDescriptorHandler, component: object) -> PropertyDescriptor
        
            Gets the default property for the specified component.
        
            component: The component to get the default property for.
            Returns: A System.ComponentModel.PropertyDescriptor that represents component's default property.
        """
        pass

    def GetEditor(self, component, baseEditorType):
        """
        GetEditor(self: IComNativeDescriptorHandler, component: object, baseEditorType: Type) -> object
        
            Gets the editor for the specified component.
        
            component: The component to get the editor for.
            baseEditorType: The base type of the editor for component.
            Returns: The editor for component.
        """
        pass

    def GetEvents(self, component, attributes=None):
        """
        GetEvents(self: IComNativeDescriptorHandler, component: object, attributes: Array[Attribute]) -> EventDescriptorCollection
        
            Gets the events with the specified attributes for the specified component.
        
            component: The component to get events for.
            attributes: The attributes used to filter events.
            Returns: A collection of event descriptors for component.
        GetEvents(self: IComNativeDescriptorHandler, component: object) -> EventDescriptorCollection
        
            Gets the events for the specified component.
        
            component: The component to get events for.
            Returns: A collection of event descriptors for component.
        """
        pass

    def GetName(self, component):
        """
        GetName(self: IComNativeDescriptorHandler, component: object) -> str
        
            Gets the name of the specified component.
        
            component: The component to get the name of.
            Returns: The name of component.
        """
        pass

    def GetProperties(self, component, attributes):
        """
        GetProperties(self: IComNativeDescriptorHandler, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets the properties with the specified attributes for the specified component.
        
            component: The component to get events for.
            attributes: The attributes used to filter properties.
            Returns: A collection of property descriptors for component.
        """
        pass

    def GetPropertyValue(self, component, *__args):
        """
        GetPropertyValue(self: IComNativeDescriptorHandler, component: object, dispid: int, success: bool) -> (object, bool)
        
            Gets the value of the property that has the specified dispatch identifier.
        
            component: The object to which the property belongs.
            dispid: The dispatch identifier.
            success: A System.Boolean, passed by reference, that represents whether the property was retrieved.
            Returns: The value of the property that has the specified dispatch identifier.
        GetPropertyValue(self: IComNativeDescriptorHandler, component: object, propertyName: str, success: bool) -> (object, bool)
        
            Gets the value of the property that has the specified name.
        
            component: The object to which the property belongs.
            propertyName: The name of the property.
            success: A System.Boolean, passed by reference, that represents whether the property was retrieved.
            Returns: The value of the property that has the specified name.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IComponent(IDisposable):
    """ Provides functionality required by all components. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.ComponentModel.ISite associated with the System.ComponentModel.IComponent.

Get: Site(self: IComponent) -> ISite

Set: Site(self: IComponent) = value
"""


    Disposed = None


class IContainer(IDisposable):
    """ Provides functionality for containers. Containers are objects that logically contain zero or more components. """
    def Add(self, component, name=None):
        """
        Add(self: IContainer, component: IComponent, name: str)
            Adds the specified System.ComponentModel.IComponent to the System.ComponentModel.IContainer at 
             the end of the list, and assigns a name to the component.
        
        
            component: The System.ComponentModel.IComponent to add.
            name: The unique, case-insensitive name to assign to the component.-or- null that leaves the component 
             unnamed.
        
        Add(self: IContainer, component: IComponent)
            Adds the specified System.ComponentModel.IComponent to the System.ComponentModel.IContainer at 
             the end of the list.
        
        
            component: The System.ComponentModel.IComponent to add.
        """
        pass

    def Remove(self, component):
        """
        Remove(self: IContainer, component: IComponent)
            Removes a component from the System.ComponentModel.IContainer.
        
            component: The System.ComponentModel.IComponent to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the components in the System.ComponentModel.IContainer.

Get: Components(self: IContainer) -> ComponentCollection

"""



class ICustomTypeDescriptor:
    """ Provides an interface that supplies dynamic custom type information for an object. """
    def GetAttributes(self):
        """
        GetAttributes(self: ICustomTypeDescriptor) -> AttributeCollection
        
            Returns a collection of custom attributes for this instance of a component.
            Returns: An System.ComponentModel.AttributeCollection containing the attributes for this object.
        """
        pass

    def GetClassName(self):
        """
        GetClassName(self: ICustomTypeDescriptor) -> str
        
            Returns the class name of this instance of a component.
            Returns: The class name of the object, or null if the class does not have a name.
        """
        pass

    def GetComponentName(self):
        """
        GetComponentName(self: ICustomTypeDescriptor) -> str
        
            Returns the name of this instance of a component.
            Returns: The name of the object, or null if the object does not have a name.
        """
        pass

    def GetConverter(self):
        """
        GetConverter(self: ICustomTypeDescriptor) -> TypeConverter
        
            Returns a type converter for this instance of a component.
            Returns: A System.ComponentModel.TypeConverter that is the converter for this object, or null if there is 
             no System.ComponentModel.TypeConverter for this object.
        """
        pass

    def GetDefaultEvent(self):
        """
        GetDefaultEvent(self: ICustomTypeDescriptor) -> EventDescriptor
        
            Returns the default event for this instance of a component.
            Returns: An System.ComponentModel.EventDescriptor that represents the default event for this object, or 
             null if this object does not have events.
        """
        pass

    def GetDefaultProperty(self):
        """
        GetDefaultProperty(self: ICustomTypeDescriptor) -> PropertyDescriptor
        
            Returns the default property for this instance of a component.
            Returns: A System.ComponentModel.PropertyDescriptor that represents the default property for this object, 
             or null if this object does not have properties.
        """
        pass

    def GetEditor(self, editorBaseType):
        """
        GetEditor(self: ICustomTypeDescriptor, editorBaseType: Type) -> object
        
            Returns an editor of the specified type for this instance of a component.
        
            editorBaseType: A System.Type that represents the editor for this object.
            Returns: An System.Object of the specified type that is the editor for this object, or null if the editor 
             cannot be found.
        """
        pass

    def GetEvents(self, attributes=None):
        """
        GetEvents(self: ICustomTypeDescriptor, attributes: Array[Attribute]) -> EventDescriptorCollection
        
            Returns the events for this instance of a component using the specified attribute array as a 
             filter.
        
        
            attributes: An array of type System.Attribute that is used as a filter.
            Returns: An System.ComponentModel.EventDescriptorCollection that represents the filtered events for this 
             component instance.
        
        GetEvents(self: ICustomTypeDescriptor) -> EventDescriptorCollection
        
            Returns the events for this instance of a component.
            Returns: An System.ComponentModel.EventDescriptorCollection that represents the events for this component 
             instance.
        """
        pass

    def GetProperties(self, attributes=None):
        """
        GetProperties(self: ICustomTypeDescriptor, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns the properties for this instance of a component using the attribute array as a filter.
        
            attributes: An array of type System.Attribute that is used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the filtered properties for 
             this component instance.
        
        GetProperties(self: ICustomTypeDescriptor) -> PropertyDescriptorCollection
        
            Returns the properties for this instance of a component.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the properties for this 
             component instance.
        """
        pass

    def GetPropertyOwner(self, pd):
        """
        GetPropertyOwner(self: ICustomTypeDescriptor, pd: PropertyDescriptor) -> object
        
            Returns an object that contains the property described by the specified property descriptor.
        
            pd: A System.ComponentModel.PropertyDescriptor that represents the property whose owner is to be 
             found.
        
            Returns: An System.Object that represents the owner of the specified property.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDataErrorInfo:
    """ Provides the functionality to offer custom error information that a user interface can bind to. """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an error message indicating what is wrong with this object.

Get: Error(self: IDataErrorInfo) -> str

"""



class IEditableObject:
    """ Provides functionality to commit or rollback changes to an object that is used as a data source. """
    def BeginEdit(self):
        """
        BeginEdit(self: IEditableObject)
            Begins an edit on an object.
        """
        pass

    def CancelEdit(self):
        """
        CancelEdit(self: IEditableObject)
            Discards changes since the last System.ComponentModel.IEditableObject.BeginEdit call.
        """
        pass

    def EndEdit(self):
        """
        EndEdit(self: IEditableObject)
            Pushes changes since the last System.ComponentModel.IEditableObject.BeginEdit or 
             System.ComponentModel.IBindingList.AddNew call into the underlying object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExtenderProvider:
    """ Defines the interface for extending properties to other components in a container. """
    def CanExtend(self, extendee):
        """
        CanExtend(self: IExtenderProvider, extendee: object) -> bool
        
            Specifies whether this object can provide its extender properties to the specified object.
        
            extendee: The System.Object to receive the extender properties.
            Returns: true if this object can provide extender properties to the specified object; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IIntellisenseBuilder:
    """ Provides an interface to facilitate the retrieval of the builder's name and to display the builder. """
    def Show(self, language, value, newValue):
        """
        Show(self: IIntellisenseBuilder, language: str, value: str, newValue: str) -> (bool, str)
        
            Shows the builder.
        
            language: The language service that is calling the builder.
            value: The expression being edited.
            newValue: The new value.
            Returns: true if the value should be replaced with newValue; otherwise, false (if the user cancels, for 
             example).
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a localized name.

Get: Name(self: IIntellisenseBuilder) -> str

"""



class IListSource:
    """ Provides functionality to an object to return a list that can be bound to a data source. """
    def GetList(self):
        """
        GetList(self: IListSource) -> IList
        
            Returns an System.Collections.IList that can be bound to a data source from an object that does 
             not implement an System.Collections.IList itself.
        
            Returns: An System.Collections.IList that can be bound to a data source from the object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ContainsListCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is a collection of System.Collections.IList objects.

Get: ContainsListCollection(self: IListSource) -> bool

"""



class ImmutableObjectAttribute(Attribute, _Attribute):
    """
    Specifies that an object has no subproperties capable of being edited. This class cannot be inherited.
    
    ImmutableObjectAttribute(immutable: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: ImmutableObjectAttribute, obj: object) -> bool
        
            obj: An System.Object to compare with this instance or null.
            Returns: true if obj equals the type and value of this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ImmutableObjectAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.ImmutableObjectAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ImmutableObjectAttribute) -> bool
        
            Indicates whether the value of this instance is the default value.
            Returns: true if this instance is the default attribute for the class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, immutable):
        """ __new__(cls: type, immutable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Immutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the object is immutable.

Get: Immutable(self: ImmutableObjectAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class INestedContainer(IContainer, IDisposable):
    """ Provides functionality for nested containers, which logically contain zero or more other components and are owned by a parent component. """
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the owning component for the nested container.

Get: Owner(self: INestedContainer) -> IComponent

"""



class ISite(IServiceProvider):
    """ Provides functionality required by sites. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component associated with the System.ComponentModel.ISite when implemented by a class.

Get: Component(self: ISite) -> IComponent

"""

    Container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.IContainer associated with the System.ComponentModel.ISite when implemented by a class.

Get: Container(self: ISite) -> IContainer

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the component is in design mode when implemented by a class.

Get: DesignMode(self: ISite) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the component associated with the System.ComponentModel.ISite when implemented by a class.

Get: Name(self: ISite) -> str

Set: Name(self: ISite) = value
"""



class INestedSite(ISite, IServiceProvider):
    """ Provides the ability to retrieve the full nested name of a component. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of the component in this site.

Get: FullName(self: INestedSite) -> str

"""



class InheritanceAttribute(Attribute, _Attribute):
    """
    Indicates whether the component associated with this attribute has been inherited from a base class. This class cannot be inherited.
    
    InheritanceAttribute()
    InheritanceAttribute(inheritanceLevel: InheritanceLevel)
    """
    def Equals(self, value):
        """
        Equals(self: InheritanceAttribute, value: object) -> bool
        
            Override to test for equality.
        
            value: The object to test.
            Returns: true if the object is the same; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: InheritanceAttribute) -> int
        
            Returns the hashcode for this object.
            Returns: A hash code for the current System.ComponentModel.InheritanceAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: InheritanceAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default; otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: InheritanceAttribute) -> str
        
            Converts this attribute to a string.
            Returns: A string that represents this System.ComponentModel.InheritanceAttribute.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, inheritanceLevel=None):
        """
        __new__(cls: type)
        __new__(cls: type, inheritanceLevel: InheritanceLevel)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InheritanceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current inheritance level stored in this attribute.

Get: InheritanceLevel(self: InheritanceAttribute) -> InheritanceLevel

"""


    Default = None
    Inherited = None
    InheritedReadOnly = None
    NotInherited = None


class InheritanceLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers for types of inheritance levels.
    
    enum InheritanceLevel, values: Inherited (1), InheritedReadOnly (2), NotInherited (3)
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

    Inherited = None
    InheritedReadOnly = None
    NotInherited = None
    value__ = None


class InitializationEventAttribute(Attribute, _Attribute):
    """
    Specifies which event is raised on initialization. This class cannot be inherited.
    
    InitializationEventAttribute(eventName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, eventName):
        """ __new__(cls: type, eventName: str) """
        pass

    EventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the initialization event.

Get: EventName(self: InitializationEventAttribute) -> str

"""



class INotifyDataErrorInfo:
    # no doc
    def GetErrors(self, propertyName):
        """ GetErrors(self: INotifyDataErrorInfo, propertyName: str) -> IEnumerable """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasErrors(self: INotifyDataErrorInfo) -> bool

"""


    ErrorsChanged = None


class INotifyPropertyChanged:
    """ Notifies clients that a property value has changed. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PropertyChanged = None


class INotifyPropertyChanging:
    """ Notifies clients that a property value is changing. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PropertyChanging = None


class InstallerTypeAttribute(Attribute, _Attribute):
    """
    Specifies the installer for a type that installs components.
    
    InstallerTypeAttribute(installerType: Type)
    InstallerTypeAttribute(typeName: str)
    """
    def Equals(self, obj):
        """
        Equals(self: InstallerTypeAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.InstallerTypeAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: InstallerTypeAttribute) -> int
        
            Returns the hashcode for this object.
            Returns: A hash code for the current System.ComponentModel.InstallerTypeAttribute.
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
        __new__(cls: type, installerType: Type)
        __new__(cls: type, typeName: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    InstallerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of installer associated with this attribute.

Get: InstallerType(self: InstallerTypeAttribute) -> Type

"""



class InstanceCreationEditor(object):
    """ Creates an instance of a particular type of property from a drop-down box within the System.Windows.Forms.PropertyGrid. """
    def CreateInstance(self, context, instanceType):
        """
        CreateInstance(self: InstanceCreationEditor, context: ITypeDescriptorContext, instanceType: Type) -> object
        
            When overridden in a derived class, returns an instance of the specified type.
        
            context: The context information.
            instanceType: The specified type.
            Returns: An instance of the specified type or null.
        """
        pass

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the specified text.

Get: Text(self: InstanceCreationEditor) -> str

"""



class Int16Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 16-bit signed integer objects to and from other representations.
    
    Int16Converter()
    """

class Int32Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 32-bit signed integer objects to and from other representations.
    
    Int32Converter()
    """

class Int64Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 64-bit signed integer objects to and from various other representations.
    
    Int64Converter()
    """

class InvalidAsynchronousStateException(ArgumentException, ISerializable, _Exception):
    """
    Thrown when a thread on which an operation should execute no longer exists or has no message loop.
    
    InvalidAsynchronousStateException()
    InvalidAsynchronousStateException(message: str)
    InvalidAsynchronousStateException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class InvalidEnumArgumentException(ArgumentException, ISerializable, _Exception):
    """
    The exception thrown when using invalid arguments that are enumerators.
    
    InvalidEnumArgumentException()
    InvalidEnumArgumentException(message: str)
    InvalidEnumArgumentException(message: str, innerException: Exception)
    InvalidEnumArgumentException(argumentName: str, invalidValue: int, enumClass: Type)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, argumentName: str, invalidValue: int, enumClass: Type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IRevertibleChangeTracking(IChangeTracking):
    """ Provides support for rolling back the changes """
    def RejectChanges(self):
        """
        RejectChanges(self: IRevertibleChangeTracking)
                """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISupportInitialize:
    """ Specifies that this object supports a simple, transacted notification for batch initialization. """
    def BeginInit(self):
        """
        BeginInit(self: ISupportInitialize)
            Signals the object that initialization is starting.
        """
        pass

    def EndInit(self):
        """
        EndInit(self: ISupportInitialize)
            Signals the object that initialization is complete.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISupportInitializeNotification(ISupportInitialize):
    """ Allows coordination of initialization for a component and its dependent properties. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component is initialized.

Get: IsInitialized(self: ISupportInitializeNotification) -> bool

"""


    Initialized = None


class ISynchronizeInvoke:
    """ Provides a way to synchronously or asynchronously execute a delegate. """
    def BeginInvoke(self, method, args):
        """
        BeginInvoke(self: ISynchronizeInvoke, method: Delegate, args: Array[object]) -> IAsyncResult
        
            Asynchronously executes the delegate on the thread that created this object.
        
            method: A System.Delegate to a method that takes parameters of the same number and type that are 
             contained in args.
        
            args: An array of type System.Object to pass as arguments to the given method. This can be null if no 
             arguments are needed.
        
            Returns: An System.IAsyncResult interface that represents the asynchronous operation started by calling 
             this method.
        """
        pass

    def EndInvoke(self, result):
        """
        EndInvoke(self: ISynchronizeInvoke, result: IAsyncResult) -> object
        
            Waits until the process started by calling 
             System.ComponentModel.ISynchronizeInvoke.BeginInvoke(System.Delegate,System.Object[]) completes, 
             and then returns the value generated by the process.
        
        
            result: An System.IAsyncResult interface that represents the asynchronous operation started by calling 
             System.ComponentModel.ISynchronizeInvoke.BeginInvoke(System.Delegate,System.Object[]).
        
            Returns: An System.Object that represents the return value generated by the asynchronous operation.
        """
        pass

    def Invoke(self, method, args):
        """
        Invoke(self: ISynchronizeInvoke, method: Delegate, args: Array[object]) -> object
        
            Synchronously executes the delegate on the thread that created this object and marshals the call 
             to the creating thread.
        
        
            method: A System.Delegate that contains a method to call, in the context of the thread for the control.
            args: An array of type System.Object that represents the arguments to pass to the given method. This 
             can be null if no arguments are needed.
        
            Returns: An System.Object that represents the return value from the delegate being invoked, or null if 
             the delegate has no return value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    InvokeRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the caller must call System.ComponentModel.ISynchronizeInvoke.Invoke(System.Delegate,System.Object[]) when calling an object that implements this interface.

Get: InvokeRequired(self: ISynchronizeInvoke) -> bool

"""



class ITypeDescriptorContext(IServiceProvider):
    """ Provides contextual information about a component, such as its container and property descriptor. """
    def OnComponentChanged(self):
        """
        OnComponentChanged(self: ITypeDescriptorContext)
            Raises the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event.
        """
        pass

    def OnComponentChanging(self):
        """
        OnComponentChanging(self: ITypeDescriptorContext) -> bool
        
            Raises the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event.
            Returns: true if this object can be changed; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container representing this System.ComponentModel.TypeDescriptor request.

Get: Container(self: ITypeDescriptorContext) -> IContainer

"""

    Instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that is connected with this type descriptor request.

Get: Instance(self: ITypeDescriptorContext) -> object

"""

    PropertyDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.PropertyDescriptor that is associated with the given context item.

Get: PropertyDescriptor(self: ITypeDescriptorContext) -> PropertyDescriptor

"""



class ITypedList:
    """ Provides functionality to discover the schema for a bindable list, where the properties available for binding differ from the public properties of the object to bind to. """
    def GetItemProperties(self, listAccessors):
        """
        GetItemProperties(self: ITypedList, listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection
        
            Returns the System.ComponentModel.PropertyDescriptorCollection that represents the properties on 
             each item used to bind data.
        
        
            listAccessors: An array of System.ComponentModel.PropertyDescriptor objects to find in the collection as 
             bindable. This can be null.
        
            Returns: The System.ComponentModel.PropertyDescriptorCollection that represents the properties on each 
             item used to bind data.
        """
        pass

    def GetListName(self, listAccessors):
        """
        GetListName(self: ITypedList, listAccessors: Array[PropertyDescriptor]) -> str
        
            Returns the name of the list.
        
            listAccessors: An array of System.ComponentModel.PropertyDescriptor objects, for which the list name is 
             returned. This can be null.
        
            Returns: The name of the list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class License(object, IDisposable):
    """ Provides the abstract base class for all licenses. A license is granted to a specific instance of a component. """
    def Dispose(self):
        """
        Dispose(self: License)
            When overridden in a derived class, disposes of the resources used by the license.
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

    LicenseKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the license key granted to this component.

Get: LicenseKey(self: License) -> str

"""



class LicenseContext(object, IServiceProvider):
    """
    Specifies when you can use a licensed object and provides a way of obtaining additional services needed to support licenses running within its domain.
    
    LicenseContext()
    """
    def GetSavedLicenseKey(self, type, resourceAssembly):
        """
        GetSavedLicenseKey(self: LicenseContext, type: Type, resourceAssembly: Assembly) -> str
        
            When overridden in a derived class, returns a saved license key for the specified type, from the 
             specified resource assembly.
        
        
            type: A System.Type that represents the type of component.
            resourceAssembly: An System.Reflection.Assembly with the license key.
            Returns: The System.ComponentModel.License.LicenseKey for the specified type. This method returns null 
             unless you override it.
        """
        pass

    def GetService(self, type):
        """
        GetService(self: LicenseContext, type: Type) -> object
        
            Gets the requested service, if it is available.
        
            type: The type of service to retrieve.
            Returns: An instance of the service, or null if the service cannot be found.
        """
        pass

    def SetSavedLicenseKey(self, type, key):
        """
        SetSavedLicenseKey(self: LicenseContext, type: Type, key: str)
            When overridden in a derived class, sets a license key for the specified type.
        
            type: A System.Type that represents the component associated with the license key.
            key: The System.ComponentModel.License.LicenseKey to save for the type of component.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UsageMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value that specifies when you can use a license.

Get: UsageMode(self: LicenseContext) -> LicenseUsageMode

"""



class LicenseException(SystemException, ISerializable, _Exception):
    """
    Represents the exception thrown when a component cannot be granted a license.
    
    LicenseException(type: Type)
    LicenseException(type: Type, instance: object)
    LicenseException(type: Type, instance: object, message: str)
    LicenseException(type: Type, instance: object, message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: LicenseException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo with information about the exception.
        
            info: The System.Runtime.Serialization.SerializationInfo to be used for deserialization.
            context: The destination to be used for deserialization.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, instance=None, message=None, innerException=None):
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, type: Type, instance: object)
        __new__(cls: type, type: Type, instance: object, message: str)
        __new__(cls: type, type: Type, instance: object, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LicensedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the component that was not granted a license.

Get: LicensedType(self: LicenseException) -> Type

"""



class LicenseManager(object):
    """ Provides properties and methods to add a license to a component and to manage a System.ComponentModel.LicenseProvider. This class cannot be inherited. """
    @staticmethod
    def CreateWithContext(type, creationContext, args=None):
        """
        CreateWithContext(type: Type, creationContext: LicenseContext, args: Array[object]) -> object
        
            Creates an instance of the specified type with the specified arguments, given a context in which 
             you can use the licensed instance.
        
        
            type: A System.Type that represents the type to create.
            creationContext: A System.ComponentModel.LicenseContext that specifies when you can use the licensed instance.
            args: An array of type System.Object that represents the arguments for the type.
            Returns: An instance of the specified type with the given array of arguments.
        CreateWithContext(type: Type, creationContext: LicenseContext) -> object
        
            Creates an instance of the specified type, given a context in which you can use the licensed 
             instance.
        
        
            type: A System.Type that represents the type to create.
            creationContext: A System.ComponentModel.LicenseContext that specifies when you can use the licensed instance.
            Returns: An instance of the specified type.
        """
        pass

    @staticmethod
    def IsLicensed(type):
        """
        IsLicensed(type: Type) -> bool
        
            Returns whether the given type has a valid license.
        
            type: The System.Type to find a valid license for.
            Returns: true if the given type is licensed; otherwise, false.
        """
        pass

    @staticmethod
    def IsValid(type, instance=None, license=None):
        """
        IsValid(type: Type, instance: object) -> (bool, License)
        
            Determines whether a valid license can be granted for the specified instance of the type. This 
             method creates a valid System.ComponentModel.License.
        
        
            type: A System.Type that represents the type of object that requests the license.
            instance: An object of the specified type or a type derived from the specified type.
            Returns: true if a valid System.ComponentModel.License can be granted; otherwise, false.
        IsValid(type: Type) -> bool
        
            Determines whether a valid license can be granted for the specified type.
        
            type: A System.Type that represents the type of object that requests the System.ComponentModel.License.
            Returns: true if a valid license can be granted; otherwise, false.
        """
        pass

    @staticmethod
    def LockContext(contextUser):
        """
        LockContext(contextUser: object)
            Prevents changes being made to the current System.ComponentModel.LicenseContext of the given 
             object.
        
        
            contextUser: The object whose current context you want to lock.
        """
        pass

    @staticmethod
    def UnlockContext(contextUser):
        """
        UnlockContext(contextUser: object)
            Allows changes to be made to the current System.ComponentModel.LicenseContext of the given 
             object.
        
        
            contextUser: The object whose current context you want to unlock.
        """
        pass

    @staticmethod
    def Validate(type, instance=None):
        """
        Validate(type: Type, instance: object) -> License
        
            Determines whether a license can be granted for the instance of the specified type.
        
            type: A System.Type that represents the type of object that requests the license.
            instance: An System.Object of the specified type or a type derived from the specified type.
            Returns: A valid System.ComponentModel.License.
        Validate(type: Type)
            Determines whether a license can be granted for the specified type.
        
            type: A System.Type that represents the type of object that requests the license.
        """
        pass

    CurrentContext = None
    UsageMode = None


class LicenseProvider(object):
    """ Provides the abstract base class for implementing a license provider. """
    def GetLicense(self, context, type, instance, allowExceptions):
        """
        GetLicense(self: LicenseProvider, context: LicenseContext, type: Type, instance: object, allowExceptions: bool) -> License
        
            When overridden in a derived class, gets a license for an instance or type of component, when 
             given a context and whether the denial of a license throws an exception.
        
        
            context: A System.ComponentModel.LicenseContext that specifies where you can use the licensed object.
            type: A System.Type that represents the component requesting the license.
            instance: An object that is requesting the license.
            allowExceptions: true if a System.ComponentModel.LicenseException should be thrown when the component cannot be 
             granted a license; otherwise, false.
        
            Returns: A valid System.ComponentModel.License.
        """
        pass


class LicenseProviderAttribute(Attribute, _Attribute):
    """
    Specifies the System.ComponentModel.LicenseProvider to use with a class. This class cannot be inherited.
    
    LicenseProviderAttribute()
    LicenseProviderAttribute(typeName: str)
    LicenseProviderAttribute(type: Type)
    """
    def Equals(self, value):
        """
        Equals(self: LicenseProviderAttribute, value: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            value: Another object to compare to.
            Returns: true if value is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LicenseProviderAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.LicenseProviderAttribute.
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
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    LicenseProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the license provider that must be used with the associated class.

Get: LicenseProvider(self: LicenseProviderAttribute) -> Type

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates a unique ID for this attribute type.

Get: TypeId(self: LicenseProviderAttribute) -> object

"""


    Default = None


class LicenseUsageMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies when the System.ComponentModel.License can be used.
    
    enum LicenseUsageMode, values: Designtime (1), Runtime (0)
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

    Designtime = None
    Runtime = None
    value__ = None


class LicFileLicenseProvider(LicenseProvider):
    """
    Provides an implementation of a System.ComponentModel.LicenseProvider. The provider works in a similar fashion to the Microsoft .NET Framework standard licensing model.
    
    LicFileLicenseProvider()
    """
    def GetKey(self, *args): #cannot find CLR method
        """
        GetKey(self: LicFileLicenseProvider, type: Type) -> str
        
            Returns a key for the specified type.
        
            type: The object type to return the key.
            Returns: A confirmation that the type parameter is licensed.
        """
        pass

    def GetLicense(self, context, type, instance, allowExceptions):
        """
        GetLicense(self: LicFileLicenseProvider, context: LicenseContext, type: Type, instance: object, allowExceptions: bool) -> License
        
            Returns a license for the instance of the component, if one is available.
        
            context: A System.ComponentModel.LicenseContext that specifies where you can use the licensed object.
            type: A System.Type that represents the component requesting the System.ComponentModel.License.
            instance: An object that requests the System.ComponentModel.License.
            allowExceptions: true if a System.ComponentModel.LicenseException should be thrown when a component cannot be 
             granted a license; otherwise, false.
        
            Returns: A valid System.ComponentModel.License. If this method cannot find a valid 
             System.ComponentModel.License or a valid context parameter, it returns null.
        """
        pass

    def IsKeyValid(self, *args): #cannot find CLR method
        """
        IsKeyValid(self: LicFileLicenseProvider, key: str, type: Type) -> bool
        
            Determines whether the key that the 
             System.ComponentModel.LicFileLicenseProvider.GetLicense(System.ComponentModel.LicenseContext,Syst
             em.Type,System.Object,System.Boolean) method retrieves is valid for the specified type.
        
        
            key: The System.ComponentModel.License.LicenseKey to check.
            type: A System.Type that represents the component requesting the System.ComponentModel.License.
            Returns: true if the key is a valid System.ComponentModel.License.LicenseKey for the specified type; 
             otherwise, false.
        """
        pass


class ListBindableAttribute(Attribute, _Attribute):
    """
    Specifies that a list can be used as a data source. A visual designer should use this attribute to determine whether to display a particular list in a data-binding picker. This class cannot be inherited.
    
    ListBindableAttribute(listBindable: bool)
    ListBindableAttribute(flags: BindableSupport)
    """
    def Equals(self, obj):
        """
        Equals(self: ListBindableAttribute, obj: object) -> bool
        
            Returns whether the object passed is equal to this System.ComponentModel.ListBindableAttribute.
        
            obj: The object to test equality with.
            Returns: true if the object passed is equal to this System.ComponentModel.ListBindableAttribute; 
             otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ListBindableAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.ListBindableAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ListBindableAttribute) -> bool
        
            Returns whether System.ComponentModel.ListBindableAttribute.ListBindable is set to the default 
             value.
        
            Returns: true if System.ComponentModel.ListBindableAttribute.ListBindable is set to the default value; 
             otherwise, false.
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
        __new__(cls: type, listBindable: bool)
        __new__(cls: type, flags: BindableSupport)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ListBindable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the list is bindable.

Get: ListBindable(self: ListBindableAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class ListChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.IBindingList.ListChanged event.
    
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int)
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor)
    ListChangedEventArgs(listChangedType: ListChangedType, propDesc: PropertyDescriptor)
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int, oldIndex: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, listChangedType, *__args):
        """
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int)
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor)
        __new__(cls: type, listChangedType: ListChangedType, propDesc: PropertyDescriptor)
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int, oldIndex: int)
        """
        pass

    ListChangedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of change.

Get: ListChangedType(self: ListChangedEventArgs) -> ListChangedType

"""

    NewIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the item affected by the change.

Get: NewIndex(self: ListChangedEventArgs) -> int

"""

    OldIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the old index of an item that has been moved.

Get: OldIndex(self: ListChangedEventArgs) -> int

"""

    PropertyDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.ComponentModel.PropertyDescriptor that was added, changed, or deleted.

Get: PropertyDescriptor(self: ListChangedEventArgs) -> PropertyDescriptor

"""



class ListChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.IBindingList.ListChanged event of the System.ComponentModel.IBindingList class.
    
    ListChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ListChangedEventHandler, sender: object, e: ListChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ListChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ListChangedEventHandler, sender: object, e: ListChangedEventArgs) """
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


class ListChangedType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the list changed.
    
    enum ListChangedType, values: ItemAdded (1), ItemChanged (4), ItemDeleted (2), ItemMoved (3), PropertyDescriptorAdded (5), PropertyDescriptorChanged (7), PropertyDescriptorDeleted (6), Reset (0)
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

    ItemAdded = None
    ItemChanged = None
    ItemDeleted = None
    ItemMoved = None
    PropertyDescriptorAdded = None
    PropertyDescriptorChanged = None
    PropertyDescriptorDeleted = None
    Reset = None
    value__ = None


class ListSortDescription(object):
    """
    Provides a description of the sort operation applied to a data source.
    
    ListSortDescription(property: PropertyDescriptor, direction: ListSortDirection)
    """
    @staticmethod # known case of __new__
    def __new__(self, property, direction):
        """ __new__(cls: type, property: PropertyDescriptor, direction: ListSortDirection) """
        pass

    PropertyDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the abstract description of a class property associated with this System.ComponentModel.ListSortDescription

Get: PropertyDescriptor(self: ListSortDescription) -> PropertyDescriptor

Set: PropertyDescriptor(self: ListSortDescription) = value
"""

    SortDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the direction of the sort operation associated with this System.ComponentModel.ListSortDescription.

Get: SortDirection(self: ListSortDescription) -> ListSortDirection

Set: SortDirection(self: ListSortDescription) = value
"""



class ListSortDescriptionCollection(object, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.ComponentModel.ListSortDescription objects.
    
    ListSortDescriptionCollection()
    ListSortDescriptionCollection(sorts: Array[ListSortDescription])
    """
    def Contains(self, value):
        """
        Contains(self: ListSortDescriptionCollection, value: object) -> bool
        
            Determines if the System.ComponentModel.ListSortDescriptionCollection contains a specific value.
        
            value: The System.Object to locate in the collection.
            Returns: true if the System.Object is found in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ListSortDescriptionCollection, array: Array, index: int)
            Copies the contents of the collection to the specified array, starting at the specified 
             destination array index.
        
        
            array: The destination array for the items copied from the collection.
            index: The index of the destination array at which copying begins.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ListSortDescriptionCollection, value: object) -> int
        
            Returns the index of the specified item in the collection.
        
            value: The System.Object to locate in the collection.
            Returns: The index of value if found in the list; otherwise, -1.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sorts=None):
        """
        __new__(cls: type)
        __new__(cls: type, sorts: Array[ListSortDescription])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the collection.

Get: Count(self: ListSortDescriptionCollection) -> int

"""



class ListSortDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the direction of a sort operation.
    
    enum ListSortDirection, values: Ascending (0), Descending (1)
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

    Ascending = None
    Descending = None
    value__ = None


class LocalizableAttribute(Attribute, _Attribute):
    """
    Specifies whether a property should be localized. This class cannot be inherited.
    
    LocalizableAttribute(isLocalizable: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: LocalizableAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.LocalizableAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LocalizableAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.LocalizableAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: LocalizableAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isLocalizable):
        """ __new__(cls: type, isLocalizable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsLocalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property should be localized.

Get: IsLocalizable(self: LocalizableAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class LookupBindingPropertiesAttribute(Attribute, _Attribute):
    """
    Specifies the properties that support lookup-based binding. This class cannot be inherited.
    
    LookupBindingPropertiesAttribute()
    LookupBindingPropertiesAttribute(dataSource: str, displayMember: str, valueMember: str, lookupMember: str)
    """
    def Equals(self, obj):
        """
        Equals(self: LookupBindingPropertiesAttribute, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.ComponentModel.LookupBindingPropertiesAttribute instance.
        
        
            obj: The System.Object to compare with the current 
             System.ComponentModel.LookupBindingPropertiesAttribute instance
        
            Returns: true if the object is equal to the current instance; otherwise, false, indicating they are not 
             equal.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LookupBindingPropertiesAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.LookupBindingPropertiesAttribute.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dataSource=None, displayMember=None, valueMember=None, lookupMember=None):
        """
        __new__(cls: type)
        __new__(cls: type, dataSource: str, displayMember: str, valueMember: str, lookupMember: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the data source property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.

Get: DataSource(self: LookupBindingPropertiesAttribute) -> str

"""

    DisplayMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the display member property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.

Get: DisplayMember(self: LookupBindingPropertiesAttribute) -> str

"""

    LookupMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the lookup member for the component to which this attribute is bound.

Get: LookupMember(self: LookupBindingPropertiesAttribute) -> str

"""

    ValueMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the value member property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.

Get: ValueMember(self: LookupBindingPropertiesAttribute) -> str

"""


    Default = None


class MarshalByValueComponent(object, IComponent, IDisposable, IServiceProvider):
    """
    Implements System.ComponentModel.IComponent and provides the base implementation for remotable components that are marshaled by value (a copy of the serialized object is passed).
    
    MarshalByValueComponent()
    """
    def Dispose(self):
        """
        Dispose(self: MarshalByValueComponent)
            Releases all resources used by the System.ComponentModel.MarshalByValueComponent.
        """
        pass

    def GetService(self, service):
        """
        GetService(self: MarshalByValueComponent, service: Type) -> object
        
            Gets the implementer of the System.IServiceProvider.
        
            service: A System.Type that represents the type of service you want.
            Returns: An System.Object that represents the implementer of the System.IServiceProvider.
        """
        pass

    def ToString(self):
        """
        ToString(self: MarshalByValueComponent) -> str
        
            Returns a System.String containing the name of the System.ComponentModel.Component, if any. This 
             method should not be overridden.
        
            Returns: A System.String containing the name of the System.ComponentModel.Component, if any.null if the 
             System.ComponentModel.Component is unnamed.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    Container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the container for the component.

Get: Container(self: MarshalByValueComponent) -> IContainer

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component is currently in design mode.

Get: DesignMode(self: MarshalByValueComponent) -> bool

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this component.

"""

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the site of the component.

Get: Site(self: MarshalByValueComponent) -> ISite

Set: Site(self: MarshalByValueComponent) = value
"""


    Disposed = None


class MaskedTextProvider(object, ICloneable):
    """
    Represents a mask-parsing service that can be used by any number of controls that support masking, such as the System.Windows.Forms.MaskedTextBox control.
    
    MaskedTextProvider(mask: str)
    MaskedTextProvider(mask: str, restrictToAscii: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo)
    MaskedTextProvider(mask: str, culture: CultureInfo, restrictToAscii: bool)
    MaskedTextProvider(mask: str, passwordChar: Char, allowPromptAsInput: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo, passwordChar: Char, allowPromptAsInput: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo, allowPromptAsInput: bool, promptChar: Char, passwordChar: Char, restrictToAscii: bool)
    """
    def Add(self, input, testPosition=None, resultHint=None):
        """
        Add(self: MaskedTextProvider, input: str) -> bool
        
            Adds the characters in the specified input string to the end of the formatted string.
        
            input: A System.String containing character values to be appended to the formatted string.
            Returns: true if all the characters from the input string were added successfully; otherwise false to 
             indicate that no characters were added.
        
        Add(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        
            Adds the characters in the specified input string to the end of the formatted string, and then 
             outputs position and descriptive information.
        
        
            input: A System.String containing character values to be appended to the formatted string.
            Returns: true if all the characters from the input string were added successfully; otherwise false to 
             indicate that no characters were added.
        
        Add(self: MaskedTextProvider, input: Char) -> bool
        
            Adds the specified input character to the end of the formatted string.
        
            input: A System.Char value to be appended to the formatted string.
            Returns: true if the input character was added successfully; otherwise false.
        Add(self: MaskedTextProvider, input: Char) -> (bool, int, MaskedTextResultHint)
        
            Adds the specified input character to the end of the formatted string, and then outputs position 
             and descriptive information.
        
        
            input: A System.Char value to be appended to the formatted string.
            Returns: true if the input character was added successfully; otherwise false.
        """
        pass

    def Clear(self, resultHint=None):
        """
        Clear(self: MaskedTextProvider) -> MaskedTextResultHint
        
            Clears all the editable input characters from the formatted string, replacing them with prompt 
             characters, and then outputs descriptive information.
        
        Clear(self: MaskedTextProvider)
            Clears all the editable input characters from the formatted string, replacing them with prompt 
             characters.
        """
        pass

    def Clone(self):
        """
        Clone(self: MaskedTextProvider) -> object
        
            Creates a copy of the current System.ComponentModel.MaskedTextProvider.
            Returns: The System.ComponentModel.MaskedTextProvider object this method creates, cast as an object.
        """
        pass

    def FindAssignedEditPositionFrom(self, position, direction):
        """
        FindAssignedEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int
        
            Returns the position of the first assigned editable position after the specified position using 
             the specified search direction.
        
        
            position: The zero-based position in the formatted string to start the search.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first assigned 
             editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindAssignedEditPositionInRange(self, startPosition, endPosition, direction):
        """
        FindAssignedEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int
        
            Returns the position of the first assigned editable position between the specified positions 
             using the specified search direction.
        
        
            startPosition: The zero-based position in the formatted string where the search starts.
            endPosition: The zero-based position in the formatted string where the search ends.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first assigned 
             editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindEditPositionFrom(self, position, direction):
        """
        FindEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int
        
            Returns the position of the first editable position after the specified position using the 
             specified search direction.
        
        
            position: The zero-based position in the formatted string to start the search.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first editable 
             position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindEditPositionInRange(self, startPosition, endPosition, direction):
        """
        FindEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int
        
            Returns the position of the first editable position between the specified positions using the 
             specified search direction.
        
        
            startPosition: The zero-based position in the formatted string where the search starts.
            endPosition: The zero-based position in the formatted string where the search ends.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first editable 
             position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindNonEditPositionFrom(self, position, direction):
        """
        FindNonEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int
        
            Returns the position of the first non-editable position after the specified position using the 
             specified search direction.
        
        
            position: The zero-based position in the formatted string to start the search.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first literal 
             position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindNonEditPositionInRange(self, startPosition, endPosition, direction):
        """
        FindNonEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int
        
            Returns the position of the first non-editable position between the specified positions using 
             the specified search direction.
        
        
            startPosition: The zero-based position in the formatted string where the search starts.
            endPosition: The zero-based position in the formatted string where the search ends.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first literal 
             position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindUnassignedEditPositionFrom(self, position, direction):
        """
        FindUnassignedEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int
        
            Returns the position of the first unassigned editable position after the specified position 
             using the specified search direction.
        
        
            position: The zero-based position in the formatted string to start the search.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first unassigned 
             editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    def FindUnassignedEditPositionInRange(self, startPosition, endPosition, direction):
        """
        FindUnassignedEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int
        
            Returns the position of the first unassigned editable position between the specified positions 
             using the specified search direction.
        
        
            startPosition: The zero-based position in the formatted string where the search starts.
            endPosition: The zero-based position in the formatted string where the search ends.
            direction: A System.Boolean indicating the search direction; either true to search forward or false to 
             search backward.
        
            Returns: If successful, an System.Int32 representing the zero-based position of the first unassigned 
             editable position encountered; otherwise System.ComponentModel.MaskedTextProvider.InvalidIndex.
        """
        pass

    @staticmethod
    def GetOperationResultFromHint(hint):
        """
        GetOperationResultFromHint(hint: MaskedTextResultHint) -> bool
        
            Determines whether the specified System.ComponentModel.MaskedTextResultHint denotes success or 
             failure.
        
        
            hint: A System.ComponentModel.MaskedTextResultHint value typically obtained as an output parameter 
             from a previous operation.
        
            Returns: true if the specified System.ComponentModel.MaskedTextResultHint value represents a success; 
             otherwise, false if it represents failure.
        """
        pass

    def InsertAt(self, input, position, testPosition=None, resultHint=None):
        """
        InsertAt(self: MaskedTextProvider, input: str, position: int) -> bool
        
            Inserts the specified string at a specified position within the formatted string.
        
            input: The System.String to be inserted.
            position: The zero-based position in the formatted string to insert the input string.
            Returns: true if the insertion was successful; otherwise, false.
        InsertAt(self: MaskedTextProvider, input: str, position: int) -> (bool, int, MaskedTextResultHint)
        
            Inserts the specified string at a specified position within the formatted string, returning the 
             last insertion position and the status of the operation.
        
        
            input: The System.String to be inserted.
            position: The zero-based position in the formatted string to insert the input string.
            Returns: true if the insertion was successful; otherwise, false.
        InsertAt(self: MaskedTextProvider, input: Char, position: int) -> bool
        
            Inserts the specified character at the specified position within the formatted string.
        
            input: The System.Char to be inserted.
            position: The zero-based position in the formatted string to insert the character.
            Returns: true if the insertion was successful; otherwise, false.
        InsertAt(self: MaskedTextProvider, input: Char, position: int) -> (bool, int, MaskedTextResultHint)
        
            Inserts the specified character at the specified position within the formatted string, returning 
             the last insertion position and the status of the operation.
        
        
            input: The System.Char to be inserted.
            position: The zero-based position in the formatted string to insert the character.
            Returns: true if the insertion was successful; otherwise, false.
        """
        pass

    def IsAvailablePosition(self, position):
        """
        IsAvailablePosition(self: MaskedTextProvider, position: int) -> bool
        
            Determines whether the specified position is available for assignment.
        
            position: The zero-based position in the mask to test.
            Returns: true if the specified position in the formatted string is editable and has not been assigned to 
             yet; otherwise false.
        """
        pass

    def IsEditPosition(self, position):
        """
        IsEditPosition(self: MaskedTextProvider, position: int) -> bool
        
            Determines whether the specified position is editable.
        
            position: The zero-based position in the mask to test.
            Returns: true if the specified position in the formatted string is editable; otherwise false.
        """
        pass

    @staticmethod
    def IsValidInputChar(c):
        """
        IsValidInputChar(c: Char) -> bool
        
            Determines whether the specified character is a valid input character.
        
            c: The System.Char value to test.
            Returns: true if the specified character contains a valid input value; otherwise false.
        """
        pass

    @staticmethod
    def IsValidMaskChar(c):
        """
        IsValidMaskChar(c: Char) -> bool
        
            Determines whether the specified character is a valid mask character.
        
            c: The System.Char value to test.
            Returns: true if the specified character contains a valid mask value; otherwise false.
        """
        pass

    @staticmethod
    def IsValidPasswordChar(c):
        """
        IsValidPasswordChar(c: Char) -> bool
        
            Determines whether the specified character is a valid password character.
        
            c: The System.Char value to test.
            Returns: true if the specified character contains a valid password value; otherwise false.
        """
        pass

    def Remove(self, testPosition=None, resultHint=None):
        """
        Remove(self: MaskedTextProvider) -> (bool, int, MaskedTextResultHint)
        
            Removes the last assigned character from the formatted string, and then outputs the removal 
             position and descriptive information.
        
            Returns: true if the character was successfully removed; otherwise, false.
        Remove(self: MaskedTextProvider) -> bool
        
            Removes the last assigned character from the formatted string.
            Returns: true if the character was successfully removed; otherwise, false.
        """
        pass

    def RemoveAt(self, *__args):
        """
        RemoveAt(self: MaskedTextProvider, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        
            Removes the assigned characters between the specified positions from the formatted string, and 
             then outputs the removal position and descriptive information.
        
        
            startPosition: The zero-based index of the first assigned character to remove.
            endPosition: The zero-based index of the last assigned character to remove.
            Returns: true if the character was successfully removed; otherwise, false.
        RemoveAt(self: MaskedTextProvider, startPosition: int, endPosition: int) -> bool
        
            Removes the assigned characters between the specified positions from the formatted string.
        
            startPosition: The zero-based index of the first assigned character to remove.
            endPosition: The zero-based index of the last assigned character to remove.
            Returns: true if the character was successfully removed; otherwise, false.
        RemoveAt(self: MaskedTextProvider, position: int) -> bool
        
            Removes the assigned character at the specified position from the formatted string.
        
            position: The zero-based position of the assigned character to remove.
            Returns: true if the character was successfully removed; otherwise, false.
        """
        pass

    def Replace(self, input, *__args):
        """
        Replace(self: MaskedTextProvider, input: str, position: int) -> bool
        
            Replaces a range of editable characters starting at the specified position with the specified 
             string.
        
        
            input: The System.String value used to replace the existing editable characters.
            position: The zero-based position to search for the first editable character to replace.
            Returns: true if all the characters were successfully replaced; otherwise, false.
        Replace(self: MaskedTextProvider, input: str, position: int) -> (bool, int, MaskedTextResultHint)
        
            Replaces a range of editable characters starting at the specified position with the specified 
             string, and then outputs the removal position and descriptive information.
        
        
            input: The System.String value used to replace the existing editable characters.
            position: The zero-based position to search for the first editable character to replace.
            Returns: true if all the characters were successfully replaced; otherwise, false.
        Replace(self: MaskedTextProvider, input: str, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        
            Replaces a range of editable characters between the specified starting and ending positions with 
             the specified string, and then outputs the removal position and descriptive information.
        
        
            input: The System.String value used to replace the existing editable characters.
            startPosition: The zero-based position in the formatted string where the replacement starts.
            endPosition: The zero-based position in the formatted string where the replacement ends.
            Returns: true if all the characters were successfully replaced; otherwise, false.
        Replace(self: MaskedTextProvider, input: Char, position: int) -> bool
        
            Replaces a single character at or beyond the specified position with the specified character 
             value.
        
        
            input: The System.Char value that replaces the existing value.
            position: The zero-based position to search for the first editable character to replace.
            Returns: true if the character was successfully replaced; otherwise, false.
        Replace(self: MaskedTextProvider, input: Char, position: int) -> (bool, int, MaskedTextResultHint)
        
            Replaces a single character at or beyond the specified position with the specified character 
             value, and then outputs the removal position and descriptive information.
        
        
            input: The System.Char value that replaces the existing value.
            position: The zero-based position to search for the first editable character to replace.
            Returns: true if the character was successfully replaced; otherwise, false.
        Replace(self: MaskedTextProvider, input: Char, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        
            Replaces a single character between the specified starting and ending positions with the 
             specified character value, and then outputs the removal position and descriptive information.
        
        
            input: The System.Char value that replaces the existing value.
            startPosition: The zero-based position in the formatted string where the replacement starts.
            endPosition: The zero-based position in the formatted string where the replacement ends.
            Returns: true if the character was successfully replaced; otherwise, false.
        """
        pass

    def Set(self, input, testPosition=None, resultHint=None):
        """
        Set(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        
            Sets the formatted string to the specified input string, and then outputs the removal position 
             and descriptive information.
        
        
            input: The System.String value used to set the formatted string.
            Returns: true if all the characters were successfully set; otherwise, false.
        Set(self: MaskedTextProvider, input: str) -> bool
        
            Sets the formatted string to the specified input string.
        
            input: The System.String value used to set the formatted string.
            Returns: true if all the characters were successfully set; otherwise, false.
        """
        pass

    def ToDisplayString(self):
        """
        ToDisplayString(self: MaskedTextProvider) -> str
        
            Returns the formatted string in a displayable form.
            Returns: The formatted System.String that includes prompts and mask literals.
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: MaskedTextProvider, includePrompt: bool, includeLiterals: bool) -> str
        
            Returns the formatted string, optionally including prompt and literal characters.
        
            includePrompt: true to include prompt characters in the return string; otherwise, false.
            includeLiterals: true to include literal characters in the return string; otherwise, false.
            Returns: The formatted System.String that includes all the assigned character values and optionally 
             includes literals and prompts.
        
        ToString(self: MaskedTextProvider, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int) -> str
        
            Returns a substring of the formatted string, optionally including prompt and literal characters.
        
            includePrompt: true to include prompt characters in the return string; otherwise, false.
            includeLiterals: true to include literal characters in the return string; otherwise, false.
            startPosition: The zero-based position in the formatted string where the output begins.
            length: The number of characters to return.
            Returns: If successful, a substring of the formatted System.String, which includes all the assigned 
             character values and optionally includes literals and prompts; otherwise the System.String.Empty 
             string.
        
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int) -> str
        
            Returns a substring of the formatted string, optionally including prompt, literal, and password 
             characters.
        
        
            ignorePasswordChar: true to return the actual editable characters; otherwise, false to indicate that the 
             System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.
        
            includePrompt: true to include prompt characters in the return string; otherwise, false.
            includeLiterals: true to return literal characters in the return string; otherwise, false.
            startPosition: The zero-based position in the formatted string where the output begins.
            length: The number of characters to return.
            Returns: If successful, a substring of the formatted System.String, which includes all the assigned 
             character values and optionally includes literals, prompts, and password characters; otherwise 
             the System.String.Empty string.
        
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool, startPosition: int, length: int) -> str
        
            Returns a substring of the formatted string, optionally including password characters.
        
            ignorePasswordChar: true to return the actual editable characters; otherwise, false to indicate that the 
             System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.
        
            startPosition: The zero-based position in the formatted string where the output begins.
            length: The number of characters to return.
            Returns: If successful, a substring of the formatted System.String, which includes literals, prompts, and 
             optionally password characters; otherwise the System.String.Empty string.
        
        ToString(self: MaskedTextProvider) -> str
        
            Returns the formatted string that includes all the assigned character values.
            Returns: The formatted System.String that includes all the assigned character values.
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool) -> str
        
            Returns the formatted string, optionally including password characters.
        
            ignorePasswordChar: true to return the actual editable characters; otherwise, false to indicate that the 
             System.ComponentModel.MaskedTextProvider.PasswordChar property is to be honored.
        
            Returns: The formatted System.String that includes literals, prompts, and optionally password characters.
        ToString(self: MaskedTextProvider, startPosition: int, length: int) -> str
        
            Returns a substring of the formatted string.
        
            startPosition: The zero-based position in the formatted string where the output begins.
            length: The number of characters to return.
            Returns: If successful, a substring of the formatted System.String, which includes all the assigned 
             character values; otherwise the System.String.Empty string.
        """
        pass

    def VerifyChar(self, input, position, hint):
        """
        VerifyChar(self: MaskedTextProvider, input: Char, position: int) -> (bool, MaskedTextResultHint)
        
            Tests whether the specified character could be set successfully at the specified position.
        
            input: The System.Char value to test.
            position: The position in the mask to test the input character against.
            Returns: true if the specified character is valid for the specified position; otherwise, false.
        """
        pass

    def VerifyEscapeChar(self, input, position):
        """
        VerifyEscapeChar(self: MaskedTextProvider, input: Char, position: int) -> bool
        
            Tests whether the specified character would be escaped at the specified position.
        
            input: The System.Char value to test.
            position: The position in the mask to test the input character against.
            Returns: true if the specified character would be escaped at the specified position; otherwise, false.
        """
        pass

    def VerifyString(self, input, testPosition=None, resultHint=None):
        """
        VerifyString(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        
            Tests whether the specified string could be set successfully, and then outputs position and 
             descriptive information.
        
        
            input: The System.String value to test.
            Returns: true if the specified string represents valid input; otherwise, false.
        VerifyString(self: MaskedTextProvider, input: str) -> bool
        
            Tests whether the specified string could be set successfully.
        
            input: The System.String value to test.
            Returns: true if the specified string represents valid input; otherwise, false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mask, *__args):
        """
        __new__(cls: type, mask: str)
        __new__(cls: type, mask: str, restrictToAscii: bool)
        __new__(cls: type, mask: str, culture: CultureInfo)
        __new__(cls: type, mask: str, culture: CultureInfo, restrictToAscii: bool)
        __new__(cls: type, mask: str, passwordChar: Char, allowPromptAsInput: bool)
        __new__(cls: type, mask: str, culture: CultureInfo, passwordChar: Char, allowPromptAsInput: bool)
        __new__(cls: type, mask: str, culture: CultureInfo, allowPromptAsInput: bool, promptChar: Char, passwordChar: Char, restrictToAscii: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllowPromptAsInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the prompt character should be treated as a valid input character or not.

Get: AllowPromptAsInput(self: MaskedTextProvider) -> bool

"""

    AsciiOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the mask accepts characters outside of the ASCII character set.

Get: AsciiOnly(self: MaskedTextProvider) -> bool

"""

    AssignedEditPositionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of editable character positions that have already been successfully assigned an input value.

Get: AssignedEditPositionCount(self: MaskedTextProvider) -> int

"""

    AvailableEditPositionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of editable character positions in the input mask that have not yet been assigned an input value.

Get: AvailableEditPositionCount(self: MaskedTextProvider) -> int

"""

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the culture that determines the value of the localizable separators and placeholders in the input mask.

Get: Culture(self: MaskedTextProvider) -> CultureInfo

"""

    EditPositionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of editable positions in the formatted string.

Get: EditPositionCount(self: MaskedTextProvider) -> int

"""

    EditPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a newly created enumerator for the editable positions in the formatted string.

Get: EditPositions(self: MaskedTextProvider) -> IEnumerator

"""

    IncludeLiterals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether literal characters in the input mask should be included in the formatted string.

Get: IncludeLiterals(self: MaskedTextProvider) -> bool

Set: IncludeLiterals(self: MaskedTextProvider) = value
"""

    IncludePrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether System.Windows.Forms.MaskedTextBox.PromptChar is used to represent the absence of user input when displaying the formatted string.

Get: IncludePrompt(self: MaskedTextProvider) -> bool

Set: IncludePrompt(self: MaskedTextProvider) = value
"""

    IsPassword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines whether password protection should be applied to the formatted string.

Get: IsPassword(self: MaskedTextProvider) -> bool

Set: IsPassword(self: MaskedTextProvider) = value
"""

    LastAssignedPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index in the mask of the rightmost input character that has been assigned to the mask.

Get: LastAssignedPosition(self: MaskedTextProvider) -> int

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the mask, absent any mask modifier characters.

Get: Length(self: MaskedTextProvider) -> int

"""

    Mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input mask.

Get: Mask(self: MaskedTextProvider) -> str

"""

    MaskCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether all required inputs have been entered into the formatted string.

Get: MaskCompleted(self: MaskedTextProvider) -> bool

"""

    MaskFull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether all required and optional inputs have been entered into the formatted string.

Get: MaskFull(self: MaskedTextProvider) -> bool

"""

    PasswordChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character to be substituted for the actual input characters.

Get: PasswordChar(self: MaskedTextProvider) -> Char

Set: PasswordChar(self: MaskedTextProvider) = value
"""

    PromptChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character used to represent the absence of user input for all available edit positions.

Get: PromptChar(self: MaskedTextProvider) -> Char

Set: PromptChar(self: MaskedTextProvider) = value
"""

    ResetOnPrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines how an input character that matches the prompt character should be handled.

Get: ResetOnPrompt(self: MaskedTextProvider) -> bool

Set: ResetOnPrompt(self: MaskedTextProvider) = value
"""

    ResetOnSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines how a space input character should be handled.

Get: ResetOnSpace(self: MaskedTextProvider) -> bool

Set: ResetOnSpace(self: MaskedTextProvider) = value
"""

    SkipLiterals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether literal character positions in the mask can be overwritten by their same values.

Get: SkipLiterals(self: MaskedTextProvider) -> bool

Set: SkipLiterals(self: MaskedTextProvider) = value
"""


    DefaultPasswordChar = None
    InvalidIndex = -1


class MaskedTextResultHint(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies values that succinctly describe the results of a masked text parsing operation.
    
    enum MaskedTextResultHint, values: AlphanumericCharacterExpected (-2), AsciiCharacterExpected (-1), CharacterEscaped (1), DigitExpected (-3), InvalidInput (-51), LetterExpected (-4), NoEffect (2), NonEditPosition (-54), PositionOutOfRange (-55), PromptCharNotAllowed (-52), SideEffect (3), SignedDigitExpected (-5), Success (4), UnavailableEditPosition (-53), Unknown (0)
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

    AlphanumericCharacterExpected = None
    AsciiCharacterExpected = None
    CharacterEscaped = None
    DigitExpected = None
    InvalidInput = None
    LetterExpected = None
    NoEffect = None
    NonEditPosition = None
    PositionOutOfRange = None
    PromptCharNotAllowed = None
    SideEffect = None
    SignedDigitExpected = None
    Success = None
    UnavailableEditPosition = None
    Unknown = None
    value__ = None


class MergablePropertyAttribute(Attribute, _Attribute):
    """
    Specifies that this property can be combined with properties belonging to other objects in a Properties window.
    
    MergablePropertyAttribute(allowMerge: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: MergablePropertyAttribute, obj: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            obj: Another object to compare to.
            Returns: true if obj is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MergablePropertyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.MergablePropertyAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: MergablePropertyAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allowMerge):
        """ __new__(cls: type, allowMerge: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AllowMerge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this property can be combined with properties belonging to other objects in a Properties window.

Get: AllowMerge(self: MergablePropertyAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class MultilineStringConverter(TypeConverter):
    """
    Provides a type converter to convert multiline strings to a simple string.
    
    MultilineStringConverter()
    """
    def ConvertTo(self, *__args):
        """
        ConvertTo(self: MultilineStringConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.
            culture: A System.Globalization.CultureInfo. If null is passed, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: MultilineStringConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a collection of properties for the type of array specified by the value parameter, using 
             the specified context and attributes.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.
            value: An System.Object that specifies the type of array for which to get properties.
            attributes: An array of type System.Attribute that is used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: MultilineStringConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether this object supports properties, using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.
            Returns: true if erload:System.ComponentModel.MultilineStringConverter.GetProperties should be called to 
             find the properties of this object; otherwise, false.
        """
        pass


class NestedContainer(Container, IContainer, IDisposable, INestedContainer):
    """
    Provides the base implementation for the System.ComponentModel.INestedContainer interface, which enables containers to have an owning component.
    
    NestedContainer(owner: IComponent)
    """
    def CreateSite(self, *args): #cannot find CLR method
        """
        CreateSite(self: NestedContainer, component: IComponent, name: str) -> ISite
        
            Creates a site for the component within the container.
        
            component: The System.ComponentModel.IComponent to create a site for.
            name: The name to assign to component, or null to skip the name assignment.
            Returns: The newly created System.ComponentModel.ISite.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: NestedContainer, disposing: bool)
            Releases the resources used by the nested container.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: NestedContainer, service: Type) -> object
        
            Gets the service object of the specified type, if it is available.
        
            service: The System.Type of the service to retrieve.
            Returns: An System.Object that implements the requested service, or null if the service cannot be 
             resolved.
        """
        pass

    def RemoveWithoutUnsiting(self, *args): #cannot find CLR method
        """
        RemoveWithoutUnsiting(self: Container, component: IComponent)
            Removes a component from the System.ComponentModel.Container without setting 
             System.ComponentModel.IComponent.Site to null.
        
        
            component: The component to remove.
        """
        pass

    def ValidateName(self, *args): #cannot find CLR method
        """
        ValidateName(self: Container, component: IComponent, name: str)
            Determines whether the component name is unique for this container.
        
            component: The named component.
            name: The component name to validate.
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
    def __new__(self, owner):
        """ __new__(cls: type, owner: IComponent) """
        pass

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the owning component for this nested container.

Get: Owner(self: NestedContainer) -> IComponent

"""

    OwnerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the owning component.

"""



class NotifyParentPropertyAttribute(Attribute, _Attribute):
    """
    Indicates that the parent property is notified when the value of the property that this attribute is applied to is modified. This class cannot be inherited.
    
    NotifyParentPropertyAttribute(notifyParent: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: NotifyParentPropertyAttribute, obj: object) -> bool
        
            Gets a value indicating whether the specified object is the same as the current object.
        
            obj: The object to test for equality.
            Returns: true if the object is the same as this object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: NotifyParentPropertyAttribute) -> int
        
            Gets the hash code for this object.
            Returns: The hash code for the object the attribute belongs to.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: NotifyParentPropertyAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default value of the attribute; otherwise, 
             false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, notifyParent):
        """ __new__(cls: type, notifyParent: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    NotifyParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the parent property should be notified of changes to the value of the property.

Get: NotifyParent(self: NotifyParentPropertyAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class NullableConverter(TypeConverter):
    """
    Provides automatic conversion between a nullable type and its underlying primitive type.
    
    NullableConverter(type: Type)
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: NullableConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of the given type to the type of this 
             converter, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext  that provides a format context.
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: NullableConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type, using the specified 
             context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: NullableConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the type of this converter, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: NullableConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type, using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: NullableConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            propertyValues: An System.Collections.IDictionary of new property values.
            Returns: An System.Object representing the given System.Collections.IDictionary, or null if the object 
             cannot be created. This method always returns null.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: NullableConverter, context: ITypeDescriptorContext) -> bool
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if changing a property on this object requires a call to 
             System.ComponentModel.TypeConverter.CreateInstance(System.Collections.IDictionary) to create a 
             new value; otherwise, false.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: NullableConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: An System.Object that specifies the type of array for which to get properties.
            attributes: An array of type System.Attribute that is used as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that are exposed for 
             this data type, or null if there are no properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: NullableConverter, context: ITypeDescriptorContext) -> bool
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if System.ComponentModel.TypeConverter.GetProperties(System.Object) should be called to 
             find the properties of this object; otherwise, false.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: NullableConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context that can be used 
             to extract additional information about the environment from which this converter is invoked. 
             This parameter or properties of this parameter can be null.
        
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: NullableConverter, context: ITypeDescriptorContext) -> bool
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.TypeConverter.GetStandardValues is an exhaustive list of possible values; 
             false if other values are possible.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: NullableConverter, context: ITypeDescriptorContext) -> bool
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if System.ComponentModel.TypeConverter.GetStandardValues should be called to find a common 
             set of values the object supports; otherwise, false.
        """
        pass

    def IsValid(self, *__args):
        """
        IsValid(self: NullableConverter, context: ITypeDescriptorContext, value: object) -> bool
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            value: The System.Object to test for validity.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass

    NullableType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the nullable type.

Get: NullableType(self: NullableConverter) -> Type

"""

    UnderlyingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying type.

Get: UnderlyingType(self: NullableConverter) -> Type

"""

    UnderlyingTypeConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying type converter.

Get: UnderlyingTypeConverter(self: NullableConverter) -> TypeConverter

"""



class ParenthesizePropertyNameAttribute(Attribute, _Attribute):
    """
    Indicates whether the name of the associated property is displayed with parentheses in the Properties window. This class cannot be inherited.
    
    ParenthesizePropertyNameAttribute()
    ParenthesizePropertyNameAttribute(needParenthesis: bool)
    """
    def Equals(self, o):
        """
        Equals(self: ParenthesizePropertyNameAttribute, o: object) -> bool
        
            Compares the specified object to this object and tests for equality.
        
            o: The object to be compared.
            Returns: true if equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ParenthesizePropertyNameAttribute) -> int
        
            Gets the hash code for this object.
            Returns: The hash code for the object the attribute belongs to.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ParenthesizePropertyNameAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default value of the attribute; otherwise, 
             false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, needParenthesis=None):
        """
        __new__(cls: type)
        __new__(cls: type, needParenthesis: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    NeedParenthesis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the Properties window displays the name of the property in parentheses in the Properties window.

Get: NeedParenthesis(self: ParenthesizePropertyNameAttribute) -> bool

"""


    Default = None


class PasswordPropertyTextAttribute(Attribute, _Attribute):
    """
    Indicates that an object's text representation is obscured by characters such as asterisks. This class cannot be inherited.
    
    PasswordPropertyTextAttribute()
    PasswordPropertyTextAttribute(password: bool)
    """
    def Equals(self, o):
        """
        Equals(self: PasswordPropertyTextAttribute, o: object) -> bool
        
            Determines whether two System.ComponentModel.PasswordPropertyTextAttribute instances are equal.
        
            o: The System.ComponentModel.PasswordPropertyTextAttribute to compare with the current 
             System.ComponentModel.PasswordPropertyTextAttribute.
        
            Returns: true if the specified System.ComponentModel.PasswordPropertyTextAttribute is equal to the 
             current System.ComponentModel.PasswordPropertyTextAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PasswordPropertyTextAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.PasswordPropertyTextAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: PasswordPropertyTextAttribute) -> bool
        
            Returns an indication whether the value of this instance is the default value.
            Returns: true if this instance is the default attribute for the class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, password=None):
        """
        __new__(cls: type)
        __new__(cls: type, password: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating if the property for which the System.ComponentModel.PasswordPropertyTextAttribute is defined should be shown as password text.

Get: Password(self: PasswordPropertyTextAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class ProgressChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.BackgroundWorker.ProgressChanged event.
    
    ProgressChangedEventArgs(progressPercentage: int, userState: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, progressPercentage, userState):
        """ __new__(cls: type, progressPercentage: int, userState: object) """
        pass

    ProgressPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the asynchronous task progress percentage.

Get: ProgressPercentage(self: ProgressChangedEventArgs) -> int

"""

    UserState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique user state.

Get: UserState(self: ProgressChangedEventArgs) -> object

"""



class ProgressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.BackgroundWorker.ProgressChanged event of the System.ComponentModel.BackgroundWorker class. This class cannot be inherited.
    
    ProgressChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ProgressChangedEventHandler, sender: object, e: ProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ProgressChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ProgressChangedEventHandler, sender: object, e: ProgressChangedEventArgs) """
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


class PropertyChangedEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event.
    
    PropertyChangedEventArgs(propertyName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property that changed.

Get: PropertyName(self: PropertyChangedEventArgs) -> str

"""



class PropertyChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event raised when a property is changed on a component.
    
    PropertyChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PropertyChangedEventHandler, sender: object, e: PropertyChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PropertyChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PropertyChangedEventHandler, sender: object, e: PropertyChangedEventArgs) """
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


class PropertyChangingEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.INotifyPropertyChanging.PropertyChanging event.
    
    PropertyChangingEventArgs(propertyName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property whose value is changing.

Get: PropertyName(self: PropertyChangingEventArgs) -> str

"""



class PropertyChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.INotifyPropertyChanging.PropertyChanging event of an System.ComponentModel.INotifyPropertyChanging interface.
    
    PropertyChangingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PropertyChangingEventHandler, sender: object, e: PropertyChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PropertyChangingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PropertyChangingEventHandler, sender: object, e: PropertyChangingEventArgs) """
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


class PropertyDescriptor(MemberDescriptor):
    """ Provides an abstraction of a property on a class. """
    def AddValueChanged(self, component, handler):
        """
        AddValueChanged(self: PropertyDescriptor, component: object, handler: EventHandler)
            Enables other objects to be notified when this property changes.
        
            component: The component to add the handler for.
            handler: The delegate to add as a listener.
        """
        pass

    def CanResetValue(self, component):
        """
        CanResetValue(self: PropertyDescriptor, component: object) -> bool
        
            When overridden in a derived class, returns whether resetting an object changes its value.
        
            component: The component to test for reset capability.
            Returns: true if resetting the component changes its value; otherwise, false.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: PropertyDescriptor, type: Type) -> object
        
            Creates an instance of the specified type.
        
            type: A System.Type that represents the type to create.
            Returns: A new instance of the type.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PropertyDescriptor, obj: object) -> bool
        
            Compares this to another object to see if they are equivalent.
        
            obj: The object to compare to this System.ComponentModel.PropertyDescriptor.
            Returns: true if the values are equivalent; otherwise, false.
        """
        pass

    def GetChildProperties(self, *__args):
        """
        GetChildProperties(self: PropertyDescriptor, instance: object) -> PropertyDescriptorCollection
        
            Returns a System.ComponentModel.PropertyDescriptorCollection for a given object.
        
            instance: A component to get the properties for.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for the specified 
             component.
        
        GetChildProperties(self: PropertyDescriptor, instance: object, filter: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a System.ComponentModel.PropertyDescriptorCollection for a given object using a 
             specified array of attributes as a filter.
        
        
            instance: A component to get the properties for.
            filter: An array of type System.Attribute to use as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 
             specified attributes for the specified component.
        
        GetChildProperties(self: PropertyDescriptor) -> PropertyDescriptorCollection
        
            Returns the default System.ComponentModel.PropertyDescriptorCollection.
            Returns: A System.ComponentModel.PropertyDescriptorCollection.
        GetChildProperties(self: PropertyDescriptor, filter: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a System.ComponentModel.PropertyDescriptorCollection using a specified array of 
             attributes as a filter.
        
        
            filter: An array of type System.Attribute to use as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 
             specified attributes.
        """
        pass

    def GetEditor(self, editorBaseType):
        """
        GetEditor(self: PropertyDescriptor, editorBaseType: Type) -> object
        
            Gets an editor of the specified type.
        
            editorBaseType: The base type of editor, which is used to differentiate between multiple editors that a property 
             supports.
        
            Returns: An instance of the requested editor type, or null if an editor cannot be found.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PropertyDescriptor) -> int
        
            Returns the hash code for this object.
            Returns: The hash code for this object.
        """
        pass

    def GetTypeFromName(self, *args): #cannot find CLR method
        """
        GetTypeFromName(self: PropertyDescriptor, typeName: str) -> Type
        
            Returns a type using its name.
        
            typeName: The assembly-qualified name of the type to retrieve.
            Returns: A System.Type that matches the given type name, or null if a match cannot be found.
        """
        pass

    def GetValue(self, component):
        """
        GetValue(self: PropertyDescriptor, component: object) -> object
        
            When overridden in a derived class, gets the current value of the property on a component.
        
            component: The component with the property for which to retrieve the value.
            Returns: The value of a property for a given component.
        """
        pass

    def GetValueChangedHandler(self, *args): #cannot find CLR method
        """
        GetValueChangedHandler(self: PropertyDescriptor, component: object) -> EventHandler
        
            Retrieves the current set of ValueChanged event handlers for a specific component
        
            component: The component for which to retrieve event handlers.
            Returns: A combined multicast event handler, or null if no event handlers are currently assigned to 
             component.
        """
        pass

    def OnValueChanged(self, *args): #cannot find CLR method
        """
        OnValueChanged(self: PropertyDescriptor, component: object, e: EventArgs)
            Raises the ValueChanged event that you implemented.
        
            component: The object that raises the event.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def RemoveValueChanged(self, component, handler):
        """
        RemoveValueChanged(self: PropertyDescriptor, component: object, handler: EventHandler)
            Enables other objects to be notified when this property changes.
        
            component: The component to remove the handler for.
            handler: The delegate to remove as a listener.
        """
        pass

    def ResetValue(self, component):
        """
        ResetValue(self: PropertyDescriptor, component: object)
            When overridden in a derived class, resets the value for this property of the component to the 
             default value.
        
        
            component: The component with the property value that is to be reset to the default value.
        """
        pass

    def SetValue(self, component, value):
        """
        SetValue(self: PropertyDescriptor, component: object, value: object)
            When overridden in a derived class, sets the value of the component to a different value.
        
            component: The component with the property value that is to be set.
            value: The new value.
        """
        pass

    def ShouldSerializeValue(self, component):
        """
        ShouldSerializeValue(self: PropertyDescriptor, component: object) -> bool
        
            When overridden in a derived class, determines a value indicating whether the value of this 
             property needs to be persisted.
        
        
            component: The component with the property to be examined for persistence.
            Returns: true if the property should be persisted; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, name: str, attrs: Array[Attribute])
        __new__(cls: type, descr: MemberDescriptor)
        __new__(cls: type, descr: MemberDescriptor, attrs: Array[Attribute])
        """
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of attributes.

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the type of the component this property is bound to.

Get: ComponentType(self: PropertyDescriptor) -> Type

"""

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type converter for this property.

Get: Converter(self: PropertyDescriptor) -> TypeConverter

"""

    IsLocalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this property should be localized, as specified in the System.ComponentModel.LocalizableAttribute.

Get: IsLocalizable(self: PropertyDescriptor) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether this property is read-only.

Get: IsReadOnly(self: PropertyDescriptor) -> bool

"""

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash code for the name of the member, as specified in System.String.GetHashCode.

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the type of the property.

Get: PropertyType(self: PropertyDescriptor) -> Type

"""

    SerializationVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this property should be serialized, as specified in the System.ComponentModel.DesignerSerializationVisibilityAttribute.

Get: SerializationVisibility(self: PropertyDescriptor) -> DesignerSerializationVisibility

"""

    SupportsChangeEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether value change notifications for this property may originate from outside the property descriptor.

Get: SupportsChangeEvents(self: PropertyDescriptor) -> bool

"""



class PropertyDescriptorCollection(object, ICollection, IEnumerable, IList, IDictionary):
    """
    Represents a collection of System.ComponentModel.PropertyDescriptor objects.
    
    PropertyDescriptorCollection(properties: Array[PropertyDescriptor])
    PropertyDescriptorCollection(properties: Array[PropertyDescriptor], readOnly: bool)
    """
    def Add(self, value):
        """
        Add(self: PropertyDescriptorCollection, value: PropertyDescriptor) -> int
        
            Adds the specified System.ComponentModel.PropertyDescriptor to the collection.
        
            value: The System.ComponentModel.PropertyDescriptor to add to the collection.
            Returns: The index of the System.ComponentModel.PropertyDescriptor that was added to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: PropertyDescriptorCollection)
            Removes all System.ComponentModel.PropertyDescriptor objects from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: PropertyDescriptorCollection, value: PropertyDescriptor) -> bool
        
            Returns whether the collection contains the given System.ComponentModel.PropertyDescriptor.
        
            value: The System.ComponentModel.PropertyDescriptor to find in the collection.
            Returns: true if the collection contains the given System.ComponentModel.PropertyDescriptor; otherwise, 
             false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: PropertyDescriptorCollection, array: Array, index: int)
            Copies the entire collection to an array, starting at the specified index number.
        
            array: An array of System.ComponentModel.PropertyDescriptor objects to copy elements of the collection 
             to.
        
            index: The index of the array parameter at which copying begins.
        """
        pass

    def Find(self, name, ignoreCase):
        """
        Find(self: PropertyDescriptorCollection, name: str, ignoreCase: bool) -> PropertyDescriptor
        
            Returns the System.ComponentModel.PropertyDescriptor with the specified name, using a Boolean to 
             indicate whether to ignore case.
        
        
            name: The name of the System.ComponentModel.PropertyDescriptor to return from the collection.
            ignoreCase: true if you want to ignore the case of the property name; otherwise, false.
            Returns: A System.ComponentModel.PropertyDescriptor with the specified name, or null if the property does 
             not exist.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PropertyDescriptorCollection) -> IEnumerator
        
            Returns an enumerator for this class.
            Returns: An enumerator of type System.Collections.IEnumerator.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: PropertyDescriptorCollection, value: PropertyDescriptor) -> int
        
            Returns the index of the given System.ComponentModel.PropertyDescriptor.
        
            value: The System.ComponentModel.PropertyDescriptor to return the index of.
            Returns: The index of the given System.ComponentModel.PropertyDescriptor.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: PropertyDescriptorCollection, index: int, value: PropertyDescriptor)
            Adds the System.ComponentModel.PropertyDescriptor to the collection at the specified index 
             number.
        
        
            index: The index at which to add the value parameter to the collection.
            value: The System.ComponentModel.PropertyDescriptor to add to the collection.
        """
        pass

    def InternalSort(self, *args): #cannot find CLR method
        """
        InternalSort(self: PropertyDescriptorCollection, sorter: IComparer)
            Sorts the members of this collection, using the specified System.Collections.IComparer.
        
            sorter: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 
             collection.
        
        InternalSort(self: PropertyDescriptorCollection, names: Array[str])
            Sorts the members of this collection. The specified order is applied first, followed by the 
             default sort for this collection, which is usually alphabetical.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.PropertyDescriptor objects in this collection.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: PropertyDescriptorCollection, value: PropertyDescriptor)
            Removes the specified System.ComponentModel.PropertyDescriptor from the collection.
        
            value: The System.ComponentModel.PropertyDescriptor to remove from the collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: PropertyDescriptorCollection, index: int)
            Removes the System.ComponentModel.PropertyDescriptor at the specified index from the collection.
        
            index: The index of the System.ComponentModel.PropertyDescriptor to remove from the collection.
        """
        pass

    def Sort(self, *__args):
        """
        Sort(self: PropertyDescriptorCollection, names: Array[str], comparer: IComparer) -> PropertyDescriptorCollection
        
            Sorts the members of this collection. The specified order is applied first, followed by the sort 
             using the specified System.Collections.IComparer.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.PropertyDescriptor objects in this collection.
        
            comparer: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 
             collection.
        
            Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 
             System.ComponentModel.PropertyDescriptor objects.
        
        Sort(self: PropertyDescriptorCollection, comparer: IComparer) -> PropertyDescriptorCollection
        
            Sorts the members of this collection, using the specified System.Collections.IComparer.
        
            comparer: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 
             collection.
        
            Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 
             System.ComponentModel.PropertyDescriptor objects.
        
        Sort(self: PropertyDescriptorCollection) -> PropertyDescriptorCollection
        
            Sorts the members of this collection, using the default sort for this collection, which is 
             usually alphabetical.
        
            Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 
             System.ComponentModel.PropertyDescriptor objects.
        
        Sort(self: PropertyDescriptorCollection, names: Array[str]) -> PropertyDescriptorCollection
        
            Sorts the members of this collection. The specified order is applied first, followed by the 
             default sort for this collection, which is usually alphabetical.
        
        
            names: An array of strings describing the order in which to sort the 
             System.ComponentModel.PropertyDescriptor objects in this collection.
        
            Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 
             System.ComponentModel.PropertyDescriptor objects.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, properties, readOnly=None):
        """
        __new__(cls: type, properties: Array[PropertyDescriptor])
        __new__(cls: type, properties: Array[PropertyDescriptor], readOnly: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of property descriptors in the collection.

Get: Count(self: PropertyDescriptorCollection) -> int

"""


    Empty = None


class PropertyTabAttribute(Attribute, _Attribute):
    """
    Identifies the property tab or tabs to display for the specified class or classes.
    
    PropertyTabAttribute()
    PropertyTabAttribute(tabClass: Type)
    PropertyTabAttribute(tabClassName: str)
    PropertyTabAttribute(tabClass: Type, tabScope: PropertyTabScope)
    PropertyTabAttribute(tabClassName: str, tabScope: PropertyTabScope)
    """
    def Equals(self, other):
        """
        Equals(self: PropertyTabAttribute, other: PropertyTabAttribute) -> bool
        
            Returns a value indicating whether this instance is equal to a specified attribute.
        
            other: A System.ComponentModel.PropertyTabAttribute to compare to this instance, or null.
            Returns: true if the System.ComponentModel.PropertyTabAttribute instances are equal; otherwise, false.
        Equals(self: PropertyTabAttribute, other: object) -> bool
        
            Returns a value indicating whether this instance is equal to a specified object.
        
            other: An object to compare to this instance, or null.
            Returns: true if other refers to the same System.ComponentModel.PropertyTabAttribute instance; otherwise, 
             false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PropertyTabAttribute) -> int
        
            Gets the hash code for this object.
            Returns: The hash code for the object the attribute belongs to.
        """
        pass

    def InitializeArrays(self, *args): #cannot find CLR method
        """
        InitializeArrays(self: PropertyTabAttribute, tabClasses: Array[Type], tabScopes: Array[PropertyTabScope])
            Initializes the attribute using the specified names of tab classes and array of tab scopes.
        
            tabClasses: The types of tabs to create.
            tabScopes: The scope of each tab. If the scope is System.ComponentModel.PropertyTabScope.Component, it is 
             shown only for components with the corresponding System.ComponentModel.PropertyTabAttribute. If 
             it is System.ComponentModel.PropertyTabScope.Document, it is shown for all components on the 
             document.
        
        InitializeArrays(self: PropertyTabAttribute, tabClassNames: Array[str], tabScopes: Array[PropertyTabScope])
            Initializes the attribute using the specified names of tab classes and array of tab scopes.
        
            tabClassNames: An array of fully qualified type names of the types to create for tabs on the Properties window.
            tabScopes: The scope of each tab. If the scope is System.ComponentModel.PropertyTabScope.Component, it is 
             shown only for components with the corresponding System.ComponentModel.PropertyTabAttribute. If 
             it is System.ComponentModel.PropertyTabScope.Document, it is shown for all components on the 
             document.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, tabClass: Type)
        __new__(cls: type, tabClassName: str)
        __new__(cls: type, tabClass: Type, tabScope: PropertyTabScope)
        __new__(cls: type, tabClassName: str, tabScope: PropertyTabScope)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    TabClasses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the types of tabs that this attribute uses.

Get: TabClasses(self: PropertyTabAttribute) -> Array[Type]

"""

    TabClassNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the names of the tab classes that this attribute uses.

"""

    TabScopes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of tab scopes of each tab of this System.ComponentModel.PropertyTabAttribute.

Get: TabScopes(self: PropertyTabAttribute) -> Array[PropertyTabScope]

"""



class PropertyTabScope(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate the persistence scope of a tab in the Properties window.
    
    enum PropertyTabScope, values: Component (3), Document (2), Global (1), Static (0)
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

    Component = None
    Document = None
    Global = None
    Static = None
    value__ = None


class ProvidePropertyAttribute(Attribute, _Attribute):
    """
    Specifies the name of the property that an implementer of System.ComponentModel.IExtenderProvider offers to other components. This class cannot be inherited
    
    ProvidePropertyAttribute(propertyName: str, receiverType: Type)
    ProvidePropertyAttribute(propertyName: str, receiverTypeName: str)
    """
    def Equals(self, obj):
        """
        Equals(self: ProvidePropertyAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.ProvidePropertyAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ProvidePropertyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.ProvidePropertyAttribute.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, propertyName, *__args):
        """
        __new__(cls: type, propertyName: str, receiverType: Type)
        __new__(cls: type, propertyName: str, receiverTypeName: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a property that this class provides.

Get: PropertyName(self: ProvidePropertyAttribute) -> str

"""

    ReceiverTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the data type this property can extend.

Get: ReceiverTypeName(self: ProvidePropertyAttribute) -> str

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique identifier for this attribute.

Get: TypeId(self: ProvidePropertyAttribute) -> object

"""



class ReadOnlyAttribute(Attribute, _Attribute):
    """
    Specifies whether the property this attribute is bound to is read-only or read/write. This class cannot be inherited
    
    ReadOnlyAttribute(isReadOnly: bool)
    """
    def Equals(self, value):
        """
        Equals(self: ReadOnlyAttribute, value: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            value: Another object to compare to.
            Returns: true if value is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ReadOnlyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.ReadOnlyAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ReadOnlyAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isReadOnly):
        """ __new__(cls: type, isReadOnly: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the property this attribute is bound to is read-only.

Get: IsReadOnly(self: ReadOnlyAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class RecommendedAsConfigurableAttribute(Attribute, _Attribute):
    """
    Specifies that the property can be used as an application setting.
    
    RecommendedAsConfigurableAttribute(recommendedAsConfigurable: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: RecommendedAsConfigurableAttribute, obj: object) -> bool
        
            Indicates whether this instance and a specified object are equal.
        
            obj: Another object to compare to.
            Returns: true if obj is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RecommendedAsConfigurableAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.RecommendedAsConfigurableAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: RecommendedAsConfigurableAttribute) -> bool
        
            Indicates whether the value of this instance is the default value for the class.
            Returns: true if this instance is the default attribute for the class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, recommendedAsConfigurable):
        """ __new__(cls: type, recommendedAsConfigurable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    RecommendedAsConfigurable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the property this attribute is bound to can be used as an application setting.

Get: RecommendedAsConfigurable(self: RecommendedAsConfigurableAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class RefreshEventArgs(EventArgs):
    """
    Provides data for the System.ComponentModel.TypeDescriptor.Refreshed event.
    
    RefreshEventArgs(componentChanged: object)
    RefreshEventArgs(typeChanged: Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, componentChanged: object)
        __new__(cls: type, typeChanged: Type)
        """
        pass

    ComponentChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the component that changed its properties, events, or extenders.

Get: ComponentChanged(self: RefreshEventArgs) -> object

"""

    TypeChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type that changed its properties or events.

Get: TypeChanged(self: RefreshEventArgs) -> Type

"""



class RefreshEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.ComponentModel.TypeDescriptor.Refreshed event raised when a System.Type or component is changed during design time.
    
    RefreshEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, e, callback, object):
        """ BeginInvoke(self: RefreshEventHandler, e: RefreshEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: RefreshEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, e):
        """ Invoke(self: RefreshEventHandler, e: RefreshEventArgs) """
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


class RefreshProperties(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate the type of a refresh of the Properties window.
    
    enum RefreshProperties, values: All (1), None (0), Repaint (2)
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
    None = None
    Repaint = None
    value__ = None


class RefreshPropertiesAttribute(Attribute, _Attribute):
    """
    Indicates that the property grid should refresh when the associated property value changes. This class cannot be inherited.
    
    RefreshPropertiesAttribute(refresh: RefreshProperties)
    """
    def Equals(self, value):
        """
        Equals(self: RefreshPropertiesAttribute, value: object) -> bool
        
            Overrides the object's erload:System.Object.Equals method.
        
            value: The object to test for equality.
            Returns: true if the specified object is the same; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RefreshPropertiesAttribute) -> int
        
            Returns the hash code for this object.
            Returns: The hash code for the object that the attribute belongs to.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: RefreshPropertiesAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, refresh):
        """ __new__(cls: type, refresh: RefreshProperties) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    RefreshProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the refresh properties for the member.

Get: RefreshProperties(self: RefreshPropertiesAttribute) -> RefreshProperties

"""


    All = None
    Default = None
    Repaint = None


class RunInstallerAttribute(Attribute, _Attribute):
    """
    Specifies whether the Visual Studio Custom Action Installer or the Installutil.exe (Installer Tool) should be invoked when the assembly is installed.
    
    RunInstallerAttribute(runInstaller: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: RunInstallerAttribute, obj: object) -> bool
        
            Determines whether the value of the specified System.ComponentModel.RunInstallerAttribute is 
             equivalent to the current System.ComponentModel.RunInstallerAttribute.
        
        
            obj: The object to compare.
            Returns: true if the specified System.ComponentModel.RunInstallerAttribute is equal to the current 
             System.ComponentModel.RunInstallerAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RunInstallerAttribute) -> int
        
            Generates a hash code for the current System.ComponentModel.RunInstallerAttribute.
            Returns: A hash code for the current System.ComponentModel.RunInstallerAttribute.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: RunInstallerAttribute) -> bool
        
            Determines if this attribute is the default.
            Returns: true if the attribute is the default value for this attribute class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, runInstaller):
        """ __new__(cls: type, runInstaller: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    RunInstaller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an installer should be invoked during installation of an assembly.

Get: RunInstaller(self: RunInstallerAttribute) -> bool

"""


    Default = None
    No = None
    Yes = None


class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the MethodNameCompleted event.
    
    RunWorkerCompletedEventArgs(result: object, error: Exception, cancelled: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, result, error, cancelled):
        """ __new__(cls: type, result: object, error: Exception, cancelled: bool) """
        pass

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the result of an asynchronous operation.

Get: Result(self: RunWorkerCompletedEventArgs) -> object

"""

    UserState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the user state.

Get: UserState(self: RunWorkerCompletedEventArgs) -> object

"""



class RunWorkerCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.ComponentModel.BackgroundWorker.RunWorkerCompleted event of a System.ComponentModel.BackgroundWorker class.
    
    RunWorkerCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: RunWorkerCompletedEventHandler, sender: object, e: RunWorkerCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: RunWorkerCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: RunWorkerCompletedEventHandler, sender: object, e: RunWorkerCompletedEventArgs) """
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


class SByteConverter(BaseNumberConverter):
    """
    Provides a type converter to convert 8-bit unsigned integer objects to and from a string.
    
    SByteConverter()
    """

class SettingsBindableAttribute(Attribute, _Attribute):
    """
    Specifies when a component property can be bound to an application setting.
    
    SettingsBindableAttribute(bindable: bool)
    """
    def Equals(self, obj):
        """
        Equals(self: SettingsBindableAttribute, obj: object) -> bool
        
            Determines whether two System.ComponentModel.SettingsBindableAttribute objects are equal.
        
            obj: The value to compare to.
            Returns: true if obj equals the type and value of this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SettingsBindableAttribute) -> int
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bindable):
        """ __new__(cls: type, bindable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Bindable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a property is appropriate to bind settings to.

Get: Bindable(self: SettingsBindableAttribute) -> bool

"""


    No = None
    Yes = None


class SingleConverter(BaseNumberConverter):
    """
    Provides a type converter to convert single-precision, floating point number objects to and from various other representations.
    
    SingleConverter()
    """

class StringConverter(TypeConverter):
    """
    Provides a type converter to convert string objects to and from other representations.
    
    StringConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: StringConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a string using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: StringConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified value object to a System.String object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass


class SyntaxCheck(object):
    """ Provides methods to verify the machine name and path conform to a specific syntax. This class cannot be inherited. """
    @staticmethod
    def CheckMachineName(value):
        """
        CheckMachineName(value: str) -> bool
        
            Checks the syntax of the machine name to confirm that it does not contain "\".
        
            value: A string containing the machine name to check.
            Returns: true if value matches the proper machine name format; otherwise, false.
        """
        pass

    @staticmethod
    def CheckPath(value):
        """
        CheckPath(value: str) -> bool
        
            Checks the syntax of the path to see whether it starts with "\\".
        
            value: A string containing the path to check.
            Returns: true if value matches the proper path format; otherwise, false.
        """
        pass

    @staticmethod
    def CheckRootedPath(value):
        """
        CheckRootedPath(value: str) -> bool
        
            Checks the syntax of the path to see if it starts with "\" or drive letter "C:".
        
            value: A string containing the path to check.
            Returns: true if value matches the proper path format; otherwise, false.
        """
        pass

    __all__ = [
        'CheckMachineName',
        'CheckPath',
        'CheckRootedPath',
    ]


class TimeSpanConverter(TypeConverter):
    """
    Provides a type converter to convert System.TimeSpan objects to and from other representations.
    
    TimeSpanConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TimeSpanConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object in the given source type to 
             a System.TimeSpan using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you wish to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TimeSpanConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TimeSpanConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to a System.TimeSpan.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TimeSpanConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given object to another type.
        
            context: A formatter context.
            culture: The culture into which value will be converted.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass


class ToolboxItemAttribute(Attribute, _Attribute):
    """
    Represents an attribute of a toolbox item.
    
    ToolboxItemAttribute(defaultType: bool)
    ToolboxItemAttribute(toolboxItemTypeName: str)
    ToolboxItemAttribute(toolboxItemType: Type)
    """
    def Equals(self, obj):
        """
        Equals(self: ToolboxItemAttribute, obj: object) -> bool
        
            obj: The object to compare.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ToolboxItemAttribute) -> int """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ToolboxItemAttribute) -> bool
        
            Gets a value indicating whether the current value of the attribute is the default value for the 
             attribute.
        
            Returns: true if the current value of the attribute is the default; otherwise, false.
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
        __new__(cls: type, defaultType: bool)
        __new__(cls: type, toolboxItemTypeName: str)
        __new__(cls: type, toolboxItemType: Type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ToolboxItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the toolbox item.

Get: ToolboxItemType(self: ToolboxItemAttribute) -> Type

"""

    ToolboxItemTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the type of the current System.Drawing.Design.ToolboxItem.

Get: ToolboxItemTypeName(self: ToolboxItemAttribute) -> str

"""


    Default = None
    None = None


class ToolboxItemFilterAttribute(Attribute, _Attribute):
    """
    Specifies the filter string and filter type to use for a toolbox item.
    
    ToolboxItemFilterAttribute(filterString: str)
    ToolboxItemFilterAttribute(filterString: str, filterType: ToolboxItemFilterType)
    """
    def Equals(self, obj):
        """
        Equals(self: ToolboxItemFilterAttribute, obj: object) -> bool
        
            obj: The object to compare.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ToolboxItemFilterAttribute) -> int """
        pass

    def Match(self, obj):
        """
        Match(self: ToolboxItemFilterAttribute, obj: object) -> bool
        
            Indicates whether the specified object has a matching filter string.
        
            obj: The object to test for a matching filter string.
            Returns: true if the specified object has a matching filter string; otherwise, false.
        """
        pass

    def ToString(self):
        """ ToString(self: ToolboxItemFilterAttribute) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filterString, filterType=None):
        """
        __new__(cls: type, filterString: str)
        __new__(cls: type, filterString: str, filterType: ToolboxItemFilterType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FilterString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the filter string for the toolbox item.

Get: FilterString(self: ToolboxItemFilterAttribute) -> str

"""

    FilterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the filter.

Get: FilterType(self: ToolboxItemFilterAttribute) -> ToolboxItemFilterType

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type ID for the attribute.

Get: TypeId(self: ToolboxItemFilterAttribute) -> object

"""



class ToolboxItemFilterType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers used to indicate the type of filter that a System.ComponentModel.ToolboxItemFilterAttribute uses.
    
    enum ToolboxItemFilterType, values: Allow (0), Custom (1), Prevent (2), Require (3)
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

    Allow = None
    Custom = None
    Prevent = None
    Require = None
    value__ = None


class TypeConverterAttribute(Attribute, _Attribute):
    """
    Specifies what type to use as a converter for the object this attribute is bound to.
    
    TypeConverterAttribute()
    TypeConverterAttribute(type: Type)
    TypeConverterAttribute(typeName: str)
    """
    def Equals(self, obj):
        """
        Equals(self: TypeConverterAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current 
             System.ComponentModel.TypeConverterAttribute.
        
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current 
             System.ComponentModel.TypeConverterAttribute; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: TypeConverterAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.ComponentModel.TypeConverterAttribute.
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
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ConverterTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualified type name of the System.Type to use as a converter for the object this attribute is bound to.

Get: ConverterTypeName(self: TypeConverterAttribute) -> str

"""


    Default = None


class TypeDescriptionProvider(object):
    """ Provides supplemental metadata to the System.ComponentModel.TypeDescriptor. """
    def CreateInstance(self, provider, objectType, argTypes, args):
        """
        CreateInstance(self: TypeDescriptionProvider, provider: IServiceProvider, objectType: Type, argTypes: Array[Type], args: Array[object]) -> object
        
            Creates an object that can substitute for another data type.
        
            provider: An optional service provider.
            objectType: The type of object to create. This parameter is never null.
            argTypes: An optional array of types that represent the parameter types to be passed to the object's 
             constructor. This array can be null or of zero length.
        
            args: An optional array of parameter values to pass to the object's constructor.
            Returns: The substitute System.Object.
        """
        pass

    def GetCache(self, instance):
        """
        GetCache(self: TypeDescriptionProvider, instance: object) -> IDictionary
        
            Gets a per-object cache, accessed as an System.Collections.IDictionary of key/value pairs.
        
            instance: The object for which to get the cache.
            Returns: An System.Collections.IDictionary if the provided object supports caching; otherwise, null.
        """
        pass

    def GetExtendedTypeDescriptor(self, instance):
        """
        GetExtendedTypeDescriptor(self: TypeDescriptionProvider, instance: object) -> ICustomTypeDescriptor
        
            Gets an extended custom type descriptor for the given object.
        
            instance: The object for which to get the extended type descriptor.
            Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide extended metadata for the object.
        """
        pass

    def GetExtenderProviders(self, *args): #cannot find CLR method
        """
        GetExtenderProviders(self: TypeDescriptionProvider, instance: object) -> Array[IExtenderProvider]
        
            Gets the extender providers for the specified object.
        
            instance: The object to get extender providers for.
            Returns: An array of extender providers for instance.
        """
        pass

    def GetFullComponentName(self, component):
        """
        GetFullComponentName(self: TypeDescriptionProvider, component: object) -> str
        
            Gets the name of the specified component, or null if the component has no name.
        
            component: The specified component.
            Returns: The name of the specified component.
        """
        pass

    def GetReflectionType(self, *__args):
        """
        GetReflectionType(self: TypeDescriptionProvider, objectType: Type, instance: object) -> Type
        
            Performs normal reflection against the given object with the given type.
        
            objectType: The type of object for which to retrieve the System.Reflection.IReflect.
            instance: An instance of the type. Can be null.
            Returns: A System.Type.
        GetReflectionType(self: TypeDescriptionProvider, instance: object) -> Type
        
            Performs normal reflection against the given object.
        
            instance: An instance of the type (should not be null).
            Returns: A System.Type.
        GetReflectionType(self: TypeDescriptionProvider, objectType: Type) -> Type
        
            Performs normal reflection against a type.
        
            objectType: The type of object for which to retrieve the System.Reflection.IReflect.
            Returns: A System.Type.
        """
        pass

    def GetRuntimeType(self, reflectionType):
        """
        GetRuntimeType(self: TypeDescriptionProvider, reflectionType: Type) -> Type
        
            Converts a reflection type into a runtime type.
        
            reflectionType: The type to convert to its runtime equivalent.
            Returns: A System.Type that represents the runtime equivalent of reflectionType.
        """
        pass

    def GetTypeDescriptor(self, *__args):
        """
        GetTypeDescriptor(self: TypeDescriptionProvider, objectType: Type, instance: object) -> ICustomTypeDescriptor
        
            Gets a custom type descriptor for the given type and object.
        
            objectType: The type of object for which to retrieve the type descriptor.
            instance: An instance of the type. Can be null if no instance was passed to the 
             System.ComponentModel.TypeDescriptor.
        
            Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.
        GetTypeDescriptor(self: TypeDescriptionProvider, instance: object) -> ICustomTypeDescriptor
        
            Gets a custom type descriptor for the given object.
        
            instance: An instance of the type. Can be null if no instance was passed to the 
             System.ComponentModel.TypeDescriptor.
        
            Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.
        GetTypeDescriptor(self: TypeDescriptionProvider, objectType: Type) -> ICustomTypeDescriptor
        
            Gets a custom type descriptor for the given type.
        
            objectType: The type of object for which to retrieve the type descriptor.
            Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.
        """
        pass

    def IsSupportedType(self, type):
        """
        IsSupportedType(self: TypeDescriptionProvider, type: Type) -> bool
        
            Gets a value that indicates whether the specified type is compatible with the type description 
             and its chain of type description providers.
        
        
            type: The type to test for compatibility.
            Returns: true if type is compatible with the type description and its chain of type description 
             providers; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, parent: TypeDescriptionProvider)
        """
        pass


class TypeDescriptionProviderAttribute(Attribute, _Attribute):
    """
    Specifies the custom type description provider for a class. This class cannot be inherited.
    
    TypeDescriptionProviderAttribute(typeName: str)
    TypeDescriptionProviderAttribute(type: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        pass

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name for the type description provider.

Get: TypeName(self: TypeDescriptionProviderAttribute) -> str

"""



class TypeDescriptor(object):
    """ Provides information about the characteristics for a component, such as its attributes, properties, and events. This class cannot be inherited. """
    @staticmethod
    def AddAttributes(*__args):
        """
        AddAttributes(instance: object, *attributes: Array[Attribute]) -> TypeDescriptionProvider
        
            Adds class-level attributes to the target component instance.
        
            instance: An instance of the target component.
            attributes: An array of System.Attribute objects to add to the component's class.
            Returns: The newly created System.ComponentModel.TypeDescriptionProvider that was used to add the 
             specified attributes.
        
        AddAttributes(type: Type, *attributes: Array[Attribute]) -> TypeDescriptionProvider
        
            Adds class-level attributes to the target component type.
        
            type: The System.Type of the target component.
            attributes: An array of System.Attribute objects to add to the component's class.
            Returns: The newly created System.ComponentModel.TypeDescriptionProvider that was used to add the 
             specified attributes.
        """
        pass

    @staticmethod
    def AddEditorTable(editorBaseType, table):
        """
        AddEditorTable(editorBaseType: Type, table: Hashtable)
            Adds an editor table for the given editor base type.
        
            editorBaseType: The editor base type to add the editor table for. If a table already exists for this type, this 
             method will do nothing.
        
            table: The System.Collections.Hashtable to add.
        """
        pass

    @staticmethod
    def AddProvider(provider, *__args):
        """
        AddProvider(provider: TypeDescriptionProvider, instance: object)
            Adds a type description provider for a single instance of a component.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to add.
            instance: An instance of the target component.
        AddProvider(provider: TypeDescriptionProvider, type: Type)
            Adds a type description provider for a component class.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to add.
            type: The System.Type of the target component.
        """
        pass

    @staticmethod
    def AddProviderTransparent(provider, *__args):
        """
        AddProviderTransparent(provider: TypeDescriptionProvider, instance: object)
            Adds a type description provider for a single instance of a component.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to add.
            instance: An instance of the target component.
        AddProviderTransparent(provider: TypeDescriptionProvider, type: Type)
            Adds a type description provider for a component class.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to add.
            type: The System.Type of the target component.
        """
        pass

    @staticmethod
    def CreateAssociation(primary, secondary):
        """
        CreateAssociation(primary: object, secondary: object)
            Creates a primary-secondary association between two objects.
        
            primary: The primary System.Object.
            secondary: The secondary System.Object.
        """
        pass

    @staticmethod
    def CreateDesigner(component, designerBaseType):
        """
        CreateDesigner(component: IComponent, designerBaseType: Type) -> IDesigner
        
            Creates an instance of the designer associated with the specified component and of the specified 
             type of designer.
        
        
            component: An System.ComponentModel.IComponent that specifies the component to associate with the designer.
            designerBaseType: A System.Type that represents the type of designer to create.
            Returns: An System.ComponentModel.Design.IDesigner that is an instance of the designer for the component, 
             or null if no designer can be found.
        """
        pass

    @staticmethod
    def CreateEvent(componentType, *__args):
        """
        CreateEvent(componentType: Type, oldEventDescriptor: EventDescriptor, *attributes: Array[Attribute]) -> EventDescriptor
        
            Creates a new event descriptor that is identical to an existing event descriptor, when passed 
             the existing System.ComponentModel.EventDescriptor.
        
        
            componentType: The type of the component for which to create the new event.
            oldEventDescriptor: The existing event information.
            attributes: The new attributes.
            Returns: A new System.ComponentModel.EventDescriptor that has merged the specified metadata attributes 
             with the existing metadata attributes.
        
        CreateEvent(componentType: Type, name: str, type: Type, *attributes: Array[Attribute]) -> EventDescriptor
        
            Creates a new event descriptor that is identical to an existing event descriptor by dynamically 
             generating descriptor information from a specified event on a type.
        
        
            componentType: The type of the component the event lives on.
            name: The name of the event.
            type: The type of the delegate that handles the event.
            attributes: The attributes for this event.
            Returns: An System.ComponentModel.EventDescriptor that is bound to a type.
        """
        pass

    @staticmethod
    def CreateInstance(provider, objectType, argTypes, args):
        """
        CreateInstance(provider: IServiceProvider, objectType: Type, argTypes: Array[Type], args: Array[object]) -> object
        
            Creates an object that can substitute for another data type.
        
            provider: The service provider that provides a System.ComponentModel.TypeDescriptionProvider service. This 
             parameter can be null.
        
            objectType: The System.Type of object to create.
            argTypes: An optional array of parameter types to be passed to the object's constructor. This parameter 
             can be null or an array of zero length.
        
            args: An optional array of parameter values to pass to the object's constructor. If not null, the 
             number of elements must be the same as argTypes.
        
            Returns: An instance of the substitute data type if an associated 
             System.ComponentModel.TypeDescriptionProvider is found; otherwise, null.
        """
        pass

    @staticmethod
    def CreateProperty(componentType, *__args):
        """
        CreateProperty(componentType: Type, oldPropertyDescriptor: PropertyDescriptor, *attributes: Array[Attribute]) -> PropertyDescriptor
        
            Creates a new property descriptor from an existing property descriptor, using the specified 
             existing System.ComponentModel.PropertyDescriptor and attribute array.
        
        
            componentType: The System.Type of the component that the property is a member of.
            oldPropertyDescriptor: The existing property descriptor.
            attributes: The new attributes for this property.
            Returns: A new System.ComponentModel.PropertyDescriptor that has the specified metadata attributes merged 
             with the existing metadata attributes.
        
        CreateProperty(componentType: Type, name: str, type: Type, *attributes: Array[Attribute]) -> PropertyDescriptor
        
            Creates and dynamically binds a property descriptor to a type, using the specified property 
             name, type, and attribute array.
        
        
            componentType: The System.Type of the component that the property is a member of.
            name: The name of the property.
            type: The System.Type of the property.
            attributes: The new attributes for this property.
            Returns: A System.ComponentModel.PropertyDescriptor that is bound to the specified type and that has the 
             specified metadata attributes merged with the existing metadata attributes.
        """
        pass

    @staticmethod
    def GetAssociation(type, primary):
        """
        GetAssociation(type: Type, primary: object) -> object
        
            Returns an instance of the type associated with the specified primary object.
        
            type: The System.Type of the target component.
            primary: The primary object of the association.
            Returns: An instance of the secondary type that has been associated with the primary object if an 
             association exists; otherwise, primary if no specified association exists.
        """
        pass

    @staticmethod
    def GetAttributes(*__args):
        """
        GetAttributes(component: object, noCustomTypeDesc: bool) -> AttributeCollection
        
            Returns a collection of attributes for the specified component and a Boolean indicating that a 
             custom type descriptor has been created.
        
        
            component: The component for which you want to get attributes.
            noCustomTypeDesc: true to use a baseline set of attributes from the custom type descriptor if component is of type 
             System.ComponentModel.ICustomTypeDescriptor; otherwise, false.
        
            Returns: An System.ComponentModel.AttributeCollection with the attributes for the component. If the 
             component is null, this method returns an empty collection.
        
        GetAttributes(component: object) -> AttributeCollection
        
            Returns the collection of attributes for the specified component.
        
            component: The component for which you want to get attributes.
            Returns: An System.ComponentModel.AttributeCollection containing the attributes for the component. If 
             component is null, this method returns an empty collection.
        
        GetAttributes(componentType: Type) -> AttributeCollection
        
            Returns a collection of attributes for the specified type of component.
        
            componentType: The System.Type of the target component.
            Returns: An System.ComponentModel.AttributeCollection with the attributes for the type of the component. 
             If the component is null, this method returns an empty collection.
        """
        pass

    @staticmethod
    def GetClassName(*__args):
        """
        GetClassName(componentType: Type) -> str
        
            Returns the name of the class for the specified type.
        
            componentType: The System.Type of the target component.
            Returns: A System.String containing the name of the class for the specified component type.
        GetClassName(component: object, noCustomTypeDesc: bool) -> str
        
            Returns the name of the class for the specified component using a custom type descriptor.
        
            component: The System.Object for which you want the class name.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: A System.String containing the name of the class for the specified component.
        GetClassName(component: object) -> str
        
            Returns the name of the class for the specified component using the default type descriptor.
        
            component: The System.Object for which you want the class name.
            Returns: A System.String containing the name of the class for the specified component.
        """
        pass

    @staticmethod
    def GetComponentName(component, noCustomTypeDesc=None):
        """
        GetComponentName(component: object, noCustomTypeDesc: bool) -> str
        
            Returns the name of the specified component using a custom type descriptor.
        
            component: The System.Object for which you want the class name.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: The name of the class for the specified component, or null if there is no component name.
        GetComponentName(component: object) -> str
        
            Returns the name of the specified component using the default type descriptor.
        
            component: The System.Object for which you want the class name.
            Returns: A System.String containing the name of the specified component, or null if there is no component 
             name.
        """
        pass

    @staticmethod
    def GetConverter(*__args):
        """
        GetConverter(type: Type) -> TypeConverter
        
            Returns a type converter for the specified type.
        
            type: The System.Type of the target component.
            Returns: A System.ComponentModel.TypeConverter for the specified type.
        GetConverter(component: object, noCustomTypeDesc: bool) -> TypeConverter
        
            Returns a type converter for the type of the specified component with a custom type descriptor.
        
            component: A component to get the converter for.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: A System.ComponentModel.TypeConverter for the specified component.
        GetConverter(component: object) -> TypeConverter
        
            Returns a type converter for the type of the specified component.
        
            component: A component to get the converter for.
            Returns: A System.ComponentModel.TypeConverter for the specified component.
        """
        pass

    @staticmethod
    def GetDefaultEvent(*__args):
        """
        GetDefaultEvent(component: object, noCustomTypeDesc: bool) -> EventDescriptor
        
            Returns the default event for a component with a custom type descriptor.
        
            component: The component to get the event for.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: An System.ComponentModel.EventDescriptor with the default event, or null if there are no events.
        GetDefaultEvent(component: object) -> EventDescriptor
        
            Returns the default event for the specified component.
        
            component: The component to get the event for.
            Returns: An System.ComponentModel.EventDescriptor with the default event, or null if there are no events.
        GetDefaultEvent(componentType: Type) -> EventDescriptor
        
            Returns the default event for the specified type of component.
        
            componentType: The System.Type of the target component.
            Returns: An System.ComponentModel.EventDescriptor with the default event, or null if there are no events.
        """
        pass

    @staticmethod
    def GetDefaultProperty(*__args):
        """
        GetDefaultProperty(component: object, noCustomTypeDesc: bool) -> PropertyDescriptor
        
            Returns the default property for the specified component with a custom type descriptor.
        
            component: The component to get the default property for.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: A System.ComponentModel.PropertyDescriptor with the default property, or null if there are no 
             properties.
        
        GetDefaultProperty(component: object) -> PropertyDescriptor
        
            Returns the default property for the specified component.
        
            component: The component to get the default property for.
            Returns: A System.ComponentModel.PropertyDescriptor with the default property, or null if there are no 
             properties.
        
        GetDefaultProperty(componentType: Type) -> PropertyDescriptor
        
            Returns the default property for the specified type of component.
        
            componentType: A System.Type that represents the class to get the property for.
            Returns: A System.ComponentModel.PropertyDescriptor with the default property, or null if there are no 
             properties.
        """
        pass

    @staticmethod
    def GetEditor(*__args):
        """
        GetEditor(type: Type, editorBaseType: Type) -> object
        
            Returns an editor with the specified base type for the specified type.
        
            type: The System.Type of the target component.
            editorBaseType: A System.Type that represents the base type of the editor you are trying to find.
            Returns: An instance of the editor object that can be cast to the given base type, or null if no editor 
             of the requested type can be found.
        
        GetEditor(component: object, editorBaseType: Type, noCustomTypeDesc: bool) -> object
        
            Returns an editor with the specified base type and with a custom type descriptor for the 
             specified component.
        
        
            component: The component to get the editor for.
            editorBaseType: A System.Type that represents the base type of the editor you want to find.
            noCustomTypeDesc: A flag indicating whether custom type description information should be considered.
            Returns: An instance of the editor that can be cast to the specified editor type, or null if no editor of 
             the requested type can be found.
        
        GetEditor(component: object, editorBaseType: Type) -> object
        
            Gets an editor with the specified base type for the specified component.
        
            component: The component to get the editor for.
            editorBaseType: A System.Type that represents the base type of the editor you want to find.
            Returns: An instance of the editor that can be cast to the specified editor type, or null if no editor of 
             the requested type can be found.
        """
        pass

    @staticmethod
    def GetEvents(*__args):
        """
        GetEvents(component: object, noCustomTypeDesc: bool) -> EventDescriptorCollection
        
            Returns the collection of events for a specified component with a custom type descriptor.
        
            component: A component to get the events for.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.
        GetEvents(component: object, attributes: Array[Attribute]) -> EventDescriptorCollection
        
            Returns the collection of events for a specified component using a specified array of attributes 
             as a filter.
        
        
            component: A component to get the events for.
            attributes: An array of type System.Attribute that you can use as a filter.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 
             attributes for this component.
        
        GetEvents(component: object, attributes: Array[Attribute], noCustomTypeDesc: bool) -> EventDescriptorCollection
        
            Returns the collection of events for a specified component using a specified array of attributes 
             as a filter and using a custom type descriptor.
        
        
            component: A component to get the events for.
            attributes: An array of type System.Attribute to use as a filter.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 
             attributes for this component.
        
        GetEvents(componentType: Type) -> EventDescriptorCollection
        
            Returns the collection of events for a specified type of component.
        
            componentType: The System.Type of the target component.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.
        GetEvents(componentType: Type, attributes: Array[Attribute]) -> EventDescriptorCollection
        
            Returns the collection of events for a specified type of component using a specified array of 
             attributes as a filter.
        
        
            componentType: The System.Type of the target component.
            attributes: An array of type System.Attribute that you can use as a filter.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 
             attributes for this component.
        
        GetEvents(component: object) -> EventDescriptorCollection
        
            Returns the collection of events for the specified component.
        
            component: A component to get the events for.
            Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.
        """
        pass

    @staticmethod
    def GetFullComponentName(component):
        """
        GetFullComponentName(component: object) -> str
        
            Returns the fully qualified name of the component.
        
            component: The System.ComponentModel.Component to find the name for.
            Returns: The fully qualified name of the specified component, or null if the component has no name.
        """
        pass

    @staticmethod
    def GetProperties(*__args):
        """
        GetProperties(component: object, noCustomTypeDesc: bool) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified component using the default type descriptor.
        
            component: A component to get the properties for.
            noCustomTypeDesc: true to not consider custom type description information; otherwise, false.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for a specified 
             component.
        
        GetProperties(component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified component using a specified array of 
             attributes as a filter.
        
        
            component: A component to get the properties for.
            attributes: An array of type System.Attribute to use as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 
             specified attributes for the specified component.
        
        GetProperties(component: object, attributes: Array[Attribute], noCustomTypeDesc: bool) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified component using a specified array of 
             attributes as a filter and using a custom type descriptor.
        
        
            component: A component to get the properties for.
            attributes: An array of type System.Attribute to use as a filter.
            noCustomTypeDesc: true to consider custom type description information; otherwise, false.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the events that match the specified 
             attributes for the specified component.
        
        GetProperties(componentType: Type) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified type of component.
        
            componentType: A System.Type that represents the component to get properties for.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for a specified type of 
             component.
        
        GetProperties(componentType: Type, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified type of component using a specified array 
             of attributes as a filter.
        
        
            componentType: The System.Type of the target component.
            attributes: An array of type System.Attribute to use as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 
             specified attributes for this type of component.
        
        GetProperties(component: object) -> PropertyDescriptorCollection
        
            Returns the collection of properties for a specified component.
        
            component: A component to get the properties for.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for the specified 
             component.
        """
        pass

    @staticmethod
    def GetProvider(*__args):
        """
        GetProvider(instance: object) -> TypeDescriptionProvider
        
            Returns the type description provider for the specified component.
        
            instance: An instance of the target component.
            Returns: A System.ComponentModel.TypeDescriptionProvider associated with the specified component.
        GetProvider(type: Type) -> TypeDescriptionProvider
        
            Returns the type description provider for the specified type.
        
            type: The System.Type of the target component.
            Returns: A System.ComponentModel.TypeDescriptionProvider associated with the specified type.
        """
        pass

    @staticmethod
    def GetReflectionType(*__args):
        """
        GetReflectionType(instance: object) -> Type
        
            Returns a System.Type that can be used to perform reflection, given an object.
        
            instance: An instance of the target component.
            Returns: A System.Type for the specified object.
        GetReflectionType(type: Type) -> Type
        
            Returns a System.Type that can be used to perform reflection, given a class type.
        
            type: The System.Type of the target component.
            Returns: A System.Type of the specified class.
        """
        pass

    @staticmethod
    def Refresh(*__args):
        """
        Refresh(module: Module)
            Clears the properties and events for the specified module from the cache.
        
            module: The System.Reflection.Module that represents the module to refresh. Each System.Type in this 
             module will be refreshed.
        
        Refresh(assembly: Assembly)
            Clears the properties and events for the specified assembly from the cache.
        
            assembly: The System.Reflection.Assembly that represents the assembly to refresh. Each System.Type in this 
             assembly will be refreshed.
        
        Refresh(component: object)
            Clears the properties and events for the specified component from the cache.
        
            component: A component for which the properties or events have changed.
        Refresh(type: Type)
            Clears the properties and events for the specified type of component from the cache.
        
            type: The System.Type of the target component.
        """
        pass

    @staticmethod
    def RemoveAssociation(primary, secondary):
        """
        RemoveAssociation(primary: object, secondary: object)
            Removes an association between two objects.
        
            primary: The primary System.Object.
            secondary: The secondary System.Object.
        """
        pass

    @staticmethod
    def RemoveAssociations(primary):
        """
        RemoveAssociations(primary: object)
            Removes all associations for a primary object.
        
            primary: The primary System.Object in an association.
        """
        pass

    @staticmethod
    def RemoveProvider(provider, *__args):
        """
        RemoveProvider(provider: TypeDescriptionProvider, instance: object)
            Removes a previously added type description provider that is associated with the specified 
             object.
        
        
            provider: The System.ComponentModel.TypeDescriptionProvider to remove.
            instance: An instance of the target component.
        RemoveProvider(provider: TypeDescriptionProvider, type: Type)
            Removes a previously added type description provider that is associated with the specified type.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to remove.
            type: The System.Type of the target component.
        """
        pass

    @staticmethod
    def RemoveProviderTransparent(provider, *__args):
        """
        RemoveProviderTransparent(provider: TypeDescriptionProvider, instance: object)
            Removes a previously added type description provider that is associated with the specified 
             object.
        
        
            provider: The System.ComponentModel.TypeDescriptionProvider to remove.
            instance: An instance of the target component.
        RemoveProviderTransparent(provider: TypeDescriptionProvider, type: Type)
            Removes a previously added type description provider that is associated with the specified type.
        
            provider: The System.ComponentModel.TypeDescriptionProvider to remove.
            type: The System.Type of the target component.
        """
        pass

    @staticmethod
    def SortDescriptorArray(infos):
        """
        SortDescriptorArray(infos: IList)
            Sorts descriptors using the name of the descriptor.
        
            infos: An System.Collections.IList that contains the descriptors to sort.
        """
        pass

    ComNativeDescriptorHandler = None
    ComObjectType = None
    InterfaceType = None
    Refreshed = None


class TypeListConverter(TypeConverter):
    """ Provides a type converter that can be used to populate a list box with available types. """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TypeListConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Gets a value indicating whether this converter can convert the specified System.Type of the 
             source object using the given context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: The System.Type of the source object.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TypeListConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you wish to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TypeListConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to the native type of the converter.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that specifies the culture used to represent the font.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TypeListConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: An optional System.Globalization.CultureInfo. If not supplied, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: TypeListConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection of standard values for the data type this validator is designed for.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 
             valid values, or null if the data type does not support a standard set of values.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: TypeListConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether the list of standard values returned from the 
             System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo
             ntext) method is an exclusive list.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because the System.ComponentModel.TypeConverter.StandardValuesCollection returned from 
             System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo
             ntext) is an exhaustive list of possible values. This method never returns false.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: TypeListConverter, context: ITypeDescriptorContext) -> bool
        
            Gets a value indicating whether this object supports a standard set of values that can be picked 
             from a list using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true because 
             System.ComponentModel.TypeListConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorCo
             ntext) should be called to find a common set of values the object supports. This method never 
             returns false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, types: Array[Type]) """
        pass


class UInt16Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 16-bit unsigned integer objects to and from other representations.
    
    UInt16Converter()
    """

class UInt32Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 32-bit unsigned integer objects to and from various other representations.
    
    UInt32Converter()
    """

class UInt64Converter(BaseNumberConverter):
    """
    Provides a type converter to convert 64-bit unsigned integer objects to and from other representations.
    
    UInt64Converter()
    """

class WarningException(SystemException, ISerializable, _Exception):
    """
    Specifies an exception that is handled as a warning instead of an error.
    
    WarningException()
    WarningException(message: str)
    WarningException(message: str, helpUrl: str)
    WarningException(message: str, innerException: Exception)
    WarningException(message: str, helpUrl: str, helpTopic: str)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: WarningException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo with the parameter name and additional 
             exception information.
        
        
            info: Stores the data that was being used to serialize or deserialize the object that the 
             System.ComponentModel.Design.Serialization.CodeDomSerializer was serializing or deserializing.
        
            context: Describes the source and destination of the stream that generated the exception, as well as a 
             means for serialization to retain that context and an additional caller-defined context.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, helpUrl: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, helpUrl: str, helpTopic: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HelpTopic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help topic associated with the warning.

Get: HelpTopic(self: WarningException) -> str

"""

    HelpUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help file associated with the warning.

Get: HelpUrl(self: WarningException) -> str

"""



class Win32Exception(ExternalException, ISerializable, _Exception):
    """
    Throws an exception for a Win32 error code.
    
    Win32Exception()
    Win32Exception(error: int)
    Win32Exception(error: int, message: str)
    Win32Exception(message: str)
    Win32Exception(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: Win32Exception, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the file name and line 
             number at which this System.ComponentModel.Win32Exception occurred.
        
        
            info: A System.Runtime.Serialization.SerializationInfo.
            context: The contextual information about the source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, error: int)
        __new__(cls: type, error: int, message: str)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    NativeErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Win32 error code associated with this exception.

Get: NativeErrorCode(self: Win32Exception) -> int

"""



# variables with complex values

