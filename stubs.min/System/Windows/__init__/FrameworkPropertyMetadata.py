class FrameworkPropertyMetadata(UIPropertyMetadata):
    """
    Reports or applies metadata for a dependency property, specifically adding framework-specific property system characteristics.
    
    FrameworkPropertyMetadata()
    FrameworkPropertyMetadata(defaultValue: object)
    FrameworkPropertyMetadata(propertyChangedCallback: PropertyChangedCallback)
    FrameworkPropertyMetadata(propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
    FrameworkPropertyMetadata(defaultValue: object, propertyChangedCallback: PropertyChangedCallback)
    FrameworkPropertyMetadata(defaultValue: object, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
    FrameworkPropertyMetadata(defaultValue: object, flags: FrameworkPropertyMetadataOptions)
    FrameworkPropertyMetadata(defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback)
    FrameworkPropertyMetadata(defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
    FrameworkPropertyMetadata(defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback, isAnimationProhibited: bool)
    FrameworkPropertyMetadata(defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback, isAnimationProhibited: bool, defaultUpdateSourceTrigger: UpdateSourceTrigger)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, defaultValue: object)
        __new__(cls: type, propertyChangedCallback: PropertyChangedCallback)
        __new__(cls: type, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
        __new__(cls: type, defaultValue: object, propertyChangedCallback: PropertyChangedCallback)
        __new__(cls: type, defaultValue: object, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
        __new__(cls: type, defaultValue: object, flags: FrameworkPropertyMetadataOptions)
        __new__(cls: type, defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback)
        __new__(cls: type, defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback)
        __new__(cls: type, defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback, isAnimationProhibited: bool)
        __new__(cls: type, defaultValue: object, flags: FrameworkPropertyMetadataOptions, propertyChangedCallback: PropertyChangedCallback, coerceValueCallback: CoerceValueCallback, isAnimationProhibited: bool, defaultUpdateSourceTrigger: UpdateSourceTrigger)
        """
        pass

    AffectsArrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a dependency property potentially affects the arrange pass during layout engine operations.

Get: AffectsArrange(self: FrameworkPropertyMetadata) -> bool

Set: AffectsArrange(self: FrameworkPropertyMetadata) = value
"""

    AffectsMeasure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a dependency property potentially affects the measure pass during layout engine operations.

Get: AffectsMeasure(self: FrameworkPropertyMetadata) -> bool

Set: AffectsMeasure(self: FrameworkPropertyMetadata) = value
"""

    AffectsParentArrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a dependency property potentially affects the arrange pass of its parent element's layout during layout engine operations.

Get: AffectsParentArrange(self: FrameworkPropertyMetadata) -> bool

Set: AffectsParentArrange(self: FrameworkPropertyMetadata) = value
"""

    AffectsParentMeasure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a dependency property potentially affects the measure pass of its parent element's layout during layout engine operations.

Get: AffectsParentMeasure(self: FrameworkPropertyMetadata) -> bool

Set: AffectsParentMeasure(self: FrameworkPropertyMetadata) = value
"""

    AffectsRender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a dependency property potentially affects the general layout in some way that does not specifically influence arrangement or measurement, but would require a redraw.

Get: AffectsRender(self: FrameworkPropertyMetadata) -> bool

Set: AffectsRender(self: FrameworkPropertyMetadata) = value
"""

    BindsTwoWayByDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the property binds two-way by default.

Get: BindsTwoWayByDefault(self: FrameworkPropertyMetadata) -> bool

Set: BindsTwoWayByDefault(self: FrameworkPropertyMetadata) = value
"""

    DefaultUpdateSourceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default for System.Windows.Data.UpdateSourceTrigger to use when bindings for the property with this metadata are applied, which have their System.Windows.Data.UpdateSourceTrigger set to System.Windows.Data.UpdateSourceTrigger.Default.

Get: DefaultUpdateSourceTrigger(self: FrameworkPropertyMetadata) -> UpdateSourceTrigger

Set: DefaultUpdateSourceTrigger(self: FrameworkPropertyMetadata) = value
"""

    Inherits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the value of the dependency property is inheritable.

Get: Inherits(self: FrameworkPropertyMetadata) -> bool

Set: Inherits(self: FrameworkPropertyMetadata) = value
"""

    IsDataBindingAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether data binding is supported for the dependency property.

Get: IsDataBindingAllowed(self: FrameworkPropertyMetadata) -> bool

"""

    IsNotDataBindable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the dependency property supports data binding.

Get: IsNotDataBindable(self: FrameworkPropertyMetadata) -> bool

Set: IsNotDataBindable(self: FrameworkPropertyMetadata) = value
"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether the metadata has been applied to a property in some way, resulting in the immutable state of that metadata instance.

"""

    Journal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether this property contains journaling information that applications can or should store as part of a journaling implementation.

Get: Journal(self: FrameworkPropertyMetadata) -> bool

Set: Journal(self: FrameworkPropertyMetadata) = value
"""

    OverridesInheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the property value inheritance evaluation should span across certain content boundaries in the logical tree of elements.

Get: OverridesInheritanceBehavior(self: FrameworkPropertyMetadata) -> bool

Set: OverridesInheritanceBehavior(self: FrameworkPropertyMetadata) = value
"""

    SubPropertiesDoNotAffectRender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether sub-properties of the dependency property do not affect the rendering of the containing object.

Get: SubPropertiesDoNotAffectRender(self: FrameworkPropertyMetadata) -> bool

Set: SubPropertiesDoNotAffectRender(self: FrameworkPropertyMetadata) = value
"""


