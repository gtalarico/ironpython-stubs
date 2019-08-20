import json

data = {}
data["1.20"] = {}
data["1.20"]["Attribute"] = {}
data["1.21"]["Attribute"]["outbound.PickInBatch"] = " 1.20: The loose arguments are combined into 1 object and put in a dataflowobjects: DataFlow<pickArgs>"
data["1.21"]["Attribute"]["getitemcodefrombarcode"] = " Deleted in 1.23, use general.getiteminfofrombarcode instead"
data["1.21"]["Attribute"]["GetDocumentPrinterOfCurrentUser"] = "Updated in 1.21: Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["GetLabelPrinterOfCurrentUser"] = "Updated in 1.21: Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["GetPrintersOfUser"] = "Updated in 1.21: Use DocumentQueue.AddPrintJob or Printing (IOC).py"
data["1.21"]["Attribute"]["CreateDevicePrinterSetting"] = "Updated in 1.21: Use DocumentQueue.AddPrintJob or Printing (IOC).py"


if __name__ == "__main__":
    with open('changelist.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)
        print 'Changelist made :)'