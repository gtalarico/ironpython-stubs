class DependencyPropertyKey(object):
    """ Provides a dependency property identifier for limited write access to a read-only dependency property. """
    def OverrideMetadata(self, forType, typeMetadata):
        """
        OverrideMetadata(self: DependencyPropertyKey, forType: Type, typeMetadata: PropertyMetadata)
            Overrides the metadata of a read-only dependency property that is represented by this dependency property identifier.
        
            forType: The type on which this dependency property exists and metadata should be overridden.
            typeMetadata: Metadata supplied for this type.
        """
        pass

    DependencyProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the dependency property identifier associated with this specialized read-only dependency property identifier.

Get: DependencyProperty(self: DependencyPropertyKey) -> DependencyProperty

"""


