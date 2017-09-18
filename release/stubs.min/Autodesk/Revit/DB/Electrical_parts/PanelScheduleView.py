class PanelScheduleView(TableView,IDisposable):
 """ An instance of a panel schedule view. """
 def CanMoveSlotTo(self,nMovingRow,nMovingCol,nToRow,nToCol):
  """
  CanMoveSlotTo(self: PanelScheduleView,nMovingRow: int,nMovingCol: int,nToRow: int,nToCol: int) -> bool

  

   Verifies if can circuits in the source slot to the specific slot.

  

   nMovingRow: The Row Number of cell to be moved.

   nMovingCol: Start Column Number of cell to be moved.

   nToRow: The Row Number of cell to moved to.

   nToCol: End Column Number of cell to moved to.

   Returns: True if can move circuits in the source slot to the specific slot.
  """
  pass
 @staticmethod
 def CreateInstanceView(ADoc,*__args):
  """
  CreateInstanceView(ADoc: Document,panelId: ElementId) -> PanelScheduleView

  

   Creates a new instance of this view (using default template)

  

   ADoc: The Document

   panelId: Element id of the electrical panel element.

   Returns: The PanelScheduleView

  CreateInstanceView(ADoc: Document,templateId: ElementId,panelId: ElementId) -> PanelScheduleView

  

   Creates a new instance of this view (using specific template)

  

   ADoc: The Document

   templateId: The templateId that this function will use

   panelId: Element id of the electrical panel element.

   Returns: The PanelScheduleView
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GenerateInstanceFromTemplate(self,templateId):
  """
  GenerateInstanceFromTemplate(self: PanelScheduleView,templateId: ElementId)

   Assigns the data from the template to the instance and performs any tasks 

    specific to the instance (3rd phase,borders,etc)

  

  

   templateId: Element id of the template element.
  """
  pass
 def GetApparentPhaseValue(self,circuitId,apparentLoadParam):
  """
  GetApparentPhaseValue(self: PanelScheduleView,circuitId: ElementId,apparentLoadParam: ElementId) -> float

  

   Gets the apparent load for the given phase for the given slotted circuit

  

   circuitId: Circuit id for the apparent phase value

   apparentLoadParam: The requested apparent load phase parameter

   Returns: The value of the apparent phase
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetCellsBySlotNumber(self,nSlotNumber,RowArr,ColArr):
  """ GetCellsBySlotNumber(self: PanelScheduleView,nSlotNumber: int) -> (IList[int],IList[int]) """
  pass
 def GetCircuitByCell(self,nRow,nCol):
  """
  GetCircuitByCell(self: PanelScheduleView,nRow: int,nCol: int) -> ElectricalSystem

  

   Gets the circuit element for the given slot number

  

   nRow: Row Number of the Body Section

   nCol: Column Number of the Body Section

   Returns: The circuit found at the given row and column
  """
  pass
 def GetCircuitIdByCell(self,nRow,nCol):
  """
  GetCircuitIdByCell(self: PanelScheduleView,nRow: int,nCol: int) -> ElementId

  

   Gets the circuit id for the given slot number

  

   nRow: Row Number

   nCol: Column Number

   Returns: ElementId of the circuit found at the given row and column
  """
  pass
 def GetCombinedParamValue(self,sectionType,nRow,nCol):
  """
  GetCombinedParamValue(self: PanelScheduleView,sectionType: SectionType,nRow: int,nCol: int) -> str

  

   Returns the combined parameter text for instance view

  

   sectionType: Section type

   nRow: Row Number

   nCol: Column Number

   Returns: The combined parameter text
  """
  pass
 def GetLoadClassificationConnectedCurrent(self,nRow,nCol):
  """
  GetLoadClassificationConnectedCurrent(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the Total Current for given Load Classification

  

   nRow: Row number of Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The Connected Current for the given Load Classification
  """
  pass
 def GetLoadClassificationConnectedLoad(self,nRow,nCol):
  """
  GetLoadClassificationConnectedLoad(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the Total Load for given Load Classification

  

   nRow: Row number of Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The total load for the given Load Classification
  """
  pass
 def GetLoadClassificationDemandCurrent(self,nRow,nCol):
  """
  GetLoadClassificationDemandCurrent(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the Demand Current for given Load Classification

  

   nRow: Row number of Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The Demand Current for the given Load Classification
  """
  pass
 def GetLoadClassificationDemandFactor(self,nRow,nCol):
  """
  GetLoadClassificationDemandFactor(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the Demand Factor for given Load Classification

  

   nRow: Row number of Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The Demand Factor for the given Load Classification
  """
  pass
 def GetLoadClassificationDemandLoad(self,nRow,nCol):
  """
  GetLoadClassificationDemandLoad(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the Demand Load for given Load Classification

  

   nRow: Row number of Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The Demand Load for the Load Classification
  """
  pass
 def GetLoadClassificationId(self,nRow):
  """
  GetLoadClassificationId(self: PanelScheduleView,nRow: int) -> ElementId

  

   Gets the id of the associated Load Classification at the given row

  

   nRow: Row number of Load Summary Section

   Returns: The element id of the Load Classification
  """
  pass
 def GetLoadClassificationName(self,nRow,nCol):
  """
  GetLoadClassificationName(self: PanelScheduleView,nRow: int,nCol: int) -> str

  

   Gets the name of the Load Classification at the given row/column

  

   nRow: Row Number of the Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The name of the Load Classification
  """
  pass
 def GetLoadClassificationParamValue(self,parameterId,nRow,nCol):
  """
  GetLoadClassificationParamValue(self: PanelScheduleView,parameterId: ElementId,nRow: int,nCol: int) -> str

  

   Gets the load classification parameter value.

  

   parameterId: Parameter Id of the Load Classification

   nRow: Row Number of the Load Summary Section

   nCol: Column number of Load Summary Section

   Returns: The value of the Load Classification parameter
  """
  pass
 def GetPanel(self):
  """
  GetPanel(self: PanelScheduleView) -> ElementId

  

   Gets the panel for this view

   Returns: The id of the panel for this view
  """
  pass
 def GetParamValue(self,sectionType,nRow,nCol):
  """
  GetParamValue(self: PanelScheduleView,sectionType: SectionType,nRow: int,nCol: int) -> str

  

   Gets the cell's text based on its type

  

   sectionType: Section of the desired parameter value

   nRow: Row Number of the Section

   nCol: Column Number of the Section

   Returns: The cell's text
  """
  pass
 def GetSectionData(self,sectionType):
  """
  GetSectionData(self: PanelScheduleView,sectionType: SectionType) -> TableSectionData

  

   Gets section data that will be written to

  

   sectionType: The section type

   Returns: The Autodesk.Revit.DB.TableSectionData
  """
  pass
 def GetSlotNumberByCell(self,nRow,nCol):
  """
  GetSlotNumberByCell(self: PanelScheduleView,nRow: int,nCol: int) -> int

  

   Gets the slot number in the circuit table

  

   nRow: Column Number

   Returns: Row Number
  """
  pass
 def GetSpareCurrentValue(self,row,column,idCurrentParameter):
  """
  GetSpareCurrentValue(self: PanelScheduleView,row: int,column: int,idCurrentParameter: ElementId) -> float

  

   Gets the value of the apparent current parameter for a spare

  

   row: A row where the valid spare is

   column: A column where the valid spare is

   idCurrentParameter: One of 4 valid current parameters: RBS_ELEC_APPARENT_CURRENT_PARAM,

    RBS_ELEC_APPARENT_CURRENT_PHASEA_PARAM,RBS_ELEC_APPARENT_CURRENT_PHASEB_PARAM,

    RBS_ELEC_APPARENT_CURRENT_PHASEC_PARAM

  

   Returns: The value of the spare's current parameter
  """
  pass
 def GetSpareLoadValue(self,row,column,idLoadParameter):
  """
  GetSpareLoadValue(self: PanelScheduleView,row: int,column: int,idLoadParameter: ElementId) -> float

  

   Gets the value of the apparent load parameter for a spare

  

   row: A row where the valid spare is

   column: A column where the valid spare is

   idLoadParameter: One of 4 valid load parameters: RBS_ELEC_APPARENT_LOAD,

    RBS_ELEC_APPARENT_LOAD_PHASEA,RBS_ELEC_APPARENT_LOAD_PHASEB,

    RBS_ELEC_APPARENT_LOAD_PHASEC

  

   Returns: The value of the spare's load parameter
  """
  pass
 def GetTableData(self):
  """
  GetTableData(self: PanelScheduleView) -> PanelScheduleData

  

   Gets table data that can be written to

   Returns: The Autodesk.Revit.DB.Electrical.PanelScheduleData
  """
  pass
 def GetTemplate(self):
  """
  GetTemplate(self: PanelScheduleView) -> ElementId

  

   Gets the template for this view (to set the template,you must go through 

    generateInstanceFromTemplate)

  

   Returns: The template id for this view
  """
  pass
 def IsCellInPhaseLoads(self,nRow,nCol):
  """
  IsCellInPhaseLoads(self: PanelScheduleView,nRow: int,nCol: int) -> bool

  

   Check if this cell in the phase loads

  

   nRow: Row Number

   nCol: Column Number

   Returns: True if this cell in the phase loads,false otherwise
  """
  pass
 def IsColumnInLoadSummary(self,nCol):
  """
  IsColumnInLoadSummary(self: PanelScheduleView,nCol: int) -> bool

  

   Check if this column in the load summary

  

   nCol: Column Number

   Returns: Check if this column in the load summary
  """
  pass
 def IsPanelScheduleTemplate(self):
  """
  IsPanelScheduleTemplate(self: PanelScheduleView) -> bool

  

   Check if this is a panel schedule template.

   Returns: Check if this is a panel schedule template.
  """
  pass
 def IsRowInCircuitTable(self,nRow):
  """
  IsRowInCircuitTable(self: PanelScheduleView,nRow: int) -> bool

  

   Check if this row in the circuit table

  

   nRow: Row Number

   Returns: True if this row in the circuit table,false otherwise.
  """
  pass
 def IsSlotGrouped(self,nRow,nCol):
  """
  IsSlotGrouped(self: PanelScheduleView,nRow: int,nCol: int) -> int

  

   Check if the slot is in a group

  

   nRow: Row Number

   nCol: Column Number

   Returns: It is not in a group if the return value equals to 0. It is in a group if the 

    return value is greater than 0 and the return value is the group number.
  """
  pass
 def IsSlotLocked(self,nRow,nCol):
  """
  IsSlotLocked(self: PanelScheduleView,nRow: int,nCol: int) -> bool

  

   Check if the circuit slot in this cell is locked.

  

   nRow: Row Number

   nCol: Column Number

   Returns: True if the circuit slot in this cell is locked,false otherwise
  """
  pass
 def IsSpace(self,nRow,nCol):
  """
  IsSpace(self: PanelScheduleView,nRow: int,nCol: int) -> bool

  

   Check if the selected cell is a space

  

   nRow: Row Number

   nCol: Column Number

   Returns: True if the selected cell is a space,false otherwise
  """
  pass
 def IsSpare(self,nRow,nCol):
  """
  IsSpare(self: PanelScheduleView,nRow: int,nCol: int) -> bool

  

   Check if the circuit is a spare

  

   nRow: Row Number

   nCol: Column Number

   Returns: True if the circuit is a spare,false otherwise
  """
  pass
 def MoveSlotTo(self,nMovingRow,nMovingCol,nToRow,nToCol):
  """
  MoveSlotTo(self: PanelScheduleView,nMovingRow: int,nMovingCol: int,nToRow: int,nToCol: int)

   Move the circuits in the source slot to the specific slot.

  

   nMovingRow: The Row Number of cell to be moved.

   nMovingCol: Start Column Number of cell to be moved.

   nToRow: The Row Number of cell to moved to.

   nToCol: End Column Number of cell to moved to.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetParamValue(self,sectionType,nRow,nCol,sValue):
  """
  SetParamValue(self: PanelScheduleView,sectionType: SectionType,nRow: int,nCol: int,sValue: str) -> bool

  

   Sets the text for the given cell,returns true if successful,false otherwise

  

   sectionType: The associated section

   nRow: Row Number of the Section

   nCol: Column Number of the Section

   sValue: String value to set the parameter

   Returns: Returns whether the function succeeded
  """
  pass
 def SetSpareCurrentValue(self,row,column,idCurrentParameter,value):
  """
  SetSpareCurrentValue(self: PanelScheduleView,row: int,column: int,idCurrentParameter: ElementId,value: float)

   Sets the value of the apparent current parameter for a spare

  

   row: A row where the valid spare is

   column: A column where the valid spare is

   idCurrentParameter: One of 4 valid current parameters: RBS_ELEC_APPARENT_CURRENT_PARAM,

    RBS_ELEC_APPARENT_CURRENT_PHASEA_PARAM,RBS_ELEC_APPARENT_CURRENT_PHASEB_PARAM,

    RBS_ELEC_APPARENT_CURRENT_PHASEC_PARAM

  

   value: The value of the spare's current for the given parameter
  """
  pass
 def SetSpareLoadValue(self,row,column,idLoadParameter,value):
  """
  SetSpareLoadValue(self: PanelScheduleView,row: int,column: int,idLoadParameter: ElementId,value: float)

   Sets the value of the apparent load parameter for a spare

  

   row: A row where the valid spare is

   column: A column where the valid spare is

   idLoadParameter: One of 4 valid load parameters: RBS_ELEC_APPARENT_LOAD,

    RBS_ELEC_APPARENT_LOAD_PHASEA,RBS_ELEC_APPARENT_LOAD_PHASEB,

    RBS_ELEC_APPARENT_LOAD_PHASEC

  

   value: The value of the spare's load for the given parameter
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
