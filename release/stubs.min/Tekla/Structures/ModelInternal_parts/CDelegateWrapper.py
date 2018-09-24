class CDelegateWrapper(MarshalByRefObject):
 """ CDelegateWrapper(instance: ICDelegate,functionality: WrapperFunctionalityBase) """
 def ExplodeBentPlate(self,partId):
  """ ExplodeBentPlate(self: CDelegateWrapper,partId: int) -> int """
  pass
 def ExportAddComponentAttributeToStack(self,pAttr):
  """ ExportAddComponentAttributeToStack(self: CDelegateWrapper,pAttr: dotComponentAttribute_t) -> (int,dotComponentAttribute_t) """
  pass
 def ExportAddComponentInputToStack(self,pObj):
  """ ExportAddComponentInputToStack(self: CDelegateWrapper,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportAddToPourUnit(self,inputPour,clientId):
  """ ExportAddToPourUnit(self: CDelegateWrapper,inputPour: dotPourObject_t,clientId: dotClientId_t) -> (bool,dotPourObject_t,dotClientId_t) """
  pass
 def ExportCalculateContourPolygon(self,pContour,pPolygon):
  """ ExportCalculateContourPolygon(self: CDelegateWrapper,pContour: dotContour_t,pPolygon: dotPolygon_t) -> (int,dotContour_t,dotPolygon_t) """
  pass
 def ExportCalculatePourUnits(self):
  """ ExportCalculatePourUnits(self: CDelegateWrapper) -> bool """
  pass
 def ExportChangeManagerAllowNumbering(self,NumberingFlag):
  """ ExportChangeManagerAllowNumbering(self: CDelegateWrapper,NumberingFlag: bool) -> int """
  pass
 def ExportChangeManagerAllowSave(self,SaveFlag):
  """ ExportChangeManagerAllowSave(self: CDelegateWrapper,SaveFlag: bool) -> int """
  pass
 def ExportCleanDrawingFiles(self,Silent,BackupPath):
  """ ExportCleanDrawingFiles(self: CDelegateWrapper,Silent: bool,BackupPath: str) -> int """
  pass
 def ExportClearAllTemporaryStates(self):
  """ ExportClearAllTemporaryStates(self: CDelegateWrapper) -> int """
  pass
 def ExportClearTemporaryState(self,pObjectId):
  """ ExportClearTemporaryState(self: CDelegateWrapper,pObjectId: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportCommitChanges(self,pModelCommit):
  """ ExportCommitChanges(self: CDelegateWrapper,pModelCommit: dotModelCommit_t) -> (int,dotModelCommit_t) """
  pass
 def ExportCompareFingerprints(self,fingerprint1,fingerprint2):
  """ ExportCompareFingerprints(self: CDelegateWrapper,fingerprint1: str,fingerprint2: str) -> bool """
  pass
 def ExportCompareObjects(self,ObjectId,ObjectToCompareId):
  """ ExportCompareObjects(self: CDelegateWrapper,ObjectId: int,ObjectToCompareId: int) -> int """
  pass
 def ExportConnectGeometryTrees(self,clientId):
  """ ExportConnectGeometryTrees(self: CDelegateWrapper,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPoints(self,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPoints(self: CDelegateWrapper,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesByPointsWithRadius(self,radius,side1Start,side1End,side2Start,side2End,clientId):
  """ ExportConnectGeometryTreesByPointsWithRadius(self: CDelegateWrapper,radius: float,side1Start: dotPoint_t,side1End: dotPoint_t,side2Start: dotPoint_t,side2End: dotPoint_t,clientId: dotClientId_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t,dotPoint_t,dotClientId_t) """
  pass
 def ExportConnectGeometryTreesWithRadius(self,radius,clientId):
  """ ExportConnectGeometryTreesWithRadius(self: CDelegateWrapper,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportCreateBasePoint(self,pBasePoint):
  """ ExportCreateBasePoint(self: CDelegateWrapper,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportCreateBentPlateByFaces(self,part1Id,part2Id,face1,face2):
  """ ExportCreateBentPlateByFaces(self: CDelegateWrapper,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByFacesAndRadius(self,part1Id,part2Id,face1,face2,radius):
  """ ExportCreateBentPlateByFacesAndRadius(self: CDelegateWrapper,part1Id: int,part2Id: int,face1: dotPolygon_t,face2: dotPolygon_t,radius: float) -> (int,dotPolygon_t,dotPolygon_t) """
  pass
 def ExportCreateBentPlateByParts(self,part1Id,part2Id):
  """ ExportCreateBentPlateByParts(self: CDelegateWrapper,part1Id: int,part2Id: int) -> int """
  pass
 def ExportCreateBentPlateByPartsAndRadius(self,part1Id,part2Id,radius):
  """ ExportCreateBentPlateByPartsAndRadius(self: CDelegateWrapper,part1Id: int,part2Id: int,radius: float) -> int """
  pass
 def ExportCreateBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportCreateBoltGroup(self: CDelegateWrapper,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportCreateBooleanPart(self,pBooleanPart):
  """ ExportCreateBooleanPart(self: CDelegateWrapper,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportCreateClipPlane(self,pView,pClipPlane):
  """ ExportCreateClipPlane(self: CDelegateWrapper,pView: dotView_t,pClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportCreateComponent(self,pBaseComponent):
  """ ExportCreateComponent(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportCreateControlPlane(self,pControlObject):
  """ ExportCreateControlPlane(self: CDelegateWrapper,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportCreateConversionLink(self,pConversionLink):
  """ ExportCreateConversionLink(self: CDelegateWrapper,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportCreateEdgeChamfer(self,pEdgeChamfer):
  """ ExportCreateEdgeChamfer(self: CDelegateWrapper,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportCreateFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportCreateFittingOrCutPlane(self: CDelegateWrapper,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportCreateGrid(self,pGrid):
  """ ExportCreateGrid(self: CDelegateWrapper,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportCreateGridPlane(self,pGridPlane):
  """ ExportCreateGridPlane(self: CDelegateWrapper,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportCreateGuideline(self,pGuideline):
  """ ExportCreateGuideline(self: CDelegateWrapper,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportCreateIFC(self,aIFC):
  """ ExportCreateIFC(self: CDelegateWrapper,aIFC: dotCreateIFCFromModel_t) -> (int,dotCreateIFCFromModel_t) """
  pass
 def ExportCreateLegFace(self,pLegFace):
  """ ExportCreateLegFace(self: CDelegateWrapper,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportCreateLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportCreateLoad(self: CDelegateWrapper,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportCreateLoadGroup(self,pLoadGroup):
  """ ExportCreateLoadGroup(self: CDelegateWrapper,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportCreateNC(self,aNC):
  """ ExportCreateNC(self: CDelegateWrapper,aNC: dotCreateNCFromModel_t) -> (int,dotCreateNCFromModel_t) """
  pass
 def ExportCreateNewModel(self,pInfo):
  """ ExportCreateNewModel(self: CDelegateWrapper,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportCreatePart(self,pPart,contour):
  """ ExportCreatePart(self: CDelegateWrapper,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportCreatePourBreak(self,pPourBreak):
  """ ExportCreatePourBreak(self: CDelegateWrapper,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportCreateRebarEndDetailStrip(self,pStrip):
  """ ExportCreateRebarEndDetailStrip(self: CDelegateWrapper,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportCreateRebarGroup(self,pRebarGroup):
  """ ExportCreateRebarGroup(self: CDelegateWrapper,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportCreateRebarMesh(self,pRebarMesh):
  """ ExportCreateRebarMesh(self: CDelegateWrapper,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportCreateRebarPropertyStrip(self,pStrip):
  """ ExportCreateRebarPropertyStrip(self: CDelegateWrapper,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportCreateRebarSplice(self,pRebarSplice):
  """ ExportCreateRebarSplice(self: CDelegateWrapper,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportCreateRebarSplitter(self,pStrip):
  """ ExportCreateRebarSplitter(self: CDelegateWrapper,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportCreateRebarStrand(self,pRebarStrand):
  """ ExportCreateRebarStrand(self: CDelegateWrapper,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportCreateReferenceModel(self,pReferenceModel):
  """ ExportCreateReferenceModel(self: CDelegateWrapper,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportCreateReferenceModelObjectAttribute(self,pRMOAttribute):
  """ ExportCreateReferenceModelObjectAttribute(self: CDelegateWrapper,pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int,dotReferenceModelObjectAttribute_t) """
  pass
 def ExportCreateReferenceModelObjectAttributeEnumerator(self,pEnumerator):
  """ ExportCreateReferenceModelObjectAttributeEnumerator(self: CDelegateWrapper,pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int,dotReferenceModelObjectAttributeEnumerator_t) """
  pass
 def ExportCreateReport(self,aReport):
  """ ExportCreateReport(self: CDelegateWrapper,aReport: dotCreateReportFromModel_t) -> (int,dotCreateReportFromModel_t) """
  pass
 def ExportCreateSingleRebar(self,pSingleRebar):
  """ ExportCreateSingleRebar(self: CDelegateWrapper,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportCreateSurfaceByFace(self,hitPoint,faceNormal,id):
  """ ExportCreateSurfaceByFace(self: CDelegateWrapper,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceByFaceAndAttrib(self,hitPoint,faceNormal,id,name,surfaceClass):
  """ ExportCreateSurfaceByFaceAndAttrib(self: CDelegateWrapper,hitPoint: dotPoint_t,faceNormal: dotPoint_t,id: int,name: str,surfaceClass: str) -> (int,dotPoint_t,dotPoint_t) """
  pass
 def ExportCreateSurfaceObject(self,pSurfaceObject):
  """ ExportCreateSurfaceObject(self: CDelegateWrapper,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportCreateSurfaceTreatment(self,pTreatment):
  """ ExportCreateSurfaceTreatment(self: CDelegateWrapper,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportCreateTask(self,pTask):
  """ ExportCreateTask(self: CDelegateWrapper,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportCreateTaskDependency(self,pTaskDependency):
  """ ExportCreateTaskDependency(self: CDelegateWrapper,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportCreateTaskWorktype(self,pTaskWorktype):
  """ ExportCreateTaskWorktype(self: CDelegateWrapper,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportCreateWeld(self,pWeld):
  """ ExportCreateWeld(self: CDelegateWrapper,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportDasStartAction(self,ActionName,Parameter):
  """ ExportDasStartAction(self: CDelegateWrapper,ActionName: str,Parameter: str) -> int """
  pass
 def ExportDasStartCommand(self,CommandName,Parameter):
  """ ExportDasStartCommand(self: CDelegateWrapper,CommandName: str,Parameter: str) -> int """
  pass
 def ExportDeleteBasePoint(self,pBasePoint):
  """ ExportDeleteBasePoint(self: CDelegateWrapper,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportDeleteClipPlane(self,pView,pClipPlane):
  """ ExportDeleteClipPlane(self: CDelegateWrapper,pView: dotView_t,pClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportDeleteConversionLink(self,pConversionLink):
  """ ExportDeleteConversionLink(self: CDelegateWrapper,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportDeleteObject(self,pIdentifier):
  """ ExportDeleteObject(self: CDelegateWrapper,pIdentifier: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportDisplayAutoDefaultSettings(self,pBaseComponent):
  """ ExportDisplayAutoDefaultSettings(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayComponentHelp(self,pBaseComponent):
  """ ExportDisplayComponentHelp(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportDisplayPrompt(self,Message):
  """ ExportDisplayPrompt(self: CDelegateWrapper,Message: str) -> int """
  pass
 def ExportDisplayReport(self,FileName):
  """ ExportDisplayReport(self: CDelegateWrapper,FileName: str) -> int """
  pass
 def ExportDoubleListHandler(self,pDoubleList):
  """ ExportDoubleListHandler(self: CDelegateWrapper,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ExportDrawTemporaryPolygonSurface(self,pArgument):
  """ ExportDrawTemporaryPolygonSurface(self: CDelegateWrapper,pArgument: dotDrawPolygonSurface_t) -> (int,dotDrawPolygonSurface_t) """
  pass
 def ExportDrawTemporaryPolyLine(self,pArgument):
  """ ExportDrawTemporaryPolyLine(self: CDelegateWrapper,pArgument: dotDrawPolyLine_t) -> (int,dotDrawPolyLine_t) """
  pass
 def ExportDrawTemporaryPolyLineWithId(self,pArgument):
  """ ExportDrawTemporaryPolyLineWithId(self: CDelegateWrapper,pArgument: dotGraphicPolyLine_t) -> (int,dotGraphicPolyLine_t) """
  pass
 def ExportDrawTemporaryText(self,pArgument):
  """ ExportDrawTemporaryText(self: CDelegateWrapper,pArgument: dotDrawText_t) -> (int,dotDrawText_t) """
  pass
 def ExportEdgeListHandler(self,pEdgeList):
  """ ExportEdgeListHandler(self: CDelegateWrapper,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ExportEnumerateObjects(self,pEnumerator):
  """ ExportEnumerateObjects(self: CDelegateWrapper,pEnumerator: dotEnumerator_t) -> (int,dotEnumerator_t) """
  pass
 def ExportExtractBentPlateFromComponent(self,partId):
  """ ExportExtractBentPlateFromComponent(self: CDelegateWrapper,partId: int) -> int """
  pass
 def ExportFingerprint(self,pInput,fingerprint):
  """ ExportFingerprint(self: CDelegateWrapper,pInput: dotPolymesh_t,fingerprint: str) -> (int,dotPolymesh_t,str) """
  pass
 def ExportFormatProfile(self,profile):
  """ ExportFormatProfile(self: CDelegateWrapper,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportGetAllProperties(self,pProperties,pNames,pValues):
  """ ExportGetAllProperties(self: CDelegateWrapper,pProperties: dotGetProperties_t,pNames: List[object],pValues: List[object]) -> (int,dotGetProperties_t,List[object],List[object]) """
  pass
 def ExportGetAllReportProperties(self,pProperties):
  """ ExportGetAllReportProperties(self: CDelegateWrapper,pProperties: List[dotGetProperties_t]) -> (int,List[dotGetProperties_t]) """
  pass
 def ExportGetAssociateSurfaces(self,id):
  """ ExportGetAssociateSurfaces(self: CDelegateWrapper,id: int) -> List[int] """
  pass
 def ExportGetBasePoints(self,ClientId):
  """ ExportGetBasePoints(self: CDelegateWrapper,ClientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportGetBentPlateMaximumRadius(self,geometryNodeId,clientId):
  """ ExportGetBentPlateMaximumRadius(self: CDelegateWrapper,geometryNodeId: int,clientId: dotClientId_t) -> (float,dotClientId_t) """
  pass
 def ExportGetBentPlateMinimumRadius(self,partId):
  """ ExportGetBentPlateMinimumRadius(self: CDelegateWrapper,partId: int) -> float """
  pass
 def ExportGetClipPlanes(self,pView,pGetClipPlanes):
  """ ExportGetClipPlanes(self: CDelegateWrapper,pView: dotView_t,pGetClipPlanes: dotGetClipPlanes_t) -> (int,dotView_t,dotGetClipPlanes_t) """
  pass
 def ExportGetColorRepresentationForObject(self,pIdentifier,pColor):
  """ ExportGetColorRepresentationForObject(self: CDelegateWrapper,pIdentifier: dotIdentifier_t,pColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportGetCommandStatus(self,TSCommand,TSCommandParam,Status):
  """ ExportGetCommandStatus(self: CDelegateWrapper,TSCommand: str,TSCommandParam: str,Status: bool) -> (int,str,str,bool) """
  pass
 def ExportGetCommitData(self,pId,pObjectType,pObjectSubType,pCommitType):
  """ ExportGetCommitData(self: CDelegateWrapper,pId: dotIdentifier_t,pObjectType: int,pObjectSubType: int,pCommitType: int) -> (int,dotIdentifier_t,int,int,int) """
  pass
 def ExportGetComponentAttribute(self,pIdentifier,pAttribute):
  """ ExportGetComponentAttribute(self: CDelegateWrapper,pIdentifier: dotIdentifier_t,pAttribute: dotComponentAttribute_t) -> (int,dotIdentifier_t,dotComponentAttribute_t) """
  pass
 def ExportGetComponentInput(self,pObj):
  """ ExportGetComponentInput(self: CDelegateWrapper,pObj: dotComponentInputObject_t) -> (int,dotComponentInputObject_t) """
  pass
 def ExportGetCoordinateSystem(self,pModelObject,pCoordinateSystem):
  """ ExportGetCoordinateSystem(self: CDelegateWrapper,pModelObject: dotModelObject_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotModelObject_t,dotCoordinateSystem_t) """
  pass
 def ExportGetCutSolidSerialized(self,dotSolid1,dotSolid2,serializedFaceList,serializedVectorList,serializedFaceOriginPartIdList,serializedShellIndexList,serializedEdgeVertexList,serializedEdgeTypeList,serializedEdgeShellIndexList):
  """ ExportGetCutSolidSerialized(self: CDelegateWrapper,dotSolid1: dotSolid_t,dotSolid2: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedFaceOriginPartIdList: List[int],serializedShellIndexList: List[int],serializedEdgeVertexList: List[dotPoint_t],serializedEdgeTypeList: List[int],serializedEdgeShellIndexList: List[int]) -> (int,dotSolid_t,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetDatabaseVersion(self,Version):
  """ ExportGetDatabaseVersion(self: CDelegateWrapper,Version: int) -> (int,int) """
  pass
 def ExportGetDataBaseVersionInfoFromModel(self,pInfo):
  """ ExportGetDataBaseVersionInfoFromModel(self: CDelegateWrapper,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetDetectedClash(self,pClash):
  """ ExportGetDetectedClash(self: CDelegateWrapper,pClash: dotClash_t) -> (int,dotClash_t) """
  pass
 def ExportGetDotType(self,pModelObject):
  """ ExportGetDotType(self: CDelegateWrapper,pModelObject: dotModelObject_t) -> (int,dotModelObject_t) """
  pass
 def ExportGetFatherComponent(self,ObjectId,FatherComponentId):
  """ ExportGetFatherComponent(self: CDelegateWrapper,ObjectId: int,FatherComponentId: int) -> (int,int) """
  pass
 def ExportGetIntersectionBoundingBoxes(self,Identifier1,Identifier2,ClientId):
  """ ExportGetIntersectionBoundingBoxes(self: CDelegateWrapper,Identifier1: dotIdentifier_t,Identifier2: dotIdentifier_t,ClientId: dotClientId_t) -> (int,dotIdentifier_t,dotIdentifier_t,dotClientId_t) """
  pass
 def ExportGetIntersectionPoints(self,pIntersectionPoints):
  """ ExportGetIntersectionPoints(self: CDelegateWrapper,pIntersectionPoints: dotIntersectionPoints_t) -> (int,dotIntersectionPoints_t) """
  pass
 def ExportGetIntersectionSolid(self,pSolid):
  """ ExportGetIntersectionSolid(self: CDelegateWrapper,pSolid: dotIntersectionSolid_t) -> (int,dotIntersectionSolid_t) """
  pass
 def ExportGetModificationStamp(self,pModStmp):
  """ ExportGetModificationStamp(self: CDelegateWrapper,pModStmp: dotModificationStamp_t) -> (int,dotModificationStamp_t) """
  pass
 def ExportGetModificationStampGuid(self,pModStmp):
  """ ExportGetModificationStampGuid(self: CDelegateWrapper,pModStmp: str) -> (int,str) """
  pass
 def ExportGetNumberingUpToDate(self,pNumberingQuery):
  """ ExportGetNumberingUpToDate(self: CDelegateWrapper,pNumberingQuery: dotNumberingQuery_t) -> (int,dotNumberingQuery_t) """
  pass
 def ExportGetNumberOfClashes(self,pClashes):
  """ ExportGetNumberOfClashes(self: CDelegateWrapper,pClashes: int) -> (int,int) """
  pass
 def ExportGetObjectLastModified(self,pIdentifier,pTime,pLocallyModified):
  """ ExportGetObjectLastModified(self: CDelegateWrapper,pIdentifier: dotIdentifier_t,pTime: int,pLocallyModified: bool) -> (int,dotIdentifier_t,int,bool) """
  pass
 def ExportGetObjectPhase(self,pArgument):
  """ ExportGetObjectPhase(self: CDelegateWrapper,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportGetParentObject(self,surfaceId):
  """ ExportGetParentObject(self: CDelegateWrapper,surfaceId: int) -> int """
  pass
 def ExportGetPartLine(self,pPartLine):
  """ ExportGetPartLine(self: CDelegateWrapper,pPartLine: dotPartLine_t) -> (int,dotPartLine_t) """
  pass
 def ExportGetPartMark(self,pPartMark):
  """ ExportGetPartMark(self: CDelegateWrapper,pPartMark: dotPartMark_t) -> (int,dotPartMark_t) """
  pass
 def ExportGetPhaseNumbers(self,pArgument):
  """ ExportGetPhaseNumbers(self: CDelegateWrapper,pArgument: dotPhaseNumbers_t) -> (int,dotPhaseNumbers_t) """
  pass
 def ExportGetPlane(self,pPlane):
  """ ExportGetPlane(self: CDelegateWrapper,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportGetPolybeamCoordinateSystem(self,Id,SubId,Chamfered,pX,pY,pZ):
  """ ExportGetPolybeamCoordinateSystem(self: CDelegateWrapper,Id: int,SubId: int,Chamfered: int,pX: dotPoint_t,pY: dotPoint_t,pZ: dotPoint_t) -> (int,dotPoint_t,dotPoint_t,dotPoint_t) """
  pass
 def ExportGetProjectInfo(self,pInfo):
  """ ExportGetProjectInfo(self: CDelegateWrapper,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportGetProperties(self,pProperties):
  """ ExportGetProperties(self: CDelegateWrapper,pProperties: dotGetProperties_t) -> (int,dotGetProperties_t) """
  pass
 def ExportGetReferenceModelObjectByExternalGuid(self,referenceModelId,externalGuid):
  """ ExportGetReferenceModelObjectByExternalGuid(self: CDelegateWrapper,referenceModelId: int,externalGuid: dotIdentifier_t) -> (int,dotIdentifier_t) """
  pass
 def ExportGetReferenceModelRevisionIds(self,pReferenceModel,ClientId):
  """ ExportGetReferenceModelRevisionIds(self: CDelegateWrapper,pReferenceModel: dotReferenceModel_t,ClientId: dotClientId_t) -> (int,dotReferenceModel_t,dotClientId_t) """
  pass
 def ExportGetSetModelInfo(self,pInfo):
  """ ExportGetSetModelInfo(self: CDelegateWrapper,pInfo: dotModelInfo_t) -> (int,dotModelInfo_t) """
  pass
 def ExportGetSetModstamp(self,ModStampData):
  """ ExportGetSetModstamp(self: CDelegateWrapper,ModStampData: dotModStamp_t) -> (int,dotModStamp_t) """
  pass
 def ExportGetSnapshotFromDatabase(self,Enumerator,SelectInstances):
  """ ExportGetSnapshotFromDatabase(self: CDelegateWrapper,Enumerator: dotEnumerator_t,SelectInstances: bool) -> (Serializable[List[ModelObject]],dotEnumerator_t) """
  pass
 def ExportGetSolid(self,pSolid):
  """ ExportGetSolid(self: CDelegateWrapper,pSolid: dotSolid_t) -> (int,dotSolid_t) """
  pass
 def ExportGetSolidBrep(self,polymeshToClean,polymeshCleaned):
  """ ExportGetSolidBrep(self: CDelegateWrapper,polymeshToClean: dotPolymesh_t,polymeshCleaned: dotPolymesh_t) -> (bool,dotPolymesh_t,dotPolymesh_t) """
  pass
 def ExportGetSolidMerged(self,dotSolid,polymeshes):
  """ ExportGetSolidMerged(self: CDelegateWrapper,dotSolid: dotSolid_t,polymeshes: dotPolymesh_t) -> (int,dotSolid_t,dotPolymesh_t) """
  pass
 def ExportGetSolidSerialized(self,dotSolid,serializedFaceList,serializedVectorList,serializedShellIndexList,serializedFaceOriginIdList):
  """ ExportGetSolidSerialized(self: CDelegateWrapper,dotSolid: dotSolid_t,serializedFaceList: List[List[List[dotPoint_t]]],serializedVectorList: List[dotPoint_t],serializedShellIndexList: List[int],serializedFaceOriginIdList: List[int]) -> (int,dotSolid_t,List[List[List[dotPoint_t]]],List[dotPoint_t],List[int],List[int]) """
  pass
 def ExportGetStringPropertyFromDatabase(self,pProperty,stringValues):
  """ ExportGetStringPropertyFromDatabase(self: CDelegateWrapper,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportGetSurfaceGeometryType(self,surfaceId):
  """ ExportGetSurfaceGeometryType(self: CDelegateWrapper,surfaceId: int) -> int """
  pass
 def ExportGetTrackEvent(self,category,eventName,eventContent):
  """ ExportGetTrackEvent(self: CDelegateWrapper,category: str,eventName: str,eventContent: str) -> (int,str,str,str) """
  pass
 def ExportGetTransformationPlane(self,pPlane):
  """ ExportGetTransformationPlane(self: CDelegateWrapper,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportGetViewCamera(self,pView,pCamera):
  """ ExportGetViewCamera(self: CDelegateWrapper,pView: dotView_t,pCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportGetViews(self,pViews):
  """ ExportGetViews(self: CDelegateWrapper,pViews: dotViewSelector_t) -> (int,dotViewSelector_t) """
  pass
 def ExportGetWeldGeometry(self,pWeldGeometry):
  """ ExportGetWeldGeometry(self: CDelegateWrapper,pWeldGeometry: dotWeldGeometry_t) -> (int,dotWeldGeometry_t) """
  pass
 def ExportGetWriteOutStampGuid(self,pModStmp):
  """ ExportGetWriteOutStampGuid(self: CDelegateWrapper,pModStmp: str) -> (int,str) """
  pass
 def ExportHierarchicDefinition(self,pHierarchicDefinition):
  """ ExportHierarchicDefinition(self: CDelegateWrapper,pHierarchicDefinition: dotHierarchicDefinition_t) -> (int,dotHierarchicDefinition_t) """
  pass
 def ExportHierarchicObject(self,pHierarchicObject):
  """ ExportHierarchicObject(self: CDelegateWrapper,pHierarchicObject: dotHierarchicObject_t) -> (int,dotHierarchicObject_t) """
  pass
 def ExportHierarchicObjectChildrenOperation(self,pHierarchicList):
  """ ExportHierarchicObjectChildrenOperation(self: CDelegateWrapper,pHierarchicList: dotHierarchicList_t) -> (int,dotHierarchicList_t) """
  pass
 def ExportInitializeComponentStacks(self):
  """ ExportInitializeComponentStacks(self: CDelegateWrapper) -> int """
  pass
 def ExportInsertView(self,pDotView):
  """ ExportInsertView(self: CDelegateWrapper,pDotView: dotView_t) -> (int,dotView_t) """
  pass
 def ExportIntListHandler(self,pIntList):
  """ ExportIntListHandler(self: CDelegateWrapper,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ExportLoadComponentAttributes(self,pBaseComponent):
  """ ExportLoadComponentAttributes(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportManipulateObject(self,pArgument):
  """ ExportManipulateObject(self: CDelegateWrapper,pArgument: dotManipulateObject_t) -> (int,dotManipulateObject_t) """
  pass
 def ExportModifyAssembly(self,pAssembly):
  """ ExportModifyAssembly(self: CDelegateWrapper,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportModifyBasePoint(self,pBasePoint):
  """ ExportModifyBasePoint(self: CDelegateWrapper,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportModifyBentPlate(self,pPart):
  """ ExportModifyBentPlate(self: CDelegateWrapper,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportModifyBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportModifyBoltGroup(self: CDelegateWrapper,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportModifyBooleanPart(self,pBooleanPart):
  """ ExportModifyBooleanPart(self: CDelegateWrapper,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportModifyClipPlane(self,pView,pClipPlane):
  """ ExportModifyClipPlane(self: CDelegateWrapper,pView: dotView_t,pClipPlane: dotClipPlane_t) -> (int,dotView_t,dotClipPlane_t) """
  pass
 def ExportModifyComponent(self,pBaseComponent):
  """ ExportModifyComponent(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportModifyControlPlane(self,pControlObject):
  """ ExportModifyControlPlane(self: CDelegateWrapper,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportModifyCylindricalSurfaceNode(self,geometryNodeId,surfacePoints,clientId):
  """ ExportModifyCylindricalSurfaceNode(self: CDelegateWrapper,geometryNodeId: int,surfacePoints: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyEdgeChamfer(self,pEdgeChamfer):
  """ ExportModifyEdgeChamfer(self: CDelegateWrapper,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportModifyFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportModifyFittingOrCutPlane(self: CDelegateWrapper,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeCurveType(self,geometryNodeId,newCurveType,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: CDelegateWrapper,geometryNodeId: int,newCurveType: int,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreeCylindricalNodeRadius(self,geometryNodeId,radius,clientId):
  """ ExportModifyGeometryTreeCylindricalNodeRadius(self: CDelegateWrapper,geometryNodeId: int,radius: float,clientId: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportModifyGeometryTreePolygonNode(self,geometryNodeId,contour,clientId):
  """ ExportModifyGeometryTreePolygonNode(self: CDelegateWrapper,geometryNodeId: int,contour: dotContour_t,clientId: dotClientId_t) -> (int,dotContour_t,dotClientId_t) """
  pass
 def ExportModifyGrid(self,pGrid):
  """ ExportModifyGrid(self: CDelegateWrapper,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportModifyGridPlane(self,pGridPlane):
  """ ExportModifyGridPlane(self: CDelegateWrapper,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportModifyLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportModifyLoad(self: CDelegateWrapper,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportModifyLoadGroup(self,pLoadGroup):
  """ ExportModifyLoadGroup(self: CDelegateWrapper,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportModifyPart(self,pPart,contour):
  """ ExportModifyPart(self: CDelegateWrapper,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportModifyPourBreak(self,pPourBreak):
  """ ExportModifyPourBreak(self: CDelegateWrapper,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportModifyPourObject(self,pPourObject):
  """ ExportModifyPourObject(self: CDelegateWrapper,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportModifyProjectInfo(self,pInfo):
  """ ExportModifyProjectInfo(self: CDelegateWrapper,pInfo: dotProjectInfo_t) -> (int,dotProjectInfo_t) """
  pass
 def ExportModifyRebarEndDetailStrip(self,pStrip):
  """ ExportModifyRebarEndDetailStrip(self: CDelegateWrapper,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportModifyRebarGroup(self,pRebarGroup):
  """ ExportModifyRebarGroup(self: CDelegateWrapper,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportModifyRebarMesh(self,pRebarMesh):
  """ ExportModifyRebarMesh(self: CDelegateWrapper,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportModifyRebarPropertyStrip(self,pStrip):
  """ ExportModifyRebarPropertyStrip(self: CDelegateWrapper,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportModifyRebarSplice(self,pRebarSplice):
  """ ExportModifyRebarSplice(self: CDelegateWrapper,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportModifyRebarSplitter(self,pStrip):
  """ ExportModifyRebarSplitter(self: CDelegateWrapper,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportModifyRebarStrand(self,pRebarStrand):
  """ ExportModifyRebarStrand(self: CDelegateWrapper,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportModifyReferenceModel(self,pReferenceModel):
  """ ExportModifyReferenceModel(self: CDelegateWrapper,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportModifySingleRebar(self,pSingleRebar):
  """ ExportModifySingleRebar(self: CDelegateWrapper,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportModifySurfaceObject(self,pSurfaceObject):
  """ ExportModifySurfaceObject(self: CDelegateWrapper,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportModifySurfaceTreatment(self,pTreatment):
  """ ExportModifySurfaceTreatment(self: CDelegateWrapper,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportModifyTask(self,pTask):
  """ ExportModifyTask(self: CDelegateWrapper,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportModifyTaskDependency(self,pTaskDependency):
  """ ExportModifyTaskDependency(self: CDelegateWrapper,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportModifyTaskWorktype(self,pTaskWorktype):
  """ ExportModifyTaskWorktype(self: CDelegateWrapper,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportModifyView(self,pDotView):
  """ ExportModifyView(self: CDelegateWrapper,pDotView: dotView_t) -> (int,dotView_t) """
  pass
 def ExportModifyWeld(self,pWeld):
  """ ExportModifyWeld(self: CDelegateWrapper,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportModStampCompare(self,ModStampCompare):
  """ ExportModStampCompare(self: CDelegateWrapper,ModStampCompare: dotModStampCompare_t) -> (int,dotModStampCompare_t) """
  pass
 def ExportObjectMatchesToFilter(self,pObjectId,FileName):
  """ ExportObjectMatchesToFilter(self: CDelegateWrapper,pObjectId: dotIdentifier_t,FileName: str) -> (int,dotIdentifier_t) """
  pass
 def ExportParseProfile(self,profile):
  """ ExportParseProfile(self: CDelegateWrapper,profile: dotProfile_t) -> (int,dotProfile_t) """
  pass
 def ExportPointListHandler(self,pPointList):
  """ ExportPointListHandler(self: CDelegateWrapper,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ExportProgressBarOperation(self,pProgressBar):
  """ ExportProgressBarOperation(self: CDelegateWrapper,pProgressBar: dotProgressBar_t) -> (int,dotProgressBar_t) """
  pass
 def ExportRebarSetAdditionFunction(self,action,pRebarSetAddition):
  """ ExportRebarSetAdditionFunction(self: CDelegateWrapper,action: RebarSetAction,pRebarSetAddition: dotRebarSetAddition_t) -> (int,dotRebarSetAddition_t) """
  pass
 def ExportRebarSetFunction(self,action,pRebarSet):
  """ ExportRebarSetFunction(self: CDelegateWrapper,action: RebarSetAction,pRebarSet: dotRebarSet_t) -> (int,dotRebarSet_t) """
  pass
 def ExportRefreshReferenceFile(self,pReferenceModel):
  """ ExportRefreshReferenceFile(self: CDelegateWrapper,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportRemoveFromPourUnit(self,clientId):
  """ ExportRemoveFromPourUnit(self: CDelegateWrapper,clientId: dotClientId_t) -> (bool,dotClientId_t) """
  pass
 def ExportRemoveTemporaryGraphicsObjects(self,pArgument):
  """ ExportRemoveTemporaryGraphicsObjects(self: CDelegateWrapper,pArgument: dotClientId_t) -> (int,dotClientId_t) """
  pass
 def ExportRunMacro(self,FileName):
  """ ExportRunMacro(self: CDelegateWrapper,FileName: str) -> int """
  pass
 def ExportRunOrStopClashCheck(self,RunningClashCheck):
  """ ExportRunOrStopClashCheck(self: CDelegateWrapper,RunningClashCheck: bool) -> int """
  pass
 def ExportSaveAsWebModel(self,pSaveAsWebModel):
  """ ExportSaveAsWebModel(self: CDelegateWrapper,pSaveAsWebModel: dotSaveAsWebModel_t) -> (int,dotSaveAsWebModel_t) """
  pass
 def ExportSaveOperation(self,pOperation):
  """ ExportSaveOperation(self: CDelegateWrapper,pOperation: dotSaveOperation_t) -> (int,dotSaveOperation_t) """
  pass
 def ExportSelectAssembly(self,pAssembly):
  """ ExportSelectAssembly(self: CDelegateWrapper,pAssembly: dotAssembly_t) -> (int,dotAssembly_t) """
  pass
 def ExportSelectBasePoint(self,guid,pBasePoint):
  """ ExportSelectBasePoint(self: CDelegateWrapper,guid: str,pBasePoint: dotBasePointData_t) -> (int,dotBasePointData_t) """
  pass
 def ExportSelectBentPlate(self,pPart):
  """ ExportSelectBentPlate(self: CDelegateWrapper,pPart: dotPart_t) -> (int,dotPart_t) """
  pass
 def ExportSelectBoltGroup(self,pBoltShapeData,pBoltGroup):
  """ ExportSelectBoltGroup(self: CDelegateWrapper,pBoltShapeData: dotBoltShapeData_t,pBoltGroup: dotBoltGroup_t) -> (int,dotBoltShapeData_t,dotBoltGroup_t) """
  pass
 def ExportSelectBooleanPart(self,pBooleanPart):
  """ ExportSelectBooleanPart(self: CDelegateWrapper,pBooleanPart: dotBooleanPart_t) -> (int,dotBooleanPart_t) """
  pass
 def ExportSelectComponent(self,pBaseComponent):
  """ ExportSelectComponent(self: CDelegateWrapper,pBaseComponent: dotBaseComponent_t) -> (int,dotBaseComponent_t) """
  pass
 def ExportSelectControlPlane(self,pControlObject):
  """ ExportSelectControlPlane(self: CDelegateWrapper,pControlObject: dotControlObject_t) -> (int,dotControlObject_t) """
  pass
 def ExportSelectConversionLink(self,pConversionLink):
  """ ExportSelectConversionLink(self: CDelegateWrapper,pConversionLink: dotConversionLink_t) -> (int,dotConversionLink_t) """
  pass
 def ExportSelectEdgeChamfer(self,pEdgeChamfer):
  """ ExportSelectEdgeChamfer(self: CDelegateWrapper,pEdgeChamfer: dotEdgeChamfer_t) -> (int,dotEdgeChamfer_t) """
  pass
 def ExportSelectFittingOrCutPlane(self,pFittingOrCutPlane):
  """ ExportSelectFittingOrCutPlane(self: CDelegateWrapper,pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int,dotFittingOrCutPlane_t) """
  pass
 def ExportSelectGrid(self,pGrid):
  """ ExportSelectGrid(self: CDelegateWrapper,pGrid: dotGrid_t) -> (int,dotGrid_t) """
  pass
 def ExportSelectGridPlane(self,pGridPlane):
  """ ExportSelectGridPlane(self: CDelegateWrapper,pGridPlane: dotGridPlane_t) -> (int,dotGridPlane_t) """
  pass
 def ExportSelectGuideline(self,pGuideline):
  """ ExportSelectGuideline(self: CDelegateWrapper,pGuideline: dotGuideline_t) -> (int,dotGuideline_t) """
  pass
 def ExportSelectLegFace(self,pLegFace):
  """ ExportSelectLegFace(self: CDelegateWrapper,pLegFace: dotLegFace_t) -> (int,dotLegFace_t) """
  pass
 def ExportSelectLoad(self,pLoadCommonAttributes,pLoadClassAttributes):
  """ ExportSelectLoad(self: CDelegateWrapper,pLoadCommonAttributes: dotLoadCommonAttributes_t,pLoadClassAttributes: dotLoadClassAttributes_t) -> (int,dotLoadCommonAttributes_t,dotLoadClassAttributes_t) """
  pass
 def ExportSelectLoadGroup(self,pLoadGroup):
  """ ExportSelectLoadGroup(self: CDelegateWrapper,pLoadGroup: dotLoadGroup_t) -> (int,dotLoadGroup_t) """
  pass
 def ExportSelectPart(self,pPart,contour):
  """ ExportSelectPart(self: CDelegateWrapper,pPart: dotPart_t,contour: List[dotContourPoint_t]) -> (int,dotPart_t,List[dotContourPoint_t]) """
  pass
 def ExportSelectPourBreak(self,pPourBreak):
  """ ExportSelectPourBreak(self: CDelegateWrapper,pPourBreak: dotPolymeshObject_t) -> (int,dotPolymeshObject_t) """
  pass
 def ExportSelectPourObject(self,pPourObject):
  """ ExportSelectPourObject(self: CDelegateWrapper,pPourObject: dotPourObject_t) -> (int,dotPourObject_t) """
  pass
 def ExportSelectRebarBars(self,pWire):
  """ ExportSelectRebarBars(self: CDelegateWrapper,pWire: dotWire_t) -> (int,dotWire_t) """
  pass
 def ExportSelectRebarEndDetailStrip(self,pStrip):
  """ ExportSelectRebarEndDetailStrip(self: CDelegateWrapper,pStrip: dotRebarEndDetailStrip_t) -> (int,dotRebarEndDetailStrip_t) """
  pass
 def ExportSelectRebarGroup(self,pRebarGroup):
  """ ExportSelectRebarGroup(self: CDelegateWrapper,pRebarGroup: dotRebarGroup_t) -> (int,dotRebarGroup_t) """
  pass
 def ExportSelectRebarMesh(self,pRebarMesh):
  """ ExportSelectRebarMesh(self: CDelegateWrapper,pRebarMesh: dotRebarMesh_t) -> (int,dotRebarMesh_t) """
  pass
 def ExportSelectRebarPropertyStrip(self,pStrip):
  """ ExportSelectRebarPropertyStrip(self: CDelegateWrapper,pStrip: dotRebarPropertyStrip_t) -> (int,dotRebarPropertyStrip_t) """
  pass
 def ExportSelectRebarSplice(self,pRebarSplice):
  """ ExportSelectRebarSplice(self: CDelegateWrapper,pRebarSplice: dotRebarSplice_t) -> (int,dotRebarSplice_t) """
  pass
 def ExportSelectRebarSplitter(self,pStrip):
  """ ExportSelectRebarSplitter(self: CDelegateWrapper,pStrip: dotRebarSplitter_t) -> (int,dotRebarSplitter_t) """
  pass
 def ExportSelectRebarStrand(self,pRebarStrand):
  """ ExportSelectRebarStrand(self: CDelegateWrapper,pRebarStrand: dotRebarStrand_t) -> (int,dotRebarStrand_t) """
  pass
 def ExportSelectReferenceModel(self,pReferenceModel):
  """ ExportSelectReferenceModel(self: CDelegateWrapper,pReferenceModel: dotReferenceModel_t) -> (int,dotReferenceModel_t) """
  pass
 def ExportSelectReferenceModelObject(self,pReferenceModelObject):
  """ ExportSelectReferenceModelObject(self: CDelegateWrapper,pReferenceModelObject: dotReferenceModelObject_t) -> (int,dotReferenceModelObject_t) """
  pass
 def ExportSelectReferenceModelRevision(self,modelId,revisionId,pRevision):
  """ ExportSelectReferenceModelRevision(self: CDelegateWrapper,modelId: int,revisionId: int,pRevision: dotReferenceModelRevision_t) -> (int,dotReferenceModelRevision_t) """
  pass
 def ExportSelectSingleRebar(self,pSingleRebar):
  """ ExportSelectSingleRebar(self: CDelegateWrapper,pSingleRebar: dotSingleRebar_t) -> (int,dotSingleRebar_t) """
  pass
 def ExportSelectSurfaceObject(self,pSurfaceObject):
  """ ExportSelectSurfaceObject(self: CDelegateWrapper,pSurfaceObject: dotSurfaceObject_t) -> (int,dotSurfaceObject_t) """
  pass
 def ExportSelectSurfaceTreatment(self,pTreatment):
  """ ExportSelectSurfaceTreatment(self: CDelegateWrapper,pTreatment: dotSurfaceTreatment_t) -> (int,dotSurfaceTreatment_t) """
  pass
 def ExportSelectTask(self,pTask):
  """ ExportSelectTask(self: CDelegateWrapper,pTask: dotTask_t) -> (int,dotTask_t) """
  pass
 def ExportSelectTaskDependency(self,pTaskDependency):
  """ ExportSelectTaskDependency(self: CDelegateWrapper,pTaskDependency: dotTaskDependency_t) -> (int,dotTaskDependency_t) """
  pass
 def ExportSelectTaskWorktype(self,pTaskWorktype):
  """ ExportSelectTaskWorktype(self: CDelegateWrapper,pTaskWorktype: dotTaskWorktype_t) -> (int,dotTaskWorktype_t) """
  pass
 def ExportSelectView(self,pDotView):
  """ ExportSelectView(self: CDelegateWrapper,pDotView: dotView_t) -> (int,dotView_t) """
  pass
 def ExportSelectWeld(self,pWeld):
  """ ExportSelectWeld(self: CDelegateWrapper,pWeld: dotWeld_t) -> (int,dotWeld_t) """
  pass
 def ExportSetAdvancedOption(self,pArgument):
  """ ExportSetAdvancedOption(self: CDelegateWrapper,pArgument: dotGetAdvancedOption_t) -> (int,dotGetAdvancedOption_t) """
  pass
 def ExportSetAsCurrentRevision(self,modelId,revisionId):
  """ ExportSetAsCurrentRevision(self: CDelegateWrapper,modelId: int,revisionId: int) -> int """
  pass
 def ExportSetGetPhaseProperty(self,pArgument):
  """ ExportSetGetPhaseProperty(self: CDelegateWrapper,pArgument: dotSetGetProperty_t) -> (int,dotSetGetProperty_t) """
  pass
 def ExportSetObjectPhase(self,pArgument):
  """ ExportSetObjectPhase(self: CDelegateWrapper,pArgument: dotPhase_t) -> (int,dotPhase_t) """
  pass
 def ExportSetPlane(self,pPlane):
  """ ExportSetPlane(self: CDelegateWrapper,pPlane: dotPlane_t) -> (int,dotPlane_t) """
  pass
 def ExportSetProperty(self,pProperty):
  """ ExportSetProperty(self: CDelegateWrapper,pProperty: dotSetProperty_t) -> (int,dotSetProperty_t) """
  pass
 def ExportSetRepresentation(self,pViews):
  """ ExportSetRepresentation(self: CDelegateWrapper,pViews: str) -> int """
  pass
 def ExportSetStringPropertyToDatabase(self,pProperty,stringValues):
  """ ExportSetStringPropertyToDatabase(self: CDelegateWrapper,pProperty: dotStringProperty_t,stringValues: List[str]) -> (int,dotStringProperty_t,List[str]) """
  pass
 def ExportSetTemporaryColor(self,pObjectId,pNewColor):
  """ ExportSetTemporaryColor(self: CDelegateWrapper,pObjectId: dotIdentifier_t,pNewColor: dotColor_t) -> (int,dotIdentifier_t,dotColor_t) """
  pass
 def ExportSetTemporaryColors(self,pSetTemporaryColors):
  """ ExportSetTemporaryColors(self: CDelegateWrapper,pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryColors_FAST(self,pObjects,pSetTemporaryColors):
  """ ExportSetTemporaryColors_FAST(self: CDelegateWrapper,pObjects: List[Identifier],pSetTemporaryColors: dotSetTemporaryColors_t) -> (int,List[Identifier],dotSetTemporaryColors_t) """
  pass
 def ExportSetTemporaryState(self,pObjectId,pNewState):
  """ ExportSetTemporaryState(self: CDelegateWrapper,pObjectId: dotIdentifier_t,pNewState: dotTemporaryStatesEnum) -> (int,dotIdentifier_t,dotTemporaryStatesEnum) """
  pass
 def ExportSetTemporaryStates(self,pSetTemporaryStates):
  """ ExportSetTemporaryStates(self: CDelegateWrapper,pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,dotSetTemporaryStates_t) """
  pass
 def ExportSetTemporaryStates_FAST(self,pObjects,pSetTemporaryStates):
  """ ExportSetTemporaryStates_FAST(self: CDelegateWrapper,pObjects: List[Identifier],pSetTemporaryStates: dotSetTemporaryStates_t) -> (int,List[Identifier],dotSetTemporaryStates_t) """
  pass
 def ExportSetTransformationPlane(self,pPlane):
  """ ExportSetTransformationPlane(self: CDelegateWrapper,pPlane: dotTransformationPlane_t) -> (int,dotTransformationPlane_t) """
  pass
 def ExportSetViewCamera(self,pView,pCamera):
  """ ExportSetViewCamera(self: CDelegateWrapper,pView: dotView_t,pCamera: dotCamera_t) -> (int,dotView_t,dotCamera_t) """
  pass
 def ExportShadowArea(self,pArgument):
  """ ExportShadowArea(self: CDelegateWrapper,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportShadowAreaComplement(self,pArgument):
  """ ExportShadowAreaComplement(self: CDelegateWrapper,pArgument: dotAreaPolygons_t) -> (int,dotAreaPolygons_t) """
  pass
 def ExportSharingOperation(self,pOperation):
  """ ExportSharingOperation(self: CDelegateWrapper,pOperation: dotSharingOperation_t) -> (int,dotSharingOperation_t) """
  pass
 def ExportSingleRebarGetRebarSet(self,singleRebarId):
  """ ExportSingleRebarGetRebarSet(self: CDelegateWrapper,singleRebarId: int) -> int """
  pass
 def ExportStartCustomComponentCreation(self,ComponentName):
  """ ExportStartCustomComponentCreation(self: CDelegateWrapper,ComponentName: str) -> int """
  pass
 def ExportStartPluginCreation(self,ComponentName):
  """ ExportStartPluginCreation(self: CDelegateWrapper,ComponentName: str) -> int """
  pass
 def ExportStringListHandler(self,pStringList):
  """ ExportStringListHandler(self: CDelegateWrapper,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def ExportTaskObjectAttach(self,pSelector):
  """ ExportTaskObjectAttach(self: CDelegateWrapper,pSelector: dotTaskObjectAttacher_t) -> (int,dotTaskObjectAttacher_t) """
  pass
 def ExportUIObjectPick(self,pPicker):
  """ ExportUIObjectPick(self: CDelegateWrapper,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUIObjectSelect(self,pSelector):
  """ ExportUIObjectSelect(self: CDelegateWrapper,pSelector: dotUIModelObjectSelector_t) -> (int,dotUIModelObjectSelector_t) """
  pass
 def ExportUIObjectsPick(self,pPicker):
  """ ExportUIObjectsPick(self: CDelegateWrapper,pPicker: dotUIPicker_t) -> (int,dotUIPicker_t) """
  pass
 def ExportUndoOperation(self,pOperation):
  """ ExportUndoOperation(self: CDelegateWrapper,pOperation: dotUndoOperation_t) -> (int,dotUndoOperation_t) """
  pass
 def ExportValidatePolymesh(self,checkCriteria,polymeshToValidate,invalidInfo):
  """ ExportValidatePolymesh(self: CDelegateWrapper,checkCriteria: int,polymeshToValidate: dotPolymesh_t,invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool,dotPolymesh_t,dotPolymeshValidateInvalidInfo_t) """
  pass
 def ExportViewHideUnselected(self,HideCompletely,DrawAsStick):
  """ ExportViewHideUnselected(self: CDelegateWrapper,HideCompletely: bool,DrawAsStick: bool) -> int """
  pass
 def ExportWriteToSessionLog(self,Message):
  """ ExportWriteToSessionLog(self: CDelegateWrapper,Message: str) -> int """
  pass
 def GetDSTVCoordinateSystem(self,PartId,pCoordinateSystem):
  """ GetDSTVCoordinateSystem(self: CDelegateWrapper,PartId: dotIdentifier_t,pCoordinateSystem: dotCoordinateSystem_t) -> (int,dotCoordinateSystem_t) """
  pass
 def ImportDoubleListHandler(self,pDoubleList):
  """ ImportDoubleListHandler(self: CDelegateWrapper,pDoubleList: dotnetDoubleList_t) -> (int,dotnetDoubleList_t) """
  pass
 def ImportEdgeListHandler(self,pEdgeList):
  """ ImportEdgeListHandler(self: CDelegateWrapper,pEdgeList: dotnetEdgeList_t) -> (int,dotnetEdgeList_t) """
  pass
 def ImportIntListHandler(self,pIntList):
  """ ImportIntListHandler(self: CDelegateWrapper,pIntList: dotnetIntList_t) -> (int,dotnetIntList_t) """
  pass
 def ImportPointListHandler(self,pPointList):
  """ ImportPointListHandler(self: CDelegateWrapper,pPointList: dotnetPointList_t) -> (int,dotnetPointList_t) """
  pass
 def ImportStringListHandler(self,pStringList):
  """ ImportStringListHandler(self: CDelegateWrapper,pStringList: dotnetStringList_t) -> (int,dotnetStringList_t) """
  pass
 def IsMacroRunning(self):
  """ IsMacroRunning(self: CDelegateWrapper) -> int """
  pass
 @staticmethod
 def __new__(self,instance,functionality):
  """ __new__(cls: type,instance: ICDelegate,functionality: WrapperFunctionalityBase) """
  pass
 _functionality=None
 _instance=None

