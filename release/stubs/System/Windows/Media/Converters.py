# encoding: utf-8
# module System.Windows.Media.Converters calls itself Converters
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BaseIListConverter(TypeConverter):
    """ Defines methods used to convert System.Collections.IList collection members to and from instances of System.String. """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: BaseIListConverter, td: ITypeDescriptorContext, t: Type) -> bool
        
            Determines if a given type can be converted.
        
            td: Provides contextual information required for conversion.
            t: Type being evaluated for conversion.
            Returns: true if this type can be converted; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: BaseIListConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines if a given type can be converted to a System.String.
        
            context: Provides contextual information required for conversion.
            destinationType: Type being evaluated for conversion.
            Returns: true if this type can be converted; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: BaseIListConverter, td: ITypeDescriptorContext, ci: CultureInfo, value: object) -> object
        
            Converts a System.String to a supported instance of System.Collections.IList.
        
            td: Provides contextual information required for conversion.
            ci: Cultural information to respect during conversion.
            value: String used for conversion.
            Returns: An System.Object that represents the result of the conversion.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: BaseIListConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a supported instance of System.Collections.IList to a System.String.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information to respect during conversion.
            value: Object being evaluated for conversion.
            destinationType: Destination type being evaluated for conversion.
            Returns: String representation of the System.Collections.IList collection.
        """
        pass


class BoolIListConverter(BaseIListConverter):
    """
    Converts the members of an System.Collections.IList collection of Boolean values to and from instances of System.String.
    
    BoolIListConverter()
    """

class BrushValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.Brush.
    
    BrushValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: BrushValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of System.Windows.Media.Brush 
             is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: BrushValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.Brush can be converted to a System.String.
        
            value: Instance of System.Windows.Media.Brush to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: BrushValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.Brush.
        
            value: System.String value to convert into a System.Windows.Media.Brush.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.Brush based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: BrushValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.Brush to a System.String.
        
            value: Instance of System.Windows.Media.Brush to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.Brush object.
        """
        pass


class CacheModeValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.CacheMode.
    
    CacheModeValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: CacheModeValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines whether the specified System.String can be converted to an instance of 
             System.Windows.Media.CacheMode.
        
        
            value: A System.String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: CacheModeValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines whether the specified instance of System.Windows.Media.CacheMode can be converted to 
             a System.String.
        
        
            value: An instance of System.Windows.Media.CacheMode to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: CacheModeValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.CacheMode.
        
            value: A System.String value to convert into a System.Windows.Media.CacheMode.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Media.CacheMode based on the specified value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: CacheModeValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.CacheMode to a System.String.
        
            value: An instance of System.Windows.Media.CacheMode to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: A System.String representation of the specified System.Windows.Media.CacheMode object.
        """
        pass


class CharIListConverter(BaseIListConverter):
    """
    Converts the members of an System.Collections.IList collection of Unicode characters to and from instances of System.String.
    
    CharIListConverter()
    """

class DoubleCollectionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.DoubleCollection.
    
    DoubleCollectionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: DoubleCollectionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.DoubleCollection is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: DoubleCollectionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.DoubleCollection can be converted to a 
             System.String.
        
        
            value: Instance of System.Windows.Media.DoubleCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: DoubleCollectionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.DoubleCollection.
        
            value: System.String value to convert into a System.Windows.Media.DoubleCollection.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.DoubleCollection based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: DoubleCollectionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.DoubleCollection to a System.String.
        
            value: Instance of System.Windows.Media.DoubleCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.DoubleCollection object.
        """
        pass


class DoubleIListConverter(BaseIListConverter):
    """
    Converts members of an System.Collections.IList collection containing System.Double numbers to and from instances of System.String.
    
    DoubleIListConverter()
    """

class GeometryValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.Geometry.
    
    GeometryValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: GeometryValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.Geometry is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: GeometryValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.Geometry can be converted to a System.String.
        
            value: Instance of System.Windows.Media.Geometry to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: GeometryValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.Geometry.
        
            value: System.String value to convert into a System.Windows.Media.Geometry.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.Geometry based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: GeometryValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.Geometry to a System.String.
        
            value: Instance of System.Windows.Media.Geometry to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.Geometry object.
        """
        pass


class Int32CollectionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.Int32Collection.
    
    Int32CollectionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: Int32CollectionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Converts an instance of System.Windows.Media.Int32Collection to a System.String.
        
            value: Instance of System.Windows.Media.Int32Collection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.Int32Collection object.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: Int32CollectionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Converts a System.String into a System.Windows.Media.Int32Collection.
        
            value: System.String value to convert into a System.Windows.Media.Int32Collection.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.Int32Collection based on the supplied value.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: Int32CollectionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Determines if an instance of System.Windows.Media.Int32Collection can be converted to a 
             System.String.
        
        
            value: Instance of System.Windows.Media.Int32Collection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: Int32CollectionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.Int32Collection is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass


class PathFigureCollectionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.PathFigureCollection.
    
    PathFigureCollectionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: PathFigureCollectionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.PathFigureCollection is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: PathFigureCollectionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.PathFigureCollection can be converted to a 
             System.String.
        
        
            value: Instance of System.Windows.Media.PathFigureCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: PathFigureCollectionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.PathFigureCollection.
        
            value: System.String value to convert into a System.Windows.Media.PathFigureCollection.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.PathFigureCollection based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: PathFigureCollectionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.PathFigureCollection to a System.String
        
            value: Instance of System.Windows.Media.PathFigureCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.PathFigureCollection object.
        """
        pass


class PointCollectionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.PointCollection.
    
    PointCollectionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: PointCollectionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.PointCollection is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: PointCollectionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.PointCollection can be converted to a 
             System.String.
        
        
            value: Instance of System.Windows.Media.PointCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: PointCollectionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.PointCollection.
        
            value: System.String value to convert into a System.Windows.Media.PointCollection.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.PointCollection based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: PointCollectionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.PointCollection to a System.String.
        
            value: Instance of System.Windows.Media.PointCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.PointCollection object.
        """
        pass


class PointIListConverter(BaseIListConverter):
    """
    Converts an System.Collections.IList collection of System.Windows.Point values to and from instances of System.String.
    
    PointIListConverter()
    """

class TransformValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.Transform.
    
    TransformValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: TransformValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.Transform is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: TransformValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.Transform can be converted to a System.String.
        
            value: Instance of System.Windows.Media.Transform to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: TransformValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.Transform.
        
            value: System.String value to convert into a System.Windows.Media.Transform.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.Transform based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: TransformValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.Transform to a System.String.
        
            value: Instance of System.Windows.Media.Transform to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.Transform object.
        """
        pass


class UShortIListConverter(BaseIListConverter):
    """
    Converts an System.Collections.IList collection of UShort number values to and from instances of System.String.
    
    UShortIListConverter()
    """

class VectorCollectionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.VectorCollection.
    
    VectorCollectionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: VectorCollectionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if conversion from a given System.String to an instance of 
             System.Windows.Media.VectorCollection is possible.
        
        
            value: String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if the value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: VectorCollectionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.VectorCollection can be converted to a 
             System.String.
        
        
            value: Instance of System.Windows.Media.VectorCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: VectorCollectionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Media.VectorCollection.
        
            value: System.String value to convert into a System.Windows.Media.VectorCollection.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.VectorCollection based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: VectorCollectionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.VectorCollection to a System.String.
        
            value: Instance of System.Windows.Media.VectorCollection to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.VectorCollection object.
        """
        pass


