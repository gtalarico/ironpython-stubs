class Operation(object):
 # no doc
 @staticmethod
 def AddToPourUnit(inputPour,objectsToBeAdded):
  """ AddToPourUnit(inputPour: PourObject,objectsToBeAdded: List[ModelObject]) -> bool """
  pass
 @staticmethod
 def CreateBasePoint(basePoint):
  """ CreateBasePoint(basePoint: BasePoint) -> bool """
  pass
 @staticmethod
 def DeleteBasePoint(basePoint):
  """ DeleteBasePoint(basePoint: BasePoint) -> bool """
  pass
 @staticmethod
 def DeleteMacro(fileName,macroLocation):
  """ DeleteMacro(fileName: str,macroLocation: MacroLocationEnum) -> bool """
  pass
 @staticmethod
 def dotAutoSaveModel(Comment,User):
  """ dotAutoSaveModel(Comment: str,User: str) -> bool """
  pass
 @staticmethod
 def dotCheckBoltAssemblyDefinitionsModified(ModStamp):
  """ dotCheckBoltAssemblyDefinitionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckBoltDefinitionsModified(ModStamp):
  """ dotCheckBoltDefinitionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckCustomPropertiesModified(ModStamp):
  """ dotCheckCustomPropertiesModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckDrawingOptionsModified(ModStamp):
  """ dotCheckDrawingOptionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckDrawingsModified(ModStamp):
  """ dotCheckDrawingsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckMaterialDefinitionsModified(ModStamp):
  """ dotCheckMaterialDefinitionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckModelOptionsModified(ModStamp):
  """ dotCheckModelOptionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckObjectModifiedAfterStamp(objectGuid,ModStamp):
  """ dotCheckObjectModifiedAfterStamp(objectGuid: Guid,ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCheckProfileDefinitionsModified(ModStamp):
  """ dotCheckProfileDefinitionsModified(ModStamp: str) -> bool """
  pass
 @staticmethod
 def dotCleanDrawingFiles(Silent,BackupPath):
  """ dotCleanDrawingFiles(Silent: bool,BackupPath: str) -> bool """
  pass
 @staticmethod
 def dotClearUndoLog():
  """ dotClearUndoLog() """
  pass
 @staticmethod
 def dotConnectToNewMultiUserServerAndOpenModel(ModelFolder,ServerName):
  """ dotConnectToNewMultiUserServerAndOpenModel(ModelFolder: str,ServerName: str) -> bool """
  pass
 @staticmethod
 def dotConvertAndOpenAsMultiUserModel(ModelFolder,ServerName):
  """ dotConvertAndOpenAsMultiUserModel(ModelFolder: str,ServerName: str) -> bool """
  pass
 @staticmethod
 def dotConvertAndOpenAsSingleUserModel(ModelFolder):
  """ dotConvertAndOpenAsSingleUserModel(ModelFolder: str) -> bool """
  pass
 @staticmethod
 def dotCreateNewMultiUserModel(ModelName,ModelPath,ServerName):
  """ dotCreateNewMultiUserModel(ModelName: str,ModelPath: str,ServerName: str) -> bool """
  pass
 @staticmethod
 def dotCreateNewSharedModel(ModelName,ModelPath):
  """ dotCreateNewSharedModel(ModelName: str,ModelPath: str) -> bool """
  pass
 @staticmethod
 def dotCreateNewSingleUserModel(ModelName,ModelPath):
  """ dotCreateNewSingleUserModel(ModelName: str,ModelPath: str) -> bool """
  pass
 @staticmethod
 def dotCreateNewSingleUserModelFromTemplate(ModelName,ModelPath,ModelTemplateName):
  """ dotCreateNewSingleUserModelFromTemplate(ModelName: str,ModelPath: str,ModelTemplateName: str) -> bool """
  pass
 @staticmethod
 def dotDisplayAutoDefaultSettings(type,componentNumber,componentName):
  """ dotDisplayAutoDefaultSettings(type: ModelObjectEnum,componentNumber: int,componentName: str) -> bool """
  pass
 @staticmethod
 def dotDisplayComponentHelp(type,componentNumber,componentName):
  """ dotDisplayComponentHelp(type: ModelObjectEnum,componentNumber: int,componentName: str) -> bool """
  pass
 @staticmethod
 def dotExcludeFromSharingAndOpen(ModelFolder):
  """ dotExcludeFromSharingAndOpen(ModelFolder: str) -> bool """
  pass
 @staticmethod
 def dotExportGetColorRepresentationForObject(ID,color):
  """ dotExportGetColorRepresentationForObject(ID: int,color: Color) -> (bool,Color) """
  pass
 @staticmethod
 def dotExportShadowRegion(PartIdentifiers):
  """ dotExportShadowRegion(PartIdentifiers: ArrayList) -> ArrayList """
  pass
 @staticmethod
 def dotExportShadowRegionComplement(PartIdentifiers):
  """ dotExportShadowRegionComplement(PartIdentifiers: ArrayList) -> ArrayList """
  pass
 @staticmethod
 def dotGetCurrentModificationStampGuid():
  """ dotGetCurrentModificationStampGuid() -> str """
  pass
 @staticmethod
 def dotGetDatabaseVersion():
  """ dotGetDatabaseVersion() -> int """
  pass
 @staticmethod
 def dotGetDataBaseVersionInfoFromModel(ModelName,ModelPath,ModelVersion,CurrentVersion):
  """ dotGetDataBaseVersionInfoFromModel(ModelName: str,ModelPath: str,ModelVersion: int,CurrentVersion: int) -> (bool,int,int) """
  pass
 @staticmethod
 def dotGetDeletedObjecs(ModStamp,ObjectTypes,returnAlsoIfObjectIsCreatedAndDeletedAfterEvent):
  """ dotGetDeletedObjecs(ModStamp: str,ObjectTypes: IEnumerable[ModelObjectEnum],returnAlsoIfObjectIsCreatedAndDeletedAfterEvent: bool) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def dotGetModifications(ModStamp,ObjectTypes,returnAlsoIfObjectIsCreatedAndDeletedAfterEvent):
  """ dotGetModifications(ModStamp: str,ObjectTypes: IEnumerable[ModelObjectEnum],returnAlsoIfObjectIsCreatedAndDeletedAfterEvent: bool) -> ModificationInfo """
  pass
 @staticmethod
 def dotGetModificationsByFilter(ModStamp,FilterName):
  """ dotGetModificationsByFilter(ModStamp: str,FilterName: str) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def dotGetObjectsWithAnyModification(ModStamp,ObjectTypes):
  """ dotGetObjectsWithAnyModification(ModStamp: str,ObjectTypes: IEnumerable[ModelObjectEnum]) -> ModelObjectEnumerator """
  pass
 @staticmethod
 def dotIsModelSaved(ModelFolder):
  """ dotIsModelSaved(ModelFolder: str) -> bool """
  pass
 @staticmethod
 def dotModelImportIsEnabled():
  """ dotModelImportIsEnabled() -> bool """
  pass
 @staticmethod
 def dotModelSharingLicenseInfo(ProfileId):
  """ dotModelSharingLicenseInfo(ProfileId: str) -> bool """
  pass
 @staticmethod
 def dotQuitProgram(Comment,User):
  """ dotQuitProgram(Comment: str,User: str) -> bool """
  pass
 @staticmethod
 def dotRedo():
  """ dotRedo() """
  pass
 @staticmethod
 def dotResetUserOptionToDefaultValue(VariableName):
  """ dotResetUserOptionToDefaultValue(VariableName: str) -> bool """
  pass
 @staticmethod
 def dotSaveAsModel(path,Comment,User):
  """ dotSaveAsModel(path: str,Comment: str,User: str) -> bool """
  pass
 @staticmethod
 def dotSaveModel(Comment,User):
  """ dotSaveModel(Comment: str,User: str) -> bool """
  pass
 @staticmethod
 def dotSetAdvancedOption(VariableName,Value):
  """
  dotSetAdvancedOption(VariableName: str,Value: str) -> bool
  dotSetAdvancedOption(VariableName: str,Value: float) -> bool
  dotSetAdvancedOption(VariableName: str,Value: bool) -> bool
  dotSetAdvancedOption(VariableName: str,Value: int) -> bool
  """
  pass
 @staticmethod
 def dotSetUserModelRole(modelId,modelFolder,userId,role):
  """ dotSetUserModelRole(modelId: Guid,modelFolder: str,userId: Guid,role: DotSharingPrivilegeEnum) -> bool """
  pass
 @staticmethod
 def dotSharingCommandResult(commandId,success,ErrorCode,ErrorDetail):
  """ dotSharingCommandResult(commandId: int,success: bool,ErrorCode: DotSharingErrorCodeEnum,ErrorDetail: str) -> bool """
  pass
 @staticmethod
 def dotSharingCreateEmptyModel(modelName,modelPath):
  """ dotSharingCreateEmptyModel(modelName: str,modelPath: str) -> bool """
  pass
 @staticmethod
 def dotSharingCreateNewModel(modelName,modelPath):
  """ dotSharingCreateNewModel(modelName: str,modelPath: str) -> bool """
  pass
 @staticmethod
 def dotSharingCreateStartSharingBackup(backupFolder):
  """ dotSharingCreateStartSharingBackup(backupFolder: str) -> bool """
  pass
 @staticmethod
 def dotSharingGetVersionGuid(versionGuid):
  """ dotSharingGetVersionGuid(versionGuid: Guid) -> (bool,Guid) """
  pass
 @staticmethod
 def dotSharingIsEnabled():
  """ dotSharingIsEnabled() -> bool """
  pass
 @staticmethod
 def dotSharingLogPrint(type,message):
  """ dotSharingLogPrint(type: DotSharingLogTypeEnum,message: str) """
  pass
 @staticmethod
 def dotSharingMakeModelShareable(xml):
  """ dotSharingMakeModelShareable(xml: str) -> bool """
  pass
 @staticmethod
 def dotSharingOpenModelForJoin(modelFolder):
  """ dotSharingOpenModelForJoin(modelFolder: str) -> bool """
  pass
 @staticmethod
 def dotSharingReadIn(packetFolder,packetNumber,errorCode,errorDetail,moduleBaselines):
  """ dotSharingReadIn(packetFolder: str,packetNumber: int) -> (bool,DotSharingErrorCodeEnum,str,Dictionary[str,Tuple[str,str]]) """
  pass
 @staticmethod
 def dotSharingReadInCommit(success,joiningSharing):
  """ dotSharingReadInCommit(success: bool,joiningSharing: bool) -> bool """
  pass
 @staticmethod
 def dotSharingReadInStarting(joiningSharing):
  """ dotSharingReadInStarting(joiningSharing: bool) -> bool """
  pass
 @staticmethod
 def dotSharingRegisterPlugin(name,asynchronous):
  """ dotSharingRegisterPlugin(name: str,asynchronous: bool) -> bool """
  pass
 @staticmethod
 def dotSharingRestoreStartSharingBackup(backupFolder):
  """ dotSharingRestoreStartSharingBackup(backupFolder: str) -> bool """
  pass
 @staticmethod
 def dotSharingSaveVersionGuid(versionGuid,packetNumber,baselines):
  """ dotSharingSaveVersionGuid(versionGuid: Guid,packetNumber: int,baselines: Dictionary[str,str]) -> bool """
  pass
 @staticmethod
 def dotSharingSetMenu(privilege):
  """ dotSharingSetMenu(privilege: DotSharingPrivilegeEnum) -> bool """
  pass
 @staticmethod
 def dotSharingShowReadInChanges():
  """ dotSharingShowReadInChanges() -> bool """
  pass
 @staticmethod
 def dotSharingWriteOut(permission,packetFolder,mode,revisionInfo,errorCode,errorDetail,moduleBaselines):
  """ dotSharingWriteOut(permission: DotSharingPrivilegeEnum,packetFolder: str,mode: DotSharingWriteOutModeEnum,revisionInfo: str) -> (bool,DotSharingErrorCodeEnum,str,Dictionary[str,Tuple[str,str]]) """
  pass
 @staticmethod
 def dotSharingWriteOutCommit(success,packetFolder,packetNumber,moduleBaselines):
  """ dotSharingWriteOutCommit(success: bool,packetFolder: str,packetNumber: int) -> (bool,Dictionary[str,Tuple[str,str]]) """
  pass
 @staticmethod
 def dotStartAction(ActionName,Parameters):
  """ dotStartAction(ActionName: str,Parameters: str) -> bool """
  pass
 @staticmethod
 def dotStartCommand(CommandName,Parameters):
  """ dotStartCommand(CommandName: str,Parameters: str) -> bool """
  pass
 @staticmethod
 def dotStartCustomComponentCreation(ComponentName):
  """ dotStartCustomComponentCreation(ComponentName: str) -> bool """
  pass
 @staticmethod
 def dotStartPluginCreation(ComponentName):
  """ dotStartPluginCreation(ComponentName: str) -> bool """
  pass
 @staticmethod
 def dotUndo():
  """ dotUndo() """
  pass
 @staticmethod
 def dotWriteToSessionLog(Message):
  """ dotWriteToSessionLog(Message: str) -> bool """
  pass
 @staticmethod
 def ExportIFCFromAll(ModelName,FullFileName,ViewType,PropertySets,BasePoint,UseTimer,CreateReport):
  """ ExportIFCFromAll(ModelName: str,FullFileName: str,ViewType: IFCExportViewTypeEnum,PropertySets: List[str],BasePoint: IFCExportBasePoint,UseTimer: bool,CreateReport: bool) -> bool """
  pass
 @staticmethod
 def ExportIFCFromFilteredObjects(ModelName,FullFileName,ViewType,PropertySets,FilterName,BasePoint,UseTimer,CreateReport):
  """ ExportIFCFromFilteredObjects(ModelName: str,FullFileName: str,ViewType: IFCExportViewTypeEnum,PropertySets: List[str],FilterName: str,BasePoint: IFCExportBasePoint,UseTimer: bool,CreateReport: bool) -> bool """
  pass
 @staticmethod
 def ExportIFCFromObjects(ModelName,FullFileName,ViewType,PropertySets,ModelObjects,BasePoint,UseTimer,CreateReport):
  """ ExportIFCFromObjects(ModelName: str,FullFileName: str,ViewType: IFCExportViewTypeEnum,PropertySets: List[str],ModelObjects: List[ModelObject],BasePoint: IFCExportBasePoint,UseTimer: bool,CreateReport: bool) -> bool """
  pass
 @staticmethod
 def ExportIFCFromSelected(ModelName,FullFileName,ViewType,PropertySets,BasePoint,UseTimer,CreateReport):
  """ ExportIFCFromSelected(ModelName: str,FullFileName: str,ViewType: IFCExportViewTypeEnum,PropertySets: List[str],BasePoint: IFCExportBasePoint,UseTimer: bool,CreateReport: bool) -> bool """
  pass
 @staticmethod
 def GetBasePointByGuid(guid):
  """ GetBasePointByGuid(guid: Guid) -> BasePoint """
  pass
 @staticmethod
 def GetBasePointByName(name):
  """ GetBasePointByName(name: str) -> BasePoint """
  pass
 @staticmethod
 def GetBasePoints():
  """ GetBasePoints() -> List[BasePoint] """
  pass
 @staticmethod
 def ModifyBasePoint(basePoint):
  """ ModifyBasePoint(basePoint: BasePoint) -> bool """
  pass
 @staticmethod
 def RollbackToTestSavePoint():
  """ RollbackToTestSavePoint() """
  pass
 @staticmethod
 def SetTestSavePoint():
  """ SetTestSavePoint() """
  pass
 DotSharingErrorCodeEnum=None
 DotSharingLogTypeEnum=None
 DotSharingPrivilegeEnum=None
 DotSharingWriteOutModeEnum=None
 IFCExportBasePoint=None
 IFCExportViewTypeEnum=None
 MacroLocationEnum=None
 OperationsMaxMessageLength=2000
 SaveOperationEnum=None
 SharingOperationEnum=None
 UndoOperationEnum=None
 __all__=[
  '__reduce_ex__',
  'AddToPourUnit',
  'CreateBasePoint',
  'DeleteBasePoint',
  'DeleteMacro',
  'dotAutoSaveModel',
  'dotCheckBoltAssemblyDefinitionsModified',
  'dotCheckBoltDefinitionsModified',
  'dotCheckCustomPropertiesModified',
  'dotCheckDrawingOptionsModified',
  'dotCheckDrawingsModified',
  'dotCheckMaterialDefinitionsModified',
  'dotCheckModelOptionsModified',
  'dotCheckObjectModifiedAfterStamp',
  'dotCheckProfileDefinitionsModified',
  'dotCleanDrawingFiles',
  'dotClearUndoLog',
  'dotConnectToNewMultiUserServerAndOpenModel',
  'dotConvertAndOpenAsMultiUserModel',
  'dotConvertAndOpenAsSingleUserModel',
  'dotCreateNewMultiUserModel',
  'dotCreateNewSharedModel',
  'dotCreateNewSingleUserModel',
  'dotCreateNewSingleUserModelFromTemplate',
  'dotDisplayAutoDefaultSettings',
  'dotDisplayComponentHelp',
  'dotExcludeFromSharingAndOpen',
  'dotExportGetColorRepresentationForObject',
  'dotExportShadowRegion',
  'dotExportShadowRegionComplement',
  'dotGetCurrentModificationStampGuid',
  'dotGetDatabaseVersion',
  'dotGetDataBaseVersionInfoFromModel',
  'dotGetDeletedObjecs',
  'dotGetModifications',
  'dotGetModificationsByFilter',
  'dotGetObjectsWithAnyModification',
  'dotIsModelSaved',
  'dotModelImportIsEnabled',
  'dotModelSharingLicenseInfo',
  'dotQuitProgram',
  'dotRedo',
  'dotResetUserOptionToDefaultValue',
  'dotSaveAsModel',
  'dotSaveModel',
  'dotSetAdvancedOption',
  'dotSetUserModelRole',
  'dotSharingCommandResult',
  'dotSharingCreateEmptyModel',
  'dotSharingCreateNewModel',
  'dotSharingCreateStartSharingBackup',
  'DotSharingErrorCodeEnum',
  'dotSharingGetVersionGuid',
  'dotSharingIsEnabled',
  'dotSharingLogPrint',
  'DotSharingLogTypeEnum',
  'dotSharingMakeModelShareable',
  'dotSharingOpenModelForJoin',
  'DotSharingPrivilegeEnum',
  'dotSharingReadIn',
  'dotSharingReadInCommit',
  'dotSharingReadInStarting',
  'dotSharingRegisterPlugin',
  'dotSharingRestoreStartSharingBackup',
  'dotSharingSaveVersionGuid',
  'dotSharingSetMenu',
  'dotSharingShowReadInChanges',
  'dotSharingWriteOut',
  'dotSharingWriteOutCommit',
  'DotSharingWriteOutModeEnum',
  'dotStartAction',
  'dotStartCommand',
  'dotStartCustomComponentCreation',
  'dotStartPluginCreation',
  'dotUndo',
  'dotWriteToSessionLog',
  'ExportIFCFromAll',
  'ExportIFCFromFilteredObjects',
  'ExportIFCFromObjects',
  'ExportIFCFromSelected',
  'GetBasePointByGuid',
  'GetBasePointByName',
  'GetBasePoints',
  'IFCExportBasePoint',
  'IFCExportViewTypeEnum',
  'MacroLocationEnum',
  'ModifyBasePoint',
  'OperationsMaxMessageLength',
  'RollbackToTestSavePoint',
  'SaveOperationEnum',
  'SetTestSavePoint',
  'SharingOperationEnum',
  'UndoOperationEnum',
 ]

