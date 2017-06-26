class ItemContainerTemplate(DataTemplate, INameScope, ISealable, IHaveResources, IQueryAmbient):
    """ ItemContainerTemplate() """
    def ValidateTemplatedParent(self, *args): #cannot find CLR method
        """
        ValidateTemplatedParent(self: DataTemplate, templatedParent: FrameworkElement)
            Checks the templated parent against a set of rules.
        
            templatedParent: The element this template is applied to.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ItemContainerTemplateKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemContainerTemplateKey(self: ItemContainerTemplate) -> object

"""


