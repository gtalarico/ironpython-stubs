class PathFigureCollectionConverter(TypeConverter):
    """
    Converts instances of other types to and from a System.Windows.Media.PathFigureCollection.
    
    PathFigureCollectionConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: PathFigureCollectionConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Indicates whether an object can be converted from a given type to an instance of a System.Windows.Media.PathFigureCollection.
        
            context: Describes the context information of a type.
            sourceType: The source System.Type that is being queried for conversion support.
            Returns: true if object of the specified type can be converted to a System.Windows.Media.PathFigureCollection; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: PathFigureCollectionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether instances of System.Windows.Media.PathFigureCollection can be converted to the specified type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Media.PathFigureCollection is being evaluated to be converted to.
            Returns: true if instances of System.Windows.Media.PathFigureCollection can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: PathFigureCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to a System.Windows.Media.PathFigureCollection.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The object being converted.
            Returns: The System.Windows.Media.PathFigureCollection created from converting value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: PathFigureCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.Media.PathFigureCollection to the specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The System.Windows.Media.PathFigureCollection to convert.
            destinationType: The type to convert the System.Windows.Media.PathFigureCollection to.
            Returns: An System.Object that represents the converted value.
        """
        pass

