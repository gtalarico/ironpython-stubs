import json

data = {}
data["1.20"] = {}
data["1.20"]["Attribute"] = {}
data["1.20"]["Attribute"]["General.GetItemcodeFromBarcode"] = " Deleted in 1.20, Use General.GetItemInfoFromBarcode instead"
data["1.20"]["Attribute"]["PackageBase.OurReference"] = "Use PackageBase.OrderReferences.OrderNumbers instead"
data["1.20"]["Attribute"]["PackageBase.CustomerReference"] = "Use PackageBase.OrderReferences.CustomerReferences instead"

data["1.21"] = {}
data["1.21"]["Attribute"] = {}
data["1.21"]["Attribute"]["General.GetDocumentPrinterOfCurrentUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["General.GetLabelPrinterOfCurrentUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["General.GetPrintersOfUser"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["General.CreateDevicePrinterSetting"] = "Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["GetOutboundOrderLinesBatchable]"] = "Is verwijderd wmspro-4431 (mocht dit in GetSalesOrdersByFilter gebruikt worden, dan kan Jolley als voorbeeld vormen voor herschrijven.)"
data["1.21"]["Attribute"]["ProcessShipmentArgs.DocumentPrinter"] =  "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["1.21"]["Attribute"]["ProcessShipmentArgs.LabelPrinter"] = "  Properties zijn verwijderd (in principe alles via printregels configureren)"
data["1.21"]["Attribute"]["ProcessShipmentArgs.NrOfCustomPackageslips"] = "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["1.21"]["Attribute"]["PrintBaseArgs.NumberOfCopies"] = "Properties zijn verwijderd (in principe alles via printregels configureren)"
data["1.21"]["Attribute"]["PrintPickingListArgs.NrOfCopies"] = "Veranderd naar PrintingOptions.Copies"

data["1.22"] = {}
data["1.22"]["Attribute"] = {}
data["1.23"] = {}
data["1.23"]["Attribute"] = {}
if __name__ == "__main__":
    with open('changelist.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)
        print 'Changelist made :)'