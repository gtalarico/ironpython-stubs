class DependencyPropertyDescriptor(PropertyDescriptor):
    """ Provides an extension of System.ComponentModel.PropertyDescriptor that accounts for the additional property characteristics of a dependency property. """
    def AddValueChanged(self, component, handler):
        """
        AddValueChanged(self: DependencyPropertyDescriptor, component: object, handler: EventHandler)
            Enables other objects to be notified when this property changes.
        
            component: The component to add the handler for.
            handler: The delegate to add as a listener.
        """
        pass

    def CanResetValue(self, component):
        """
        CanResetValue(self: DependencyPropertyDescriptor, component: object) -> bool
        
            Returns whether resetting an object changes its value.
        
            component: The component to test for reset capability.
            Returns: true if resetting the component changes its value; otherwise, false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DependencyPropertyDescriptor, obj: object) -> bool
        
            Compares two System.ComponentModel.DependencyPropertyDescriptor instances for equality.
        
            obj: The System.ComponentModel.DependencyPropertyDescriptor  to compare with the current instance.
            Returns: true if the values are equivalent; otherwise, false.
        """
        pass

    @staticmethod
    def FromName(name, ownerType, targetType, ignorePropertyType=None):
        """
        FromName(name: str, ownerType: Type, targetType: Type, ignorePropertyType: bool) -> DependencyPropertyDescriptor
        
            Returns a System.ComponentModel.DependencyPropertyDescriptor for a provided property name.
        
            name: The registered name of a dependency property or an attached property.
            ownerType: The System.Type of the object that owns the property definition.
            targetType: The System.Type of the object you want to set the property for.
            ignorePropertyType: Specifies to ignore the property type.
            Returns: The requested System.ComponentModel.DependencyPropertyDescriptor.
        FromName(name: str, ownerType: Type, targetType: Type) -> DependencyPropertyDescriptor
        
            Returns a System.ComponentModel.DependencyPropertyDescriptor for a provided property name.
        
            name: The registered name of a dependency property or an attached property.
            ownerType: The System.Type of the object that owns the property definition.
            targetType: The System.Type of the object you want to set the property for.
            Returns: The requested System.ComponentModel.DependencyPropertyDescriptor.
        """
        pass

    @staticmethod
    def FromProperty(*__args):
        """
        FromProperty(dependencyProperty: DependencyProperty, targetType: Type) -> DependencyPropertyDescriptor
        
            Returns a System.ComponentModel.DependencyPropertyDescriptor for a provided dependency property and target type.
        
            dependencyProperty: The identifier for a dependency property.
            targetType: The type of the object where the property is set.
            Returns: A System.ComponentModel.DependencyPropertyDescriptor for the provided dependency property.
        FromProperty(property: PropertyDescriptor) -> DependencyPropertyDescriptor
        
            Returns a System.ComponentModel.DependencyPropertyDescriptor for a provided System.ComponentModel.PropertyDescriptor.
        
            property: The System.ComponentModel.PropertyDescriptor to check.
            Returns: If the property described by property is a dependency property, returns a valid System.ComponentModel.DependencyPropertyDescriptor. Otherwise, returns a 
             nullSystem.ComponentModel.DependencyPropertyDescriptor.
        """
        pass

    def GetChildProperties(self, *__args):
        """
        GetChildProperties(self: DependencyPropertyDescriptor, instance: object, filter: Array[Attribute]) -> PropertyDescriptorCollection
        
            Returns a System.ComponentModel.PropertyDescriptorCollection.
        
            instance: A component to get the properties for.
            filter: An array of type System.Attribute to use as a filter.
            Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the specified attributes for the specified component.
        """
        pass

    def GetEditor(self, editorBaseType):
        """
        GetEditor(self: DependencyPropertyDescriptor, editorBaseType: Type) -> object
        
            Gets an editor of the specified type.
        
            editorBaseType: The base type of editor, which is used to differentiate between multiple editors that a property supports.
            Returns: An instance of the requested editor type, or null if an editor cannot be found.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DependencyPropertyDescriptor) -> int
        
            Returns the hash code for this System.ComponentModel.DependencyPropertyDescriptor.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def GetValue(self, component):
        """
        GetValue(self: DependencyPropertyDescriptor, component: object) -> object
        
            Resturns the current value of the property on a component.
        
            component: The component instance.
            Returns: The requested value.
        """
        pass

    def RemoveValueChanged(self, component, handler):
        """
        RemoveValueChanged(self: DependencyPropertyDescriptor, component: object, handler: EventHandler)
            Enables other objects to be notified when this property changes.
        
            component: The component to add the handler for.
            handler: The delegate to add as a listener.
        """
        pass

    def ResetValue(self, component):
        """
        ResetValue(self: DependencyPropertyDescriptor, component: object)
            Resets the value for this property of the component to the default value.
        
            component: The component with the property value that is to be reset to the default value.
        """
        pass

    def SetValue(self, component, value):
        """
        SetValue(self: DependencyPropertyDescriptor, component: object, value: object)
            Sets the value of the component to a different value.
        
            component: The component with the property value that is to be set.
            value: The new value.
        """
        pass

    def ShouldSerializeValue(self, component):
        """
        ShouldSerializeValue(self: DependencyPropertyDescriptor, component: object) -> bool
        
            Indicates whether the value of this property needs to be persisted by serialization processes.
        
            component: The component with the property to be examined for persistence.
            Returns: true if the property should be persisted; otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: DependencyPropertyDescriptor) -> str
        
            Converts the value of this instance to its equivalent string representation.
            Returns: Returns the System.ComponentModel.MemberDescriptor.Name value.
        """
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of attributes.

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of attributes for this member.

Get: Attributes(self: DependencyPropertyDescriptor) -> AttributeCollection

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the category that the member belongs to, as specified in the System.ComponentModel.CategoryAttribute.

Get: Category(self: DependencyPropertyDescriptor) -> str

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the component this property is bound to.

Get: ComponentType(self: DependencyPropertyDescriptor) -> Type

"""

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type converter for this property.

Get: Converter(self: DependencyPropertyDescriptor) -> TypeConverter

"""

    DependencyProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the dependency property identifier.

Get: DependencyProperty(self: DependencyPropertyDescriptor) -> DependencyProperty

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the description of the member, as specified in the System.ComponentModel.DescriptionAttribute.

Get: Description(self: DependencyPropertyDescriptor) -> str

"""

    DesignerCoerceValueCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a callback that designers use to modify the effective value of a dependency property before the dependency property value is stored in the dependency property engine.

Get: DesignerCoerceValueCallback(self: DependencyPropertyDescriptor) -> CoerceValueCallback

Set: DesignerCoerceValueCallback(self: DependencyPropertyDescriptor) = value
"""

    DesignTimeOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this member should be set only at design time, as specified in the System.ComponentModel.DesignOnlyAttribute.

Get: DesignTimeOnly(self: DependencyPropertyDescriptor) -> bool

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name that can be displayed in a window, such as a Properties window.

Get: DisplayName(self: DependencyPropertyDescriptor) -> str

"""

    IsAttached = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the property is registered as an attached property and is being used through an attached usage.

Get: IsAttached(self: DependencyPropertyDescriptor) -> bool

"""

    IsBrowsable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the value of the System.ComponentModel.BrowsableAttribute on the property.

Get: IsBrowsable(self: DependencyPropertyDescriptor) -> bool

"""

    IsLocalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this property should be localized, as specified in the System.ComponentModel.LocalizableAttribute.

Get: IsLocalizable(self: DependencyPropertyDescriptor) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this property is read-only.

Get: IsReadOnly(self: DependencyPropertyDescriptor) -> bool

"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the metadata associated with the dependency property.

Get: Metadata(self: DependencyPropertyDescriptor) -> PropertyMetadata

"""

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash code for the name of the member, as specified in System.String.GetHashCode.

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the represented System.Type of the dependency property.

Get: PropertyType(self: DependencyPropertyDescriptor) -> Type

"""

    SupportsChangeEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether value change notifications for this property may originate from outside the property descriptor, such as from the component itself, or whether notifications will only originate from direct calls made to System.ComponentModel.DependencyPropertyDescriptor.SetValue(System.Object,System.Object).

Get: SupportsChangeEvents(self: DependencyPropertyDescriptor) -> bool

"""


