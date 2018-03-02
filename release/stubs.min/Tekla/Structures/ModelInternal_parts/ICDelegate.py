class ICDelegate:
 # no doc
 def ExplodeBentPlate(self,partId):
  """ ExplodeBentPlate(self: ICDelegate,partId: int) -> int """
  pass
 def ExportAddComponentAttributeToStack(self,pAttr):
  """ ExportAddComponentAttributeToStack(self: ICDelegate,pAttr: dotComponentAttribute_t) -> (int,dotComponentAttribute_t) """
  pass
 def ExportAddComponentInputToStack(self,pObj):
  """ ExportAddComponentInputToStack(self: ICDelegate,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportAddToPourUnit(self,inputPour,clientId):
  """ ExportAddToPourUnit(self: ICDelegate,inputPour: dotPourObject_t,clientId: dotClientId_t) -> (bool,dotPourObject_t,dotClientId_t) """
  pass
 def ExportCalculateContourPolygon(self,pContour,pPolygon):
  """ ExportCalculateContourPolygon(self: ICDelegate,pContour: dotContour_t,pPolygon: dotPolygon_t) -> (int,dotContour_t,dotPolygon_t) """
  pass
 def ExportCalculatePourUnits(self):
  """ ExportCalculatePourUnits(self: ICDelegate) -> bool """
  pass
 def ExportChangeManagerAllowNumbering(self,NumberingFlag):
  """ ExportChangeManagerAllowNumbering(self: ICDelegate,NumberingFlag: bool) -> int """
  pass
 def ExportChangeManagerAllowSave(self,SaveFlag):
  """ ExportChangeManagerAllowSave(self: ICDelegate,SaveFlag: bool) -> int """
  pass
 def ExportCleanDrawingFiles(self,Silent,BackupPath):
  """ ExportCleanDrawingFiles(self: ICDelegate,Silent: bool,BackupPath: str) -> int """
  pass
 def ExportClearAllTemporaryStates(self):
  """ ExportClearAllTemporaryStates(self: ICDelegate) -> int """
  pass
 def ExportClearTemporaryState(self,pObjectId):
  """ ExportClearTemporaryState(self: ICDelegate,pObjectId: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportCommitChanges(self,pModelCommit):
  """ ExportCommitChanges(self: ICDelegate,pModelCommit: dotModelCommit_t) -> (int,dotModelCommit_t) """
  pass
 def ExportCompareFingerprints(self,fingerprint1,fingerprint2):
  """ ExportCompareFingerprints(self: ICDelegate,fingerprint1: str,fingerprint2: str) -> bool """
  pass
 def ExportCompareObjects(self,ObjectId,ObjectToCompareId):
  """ ExportCompareObjects(self: ICDelegate,ObjectId: int,ObjectToCompareId: int) -> int """
  pass
 def ExportConnectGeometryTrees(self,clientId):
  """ ExportConnectGeometryTrees(self: ICDelegate,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPoints(self,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPoints(self: ICDelegate,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPointsWithRadius(self,radius,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPointsWithRadius(self: ICDelegate,radius: float,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesWithRadius(self,radius,clientId):
  """ ExportConnectGeometryTreesWithRadius(self: ICDelegate,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportCreateBasePoint(self,pBasePoint):
  """ ExportCreateBasePoint(self: ICDelegate,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportCreateBentPlateByFaces(self,part1Id,part2Id,face1,face2):
  """ ExportCreateBentPlateByFaces(self: ICDelegate,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByFacesAndRadius(self,part1Id,part2Id,face1,face2,radius):
  """ ExportCreateBentPlateByFacesAndRadius(self: ICDelegate,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t,radius: float) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByParts(self,part1Id,part2Id):
  """ ExportCreateBentPlateByParts(self: ICDelegate,part1Id: int,part2Id: int) -> int """
  pass
 def ExportCreateBentPlateByPartsAndRadius(self,part1Id,part2Id,radius):
  """ ExportCreateBentPlateByPartsAndRadius(self: ICDelegate,part1Id: int,part2Id: int,radius: float) -> int """
  pass
 def ExportCreateBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportCreateBoltGroup(self: ICDelegate,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportCreateBooleanPart(self,pBooleanPart):
  """ ExportCreateBooleanPart(self: ICDelegate,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportCreateClipPlane(self,pDotView,pDotClipPlane):
  """ ExportCreateClipPlane(self: ICDelegate,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportCreateComponent(self,pBaseComponent):
  """ ExportCreateComponent(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportCreateControlPlane(self,pControlObject):
  """ ExportCreateControlPlane(self: ICDelegate,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportCreateConversionLink(self,pConversionLink):
  """ ExportCreateConversionLink(self: ICDelegate,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportCreateEdgeChamfer(self,pEdgeChamfer):
  """ ExportCreateEdgeChamfer(self: ICDelegate,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportCreateFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportCreateFittingOrCutPlane(self: ICDelegate,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportCreateGrid(self,pGrid):
  """ ExportCreateGrid(self: ICDelegate,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportCreateGridPlane(self,pGridPlane):
  """ ExportCreateGridPlane(self: ICDelegate,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportCreateGuideline(self,pGuideline):
  """ ExportCreateGuideline(self: ICDelegate,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportCreateIFC(self,aIFC):
  """ ExportCreateIFC(self: ICDelegate,aIFC: dotCreateIFCFromModel_t) -> (int,dotCreateIFCFromModel_t) """
  pass
 def ExportCreateLegFace(self,pLegFace):
  """ ExportCreateLegFace(self: ICDelegate,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportCreateLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportCreateLoad(self: ICDelegate,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportCreateLoadGroup(self,pLoadGroup):
  """ ExportCreateLoadGroup(self: ICDelegate,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportCreateNC(self,aNC):
  """ ExportCreateNC(self: ICDelegate,aNC: dotCreateNCFromModel_t) -> (int,dotCreateNCFromModel_t) """
  pass
 def ExportCreateNewModel(self,pInfo):
  """ ExportCreateNewModel(self: ICDelegate,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportCreatePart(self,pPart,contour):
  """ ExportCreatePart(self: ICDelegate,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportCreatePourBreak(self,pPourBreak):
  """ ExportCreatePourBreak(self: ICDelegate,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportCreateRebarEndDetailStrip(self,pStrip):
  """ ExportCreateRebarEndDetailStrip(self: ICDelegate,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportCreateRebarGroup(self,pRebarGroup):
  """ ExportCreateRebarGroup(self: ICDelegate,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportCreateRebarMesh(self,pRebarMesh):
  """ ExportCreateRebarMesh(self: ICDelegate,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportCreateRebarPropertyStrip(self,pStrip):
  """ ExportCreateRebarPropertyStrip(self: ICDelegate,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportCreateRebarSplice(self,pRebarSplice):
  """ ExportCreateRebarSplice(self: ICDelegate,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportCreateRebarSplitter(self,pStrip):
  """ ExportCreateRebarSplitter(self: ICDelegate,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportCreateRebarStrand(self,pRebarStrand):
  """ ExportCreateRebarStrand(self: ICDelegate,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportCreateReferenceModel(self,pReferenceModel):
  """ ExportCreateReferenceModel(self: ICDelegate,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportCreateReferenceModelObjectAttribute(self,pRMOAttribute):
  """ ExportCreateReferenceModelObjectAttribute(self: ICDelegate,pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int,dotReferenceModelObjectAttribute_t) """
  pass
 def ExportCreateReferenceModelObjectAttributeEnumerator(self,pEnumerator):
  """ ExportCreateReferenceModelObjectAttributeEnumerator(self: ICDelegate,pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int,dotReferenceModelObjectAttributeEnumerator_t) """
  pass
 def ExportCreateReport(self,aReport):
  """ ExportCreateReport(self: ICDelegate,aReport: dotCreateReportFromModel_t) -> (int,dotCreateReportFromModel_t) """
  pass
 def ExportCreateSingleRebar(self,pSingleRebar):
  """ ExportCreateSingleRebar(self: ICDelegate,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportCreateSurfaceByFace(self,hitPoint,faceNormal,id):
  """ ExportCreateSurfaceByFace(self: ICDelegate,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceByFaceAndAttrib(self,hitPoint,faceNormal,id,name,surfaceClass):
  """ ExportCreateSurfaceByFaceAndAttrib(self: ICDelegate,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int,name: str,surfaceClass: str) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceObject(self,pSurfaceObject):
  """ ExportCreateSurfaceObject(self: ICDelegate,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportCreateSurfaceTreatment(self,pTreatment):
  """ ExportCreateSurfaceTreatment(self: ICDelegate,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportCreateTask(self,pTask):
  """ ExportCreateTask(self: ICDelegate,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportCreateTaskDependency(self,pTaskDependency):
  """ ExportCreateTaskDependency(self: ICDelegate,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportCreateTaskWorktype(self,pTaskWorktype):
  """ ExportCreateTaskWorktype(self: ICDelegate,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportCreateWeld(self,pWeld):
  """ ExportCreateWeld(self: ICDelegate,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportDasStartAction(self,ActionName,Parameter):
  """ ExportDasStartAction(self: ICDelegate,ActionName: str,Parameter: str) -> int """
  pass
 def ExportDasStartCommand(self,CommandName,Parameter):
  """ ExportDasStartCommand(self: ICDelegate,CommandName: str,Parameter: str) -> int """
  pass
 def ExportDeleteBasePoint(self,pBasePoint):
  """ ExportDeleteBasePoint(self: ICDelegate,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportDeleteClipPlane(self,pDotView,pDotClipPlane):
  """ ExportDeleteClipPlane(self: ICDelegate,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportDeleteConversionLink(self,pConversionLink):
  """ ExportDeleteConversionLink(self: ICDelegate,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportDeleteObject(self,pIdentifier):
  """ ExportDeleteObject(self: ICDelegate,pIdentifier: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportDisplayAutoDefaultSettings(self,pBaseComponent):
  """ ExportDisplayAutoDefaultSettings(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayComponentHelp(self,pBaseComponent):
  """ ExportDisplayComponentHelp(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayPrompt(self,Message):
  """ ExportDisplayPrompt(self: ICDelegate,Message: str) -> int """
  pass
 def ExportDisplayReport(self,FileName):
  """ ExportDisplayReport(self: ICDelegate,FileName: str) -> int """
  pass
 def ExportDoubleListHandler(self,pDoubleList):
  """ ExportDoubleListHandler(self: ICDelegate,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ExportDrawTemporaryPolygonSurface(self,pArgument):
  """ ExportDrawTemporaryPolygonSurface(self: ICDelegate,pArgument: dotDrawPolygonSurface_t) -> (int,dotDrawPolygonSurface_t) """
  pass
 def ExportDrawTemporaryPolyLine(self,pArgument):
  """ ExportDrawTemporaryPolyLine(self: ICDelegate,pArgument: dotDrawPolyLine_t) -> (int,dotDrawPolyLine_t) """
  pass
 def ExportDrawTemporaryPolyLineWithId(self,pArgument):
  """ ExportDrawTemporaryPolyLineWithId(self: ICDelegate,pArgument: dotGraphicPolyLine_t) -> (int,dotGraphicPolyLine_t) """
  pass
 def ExportDrawTemporaryText(self,pArgument):
  """ ExportDrawTemporaryText(self: ICDelegate,pArgument: dotDrawText_t) -> (int,dotDrawText_t) """
  pass
 def ExportEdgeListHandler(self,pEdgeList):
  """ ExportEdgeListHandler(self: ICDelegate,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ExportEnumerateObjects(self,pEnumerator):
  """ ExportEnumerateObjects(self: ICDelegate,pEnumerator: dotEnumerator_t) -> (int,dotEnumerator_t) """
  pass
 def ExportExtractBentPlateFromComponent(self,partId):
  """ ExportExtractBentPlateFromComponent(self: ICDelegate,partId: int) -> int """
  pass
 def ExportFingerprint(self,pInput,fingerprint):
  """ ExportFingerprint(self: ICDelegate,pInput: dotPolymesh_t,fingerprint: str) -> (int,dotPolymesh_t,str) """
  pass
 def ExportFormatProfile(self,profile):
  """ ExportFormatProfile(self: ICDelegate,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportGetAllProperties(self,pProperties,pNames,pValues):
  """ ExportGetAllProperties(self: ICDelegate,pProperties: dotGetProperties_t,pNames: List[object],pValues: List[object]) -> (int,dotGetProperties_t,List[object],List[object]) """
  pass
 def ExportGetAllReportProperties(self,pProperties):
  """ ExportGetAllReportProperties(self: ICDelegate,pProperties: List[dotGetProperties_t]) -> (int,List[dotGetProperties_t]) """
  pass
 def ExportGetAssociateSurfaces(self,id):
  """ ExportGetAssociateSurfaces(self: ICDelegate,id: int) -> List[int] """
  pass
 def ExportGetBasePoints(self,ClientId):
  """ ExportGetBasePoints(self: ICDelegate,ClientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportGetBentPlateMaximumRadius(self,geometryNodeId,clientId):
  """ ExportGetBentPlateMaximumRadius(self: ICDelegate,geometryNodeId: int,clientId: dotClientId_t) -> (float,dotClientId_t) """
  pass
 def ExportGetBentPlateMinimumRadius(self,partId):
  """ ExportGetBentPlateMinimumRadius(self: ICDelegate,partId: int) -> float """
  pass
 def ExportGetClipPlanes(self,pDotView,pDotGetClipPlanes):
  """ ExportGetClipPlanes(self: ICDelegate,pDotView: dotView_t,pDotGetClipPlanes: dotGetClipPlanes_t) -> (int,dotView_t,dotGetClipPlanes_t) """
  pass
 def ExportGetColorRepresentationForObject(self,pIdentifier,pColor):
  """ ExportGetColorRepresentationForObject(self: ICDelegate,pIdentifier: dotIdentifier_t,pColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportGetCommandStatus(self,TSCommand,TSCommandParam,Status):
  """ ExportGetCommandStatus(self: ICDelegate,TSCommand: str,TSCommandParam: str,Status: bool) -> (int,str,str,bool) """
  pass
 def ExportGetCommitData(self,pId,pObjectType,pObjectSubType,pCommitType):
  """ ExportGetCommitData(self: ICDelegate,pId: dotIdentifier_t,pObjectType: int,pObjectSubType: int,pCommitType: int) -> (int,dotIdentifier_t,int,int,int) """
  pass
 def ExportGetComponentAttribute(self,pIdentifier,pAttribute):
  """ ExportGetComponentAttribute(self: ICDelegate,pIdentifier: dotIdentifier_t,pAttribute: dotComponentAttribute_t) -> (int,dotIdentifier_t,dotComponentAttribute_t) """
  pass
 def ExportGetComponentInput(self,pObj):
  """ ExportGetComponentInput(self: ICDelegate,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportGetCoordinateSystem(self,pModelObject,pCoordinateSystem):
  """ ExportGetCoordinateSystem(self: ICDelegate,pModelObject: dotModelObject_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotModelObject_t,dotCoordinateSystem_t) """
  pass
 def ExportGetCutSolidSerialized(self,dotSolid1,dotSolid2,serializedFaceList,serializedVectorList,serializedFaceOriginPartIdList,serializedShellIndexList,serializedEdgeVertexList,serializedEdgeTypeList,serializedEdgeShellIndexList):
  """ ExportGetCutSolidSerialized(self: ICDelegate,dotSolid1: dotSolid_t,dotSolid2: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedFaceOriginPartIdList: List[int],serializedShellIndexList: List[int],serializedEdgeVertexList: List[dotPoint_t],serializedEdgeTypeList: List[int],serializedEdgeShellIndexList: List[int]) -> (int,dotSolid_t,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetDatabaseVersion(self,version):
  """ ExportGetDatabaseVersion(self: ICDelegate,version: int) -> (int,int) """
  pass
 def ExportGetDataBaseVersionInfoFromModel(self,pInfo):
  """ ExportGetDataBaseVersionInfoFromModel(self: ICDelegate,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetDetectedClash(self,pClash):
  """ ExportGetDetectedClash(self: ICDelegate,pClash: dotClash_t) -> (int,dotClash_t) """
  pass
 def ExportGetDotType(self,pModelObject):
  """ ExportGetDotType(self: ICDelegate,pModelObject: dotModelObject_t) -> (int,dotModelObject_t) """
  pass
 def ExportGetFatherComponent(self,ObjectId,FatherComponentId):
  """ ExportGetFatherComponent(self: ICDelegate,ObjectId: int,FatherComponentId: int) -> (int,int) """
  pass
 def ExportGetIntersectionBoundingBoxes(self,Identifier1,Identifier2,ClientId):
  """ ExportGetIntersectionBoundingBoxes(self: ICDelegate,Identifier1: dotIdentifier_t,Identifier2: dotIdentifier_t,ClientId: dotClientId_t) -> (int,dotIdentifier_t,dotIdentifier_t,dotClientId_t) """
  pass
 def ExportGetIntersectionPoints(self,pIntersectionPoints):
  """ ExportGetIntersectionPoints(self: ICDelegate,pIntersectionPoints: dotIntersectionPoints_t) -> (int,dotIntersectionPoints_t) """
  pass
 def ExportGetIntersectionSolid(self,pSolid):
  """ ExportGetIntersectionSolid(self: ICDelegate,pSolid: dotIntersectionSolid_t) -> (int,dotIntersectionSolid_t) """
  pass
 def ExportGetModificationStamp(self,pModStmp):
  """ ExportGetModificationStamp(self: ICDelegate,pModStmp: dotModificationStamp_t) -> (int,dotModificationStamp_t) """
  pass
 def ExportGetModificationStampGuid(self,pModStmp):
  """ ExportGetModificationStampGuid(self: ICDelegate,pModStmp: str) -> (int,str) """
  pass
 def ExportGetNumberingUpToDate(self,pNumberingQuery):
  """ ExportGetNumberingUpToDate(self: ICDelegate,pNumberingQuery: dotNumberingQuery_t) -> (int,dotNumberingQuery_t) """
  pass
 def ExportGetNumberOfClashes(self,pClashes):
  """ ExportGetNumberOfClashes(self: ICDelegate,pClashes: int) -> (int,int) """
  pass
 def ExportGetObjectLastModified(self,pIdentifier,pTime,pLocallyModified):
  """ ExportGetObjectLastModified(self: ICDelegate,pIdentifier: dotIdentifier_t,pTime: int,pLocallyModified: bool) -> (int,dotIdentifier_t,int,bool) """
  pass
 def ExportGetObjectPhase(self,pArgument):
  """ ExportGetObjectPhase(self: ICDelegate,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportGetParentObject(self,surfaceId):
  """ ExportGetParentObject(self: ICDelegate,surfaceId: int) -> int """
  pass
 def ExportGetPartLine(self,pPartLine):
  """ ExportGetPartLine(self: ICDelegate,pPartLine: dotPartLine_t) -> (int,dotPartLine_t) """
  pass
 def ExportGetPartMark(self,pPartMark):
  """ ExportGetPartMark(self: ICDelegate,pPartMark: dotPartMark_t) -> (int,dotPartMark_t) """
  pass
 def ExportGetPhaseNumbers(self,pArgument):
  """ ExportGetPhaseNumbers(self: ICDelegate,pArgument: dotPhaseNumbers_t) -> (int,dotPhaseNumbers_t) """
  pass
 def ExportGetPlane(self,pPlane):
  """ ExportGetPlane(self: ICDelegate,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportGetPolybeamCoordinateSystem(self,Id,SubId,Chamfered,pX,pY,pZ):
  """ ExportGetPolybeamCoordinateSystem(self: ICDelegate,Id: int,SubId: int,Chamfered: int,pX: dotPoint_t,pY: dotPoint_t,pZ: dotPoint_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t) """
  pass
 def ExportGetProjectInfo(self,pInfo):
  """ ExportGetProjectInfo(self: ICDelegate,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportGetProperties(self,pProperties):
  """ ExportGetProperties(self: ICDelegate,pProperties: dotGetProperties_t) -> (int,dotGetProperties_t) """
  pass
 def ExportGetReferenceModelObjectByExternalGuid(self,referenceModelId,externalGuid):
  """ ExportGetReferenceModelObjectByExternalGuid(self: ICDelegate,referenceModelId: int,externalGuid: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportGetReferenceModelRevisionIds(self,pReferenceModel,ClientId):
  """ ExportGetReferenceModelRevisionIds(self: ICDelegate,pReferenceModel: dotReferenceModel_t,ClientId: dotClientId_t) -> (int,dotReferenceModel_t,dotClientId_t) """
  pass
 def ExportGetSetModelInfo(self,pInfo):
  """ ExportGetSetModelInfo(self: ICDelegate,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetSetModstamp(self,ModStampData):
  """ ExportGetSetModstamp(self: ICDelegate,ModStampData: dotModStamp_t) -> (int,dotModStamp_t) """
  pass
 def ExportGetSnapshotFromDatabase(self,Enumerator,SelectInstances):
  """ ExportGetSnapshotFromDatabase(self: ICDelegate,Enumerator: dotEnumerator_t,SelectInstances: bool) -> (Serializable[List[ModelObject]],dotEnumerator_t) """
  pass
 def ExportGetSolid(self,pSolid):
  """ ExportGetSolid(self: ICDelegate,pSolid: dotSolid_t) -> (int,dotSolid_t) """
  pass
 def ExportGetSolidBrep(self,polymeshToClean,polymeshCleaned):
  """ ExportGetSolidBrep(self: ICDelegate,polymeshToClean: dotPolymesh_t,polymeshCleaned: dotPolymesh_t) -> (bool,dotPolymesh_t,dotPolymesh_t) """
  pass
 def ExportGetSolidMerged(self,dotSolid,polymeshes):
  """ ExportGetSolidMerged(self: ICDelegate,dotSolid: dotSolid_t,polymeshes: dotPolymesh_t) -> (int,dotSolid_t,dotPolymesh_t) """
  pass
 def ExportGetSolidSerialized(self,dotSolid,serializedFaceList,serializedVectorList,serializedShellIndexList,serializedFaceOriginIdList):
  """ ExportGetSolidSerialized(self: ICDelegate,dotSolid: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedShellIndexList: List[int],serializedFaceOriginIdList: List[int]) -> (int,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetStringPropertyFromDatabase(self,pProperty,stringValues):
  """ ExportGetStringPropertyFromDatabase(self: ICDelegate,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportGetSurfaceGeometryType(self,surfaceId):
  """ ExportGetSurfaceGeometryType(self: ICDelegate,surfaceId: int) -> int """
  pass
 def ExportGetTrackEvent(self,category,eventName,eventContent):
  """ ExportGetTrackEvent(self: ICDelegate,category: str,eventName: str,eventContent: str) -> (int,str,str,str) """
  pass
 def ExportGetTransformationPlane(self,pPlane):
  """ ExportGetTransformationPlane(self: ICDelegate,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportGetViewCamera(self,pDotView,pDotCamera):
  """ ExportGetViewCamera(self: ICDelegate,pDotView: dotView_t,pDotCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportGetViews(self,pViews):
  """ ExportGetViews(self: ICDelegate,pViews: dotViewSelector_t) -> (int,dotViewSelector_t) """
  pass
 def ExportGetWeldGeometry(self,pWeldGeometry):
  """ ExportGetWeldGeometry(self: ICDelegate,pWeldGeometry: dotWeldGeometry_t) -> (int,dotWeldGeometry_t) """
  pass
 def ExportGetWriteOutStampGuid(self,pModStmp):
  """ ExportGetWriteOutStampGuid(self: ICDelegate,pModStmp: str) -> (int,str) """
  pass
 def ExportHierarchicDefinition(self,pHierarchicDefinition):
  """ ExportHierarchicDefinition(self: ICDelegate,pHierarchicDefinition: dotHierarchicDefinition_t) -> (int,dotHierarchicDefinition_t) """
  pass
 def ExportHierarchicObject(self,pHierarchicObject):
  """ ExportHierarchicObject(self: ICDelegate,pHierarchicObject: dotHierarchicObject_t) -> (int,dotHierarchicObject_t) """
  pass
 def ExportHierarchicObjectChildrenOperation(self,pHierarchicList):
  """ ExportHierarchicObjectChildrenOperation(self: ICDelegate,pHierarchicList: dotHierarchicList_t) -> (int,dotHierarchicList_t) """
  pass
 def ExportInitializeComponentStacks(self):
  """ ExportInitializeComponentStacks(self: ICDelegate) -> int """
  pass
 def ExportInsertView(self,View):
  """ ExportInsertView(self: ICDelegate,View: dotView_t) -> (int,dotView_t) """
  pass
 def ExportIntListHandler(self,pIntList):
  """ ExportIntListHandler(self: ICDelegate,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ExportLoadComponentAttributes(self,pBaseComponent):
  """ ExportLoadComponentAttributes(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportManipulateObject(self,pArgument):
  """ ExportManipulateObject(self: ICDelegate,pArgument: dotManipulateObject_t) -> (int,dotManipulateObject_t) """
  pass
 def ExportModifyAssembly(self,pAssembly):
  """ ExportModifyAssembly(self: ICDelegate,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportModifyBasePoint(self,pBasePoint):
  """ ExportModifyBasePoint(self: ICDelegate,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportModifyBentPlate(self,pPart):
  """ ExportModifyBentPlate(self: ICDelegate,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportModifyBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportModifyBoltGroup(self: ICDelegate,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportModifyBooleanPart(self,pBooleanPart):
  """ ExportModifyBooleanPart(self: ICDelegate,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportModifyClipPlane(self,pDotView,pDotClipPlane):
  """ ExportModifyClipPlane(self: ICDelegate,pDotView: dotView_t,pDotClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportModifyComponent(self,pBaseComponent):
  """ ExportModifyComponent(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportModifyControlPlane(self,pControlObject):
  """ ExportModifyControlPlane(self: ICDelegate,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportModifyCylindricalSurfaceNode(self,geometryNodeId,surfacePoints,clientId):
  """ ExportModifyCylindricalSurfaceNode(self: ICDelegate,geometryNodeId: int,surfacePoints: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyEdgeChamfer(self,pEdgeChamfer):
  """ ExportModifyEdgeChamfer(self: ICDelegate,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportModifyFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportModifyFittingOrCutPlane(self: ICDelegate,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeCurveType(self,geometryNodeId,newCurveType,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: ICDelegate,geometryNodeId: int,newCurveType: int,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeRadius(self,geometryNodeId,radius,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeRadius(self: ICDelegate,geometryNodeId: int,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreePolygonNode(self,geometryNodeId,contour,clientId):
  """ ExportModifyGeometryTreePolygonNode(self: ICDelegate,geometryNodeId: int,contour: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyGrid(self,pGrid):
  """ ExportModifyGrid(self: ICDelegate,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportModifyGridPlane(self,pGridPlane):
  """ ExportModifyGridPlane(self: ICDelegate,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportModifyLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportModifyLoad(self: ICDelegate,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportModifyLoadGroup(self,pLoadGroup):
  """ ExportModifyLoadGroup(self: ICDelegate,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportModifyPart(self,pPart,contour):
  """ ExportModifyPart(self: ICDelegate,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportModifyPourBreak(self,pPourBreak):
  """ ExportModifyPourBreak(self: ICDelegate,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportModifyPourObject(self,pPourObject):
  """ ExportModifyPourObject(self: ICDelegate,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportModifyProjectInfo(self,pInfo):
  """ ExportModifyProjectInfo(self: ICDelegate,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportModifyRebarEndDetailStrip(self,pStrip):
  """ ExportModifyRebarEndDetailStrip(self: ICDelegate,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportModifyRebarGroup(self,pRebarGroup):
  """ ExportModifyRebarGroup(self: ICDelegate,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportModifyRebarMesh(self,pRebarMesh):
  """ ExportModifyRebarMesh(self: ICDelegate,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportModifyRebarPropertyStrip(self,pStrip):
  """ ExportModifyRebarPropertyStrip(self: ICDelegate,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportModifyRebarSplice(self,pRebarSplice):
  """ ExportModifyRebarSplice(self: ICDelegate,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportModifyRebarSplitter(self,pStrip):
  """ ExportModifyRebarSplitter(self: ICDelegate,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportModifyRebarStrand(self,pRebarStrand):
  """ ExportModifyRebarStrand(self: ICDelegate,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportModifyReferenceModel(self,pReferenceModel):
  """ ExportModifyReferenceModel(self: ICDelegate,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportModifySingleRebar(self,pSingleRebar):
  """ ExportModifySingleRebar(self: ICDelegate,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportModifySurfaceObject(self,pSurfaceObject):
  """ ExportModifySurfaceObject(self: ICDelegate,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportModifySurfaceTreatment(self,pTreatment):
  """ ExportModifySurfaceTreatment(self: ICDelegate,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportModifyTask(self,pTask):
  """ ExportModifyTask(self: ICDelegate,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportModifyTaskDependency(self,pTaskDependency):
  """ ExportModifyTaskDependency(self: ICDelegate,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportModifyTaskWorktype(self,pTaskWorktype):
  """ ExportModifyTaskWorktype(self: ICDelegate,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportModifyView(self,View):
  """ ExportModifyView(self: ICDelegate,View: dotView_t) -> (int,dotView_t) """
  pass
 def ExportModifyWeld(self,pWeld):
  """ ExportModifyWeld(self: ICDelegate,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportModStampCompare(self,ModStampCompare):
  """ ExportModStampCompare(self: ICDelegate,ModStampCompare: dotModStampCompare_t) -> (int,dotModStampCompare_t) """
  pass
 def ExportObjectMatchesToFilter(self,pObjectId,FileName):
  """ ExportObjectMatchesToFilter(self: ICDelegate,pObjectId: dotIdentifier_t,FileName: str) -> (int,dotIdentifier_t) """
  pass
 def ExportParseProfile(self,profile):
  """ ExportParseProfile(self: ICDelegate,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportPointListHandler(self,pPointList):
  """ ExportPointListHandler(self: ICDelegate,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ExportProgressBarOperation(self,pProgressBar):
  """ ExportProgressBarOperation(self: ICDelegate,pProgressBar: dotProgressBar_t) -> (int,dotProgressBar_t) """
  pass
 def ExportRebarSetAdditionFunction(self,action,pRebarSet):
  """ ExportRebarSetAdditionFunction(self: ICDelegate,action: RebarSetAction,pRebarSet: dotRebarSetAddition_t) -> (int,dotRebarSetAddition_t) """
  pass
 def ExportRebarSetFunction(self,action,pRebarSet):
  """ ExportRebarSetFunction(self: ICDelegate,action: RebarSetAction,pRebarSet: dotRebarSet_t) -> (int,dotRebarSet_t) """
  pass
 def ExportRefreshReferenceFile(self,pReferenceModel):
  """ ExportRefreshReferenceFile(self: ICDelegate,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportRemoveFromPourUnit(self,clientId):
  """ ExportRemoveFromPourUnit(self: ICDelegate,clientId: dotClientId_t) -> (bool,dotClientId_t) """
  pass
 def ExportRemoveTemporaryGraphicsObjects(self,pArgument):
  """ ExportRemoveTemporaryGraphicsObjects(self: ICDelegate,pArgument: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportRunMacro(self,FileName):
  """ ExportRunMacro(self: ICDelegate,FileName: str) -> int """
  pass
 def ExportRunOrStopClashCheck(self,RunningClashCheck):
  """ ExportRunOrStopClashCheck(self: ICDelegate,RunningClashCheck: bool) -> int """
  pass
 def ExportSaveAsWebModel(self,pSaveAsWebModel):
  """ ExportSaveAsWebModel(self: ICDelegate,pSaveAsWebModel: dotSaveAsWebModel_t) -> (int,dotSaveAsWebModel_t) """
  pass
 def ExportSaveOperation(self,pOperation):
  """ ExportSaveOperation(self: ICDelegate,pOperation: dotSaveOperation_t) -> (int,dotSaveOperation_t) """
  pass
 def ExportSelectAssembly(self,pAssembly):
  """ ExportSelectAssembly(self: ICDelegate,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportSelectBasePoint(self,guid,pBasePoint):
  """ ExportSelectBasePoint(self: ICDelegate,guid: str,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportSelectBentPlate(self,pPart):
  """ ExportSelectBentPlate(self: ICDelegate,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportSelectBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportSelectBoltGroup(self: ICDelegate,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportSelectBooleanPart(self,pBooleanPart):
  """ ExportSelectBooleanPart(self: ICDelegate,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportSelectComponent(self,pBaseComponent):
  """ ExportSelectComponent(self: ICDelegate,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportSelectControlPlane(self,pControlObject):
  """ ExportSelectControlPlane(self: ICDelegate,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportSelectConversionLink(self,pConversionLink):
  """ ExportSelectConversionLink(self: ICDelegate,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportSelectEdgeChamfer(self,pEdgeChamfer):
  """ ExportSelectEdgeChamfer(self: ICDelegate,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportSelectFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportSelectFittingOrCutPlane(self: ICDelegate,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportSelectGrid(self,pGrid):
  """ ExportSelectGrid(self: ICDelegate,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportSelectGridPlane(self,pGridPlane):
  """ ExportSelectGridPlane(self: ICDelegate,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportSelectGuideline(self,pGuideline):
  """ ExportSelectGuideline(self: ICDelegate,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportSelectLegFace(self,pLegFace):
  """ ExportSelectLegFace(self: ICDelegate,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportSelectLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportSelectLoad(self: ICDelegate,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportSelectLoadGroup(self,pLoadGroup):
  """ ExportSelectLoadGroup(self: ICDelegate,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportSelectPart(self,pPart,contour):
  """ ExportSelectPart(self: ICDelegate,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportSelectPourBreak(self,pPourBreak):
  """ ExportSelectPourBreak(self: ICDelegate,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportSelectPourObject(self,pPourObject):
  """ ExportSelectPourObject(self: ICDelegate,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportSelectRebarBars(self,pWire):
  """ ExportSelectRebarBars(self: ICDelegate,pWire: dotWire_t) -> (int,dotWire_t) """
  pass
 def ExportSelectRebarEndDetailStrip(self,pStrip):
  """ ExportSelectRebarEndDetailStrip(self: ICDelegate,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportSelectRebarGroup(self,pRebarGroup):
  """ ExportSelectRebarGroup(self: ICDelegate,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportSelectRebarMesh(self,pRebarMesh):
  """ ExportSelectRebarMesh(self: ICDelegate,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportSelectRebarPropertyStrip(self,pStrip):
  """ ExportSelectRebarPropertyStrip(self: ICDelegate,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportSelectRebarSplice(self,pRebarSplice):
  """ ExportSelectRebarSplice(self: ICDelegate,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportSelectRebarSplitter(self,pStrip):
  """ ExportSelectRebarSplitter(self: ICDelegate,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportSelectRebarStrand(self,pRebarStrand):
  """ ExportSelectRebarStrand(self: ICDelegate,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportSelectReferenceModel(self,pReferenceModel):
  """ ExportSelectReferenceModel(self: ICDelegate,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportSelectReferenceModelObject(self,pReferenceModelObject):
  """ ExportSelectReferenceModelObject(self: ICDelegate,pReferenceModelObject: dotReferenceModelObject_t) -> (int,dotReferenceModelObject_t) """
  pass
 def ExportSelectReferenceModelRevision(self,modelId,revisionId,pRevision):
  """ ExportSelectReferenceModelRevision(self: ICDelegate,modelId: int,revisionId: int,pRevision: dotReferenceModelRevision_t) -> (int,dotReferenceModelRevision_t) """
  pass
 def ExportSelectSingleRebar(self,pSingleRebar):
  """ ExportSelectSingleRebar(self: ICDelegate,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportSelectSurfaceObject(self,pSurfaceObject):
  """ ExportSelectSurfaceObject(self: ICDelegate,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportSelectSurfaceTreatment(self,pTreatment):
  """ ExportSelectSurfaceTreatment(self: ICDelegate,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportSelectTask(self,pTask):
  """ ExportSelectTask(self: ICDelegate,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportSelectTaskDependency(self,pTaskDependency):
  """ ExportSelectTaskDependency(self: ICDelegate,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportSelectTaskWorktype(self,pTaskWorktype):
  """ ExportSelectTaskWorktype(self: ICDelegate,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportSelectView(self,pView):
  """ ExportSelectView(self: ICDelegate,pView: dotView_t) -> (int,dotView_t) """
  pass
 def ExportSelectWeld(self,pWeld):
  """ ExportSelectWeld(self: ICDelegate,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportSetAdvancedOption(self,pArgument):
  """ ExportSetAdvancedOption(self: ICDelegate,pArgument: dotGetAdvancedOption_t) -> (int,dotGetAdvancedOption_t) """
  pass
 def ExportSetAsCurrentRevision(self,modelId,revisionId):
  """ ExportSetAsCurrentRevision(self: ICDelegate,modelId: int,revisionId: int) -> int """
  pass
 def ExportSetGetPhaseProperty(self,pArgument):
  """ ExportSetGetPhaseProperty(self: ICDelegate,pArgument: dotSetGetProperty_t) -> (int,dotSetGetProperty_t) """
  pass
 def ExportSetObjectPhase(self,pArgument):
  """ ExportSetObjectPhase(self: ICDelegate,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportSetPlane(self,pPlane):
  """ ExportSetPlane(self: ICDelegate,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportSetProperty(self,pProperty):
  """ ExportSetProperty(self: ICDelegate,pProperty: dotSetProperty_t) -> (int,dotSetProperty_t) """
  pass
 def ExportSetRepresentation(self,Representation):
  """ ExportSetRepresentation(self: ICDelegate,Representation: str) -> int """
  pass
 def ExportSetStringPropertyToDatabase(self,pProperty,stringValues):
  """ ExportSetStringPropertyToDatabase(self: ICDelegate,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportSetTemporaryColor(self,pObjectId,pNewColor):
  """ ExportSetTemporaryColor(self: ICDelegate,pObjectId: dotIdentifier_t,pNewColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportSetTemporaryColors(self,pSetTemporaryColors):
  """ ExportSetTemporaryColors(self: ICDelegate,pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryColors_FAST(self,pObjects,pSetTemporaryColors):
  """ ExportSetTemporaryColors_FAST(self: ICDelegate,pObjects: List[Identifier],pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,List[Identifier],dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryState(self,pObjectId,pNewState):
  """ ExportSetTemporaryState(self: ICDelegate,pObjectId: dotIdentifier_t,pNewState: dotTemporaryStatesEnum) -> (int,dotIdentifier_t,dotTemporaryStatesEnum) """
  pass
 def ExportSetTemporaryStates(self,pSetTemporaryStates):
  """ ExportSetTemporaryStates(self: ICDelegate,pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,dotSetTemporaryStates_t) """
  pass
 def ExportSetTemporaryStates_FAST(self,pObjects,pSetTemporaryStates):
  """ ExportSetTemporaryStates_FAST(self: ICDelegate,pObjects: List[Identifier],pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,List[Identifier],dotSetTemporaryStates_t) """
  pass
 def ExportSetTransformationPlane(self,pPlane):
  """ ExportSetTransformationPlane(self: ICDelegate,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportSetViewCamera(self,pDotView,pDotCamera):
  """ ExportSetViewCamera(self: ICDelegate,pDotView: dotView_t,pDotCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportShadowArea(self,pArgument):
  """ ExportShadowArea(self: ICDelegate,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportShadowAreaComplement(self,pArgument):
  """ ExportShadowAreaComplement(self: ICDelegate,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportSharingOperation(self,pOperation):
  """ ExportSharingOperation(self: ICDelegate,pOperation: dotSharingOperation_t) -> (int,dotSharingOperation_t) """
  pass
 def ExportSingleRebarGetRebarSet(self,singleRebarId):
  """ ExportSingleRebarGetRebarSet(self: ICDelegate,singleRebarId: int) -> int """
  pass
 def ExportStartCustomComponentCreation(self,ComponentName):
  """ ExportStartCustomComponentCreation(self: ICDelegate,ComponentName: str) -> int """
  pass
 def ExportStartPluginCreation(self,ComponentName):
  """ ExportStartPluginCreation(self: ICDelegate,ComponentName: str) -> int """
  pass
 def ExportStringListHandler(self,pStringList):
  """ ExportStringListHandler(self: ICDelegate,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def ExportTaskObjectAttach(self,pSelector):
  """ ExportTaskObjectAttach(self: ICDelegate,pSelector: dotTaskObjectAttacher_t) -> (int,dotTaskObjectAttacher_t) """
  pass
 def ExportUIObjectPick(self,pPicker):
  """ ExportUIObjectPick(self: ICDelegate,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUIObjectSelect(self,pSelector):
  """ ExportUIObjectSelect(self: ICDelegate,pSelector: dotUIModelObjectSelector_t) -> (int,dotUIModelObjectSelector_t) """
  pass
 def ExportUIObjectsPick(self,pPicker):
  """ ExportUIObjectsPick(self: ICDelegate,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUndoOperation(self,pOperation):
  """ ExportUndoOperation(self: ICDelegate,pOperation: dotUndoOperation_t) -> (int,dotUndoOperation_t) """
  pass
 def ExportValidatePolymesh(self,checkCriteria,polymeshToValidate,invalidInfo):
  """ ExportValidatePolymesh(self: ICDelegate,checkCriteria: int,polymeshToValidate: dotPolymesh_t,invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool,dotPolymesh_t,dotPolymeshValidateInvalidInfo_t) """
  pass
 def ExportViewHideUnselected(self,HideCompletely,DrawAsStick):
  """ ExportViewHideUnselected(self: ICDelegate,HideCompletely: bool,DrawAsStick: bool) -> int """
  pass
 def ExportWriteToSessionLog(self,Message):
  """ ExportWriteToSessionLog(self: ICDelegate,Message: str) -> int """
  pass
 def GetDSTVCoordinateSystem(self,PartId,pCoordinateSystem):
  """ GetDSTVCoordinateSystem(self: ICDelegate,PartId: dotIdentifier_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotCoordinateSystem_t) """
  pass
 def ImportDoubleListHandler(self,pDoubleList):
  """ ImportDoubleListHandler(self: ICDelegate,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ImportEdgeListHandler(self,pEdgeList):
  """ ImportEdgeListHandler(self: ICDelegate,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ImportIntListHandler(self,pIntList):
  """ ImportIntListHandler(self: ICDelegate,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ImportPointListHandler(self,pPointList):
  """ ImportPointListHandler(self: ICDelegate,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ImportStringListHandler(self,pStringList):
  """ ImportStringListHandler(self: ICDelegate,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def IsMacroRunning(self):
  """ IsMacroRunning(self: ICDelegate) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
