class IExternalCommandAvailability:
    """ An interface that should be implemented to provide the implementation for a accessibility check for a Revit add-in External Command. """
    def IsCommandAvailable(self, applicationData, selectedCategories):
        """
        IsCommandAvailable(self: IExternalCommandAvailability, applicationData: UIApplication, selectedCategories: CategorySet) -> bool
        
            Implement this method to provide control over whether your external command is 
             enabled or disabled.
        
        
            applicationData: An ApplicationServices.Application object which contains reference to 
             Application
        needed by external command.
        
            selectedCategories: An list of categories of the elements which have been selected in Revit in the 
             active document, 
        or an empty set if no elements are selected or there is no 
             active document.
        
            Returns: Indicates whether Revit should enable or disable the corresponding external 
             command.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

