import json

data = {}
data["Deleted"] = {}
data["Deleted"]["1.20"] = {}
data["Deleted"]["1.20"]["General.GetItemcodeFromBarcode"] = " Deleted in 1.20, Use General.GetItemInfoFromBarcode instead"
data["Deleted"]["1.20"]["PackageBase.OurReference"] = "Use PackageBase.OrderReferences.OrderNumbers instead"
data["Deleted"]["1.20"]["PackageBase.CustomerReference"] = "Use PackageBase.OrderReferences.CustomerReferences instead"

data["Deleted"]["1.21"] = {}
data["Deleted"]["1.21"]["General.GetDocumentPrinterOfCurrentUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["Deleted"]["1.21"]["General.GetLabelPrinterOfCurrentUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["Deleted"]["1.21"]["General.GetPrintersOfUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["Deleted"]["1.21"]["General.CreateDevicePrinterSetting"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["Deleted"]["1.21"]["Outbound.GetOutboundOrderLinesBatchable"] = "Is verwijderd wmspro-4431 (mocht dit in GetSalesOrdersByFilter gebruikt worden, dan kan Jolley als voorbeeld vormen voor herschrijven.)"
data["Deleted"]["1.21"]["ProcessShipmentArgs.DocumentPrinter"] =  "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["Deleted"]["1.21"]["ProcessShipmentArgs.LabelPrinter"] = "  Properties zijn verwijderd (in principe alles via printregels configureren)"
data["Deleted"]["1.21"]["ProcessShipmentArgs.NrOfCustomPackageslips"] = "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["Deleted"]["1.21"]["PrintBaseArgs.NumberOfCopies"] = "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["Deleted"]["1.21"]["PrintPickingListArgs.NrOfCopies"] = "Veranderd naar PrintingOptions.Copies"

data["Deleted"]["1.23"] = {}
data["Deleted"]["1.23"]["Outbound.MovePackageItems"] = "Samengevoegd met andere functies tot 'DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> MoveTransportItemsBetweenTransportPackages(DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> dfObject)'"
data["Deleted"]["1.23"]["Outbound.AddTransportItemToTransportPackage"] = "Samengevoegd met andere functies tot 'DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> MoveTransportItemsBetweenTransportPackages(DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> dfObject)'"
data["Deleted"]["1.23"]["Outbound.RemoveTransportItemFromTransportPackage"] = "Samengevoegd met andere functies tot 'DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> MoveTransportItemsBetweenTransportPackages(DataFlowObject<MoveTransportItemsBetweenTransportPackagesArgs> dfObject)'"




data["Refactors"] = {}
data["Refactors"]["1.20"] = {}
data["Refactors"]["1.20"]["Outbound.PickInBatch"] = "De losse argumenten zijn samengevoegd in 1 object en in een DataFlowObject gestopt: DataFlow<PickArgs>"
data["Refactors"]["1.20"]["Outbound.ProcessBatchPickingToErp"] = "Er is een extra argument toegevoegd: DataFlowObject<ProcessBatchPickingArgs>"
#data["Refactors"]["1.20"]["PackageBase.*"] = "Per collo worden de pakbonnummers bijgehouden (i.t.t. pakbonnummers per zending) "


data["Refactors"]["1.21"] = {}
data["Refactors"]["1.21"]["Inbound.GetVendorsExpectedByFilter"]="Maatwerk in GetVendorsExpectedByFilter dat leveranciers sorteert o.b.v. alfabetische volgorde verwijderen i.v.m. wmspro-3649"

data["Refactors"]["1.22"] = {}


data["Refactors"]["1.23"] = {}
data["Refactors"]["1.23"]["Inbound.GetItemVendors"] = "De hook verwacht nu een returntype 'ItemVendors' in plaats van een int. De out-parameter is derhalve verwijderd."
data["Refactors"]["1.23"]["Inventory.ProcessWarehouseTransfer"] = "Overloads verwijdert: verandert naar DataFlowObject<ProcessWarehouseTransferArgs> ProcessWarehouseTransfer(DataFlowObject<ProcessWarehouseTransferArgs>)"




if __name__ == "__main__":
    with open('changelist.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)
        print 'Changelist made :)'