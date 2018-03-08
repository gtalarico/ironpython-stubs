# encoding: utf-8
# module Tekla.Structures.Model.Operations calls itself Operations
# from Tekla.Structures.Model,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GuidConversion(object):
 """ GuidConversion() """
 def GetGuidMapping(self):
  """ GetGuidMapping(self: GuidConversion) -> Dictionary[Guid,Guid] """
  pass
 def GetNewGuid(self,oldGuid):
  """ GetNewGuid(self: GuidConversion,oldGuid: Guid) -> Guid """
  pass

class Operation(object):
 # no doc
 @staticmethod
 def CalculatePourUnits():
  """ CalculatePourUnits() -> bool """
  pass
 @staticmethod
 def Combine(ObjectToCombineTo,ObjectToBeCombined):
  """
  Combine(ObjectToCombineTo: RebarGroup,ObjectToBeCombined: RebarGroup) -> RebarGroup
  Combine(ObjectToCombineTo: SingleRebar,ObjectToBeCombined: SingleRebar) -> SingleRebar
  Combine(ObjectToCombineTo: Beam,ObjectToBeCombined: Beam) -> Beam
  """
  pass
 @staticmethod
 def CopyObject(Object,*__args):
  """
  CopyObject(Object: ModelObject,StartCoordinateSystem: CoordinateSystem,EndCoordinateSystem: CoordinateSystem) -> ModelObject
  CopyObject(Object: ModelObject,CopyVector: Vector) -> ModelObject
  """
  pass
 @staticmethod
 def CreateBentPlateByFaces(part1,face1,part2,face2,radius=None):
  """
  CreateBentPlateByFaces(part1: Part,face1: IList[Point],part2: Part,face2: IList[Point],radius: float) -> BentPlate
  CreateBentPlateByFaces(part1: Part,face1: Face,part2: Part,face2: Face,radius: float) -> BentPlate
  CreateBentPlateByFaces(part1: Part,face1: IList[Point],part2: Part,face2: IList[Point]) -> BentPlate
  CreateBentPlateByFaces(part1: Part,face1: Face,part2: Part,face2: Face) -> BentPlate
  """
  pass
 @staticmethod
 def CreateBentPlateByParts(part1,part2,radius=None):
  """
  CreateBentPlateByParts(part1: Part,part2: Part,radius: float) -> BentPlate
  CreateBentPlateByParts(part1: Part,part2: Part) -> BentPlate
  """
  pass
 @staticmethod
 def CreateMISFileFromAll(MISType,FileName):
  """ CreateMISFileFromAll(MISType: MISExportTypeEnum,FileName: str) -> bool """
  pass
 @staticmethod
 def CreateMISFileFromSelected(MISType,FileName):
  """ CreateMISFileFromSelected(MISType: MISExportTypeEnum,FileName: str) -> bool """
  pass
 @staticmethod
 def CreateNCFilesFromAll(NCFileSettings,DestinationFolder):
  """ CreateNCFilesFromAll(NCFileSettings: str,DestinationFolder: str) -> bool """
  pass
 @staticmethod
 def CreateNCFilesFromSelected(NCFileSettings,DestinationFolder):
  """ CreateNCFilesFromSelected(NCFileSettings: str,DestinationFolder: str) -> bool """
  pass
 @staticmethod
 def CreateReportFromAll(TemplateName,FileName,Title1,Title2,Title3):
  """ CreateReportFromAll(TemplateName: str,FileName: str,Title1: str,Title2: str,Title3: str) -> bool """
  pass
 @staticmethod
 def CreateReportFromSelected(TemplateName,FileName,Title1,Title2,Title3):
  """ CreateReportFromSelected(TemplateName: str,FileName: str,Title1: str,Title2: str,Title3: str) -> bool """
  pass
 @staticmethod
 def DisplayPrompt(Message):
  """ DisplayPrompt(Message: str) -> bool """
  pass
 @staticmethod
 def DisplayReport(FileName):
  """ DisplayReport(FileName: str) -> bool """
  pass
 @staticmethod
 def ExplodeBentPlate(bentPlate):
  """ ExplodeBentPlate(bentPlate: BentPlate) -> bool """
  pass
 @staticmethod
 def Group(RebarList):
  """ Group(RebarList: IEnumerable) -> RebarGroup """
  pass
 @staticmethod
 def IsMacroRunning():
  """ IsMacroRunning() -> bool """
  pass
 @staticmethod
 def IsModelAutoSaved(ModelFolder):
  """ IsModelAutoSaved(ModelFolder: str) -> bool """
  pass
 @staticmethod
 def IsNumberingUpToDate(ModelObject):
  """ IsNumberingUpToDate(ModelObject: ModelObject) -> bool """
  pass
 @staticmethod
 def IsNumberingUpToDateAll():
  """ IsNumberingUpToDateAll() -> bool """
  pass
 @staticmethod
 def MoveObject(Object,*__args):
  """
  MoveObject(Object: ModelObject,StartCoordinateSystem: CoordinateSystem,EndCoordinateSystem: CoordinateSystem) -> bool
  MoveObject(Object: ModelObject,TranslationVector: Vector) -> bool
  """
  pass
 @staticmethod
 def ObjectMatchesToFilter(ModelObject,*__args):
  """
  ObjectMatchesToFilter(ModelObject: ModelObject,FilterExpression: FilterExpression) -> bool
  ObjectMatchesToFilter(ModelObject: ModelObject,FilterName: str) -> bool
  """
  pass
 @staticmethod
 def Open(ModelFolder,OpenAutoSaved=None):
  """
  Open(ModelFolder: str,OpenAutoSaved: bool) -> bool
  Open(ModelFolder: str) -> bool
  """
  pass
 @staticmethod
 def RemoveFromPourUnit(objectsToBeRemoved):
  """ RemoveFromPourUnit(objectsToBeRemoved: List[ModelObject]) -> bool """
  pass
 @staticmethod
 def RunMacro(FileName):
  """ RunMacro(FileName: str) -> bool """
  pass
 @staticmethod
 def SaveAsWebModel(Filename):
  """ SaveAsWebModel(Filename: str) -> bool """
  pass
 @staticmethod
 def SaveSelectedAsWebModel(Filename):
  """ SaveSelectedAsWebModel(Filename: str) -> bool """
  pass
 @staticmethod
 def ShowOnlySelected(UnselectedMode):
  """ ShowOnlySelected(UnselectedMode: UnselectedModeEnum) """
  pass
 @staticmethod
 def Split(Object,*__args):
  """
  Split(Object: CircleRebarGroup,SplitLine: Line) -> CircleRebarGroup
  Split(Object: RebarGroup,SplitLine: Line) -> RebarGroup
  Split(Object: ContourPlate,SplitPolygon: Polygon) -> ContourPlate
  Split(Object: Beam,SplitPoint: Point) -> Beam
  Split(Object: SingleRebar,SplitLine: Line) -> SingleRebar
  Split(Object: CurvedRebarGroup,SplitLine: Line) -> CurvedRebarGroup
  """
  pass
 @staticmethod
 def Ungrouping(Reinforcement):
  """
  Ungrouping(Reinforcement: RebarMesh) -> ModelObjectEnumerator
  Ungrouping(Reinforcement: RebarGroup) -> ModelObjectEnumerator
  """
  pass
 MISExportTypeEnum=None
 ProgressBar=None
 UnselectedModeEnum=None
 __all__=[
  '__reduce_ex__',
  'CalculatePourUnits',
  'Combine',
  'CopyObject',
  'CreateBentPlateByFaces',
  'CreateBentPlateByParts',
  'CreateMISFileFromAll',
  'CreateMISFileFromSelected',
  'CreateNCFilesFromAll',
  'CreateNCFilesFromSelected',
  'CreateReportFromAll',
  'CreateReportFromSelected',
  'DisplayPrompt',
  'DisplayReport',
  'ExplodeBentPlate',
  'Group',
  'IsMacroRunning',
  'IsModelAutoSaved',
  'IsNumberingUpToDate',
  'IsNumberingUpToDateAll',
  'MISExportTypeEnum',
  'MoveObject',
  'ObjectMatchesToFilter',
  'Open',
  'ProgressBar',
  'RemoveFromPourUnit',
  'RunMacro',
  'SaveAsWebModel',
  'SaveSelectedAsWebModel',
  'ShowOnlySelected',
  'Split',
  'Ungrouping',
  'UnselectedModeEnum',
 ]


