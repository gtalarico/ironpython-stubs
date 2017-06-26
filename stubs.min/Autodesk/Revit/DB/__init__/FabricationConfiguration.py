class FabricationConfiguration(Element, IDisposable):
    """ This element contains the information about the fabrication configuration settings used by the project. """
    def CanBeSwapped(self):
        """
        CanBeSwapped(self: FabricationConfiguration) -> bool
        
            Checks if the fabrication configuration can be swapped.
            Returns: True if the fabrication configuration can be swapped, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAllFabricationConnectorDefinitions(self, domain, shape):
        """
        GetAllFabricationConnectorDefinitions(self: FabricationConfiguration, domain: ConnectorDomainType, shape: ConnectorProfileType) -> IList[int]
        
            Gets fabrication connector identifiers from the fabrication configuration, 
             filtered by shape and domain.
        
        
            domain: ConnectorDomainType to filter by. Pass ConnectorDomainType.Undefined to get all 
             connector domains.
        
            shape: ConnectorProfileType to filter by. Pass ConnectorProfileType.Invalid to get all 
             shapes.
        
            Returns: All the fabrication connector identifiers, filtered by shape and domain. The 
             return will be empty if no connectors are found.
        """
        pass

    def GetAllInsulationSpecifications(self, pFabPart):
        """
        GetAllInsulationSpecifications(self: FabricationConfiguration, pFabPart: FabricationPart) -> IList[int]
        
            Gets all insulation specification identifiers in the fabrication configuration.
        
            pFabPart: The fabrication part.
            Returns: An array of insulation specification identifiers.
        """
        pass

    def GetAllLoadedServices(self):
        """
        GetAllLoadedServices(self: FabricationConfiguration) -> IList[FabricationService]
        
            Returns all the loaded fabrication services.
            Returns: All the loaded fabrication services.
        """
        pass

    def GetAllMaterials(self, part):
        """
        GetAllMaterials(self: FabricationConfiguration, part: FabricationPart) -> IList[int]
        
            Gets all material identifiers in the fabrication configuration.
        
            part: The fabrication part.
            Returns: An array of material identifiers.
        """
        pass

    def GetAllServices(self):
        """
        GetAllServices(self: FabricationConfiguration) -> IList[FabricationService]
        
            Returns all fabrication services in the fabrication configuration.
            Returns: All fabrication services. The return will be empty if no services are found.
        """
        pass

    def GetAllSpecifications(self, part):
        """
        GetAllSpecifications(self: FabricationConfiguration, part: FabricationPart) -> IList[int]
        
            Gets all specification identifiers in the fabrication configuration.
        
            part: The fabrication part.
            Returns: An array of specification identifiers.
        """
        pass

    def GetAllUsedServices(self):
        """
        GetAllUsedServices(self: FabricationConfiguration) -> IList[FabricationService]
        
            Returns all the used fabrication services. A service is used if any fabrication 
             part in the service is created by user.
        
            Returns: All the used fabrication services.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetFabricationConfiguration(doc):
        """
        GetFabricationConfiguration(doc: Document) -> FabricationConfiguration
        
            Gets the fabrication configuration element in the document.
        
            doc: The document.
            Returns: The fabrication configuration element in the document.
        """
        pass

    def GetFabricationConfigurationInfo(self):
        """
        GetFabricationConfigurationInfo(self: FabricationConfiguration) -> FabricationConfigurationInfo
        
            Gets the information about the fabrication configuration of the project.
            Returns: The information about the fabrication configuration of the project.
        """
        pass

    def GetFabricationConnectorDomain(self, fabricationConnectorId):
        """
        GetFabricationConnectorDomain(self: FabricationConfiguration, fabricationConnectorId: int) -> ConnectorDomainType
        
            Gets the fabrication connector domain from its identifier.
        
            fabricationConnectorId: The fabrication connector identifier.
            Returns: The fabrication connector's domain.
        """
        pass

    def GetFabricationConnectorGroup(self, fabricationConnectorId):
        """
        GetFabricationConnectorGroup(self: FabricationConfiguration, fabricationConnectorId: int) -> str
        
            Gets the fabrication connector group from its identifier.
        
            fabricationConnectorId: The fabrication connector identifier.
            Returns: The fabrication connector's group.
        """
        pass

    def GetFabricationConnectorName(self, fabricationConnectorId):
        """
        GetFabricationConnectorName(self: FabricationConfiguration, fabricationConnectorId: int) -> str
        
            Gets the fabrication connector name from its identifier.
        
            fabricationConnectorId: The fabrication connector identifier.
            Returns: The fabrication connector's name.
        """
        pass

    def GetFabricationConnectorShape(self, fabricationConnectorId):
        """
        GetFabricationConnectorShape(self: FabricationConfiguration, fabricationConnectorId: int) -> ConnectorProfileType
        
            Gets the fabrication connector shape from its identifier.
        
            fabricationConnectorId: The fabrication connector identifier.
            Returns: The fabrication connector's shape.
        """
        pass

    def GetInsulationSpecificationAbbreviation(self, insulationSpecificationId):
        """
        GetInsulationSpecificationAbbreviation(self: FabricationConfiguration, insulationSpecificationId: int) -> str
        
            Gets insulation specification abbreviation.
        
            insulationSpecificationId: The insulation specification identifier.
        """
        pass

    def GetInsulationSpecificationGroup(self, specId):
        """
        GetInsulationSpecificationGroup(self: FabricationConfiguration, specId: int) -> str
        
            Gets the insulation specification group from its identifier.
        
            specId: The insulation specification identifier.
            Returns: The insulation specification group.
        """
        pass

    def GetInsulationSpecificationName(self, specId):
        """
        GetInsulationSpecificationName(self: FabricationConfiguration, specId: int) -> str
        
            Gets the insulation specification name from its identifier.
        
            specId: The insulation specification identifier.
            Returns: The insulation specification name.
        """
        pass

    def GetMaterialAbbreviation(self, materialId):
        """
        GetMaterialAbbreviation(self: FabricationConfiguration, materialId: int) -> str
        
            Gets the abreviation of the material or the insulation or the double wall 
             material.
        
        
            materialId: The material identifier.
        """
        pass

    def GetMaterialGroup(self, materialId):
        """
        GetMaterialGroup(self: FabricationConfiguration, materialId: int) -> str
        
            Gets material group from its identifier.
        
            materialId: The material identifier.
            Returns: The material group.
        """
        pass

    def GetMaterialName(self, materialId):
        """
        GetMaterialName(self: FabricationConfiguration, materialId: int) -> str
        
            Gets material name from its identifier.
        
            materialId: The material identifier.
            Returns: The material name without the group.
        """
        pass

    def GetMaterialThickness(self, materialId, gaugeId):
        """
        GetMaterialThickness(self: FabricationConfiguration, materialId: int, gaugeId: int) -> float
        
            Gets material thickness from its material/gauge identifiers.
        
            materialId: The material identifier.
            gaugeId: The gauge identifier within the specified material.
            Returns: The thickness of the material/gauge.
        """
        pass

    def GetProfile(self):
        """
        GetProfile(self: FabricationConfiguration) -> str
        
            Return the profile of the loaded fabrication configuration. Return empty string 
             for global profile.
        """
        pass

    def GetService(self, serviceId):
        """
        GetService(self: FabricationConfiguration, serviceId: int) -> FabricationService
        
            Get the service based on the service identifier from the fabrication 
             configuration in the current document.
        
        
            serviceId: The service identifier.
            Returns: The service based on the service identifier.
        """
        pass

    def GetSpecificationAbbreviation(self, specificationId):
        """
        GetSpecificationAbbreviation(self: FabricationConfiguration, specificationId: int) -> str
        
            Gets specification abreviation.
        
            specificationId: The specification identifier.
        """
        pass

    def GetSpecificationGroup(self, specId):
        """
        GetSpecificationGroup(self: FabricationConfiguration, specId: int) -> str
        
            Gets the specification group from its identifier.
        
            specId: The specification identifier.
            Returns: The specification group.
        """
        pass

    def GetSpecificationName(self, specId):
        """
        GetSpecificationName(self: FabricationConfiguration, specId: int) -> str
        
            Gets the specification name from its identifier.
        
            specId: The specification identifier.
            Returns: The specification name;
        """
        pass

    def HasValidConfiguration(self):
        """
        HasValidConfiguration(self: FabricationConfiguration) -> bool
        
            Checks whether a valid fabrication configuration has been set for the project.
            Returns: True if a valid fabrication configuration has been set for the project.
        """
        pass

    def LoadServices(self, serviceIds):
        """ LoadServices(self: FabricationConfiguration, serviceIds: IList[int]) -> IList[int] """
        pass

    def LocateFabricationConnector(self, group, name, domain, shape):
        """
        LocateFabricationConnector(self: FabricationConfiguration, group: str, name: str, domain: ConnectorDomainType, shape: ConnectorProfileType) -> int
        
            Gets the fabrication connector identifiers by group and name, filtered by shape 
             and domain.
        
        
            group: The fabrication connector group.
            name: The fabrication connector name.
            domain: ConnectorDomainType to filter by. Pass ConnectorDomainType::Undefined to get 
             all connector domains.
        
            shape: ConnectorProfileType to filter by. Pass ConnectorProfileType::Invalid to get 
             all shapes.
        
            Returns: Return the fabrication connector identifier. Returns -1 if not found.
        """
        pass

    def LocateInsulationSpecification(self, group, name):
        """
        LocateInsulationSpecification(self: FabricationConfiguration, group: str, name: str) -> int
        
            Gets the insulation specification by group and name.
        
            group: The insulation specification group.
            name: The insulation specification name.
            Returns: The insulation specification identifier. Returns -1 if not found.
        """
        pass

    def LocateMaterial(self, group, name):
        """
        LocateMaterial(self: FabricationConfiguration, group: str, name: str) -> int
        
            Gets material by group and name.
        
            group: The material group.
            name: The group name.
            Returns: The material identifier. Returns -1 if not found.
        """
        pass

    def LocateSpecification(self, group, name):
        """
        LocateSpecification(self: FabricationConfiguration, group: str, name: str) -> int
        
            Gets the specification identifier by group and name.
        
            group: The specification group.
            name: The specification name.
            Returns: The specification identifier. Returns -1 if not found.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def ReloadConfiguration(self):
        """
        ReloadConfiguration(self: FabricationConfiguration) -> ConfigurationReloadInfo
        
            Reloads the fabrication configuration from its source fabrication configuration.
            Returns: The information about the reload of the fabrication configuration.
        """
        pass

    def SetConfiguration(self, fabricationConfigurationInfo, profile=None):
        """
        SetConfiguration(self: FabricationConfiguration, fabricationConfigurationInfo: FabricationConfigurationInfo)
            Set the fabrication configuration with global profile.
        
            fabricationConfigurationInfo: The desired fabrication configuration.
        SetConfiguration(self: FabricationConfiguration, fabricationConfigurationInfo: FabricationConfigurationInfo, profile: str)
            Set the fabrication configuration with specific profile.
        
            fabricationConfigurationInfo: The desired fabrication configuration.
            profile: The desired profile of the fabrication configuration. Use empty string for the 
             global profile.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def UnloadServices(self, serviceIds):
        """ UnloadServices(self: FabricationConfiguration, serviceIds: IList[int]) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

