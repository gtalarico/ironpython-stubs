class NullableBoolConverter(NullableConverter):
    """
    Converts to and from the System.Nullable type (using the System.Boolean type constraint on the generic).
    
    NullableBoolConverter()
    """
    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: NullableBoolConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Returns a collection of standard values for the data type that this type converter is designed for.
        
            context: Provides contextual information about a component, such as its container and property descriptor.
            Returns: A collection that holds a standard set of valid values. For this implementation, those values are true, false, and null.
        """
        pass

    def GetStandardValuesExclusive(self, context=None):
        """
        GetStandardValuesExclusive(self: NullableBoolConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether the collection of standard values returned from System.Windows.NullableBoolConverter.GetStandardValues(System.ComponentModel.ITypeDescriptorContext) is an exclusive list.
        
            context: Provides contextual information about a component, such as its container and property descriptor.
            Returns: This implementation always returns true.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: NullableBoolConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether this object supports a standard set of values that can be picked from a list.
        
            context: Provides contextual information about a component, such as its container and property descriptor.
            Returns: This implementation always returns true.
        """
        pass

