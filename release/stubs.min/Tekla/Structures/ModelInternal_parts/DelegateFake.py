class DelegateFake(object):
 """ DelegateFake() """
 def EditMacro(self,FileName):
  """ EditMacro(self: DelegateFake,FileName: str) -> int """
  pass
 def ExplodeBentPlate(self,partId):
  """ ExplodeBentPlate(self: DelegateFake,partId: int) -> int """
  pass
 def ExportAddComponentAttributeToStack(self,pAttr):
  """ ExportAddComponentAttributeToStack(self: DelegateFake,pAttr: dotComponentAttribute_t) -> (int,dotComponentAttribute_t) """
  pass
 def ExportAddComponentInputToStack(self,pObj):
  """ ExportAddComponentInputToStack(self: DelegateFake,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportAddToPourUnit(self,inputPour,clientId):
  """ ExportAddToPourUnit(self: DelegateFake,inputPour: dotPourObject_t,clientId: dotClientId_t) -> (bool,dotPourObject_t,dotClientId_t) """
  pass
 def ExportAutoConnectSetupConnectionBrowserCB(self,elementNumber):
  """ ExportAutoConnectSetupConnectionBrowserCB(self: DelegateFake,elementNumber: int) -> int """
  pass
 def ExportCalculateContourPolygon(self,pContour,pPolygon):
  """ ExportCalculateContourPolygon(self: DelegateFake,pContour: dotContour_t,pPolygon: dotPolygon_t) -> (int,dotContour_t,dotPolygon_t) """
  pass
 def ExportCalculatePourUnits(self):
  """ ExportCalculatePourUnits(self: DelegateFake) -> bool """
  pass
 def ExportChangeManagerAllowNumbering(self,NumberingFlag):
  """ ExportChangeManagerAllowNumbering(self: DelegateFake,NumberingFlag: bool) -> int """
  pass
 def ExportChangeManagerAllowSave(self,SaveFlag):
  """ ExportChangeManagerAllowSave(self: DelegateFake,SaveFlag: bool) -> int """
  pass
 def ExportCleanDrawingFiles(self,Silent,BackupPath):
  """ ExportCleanDrawingFiles(self: DelegateFake,Silent: bool,BackupPath: str) -> int """
  pass
 def ExportClearAllTemporaryStates(self):
  """ ExportClearAllTemporaryStates(self: DelegateFake) -> int """
  pass
 def ExportClearTemporaryState(self,pObjectId):
  """ ExportClearTemporaryState(self: DelegateFake,pObjectId: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportCommitChanges(self,pModelCommit):
  """ ExportCommitChanges(self: DelegateFake,pModelCommit: dotModelCommit_t) -> (int,dotModelCommit_t) """
  pass
 def ExportCompareFingerprints(self,fingerprint1,fingerprint2):
  """ ExportCompareFingerprints(self: DelegateFake,fingerprint1: str,fingerprint2: str) -> bool """
  pass
 def ExportCompareObjects(self,ObjectId,ObjectToCompareId):
  """ ExportCompareObjects(self: DelegateFake,ObjectId: int,ObjectToCompareId: int) -> int """
  pass
 def ExportConnectGeometryTrees(self,clientId):
  """ ExportConnectGeometryTrees(self: DelegateFake,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPoints(self,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPoints(self: DelegateFake,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPointsWithRadius(self,radius,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPointsWithRadius(self: DelegateFake,radius: float,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesWithRadius(self,radius,clientId):
  """ ExportConnectGeometryTreesWithRadius(self: DelegateFake,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportCreateBasePoint(self,pBasePoint):
  """ ExportCreateBasePoint(self: DelegateFake,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportCreateBentPlateByFaces(self,part1Id,part2Id,face1,face2):
  """ ExportCreateBentPlateByFaces(self: DelegateFake,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByFacesAndRadius(self,part1Id,part2Id,face1,face2,radius):
  """ ExportCreateBentPlateByFacesAndRadius(self: DelegateFake,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t,radius: float) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByParts(self,part1Id,part2Id):
  """ ExportCreateBentPlateByParts(self: DelegateFake,part1Id: int,part2Id: int) -> int """
  pass
 def ExportCreateBentPlateByPartsAndRadius(self,part1Id,part2Id,radius):
  """ ExportCreateBentPlateByPartsAndRadius(self: DelegateFake,part1Id: int,part2Id: int,radius: float) -> int """
  pass
 def ExportCreateBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportCreateBoltGroup(self: DelegateFake,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportCreateBooleanPart(self,pBooleanPart):
  """ ExportCreateBooleanPart(self: DelegateFake,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportCreateClipPlane(self,pDotView,pDotClipPlane):
  """ ExportCreateClipPlane(self: DelegateFake,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportCreateComponent(self,pBaseComponent):
  """ ExportCreateComponent(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportCreateControlPlane(self,pControlObject):
  """ ExportCreateControlPlane(self: DelegateFake,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportCreateConversionLink(self,pConversionLink):
  """ ExportCreateConversionLink(self: DelegateFake,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportCreateEdgeChamfer(self,pEdgeChamfer):
  """ ExportCreateEdgeChamfer(self: DelegateFake,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportCreateFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportCreateFittingOrCutPlane(self: DelegateFake,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportCreateGrid(self,pGrid):
  """ ExportCreateGrid(self: DelegateFake,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportCreateGridPlane(self,pGridPlane):
  """ ExportCreateGridPlane(self: DelegateFake,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportCreateGuideline(self,pGuideline):
  """ ExportCreateGuideline(self: DelegateFake,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportCreateIFC(self,aIFC):
  """ ExportCreateIFC(self: DelegateFake,aIFC: dotCreateIFCFromModel_t) -> (int,dotCreateIFCFromModel_t) """
  pass
 def ExportCreateLegFace(self,pLegFace):
  """ ExportCreateLegFace(self: DelegateFake,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportCreateLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportCreateLoad(self: DelegateFake,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportCreateLoadGroup(self,pLoadGroup):
  """ ExportCreateLoadGroup(self: DelegateFake,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportCreateNC(self,aNC):
  """ ExportCreateNC(self: DelegateFake,aNC: dotCreateNCFromModel_t) -> (int,dotCreateNCFromModel_t) """
  pass
 def ExportCreateNewModel(self,pInfo):
  """ ExportCreateNewModel(self: DelegateFake,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportCreatePart(self,pPart,contour):
  """ ExportCreatePart(self: DelegateFake,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportCreatePourBreak(self,pPolymesh):
  """ ExportCreatePourBreak(self: DelegateFake,pPolymesh: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportCreateRebarEndDetailStrip(self,pStrip):
  """ ExportCreateRebarEndDetailStrip(self: DelegateFake,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportCreateRebarGroup(self,pRebarGroup):
  """ ExportCreateRebarGroup(self: DelegateFake,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportCreateRebarMesh(self,pRebarMesh):
  """ ExportCreateRebarMesh(self: DelegateFake,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportCreateRebarPropertyStrip(self,pStrip):
  """ ExportCreateRebarPropertyStrip(self: DelegateFake,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportCreateRebarSplice(self,pRebarSplice):
  """ ExportCreateRebarSplice(self: DelegateFake,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportCreateRebarSplitter(self,pStrip):
  """ ExportCreateRebarSplitter(self: DelegateFake,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportCreateRebarStrand(self,pRebarStrand):
  """ ExportCreateRebarStrand(self: DelegateFake,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportCreateReferenceModel(self,pReferenceModel):
  """ ExportCreateReferenceModel(self: DelegateFake,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportCreateReferenceModelObjectAttribute(self,pRMOAttribute):
  """ ExportCreateReferenceModelObjectAttribute(self: DelegateFake,pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int,dotReferenceModelObjectAttribute_t) """
  pass
 def ExportCreateReferenceModelObjectAttributeEnumerator(self,pEnumerator):
  """ ExportCreateReferenceModelObjectAttributeEnumerator(self: DelegateFake,pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int,dotReferenceModelObjectAttributeEnumerator_t) """
  pass
 def ExportCreateReport(self,aReport):
  """ ExportCreateReport(self: DelegateFake,aReport: dotCreateReportFromModel_t) -> (int,dotCreateReportFromModel_t) """
  pass
 def ExportCreateSingleRebar(self,pSingleRebar):
  """ ExportCreateSingleRebar(self: DelegateFake,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportCreateSurfaceByFace(self,hitPoint,faceNormal,id):
  """ ExportCreateSurfaceByFace(self: DelegateFake,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceByFaceAndAttrib(self,hitPoint,faceNormal,id,name,surfaceClass):
  """ ExportCreateSurfaceByFaceAndAttrib(self: DelegateFake,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int,name: str,surfaceClass: str) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceObject(self,pSurfaceObject):
  """ ExportCreateSurfaceObject(self: DelegateFake,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportCreateSurfaceTreatment(self,pTreatment):
  """ ExportCreateSurfaceTreatment(self: DelegateFake,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportCreateTask(self,pTask):
  """ ExportCreateTask(self: DelegateFake,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportCreateTaskDependency(self,pTaskDependency):
  """ ExportCreateTaskDependency(self: DelegateFake,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportCreateTaskWorktype(self,pTaskWorktype):
  """ ExportCreateTaskWorktype(self: DelegateFake,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportCreateWeld(self,pWeld):
  """ ExportCreateWeld(self: DelegateFake,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportDasStartAction(self,ActionName,Parameter):
  """ ExportDasStartAction(self: DelegateFake,ActionName: str,Parameter: str) -> int """
  pass
 def ExportDasStartCommand(self,CommandName,Parameter):
  """ ExportDasStartCommand(self: DelegateFake,CommandName: str,Parameter: str) -> int """
  pass
 def ExportDeleteBasePoint(self,pBasePoint):
  """ ExportDeleteBasePoint(self: DelegateFake,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportDeleteClipPlane(self,pDotView,pDotClipPlane):
  """ ExportDeleteClipPlane(self: DelegateFake,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportDeleteConversionLink(self,pConversionLink):
  """ ExportDeleteConversionLink(self: DelegateFake,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportDeleteObject(self,pIdentifier):
  """ ExportDeleteObject(self: DelegateFake,pIdentifier: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportDisplayAutoDefaultSettings(self,pBaseComponent):
  """ ExportDisplayAutoDefaultSettings(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayComponentHelp(self,pBaseComponent):
  """ ExportDisplayComponentHelp(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayPrompt(self,Message):
  """ ExportDisplayPrompt(self: DelegateFake,Message: str) -> int """
  pass
 def ExportDisplayReport(self,FileName):
  """ ExportDisplayReport(self: DelegateFake,FileName: str) -> int """
  pass
 def ExportDoubleListHandler(self,pDoubleList):
  """ ExportDoubleListHandler(self: DelegateFake,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ExportDrawTemporaryPolygonSurface(self,pArgument):
  """ ExportDrawTemporaryPolygonSurface(self: DelegateFake,pArgument: dotDrawPolygonSurface_t) -> (int,dotDrawPolygonSurface_t) """
  pass
 def ExportDrawTemporaryPolyLine(self,pArgument):
  """ ExportDrawTemporaryPolyLine(self: DelegateFake,pArgument: dotDrawPolyLine_t) -> (int,dotDrawPolyLine_t) """
  pass
 def ExportDrawTemporaryPolyLineWithId(self,pArgument):
  """ ExportDrawTemporaryPolyLineWithId(self: DelegateFake,pArgument: dotGraphicPolyLine_t) -> (int,dotGraphicPolyLine_t) """
  pass
 def ExportDrawTemporaryText(self,pArgument):
  """ ExportDrawTemporaryText(self: DelegateFake,pArgument: dotDrawText_t) -> (int,dotDrawText_t) """
  pass
 def ExportEdgeListHandler(self,pEdgeList):
  """ ExportEdgeListHandler(self: DelegateFake,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ExportEnumerateObjects(self,pEnumerator):
  """ ExportEnumerateObjects(self: DelegateFake,pEnumerator: dotEnumerator_t) -> (int,dotEnumerator_t) """
  pass
 def ExportExtractBentPlateFromComponent(self,partId):
  """ ExportExtractBentPlateFromComponent(self: DelegateFake,partId: int) -> int """
  pass
 def ExportFingerprint(self,pInput,fingerprint):
  """ ExportFingerprint(self: DelegateFake,pInput: dotPolymesh_t,fingerprint: str) -> (int,dotPolymesh_t,str) """
  pass
 def ExportFormatProfile(self,profile):
  """ ExportFormatProfile(self: DelegateFake,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportGetAllProperties(self,pProperties,pNames,pValues):
  """ ExportGetAllProperties(self: DelegateFake,pProperties: dotGetProperties_t,pNames: List[object],pValues: List[object]) -> (int,dotGetProperties_t,List[object],List[object]) """
  pass
 def ExportGetAllReportProperties(self,pProperties):
  """ ExportGetAllReportProperties(self: DelegateFake,pProperties: List[dotGetProperties_t]) -> (int,List[dotGetProperties_t]) """
  pass
 def ExportGetAssociateSurfaces(self,id):
  """ ExportGetAssociateSurfaces(self: DelegateFake,id: int) -> List[int] """
  pass
 def ExportGetBasePoints(self,ClientId):
  """ ExportGetBasePoints(self: DelegateFake,ClientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportGetBentPlateMaximumRadius(self,geometryNodeId,clientId):
  """ ExportGetBentPlateMaximumRadius(self: DelegateFake,geometryNodeId: int,clientId: dotClientId_t) -> (float,dotClientId_t) """
  pass
 def ExportGetBentPlateMinimumRadius(self,partId):
  """ ExportGetBentPlateMinimumRadius(self: DelegateFake,partId: int) -> float """
  pass
 def ExportGetClipPlanes(self,pDotView,pDotGetClipPlanes):
  """ ExportGetClipPlanes(self: DelegateFake,pDotView: dotView_t,pDotGetClipPlanes: dotGetClipPlanes_t) -> (int,dotView_t,dotGetClipPlanes_t) """
  pass
 def ExportGetColorRepresentationForObject(self,pIdentifier,pColor):
  """ ExportGetColorRepresentationForObject(self: DelegateFake,pIdentifier: dotIdentifier_t,pColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportGetCommandStatus(self,TSCommand,TSCommandParam,Status):
  """ ExportGetCommandStatus(self: DelegateFake,TSCommand: str,TSCommandParam: str,Status: bool) -> (int,str,str,bool) """
  pass
 def ExportGetCommitData(self,pId,pObjectType,pObjectSubType,pCommitType):
  """ ExportGetCommitData(self: DelegateFake,pId: dotIdentifier_t,pObjectType: int,pObjectSubType: int,pCommitType: int) -> (int,dotIdentifier_t,int,int,int) """
  pass
 def ExportGetComponentAttribute(self,pIdentifier,pAttribute):
  """ ExportGetComponentAttribute(self: DelegateFake,pIdentifier: dotIdentifier_t,pAttribute: dotComponentAttribute_t) -> (int,dotIdentifier_t,dotComponentAttribute_t) """
  pass
 def ExportGetComponentInput(self,pObj):
  """ ExportGetComponentInput(self: DelegateFake,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportGetCoordinateSystem(self,pModelObject,pCoordinateSystem):
  """ ExportGetCoordinateSystem(self: DelegateFake,pModelObject: dotModelObject_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotModelObject_t,dotCoordinateSystem_t) """
  pass
 def ExportGetCoordinateSystemAccordingToBasePoint(self,id,pCoordSys):
  """ ExportGetCoordinateSystemAccordingToBasePoint(self: DelegateFake,id: int,pCoordSys: dotCoordinateSystem_t) -> (int,dotCoordinateSystem_t) """
  pass
 def ExportGetCutSolidSerialized(self,dotSolid1,dotSolid2,serializedFaceList,serializedVectorList,serializedFaceOriginPartIdList,serializedShellIndexList,serializedEdgeVertexList,serializedEdgeTypeList,serializedEdgeShellIndexList):
  """ ExportGetCutSolidSerialized(self: DelegateFake,dotSolid1: dotSolid_t,dotSolid2: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedFaceOriginPartIdList: List[int],serializedShellIndexList: List[int],serializedEdgeVertexList: List[dotPoint_t],serializedEdgeTypeList: List[int],serializedEdgeShellIndexList: List[int]) -> (int,dotSolid_t,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetDatabaseVersion(self,version):
  """ ExportGetDatabaseVersion(self: DelegateFake,version: int) -> (int,int) """
  pass
 def ExportGetDataBaseVersionInfoFromModel(self,pInfo):
  """ ExportGetDataBaseVersionInfoFromModel(self: DelegateFake,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetDetectedClash(self,pClash):
  """ ExportGetDetectedClash(self: DelegateFake,pClash: dotClash_t) -> (int,dotClash_t) """
  pass
 def ExportGetDotType(self,pModelObject):
  """ ExportGetDotType(self: DelegateFake,pModelObject: dotModelObject_t) -> (int,dotModelObject_t) """
  pass
 def ExportGetFatherComponent(self,ObjectId,FatherComponentId):
  """ ExportGetFatherComponent(self: DelegateFake,ObjectId: int,FatherComponentId: int) -> (int,int) """
  pass
 def ExportGetIntersectionBoundingBoxes(self,Identifier1,Identifier2,ClientId):
  """ ExportGetIntersectionBoundingBoxes(self: DelegateFake,Identifier1: dotIdentifier_t,Identifier2: dotIdentifier_t,ClientId: dotClientId_t) -> (int,dotIdentifier_t,dotIdentifier_t,dotClientId_t) """
  pass
 def ExportGetIntersectionPoints(self,pIntersectionPoints):
  """ ExportGetIntersectionPoints(self: DelegateFake,pIntersectionPoints: dotIntersectionPoints_t) -> (int,dotIntersectionPoints_t) """
  pass
 def ExportGetIntersectionSolid(self,pSolid):
  """ ExportGetIntersectionSolid(self: DelegateFake,pSolid: dotIntersectionSolid_t) -> (int,dotIntersectionSolid_t) """
  pass
 def ExportGetModificationStamp(self,pModStmp):
  """ ExportGetModificationStamp(self: DelegateFake,pModStmp: dotModificationStamp_t) -> (int,dotModificationStamp_t) """
  pass
 def ExportGetModificationStampGuid(self,pModStmp):
  """ ExportGetModificationStampGuid(self: DelegateFake,pModStmp: str) -> (int,str) """
  pass
 def ExportGetNumberingUpToDate(self,pNumberingQuery):
  """ ExportGetNumberingUpToDate(self: DelegateFake,pNumberingQuery: dotNumberingQuery_t) -> (int,dotNumberingQuery_t) """
  pass
 def ExportGetNumberOfClashes(self,pClashes):
  """ ExportGetNumberOfClashes(self: DelegateFake,pClashes: int) -> (int,int) """
  pass
 def ExportGetObjectLastModified(self,pIdentifier,pTime,pLocallyModified):
  """ ExportGetObjectLastModified(self: DelegateFake,pIdentifier: dotIdentifier_t,pTime: int,pLocallyModified: bool) -> (int,dotIdentifier_t,int,bool) """
  pass
 def ExportGetObjectPhase(self,pArgument):
  """ ExportGetObjectPhase(self: DelegateFake,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportGetParentObject(self,surfaceId):
  """ ExportGetParentObject(self: DelegateFake,surfaceId: int) -> int """
  pass
 def ExportGetPartLine(self,pPartLine):
  """ ExportGetPartLine(self: DelegateFake,pPartLine: dotPartLine_t) -> (int,dotPartLine_t) """
  pass
 def ExportGetPartMark(self,pPartMark):
  """ ExportGetPartMark(self: DelegateFake,pPartMark: dotPartMark_t) -> (int,dotPartMark_t) """
  pass
 def ExportGetPhaseNumbers(self,pArgument):
  """ ExportGetPhaseNumbers(self: DelegateFake,pArgument: dotPhaseNumbers_t) -> (int,dotPhaseNumbers_t) """
  pass
 def ExportGetPlane(self,pPlane):
  """ ExportGetPlane(self: DelegateFake,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportGetPolybeamCoordinateSystem(self,Id,SubId,Chamfered,pX,pY,pZ):
  """ ExportGetPolybeamCoordinateSystem(self: DelegateFake,Id: int,SubId: int,Chamfered: int,pX: dotPoint_t,pY: dotPoint_t,pZ: dotPoint_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t) """
  pass
 def ExportGetProjectInfo(self,pInfo):
  """ ExportGetProjectInfo(self: DelegateFake,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportGetProperties(self,pProperties):
  """ ExportGetProperties(self: DelegateFake,pProperties: dotGetProperties_t) -> (int,dotGetProperties_t) """
  pass
 def ExportGetReferenceModelObjectByExternalGuid(self,referenceModelId,externalGuid):
  """ ExportGetReferenceModelObjectByExternalGuid(self: DelegateFake,referenceModelId: int,externalGuid: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportGetReferenceModelRevisionIds(self,pReferenceModel,ClientId):
  """ ExportGetReferenceModelRevisionIds(self: DelegateFake,pReferenceModel: dotReferenceModel_t,ClientId: dotClientId_t) -> (int,dotReferenceModel_t,dotClientId_t) """
  pass
 def ExportGetSetModelInfo(self,pInfo):
  """ ExportGetSetModelInfo(self: DelegateFake,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetSetModstamp(self,ModStampData):
  """ ExportGetSetModstamp(self: DelegateFake,ModStampData: dotModStamp_t) -> (int,dotModStamp_t) """
  pass
 def ExportGetSnapshotFromDatabase(self,Enumerator,SelectInstances):
  """ ExportGetSnapshotFromDatabase(self: DelegateFake,Enumerator: dotEnumerator_t,SelectInstances: bool) -> (Serializable[List[ModelObject]],dotEnumerator_t) """
  pass
 def ExportGetSolid(self,pSolid):
  """ ExportGetSolid(self: DelegateFake,pSolid: dotSolid_t) -> (int,dotSolid_t) """
  pass
 def ExportGetSolidBrep(self,polymeshToClean,polymeshCleaned):
  """ ExportGetSolidBrep(self: DelegateFake,polymeshToClean: dotPolymesh_t,polymeshCleaned: dotPolymesh_t) -> (bool,dotPolymesh_t,dotPolymesh_t) """
  pass
 def ExportGetSolidMerged(self,dotSolid,polymeshes):
  """ ExportGetSolidMerged(self: DelegateFake,dotSolid: dotSolid_t,polymeshes: dotPolymesh_t) -> (int,dotSolid_t,dotPolymesh_t) """
  pass
 def ExportGetSolidSerialized(self,dotSolid,serializedFaceList,serializedVectorList,serializedShellIndexList,serializedFaceOriginIdList):
  """ ExportGetSolidSerialized(self: DelegateFake,dotSolid: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedShellIndexList: List[int],serializedFaceOriginIdList: List[int]) -> (int,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetStringPropertyFromDatabase(self,pProperty,stringValues):
  """ ExportGetStringPropertyFromDatabase(self: DelegateFake,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportGetSurfaceGeometryType(self,surfaceId):
  """ ExportGetSurfaceGeometryType(self: DelegateFake,surfaceId: int) -> int """
  pass
 def ExportGetTrackEvent(self,category,eventName,eventContent):
  """ ExportGetTrackEvent(self: DelegateFake,category: str,eventName: str,eventContent: str) -> (int,str,str,str) """
  pass
 def ExportGetTransformationPlane(self,pPlane):
  """ ExportGetTransformationPlane(self: DelegateFake,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportGetViewCamera(self,pDotView,pDotCamera):
  """ ExportGetViewCamera(self: DelegateFake,pDotView: dotView_t,pDotCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportGetViews(self,pViews):
  """ ExportGetViews(self: DelegateFake,pViews: dotViewSelector_t) -> (int,dotViewSelector_t) """
  pass
 def ExportGetWeldGeometry(self,pWeldGeometry):
  """ ExportGetWeldGeometry(self: DelegateFake,pWeldGeometry: dotWeldGeometry_t) -> (int,dotWeldGeometry_t) """
  pass
 def ExportGetWriteOutStampGuid(self,pModStmp):
  """ ExportGetWriteOutStampGuid(self: DelegateFake,pModStmp: str) -> (int,str) """
  pass
 def ExportHierarchicDefinition(self,pHierarchicDefinition):
  """ ExportHierarchicDefinition(self: DelegateFake,pHierarchicDefinition: dotHierarchicDefinition_t) -> (int,dotHierarchicDefinition_t) """
  pass
 def ExportHierarchicObject(self,pHierarchicObject):
  """ ExportHierarchicObject(self: DelegateFake,pHierarchicObject: dotHierarchicObject_t) -> (int,dotHierarchicObject_t) """
  pass
 def ExportHierarchicObjectChildrenOperation(self,pHierarchicList):
  """ ExportHierarchicObjectChildrenOperation(self: DelegateFake,pHierarchicList: dotHierarchicList_t) -> (int,dotHierarchicList_t) """
  pass
 def ExportInitializeComponentStacks(self):
  """ ExportInitializeComponentStacks(self: DelegateFake) -> int """
  pass
 def ExportInsertView(self,View):
  """ ExportInsertView(self: DelegateFake,View: dotView_t) -> (int,dotView_t) """
  pass
 def ExportIntListHandler(self,pIntList):
  """ ExportIntListHandler(self: DelegateFake,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ExportLoadComponentAttributes(self,pBaseComponent):
  """ ExportLoadComponentAttributes(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportManipulateObject(self,pArgument):
  """ ExportManipulateObject(self: DelegateFake,pArgument: dotManipulateObject_t) -> (int,dotManipulateObject_t) """
  pass
 def ExportModifyAssembly(self,pAssembly):
  """ ExportModifyAssembly(self: DelegateFake,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportModifyBasePoint(self,pBasePoint):
  """ ExportModifyBasePoint(self: DelegateFake,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportModifyBentPlate(self,pPart):
  """ ExportModifyBentPlate(self: DelegateFake,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportModifyBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportModifyBoltGroup(self: DelegateFake,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportModifyBooleanPart(self,pBooleanPart):
  """ ExportModifyBooleanPart(self: DelegateFake,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportModifyClipPlane(self,pDotView,pDotClipPlane):
  """ ExportModifyClipPlane(self: DelegateFake,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportModifyComponent(self,pBaseComponent):
  """ ExportModifyComponent(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportModifyControlPlane(self,pControlObject):
  """ ExportModifyControlPlane(self: DelegateFake,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportModifyCylindricalSurfaceNode(self,geometryNodeId,surfacePoints,clientId):
  """ ExportModifyCylindricalSurfaceNode(self: DelegateFake,geometryNodeId: int,surfacePoints: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyEdgeChamfer(self,pEdgeChamfer):
  """ ExportModifyEdgeChamfer(self: DelegateFake,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportModifyFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportModifyFittingOrCutPlane(self: DelegateFake,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeCurveType(self,geometryNodeId,newCurveType,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: DelegateFake,geometryNodeId: int,newCurveType: int,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeRadius(self,geometryNodeId,radius,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeRadius(self: DelegateFake,geometryNodeId: int,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreePolygonNode(self,geometryNodeId,contour,clientId):
  """ ExportModifyGeometryTreePolygonNode(self: DelegateFake,geometryNodeId: int,contour: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyGrid(self,pGrid):
  """ ExportModifyGrid(self: DelegateFake,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportModifyGridPlane(self,pGridPlane):
  """ ExportModifyGridPlane(self: DelegateFake,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportModifyLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportModifyLoad(self: DelegateFake,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportModifyLoadGroup(self,pLoadGroup):
  """ ExportModifyLoadGroup(self: DelegateFake,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportModifyPart(self,pPart,contour):
  """ ExportModifyPart(self: DelegateFake,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportModifyPourBreak(self,pPourBreak):
  """ ExportModifyPourBreak(self: DelegateFake,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportModifyPourObject(self,pPourObject):
  """ ExportModifyPourObject(self: DelegateFake,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportModifyProjectInfo(self,pInfo):
  """ ExportModifyProjectInfo(self: DelegateFake,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportModifyRebarEndDetailStrip(self,pStrip):
  """ ExportModifyRebarEndDetailStrip(self: DelegateFake,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportModifyRebarGroup(self,pRebarGroup):
  """ ExportModifyRebarGroup(self: DelegateFake,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportModifyRebarMesh(self,pRebarMesh):
  """ ExportModifyRebarMesh(self: DelegateFake,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportModifyRebarPropertyStrip(self,pStrip):
  """ ExportModifyRebarPropertyStrip(self: DelegateFake,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportModifyRebarSplice(self,pRebarSplice):
  """ ExportModifyRebarSplice(self: DelegateFake,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportModifyRebarSplitter(self,pStrip):
  """ ExportModifyRebarSplitter(self: DelegateFake,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportModifyRebarStrand(self,pRebarStrand):
  """ ExportModifyRebarStrand(self: DelegateFake,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportModifyReferenceModel(self,pReferenceModel):
  """ ExportModifyReferenceModel(self: DelegateFake,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportModifySingleRebar(self,pSingleRebar):
  """ ExportModifySingleRebar(self: DelegateFake,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportModifySurfaceObject(self,pSurfaceObject):
  """ ExportModifySurfaceObject(self: DelegateFake,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportModifySurfaceTreatment(self,pTreatment):
  """ ExportModifySurfaceTreatment(self: DelegateFake,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportModifyTask(self,pTask):
  """ ExportModifyTask(self: DelegateFake,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportModifyTaskDependency(self,pTaskDependency):
  """ ExportModifyTaskDependency(self: DelegateFake,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportModifyTaskWorktype(self,pTaskWorktype):
  """ ExportModifyTaskWorktype(self: DelegateFake,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportModifyView(self,View):
  """ ExportModifyView(self: DelegateFake,View: dotView_t) -> (int,dotView_t) """
  pass
 def ExportModifyWeld(self,pWeld):
  """ ExportModifyWeld(self: DelegateFake,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportModStampCompare(self,ModStampCompare):
  """ ExportModStampCompare(self: DelegateFake,ModStampCompare: dotModStampCompare_t) -> (int,dotModStampCompare_t) """
  pass
 def ExportObjectMatchesToFilter(self,pObjectId,FileName):
  """ ExportObjectMatchesToFilter(self: DelegateFake,pObjectId: dotIdentifier_t,FileName: str) -> (int,dotIdentifier_t) """
  pass
 def ExportParseProfile(self,profile):
  """ ExportParseProfile(self: DelegateFake,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportPointListHandler(self,pPointList):
  """ ExportPointListHandler(self: DelegateFake,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ExportProgressBarOperation(self,pProgressBar):
  """ ExportProgressBarOperation(self: DelegateFake,pProgressBar: dotProgressBar_t) -> (int,dotProgressBar_t) """
  pass
 def ExportRebarSetAdditionFunction(self,action,pRebarSet):
  """ ExportRebarSetAdditionFunction(self: DelegateFake,action: RebarSetAction,pRebarSet: dotRebarSetAddition_t) -> (int,dotRebarSetAddition_t) """
  pass
 def ExportRebarSetFunction(self,action,pRebarSet):
  """ ExportRebarSetFunction(self: DelegateFake,action: RebarSetAction,pRebarSet: dotRebarSet_t) -> (int,dotRebarSet_t) """
  pass
 def ExportRefreshReferenceFile(self,pReferenceModel):
  """ ExportRefreshReferenceFile(self: DelegateFake,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportRemoveFromPourUnit(self,clientId):
  """ ExportRemoveFromPourUnit(self: DelegateFake,clientId: dotClientId_t) -> (bool,dotClientId_t) """
  pass
 def ExportRemoveTemporaryGraphicsObjects(self,pArgument):
  """ ExportRemoveTemporaryGraphicsObjects(self: DelegateFake,pArgument: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportRunMacro(self,FileName):
  """ ExportRunMacro(self: DelegateFake,FileName: str) -> int """
  pass
 def ExportRunOrStopClashCheck(self,RunningClashCheck):
  """ ExportRunOrStopClashCheck(self: DelegateFake,RunningClashCheck: bool) -> int """
  pass
 def ExportSaveAsWebModel(self,pSaveAsWebModel):
  """ ExportSaveAsWebModel(self: DelegateFake,pSaveAsWebModel: dotSaveAsWebModel_t) -> (int,dotSaveAsWebModel_t) """
  pass
 def ExportSaveOperation(self,pOperation):
  """ ExportSaveOperation(self: DelegateFake,pOperation: dotSaveOperation_t) -> (int,dotSaveOperation_t) """
  pass
 def ExportSelectAssembly(self,pAssembly):
  """ ExportSelectAssembly(self: DelegateFake,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportSelectBasePoint(self,guid,pBasePoint):
  """ ExportSelectBasePoint(self: DelegateFake,guid: str,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportSelectBentPlate(self,pPart):
  """ ExportSelectBentPlate(self: DelegateFake,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportSelectBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportSelectBoltGroup(self: DelegateFake,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportSelectBooleanPart(self,pBooleanPart):
  """ ExportSelectBooleanPart(self: DelegateFake,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportSelectComponent(self,pBaseComponent):
  """ ExportSelectComponent(self: DelegateFake,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportSelectControlPlane(self,pControlObject):
  """ ExportSelectControlPlane(self: DelegateFake,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportSelectConversionLink(self,pConversionLink):
  """ ExportSelectConversionLink(self: DelegateFake,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportSelectEdgeChamfer(self,pEdgeChamfer):
  """ ExportSelectEdgeChamfer(self: DelegateFake,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportSelectFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportSelectFittingOrCutPlane(self: DelegateFake,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportSelectGrid(self,pGrid):
  """ ExportSelectGrid(self: DelegateFake,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportSelectGridPlane(self,pGridPlane):
  """ ExportSelectGridPlane(self: DelegateFake,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportSelectGuideline(self,pGuideline):
  """ ExportSelectGuideline(self: DelegateFake,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportSelectLegFace(self,pLegFace):
  """ ExportSelectLegFace(self: DelegateFake,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportSelectLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportSelectLoad(self: DelegateFake,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportSelectLoadGroup(self,pLoadGroup):
  """ ExportSelectLoadGroup(self: DelegateFake,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportSelectPart(self,pPart,contour):
  """ ExportSelectPart(self: DelegateFake,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportSelectPourBreak(self,pPourBreak):
  """ ExportSelectPourBreak(self: DelegateFake,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportSelectPourObject(self,pPourObject):
  """ ExportSelectPourObject(self: DelegateFake,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportSelectRebarBars(self,pWire):
  """ ExportSelectRebarBars(self: DelegateFake,pWire: dotWire_t) -> (int,dotWire_t) """
  pass
 def ExportSelectRebarEndDetailStrip(self,pStrip):
  """ ExportSelectRebarEndDetailStrip(self: DelegateFake,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportSelectRebarGroup(self,pRebarGroup):
  """ ExportSelectRebarGroup(self: DelegateFake,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportSelectRebarMesh(self,pRebarMesh):
  """ ExportSelectRebarMesh(self: DelegateFake,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportSelectRebarPropertyStrip(self,pStrip):
  """ ExportSelectRebarPropertyStrip(self: DelegateFake,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportSelectRebarSplice(self,pRebarSplice):
  """ ExportSelectRebarSplice(self: DelegateFake,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportSelectRebarSplitter(self,pStrip):
  """ ExportSelectRebarSplitter(self: DelegateFake,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportSelectRebarStrand(self,pRebarStrand):
  """ ExportSelectRebarStrand(self: DelegateFake,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportSelectReferenceModel(self,pReferenceModel):
  """ ExportSelectReferenceModel(self: DelegateFake,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportSelectReferenceModelObject(self,pReferenceModelObject):
  """ ExportSelectReferenceModelObject(self: DelegateFake,pReferenceModelObject: dotReferenceModelObject_t) -> (int,dotReferenceModelObject_t) """
  pass
 def ExportSelectReferenceModelRevision(self,modelId,revisionId,pRevision):
  """ ExportSelectReferenceModelRevision(self: DelegateFake,modelId: int,revisionId: int,pRevision: dotReferenceModelRevision_t) -> (int,dotReferenceModelRevision_t) """
  pass
 def ExportSelectSingleRebar(self,pSingleRebar):
  """ ExportSelectSingleRebar(self: DelegateFake,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportSelectSurfaceObject(self,pSurfaceObject):
  """ ExportSelectSurfaceObject(self: DelegateFake,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportSelectSurfaceTreatment(self,pTreatment):
  """ ExportSelectSurfaceTreatment(self: DelegateFake,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportSelectTask(self,pTask):
  """ ExportSelectTask(self: DelegateFake,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportSelectTaskDependency(self,pTaskDependency):
  """ ExportSelectTaskDependency(self: DelegateFake,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportSelectTaskWorktype(self,pTaskWorktype):
  """ ExportSelectTaskWorktype(self: DelegateFake,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportSelectView(self,pView):
  """ ExportSelectView(self: DelegateFake,pView: dotView_t) -> (int,dotView_t) """
  pass
 def ExportSelectWeld(self,pWeld):
  """ ExportSelectWeld(self: DelegateFake,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportSetAdvancedOption(self,pArgument):
  """ ExportSetAdvancedOption(self: DelegateFake,pArgument: dotGetAdvancedOption_t) -> (int,dotGetAdvancedOption_t) """
  pass
 def ExportSetAsCurrentRevision(self,modelId,revisionId):
  """ ExportSetAsCurrentRevision(self: DelegateFake,modelId: int,revisionId: int) -> int """
  pass
 def ExportSetComponentNameField(self,parentDialog,fieldName,fieldValue):
  """ ExportSetComponentNameField(self: DelegateFake,parentDialog: str,fieldName: str,fieldValue: str) -> int """
  pass
 def ExportSetGetPhaseProperty(self,pArgument):
  """ ExportSetGetPhaseProperty(self: DelegateFake,pArgument: dotSetGetProperty_t) -> (int,dotSetGetProperty_t) """
  pass
 def ExportSetObjectPhase(self,pArgument):
  """ ExportSetObjectPhase(self: DelegateFake,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportSetPlane(self,pPlane):
  """ ExportSetPlane(self: DelegateFake,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportSetProperty(self,pProperty):
  """ ExportSetProperty(self: DelegateFake,pProperty: dotSetProperty_t) -> (int,dotSetProperty_t) """
  pass
 def ExportSetRepresentation(self,Representation):
  """ ExportSetRepresentation(self: DelegateFake,Representation: str) -> int """
  pass
 def ExportSetStringPropertyToDatabase(self,pProperty,stringValues):
  """ ExportSetStringPropertyToDatabase(self: DelegateFake,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportSetTemporaryColor(self,pObjectId,pNewColor):
  """ ExportSetTemporaryColor(self: DelegateFake,pObjectId: dotIdentifier_t,pNewColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportSetTemporaryColors(self,pSetTemporaryColors):
  """ ExportSetTemporaryColors(self: DelegateFake,pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryColors_FAST(self,pObjects,pSetTemporaryColors):
  """ ExportSetTemporaryColors_FAST(self: DelegateFake,pObjects: List[Identifier],pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,List[Identifier],dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryState(self,pObjectId,pNewState):
  """ ExportSetTemporaryState(self: DelegateFake,pObjectId: dotIdentifier_t,pNewState: dotTemporaryStatesEnum) -> (int,dotIdentifier_t,dotTemporaryStatesEnum) """
  pass
 def ExportSetTemporaryStates(self,pSetTemporaryStates):
  """ ExportSetTemporaryStates(self: DelegateFake,pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,dotSetTemporaryStates_t) """
  pass
 def ExportSetTemporaryStates_FAST(self,pObjects,pSetTemporaryStates):
  """ ExportSetTemporaryStates_FAST(self: DelegateFake,pObjects: List[Identifier],pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,List[Identifier],dotSetTemporaryStates_t) """
  pass
 def ExportSetTransformationPlane(self,pPlane):
  """ ExportSetTransformationPlane(self: DelegateFake,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportSetViewCamera(self,pDotView,pDotCamera):
  """ ExportSetViewCamera(self: DelegateFake,pDotView: dotView_t,pDotCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportShadowArea(self,pArgument):
  """ ExportShadowArea(self: DelegateFake,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportShadowAreaComplement(self,pArgument):
  """ ExportShadowAreaComplement(self: DelegateFake,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportSharingOperation(self,pOperation):
  """ ExportSharingOperation(self: DelegateFake,pOperation: dotSharingOperation_t) -> (int,dotSharingOperation_t) """
  pass
 def ExportSingleRebarGetRebarSet(self,singleRebarId):
  """ ExportSingleRebarGetRebarSet(self: DelegateFake,singleRebarId: int) -> int """
  pass
 def ExportStartCustomComponentCreation(self,ComponentName):
  """ ExportStartCustomComponentCreation(self: DelegateFake,ComponentName: str) -> int """
  pass
 def ExportStartPluginCreation(self,ComponentName):
  """ ExportStartPluginCreation(self: DelegateFake,ComponentName: str) -> int """
  pass
 def ExportStringListHandler(self,pStringList):
  """ ExportStringListHandler(self: DelegateFake,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def ExportTaskObjectAttach(self,pSelector):
  """ ExportTaskObjectAttach(self: DelegateFake,pSelector: dotTaskObjectAttacher_t) -> (int,dotTaskObjectAttacher_t) """
  pass
 def ExportUIObjectPick(self,pPicker):
  """ ExportUIObjectPick(self: DelegateFake,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUIObjectSelect(self,pSelector):
  """ ExportUIObjectSelect(self: DelegateFake,pSelector: dotUIModelObjectSelector_t) -> (int,dotUIModelObjectSelector_t) """
  pass
 def ExportUIObjectsPick(self,pPicker):
  """ ExportUIObjectsPick(self: DelegateFake,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUndoOperation(self,pOperation):
  """ ExportUndoOperation(self: DelegateFake,pOperation: dotUndoOperation_t) -> (int,dotUndoOperation_t) """
  pass
 def ExportValidatePolymesh(self,checkCriteria,pPolymeshToValidate,invalidInfo):
  """ ExportValidatePolymesh(self: DelegateFake,checkCriteria: int,pPolymeshToValidate: dotPolymesh_t,invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool,dotPolymesh_t,dotPolymeshValidateInvalidInfo_t) """
  pass
 def ExportViewHideUnselected(self,HideCompletely,DrawAsStick):
  """ ExportViewHideUnselected(self: DelegateFake,HideCompletely: bool,DrawAsStick: bool) -> int """
  pass
 def ExportWriteToSessionLog(self,Message):
  """ ExportWriteToSessionLog(self: DelegateFake,Message: str) -> int """
  pass
 def GetDSTVCoordinateSystem(self,PartId,pCoordinateSystem):
  """ GetDSTVCoordinateSystem(self: DelegateFake,PartId: dotIdentifier_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotCoordinateSystem_t) """
  pass
 def ImportDoubleListHandler(self,pDoubleList):
  """ ImportDoubleListHandler(self: DelegateFake,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ImportEdgeListHandler(self,pEdgeList):
  """ ImportEdgeListHandler(self: DelegateFake,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ImportIntListHandler(self,pIntList):
  """ ImportIntListHandler(self: DelegateFake,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ImportPointListHandler(self,pPointList):
  """ ImportPointListHandler(self: DelegateFake,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ImportStringListHandler(self,pStringList):
  """ ImportStringListHandler(self: DelegateFake,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def IsMacroRecording(self):
  """ IsMacroRecording(self: DelegateFake) -> int """
  pass
 def IsMacroRunning(self):
  """ IsMacroRunning(self: DelegateFake) -> int """
  pass
 def RefreshMacroList(self):
  """ RefreshMacroList(self: DelegateFake) -> int """
  pass
 def StartMacroRecording(self,FileName):
  """ StartMacroRecording(self: DelegateFake,FileName: str) -> int """
  pass
 def StopMacroRecording(self):
  """ StopMacroRecording(self: DelegateFake) -> int """
  pass
