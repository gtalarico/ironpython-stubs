# encoding: utf-8
# module System.Windows.Forms.Layout calls itself Layout
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ArrangedElementCollection(object, IList, ICollection, IEnumerable):
    """ Represents a collection of objects. """
    def CopyTo(self, array, index):
        """
        CopyTo(self: ArrangedElementCollection, array: Array, index: int)
            Copies the entire contents of this collection to a compatible one-dimensional System.Array, 
             starting at the specified index of the target array.
        
        
            array: The one-dimensional System.Array that is the destination of the elements copied from the current 
             collection. The array must have zero-based indexing.
        
            index: The zero-based index in array at which copying begins.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ArrangedElementCollection, obj: object) -> bool
        
            Determines whether two System.Windows.Forms.Layout.ArrangedElementCollection instances are equal.
        
            obj: The System.Windows.Forms.Layout.ArrangedElementCollection to compare with the current 
             System.Windows.Forms.Layout.ArrangedElementCollection.
        
            Returns: true if the specified System.Windows.Forms.Layout.ArrangedElementCollection is equal to the 
             current System.Windows.Forms.Layout.ArrangedElementCollection; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ArrangedElementCollection) -> IEnumerator
        
            Returns an enumerator for the entire collection.
            Returns: An System.Collections.IEnumerator for the entire collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ArrangedElementCollection) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current System.Windows.Forms.Layout.ArrangedElementCollection.
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

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: ArrangedElementCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the collection is read-only.

Get: IsReadOnly(self: ArrangedElementCollection) -> bool

"""



class LayoutEngine(object):
    """ Provides the base class for implementing layout engines. """
    def InitLayout(self, child, specified):
        """
        InitLayout(self: LayoutEngine, child: object, specified: BoundsSpecified)
            Initializes the layout engine.
        
            child: The container on which the layout engine will operate.
            specified: The bounds defining the container's size and position.
        """
        pass

    def Layout(self, container, layoutEventArgs):
        """
        Layout(self: LayoutEngine, container: object, layoutEventArgs: LayoutEventArgs) -> bool
        
            Requests that the layout engine perform a layout operation.
        
            container: The container on which the layout engine will operate.
            layoutEventArgs: An event argument from a System.Windows.Forms.Control.Layout event.
            Returns: true if layout should be performed again by the parent of container; otherwise, false.
        """
        pass


class TableLayoutSettingsTypeConverter(TypeConverter):
    """
    Provides a unified way of converting types of values to other types, as well as for accessing standard values and subproperties.
    
    TableLayoutSettingsTypeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TableLayoutSettingsTypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this converter can convert an object in the given source type to the native 
             type of this converter.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TableLayoutSettingsTypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value indicating whether this converter can convert an object to the given destination 
             type by using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TableLayoutSettingsTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the type of this converter by using the specified context and 
             culture information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TableLayoutSettingsTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type by using the specified context and culture 
             information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        """
        pass


