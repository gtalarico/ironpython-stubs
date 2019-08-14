from System.Collections.Generic import *
from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Zones calls itself Zones
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RightValueExtensions():
    # no doc
    Instance = RightValueExtensions
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def IsPermitted(value):
        """ IsPermitted(value: RightValue) -> bool """
        pass

    __all__ = [
        'IsPermitted',
    ]


class Zone(DbObject):
    """ Zone() """
    Instance = Zone
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Active(self: Zone) -> bool

Set: Active(self: Zone) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Description(self: Zone) -> str

Set: Description(self: Zone) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Id(self: Zone) -> int

Set: Id(self: Zone) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: Zone) -> str

Set: Name(self: Zone) = value
"""

    Rights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Rights(self: Zone) -> ZoneRights

Set: Rights(self: Zone) = value
"""

    Sys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Sys(self: Zone) -> bool

Set: Sys(self: Zone) = value
"""



class ZoneRights(DbObject):
    """ ZoneRights() """
    Instance = ZoneRights
    """hardcoded/returns an instance of the class"""
    @staticmethod
    def FromString(zoneRightsString):
        """
        FromString(zoneRightsString: str) -> ZoneRights
        
            Creates a new ZoneRights object and sets the properties with the string wich is retrieved from 
                    the database.
        
            zoneRightsString: A System.String with the properties of the Wms.RemotingObjects.Zones.ZoneRights object and its
                    values.
            Returns: A new Wms.RemotingObjects.Zones.ZoneRights with the properties wich were stored in the database.
        """
        pass

    @staticmethod
    def FromZoneRightViews(zoneRightViews):
        """
        FromZoneRightViews(zoneRightViews: ZoneRightViews) -> ZoneRights
        
            zoneRightViews: A Wms.RemotingObjects.Zones.ZoneRightViews with the properties of the Wms.RemotingObjects.Zones.ZoneRights object and its
                    values.
            Returns: A new Wms.RemotingObjects.Zones.ZoneRights with the properties wich were stored in the database.
        """
        pass

    def ToString(self):
        """
        ToString(self: ZoneRights) -> str
        
            Creates a System.String with all rights and their values. Format for each 
                    right : '[Name]|[Value],'
            Returns: A System.String with all rights and their values.
        """
        pass

    def ToZoneRightViews(self):
        """
        ToZoneRightViews(self: ZoneRights) -> ZoneRightViews
        
            Creates a Wms.RemotingObjects.Zones.ZoneRightViews with all rights and their values.
            Returns: A Wms.RemotingObjects.Zones.ZoneRightViews with all rights and their values.
        """
        pass

    def UpdateZoneRights(self, zoneRightViews):
        """
        UpdateZoneRights(self: ZoneRights, zoneRightViews: ZoneRightViews)
            Updates the settings of the current Wms.RemotingObjects.Zones.ZoneRights.
        
            zoneRightViews: The updated rights.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Set: All(self: ZoneRights) = value
"""

    AllowAddReferenceOnTransfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowAddReferenceOnTransfer(self: ZoneRights) -> RightValue

Set: AllowAddReferenceOnTransfer(self: ZoneRights) = value
"""

    AllowBatchPackMultiSelectBatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowBatchPackMultiSelectBatches(self: ZoneRights) -> RightValue

Set: AllowBatchPackMultiSelectBatches(self: ZoneRights) = value
"""

    AllowConsolidatePacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowConsolidatePacks(self: ZoneRights) -> RightValue

Set: AllowConsolidatePacks(self: ZoneRights) = value
"""

    AllowManualPicking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowManualPicking(self: ZoneRights) -> RightValue

Set: AllowManualPicking(self: ZoneRights) = value
"""

    AllowOutboundProcessPartialPacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowOutboundProcessPartialPacked(self: ZoneRights) -> RightValue

Set: AllowOutboundProcessPartialPacked(self: ZoneRights) = value
"""

    AllowToDeliverMoreThanOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowToDeliverMoreThanOrdered(self: ZoneRights) -> RightValue

Set: AllowToDeliverMoreThanOrdered(self: ZoneRights) = value
"""

    AllowUsersToChangeFromRoute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: AllowUsersToChangeFromRoute(self: ZoneRights) -> RightValue

Set: AllowUsersToChangeFromRoute(self: ZoneRights) = value
"""

    ClientAllowUpdateBarcodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ClientAllowUpdateBarcodes(self: ZoneRights) -> RightValue

Set: ClientAllowUpdateBarcodes(self: ZoneRights) = value
"""

    ClientAllowUpdateOfDefaultItemLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientAllowUpdateOfDefaultItemLocation(self: ZoneRights) -> RightValue

Set: ClientAllowUpdateOfDefaultItemLocation(self: ZoneRights) = value
"""

    ConfirmPickDifferentItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ConfirmPickDifferentItemId(self: ZoneRights) -> RightValue

Set: ConfirmPickDifferentItemId(self: ZoneRights) = value
"""

    EnablePickPerItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EnablePickPerItemId(self: ZoneRights) -> RightValue

Set: EnablePickPerItemId(self: ZoneRights) = value
"""

    EnableRegistrationOfColliReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: EnableRegistrationOfColliReferences(self: ZoneRights) -> RightValue

Set: EnableRegistrationOfColliReferences(self: ZoneRights) = value
"""

    ManageUsersInZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ManageUsersInZone(self: ZoneRights) -> RightValue

Set: ManageUsersInZone(self: ZoneRights) = value
"""

    ManageZoneRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ManageZoneRights(self: ZoneRights) -> RightValue

Set: ManageZoneRights(self: ZoneRights) = value
"""

    MandatoryRegistrationOfInnerColliReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MandatoryRegistrationOfInnerColliReferences(self: ZoneRights) -> RightValue

Set: MandatoryRegistrationOfInnerColliReferences(self: ZoneRights) = value
"""

    MandatoryRegistrationOfOuterColliReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MandatoryRegistrationOfOuterColliReferences(self: ZoneRights) -> RightValue

Set: MandatoryRegistrationOfOuterColliReferences(self: ZoneRights) = value
"""

    MobileAllowInbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInbound(self: ZoneRights) -> RightValue

Set: MobileAllowInbound(self: ZoneRights) = value
"""

    MobileAllowInboundAdhocReceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundAdhocReceipts(self: ZoneRights) -> RightValue

Set: MobileAllowInboundAdhocReceipts(self: ZoneRights) = value
"""

    MobileAllowInboundAdhocRmaReceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundAdhocRmaReceipts(self: ZoneRights) -> RightValue

Set: MobileAllowInboundAdhocRmaReceipts(self: ZoneRights) = value
"""

    MobileAllowInboundPurchaseOrderPerOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundPurchaseOrderPerOrder(self: ZoneRights) -> RightValue

Set: MobileAllowInboundPurchaseOrderPerOrder(self: ZoneRights) = value
"""

    MobileAllowInboundPurchaseOrderPerSupplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundPurchaseOrderPerSupplier(self: ZoneRights) -> RightValue

Set: MobileAllowInboundPurchaseOrderPerSupplier(self: ZoneRights) = value
"""

    MobileAllowInboundReceiptsToLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundReceiptsToLocation(self: ZoneRights) -> RightValue

Set: MobileAllowInboundReceiptsToLocation(self: ZoneRights) = value
"""

    MobileAllowInboundRmaOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowInboundRmaOrders(self: ZoneRights) -> RightValue

Set: MobileAllowInboundRmaOrders(self: ZoneRights) = value
"""

    MobileAllowItemInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowItemInfo(self: ZoneRights) -> RightValue

Set: MobileAllowItemInfo(self: ZoneRights) = value
"""

    MobileAllowOutbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutbound(self: ZoneRights) -> RightValue

Set: MobileAllowOutbound(self: ZoneRights) = value
"""

    MobileAllowOutboundAdHocPerCustomer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundAdHocPerCustomer(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundAdHocPerCustomer(self: ZoneRights) = value
"""

    MobileAllowOutboundAdHocPerOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundAdHocPerOrder(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundAdHocPerOrder(self: ZoneRights) = value
"""

    MobileAllowOutboundBatchPicking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundBatchPicking(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundBatchPicking(self: ZoneRights) = value
"""

    MobileAllowOutboundDirectOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundDirectOrder(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundDirectOrder(self: ZoneRights) = value
"""

    MobileAllowOutboundHistoricalShipments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundHistoricalShipments(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundHistoricalShipments(self: ZoneRights) = value
"""

    MobileAllowOutboundProcessPartialPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundProcessPartialPicked(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundProcessPartialPicked(self: ZoneRights) = value
"""

    MobileAllowOutboundShipping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowOutboundShipping(self: ZoneRights) -> RightValue

Set: MobileAllowOutboundShipping(self: ZoneRights) = value
"""

    MobileAllowStockCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockCounts(self: ZoneRights) -> RightValue

Set: MobileAllowStockCounts(self: ZoneRights) = value
"""

    MobileAllowStockCountsAdHocCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockCountsAdHocCounts(self: ZoneRights) -> RightValue

Set: MobileAllowStockCountsAdHocCounts(self: ZoneRights) = value
"""

    MobileAllowStockCountsAdHocZeroCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockCountsAdHocZeroCounts(self: ZoneRights) -> RightValue

Set: MobileAllowStockCountsAdHocZeroCounts(self: ZoneRights) = value
"""

    MobileAllowStockCountsTrajectCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockCountsTrajectCounts(self: ZoneRights) -> RightValue

Set: MobileAllowStockCountsTrajectCounts(self: ZoneRights) = value
"""

    MobileAllowStockManagement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagement(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagement(self: ZoneRights) = value
"""

    MobileAllowStockManagementDirectTransfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagementDirectTransfer(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagementDirectTransfer(self: ZoneRights) = value
"""

    MobileAllowStockManagementFromLocationItemLoc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagementFromLocationItemLoc(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagementFromLocationItemLoc(self: ZoneRights) = value
"""

    MobileAllowStockManagementFromLocationLocItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagementFromLocationLocItem(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagementFromLocationLocItem(self: ZoneRights) = value
"""

    MobileAllowStockManagementPutToLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagementPutToLocation(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagementPutToLocation(self: ZoneRights) = value
"""

    MobileAllowStockManagementWarehouseTransfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowStockManagementWarehouseTransfer(self: ZoneRights) -> RightValue

Set: MobileAllowStockManagementWarehouseTransfer(self: ZoneRights) = value
"""

    MobileAllowSystemInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: MobileAllowSystemInfo(self: ZoneRights) -> RightValue

Set: MobileAllowSystemInfo(self: ZoneRights) = value
"""

    PortalAllowBatchApproval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowBatchApproval(self: ZoneRights) -> RightValue

Set: PortalAllowBatchApproval(self: ZoneRights) = value
"""

    PortalAllowBatchCreation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowBatchCreation(self: ZoneRights) -> RightValue

Set: PortalAllowBatchCreation(self: ZoneRights) = value
"""

    PortalAllowBatchDeletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowBatchDeletion(self: ZoneRights) -> RightValue

Set: PortalAllowBatchDeletion(self: ZoneRights) = value
"""

    PortalAllowBatchEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowBatchEdit(self: ZoneRights) -> RightValue

Set: PortalAllowBatchEdit(self: ZoneRights) = value
"""

    PortalAllowBatchWithOptionsCreation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowBatchWithOptionsCreation(self: ZoneRights) -> RightValue

Set: PortalAllowBatchWithOptionsCreation(self: ZoneRights) = value
"""

    PortalAllowDashboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowDashboard(self: ZoneRights) -> RightValue

Set: PortalAllowDashboard(self: ZoneRights) = value
"""

    PortalAllowExtensibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowExtensibility(self: ZoneRights) -> RightValue

Set: PortalAllowExtensibility(self: ZoneRights) = value
"""

    PortalAllowExtensibilityScriptConsole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowExtensibilityScriptConsole(self: ZoneRights) -> RightValue

Set: PortalAllowExtensibilityScriptConsole(self: ZoneRights) = value
"""

    PortalAllowExtensibilityScriptModules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowExtensibilityScriptModules(self: ZoneRights) -> RightValue

Set: PortalAllowExtensibilityScriptModules(self: ZoneRights) = value
"""

    PortalAllowExtensibilityScriptTasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowExtensibilityScriptTasks(self: ZoneRights) -> RightValue

Set: PortalAllowExtensibilityScriptTasks(self: ZoneRights) = value
"""

    PortalAllowExtensibilityZoneScripts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowExtensibilityZoneScripts(self: ZoneRights) -> RightValue

Set: PortalAllowExtensibilityZoneScripts(self: ZoneRights) = value
"""

    PortalAllowHistorical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowHistorical(self: ZoneRights) -> RightValue

Set: PortalAllowHistorical(self: ZoneRights) = value
"""

    PortalAllowHistoricalDirectOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowHistoricalDirectOrders(self: ZoneRights) -> RightValue

Set: PortalAllowHistoricalDirectOrders(self: ZoneRights) = value
"""

    PortalAllowHistoricalPurchaseOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowHistoricalPurchaseOrders(self: ZoneRights) -> RightValue

Set: PortalAllowHistoricalPurchaseOrders(self: ZoneRights) = value
"""

    PortalAllowHistoricalShipments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowHistoricalShipments(self: ZoneRights) -> RightValue

Set: PortalAllowHistoricalShipments(self: ZoneRights) = value
"""

    PortalAllowImportLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowImportLicense(self: ZoneRights) -> RightValue

Set: PortalAllowImportLicense(self: ZoneRights) = value
"""

    PortalAllowInbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see inbound menu block in portal

Get: PortalAllowInbound(self: ZoneRights) -> RightValue

Set: PortalAllowInbound(self: ZoneRights) = value
"""

    PortalAllowInboundPrereceipts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see inbound purchase orders menu in portal

Get: PortalAllowInboundPrereceipts(self: ZoneRights) -> RightValue

Set: PortalAllowInboundPrereceipts(self: ZoneRights) = value
"""

    PortalAllowInboundPurchaseOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see inbound purchase orders menu in portal

Get: PortalAllowInboundPurchaseOrder(self: ZoneRights) -> RightValue

Set: PortalAllowInboundPurchaseOrder(self: ZoneRights) = value
"""

    PortalAllowLicensePlateCreateEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowLicensePlateCreateEdit(self: ZoneRights) -> RightValue

Set: PortalAllowLicensePlateCreateEdit(self: ZoneRights) = value
"""

    PortalAllowLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowLicensePlates(self: ZoneRights) -> RightValue

Set: PortalAllowLicensePlates(self: ZoneRights) = value
"""

    PortalAllowLicensePlateStatusChange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowLicensePlateStatusChange(self: ZoneRights) -> RightValue

Set: PortalAllowLicensePlateStatusChange(self: ZoneRights) = value
"""

    PortalAllowLogin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowLogin(self: ZoneRights) -> RightValue

Set: PortalAllowLogin(self: ZoneRights) = value
"""

    PortalAllowMasterData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterData(self: ZoneRights) -> RightValue

Set: PortalAllowMasterData(self: ZoneRights) = value
"""

    PortalAllowMasterDataBarcodeStructures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataBarcodeStructures(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataBarcodeStructures(self: ZoneRights) = value
"""

    PortalAllowMasterDataColliPresets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataColliPresets(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataColliPresets(self: ZoneRights) = value
"""

    PortalAllowMasterDataGenerateBarcodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataGenerateBarcodes(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataGenerateBarcodes(self: ZoneRights) = value
"""

    PortalAllowMasterDataLabels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataLabels(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataLabels(self: ZoneRights) = value
"""

    PortalAllowMasterDataNumberRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataNumberRanges(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataNumberRanges(self: ZoneRights) = value
"""

    PortalAllowMasterDataShippersBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataShippersBinding(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataShippersBinding(self: ZoneRights) = value
"""

    PortalAllowMasterDataStorageAssignmentClassification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataStorageAssignmentClassification(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataStorageAssignmentClassification(self: ZoneRights) = value
"""

    PortalAllowMasterDataTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataTags(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataTags(self: ZoneRights) = value
"""

    PortalAllowMasterDataUsers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataUsers(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataUsers(self: ZoneRights) = value
"""

    PortalAllowMasterDataWarehouseLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataWarehouseLayout(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataWarehouseLayout(self: ZoneRights) = value
"""

    PortalAllowMasterDataZones = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMasterDataZones(self: ZoneRights) -> RightValue

Set: PortalAllowMasterDataZones(self: ZoneRights) = value
"""

    PortalAllowMessaging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowMessaging(self: ZoneRights) -> RightValue

Set: PortalAllowMessaging(self: ZoneRights) = value
"""

    PortalAllowMessagingRemotePublishing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see remote publishers menu in portal

Get: PortalAllowMessagingRemotePublishing(self: ZoneRights) -> RightValue

Set: PortalAllowMessagingRemotePublishing(self: ZoneRights) = value
"""

    PortalAllowOrderValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOrderValidation(self: ZoneRights) -> RightValue

Set: PortalAllowOrderValidation(self: ZoneRights) = value
"""

    PortalAllowOutbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOutbound(self: ZoneRights) -> RightValue

Set: PortalAllowOutbound(self: ZoneRights) = value
"""

    PortalAllowOutboundOrdersBatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOutboundOrdersBatches(self: ZoneRights) -> RightValue

Set: PortalAllowOutboundOrdersBatches(self: ZoneRights) = value
"""

    PortalAllowOutboundOrdersDeliverable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOutboundOrdersDeliverable(self: ZoneRights) -> RightValue

Set: PortalAllowOutboundOrdersDeliverable(self: ZoneRights) = value
"""

    PortalAllowOutboundOrdersNonDeliverable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOutboundOrdersNonDeliverable(self: ZoneRights) -> RightValue

Set: PortalAllowOutboundOrdersNonDeliverable(self: ZoneRights) = value
"""

    PortalAllowOutboundReplenishmentOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowOutboundReplenishmentOrders(self: ZoneRights) -> RightValue

Set: PortalAllowOutboundReplenishmentOrders(self: ZoneRights) = value
"""

    PortalAllowPreReceiptAlterStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowPreReceiptAlterStatus(self: ZoneRights) -> RightValue

Set: PortalAllowPreReceiptAlterStatus(self: ZoneRights) = value
"""

    PortalAllowPreReceiptCreation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowPreReceiptCreation(self: ZoneRights) -> RightValue

Set: PortalAllowPreReceiptCreation(self: ZoneRights) = value
"""

    PortalAllowPrintagentDeletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PortalAllowPrintagentDeletion(self: ZoneRights) -> RightValue

Set: PortalAllowPrintagentDeletion(self: ZoneRights) = value
"""

    PortalAllowPrintJobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see the Print Management > Print Jobs menu item

Get: PortalAllowPrintJobs(self: ZoneRights) -> RightValue

Set: PortalAllowPrintJobs(self: ZoneRights) = value
"""

    PortalAllowPrintManagement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see the Print Management menu item

Get: PortalAllowPrintManagement(self: ZoneRights) -> RightValue

Set: PortalAllowPrintManagement(self: ZoneRights) = value
"""

    PortalAllowPrintRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Allow user to see the Print Management > Print Rules menu item

Get: PortalAllowPrintRules(self: ZoneRights) -> RightValue

Set: PortalAllowPrintRules(self: ZoneRights) = value
"""

    PortalAllowPublishersHandlers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowPublishersHandlers(self: ZoneRights) -> RightValue

Set: PortalAllowPublishersHandlers(self: ZoneRights) = value
"""

    PortalAllowQueueMonitor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowQueueMonitor(self: ZoneRights) -> RightValue

Set: PortalAllowQueueMonitor(self: ZoneRights) = value
"""

    PortalAllowResetNumberRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowResetNumberRange(self: ZoneRights) -> RightValue

Set: PortalAllowResetNumberRange(self: ZoneRights) = value
"""

    PortalAllowSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSettings(self: ZoneRights) -> RightValue

Set: PortalAllowSettings(self: ZoneRights) = value
"""

    PortalAllowSettingsBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSettingsBarcode(self: ZoneRights) -> RightValue

Set: PortalAllowSettingsBarcode(self: ZoneRights) = value
"""

    PortalAllowSettingsErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSettingsErp(self: ZoneRights) -> RightValue

Set: PortalAllowSettingsErp(self: ZoneRights) = value
"""

    PortalAllowSettingsGeneral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSettingsGeneral(self: ZoneRights) -> RightValue

Set: PortalAllowSettingsGeneral(self: ZoneRights) = value
"""

    PortalAllowSettingsShipper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSettingsShipper(self: ZoneRights) -> RightValue

Set: PortalAllowSettingsShipper(self: ZoneRights) = value
"""

    PortalAllowStockCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockCounts(self: ZoneRights) -> RightValue

Set: PortalAllowStockCounts(self: ZoneRights) = value
"""

    PortalAllowStockCountsAllCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockCountsAllCounts(self: ZoneRights) -> RightValue

Set: PortalAllowStockCountsAllCounts(self: ZoneRights) = value
"""

    PortalAllowStockCountsCountGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockCountsCountGroups(self: ZoneRights) -> RightValue

Set: PortalAllowStockCountsCountGroups(self: ZoneRights) = value
"""

    PortalAllowStockInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockInformation(self: ZoneRights) -> RightValue

Set: PortalAllowStockInformation(self: ZoneRights) = value
"""

    PortalAllowStockInformationLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockInformationLocations(self: ZoneRights) -> RightValue

Set: PortalAllowStockInformationLocations(self: ZoneRights) = value
"""

    PortalAllowStockInformationStockList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockInformationStockList(self: ZoneRights) -> RightValue

Set: PortalAllowStockInformationStockList(self: ZoneRights) = value
"""

    PortalAllowStockInformationWarehouses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowStockInformationWarehouses(self: ZoneRights) -> RightValue

Set: PortalAllowStockInformationWarehouses(self: ZoneRights) = value
"""

    PortalAllowSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystem(self: ZoneRights) -> RightValue

Set: PortalAllowSystem(self: ZoneRights) = value
"""

    PortalAllowSystemCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemCache(self: ZoneRights) -> RightValue

Set: PortalAllowSystemCache(self: ZoneRights) = value
"""

    PortalAllowSystemDbLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemDbLog(self: ZoneRights) -> RightValue

Set: PortalAllowSystemDbLog(self: ZoneRights) = value
"""

    PortalAllowSystemErpLocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemErpLocks(self: ZoneRights) -> RightValue

Set: PortalAllowSystemErpLocks(self: ZoneRights) = value
"""

    PortalAllowSystemOfflineScanning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemOfflineScanning(self: ZoneRights) -> RightValue

Set: PortalAllowSystemOfflineScanning(self: ZoneRights) = value
"""

    PortalAllowSystemProcessMonitor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemProcessMonitor(self: ZoneRights) -> RightValue

Set: PortalAllowSystemProcessMonitor(self: ZoneRights) = value
"""

    PortalAllowSystemProfilingLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PortalAllowSystemProfilingLog(self: ZoneRights) -> RightValue

Set: PortalAllowSystemProfilingLog(self: ZoneRights) = value
"""

    PortalAllowViewPrintAgent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PortalAllowViewPrintAgent(self: ZoneRights) -> RightValue

Set: PortalAllowViewPrintAgent(self: ZoneRights) = value
"""

    PrefillInventoryQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrefillInventoryQuantity(self: ZoneRights) -> RightValue

Set: PrefillInventoryQuantity(self: ZoneRights) = value
"""

    PrefillPackQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrefillPackQuantity(self: ZoneRights) -> RightValue

Set: PrefillPackQuantity(self: ZoneRights) = value
"""

    PrefillPickQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrefillPickQuantity(self: ZoneRights) -> RightValue

Set: PrefillPickQuantity(self: ZoneRights) = value
"""

    PrefillReceiveQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrefillReceiveQuantity(self: ZoneRights) -> RightValue

Set: PrefillReceiveQuantity(self: ZoneRights) = value
"""

    PrefillRmaReceiveQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PrefillRmaReceiveQuantity(self: ZoneRights) -> RightValue

Set: PrefillRmaReceiveQuantity(self: ZoneRights) = value
"""

    ProcessCountsToErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ProcessCountsToErp(self: ZoneRights) -> RightValue

Set: ProcessCountsToErp(self: ZoneRights) = value
"""

    ShowItemCodeSupplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ShowItemCodeSupplier(self: ZoneRights) -> RightValue

Set: ShowItemCodeSupplier(self: ZoneRights) = value
"""

    SkipExpeditionWhenProcessing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SkipExpeditionWhenProcessing(self: ZoneRights) -> RightValue

Set: SkipExpeditionWhenProcessing(self: ZoneRights) = value
"""

    SkipLocationScan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SkipLocationScan(self: ZoneRights) -> RightValue

Set: SkipLocationScan(self: ZoneRights) = value
"""

    StartWithDefaultCollo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: StartWithDefaultCollo(self: ZoneRights) -> RightValue

Set: StartWithDefaultCollo(self: ZoneRights) = value
"""

    TouchAllowBatchDeletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowBatchDeletion(self: ZoneRights) -> RightValue

Set: TouchAllowBatchDeletion(self: ZoneRights) = value
"""

    TouchAllowHistoricShipments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowHistoricShipments(self: ZoneRights) -> RightValue

Set: TouchAllowHistoricShipments(self: ZoneRights) = value
"""

    TouchAllowInbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowInbound(self: ZoneRights) -> RightValue

Set: TouchAllowInbound(self: ZoneRights) = value
"""

    TouchAllowInboundRmaOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowInboundRmaOrders(self: ZoneRights) -> RightValue

Set: TouchAllowInboundRmaOrders(self: ZoneRights) = value
"""

    TouchAllowItemInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowItemInfo(self: ZoneRights) -> RightValue

Set: TouchAllowItemInfo(self: ZoneRights) = value
"""

    TouchAllowOutbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowOutbound(self: ZoneRights) -> RightValue

Set: TouchAllowOutbound(self: ZoneRights) = value
"""

    TouchAllowOutboundPick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowOutboundPick(self: ZoneRights) -> RightValue

Set: TouchAllowOutboundPick(self: ZoneRights) = value
"""

    TouchAllowPackingWithOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowPackingWithOrders(self: ZoneRights) -> RightValue

Set: TouchAllowPackingWithOrders(self: ZoneRights) = value
"""

    TouchAllowPreReceiptDeletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowPreReceiptDeletion(self: ZoneRights) -> RightValue

Set: TouchAllowPreReceiptDeletion(self: ZoneRights) = value
"""

    TouchAllowPreReceivePurchaseOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowPreReceivePurchaseOrders(self: ZoneRights) -> RightValue

Set: TouchAllowPreReceivePurchaseOrders(self: ZoneRights) = value
"""

    TouchAllowReceiveOnLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowReceiveOnLicensePlates(self: ZoneRights) -> RightValue

Set: TouchAllowReceiveOnLicensePlates(self: ZoneRights) = value
"""

    TouchAllowSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowSettings(self: ZoneRights) -> RightValue

Set: TouchAllowSettings(self: ZoneRights) = value
"""

    TouchAllowTransfer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAllowTransfer(self: ZoneRights) -> RightValue

Set: TouchAllowTransfer(self: ZoneRights) = value
"""

    TouchAutoHideWarnings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchAutoHideWarnings(self: ZoneRights) -> RightValue

Set: TouchAutoHideWarnings(self: ZoneRights) = value
"""

    TouchDisplayFullyPackedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchDisplayFullyPackedItems(self: ZoneRights) -> RightValue

Set: TouchDisplayFullyPackedItems(self: ZoneRights) = value
"""

    TouchMandatoryUseOfLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: TouchMandatoryUseOfLicensePlates(self: ZoneRights) -> RightValue

Set: TouchMandatoryUseOfLicensePlates(self: ZoneRights) = value
"""


    RightValue = None


class ZoneRightView():
    """
    ZoneRightView()
    ZoneRightView(propertyName: str, name: str, value: RightValue, groupSortKey: str, groupName: str)
    """
    Instance = ZoneRightView
    """hardcoded/returns an instance of the class"""
    @staticmethod # known case of __new__
    def __new__(self, propertyName=None, name=None, value=None, groupSortKey=None, groupName=None):
        """
        __new__(cls: type)
        __new__(cls: type, propertyName: str, name: str, value: RightValue, groupSortKey: str, groupName: str)
        """
        pass

    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupName(self: ZoneRightView) -> str

Set: GroupName(self: ZoneRightView) = value
"""

    GroupSortKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: GroupSortKey(self: ZoneRightView) -> str

Set: GroupSortKey(self: ZoneRightView) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: ZoneRightView) -> str

Set: Name(self: ZoneRightView) = value
"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: PropertyName(self: ZoneRightView) -> str

Set: PropertyName(self: ZoneRightView) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Value(self: ZoneRightView) -> RightValue

Set: Value(self: ZoneRightView) = value
"""



class ZoneRightViews(FindableList):
    """ ZoneRightViews() """
    Instance = ZoneRightViews
    """hardcoded/returns an instance of the class"""
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Name'
    ValueMember = 'Value'


class Zones(FindableList):
    """ Zones() """
    Instance = Zones
    """hardcoded/returns an instance of the class"""
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Name'
    ValueMember = 'Id'


class ZoneUser(User):
    """
    ZoneUser(basedOn: User, isInZone: bool)
    ZoneUser()
    """
    Instance = ZoneUser
    """hardcoded/returns an instance of the class"""
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, basedOn=None, isInZone=None):
        """
        __new__(cls: type, basedOn: User, isInZone: bool)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsInZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsInZone(self: ZoneUser) -> bool

Set: IsInZone(self: ZoneUser) = value
"""



class ZoneUsers(List):
    """
    ZoneUsers(collection: IEnumerable[ZoneUser])
    ZoneUsers()
    """
    Instance = ZoneUsers
    """hardcoded/returns an instance of the class"""
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, collection=None):
        """
        __new__(cls: type, collection: IEnumerable[ZoneUser])
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'FullName'
    ValueMember = 'UserId'


# variables with complex values

