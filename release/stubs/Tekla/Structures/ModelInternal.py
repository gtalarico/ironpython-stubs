# encoding: utf-8
# module Tekla.Structures.ModelInternal calls itself ModelInternal
# from Tekla.Structures.Model, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AreWeUnitTesting(object):
    # no doc
    Value = False
    __all__ = []


class BasePoint(object):
    """ BasePoint(id: int, guid: Guid, name: str, description: str, coordinateSystem: str, northSouth: float, eastWest: float, elevation: float, latitude: float, longitude: float, locationInModelX: float, locationInModelY: float, locationInModelZ: float, angleToNorth: float) """
    def GetCompoundPlaneAngleLatitude(self):
        """ GetCompoundPlaneAngleLatitude(self: BasePoint) -> Tuple[bool, int, int, int] """
        pass

    def GetCompoundPlaneAngleLongitude(self):
        """ GetCompoundPlaneAngleLongitude(self: BasePoint) -> Tuple[bool, int, int, int] """
        pass

    def GetCoordinateSystem(self, CoordsysType):
        """ GetCoordinateSystem(self: BasePoint, CoordsysType: CoordinateSystemType) -> CoordinateSystem """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, guid, name, description, coordinateSystem, northSouth, eastWest, elevation, latitude, longitude, locationInModelX, locationInModelY, locationInModelZ, angleToNorth):
        """ __new__(cls: type, id: int, guid: Guid, name: str, description: str, coordinateSystem: str, northSouth: float, eastWest: float, elevation: float, latitude: float, longitude: float, locationInModelX: float, locationInModelY: float, locationInModelZ: float, angleToNorth: float) """
        pass

    AngleToNorth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleToNorth(self: BasePoint) -> float

Set: AngleToNorth(self: BasePoint) = value
"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: BasePoint) -> str

Set: CoordinateSystem(self: BasePoint) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: BasePoint) -> str

Set: Description(self: BasePoint) = value
"""

    EastWest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EastWest(self: BasePoint) -> float

Set: EastWest(self: BasePoint) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: BasePoint) -> float

Set: Elevation(self: BasePoint) = value
"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: BasePoint) -> Guid

Set: Guid(self: BasePoint) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BasePoint) -> int

Set: Id(self: BasePoint) = value
"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Latitude(self: BasePoint) -> float

Set: Latitude(self: BasePoint) = value
"""

    LocationInModelX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationInModelX(self: BasePoint) -> float

Set: LocationInModelX(self: BasePoint) = value
"""

    LocationInModelY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationInModelY(self: BasePoint) -> float

Set: LocationInModelY(self: BasePoint) = value
"""

    LocationInModelZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationInModelZ(self: BasePoint) -> float

Set: LocationInModelZ(self: BasePoint) = value
"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Longitude(self: BasePoint) -> float

Set: Longitude(self: BasePoint) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BasePoint) -> str

Set: Name(self: BasePoint) = value
"""

    NorthSouth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NorthSouth(self: BasePoint) -> float

Set: NorthSouth(self: BasePoint) = value
"""


    CoordinateSystemType = None


class BentPlateTestingTool(object):
    """ BentPlateTestingTool() """
    def CreateByFaces(self, part1, face1, part2, face2):
        """ CreateByFaces(self: BentPlateTestingTool, part1: Part, face1: IList[Point], part2: Part, face2: IList[Point]) -> BentPlate """
        pass


class BentPlateTools(object):
    """ BentPlateTools() """
    def ExtractBentPlateFromComponent(self, partId):
        """ ExtractBentPlateFromComponent(self: BentPlateTools, partId: Identifier) -> Identifier """
        pass

    def GetMaximumRadius(self, geometryNodeId, geometry):
        """ GetMaximumRadius(self: BentPlateTools, geometryNodeId: int, geometry: ConnectiveGeometry) -> float """
        pass

    def GetMinimumRadius(self, bentPlate):
        """ GetMinimumRadius(self: BentPlateTools, bentPlate: Part) -> float """
        pass

    def ModifyCurveType(self, geometry, geometryNodeId, newCurveType):
        """ ModifyCurveType(self: BentPlateTools, geometry: ConnectiveGeometry, geometryNodeId: int, newCurveType: int) """
        pass


class CDelegateSetter(object):
    # no doc
    @staticmethod
    def SetInstanceForUnitTesting(cdelegate):
        """ SetInstanceForUnitTesting(cdelegate: ICDelegate) """
        pass

    __all__ = [
        '__reduce_ex__',
        'SetInstanceForUnitTesting',
    ]


class CDelegateWrapper(MarshalByRefObject):
    """ CDelegateWrapper(instance: ICDelegate, functionality: WrapperFunctionalityBase) """
    def ExplodeBentPlate(self, partId):
        """ ExplodeBentPlate(self: CDelegateWrapper, partId: int) -> int """
        pass

    def ExportAddComponentAttributeToStack(self, pAttr):
        """ ExportAddComponentAttributeToStack(self: CDelegateWrapper, pAttr: dotComponentAttribute_t) -> (int, dotComponentAttribute_t) """
        pass

    def ExportAddComponentInputToStack(self, pObj):
        """ ExportAddComponentInputToStack(self: CDelegateWrapper, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportAddToPourUnit(self, inputPour, clientId):
        """ ExportAddToPourUnit(self: CDelegateWrapper, inputPour: dotPourObject_t, clientId: dotClientId_t) -> (bool, dotPourObject_t, dotClientId_t) """
        pass

    def ExportCalculateContourPolygon(self, pContour, pPolygon):
        """ ExportCalculateContourPolygon(self: CDelegateWrapper, pContour: dotContour_t, pPolygon: dotPolygon_t) -> (int, dotContour_t, dotPolygon_t) """
        pass

    def ExportCalculatePourUnits(self):
        """ ExportCalculatePourUnits(self: CDelegateWrapper) -> bool """
        pass

    def ExportChangeManagerAllowNumbering(self, NumberingFlag):
        """ ExportChangeManagerAllowNumbering(self: CDelegateWrapper, NumberingFlag: bool) -> int """
        pass

    def ExportChangeManagerAllowSave(self, SaveFlag):
        """ ExportChangeManagerAllowSave(self: CDelegateWrapper, SaveFlag: bool) -> int """
        pass

    def ExportCleanDrawingFiles(self, Silent, BackupPath):
        """ ExportCleanDrawingFiles(self: CDelegateWrapper, Silent: bool, BackupPath: str) -> int """
        pass

    def ExportClearAllTemporaryStates(self):
        """ ExportClearAllTemporaryStates(self: CDelegateWrapper) -> int """
        pass

    def ExportClearTemporaryState(self, pObjectId):
        """ ExportClearTemporaryState(self: CDelegateWrapper, pObjectId: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportCommitChanges(self, pModelCommit):
        """ ExportCommitChanges(self: CDelegateWrapper, pModelCommit: dotModelCommit_t) -> (int, dotModelCommit_t) """
        pass

    def ExportCompareFingerprints(self, fingerprint1, fingerprint2):
        """ ExportCompareFingerprints(self: CDelegateWrapper, fingerprint1: str, fingerprint2: str) -> bool """
        pass

    def ExportCompareObjects(self, ObjectId, ObjectToCompareId):
        """ ExportCompareObjects(self: CDelegateWrapper, ObjectId: int, ObjectToCompareId: int) -> int """
        pass

    def ExportConnectGeometryTrees(self, clientId):
        """ ExportConnectGeometryTrees(self: CDelegateWrapper, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPoints(self, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPoints(self: CDelegateWrapper, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPointsWithRadius(self, radius, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPointsWithRadius(self: CDelegateWrapper, radius: float, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesWithRadius(self, radius, clientId):
        """ ExportConnectGeometryTreesWithRadius(self: CDelegateWrapper, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportCreateBasePoint(self, pBasePoint):
        """ ExportCreateBasePoint(self: CDelegateWrapper, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportCreateBentPlateByFaces(self, part1Id, part2Id, face1, face2):
        """ ExportCreateBentPlateByFaces(self: CDelegateWrapper, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByFacesAndRadius(self, part1Id, part2Id, face1, face2, radius):
        """ ExportCreateBentPlateByFacesAndRadius(self: CDelegateWrapper, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t, radius: float) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByParts(self, part1Id, part2Id):
        """ ExportCreateBentPlateByParts(self: CDelegateWrapper, part1Id: int, part2Id: int) -> int """
        pass

    def ExportCreateBentPlateByPartsAndRadius(self, part1Id, part2Id, radius):
        """ ExportCreateBentPlateByPartsAndRadius(self: CDelegateWrapper, part1Id: int, part2Id: int, radius: float) -> int """
        pass

    def ExportCreateBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportCreateBoltGroup(self: CDelegateWrapper, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportCreateBooleanPart(self, pBooleanPart):
        """ ExportCreateBooleanPart(self: CDelegateWrapper, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportCreateClipPlane(self, pView, pClipPlane):
        """ ExportCreateClipPlane(self: CDelegateWrapper, pView: dotView_t, pClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportCreateComponent(self, pBaseComponent):
        """ ExportCreateComponent(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportCreateControlPlane(self, pControlObject):
        """ ExportCreateControlPlane(self: CDelegateWrapper, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportCreateConversionLink(self, pConversionLink):
        """ ExportCreateConversionLink(self: CDelegateWrapper, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportCreateEdgeChamfer(self, pEdgeChamfer):
        """ ExportCreateEdgeChamfer(self: CDelegateWrapper, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportCreateFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportCreateFittingOrCutPlane(self: CDelegateWrapper, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportCreateGrid(self, pGrid):
        """ ExportCreateGrid(self: CDelegateWrapper, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportCreateGridPlane(self, pGridPlane):
        """ ExportCreateGridPlane(self: CDelegateWrapper, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportCreateGuideline(self, pGuideline):
        """ ExportCreateGuideline(self: CDelegateWrapper, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportCreateIFC(self, aIFC):
        """ ExportCreateIFC(self: CDelegateWrapper, aIFC: dotCreateIFCFromModel_t) -> (int, dotCreateIFCFromModel_t) """
        pass

    def ExportCreateLegFace(self, pLegFace):
        """ ExportCreateLegFace(self: CDelegateWrapper, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportCreateLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportCreateLoad(self: CDelegateWrapper, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportCreateLoadGroup(self, pLoadGroup):
        """ ExportCreateLoadGroup(self: CDelegateWrapper, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportCreateNC(self, aNC):
        """ ExportCreateNC(self: CDelegateWrapper, aNC: dotCreateNCFromModel_t) -> (int, dotCreateNCFromModel_t) """
        pass

    def ExportCreateNewModel(self, pInfo):
        """ ExportCreateNewModel(self: CDelegateWrapper, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportCreatePart(self, pPart, contour):
        """ ExportCreatePart(self: CDelegateWrapper, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportCreatePourBreak(self, pPourBreak):
        """ ExportCreatePourBreak(self: CDelegateWrapper, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportCreateRebarEndDetailStrip(self, pStrip):
        """ ExportCreateRebarEndDetailStrip(self: CDelegateWrapper, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportCreateRebarGroup(self, pRebarGroup):
        """ ExportCreateRebarGroup(self: CDelegateWrapper, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportCreateRebarMesh(self, pRebarMesh):
        """ ExportCreateRebarMesh(self: CDelegateWrapper, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportCreateRebarPropertyStrip(self, pStrip):
        """ ExportCreateRebarPropertyStrip(self: CDelegateWrapper, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportCreateRebarSplice(self, pRebarSplice):
        """ ExportCreateRebarSplice(self: CDelegateWrapper, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportCreateRebarSplitter(self, pStrip):
        """ ExportCreateRebarSplitter(self: CDelegateWrapper, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportCreateRebarStrand(self, pRebarStrand):
        """ ExportCreateRebarStrand(self: CDelegateWrapper, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportCreateReferenceModel(self, pReferenceModel):
        """ ExportCreateReferenceModel(self: CDelegateWrapper, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportCreateReferenceModelObjectAttribute(self, pRMOAttribute):
        """ ExportCreateReferenceModelObjectAttribute(self: CDelegateWrapper, pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int, dotReferenceModelObjectAttribute_t) """
        pass

    def ExportCreateReferenceModelObjectAttributeEnumerator(self, pEnumerator):
        """ ExportCreateReferenceModelObjectAttributeEnumerator(self: CDelegateWrapper, pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int, dotReferenceModelObjectAttributeEnumerator_t) """
        pass

    def ExportCreateReport(self, aReport):
        """ ExportCreateReport(self: CDelegateWrapper, aReport: dotCreateReportFromModel_t) -> (int, dotCreateReportFromModel_t) """
        pass

    def ExportCreateSingleRebar(self, pSingleRebar):
        """ ExportCreateSingleRebar(self: CDelegateWrapper, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportCreateSurfaceByFace(self, hitPoint, faceNormal, id):
        """ ExportCreateSurfaceByFace(self: CDelegateWrapper, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceByFaceAndAttrib(self, hitPoint, faceNormal, id, name, surfaceClass):
        """ ExportCreateSurfaceByFaceAndAttrib(self: CDelegateWrapper, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int, name: str, surfaceClass: str) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceObject(self, pSurfaceObject):
        """ ExportCreateSurfaceObject(self: CDelegateWrapper, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportCreateSurfaceTreatment(self, pTreatment):
        """ ExportCreateSurfaceTreatment(self: CDelegateWrapper, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportCreateTask(self, pTask):
        """ ExportCreateTask(self: CDelegateWrapper, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportCreateTaskDependency(self, pTaskDependency):
        """ ExportCreateTaskDependency(self: CDelegateWrapper, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportCreateTaskWorktype(self, pTaskWorktype):
        """ ExportCreateTaskWorktype(self: CDelegateWrapper, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportCreateWeld(self, pWeld):
        """ ExportCreateWeld(self: CDelegateWrapper, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportDasStartAction(self, ActionName, Parameter):
        """ ExportDasStartAction(self: CDelegateWrapper, ActionName: str, Parameter: str) -> int """
        pass

    def ExportDasStartCommand(self, CommandName, Parameter):
        """ ExportDasStartCommand(self: CDelegateWrapper, CommandName: str, Parameter: str) -> int """
        pass

    def ExportDeleteBasePoint(self, pBasePoint):
        """ ExportDeleteBasePoint(self: CDelegateWrapper, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportDeleteClipPlane(self, pView, pClipPlane):
        """ ExportDeleteClipPlane(self: CDelegateWrapper, pView: dotView_t, pClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportDeleteConversionLink(self, pConversionLink):
        """ ExportDeleteConversionLink(self: CDelegateWrapper, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportDeleteObject(self, pIdentifier):
        """ ExportDeleteObject(self: CDelegateWrapper, pIdentifier: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportDisplayAutoDefaultSettings(self, pBaseComponent):
        """ ExportDisplayAutoDefaultSettings(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayComponentHelp(self, pBaseComponent):
        """ ExportDisplayComponentHelp(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayPrompt(self, Message):
        """ ExportDisplayPrompt(self: CDelegateWrapper, Message: str) -> int """
        pass

    def ExportDisplayReport(self, FileName):
        """ ExportDisplayReport(self: CDelegateWrapper, FileName: str) -> int """
        pass

    def ExportDoubleListHandler(self, pDoubleList):
        """ ExportDoubleListHandler(self: CDelegateWrapper, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ExportDrawTemporaryPolygonSurface(self, pArgument):
        """ ExportDrawTemporaryPolygonSurface(self: CDelegateWrapper, pArgument: dotDrawPolygonSurface_t) -> (int, dotDrawPolygonSurface_t) """
        pass

    def ExportDrawTemporaryPolyLine(self, pArgument):
        """ ExportDrawTemporaryPolyLine(self: CDelegateWrapper, pArgument: dotDrawPolyLine_t) -> (int, dotDrawPolyLine_t) """
        pass

    def ExportDrawTemporaryPolyLineWithId(self, pArgument):
        """ ExportDrawTemporaryPolyLineWithId(self: CDelegateWrapper, pArgument: dotGraphicPolyLine_t) -> (int, dotGraphicPolyLine_t) """
        pass

    def ExportDrawTemporaryText(self, pArgument):
        """ ExportDrawTemporaryText(self: CDelegateWrapper, pArgument: dotDrawText_t) -> (int, dotDrawText_t) """
        pass

    def ExportEdgeListHandler(self, pEdgeList):
        """ ExportEdgeListHandler(self: CDelegateWrapper, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ExportEnumerateObjects(self, pEnumerator):
        """ ExportEnumerateObjects(self: CDelegateWrapper, pEnumerator: dotEnumerator_t) -> (int, dotEnumerator_t) """
        pass

    def ExportExtractBentPlateFromComponent(self, partId):
        """ ExportExtractBentPlateFromComponent(self: CDelegateWrapper, partId: int) -> int """
        pass

    def ExportFingerprint(self, pInput, fingerprint):
        """ ExportFingerprint(self: CDelegateWrapper, pInput: dotPolymesh_t, fingerprint: str) -> (int, dotPolymesh_t, str) """
        pass

    def ExportFormatProfile(self, profile):
        """ ExportFormatProfile(self: CDelegateWrapper, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportGetAllProperties(self, pProperties, pNames, pValues):
        """ ExportGetAllProperties(self: CDelegateWrapper, pProperties: dotGetProperties_t, pNames: List[object], pValues: List[object]) -> (int, dotGetProperties_t, List[object], List[object]) """
        pass

    def ExportGetAllReportProperties(self, pProperties):
        """ ExportGetAllReportProperties(self: CDelegateWrapper, pProperties: List[dotGetProperties_t]) -> (int, List[dotGetProperties_t]) """
        pass

    def ExportGetAssociateSurfaces(self, id):
        """ ExportGetAssociateSurfaces(self: CDelegateWrapper, id: int) -> List[int] """
        pass

    def ExportGetBasePoints(self, ClientId):
        """ ExportGetBasePoints(self: CDelegateWrapper, ClientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportGetBentPlateMaximumRadius(self, geometryNodeId, clientId):
        """ ExportGetBentPlateMaximumRadius(self: CDelegateWrapper, geometryNodeId: int, clientId: dotClientId_t) -> (float, dotClientId_t) """
        pass

    def ExportGetBentPlateMinimumRadius(self, partId):
        """ ExportGetBentPlateMinimumRadius(self: CDelegateWrapper, partId: int) -> float """
        pass

    def ExportGetClipPlanes(self, pView, pGetClipPlanes):
        """ ExportGetClipPlanes(self: CDelegateWrapper, pView: dotView_t, pGetClipPlanes: dotGetClipPlanes_t) -> (int, dotView_t, dotGetClipPlanes_t) """
        pass

    def ExportGetColorRepresentationForObject(self, pIdentifier, pColor):
        """ ExportGetColorRepresentationForObject(self: CDelegateWrapper, pIdentifier: dotIdentifier_t, pColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportGetCommandStatus(self, TSCommand, TSCommandParam, Status):
        """ ExportGetCommandStatus(self: CDelegateWrapper, TSCommand: str, TSCommandParam: str, Status: bool) -> (int, str, str, bool) """
        pass

    def ExportGetCommitData(self, pId, pObjectType, pObjectSubType, pCommitType):
        """ ExportGetCommitData(self: CDelegateWrapper, pId: dotIdentifier_t, pObjectType: int, pObjectSubType: int, pCommitType: int) -> (int, dotIdentifier_t, int, int, int) """
        pass

    def ExportGetComponentAttribute(self, pIdentifier, pAttribute):
        """ ExportGetComponentAttribute(self: CDelegateWrapper, pIdentifier: dotIdentifier_t, pAttribute: dotComponentAttribute_t) -> (int, dotIdentifier_t, dotComponentAttribute_t) """
        pass

    def ExportGetComponentInput(self, pObj):
        """ ExportGetComponentInput(self: CDelegateWrapper, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportGetCoordinateSystem(self, pModelObject, pCoordinateSystem):
        """ ExportGetCoordinateSystem(self: CDelegateWrapper, pModelObject: dotModelObject_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotModelObject_t, dotCoordinateSystem_t) """
        pass

    def ExportGetCutSolidSerialized(self, dotSolid1, dotSolid2, serializedFaceList, serializedVectorList, serializedFaceOriginPartIdList, serializedShellIndexList, serializedEdgeVertexList, serializedEdgeTypeList, serializedEdgeShellIndexList):
        """ ExportGetCutSolidSerialized(self: CDelegateWrapper, dotSolid1: dotSolid_t, dotSolid2: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedFaceOriginPartIdList: List[int], serializedShellIndexList: List[int], serializedEdgeVertexList: List[dotPoint_t], serializedEdgeTypeList: List[int], serializedEdgeShellIndexList: List[int]) -> (int, dotSolid_t, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetDatabaseVersion(self, Version):
        """ ExportGetDatabaseVersion(self: CDelegateWrapper, Version: int) -> (int, int) """
        pass

    def ExportGetDataBaseVersionInfoFromModel(self, pInfo):
        """ ExportGetDataBaseVersionInfoFromModel(self: CDelegateWrapper, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetDetectedClash(self, pClash):
        """ ExportGetDetectedClash(self: CDelegateWrapper, pClash: dotClash_t) -> (int, dotClash_t) """
        pass

    def ExportGetDotType(self, pModelObject):
        """ ExportGetDotType(self: CDelegateWrapper, pModelObject: dotModelObject_t) -> (int, dotModelObject_t) """
        pass

    def ExportGetFatherComponent(self, ObjectId, FatherComponentId):
        """ ExportGetFatherComponent(self: CDelegateWrapper, ObjectId: int, FatherComponentId: int) -> (int, int) """
        pass

    def ExportGetIntersectionBoundingBoxes(self, Identifier1, Identifier2, ClientId):
        """ ExportGetIntersectionBoundingBoxes(self: CDelegateWrapper, Identifier1: dotIdentifier_t, Identifier2: dotIdentifier_t, ClientId: dotClientId_t) -> (int, dotIdentifier_t, dotIdentifier_t, dotClientId_t) """
        pass

    def ExportGetIntersectionPoints(self, pIntersectionPoints):
        """ ExportGetIntersectionPoints(self: CDelegateWrapper, pIntersectionPoints: dotIntersectionPoints_t) -> (int, dotIntersectionPoints_t) """
        pass

    def ExportGetIntersectionSolid(self, pSolid):
        """ ExportGetIntersectionSolid(self: CDelegateWrapper, pSolid: dotIntersectionSolid_t) -> (int, dotIntersectionSolid_t) """
        pass

    def ExportGetModificationStamp(self, pModStmp):
        """ ExportGetModificationStamp(self: CDelegateWrapper, pModStmp: dotModificationStamp_t) -> (int, dotModificationStamp_t) """
        pass

    def ExportGetModificationStampGuid(self, pModStmp):
        """ ExportGetModificationStampGuid(self: CDelegateWrapper, pModStmp: str) -> (int, str) """
        pass

    def ExportGetNumberingUpToDate(self, pNumberingQuery):
        """ ExportGetNumberingUpToDate(self: CDelegateWrapper, pNumberingQuery: dotNumberingQuery_t) -> (int, dotNumberingQuery_t) """
        pass

    def ExportGetNumberOfClashes(self, pClashes):
        """ ExportGetNumberOfClashes(self: CDelegateWrapper, pClashes: int) -> (int, int) """
        pass

    def ExportGetObjectLastModified(self, pIdentifier, pTime, pLocallyModified):
        """ ExportGetObjectLastModified(self: CDelegateWrapper, pIdentifier: dotIdentifier_t, pTime: int, pLocallyModified: bool) -> (int, dotIdentifier_t, int, bool) """
        pass

    def ExportGetObjectPhase(self, pArgument):
        """ ExportGetObjectPhase(self: CDelegateWrapper, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportGetParentObject(self, surfaceId):
        """ ExportGetParentObject(self: CDelegateWrapper, surfaceId: int) -> int """
        pass

    def ExportGetPartLine(self, pPartLine):
        """ ExportGetPartLine(self: CDelegateWrapper, pPartLine: dotPartLine_t) -> (int, dotPartLine_t) """
        pass

    def ExportGetPartMark(self, pPartMark):
        """ ExportGetPartMark(self: CDelegateWrapper, pPartMark: dotPartMark_t) -> (int, dotPartMark_t) """
        pass

    def ExportGetPhaseNumbers(self, pArgument):
        """ ExportGetPhaseNumbers(self: CDelegateWrapper, pArgument: dotPhaseNumbers_t) -> (int, dotPhaseNumbers_t) """
        pass

    def ExportGetPlane(self, pPlane):
        """ ExportGetPlane(self: CDelegateWrapper, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportGetPolybeamCoordinateSystem(self, Id, SubId, Chamfered, pX, pY, pZ):
        """ ExportGetPolybeamCoordinateSystem(self: CDelegateWrapper, Id: int, SubId: int, Chamfered: int, pX: dotPoint_t, pY: dotPoint_t, pZ: dotPoint_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t) """
        pass

    def ExportGetProjectInfo(self, pInfo):
        """ ExportGetProjectInfo(self: CDelegateWrapper, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportGetProperties(self, pProperties):
        """ ExportGetProperties(self: CDelegateWrapper, pProperties: dotGetProperties_t) -> (int, dotGetProperties_t) """
        pass

    def ExportGetReferenceModelObjectByExternalGuid(self, referenceModelId, externalGuid):
        """ ExportGetReferenceModelObjectByExternalGuid(self: CDelegateWrapper, referenceModelId: int, externalGuid: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportGetReferenceModelRevisionIds(self, pReferenceModel, ClientId):
        """ ExportGetReferenceModelRevisionIds(self: CDelegateWrapper, pReferenceModel: dotReferenceModel_t, ClientId: dotClientId_t) -> (int, dotReferenceModel_t, dotClientId_t) """
        pass

    def ExportGetSetModelInfo(self, pInfo):
        """ ExportGetSetModelInfo(self: CDelegateWrapper, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetSetModstamp(self, ModStampData):
        """ ExportGetSetModstamp(self: CDelegateWrapper, ModStampData: dotModStamp_t) -> (int, dotModStamp_t) """
        pass

    def ExportGetSnapshotFromDatabase(self, Enumerator, SelectInstances):
        """ ExportGetSnapshotFromDatabase(self: CDelegateWrapper, Enumerator: dotEnumerator_t, SelectInstances: bool) -> (Serializable[List[ModelObject]], dotEnumerator_t) """
        pass

    def ExportGetSolid(self, pSolid):
        """ ExportGetSolid(self: CDelegateWrapper, pSolid: dotSolid_t) -> (int, dotSolid_t) """
        pass

    def ExportGetSolidBrep(self, polymeshToClean, polymeshCleaned):
        """ ExportGetSolidBrep(self: CDelegateWrapper, polymeshToClean: dotPolymesh_t, polymeshCleaned: dotPolymesh_t) -> (bool, dotPolymesh_t, dotPolymesh_t) """
        pass

    def ExportGetSolidMerged(self, dotSolid, polymeshes):
        """ ExportGetSolidMerged(self: CDelegateWrapper, dotSolid: dotSolid_t, polymeshes: dotPolymesh_t) -> (int, dotSolid_t, dotPolymesh_t) """
        pass

    def ExportGetSolidSerialized(self, dotSolid, serializedFaceList, serializedVectorList, serializedShellIndexList, serializedFaceOriginIdList):
        """ ExportGetSolidSerialized(self: CDelegateWrapper, dotSolid: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedShellIndexList: List[int], serializedFaceOriginIdList: List[int]) -> (int, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetStringPropertyFromDatabase(self, pProperty, stringValues):
        """ ExportGetStringPropertyFromDatabase(self: CDelegateWrapper, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportGetSurfaceGeometryType(self, surfaceId):
        """ ExportGetSurfaceGeometryType(self: CDelegateWrapper, surfaceId: int) -> int """
        pass

    def ExportGetTrackEvent(self, category, eventName, eventContent):
        """ ExportGetTrackEvent(self: CDelegateWrapper, category: str, eventName: str, eventContent: str) -> (int, str, str, str) """
        pass

    def ExportGetTransformationPlane(self, pPlane):
        """ ExportGetTransformationPlane(self: CDelegateWrapper, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportGetViewCamera(self, pView, pCamera):
        """ ExportGetViewCamera(self: CDelegateWrapper, pView: dotView_t, pCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportGetViews(self, pViews):
        """ ExportGetViews(self: CDelegateWrapper, pViews: dotViewSelector_t) -> (int, dotViewSelector_t) """
        pass

    def ExportGetWeldGeometry(self, pWeldGeometry):
        """ ExportGetWeldGeometry(self: CDelegateWrapper, pWeldGeometry: dotWeldGeometry_t) -> (int, dotWeldGeometry_t) """
        pass

    def ExportGetWriteOutStampGuid(self, pModStmp):
        """ ExportGetWriteOutStampGuid(self: CDelegateWrapper, pModStmp: str) -> (int, str) """
        pass

    def ExportHierarchicDefinition(self, pHierarchicDefinition):
        """ ExportHierarchicDefinition(self: CDelegateWrapper, pHierarchicDefinition: dotHierarchicDefinition_t) -> (int, dotHierarchicDefinition_t) """
        pass

    def ExportHierarchicObject(self, pHierarchicObject):
        """ ExportHierarchicObject(self: CDelegateWrapper, pHierarchicObject: dotHierarchicObject_t) -> (int, dotHierarchicObject_t) """
        pass

    def ExportHierarchicObjectChildrenOperation(self, pHierarchicList):
        """ ExportHierarchicObjectChildrenOperation(self: CDelegateWrapper, pHierarchicList: dotHierarchicList_t) -> (int, dotHierarchicList_t) """
        pass

    def ExportInitializeComponentStacks(self):
        """ ExportInitializeComponentStacks(self: CDelegateWrapper) -> int """
        pass

    def ExportInsertView(self, pDotView):
        """ ExportInsertView(self: CDelegateWrapper, pDotView: dotView_t) -> (int, dotView_t) """
        pass

    def ExportIntListHandler(self, pIntList):
        """ ExportIntListHandler(self: CDelegateWrapper, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ExportLoadComponentAttributes(self, pBaseComponent):
        """ ExportLoadComponentAttributes(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportManipulateObject(self, pArgument):
        """ ExportManipulateObject(self: CDelegateWrapper, pArgument: dotManipulateObject_t) -> (int, dotManipulateObject_t) """
        pass

    def ExportModifyAssembly(self, pAssembly):
        """ ExportModifyAssembly(self: CDelegateWrapper, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportModifyBasePoint(self, pBasePoint):
        """ ExportModifyBasePoint(self: CDelegateWrapper, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportModifyBentPlate(self, pPart):
        """ ExportModifyBentPlate(self: CDelegateWrapper, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportModifyBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportModifyBoltGroup(self: CDelegateWrapper, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportModifyBooleanPart(self, pBooleanPart):
        """ ExportModifyBooleanPart(self: CDelegateWrapper, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportModifyClipPlane(self, pView, pClipPlane):
        """ ExportModifyClipPlane(self: CDelegateWrapper, pView: dotView_t, pClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportModifyComponent(self, pBaseComponent):
        """ ExportModifyComponent(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportModifyControlPlane(self, pControlObject):
        """ ExportModifyControlPlane(self: CDelegateWrapper, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportModifyCylindricalSurfaceNode(self, geometryNodeId, surfacePoints, clientId):
        """ ExportModifyCylindricalSurfaceNode(self: CDelegateWrapper, geometryNodeId: int, surfacePoints: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyEdgeChamfer(self, pEdgeChamfer):
        """ ExportModifyEdgeChamfer(self: CDelegateWrapper, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportModifyFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportModifyFittingOrCutPlane(self: CDelegateWrapper, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeCurveType(self, geometryNodeId, newCurveType, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: CDelegateWrapper, geometryNodeId: int, newCurveType: int, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeRadius(self, geometryNodeId, radius, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeRadius(self: CDelegateWrapper, geometryNodeId: int, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreePolygonNode(self, geometryNodeId, contour, clientId):
        """ ExportModifyGeometryTreePolygonNode(self: CDelegateWrapper, geometryNodeId: int, contour: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyGrid(self, pGrid):
        """ ExportModifyGrid(self: CDelegateWrapper, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportModifyGridPlane(self, pGridPlane):
        """ ExportModifyGridPlane(self: CDelegateWrapper, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportModifyLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportModifyLoad(self: CDelegateWrapper, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportModifyLoadGroup(self, pLoadGroup):
        """ ExportModifyLoadGroup(self: CDelegateWrapper, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportModifyPart(self, pPart, contour):
        """ ExportModifyPart(self: CDelegateWrapper, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportModifyPourBreak(self, pPourBreak):
        """ ExportModifyPourBreak(self: CDelegateWrapper, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportModifyPourObject(self, pPourObject):
        """ ExportModifyPourObject(self: CDelegateWrapper, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportModifyProjectInfo(self, pInfo):
        """ ExportModifyProjectInfo(self: CDelegateWrapper, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportModifyRebarEndDetailStrip(self, pStrip):
        """ ExportModifyRebarEndDetailStrip(self: CDelegateWrapper, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportModifyRebarGroup(self, pRebarGroup):
        """ ExportModifyRebarGroup(self: CDelegateWrapper, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportModifyRebarMesh(self, pRebarMesh):
        """ ExportModifyRebarMesh(self: CDelegateWrapper, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportModifyRebarPropertyStrip(self, pStrip):
        """ ExportModifyRebarPropertyStrip(self: CDelegateWrapper, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportModifyRebarSplice(self, pRebarSplice):
        """ ExportModifyRebarSplice(self: CDelegateWrapper, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportModifyRebarSplitter(self, pStrip):
        """ ExportModifyRebarSplitter(self: CDelegateWrapper, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportModifyRebarStrand(self, pRebarStrand):
        """ ExportModifyRebarStrand(self: CDelegateWrapper, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportModifyReferenceModel(self, pReferenceModel):
        """ ExportModifyReferenceModel(self: CDelegateWrapper, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportModifySingleRebar(self, pSingleRebar):
        """ ExportModifySingleRebar(self: CDelegateWrapper, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportModifySurfaceObject(self, pSurfaceObject):
        """ ExportModifySurfaceObject(self: CDelegateWrapper, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportModifySurfaceTreatment(self, pTreatment):
        """ ExportModifySurfaceTreatment(self: CDelegateWrapper, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportModifyTask(self, pTask):
        """ ExportModifyTask(self: CDelegateWrapper, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportModifyTaskDependency(self, pTaskDependency):
        """ ExportModifyTaskDependency(self: CDelegateWrapper, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportModifyTaskWorktype(self, pTaskWorktype):
        """ ExportModifyTaskWorktype(self: CDelegateWrapper, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportModifyView(self, pDotView):
        """ ExportModifyView(self: CDelegateWrapper, pDotView: dotView_t) -> (int, dotView_t) """
        pass

    def ExportModifyWeld(self, pWeld):
        """ ExportModifyWeld(self: CDelegateWrapper, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportModStampCompare(self, ModStampCompare):
        """ ExportModStampCompare(self: CDelegateWrapper, ModStampCompare: dotModStampCompare_t) -> (int, dotModStampCompare_t) """
        pass

    def ExportObjectMatchesToFilter(self, pObjectId, FileName):
        """ ExportObjectMatchesToFilter(self: CDelegateWrapper, pObjectId: dotIdentifier_t, FileName: str) -> (int, dotIdentifier_t) """
        pass

    def ExportParseProfile(self, profile):
        """ ExportParseProfile(self: CDelegateWrapper, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportPointListHandler(self, pPointList):
        """ ExportPointListHandler(self: CDelegateWrapper, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ExportProgressBarOperation(self, pProgressBar):
        """ ExportProgressBarOperation(self: CDelegateWrapper, pProgressBar: dotProgressBar_t) -> (int, dotProgressBar_t) """
        pass

    def ExportRebarSetAdditionFunction(self, action, pRebarSetAddition):
        """ ExportRebarSetAdditionFunction(self: CDelegateWrapper, action: RebarSetAction, pRebarSetAddition: dotRebarSetAddition_t) -> (int, dotRebarSetAddition_t) """
        pass

    def ExportRebarSetFunction(self, action, pRebarSet):
        """ ExportRebarSetFunction(self: CDelegateWrapper, action: RebarSetAction, pRebarSet: dotRebarSet_t) -> (int, dotRebarSet_t) """
        pass

    def ExportRefreshReferenceFile(self, pReferenceModel):
        """ ExportRefreshReferenceFile(self: CDelegateWrapper, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportRemoveFromPourUnit(self, clientId):
        """ ExportRemoveFromPourUnit(self: CDelegateWrapper, clientId: dotClientId_t) -> (bool, dotClientId_t) """
        pass

    def ExportRemoveTemporaryGraphicsObjects(self, pArgument):
        """ ExportRemoveTemporaryGraphicsObjects(self: CDelegateWrapper, pArgument: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportRunMacro(self, FileName):
        """ ExportRunMacro(self: CDelegateWrapper, FileName: str) -> int """
        pass

    def ExportRunOrStopClashCheck(self, RunningClashCheck):
        """ ExportRunOrStopClashCheck(self: CDelegateWrapper, RunningClashCheck: bool) -> int """
        pass

    def ExportSaveAsWebModel(self, pSaveAsWebModel):
        """ ExportSaveAsWebModel(self: CDelegateWrapper, pSaveAsWebModel: dotSaveAsWebModel_t) -> (int, dotSaveAsWebModel_t) """
        pass

    def ExportSaveOperation(self, pOperation):
        """ ExportSaveOperation(self: CDelegateWrapper, pOperation: dotSaveOperation_t) -> (int, dotSaveOperation_t) """
        pass

    def ExportSelectAssembly(self, pAssembly):
        """ ExportSelectAssembly(self: CDelegateWrapper, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportSelectBasePoint(self, guid, pBasePoint):
        """ ExportSelectBasePoint(self: CDelegateWrapper, guid: str, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportSelectBentPlate(self, pPart):
        """ ExportSelectBentPlate(self: CDelegateWrapper, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportSelectBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportSelectBoltGroup(self: CDelegateWrapper, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportSelectBooleanPart(self, pBooleanPart):
        """ ExportSelectBooleanPart(self: CDelegateWrapper, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportSelectComponent(self, pBaseComponent):
        """ ExportSelectComponent(self: CDelegateWrapper, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportSelectControlPlane(self, pControlObject):
        """ ExportSelectControlPlane(self: CDelegateWrapper, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportSelectConversionLink(self, pConversionLink):
        """ ExportSelectConversionLink(self: CDelegateWrapper, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportSelectEdgeChamfer(self, pEdgeChamfer):
        """ ExportSelectEdgeChamfer(self: CDelegateWrapper, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportSelectFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportSelectFittingOrCutPlane(self: CDelegateWrapper, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportSelectGrid(self, pGrid):
        """ ExportSelectGrid(self: CDelegateWrapper, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportSelectGridPlane(self, pGridPlane):
        """ ExportSelectGridPlane(self: CDelegateWrapper, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportSelectGuideline(self, pGuideline):
        """ ExportSelectGuideline(self: CDelegateWrapper, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportSelectLegFace(self, pLegFace):
        """ ExportSelectLegFace(self: CDelegateWrapper, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportSelectLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportSelectLoad(self: CDelegateWrapper, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportSelectLoadGroup(self, pLoadGroup):
        """ ExportSelectLoadGroup(self: CDelegateWrapper, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportSelectPart(self, pPart, contour):
        """ ExportSelectPart(self: CDelegateWrapper, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportSelectPourBreak(self, pPourBreak):
        """ ExportSelectPourBreak(self: CDelegateWrapper, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportSelectPourObject(self, pPourObject):
        """ ExportSelectPourObject(self: CDelegateWrapper, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportSelectRebarBars(self, pWire):
        """ ExportSelectRebarBars(self: CDelegateWrapper, pWire: dotWire_t) -> (int, dotWire_t) """
        pass

    def ExportSelectRebarEndDetailStrip(self, pStrip):
        """ ExportSelectRebarEndDetailStrip(self: CDelegateWrapper, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportSelectRebarGroup(self, pRebarGroup):
        """ ExportSelectRebarGroup(self: CDelegateWrapper, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportSelectRebarMesh(self, pRebarMesh):
        """ ExportSelectRebarMesh(self: CDelegateWrapper, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportSelectRebarPropertyStrip(self, pStrip):
        """ ExportSelectRebarPropertyStrip(self: CDelegateWrapper, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportSelectRebarSplice(self, pRebarSplice):
        """ ExportSelectRebarSplice(self: CDelegateWrapper, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportSelectRebarSplitter(self, pStrip):
        """ ExportSelectRebarSplitter(self: CDelegateWrapper, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportSelectRebarStrand(self, pRebarStrand):
        """ ExportSelectRebarStrand(self: CDelegateWrapper, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportSelectReferenceModel(self, pReferenceModel):
        """ ExportSelectReferenceModel(self: CDelegateWrapper, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportSelectReferenceModelObject(self, pReferenceModelObject):
        """ ExportSelectReferenceModelObject(self: CDelegateWrapper, pReferenceModelObject: dotReferenceModelObject_t) -> (int, dotReferenceModelObject_t) """
        pass

    def ExportSelectReferenceModelRevision(self, modelId, revisionId, pRevision):
        """ ExportSelectReferenceModelRevision(self: CDelegateWrapper, modelId: int, revisionId: int, pRevision: dotReferenceModelRevision_t) -> (int, dotReferenceModelRevision_t) """
        pass

    def ExportSelectSingleRebar(self, pSingleRebar):
        """ ExportSelectSingleRebar(self: CDelegateWrapper, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportSelectSurfaceObject(self, pSurfaceObject):
        """ ExportSelectSurfaceObject(self: CDelegateWrapper, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportSelectSurfaceTreatment(self, pTreatment):
        """ ExportSelectSurfaceTreatment(self: CDelegateWrapper, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportSelectTask(self, pTask):
        """ ExportSelectTask(self: CDelegateWrapper, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportSelectTaskDependency(self, pTaskDependency):
        """ ExportSelectTaskDependency(self: CDelegateWrapper, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportSelectTaskWorktype(self, pTaskWorktype):
        """ ExportSelectTaskWorktype(self: CDelegateWrapper, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportSelectView(self, pDotView):
        """ ExportSelectView(self: CDelegateWrapper, pDotView: dotView_t) -> (int, dotView_t) """
        pass

    def ExportSelectWeld(self, pWeld):
        """ ExportSelectWeld(self: CDelegateWrapper, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportSetAdvancedOption(self, pArgument):
        """ ExportSetAdvancedOption(self: CDelegateWrapper, pArgument: dotGetAdvancedOption_t) -> (int, dotGetAdvancedOption_t) """
        pass

    def ExportSetAsCurrentRevision(self, modelId, revisionId):
        """ ExportSetAsCurrentRevision(self: CDelegateWrapper, modelId: int, revisionId: int) -> int """
        pass

    def ExportSetGetPhaseProperty(self, pArgument):
        """ ExportSetGetPhaseProperty(self: CDelegateWrapper, pArgument: dotSetGetProperty_t) -> (int, dotSetGetProperty_t) """
        pass

    def ExportSetObjectPhase(self, pArgument):
        """ ExportSetObjectPhase(self: CDelegateWrapper, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportSetPlane(self, pPlane):
        """ ExportSetPlane(self: CDelegateWrapper, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportSetProperty(self, pProperty):
        """ ExportSetProperty(self: CDelegateWrapper, pProperty: dotSetProperty_t) -> (int, dotSetProperty_t) """
        pass

    def ExportSetRepresentation(self, pViews):
        """ ExportSetRepresentation(self: CDelegateWrapper, pViews: str) -> int """
        pass

    def ExportSetStringPropertyToDatabase(self, pProperty, stringValues):
        """ ExportSetStringPropertyToDatabase(self: CDelegateWrapper, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportSetTemporaryColor(self, pObjectId, pNewColor):
        """ ExportSetTemporaryColor(self: CDelegateWrapper, pObjectId: dotIdentifier_t, pNewColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportSetTemporaryColors(self, pSetTemporaryColors):
        """ ExportSetTemporaryColors(self: CDelegateWrapper, pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryColors_FAST(self, pObjects, pSetTemporaryColors):
        """ ExportSetTemporaryColors_FAST(self: CDelegateWrapper, pObjects: List[Identifier], pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, List[Identifier], dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryState(self, pObjectId, pNewState):
        """ ExportSetTemporaryState(self: CDelegateWrapper, pObjectId: dotIdentifier_t, pNewState: dotTemporaryStatesEnum) -> (int, dotIdentifier_t, dotTemporaryStatesEnum) """
        pass

    def ExportSetTemporaryStates(self, pSetTemporaryStates):
        """ ExportSetTemporaryStates(self: CDelegateWrapper, pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, dotSetTemporaryStates_t) """
        pass

    def ExportSetTemporaryStates_FAST(self, pObjects, pSetTemporaryStates):
        """ ExportSetTemporaryStates_FAST(self: CDelegateWrapper, pObjects: List[Identifier], pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, List[Identifier], dotSetTemporaryStates_t) """
        pass

    def ExportSetTransformationPlane(self, pPlane):
        """ ExportSetTransformationPlane(self: CDelegateWrapper, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportSetViewCamera(self, pView, pCamera):
        """ ExportSetViewCamera(self: CDelegateWrapper, pView: dotView_t, pCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportShadowArea(self, pArgument):
        """ ExportShadowArea(self: CDelegateWrapper, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportShadowAreaComplement(self, pArgument):
        """ ExportShadowAreaComplement(self: CDelegateWrapper, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportSharingOperation(self, pOperation):
        """ ExportSharingOperation(self: CDelegateWrapper, pOperation: dotSharingOperation_t) -> (int, dotSharingOperation_t) """
        pass

    def ExportSingleRebarGetRebarSet(self, singleRebarId):
        """ ExportSingleRebarGetRebarSet(self: CDelegateWrapper, singleRebarId: int) -> int """
        pass

    def ExportStartCustomComponentCreation(self, ComponentName):
        """ ExportStartCustomComponentCreation(self: CDelegateWrapper, ComponentName: str) -> int """
        pass

    def ExportStartPluginCreation(self, ComponentName):
        """ ExportStartPluginCreation(self: CDelegateWrapper, ComponentName: str) -> int """
        pass

    def ExportStringListHandler(self, pStringList):
        """ ExportStringListHandler(self: CDelegateWrapper, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
        pass

    def ExportTaskObjectAttach(self, pSelector):
        """ ExportTaskObjectAttach(self: CDelegateWrapper, pSelector: dotTaskObjectAttacher_t) -> (int, dotTaskObjectAttacher_t) """
        pass

    def ExportUIObjectPick(self, pPicker):
        """ ExportUIObjectPick(self: CDelegateWrapper, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUIObjectSelect(self, pSelector):
        """ ExportUIObjectSelect(self: CDelegateWrapper, pSelector: dotUIModelObjectSelector_t) -> (int, dotUIModelObjectSelector_t) """
        pass

    def ExportUIObjectsPick(self, pPicker):
        """ ExportUIObjectsPick(self: CDelegateWrapper, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUndoOperation(self, pOperation):
        """ ExportUndoOperation(self: CDelegateWrapper, pOperation: dotUndoOperation_t) -> (int, dotUndoOperation_t) """
        pass

    def ExportValidatePolymesh(self, checkCriteria, polymeshToValidate, invalidInfo):
        """ ExportValidatePolymesh(self: CDelegateWrapper, checkCriteria: int, polymeshToValidate: dotPolymesh_t, invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool, dotPolymesh_t, dotPolymeshValidateInvalidInfo_t) """
        pass

    def ExportViewHideUnselected(self, HideCompletely, DrawAsStick):
        """ ExportViewHideUnselected(self: CDelegateWrapper, HideCompletely: bool, DrawAsStick: bool) -> int """
        pass

    def ExportWriteToSessionLog(self, Message):
        """ ExportWriteToSessionLog(self: CDelegateWrapper, Message: str) -> int """
        pass

    def GetDSTVCoordinateSystem(self, PartId, pCoordinateSystem):
        """ GetDSTVCoordinateSystem(self: CDelegateWrapper, PartId: dotIdentifier_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotCoordinateSystem_t) """
        pass

    def ImportDoubleListHandler(self, pDoubleList):
        """ ImportDoubleListHandler(self: CDelegateWrapper, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ImportEdgeListHandler(self, pEdgeList):
        """ ImportEdgeListHandler(self: CDelegateWrapper, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ImportIntListHandler(self, pIntList):
        """ ImportIntListHandler(self: CDelegateWrapper, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ImportPointListHandler(self, pPointList):
        """ ImportPointListHandler(self: CDelegateWrapper, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ImportStringListHandler(self, pStringList):
        """ ImportStringListHandler(self: CDelegateWrapper, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
        pass

    def IsMacroRunning(self):
        """ IsMacroRunning(self: CDelegateWrapper) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, instance, functionality):
        """ __new__(cls: type, instance: ICDelegate, functionality: WrapperFunctionalityBase) """
        pass

    _functionality = None
    _instance = None


class ChangeManager(object):
    """ ChangeManager() """
    def AllowNumbering(self, NumberingFlag):
        """ AllowNumbering(self: ChangeManager, NumberingFlag: bool) -> bool """
        pass

    def AllowSave(self, SaveFlag):
        """ AllowSave(self: ChangeManager, SaveFlag: bool) -> bool """
        pass


class ConversionLink(object):
    """ ConversionLink(partId: int) """
    def Delete(self):
        """ Delete(self: ConversionLink) -> bool """
        pass

    def Insert(self):
        """ Insert(self: ConversionLink) -> bool """
        pass

    def Modify(self):
        """ Modify(self: ConversionLink) -> bool """
        pass

    def Select(self):
        """ Select(self: ConversionLink) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, partId):
        """ __new__(cls: type, partId: int) """
        pass

    ApprovalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalStatus(self: ConversionLink) -> ApprovalStatusEnum

Set: ApprovalStatus(self: ConversionLink) = value
"""

    ConversionStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConversionStatus(self: ConversionLink) -> ConversionStatusEnum

Set: ConversionStatus(self: ConversionLink) = value
"""

    PartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartId(self: ConversionLink) -> int

"""

    RefModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefModelId(self: ConversionLink) -> int

Set: RefModelId(self: ConversionLink) = value
"""

    RefModelObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefModelObjectId(self: ConversionLink) -> int

Set: RefModelObjectId(self: ConversionLink) = value
"""


    ApprovalStatusEnum = None
    ConversionStatusEnum = None


class DelegateFake(object):
    """ DelegateFake() """
    def EditMacro(self, FileName):
        """ EditMacro(self: DelegateFake, FileName: str) -> int """
        pass

    def ExplodeBentPlate(self, partId):
        """ ExplodeBentPlate(self: DelegateFake, partId: int) -> int """
        pass

    def ExportAddComponentAttributeToStack(self, pAttr):
        """ ExportAddComponentAttributeToStack(self: DelegateFake, pAttr: dotComponentAttribute_t) -> (int, dotComponentAttribute_t) """
        pass

    def ExportAddComponentInputToStack(self, pObj):
        """ ExportAddComponentInputToStack(self: DelegateFake, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportAddToPourUnit(self, inputPour, clientId):
        """ ExportAddToPourUnit(self: DelegateFake, inputPour: dotPourObject_t, clientId: dotClientId_t) -> (bool, dotPourObject_t, dotClientId_t) """
        pass

    def ExportAutoConnectSetupConnectionBrowserCB(self, elementNumber):
        """ ExportAutoConnectSetupConnectionBrowserCB(self: DelegateFake, elementNumber: int) -> int """
        pass

    def ExportCalculateContourPolygon(self, pContour, pPolygon):
        """ ExportCalculateContourPolygon(self: DelegateFake, pContour: dotContour_t, pPolygon: dotPolygon_t) -> (int, dotContour_t, dotPolygon_t) """
        pass

    def ExportCalculatePourUnits(self):
        """ ExportCalculatePourUnits(self: DelegateFake) -> bool """
        pass

    def ExportChangeManagerAllowNumbering(self, NumberingFlag):
        """ ExportChangeManagerAllowNumbering(self: DelegateFake, NumberingFlag: bool) -> int """
        pass

    def ExportChangeManagerAllowSave(self, SaveFlag):
        """ ExportChangeManagerAllowSave(self: DelegateFake, SaveFlag: bool) -> int """
        pass

    def ExportCleanDrawingFiles(self, Silent, BackupPath):
        """ ExportCleanDrawingFiles(self: DelegateFake, Silent: bool, BackupPath: str) -> int """
        pass

    def ExportClearAllTemporaryStates(self):
        """ ExportClearAllTemporaryStates(self: DelegateFake) -> int """
        pass

    def ExportClearTemporaryState(self, pObjectId):
        """ ExportClearTemporaryState(self: DelegateFake, pObjectId: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportCommitChanges(self, pModelCommit):
        """ ExportCommitChanges(self: DelegateFake, pModelCommit: dotModelCommit_t) -> (int, dotModelCommit_t) """
        pass

    def ExportCompareFingerprints(self, fingerprint1, fingerprint2):
        """ ExportCompareFingerprints(self: DelegateFake, fingerprint1: str, fingerprint2: str) -> bool """
        pass

    def ExportCompareObjects(self, ObjectId, ObjectToCompareId):
        """ ExportCompareObjects(self: DelegateFake, ObjectId: int, ObjectToCompareId: int) -> int """
        pass

    def ExportConnectGeometryTrees(self, clientId):
        """ ExportConnectGeometryTrees(self: DelegateFake, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPoints(self, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPoints(self: DelegateFake, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPointsWithRadius(self, radius, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPointsWithRadius(self: DelegateFake, radius: float, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesWithRadius(self, radius, clientId):
        """ ExportConnectGeometryTreesWithRadius(self: DelegateFake, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportCreateBasePoint(self, pBasePoint):
        """ ExportCreateBasePoint(self: DelegateFake, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportCreateBentPlateByFaces(self, part1Id, part2Id, face1, face2):
        """ ExportCreateBentPlateByFaces(self: DelegateFake, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByFacesAndRadius(self, part1Id, part2Id, face1, face2, radius):
        """ ExportCreateBentPlateByFacesAndRadius(self: DelegateFake, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t, radius: float) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByParts(self, part1Id, part2Id):
        """ ExportCreateBentPlateByParts(self: DelegateFake, part1Id: int, part2Id: int) -> int """
        pass

    def ExportCreateBentPlateByPartsAndRadius(self, part1Id, part2Id, radius):
        """ ExportCreateBentPlateByPartsAndRadius(self: DelegateFake, part1Id: int, part2Id: int, radius: float) -> int """
        pass

    def ExportCreateBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportCreateBoltGroup(self: DelegateFake, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportCreateBooleanPart(self, pBooleanPart):
        """ ExportCreateBooleanPart(self: DelegateFake, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportCreateClipPlane(self, pDotView, pDotClipPlane):
        """ ExportCreateClipPlane(self: DelegateFake, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportCreateComponent(self, pBaseComponent):
        """ ExportCreateComponent(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportCreateControlPlane(self, pControlObject):
        """ ExportCreateControlPlane(self: DelegateFake, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportCreateConversionLink(self, pConversionLink):
        """ ExportCreateConversionLink(self: DelegateFake, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportCreateEdgeChamfer(self, pEdgeChamfer):
        """ ExportCreateEdgeChamfer(self: DelegateFake, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportCreateFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportCreateFittingOrCutPlane(self: DelegateFake, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportCreateGrid(self, pGrid):
        """ ExportCreateGrid(self: DelegateFake, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportCreateGridPlane(self, pGridPlane):
        """ ExportCreateGridPlane(self: DelegateFake, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportCreateGuideline(self, pGuideline):
        """ ExportCreateGuideline(self: DelegateFake, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportCreateIFC(self, aIFC):
        """ ExportCreateIFC(self: DelegateFake, aIFC: dotCreateIFCFromModel_t) -> (int, dotCreateIFCFromModel_t) """
        pass

    def ExportCreateLegFace(self, pLegFace):
        """ ExportCreateLegFace(self: DelegateFake, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportCreateLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportCreateLoad(self: DelegateFake, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportCreateLoadGroup(self, pLoadGroup):
        """ ExportCreateLoadGroup(self: DelegateFake, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportCreateNC(self, aNC):
        """ ExportCreateNC(self: DelegateFake, aNC: dotCreateNCFromModel_t) -> (int, dotCreateNCFromModel_t) """
        pass

    def ExportCreateNewModel(self, pInfo):
        """ ExportCreateNewModel(self: DelegateFake, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportCreatePart(self, pPart, contour):
        """ ExportCreatePart(self: DelegateFake, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportCreatePourBreak(self, pPolymesh):
        """ ExportCreatePourBreak(self: DelegateFake, pPolymesh: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportCreateRebarEndDetailStrip(self, pStrip):
        """ ExportCreateRebarEndDetailStrip(self: DelegateFake, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportCreateRebarGroup(self, pRebarGroup):
        """ ExportCreateRebarGroup(self: DelegateFake, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportCreateRebarMesh(self, pRebarMesh):
        """ ExportCreateRebarMesh(self: DelegateFake, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportCreateRebarPropertyStrip(self, pStrip):
        """ ExportCreateRebarPropertyStrip(self: DelegateFake, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportCreateRebarSplice(self, pRebarSplice):
        """ ExportCreateRebarSplice(self: DelegateFake, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportCreateRebarSplitter(self, pStrip):
        """ ExportCreateRebarSplitter(self: DelegateFake, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportCreateRebarStrand(self, pRebarStrand):
        """ ExportCreateRebarStrand(self: DelegateFake, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportCreateReferenceModel(self, pReferenceModel):
        """ ExportCreateReferenceModel(self: DelegateFake, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportCreateReferenceModelObjectAttribute(self, pRMOAttribute):
        """ ExportCreateReferenceModelObjectAttribute(self: DelegateFake, pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int, dotReferenceModelObjectAttribute_t) """
        pass

    def ExportCreateReferenceModelObjectAttributeEnumerator(self, pEnumerator):
        """ ExportCreateReferenceModelObjectAttributeEnumerator(self: DelegateFake, pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int, dotReferenceModelObjectAttributeEnumerator_t) """
        pass

    def ExportCreateReport(self, aReport):
        """ ExportCreateReport(self: DelegateFake, aReport: dotCreateReportFromModel_t) -> (int, dotCreateReportFromModel_t) """
        pass

    def ExportCreateSingleRebar(self, pSingleRebar):
        """ ExportCreateSingleRebar(self: DelegateFake, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportCreateSurfaceByFace(self, hitPoint, faceNormal, id):
        """ ExportCreateSurfaceByFace(self: DelegateFake, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceByFaceAndAttrib(self, hitPoint, faceNormal, id, name, surfaceClass):
        """ ExportCreateSurfaceByFaceAndAttrib(self: DelegateFake, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int, name: str, surfaceClass: str) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceObject(self, pSurfaceObject):
        """ ExportCreateSurfaceObject(self: DelegateFake, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportCreateSurfaceTreatment(self, pTreatment):
        """ ExportCreateSurfaceTreatment(self: DelegateFake, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportCreateTask(self, pTask):
        """ ExportCreateTask(self: DelegateFake, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportCreateTaskDependency(self, pTaskDependency):
        """ ExportCreateTaskDependency(self: DelegateFake, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportCreateTaskWorktype(self, pTaskWorktype):
        """ ExportCreateTaskWorktype(self: DelegateFake, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportCreateWeld(self, pWeld):
        """ ExportCreateWeld(self: DelegateFake, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportDasStartAction(self, ActionName, Parameter):
        """ ExportDasStartAction(self: DelegateFake, ActionName: str, Parameter: str) -> int """
        pass

    def ExportDasStartCommand(self, CommandName, Parameter):
        """ ExportDasStartCommand(self: DelegateFake, CommandName: str, Parameter: str) -> int """
        pass

    def ExportDeleteBasePoint(self, pBasePoint):
        """ ExportDeleteBasePoint(self: DelegateFake, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportDeleteClipPlane(self, pDotView, pDotClipPlane):
        """ ExportDeleteClipPlane(self: DelegateFake, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportDeleteConversionLink(self, pConversionLink):
        """ ExportDeleteConversionLink(self: DelegateFake, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportDeleteObject(self, pIdentifier):
        """ ExportDeleteObject(self: DelegateFake, pIdentifier: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportDisplayAutoDefaultSettings(self, pBaseComponent):
        """ ExportDisplayAutoDefaultSettings(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayComponentHelp(self, pBaseComponent):
        """ ExportDisplayComponentHelp(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayPrompt(self, Message):
        """ ExportDisplayPrompt(self: DelegateFake, Message: str) -> int """
        pass

    def ExportDisplayReport(self, FileName):
        """ ExportDisplayReport(self: DelegateFake, FileName: str) -> int """
        pass

    def ExportDoubleListHandler(self, pDoubleList):
        """ ExportDoubleListHandler(self: DelegateFake, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ExportDrawTemporaryPolygonSurface(self, pArgument):
        """ ExportDrawTemporaryPolygonSurface(self: DelegateFake, pArgument: dotDrawPolygonSurface_t) -> (int, dotDrawPolygonSurface_t) """
        pass

    def ExportDrawTemporaryPolyLine(self, pArgument):
        """ ExportDrawTemporaryPolyLine(self: DelegateFake, pArgument: dotDrawPolyLine_t) -> (int, dotDrawPolyLine_t) """
        pass

    def ExportDrawTemporaryPolyLineWithId(self, pArgument):
        """ ExportDrawTemporaryPolyLineWithId(self: DelegateFake, pArgument: dotGraphicPolyLine_t) -> (int, dotGraphicPolyLine_t) """
        pass

    def ExportDrawTemporaryText(self, pArgument):
        """ ExportDrawTemporaryText(self: DelegateFake, pArgument: dotDrawText_t) -> (int, dotDrawText_t) """
        pass

    def ExportEdgeListHandler(self, pEdgeList):
        """ ExportEdgeListHandler(self: DelegateFake, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ExportEnumerateObjects(self, pEnumerator):
        """ ExportEnumerateObjects(self: DelegateFake, pEnumerator: dotEnumerator_t) -> (int, dotEnumerator_t) """
        pass

    def ExportExtractBentPlateFromComponent(self, partId):
        """ ExportExtractBentPlateFromComponent(self: DelegateFake, partId: int) -> int """
        pass

    def ExportFingerprint(self, pInput, fingerprint):
        """ ExportFingerprint(self: DelegateFake, pInput: dotPolymesh_t, fingerprint: str) -> (int, dotPolymesh_t, str) """
        pass

    def ExportFormatProfile(self, profile):
        """ ExportFormatProfile(self: DelegateFake, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportGetAllProperties(self, pProperties, pNames, pValues):
        """ ExportGetAllProperties(self: DelegateFake, pProperties: dotGetProperties_t, pNames: List[object], pValues: List[object]) -> (int, dotGetProperties_t, List[object], List[object]) """
        pass

    def ExportGetAllReportProperties(self, pProperties):
        """ ExportGetAllReportProperties(self: DelegateFake, pProperties: List[dotGetProperties_t]) -> (int, List[dotGetProperties_t]) """
        pass

    def ExportGetAssociateSurfaces(self, id):
        """ ExportGetAssociateSurfaces(self: DelegateFake, id: int) -> List[int] """
        pass

    def ExportGetBasePoints(self, ClientId):
        """ ExportGetBasePoints(self: DelegateFake, ClientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportGetBentPlateMaximumRadius(self, geometryNodeId, clientId):
        """ ExportGetBentPlateMaximumRadius(self: DelegateFake, geometryNodeId: int, clientId: dotClientId_t) -> (float, dotClientId_t) """
        pass

    def ExportGetBentPlateMinimumRadius(self, partId):
        """ ExportGetBentPlateMinimumRadius(self: DelegateFake, partId: int) -> float """
        pass

    def ExportGetClipPlanes(self, pDotView, pDotGetClipPlanes):
        """ ExportGetClipPlanes(self: DelegateFake, pDotView: dotView_t, pDotGetClipPlanes: dotGetClipPlanes_t) -> (int, dotView_t, dotGetClipPlanes_t) """
        pass

    def ExportGetColorRepresentationForObject(self, pIdentifier, pColor):
        """ ExportGetColorRepresentationForObject(self: DelegateFake, pIdentifier: dotIdentifier_t, pColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportGetCommandStatus(self, TSCommand, TSCommandParam, Status):
        """ ExportGetCommandStatus(self: DelegateFake, TSCommand: str, TSCommandParam: str, Status: bool) -> (int, str, str, bool) """
        pass

    def ExportGetCommitData(self, pId, pObjectType, pObjectSubType, pCommitType):
        """ ExportGetCommitData(self: DelegateFake, pId: dotIdentifier_t, pObjectType: int, pObjectSubType: int, pCommitType: int) -> (int, dotIdentifier_t, int, int, int) """
        pass

    def ExportGetComponentAttribute(self, pIdentifier, pAttribute):
        """ ExportGetComponentAttribute(self: DelegateFake, pIdentifier: dotIdentifier_t, pAttribute: dotComponentAttribute_t) -> (int, dotIdentifier_t, dotComponentAttribute_t) """
        pass

    def ExportGetComponentInput(self, pObj):
        """ ExportGetComponentInput(self: DelegateFake, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportGetCoordinateSystem(self, pModelObject, pCoordinateSystem):
        """ ExportGetCoordinateSystem(self: DelegateFake, pModelObject: dotModelObject_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotModelObject_t, dotCoordinateSystem_t) """
        pass

    def ExportGetCoordinateSystemAccordingToBasePoint(self, id, pCoordSys):
        """ ExportGetCoordinateSystemAccordingToBasePoint(self: DelegateFake, id: int, pCoordSys: dotCoordinateSystem_t) -> (int, dotCoordinateSystem_t) """
        pass

    def ExportGetCutSolidSerialized(self, dotSolid1, dotSolid2, serializedFaceList, serializedVectorList, serializedFaceOriginPartIdList, serializedShellIndexList, serializedEdgeVertexList, serializedEdgeTypeList, serializedEdgeShellIndexList):
        """ ExportGetCutSolidSerialized(self: DelegateFake, dotSolid1: dotSolid_t, dotSolid2: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedFaceOriginPartIdList: List[int], serializedShellIndexList: List[int], serializedEdgeVertexList: List[dotPoint_t], serializedEdgeTypeList: List[int], serializedEdgeShellIndexList: List[int]) -> (int, dotSolid_t, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetDatabaseVersion(self, version):
        """ ExportGetDatabaseVersion(self: DelegateFake, version: int) -> (int, int) """
        pass

    def ExportGetDataBaseVersionInfoFromModel(self, pInfo):
        """ ExportGetDataBaseVersionInfoFromModel(self: DelegateFake, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetDetectedClash(self, pClash):
        """ ExportGetDetectedClash(self: DelegateFake, pClash: dotClash_t) -> (int, dotClash_t) """
        pass

    def ExportGetDotType(self, pModelObject):
        """ ExportGetDotType(self: DelegateFake, pModelObject: dotModelObject_t) -> (int, dotModelObject_t) """
        pass

    def ExportGetFatherComponent(self, ObjectId, FatherComponentId):
        """ ExportGetFatherComponent(self: DelegateFake, ObjectId: int, FatherComponentId: int) -> (int, int) """
        pass

    def ExportGetIntersectionBoundingBoxes(self, Identifier1, Identifier2, ClientId):
        """ ExportGetIntersectionBoundingBoxes(self: DelegateFake, Identifier1: dotIdentifier_t, Identifier2: dotIdentifier_t, ClientId: dotClientId_t) -> (int, dotIdentifier_t, dotIdentifier_t, dotClientId_t) """
        pass

    def ExportGetIntersectionPoints(self, pIntersectionPoints):
        """ ExportGetIntersectionPoints(self: DelegateFake, pIntersectionPoints: dotIntersectionPoints_t) -> (int, dotIntersectionPoints_t) """
        pass

    def ExportGetIntersectionSolid(self, pSolid):
        """ ExportGetIntersectionSolid(self: DelegateFake, pSolid: dotIntersectionSolid_t) -> (int, dotIntersectionSolid_t) """
        pass

    def ExportGetModificationStamp(self, pModStmp):
        """ ExportGetModificationStamp(self: DelegateFake, pModStmp: dotModificationStamp_t) -> (int, dotModificationStamp_t) """
        pass

    def ExportGetModificationStampGuid(self, pModStmp):
        """ ExportGetModificationStampGuid(self: DelegateFake, pModStmp: str) -> (int, str) """
        pass

    def ExportGetNumberingUpToDate(self, pNumberingQuery):
        """ ExportGetNumberingUpToDate(self: DelegateFake, pNumberingQuery: dotNumberingQuery_t) -> (int, dotNumberingQuery_t) """
        pass

    def ExportGetNumberOfClashes(self, pClashes):
        """ ExportGetNumberOfClashes(self: DelegateFake, pClashes: int) -> (int, int) """
        pass

    def ExportGetObjectLastModified(self, pIdentifier, pTime, pLocallyModified):
        """ ExportGetObjectLastModified(self: DelegateFake, pIdentifier: dotIdentifier_t, pTime: int, pLocallyModified: bool) -> (int, dotIdentifier_t, int, bool) """
        pass

    def ExportGetObjectPhase(self, pArgument):
        """ ExportGetObjectPhase(self: DelegateFake, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportGetParentObject(self, surfaceId):
        """ ExportGetParentObject(self: DelegateFake, surfaceId: int) -> int """
        pass

    def ExportGetPartLine(self, pPartLine):
        """ ExportGetPartLine(self: DelegateFake, pPartLine: dotPartLine_t) -> (int, dotPartLine_t) """
        pass

    def ExportGetPartMark(self, pPartMark):
        """ ExportGetPartMark(self: DelegateFake, pPartMark: dotPartMark_t) -> (int, dotPartMark_t) """
        pass

    def ExportGetPhaseNumbers(self, pArgument):
        """ ExportGetPhaseNumbers(self: DelegateFake, pArgument: dotPhaseNumbers_t) -> (int, dotPhaseNumbers_t) """
        pass

    def ExportGetPlane(self, pPlane):
        """ ExportGetPlane(self: DelegateFake, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportGetPolybeamCoordinateSystem(self, Id, SubId, Chamfered, pX, pY, pZ):
        """ ExportGetPolybeamCoordinateSystem(self: DelegateFake, Id: int, SubId: int, Chamfered: int, pX: dotPoint_t, pY: dotPoint_t, pZ: dotPoint_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t) """
        pass

    def ExportGetProjectInfo(self, pInfo):
        """ ExportGetProjectInfo(self: DelegateFake, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportGetProperties(self, pProperties):
        """ ExportGetProperties(self: DelegateFake, pProperties: dotGetProperties_t) -> (int, dotGetProperties_t) """
        pass

    def ExportGetReferenceModelObjectByExternalGuid(self, referenceModelId, externalGuid):
        """ ExportGetReferenceModelObjectByExternalGuid(self: DelegateFake, referenceModelId: int, externalGuid: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportGetReferenceModelRevisionIds(self, pReferenceModel, ClientId):
        """ ExportGetReferenceModelRevisionIds(self: DelegateFake, pReferenceModel: dotReferenceModel_t, ClientId: dotClientId_t) -> (int, dotReferenceModel_t, dotClientId_t) """
        pass

    def ExportGetSetModelInfo(self, pInfo):
        """ ExportGetSetModelInfo(self: DelegateFake, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetSetModstamp(self, ModStampData):
        """ ExportGetSetModstamp(self: DelegateFake, ModStampData: dotModStamp_t) -> (int, dotModStamp_t) """
        pass

    def ExportGetSnapshotFromDatabase(self, Enumerator, SelectInstances):
        """ ExportGetSnapshotFromDatabase(self: DelegateFake, Enumerator: dotEnumerator_t, SelectInstances: bool) -> (Serializable[List[ModelObject]], dotEnumerator_t) """
        pass

    def ExportGetSolid(self, pSolid):
        """ ExportGetSolid(self: DelegateFake, pSolid: dotSolid_t) -> (int, dotSolid_t) """
        pass

    def ExportGetSolidBrep(self, polymeshToClean, polymeshCleaned):
        """ ExportGetSolidBrep(self: DelegateFake, polymeshToClean: dotPolymesh_t, polymeshCleaned: dotPolymesh_t) -> (bool, dotPolymesh_t, dotPolymesh_t) """
        pass

    def ExportGetSolidMerged(self, dotSolid, polymeshes):
        """ ExportGetSolidMerged(self: DelegateFake, dotSolid: dotSolid_t, polymeshes: dotPolymesh_t) -> (int, dotSolid_t, dotPolymesh_t) """
        pass

    def ExportGetSolidSerialized(self, dotSolid, serializedFaceList, serializedVectorList, serializedShellIndexList, serializedFaceOriginIdList):
        """ ExportGetSolidSerialized(self: DelegateFake, dotSolid: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedShellIndexList: List[int], serializedFaceOriginIdList: List[int]) -> (int, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetStringPropertyFromDatabase(self, pProperty, stringValues):
        """ ExportGetStringPropertyFromDatabase(self: DelegateFake, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportGetSurfaceGeometryType(self, surfaceId):
        """ ExportGetSurfaceGeometryType(self: DelegateFake, surfaceId: int) -> int """
        pass

    def ExportGetTrackEvent(self, category, eventName, eventContent):
        """ ExportGetTrackEvent(self: DelegateFake, category: str, eventName: str, eventContent: str) -> (int, str, str, str) """
        pass

    def ExportGetTransformationPlane(self, pPlane):
        """ ExportGetTransformationPlane(self: DelegateFake, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportGetViewCamera(self, pDotView, pDotCamera):
        """ ExportGetViewCamera(self: DelegateFake, pDotView: dotView_t, pDotCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportGetViews(self, pViews):
        """ ExportGetViews(self: DelegateFake, pViews: dotViewSelector_t) -> (int, dotViewSelector_t) """
        pass

    def ExportGetWeldGeometry(self, pWeldGeometry):
        """ ExportGetWeldGeometry(self: DelegateFake, pWeldGeometry: dotWeldGeometry_t) -> (int, dotWeldGeometry_t) """
        pass

    def ExportGetWriteOutStampGuid(self, pModStmp):
        """ ExportGetWriteOutStampGuid(self: DelegateFake, pModStmp: str) -> (int, str) """
        pass

    def ExportHierarchicDefinition(self, pHierarchicDefinition):
        """ ExportHierarchicDefinition(self: DelegateFake, pHierarchicDefinition: dotHierarchicDefinition_t) -> (int, dotHierarchicDefinition_t) """
        pass

    def ExportHierarchicObject(self, pHierarchicObject):
        """ ExportHierarchicObject(self: DelegateFake, pHierarchicObject: dotHierarchicObject_t) -> (int, dotHierarchicObject_t) """
        pass

    def ExportHierarchicObjectChildrenOperation(self, pHierarchicList):
        """ ExportHierarchicObjectChildrenOperation(self: DelegateFake, pHierarchicList: dotHierarchicList_t) -> (int, dotHierarchicList_t) """
        pass

    def ExportInitializeComponentStacks(self):
        """ ExportInitializeComponentStacks(self: DelegateFake) -> int """
        pass

    def ExportInsertView(self, View):
        """ ExportInsertView(self: DelegateFake, View: dotView_t) -> (int, dotView_t) """
        pass

    def ExportIntListHandler(self, pIntList):
        """ ExportIntListHandler(self: DelegateFake, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ExportLoadComponentAttributes(self, pBaseComponent):
        """ ExportLoadComponentAttributes(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportManipulateObject(self, pArgument):
        """ ExportManipulateObject(self: DelegateFake, pArgument: dotManipulateObject_t) -> (int, dotManipulateObject_t) """
        pass

    def ExportModifyAssembly(self, pAssembly):
        """ ExportModifyAssembly(self: DelegateFake, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportModifyBasePoint(self, pBasePoint):
        """ ExportModifyBasePoint(self: DelegateFake, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportModifyBentPlate(self, pPart):
        """ ExportModifyBentPlate(self: DelegateFake, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportModifyBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportModifyBoltGroup(self: DelegateFake, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportModifyBooleanPart(self, pBooleanPart):
        """ ExportModifyBooleanPart(self: DelegateFake, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportModifyClipPlane(self, pDotView, pDotClipPlane):
        """ ExportModifyClipPlane(self: DelegateFake, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportModifyComponent(self, pBaseComponent):
        """ ExportModifyComponent(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportModifyControlPlane(self, pControlObject):
        """ ExportModifyControlPlane(self: DelegateFake, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportModifyCylindricalSurfaceNode(self, geometryNodeId, surfacePoints, clientId):
        """ ExportModifyCylindricalSurfaceNode(self: DelegateFake, geometryNodeId: int, surfacePoints: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyEdgeChamfer(self, pEdgeChamfer):
        """ ExportModifyEdgeChamfer(self: DelegateFake, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportModifyFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportModifyFittingOrCutPlane(self: DelegateFake, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeCurveType(self, geometryNodeId, newCurveType, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: DelegateFake, geometryNodeId: int, newCurveType: int, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeRadius(self, geometryNodeId, radius, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeRadius(self: DelegateFake, geometryNodeId: int, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreePolygonNode(self, geometryNodeId, contour, clientId):
        """ ExportModifyGeometryTreePolygonNode(self: DelegateFake, geometryNodeId: int, contour: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyGrid(self, pGrid):
        """ ExportModifyGrid(self: DelegateFake, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportModifyGridPlane(self, pGridPlane):
        """ ExportModifyGridPlane(self: DelegateFake, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportModifyLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportModifyLoad(self: DelegateFake, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportModifyLoadGroup(self, pLoadGroup):
        """ ExportModifyLoadGroup(self: DelegateFake, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportModifyPart(self, pPart, contour):
        """ ExportModifyPart(self: DelegateFake, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportModifyPourBreak(self, pPourBreak):
        """ ExportModifyPourBreak(self: DelegateFake, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportModifyPourObject(self, pPourObject):
        """ ExportModifyPourObject(self: DelegateFake, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportModifyProjectInfo(self, pInfo):
        """ ExportModifyProjectInfo(self: DelegateFake, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportModifyRebarEndDetailStrip(self, pStrip):
        """ ExportModifyRebarEndDetailStrip(self: DelegateFake, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportModifyRebarGroup(self, pRebarGroup):
        """ ExportModifyRebarGroup(self: DelegateFake, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportModifyRebarMesh(self, pRebarMesh):
        """ ExportModifyRebarMesh(self: DelegateFake, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportModifyRebarPropertyStrip(self, pStrip):
        """ ExportModifyRebarPropertyStrip(self: DelegateFake, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportModifyRebarSplice(self, pRebarSplice):
        """ ExportModifyRebarSplice(self: DelegateFake, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportModifyRebarSplitter(self, pStrip):
        """ ExportModifyRebarSplitter(self: DelegateFake, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportModifyRebarStrand(self, pRebarStrand):
        """ ExportModifyRebarStrand(self: DelegateFake, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportModifyReferenceModel(self, pReferenceModel):
        """ ExportModifyReferenceModel(self: DelegateFake, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportModifySingleRebar(self, pSingleRebar):
        """ ExportModifySingleRebar(self: DelegateFake, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportModifySurfaceObject(self, pSurfaceObject):
        """ ExportModifySurfaceObject(self: DelegateFake, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportModifySurfaceTreatment(self, pTreatment):
        """ ExportModifySurfaceTreatment(self: DelegateFake, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportModifyTask(self, pTask):
        """ ExportModifyTask(self: DelegateFake, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportModifyTaskDependency(self, pTaskDependency):
        """ ExportModifyTaskDependency(self: DelegateFake, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportModifyTaskWorktype(self, pTaskWorktype):
        """ ExportModifyTaskWorktype(self: DelegateFake, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportModifyView(self, View):
        """ ExportModifyView(self: DelegateFake, View: dotView_t) -> (int, dotView_t) """
        pass

    def ExportModifyWeld(self, pWeld):
        """ ExportModifyWeld(self: DelegateFake, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportModStampCompare(self, ModStampCompare):
        """ ExportModStampCompare(self: DelegateFake, ModStampCompare: dotModStampCompare_t) -> (int, dotModStampCompare_t) """
        pass

    def ExportObjectMatchesToFilter(self, pObjectId, FileName):
        """ ExportObjectMatchesToFilter(self: DelegateFake, pObjectId: dotIdentifier_t, FileName: str) -> (int, dotIdentifier_t) """
        pass

    def ExportParseProfile(self, profile):
        """ ExportParseProfile(self: DelegateFake, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportPointListHandler(self, pPointList):
        """ ExportPointListHandler(self: DelegateFake, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ExportProgressBarOperation(self, pProgressBar):
        """ ExportProgressBarOperation(self: DelegateFake, pProgressBar: dotProgressBar_t) -> (int, dotProgressBar_t) """
        pass

    def ExportRebarSetAdditionFunction(self, action, pRebarSet):
        """ ExportRebarSetAdditionFunction(self: DelegateFake, action: RebarSetAction, pRebarSet: dotRebarSetAddition_t) -> (int, dotRebarSetAddition_t) """
        pass

    def ExportRebarSetFunction(self, action, pRebarSet):
        """ ExportRebarSetFunction(self: DelegateFake, action: RebarSetAction, pRebarSet: dotRebarSet_t) -> (int, dotRebarSet_t) """
        pass

    def ExportRefreshReferenceFile(self, pReferenceModel):
        """ ExportRefreshReferenceFile(self: DelegateFake, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportRemoveFromPourUnit(self, clientId):
        """ ExportRemoveFromPourUnit(self: DelegateFake, clientId: dotClientId_t) -> (bool, dotClientId_t) """
        pass

    def ExportRemoveTemporaryGraphicsObjects(self, pArgument):
        """ ExportRemoveTemporaryGraphicsObjects(self: DelegateFake, pArgument: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportRunMacro(self, FileName):
        """ ExportRunMacro(self: DelegateFake, FileName: str) -> int """
        pass

    def ExportRunOrStopClashCheck(self, RunningClashCheck):
        """ ExportRunOrStopClashCheck(self: DelegateFake, RunningClashCheck: bool) -> int """
        pass

    def ExportSaveAsWebModel(self, pSaveAsWebModel):
        """ ExportSaveAsWebModel(self: DelegateFake, pSaveAsWebModel: dotSaveAsWebModel_t) -> (int, dotSaveAsWebModel_t) """
        pass

    def ExportSaveOperation(self, pOperation):
        """ ExportSaveOperation(self: DelegateFake, pOperation: dotSaveOperation_t) -> (int, dotSaveOperation_t) """
        pass

    def ExportSelectAssembly(self, pAssembly):
        """ ExportSelectAssembly(self: DelegateFake, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportSelectBasePoint(self, guid, pBasePoint):
        """ ExportSelectBasePoint(self: DelegateFake, guid: str, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportSelectBentPlate(self, pPart):
        """ ExportSelectBentPlate(self: DelegateFake, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportSelectBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportSelectBoltGroup(self: DelegateFake, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportSelectBooleanPart(self, pBooleanPart):
        """ ExportSelectBooleanPart(self: DelegateFake, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportSelectComponent(self, pBaseComponent):
        """ ExportSelectComponent(self: DelegateFake, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportSelectControlPlane(self, pControlObject):
        """ ExportSelectControlPlane(self: DelegateFake, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportSelectConversionLink(self, pConversionLink):
        """ ExportSelectConversionLink(self: DelegateFake, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportSelectEdgeChamfer(self, pEdgeChamfer):
        """ ExportSelectEdgeChamfer(self: DelegateFake, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportSelectFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportSelectFittingOrCutPlane(self: DelegateFake, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportSelectGrid(self, pGrid):
        """ ExportSelectGrid(self: DelegateFake, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportSelectGridPlane(self, pGridPlane):
        """ ExportSelectGridPlane(self: DelegateFake, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportSelectGuideline(self, pGuideline):
        """ ExportSelectGuideline(self: DelegateFake, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportSelectLegFace(self, pLegFace):
        """ ExportSelectLegFace(self: DelegateFake, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportSelectLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportSelectLoad(self: DelegateFake, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportSelectLoadGroup(self, pLoadGroup):
        """ ExportSelectLoadGroup(self: DelegateFake, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportSelectPart(self, pPart, contour):
        """ ExportSelectPart(self: DelegateFake, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportSelectPourBreak(self, pPourBreak):
        """ ExportSelectPourBreak(self: DelegateFake, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportSelectPourObject(self, pPourObject):
        """ ExportSelectPourObject(self: DelegateFake, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportSelectRebarBars(self, pWire):
        """ ExportSelectRebarBars(self: DelegateFake, pWire: dotWire_t) -> (int, dotWire_t) """
        pass

    def ExportSelectRebarEndDetailStrip(self, pStrip):
        """ ExportSelectRebarEndDetailStrip(self: DelegateFake, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportSelectRebarGroup(self, pRebarGroup):
        """ ExportSelectRebarGroup(self: DelegateFake, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportSelectRebarMesh(self, pRebarMesh):
        """ ExportSelectRebarMesh(self: DelegateFake, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportSelectRebarPropertyStrip(self, pStrip):
        """ ExportSelectRebarPropertyStrip(self: DelegateFake, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportSelectRebarSplice(self, pRebarSplice):
        """ ExportSelectRebarSplice(self: DelegateFake, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportSelectRebarSplitter(self, pStrip):
        """ ExportSelectRebarSplitter(self: DelegateFake, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportSelectRebarStrand(self, pRebarStrand):
        """ ExportSelectRebarStrand(self: DelegateFake, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportSelectReferenceModel(self, pReferenceModel):
        """ ExportSelectReferenceModel(self: DelegateFake, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportSelectReferenceModelObject(self, pReferenceModelObject):
        """ ExportSelectReferenceModelObject(self: DelegateFake, pReferenceModelObject: dotReferenceModelObject_t) -> (int, dotReferenceModelObject_t) """
        pass

    def ExportSelectReferenceModelRevision(self, modelId, revisionId, pRevision):
        """ ExportSelectReferenceModelRevision(self: DelegateFake, modelId: int, revisionId: int, pRevision: dotReferenceModelRevision_t) -> (int, dotReferenceModelRevision_t) """
        pass

    def ExportSelectSingleRebar(self, pSingleRebar):
        """ ExportSelectSingleRebar(self: DelegateFake, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportSelectSurfaceObject(self, pSurfaceObject):
        """ ExportSelectSurfaceObject(self: DelegateFake, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportSelectSurfaceTreatment(self, pTreatment):
        """ ExportSelectSurfaceTreatment(self: DelegateFake, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportSelectTask(self, pTask):
        """ ExportSelectTask(self: DelegateFake, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportSelectTaskDependency(self, pTaskDependency):
        """ ExportSelectTaskDependency(self: DelegateFake, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportSelectTaskWorktype(self, pTaskWorktype):
        """ ExportSelectTaskWorktype(self: DelegateFake, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportSelectView(self, pView):
        """ ExportSelectView(self: DelegateFake, pView: dotView_t) -> (int, dotView_t) """
        pass

    def ExportSelectWeld(self, pWeld):
        """ ExportSelectWeld(self: DelegateFake, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportSetAdvancedOption(self, pArgument):
        """ ExportSetAdvancedOption(self: DelegateFake, pArgument: dotGetAdvancedOption_t) -> (int, dotGetAdvancedOption_t) """
        pass

    def ExportSetAsCurrentRevision(self, modelId, revisionId):
        """ ExportSetAsCurrentRevision(self: DelegateFake, modelId: int, revisionId: int) -> int """
        pass

    def ExportSetComponentNameField(self, parentDialog, fieldName, fieldValue):
        """ ExportSetComponentNameField(self: DelegateFake, parentDialog: str, fieldName: str, fieldValue: str) -> int """
        pass

    def ExportSetGetPhaseProperty(self, pArgument):
        """ ExportSetGetPhaseProperty(self: DelegateFake, pArgument: dotSetGetProperty_t) -> (int, dotSetGetProperty_t) """
        pass

    def ExportSetObjectPhase(self, pArgument):
        """ ExportSetObjectPhase(self: DelegateFake, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportSetPlane(self, pPlane):
        """ ExportSetPlane(self: DelegateFake, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportSetProperty(self, pProperty):
        """ ExportSetProperty(self: DelegateFake, pProperty: dotSetProperty_t) -> (int, dotSetProperty_t) """
        pass

    def ExportSetRepresentation(self, Representation):
        """ ExportSetRepresentation(self: DelegateFake, Representation: str) -> int """
        pass

    def ExportSetStringPropertyToDatabase(self, pProperty, stringValues):
        """ ExportSetStringPropertyToDatabase(self: DelegateFake, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportSetTemporaryColor(self, pObjectId, pNewColor):
        """ ExportSetTemporaryColor(self: DelegateFake, pObjectId: dotIdentifier_t, pNewColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportSetTemporaryColors(self, pSetTemporaryColors):
        """ ExportSetTemporaryColors(self: DelegateFake, pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryColors_FAST(self, pObjects, pSetTemporaryColors):
        """ ExportSetTemporaryColors_FAST(self: DelegateFake, pObjects: List[Identifier], pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, List[Identifier], dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryState(self, pObjectId, pNewState):
        """ ExportSetTemporaryState(self: DelegateFake, pObjectId: dotIdentifier_t, pNewState: dotTemporaryStatesEnum) -> (int, dotIdentifier_t, dotTemporaryStatesEnum) """
        pass

    def ExportSetTemporaryStates(self, pSetTemporaryStates):
        """ ExportSetTemporaryStates(self: DelegateFake, pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, dotSetTemporaryStates_t) """
        pass

    def ExportSetTemporaryStates_FAST(self, pObjects, pSetTemporaryStates):
        """ ExportSetTemporaryStates_FAST(self: DelegateFake, pObjects: List[Identifier], pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, List[Identifier], dotSetTemporaryStates_t) """
        pass

    def ExportSetTransformationPlane(self, pPlane):
        """ ExportSetTransformationPlane(self: DelegateFake, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportSetViewCamera(self, pDotView, pDotCamera):
        """ ExportSetViewCamera(self: DelegateFake, pDotView: dotView_t, pDotCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportShadowArea(self, pArgument):
        """ ExportShadowArea(self: DelegateFake, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportShadowAreaComplement(self, pArgument):
        """ ExportShadowAreaComplement(self: DelegateFake, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportSharingOperation(self, pOperation):
        """ ExportSharingOperation(self: DelegateFake, pOperation: dotSharingOperation_t) -> (int, dotSharingOperation_t) """
        pass

    def ExportSingleRebarGetRebarSet(self, singleRebarId):
        """ ExportSingleRebarGetRebarSet(self: DelegateFake, singleRebarId: int) -> int """
        pass

    def ExportStartCustomComponentCreation(self, ComponentName):
        """ ExportStartCustomComponentCreation(self: DelegateFake, ComponentName: str) -> int """
        pass

    def ExportStartPluginCreation(self, ComponentName):
        """ ExportStartPluginCreation(self: DelegateFake, ComponentName: str) -> int """
        pass

    def ExportStringListHandler(self, pStringList):
        """ ExportStringListHandler(self: DelegateFake, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
        pass

    def ExportTaskObjectAttach(self, pSelector):
        """ ExportTaskObjectAttach(self: DelegateFake, pSelector: dotTaskObjectAttacher_t) -> (int, dotTaskObjectAttacher_t) """
        pass

    def ExportUIObjectPick(self, pPicker):
        """ ExportUIObjectPick(self: DelegateFake, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUIObjectSelect(self, pSelector):
        """ ExportUIObjectSelect(self: DelegateFake, pSelector: dotUIModelObjectSelector_t) -> (int, dotUIModelObjectSelector_t) """
        pass

    def ExportUIObjectsPick(self, pPicker):
        """ ExportUIObjectsPick(self: DelegateFake, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUndoOperation(self, pOperation):
        """ ExportUndoOperation(self: DelegateFake, pOperation: dotUndoOperation_t) -> (int, dotUndoOperation_t) """
        pass

    def ExportValidatePolymesh(self, checkCriteria, pPolymeshToValidate, invalidInfo):
        """ ExportValidatePolymesh(self: DelegateFake, checkCriteria: int, pPolymeshToValidate: dotPolymesh_t, invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool, dotPolymesh_t, dotPolymeshValidateInvalidInfo_t) """
        pass

    def ExportViewHideUnselected(self, HideCompletely, DrawAsStick):
        """ ExportViewHideUnselected(self: DelegateFake, HideCompletely: bool, DrawAsStick: bool) -> int """
        pass

    def ExportWriteToSessionLog(self, Message):
        """ ExportWriteToSessionLog(self: DelegateFake, Message: str) -> int """
        pass

    def GetDSTVCoordinateSystem(self, PartId, pCoordinateSystem):
        """ GetDSTVCoordinateSystem(self: DelegateFake, PartId: dotIdentifier_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotCoordinateSystem_t) """
        pass

    def ImportDoubleListHandler(self, pDoubleList):
        """ ImportDoubleListHandler(self: DelegateFake, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ImportEdgeListHandler(self, pEdgeList):
        """ ImportEdgeListHandler(self: DelegateFake, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ImportIntListHandler(self, pIntList):
        """ ImportIntListHandler(self: DelegateFake, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ImportPointListHandler(self, pPointList):
        """ ImportPointListHandler(self: DelegateFake, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ImportStringListHandler(self, pStringList):
        """ ImportStringListHandler(self: DelegateFake, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
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

    def StartMacroRecording(self, FileName):
        """ StartMacroRecording(self: DelegateFake, FileName: str) -> int """
        pass

    def StopMacroRecording(self):
        """ StopMacroRecording(self: DelegateFake) -> int """
        pass


class dotAreaPolygons_t(object):
    # no doc
    def ToStruct(self, PartIds):
        """ ToStruct(self: dotAreaPolygons_t, PartIds: ArrayList) """
        pass

    aIdList = None
    ClientID = None
    nAreas = None
    nIdList = None


class dotAssembly_t(object):
    # no doc
    aAssemblyOtherPartsIds = None
    aAssemblySubAssemblyIds = None
    aName = None
    AssemblableId = None
    MainAssembly = None
    MainPart = None
    ModelObject = None
    nAssemblyOtherParts = None
    nAssemblySubAssemblies = None
    NumberingSeries = None
    Type = None


class dotBaseComponent_t(object):
    # no doc
    aAttributeFilename = None
    aConnectionCode = None
    aName = None
    aSecondaryObjectIds = None
    AutoDirectionType = None
    AutoPosition = None
    aX = None
    aY = None
    aZ = None
    Class = None
    CustomPartPosition = None
    DetailType = None
    ErrorStatus = None
    ModelObject = None
    nPositions = None
    nSecondaryObjectIds = None
    Number = None
    PositionType = None
    PrimaryObjectId = None
    UpVector = None


class dotBasePointData_t(object):
    # no doc
    aCoordinateSystem = None
    aDescription = None
    aGuid = None
    aName = None
    AngleToNorth = None
    EastWest = None
    Elevation = None
    Id = None
    Latitude = None
    LocationInModelX = None
    LocationInModelY = None
    LocationInModelZ = None
    Longitude = None
    NorthSouth = None


class dotBoltGroup_t(object):
    # no doc
    aBoltStandard = None
    aOtherPartsToBolt = None
    Bolt = None
    BoltPositions = None
    BoltSize = None
    BoltType = None
    ConnectAssemblies = None
    CutLength = None
    EndPointOffset = None
    ExtraLength = None
    FirstPosition = None
    Hole1 = None
    Hole2 = None
    Hole3 = None
    Hole4 = None
    Hole5 = None
    HoleType = None
    Length = None
    ModelObject = None
    nOtherPartsToBolt = None
    Nut1 = None
    Nut2 = None
    PartToBeBoltedId = None
    PartToBoltToId = None
    Position = None
    RotateSlots = None
    SecondPosition = None
    Shape = None
    SlottedHoleX = None
    SlottedHoleY = None
    StartPointOffset = None
    ThreadInMaterial = None
    Tolerance = None
    Washer1 = None
    Washer2 = None
    Washer3 = None


class dotBoltPolygon_t(object):
    """ dotBoltPolygon_t(Size: int) """
    def GetPoints(self):
        """ GetPoints(self: dotBoltPolygon_t) -> ArrayList """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotBoltPolygon_t]() -> dotBoltPolygon_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aX = None
    aY = None
    aZ = None
    nPoints = None


class dotBoltShapeData_t(object):
    # no doc
    aBoltDistX = None
    aBoltDistY = None
    Diameter = None
    nBoltDistX = None
    nBoltDistY = None
    NumberOfBolts = None


class dotBooleanPart_t(object):
    # no doc
    Boolean = None
    OperativePart = None
    Type = None


class dotBoolean_t(object):
    # no doc
    Father = None
    ModelObject = None


class dotCamera_t(object):
    # no doc
    DirectionVector = None
    FieldOfView = None
    Location = None
    UpVector = None
    ZoomFactor = None


class dotChamfer_t(object):
    # no doc
    DZ1 = None
    DZ2 = None
    Type = None
    X = None
    Y = None


class dotClash_t(object):
    # no doc
    Id1 = None
    Id2 = None
    PenetrationDepth = None
    Type = None


class dotClientId_t(object):
    # no doc
    ProcessId = None
    ThreadId = None


class dotClipPlane_t(object):
    # no doc
    ID = None
    Location = None
    UpVector = None


class dotColor_t(object):
    # no doc
    Blue = None
    Green = None
    Red = None
    Transparency = None


class dotComponentAttribute_t(object):
    # no doc
    aName = None
    aStrValue = None
    AttributeType = None
    DValue = None
    IValue = None


class dotComponentInputObject_t(object):
    # no doc
    aObjects = None
    aX = None
    aY = None
    aZ = None
    ComponentId = None
    InputNumber = None
    InputType = None
    nObjects = None
    nPoints = None


class dotContourPoint_t(object):
    # no doc
    Chamfer = None
    Point = None


class dotContour_t(object):
    """ dotContour_t(Size: int) """
    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotContour_t]() -> dotContour_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aChamferDZ1 = None
    aChamferDZ2 = None
    aChamferType = None
    aChamferX = None
    aChamferY = None
    aX = None
    aY = None
    aZ = None
    nContourPoints = None


class dotControlObject_t(object):
    # no doc
    aName = None
    Color = None
    Extension = None
    IsMagnetic = None
    ModelObject = None
    Plane = None


class dotConversionLink_t(object):
    # no doc
    ApprovalStatus = None
    ConversionStatus = None
    PartId = None
    RefModelId = None
    RefModelObjectId = None


class dotCreateIFCFromModel_t(object):
    # no doc
    aFileFullName = None
    aFilterName = None
    aModelName = None
    BasePoint = None
    ClientID = None
    CreateReport = None
    OnlySelected = None
    Result = None
    UseTimer = None
    ViewType = None


class dotCreateNCFromModel_t(object):
    # no doc
    aDestinationFolderName = None
    aFileName = None
    aNCFileSettingsName = None
    aPopMarkSettingsName = None
    CreatePopMarks = None
    ExportType = None
    OnlySelected = None
    Result = None


class dotCreateReportFromModel_t(object):
    # no doc
    aFileName = None
    aTemplateName = None
    aTitle1 = None
    aTitle2 = None
    aTitle3 = None
    OnlySelected = None
    Result = None


class dotDeformingData_t(object):
    # no doc
    Angle = None
    Angle2 = None
    Cambering = None
    Shortening = None


class dotDrawPolygonSurface_t(object):
    # no doc
    Color = None
    Polygon = None


class dotDrawPolyLine_t(object):
    # no doc
    Color = None
    Polygon = None


class dotDrawText_t(object):
    # no doc
    aText = None
    Color = None
    Location = None


class dotEdgeChamfer_t(object):
    # no doc
    aName = None
    Boolean = None
    Chamfer = None
    FirstBevelDimension = None
    FirstChamferEndType = None
    FirstEnd = None
    SecondBevelDimension = None
    SecondChamferEndType = None
    SecondEnd = None


class dotEdges_t(object):
    # no doc
    def GetEdges(self):
        """ GetEdges(self: dotEdges_t) -> ArrayList """
        pass

    EdgeType = None
    EndX = None
    EndY = None
    EndZ = None
    nEdges = None
    StartX = None
    StartY = None
    StartZ = None


class dotEnumerator_t(object):
    # no doc
    AdditionalId = None
    aFilterName = None
    aObjects = None
    aObjectTypes = None
    ClientId = None
    Filter = None
    MaxPoint = None
    MinPoint = None
    ModificationStamp = None
    MoreObjectsLeft = None
    nObjects = None
    nObjectToStart = None
    ReturnAlsoIfObjectIsCreatedAndDeletedAfterEvent = None
    SubFilter = None
    ViewId = None


class dotFittingOrCutPlane_t(object):
    # no doc
    Boolean = None
    Plane = None
    Type = None


class dotFormingStates_t(object):
    # no doc
    def FromStruct(self, formingStates):
        """ FromStruct(self: dotFormingStates_t, formingStates: FormingStates) """
        pass

    def ToStruct(self, formingStates):
        """ ToStruct(self: dotFormingStates_t, formingStates: FormingStates) """
        pass

    DeformingType = None
    FoldingType = None
    WrappingType = None


class dotGetClipPlanes_t(object):
    # no doc
    aPlaneIDs = None
    aUpX = None
    aUpY = None
    aUpZ = None
    aX = None
    aY = None
    aZ = None
    nPlanes = None


class dotGetProperties_t(object):
    # no doc
    aDoubleValues = None
    aIntValues = None
    aName0 = None
    aName1 = None
    aName2 = None
    aName3 = None
    aName4 = None
    aName5 = None
    aName6 = None
    aName7 = None
    aName8 = None
    aName9 = None
    aStringValue0 = None
    aStringValue1 = None
    aStringValue2 = None
    aStringValue3 = None
    aStringValue4 = None
    aStringValue5 = None
    aStringValue6 = None
    aStringValue7 = None
    aStringValue8 = None
    aStringValue9 = None
    aSuccess = None
    FatherId = None
    InitializeTable = None
    nProperties = None
    Source = None
    Type = None


class dotGraphicPolyLine_t(object):
    # no doc
    ClientId = None
    Color = None
    Type = None
    Width = None


class dotGridPlane_t(object):
    # no doc
    aLabel = None
    Color = None
    DrawingVisibility = None
    ExtensionAbove = None
    ExtensionBelow = None
    ExtensionForMagneticArea = None
    ExtensionLeft = None
    ExtensionRight = None
    FatherId = None
    IsMagnetic = None
    ModelObject = None
    Plane = None


class dotGrid_t(object):
    # no doc
    aCoordinateX = None
    aCoordinateY = None
    aCoordinateZ = None
    aLabelX = None
    aLabelY = None
    aLabelZ = None
    Color = None
    ExtensionForMagneticArea = None
    ExtensionLeftX = None
    ExtensionLeftY = None
    ExtensionLeftZ = None
    ExtensionRightX = None
    ExtensionRightY = None
    ExtensionRightZ = None
    IsMagnetic = None
    ModelObject = None


class dotGuideline_t(object):
    # no doc
    Curve = None
    Id = None
    Spacing = None


class dotHierarchicDefinition_t(object):
    # no doc
    aCustomType = None
    aHierarchyIdentifier = None
    aName = None
    aSubHierarchyIds = None
    Drawable = None
    HierarchyType = None
    ModelObject = None
    nSubHierarchyIds = None
    ObjectParent = None
    OperationType = None


class dotHierarchicList_t(object):
    # no doc
    aObjects = None
    ModelFatherObject = None
    nObjects = None
    ObjectsLeftToGet = None
    OperationType = None


class dotHierarchicObject_t(object):
    # no doc
    aName = None
    aSubHierarchyIds = None
    Definition = None
    ModelObject = None
    nSubHierarchyIds = None
    OperationType = None
    Parent = None
    Type = None


class dotIFC2X3_Application_t(object):
    # no doc
    ApplicationFullName = None
    ApplicationIdentifier = None
    Version = None


class dotIFC2X3_Organization_t(object):
    # no doc
    Description = None
    Id = None
    Name = None
    Roles = None


class dotIFC2X3_OwnerHistoryChangeAction_t(Enum):
    """ enum dotIFC2X3_OwnerHistoryChangeAction_t, values: CHANGEACTION_ADDED (2), CHANGEACTION_DELETED (3), CHANGEACTION_MODIFIED (1), CHANGEACTION_NOCHANGE (0) """
    CHANGEACTION_ADDED = None
    CHANGEACTION_DELETED = None
    CHANGEACTION_MODIFIED = None
    CHANGEACTION_NOCHANGE = None
    value__ = None


class dotIFC2X3_OwnerHistoryState_t(Enum):
    """ enum dotIFC2X3_OwnerHistoryState_t, values: STATE_LOCKED (3), STATE_READONLY (2), STATE_READONLYLOCKED (5), STATE_READWRITE (1), STATE_READWRITELOCKED (4), STATE_UNDEFINED (0) """
    STATE_LOCKED = None
    STATE_READONLY = None
    STATE_READONLYLOCKED = None
    STATE_READWRITE = None
    STATE_READWRITELOCKED = None
    STATE_UNDEFINED = None
    value__ = None


class dotIFC2X3_OwnerHistory_t(object):
    # no doc
    ChangeAction = None
    CreationDate = None
    isSetLastModifiedDate = None
    LastModifiedDate = None
    OwningApplication = None
    OwningUser = None
    State = None


class dotIFC2X3_ParametricObject_ShapeProfile_t(object):
    # no doc
    Double1 = None
    Double2 = None
    Double3 = None
    Double4 = None
    Double5 = None
    Double6 = None
    Double7 = None
    Double8 = None
    Double9 = None
    Extrusion = None
    Origin = None
    ProfileName = None
    xDir = None


class dotIFC2X3_PersonAndOrganization_t(object):
    # no doc
    TheOrganization = None
    ThePerson = None


class dotIFC2X3_Person_t(object):
    # no doc
    FamilyName = None
    GivenName = None
    Id = None
    MiddleNames = None
    Roles = None


class dotIFC2X3_Product_t(object):
    # no doc
    Description = None
    IFC2X3_OwnerHistory = None
    Name = None
    ObjectType = None


class dotIntersectionPoints_t(object):
    """ dotIntersectionPoints_t(Size: int) """
    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotIntersectionPoints_t]() -> dotIntersectionPoints_t
        
        __new__(cls: type, Size: int)
        """
        pass

    IntersectionPoints = None
    PlanePoint1 = None
    PlanePoint2 = None
    PlanePoint3 = None
    PointIndex = None
    ReturnValue = None
    SolidId = None


class dotIntersectionSolid_t(object):
    """ dotIntersectionSolid_t(Size: int) """
    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotIntersectionSolid_t]() -> dotIntersectionSolid_t
        
        __new__(cls: type, Size: int)
        """
        pass

    CreationType = None
    FaceIndex = None
    FormingStates = None
    IntersectionPoint1 = None
    IntersectionPoint2 = None
    IntersectionPoint3 = None
    LoopIndex = None
    Polygon = None
    QueryType = None
    ReturnValue = None
    SolidId = None
    VertexIndex = None


class dotLegFace_t(object):
    # no doc
    AdditonalOffset = None
    Id = None
    LayerOrderNumber = None
    PrimaryContour = None
    Reversed = None


class dotLoadClassAttributes_t(object):
    # no doc
    DistanceA = None
    DistanceB = None
    InitialAxialElongation = None
    LoadForm = None
    Moment = None
    P1 = None
    P2 = None
    P3 = None
    P4 = None
    Position = None
    TemperatureChangeForAxialElongation = None
    TemperatureDifferentialSideToSide = None
    TemperatureDifferentialTopToBottom = None
    Torsion1 = None
    Torsion2 = None


class dotLoadCommonAttributes_t(object):
    # no doc
    aPartFilter = None
    AutomaticPrimaryAxisWeight = None
    BoundingBoxDx = None
    BoundingBoxDy = None
    BoundingBoxDz = None
    CreateFixedSupportConditionsAutomatically = None
    FatherId = None
    LoadAttachment = None
    LoadDispersionAngle = None
    LoadGroupId = None
    ModelObject = None
    PartNames = None
    PrimaryAxisDirection = None
    Spanning = None
    Weight = None


class dotLoadGroup_t(object):
    # no doc
    Color = None
    Compatible = None
    Direction = None
    GroupName = None
    GroupType = None
    Incompatible = None
    ModelObject = None


class dotManipulateObject_t(object):
    # no doc
    ClientID = None
    EndPoint1 = None
    EndPoint2 = None
    EndPoint3 = None
    Identifier = None
    Identifier2 = None
    ManipulationType = None
    Point1 = None
    Point2 = None
    Point3 = None
    Polygon = None
    Result = None


class dotMaterial_t(object):
    # no doc
    aMaterialString = None


class dotModelCommit_t(object):
    # no doc
    aMessage = None


class dotModelInfoModeEnum(Enum):
    """ enum dotModelInfoModeEnum, values: CloseModel (2), GetModelInfo (0), OpenModel (1) """
    CloseModel = None
    GetModelInfo = None
    OpenModel = None
    value__ = None


class dotModelInfo_t(object):
    # no doc
    aModelName = None
    aModelPath = None
    aModelTemplateName = None
    aServerName = None
    ConnectToServer = None
    ConvertBetweenSingleAndMultiuser = None
    CurrentDataBaseVersion = None
    CurrentPhase = None
    ExcludeFromSharing = None
    IsModelSaved = None
    IsSharedModel = None
    IsSingleUserModel = None
    Mode = None
    ModelDataBaseVersion = None
    NorthDirection = None
    OpenAutoSaved = None


class dotModelObjectType_t(object):
    # no doc
    BooleanPartType = None
    IsConcreteMaterial = None
    PrimaryType = None
    SecondaryType = None


class dotModelObject_t(object):
    # no doc
    aLabel = None
    Object = None
    Type = None


class dotModificationStamp_t(object):
    # no doc
    def FromStruct(self, I):
        """ FromStruct(self: dotModificationStamp_t, I: ModificationStamp) """
        pass

    def ToStruct(self, I, S):
        """ ToStruct(self: dotModificationStamp_t, I: int, S: int) """
        pass

    CurrentModStamp = None
    CurrentSaveStamp = None


class dotModStampCompare_t(object):
    # no doc
    ModStamp = None
    ObjectGuid = None
    Type = None
    TypeEnum = None


class dotModStamp_t(object):
    # no doc
    ActionEnum = None
    aName = None
    aValue = None
    Direction = None


class dotnetDoubleList_t(object):
    """ dotnetDoubleList_t(size: int) """
    def FromStruct(self, doubleList):
        """ FromStruct(self: dotnetDoubleList_t, doubleList: DoubleList) """
        pass

    def ToStruct(self, doubleList):
        """ ToStruct(self: dotnetDoubleList_t, doubleList: DoubleList) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, size):
        """
        __new__[dotnetDoubleList_t]() -> dotnetDoubleList_t
        
        __new__(cls: type, size: int)
        """
        pass

    aDoubleList = None
    ClientId = None
    IndexCurrentItem = None
    NumberItems = None
    NumberItemsInSet = None


class dotnetEdgeList_t(object):
    """ dotnetEdgeList_t(Size: int) """
    def FromStruct(self, Edges):
        """ FromStruct(self: dotnetEdgeList_t, Edges: IList[IndirectPolymeshEdge]) """
        pass

    def ToStruct(self, Edges):
        """ ToStruct(self: dotnetEdgeList_t, Edges: IList[IndirectPolymeshEdge]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotnetEdgeList_t]() -> dotnetEdgeList_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aEdgeList = None
    ClientId = None
    IndexCurrentItem = None
    NumberItems = None
    NumberItemsInSet = None


class dotnetIntList_t(object):
    """ dotnetIntList_t(Size: int) """
    def FromStruct(self, IntList):
        """ FromStruct(self: dotnetIntList_t, IntList: IntList) """
        pass

    def ToStruct(self, IntList):
        """ ToStruct(self: dotnetIntList_t, IntList: IntList) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotnetIntList_t]() -> dotnetIntList_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aIntList = None
    ClientId = None
    IndexCurrentItem = None
    NumberItems = None
    NumberItemsInSet = None


class DotNetModelProxy(object):
    """ DotNetModelProxy() """
    @staticmethod
    def Run(Param):
        """ Run(Param: str) -> int """
        pass


class dotnetPointList_t(object):
    """ dotnetPointList_t(Size: int) """
    def FromStruct(self, PointList):
        """ FromStruct(self: dotnetPointList_t, PointList: PointList) """
        pass

    def ToStruct(self, PointList):
        """ ToStruct(self: dotnetPointList_t, PointList: PointList) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotnetPointList_t]() -> dotnetPointList_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aPointList = None
    ClientId = None
    IndexCurrentItem = None
    NumberItems = None
    NumberItemsInSet = None


class dotnetStringList_t(object):
    # no doc
    ClientId = None
    CurrentItem = None
    IndexCurrentItem = None


class dotNumberingQuery_t(object):
    # no doc
    Id = None
    QueryMode = None


class dotNumberingSeries_t(object):
    # no doc
    aPrefix = None
    StartNumber = None


class dotObjectOperationsEnum(Enum):
    """ enum dotObjectOperationsEnum, values: DOT_CREATE_OBJECT (0), DOT_DELETE_OBJECT (3), DOT_MODIFY_OBJECT (1), DOT_SELECT_OBJECT (2) """
    DOT_CREATE_OBJECT = None
    DOT_DELETE_OBJECT = None
    DOT_MODIFY_OBJECT = None
    DOT_SELECT_OBJECT = None
    value__ = None


class dotObject_t(object):
    # no doc
    Identifier = None


class dotOffset_t(object):
    # no doc
    Dx = None
    Dy = None
    Dz = None


class dotPartLine_t(object):
    # no doc
    aPoints = None
    nPoints = None
    PartID = None
    PartLineCutted = None
    PartLineType = None


class dotPartMark_t(object):
    # no doc
    aPartMark = None
    PartID = None


class dotPart_t(object):
    # no doc
    aClass = None
    aFinish = None
    aName = None
    AssemblyNumber = None
    CastUnitType = None
    ClientId = None
    DeformingData = None
    EndPointOffset = None
    Material = None
    ModelObject = None
    PartNumber = None
    Position = None
    PourPhase = None
    Profile = None
    Radius = None
    StartPointOffset = None
    SubType = None


class dotPhaseNumbers_t(object):
    # no doc
    aPhaseNumber = None
    nPhaseNumbers = None
    Result = None


class dotPhase_t(object):
    # no doc
    Id = None
    IsCurrentPhase = None
    PhaseComment = None
    PhaseManipulationType = None
    PhaseName = None
    PhaseNumber = None
    Result = None


class dotPlane_t(object):
    # no doc
    AxisX = None
    AxisY = None
    Origin = None


class dotPolygon_t(object):
    """ dotPolygon_t(Size: int) """
    def GetPoints(self):
        """ GetPoints(self: dotPolygon_t) -> ArrayList """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotPolygon_t]() -> dotPolygon_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aX = None
    aY = None
    aZ = None
    nPoints = None


class dotPolymeshObject_t(object):
    # no doc
    ModelObject = None
    Polymesh = None


class dotPolymeshValidateInvalidInfo_t(object):
    # no doc
    ClientId = None
    nInvalidFaces = None


class dotPolymesh_t(object):
    # no doc
    ClientId = None
    nPolymeshes = None
    nPolymeshFaces = None
    nPolymeshLoops = None


class dotPosition_t(object):
    # no doc
    Depth = None
    DepthOffset = None
    Plane = None
    PlaneOffset = None
    Rotation = None
    RotationOffset = None


class dotPourObject_t(object):
    # no doc
    Class = None
    ConcreteMixture = None
    ModelObject = None
    PourNumber = None
    PourType = None


class dotProfile_t(object):
    # no doc
    aProfileString = None


class dotProgressBar_t(object):
    # no doc
    aCancelButtonLabel = None
    aMessage = None
    aProgressLabel = None
    aTitle = None
    Canceled = None
    Operation = None
    Progress = None
    SleepTime = None


class dotProjectInfo_t(object):
    # no doc
    aAddress = None
    aBuilder = None
    aDescription = None
    aDesigner = None
    aEndDate = None
    aExtra1 = None
    aExtra2 = None
    aExtra3 = None
    aModelSharingLocalPath = None
    aModelSharingServerPath = None
    aName = None
    aObject = None
    aProjectNo = None
    aStartDate = None
    GUID = None


class dotRebarEndDetailStrip_t(object):
    # no doc
    RebarHookData = None
    RebarStrip = None
    RebarThreading = None


class dotRebarGroup_t(object):
    # no doc
    aSpacingMultipliers = None
    aSpacings = None
    aX = None
    aY = None
    aZ = None
    EndHook = None
    EndPoint = None
    ExcludeType = None
    nPointsInPolygon = None
    nPolygons = None
    nSpacingValues = None
    Reinforcement = None
    SpacingType = None
    StartHook = None
    StartPoint = None
    StirrupType = None
    SubType = None


class dotRebarHookData_t(object):
    # no doc
    Angle = None
    Length = None
    Radius = None
    Shape = None


class dotRebarMesh_t(object):
    # no doc
    aCrossDistanceMultipliers = None
    aCrossDistances = None
    aLongitudinalDistanceMultipliers = None
    aLongitudinalDistances = None
    CatalogName = None
    CrossBarLocation = None
    CrossSize = None
    CutByFatherPartCuts = None
    EndHook = None
    EndPoint = None
    LeftOverhangCross = None
    LeftOverhangLongitudinal = None
    Length = None
    LongitudinalSize = None
    LongitudinalSpacingMethod = None
    MeshType = None
    nCrossDistances = None
    nLongitudinalDistances = None
    Polygon = None
    Reinforcement = None
    RightOverhangCross = None
    RightOverhangLongitudinal = None
    StartHook = None
    StartPoint = None
    Width = None


class dotRebarProperties_t(object):
    # no doc
    BendingRadius = None
    Class = None
    Finish = None
    Grade = None
    Name = None
    NumberingSeries = None
    Size = None


class dotRebarPropertyStrip_t(object):
    # no doc
    RebarProperties = None
    RebarStrip = None


class dotRebarSetAddition_t(object):
    # no doc
    FatherId = None
    LegFaces = None
    ModelObject = None


class dotRebarSet_t(object):
    # no doc
    Guidelines = None
    LayerOrderNumber = None
    LegFaces = None
    ModelObject = None
    RebarProperties = None


class dotRebarSpacing_t(object):
    # no doc
    EndOffset = None
    EndOffsetIsAutomatic = None
    EndOffsetIsFixed = None
    NumberSpacingZones = None
    StartOffset = None
    StartOffsetIsAutomatic = None
    StartOffsetIsFixed = None
    Zones = None


class dotRebarSplice_t(object):
    # no doc
    BarPositions = None
    Clearance = None
    LapLength = None
    ModelObject = None
    Offset = None
    Reinforcement1 = None
    Reinforcement2 = None
    Type = None


class dotRebarSplitter_t(object):
    # no doc
    LapLength = None
    LapOffsetDir = None
    LapOffsetType = None
    LapSide = None
    RebarStrip = None
    SplitOffset = None
    SplitTarget = None
    StaggerOffset = None
    StaggerType = None


class dotRebarStrand_t(object):
    # no doc
    aFromEnd = None
    aFromStart = None
    aMiddleToEnd = None
    aMiddleToStart = None
    aStrandIndex = None
    aX = None
    aY = None
    aZ = None
    EndPoint = None
    nPatterns = None
    nPointsInPattern = None
    nUnbondings = None
    PullPerStrand = None
    Reinforcement = None
    StartPoint = None


class dotRebarStrip_t(object):
    # no doc
    ApplyOrderNumber = None
    Curve = None
    FatherId = None
    Flags = None
    ModelObject = None


class dotRebarThreading_t(object):
    # no doc
    ExtraFabLength = None
    Length = None
    ThreadingType = None


class dotReferenceModelObjectAttributeEnumerator_t(object):
    # no doc
    AttributeIndex = None
    AttributeType = None
    ReferenceModelId = None
    ReferenceModelObjectIdentifier = None


class dotReferenceModelObjectAttribute_t(object):
    # no doc
    AttributeIndex = None
    IFC2X3_ParametricObject_ShapeProfile = None
    IFC2X3_Product = None
    ReferenceModelId = None
    ReferenceModelObjectIdentifier = None


class dotReferenceModelObject_t(object):
    # no doc
    ModelObject = None
    ReferenceHierarchyFather = None
    ReferenceModel = None


class dotReferenceModelRevision_t(object):
    # no doc
    aFileName = None
    aIdentifier = None
    Day = None
    DbId = None
    Hour = None
    IsCurrentRevision = None
    Minute = None
    Month = None
    Second = None
    Year = None


class dotReferenceModel_t(object):
    # no doc
    aActiveFilePath = None
    aBasePointGuid = None
    aFilename = None
    ModelObject = None
    Position = None
    Rotation = None
    Scale = None
    Visibility = None


class dotReinforcement_t(object):
    # no doc
    aGrade = None
    aName = None
    aOnPlaneOffsets = None
    aRadiusValues = None
    aSize = None
    Class = None
    ClientId = None
    DeformingType = None
    EndFromPlaneOffset = None
    EndPointOffsetType = None
    EndPointOffsetValue = None
    Father = None
    ModelObject = None
    nOnPlaneOffsetValues = None
    nRadiusValues = None
    NumberingSeries = None
    StartFromPlaneOffset = None
    StartPointOffsetType = None
    StartPointOffsetValue = None


class dotSaveAsWebModel_t(object):
    # no doc
    Filename = None
    OnlySelected = None
    Result = None


class dotSaveOperation_t(object):
    # no doc
    aComment = None
    aID = None
    aSaveAsPath = None
    Operation = None


class dotSetGetProperty_t(object):
    # no doc
    aName = None
    aStringValue = None
    DoubleValue = None
    IntValue = None
    OperationType = None
    PhaseNumber = None
    PropertyType = None


class dotSetProperty_t(object):
    # no doc
    aName = None
    aStringValue = None
    DoubleValue = None
    FatherId = None
    IntValue = None
    Source = None
    Type = None


class dotSetTemporaryColors_t(object):
    # no doc
    AllObjects = None
    aObjectIDs = None
    aObjectSubIDs = None
    Color = None
    nObjects = None


class dotSetTemporaryStates_t(object):
    # no doc
    AllObjects = None
    aObjectIDs = None
    aObjectSubIDs = None
    nObjects = None
    State = None
    Transparency = None


class dotSharingOperation_t(object):
    # no doc
    aErrorDetail = None
    aGuid = None
    aMessage = None
    aModuleName = None
    aNewBaseline = None
    aOldBaseline = None
    aPacketPath = None
    aProfileId = None
    CommandId = None
    ErrorCode = None
    IsOwner = None
    Joining = None
    Operation = None
    PacketNumber = None
    Status = None


class dotSingleRebar_t(object):
    # no doc
    EndHook = None
    Polygon = None
    Reinforcement = None
    StartHook = None


class dotSolid_t(object):
    """ dotSolid_t(Size: int) """
    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotSolid_t]() -> dotSolid_t
        
        __new__(cls: type, Size: int)
        """
        pass

    CreationType = None
    EdgeIndex = None
    Edges = None
    FaceIndex = None
    FormingStates = None
    LoopIndex = None
    Polygon = None
    QueryType = None
    ReturnValue = None
    ShellCount = None
    SolidId = None
    VertexIndex = None
    VertexPoint = None
    VertexStartNumber = None


class dotSpacingZone_t(object):
    # no doc
    Length = None
    LengthIsFixed = None
    Number = None
    NumberIsFixed = None
    Spacing = None
    SpacingIsFixed = None


class dotStringProperty_t(object):
    # no doc
    aName = None
    aValueString = None
    FatherId = None
    ValueStringIteration = None


class dotSurfaceObject_t(object):
    # no doc
    Class = None
    CreateHoles = None
    ModelObject = None
    Name = None
    Polymesh = None
    RelatedObjectId = None
    Type = None


class dotSurfaceTreatment_t(object):
    # no doc
    aClass = None
    aName = None
    aTypeName = None
    Color = None
    CutByFatherBooleans = None
    EndPoint = None
    Father = None
    Material = None
    ModelObject = None
    Polygon = None
    Position = None
    StartPoint = None
    Thickness = None
    Type = None


class dotTaskDependency_t(object):
    # no doc
    Lag = None
    Local = None
    ModelObject = None
    PrimaryId = None
    SecondaryId = None
    Type = None


class dotTaskObjectAttacher_t(object):
    # no doc
    aObjects = None
    Functionality = None
    ModelObject = None
    nObjects = None


class dotTaskWorktype_t(object):
    # no doc
    aName = None
    ModelObject = None


class dotTask_t(object):
    # no doc
    ActualEndDate = None
    ActualStartDate = None
    ActualWorkAmount = None
    aDescription = None
    aName = None
    aUrl = None
    Completeness = None
    Critical = None
    Local = None
    ModelObject = None
    PlannedEndDate = None
    PlannedStartDate = None
    PlannedWorkAmount = None
    Scenario = None


class dotTemporaryState(object):
    # no doc
    @staticmethod
    def ClearAllStates():
        """ ClearAllStates() -> bool """
        pass

    @staticmethod
    def ClearState(MO):
        """ ClearState(MO: ModelObject) -> bool """
        pass

    @staticmethod
    def SetColor(*__args):
        """
        SetColor(ModelObjects: ArrayList, Color: Color) -> bool
        SetColor(MO: ModelObject, Color: Color) -> bool
        """
        pass

    @staticmethod
    def SetColor_FAST(ModelObjects, Color):
        """ SetColor_FAST(ModelObjects: ArrayList, Color: Color) -> bool """
        pass

    @staticmethod
    def SetState(*__args):
        """
        SetState(ModelObjects: ArrayList, State: dotTemporaryStatesEnum, Transparency: dotTemporaryTransparenciesEnum) -> bool
        SetState(ModelObjects: ArrayList, State: dotTemporaryStatesEnum) -> bool
        SetState(Color: Color) -> bool
        SetState(State: dotTemporaryStatesEnum, Transparency: dotTemporaryTransparenciesEnum) -> bool
        SetState(State: dotTemporaryStatesEnum) -> bool
        SetState(MO: ModelObject, State: dotTemporaryStatesEnum) -> bool
        """
        pass

    @staticmethod
    def SetState_FAST(ModelObjects, State, Transparency=None):
        """
        SetState_FAST(ModelObjects: ArrayList, State: dotTemporaryStatesEnum) -> bool
        SetState_FAST(ModelObjects: ArrayList, State: dotTemporaryStatesEnum, Transparency: dotTemporaryTransparenciesEnum) -> bool
        """
        pass

    OBJECT_MAX_SIZE = 5000
    __all__ = [
        '__reduce_ex__',
        'ClearAllStates',
        'ClearState',
        'OBJECT_MAX_SIZE',
        'SetColor',
        'SetColor_FAST',
        'SetState',
        'SetState_FAST',
    ]


class dotTemporaryStatesEnum(Enum):
    """ enum dotTemporaryStatesEnum, values: DOT_TEMPORARY_STATE_ACCEPTED (8), DOT_TEMPORARY_STATE_ACTIVE (6), DOT_TEMPORARY_STATE_DELETED (3), DOT_TEMPORARY_STATE_DM_ONGOING (4), DOT_TEMPORARY_STATE_MODIFIED (2), DOT_TEMPORARY_STATE_NEW (1), DOT_TEMPORARY_STATE_ORIGINAL (7), DOT_TEMPORARY_STATE_REJECTED (9), DOT_TEMPORARY_STATE_UNCHANGED (5), DOT_TEMPORARY_STATE_UNKNOWN (0), DOT_TEMPORARY_STATE_USE_EXISTING_REPRESENTATION (10) """
    DOT_TEMPORARY_STATE_ACCEPTED = None
    DOT_TEMPORARY_STATE_ACTIVE = None
    DOT_TEMPORARY_STATE_DELETED = None
    DOT_TEMPORARY_STATE_DM_ONGOING = None
    DOT_TEMPORARY_STATE_MODIFIED = None
    DOT_TEMPORARY_STATE_NEW = None
    DOT_TEMPORARY_STATE_ORIGINAL = None
    DOT_TEMPORARY_STATE_REJECTED = None
    DOT_TEMPORARY_STATE_UNCHANGED = None
    DOT_TEMPORARY_STATE_UNKNOWN = None
    DOT_TEMPORARY_STATE_USE_EXISTING_REPRESENTATION = None
    value__ = None


class dotTemporaryTransparenciesEnum(Enum):
    """ enum dotTemporaryTransparenciesEnum, values: DOT_TEMPORARY_TRANSPARENCY_HIDDEN (0), DOT_TEMPORARY_TRANSPARENCY_SEMITRANSPARENT (3), DOT_TEMPORARY_TRANSPARENCY_SEMIVISIBLE (5), DOT_TEMPORARY_TRANSPARENCY_TRANSPARENT (1), DOT_TEMPORARY_TRANSPARENCY_VISIBLE (10) """
    DOT_TEMPORARY_TRANSPARENCY_HIDDEN = None
    DOT_TEMPORARY_TRANSPARENCY_SEMITRANSPARENT = None
    DOT_TEMPORARY_TRANSPARENCY_SEMIVISIBLE = None
    DOT_TEMPORARY_TRANSPARENCY_TRANSPARENT = None
    DOT_TEMPORARY_TRANSPARENCY_VISIBLE = None
    value__ = None


class dotTransformationPlane_t(object):
    """ dotTransformationPlane_t(Size: int) """
    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotTransformationPlane_t]() -> dotTransformationPlane_t
        
        __new__(cls: type, Size: int)
        """
        pass

    MatrixToGlobal = None
    MatrixToLocal = None
    QueryType = None
    ReturnValue = None


class dotUIModelObjectSelector_t(object):
    # no doc
    aObjects = None
    Functionality = None
    nObjects = None
    ShowDimensions = None


class dotUIPicker_t(object):
    """ dotUIPicker_t(Size: int) """
    @staticmethod
    def Construct():
        """ Construct() -> dotUIPicker_t """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Size):
        """
        __new__[dotUIPicker_t]() -> dotUIPicker_t
        
        __new__(cls: type, Size: int)
        """
        pass

    aObjects = None
    aObjectTypes = None
    aX = None
    aY = None
    aZ = None
    MaxPicks = 99
    MoreObjectsLeft = None
    nObjects = None
    nObjectToStart = None
    nPoints = None
    PickCommandStart = None
    PickEnum = None
    PickType = None
    Prompt = None
    SyncCallback = None


class dotUndoOperation_t(object):
    # no doc
    Operation = None


class dotViewSelector_t(object):
    # no doc
    ClientId = None
    SelectorType = None
    ViewCount = None


class dotViewVisibilitySettings_t(object):
    # no doc
    BoltHolesVisible = None
    BoltHolesVisibleInComponents = None
    BoltsVisible = None
    BoltsVisibleInComponents = None
    ComponentsVisible = None
    ComponentsVisibleInComponents = None
    ConstructionLinesVisible = None
    ConstructionPlanesVisible = None
    ConstructionPlanesVisibleInComponents = None
    CutsVisible = None
    CutsVisibleInComponents = None
    FittingsVisible = None
    FittingsVisibleInComponents = None
    GridsVisible = None
    LoadsVisible = None
    PartsVisible = None
    PartsVisibleInComponents = None
    PointsVisible = None
    PointsVisibleInComponents = None
    PourBreaksVisible = None
    PoursVisible = None
    RebarsVisible = None
    RebarsVisibleInComponents = None
    ReferenceObjectsVisible = None
    SurfaceTreatmentsVisible = None
    WeldsVisible = None
    WeldsVisibleInComponents = None


class dotView_t(object):
    # no doc
    aName = None
    aRepresentation = None
    aViewFilter = None
    DisplayCoordinateSystem = None
    DisplayOrientationType = None
    Identifier = None
    MaxPoint = None
    MinPoint = None
    ModifyType = None
    SharedView = None
    ViewCoordinateSystem = None
    ViewDepthDown = None
    ViewDepthUp = None
    ViewProjectionType = None
    ViewRenderingType = None
    VisibilitySettings = None
    ZoomMaxPoint = None
    ZoomMinPoint = None


class dotWeldGeometry_t(object):
    """ dotWeldGeometry_t(weldId: Identifier, position: int, maxPolygonPointsPerRequest: int) """
    def CopyAndInitialize(self):
        """ CopyAndInitialize(self: dotWeldGeometry_t) -> dotWeldGeometry_t """
        pass

    @staticmethod # known case of __new__
    def __new__(self, weldId, position, maxPolygonPointsPerRequest):
        """
        __new__[dotWeldGeometry_t]() -> dotWeldGeometry_t
        
        __new__(cls: type, weldId: Identifier, position: int, maxPolygonPointsPerRequest: int)
        """
        pass

    MaxPolygonPoints = None
    MorePoints = None
    NumberOfPolygons = None
    PointIndex = None
    Polygon = None
    PolygonIndex = None
    Position = None
    WeldId = None


class dotWeld_t(object):
    # no doc
    AngleAbove = None
    AngleBelow = None
    aReferenceText = None
    AroundWeld = None
    ClientId = None
    ConnectAssemblies = None
    ContourAbove = None
    ContourBelow = None
    Direction = None
    EffectiveThroatAbove = None
    EffectiveThroatBelow = None
    ElectrodeClassification = None
    ElectrodeCoefficient = None
    ElectrodeStrength = None
    FinishAbove = None
    FinishBelow = None
    IncrementAmountAbove = None
    IncrementAmountBelow = None
    IntermittentType = None
    LengthAbove = None
    LengthBelow = None
    LogicalWeld = None
    LogicalWeldID = None
    MainObject = None
    ModelObject = None
    NDTInspection = None
    PitchAbove = None
    PitchBelow = None
    Placement = None
    Position = None
    PrefixAboveLine = None
    PrefixBelowLine = None
    Preparation = None
    ProcessType = None
    RootFaceAbove = None
    RootFaceBelow = None
    RootOpeningAbove = None
    RootOpeningBelow = None
    SecondaryObject = None
    ShopWeld = None
    SizeAbove = None
    SizeBelow = None
    Standard = None
    StitchWeld = None
    TypeAbove = None
    TypeBelow = None
    WeldNumber = None
    WeldNumberPrefix = None


class dotWire_t(object):
    # no doc
    aBendingRadiuses = None
    aDiameter = None
    anPolygonPoints = None
    aPositionPoints = None
    ClientIdentifier = None
    GroupIdentifier = None
    nPolygons = None
    UsingLists = None
    WithHooks = None
    WithoutClashes = None


class DoubleList(CollectionBase):
    """
    DoubleList()
    DoubleList(doubles: IEnumerable)
    """
    def Add(self, value):
        """ Add(self: DoubleList, value: float) -> int """
        pass

    def Contains(self, value):
        """ Contains(self: DoubleList, value: float) -> bool """
        pass

    def GetRange(self, index, count):
        """ GetRange(self: DoubleList, index: int, count: int) -> DoubleList """
        pass

    def IndexOf(self, value, startIndex=None, count=None):
        """
        IndexOf(self: DoubleList, value: float, startIndex: int, count: int) -> int
        IndexOf(self: DoubleList, value: float, startIndex: int) -> int
        IndexOf(self: DoubleList, value: float) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: DoubleList, index: int, value: float) """
        pass

    def IsEqual(self, objectToCompare):
        """ IsEqual(self: DoubleList, objectToCompare: object) -> bool """
        pass

    def LastIndexOf(self, value, startIndex=None, count=None):
        """
        LastIndexOf(self: DoubleList, value: float, startIndex: int, count: int) -> int
        LastIndexOf(self: DoubleList, value: float, startIndex: int) -> int
        LastIndexOf(self: DoubleList, value: float) -> int
        """
        pass

    def Remove(self, value):
        """ Remove(self: DoubleList, value: float) """
        pass

    def RemoveRange(self, index, count):
        """ RemoveRange(self: DoubleList, index: int, count: int) """
        pass

    def ToArray(self):
        """ ToArray(self: DoubleList) -> Array[float] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, doubles=None):
        """
        __new__(cls: type)
        __new__(cls: type, doubles: IEnumerable)
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class EventHandlerWrapper(MarshalByRefObject):
    """ EventHandlerWrapper(Instance: IEventHandler, Functionality: WrapperFunctionalityBase) """
    def AddListener(self, EventListener):
        """ AddListener(self: EventHandlerWrapper, EventListener: Events) """
        pass

    def RemoveListener(self, EventListener):
        """ RemoveListener(self: EventHandlerWrapper, EventListener: Events) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Instance, Functionality):
        """ __new__(cls: type, Instance: IEventHandler, Functionality: WrapperFunctionalityBase) """
        pass

    Functionality = None
    Instance = None


class GeometryImporter(object):
    # no doc
    @staticmethod
    def ImportGeometry(connectiveGeometry):
        """ ImportGeometry() -> (bool, ConnectiveGeometry) """
        pass

    GeometryType = None
    __all__ = [
        '__reduce_ex__',
        'GeometryType',
        'ImportGeometry',
    ]


class GeometryTree(object):
    """ GeometryTree(node: IGeometryNode) """
    def AddBranch(self, branchSource, branchRoot):
        """ AddBranch(self: GeometryTree, branchSource: GeometryTree, branchRoot: IGeometryNode) """
        pass

    def AddEdge(self, *__args):
        """ AddEdge(self: GeometryTree, fromIndex: int, toIndex: int)AddEdge(self: GeometryTree, from: IGeometryNode, to: IGeometryNode) """
        pass

    def AddNode(self, node):
        """ AddNode(self: GeometryTree, node: IGeometryNode) -> int """
        pass

    def Clone(self):
        """ Clone(self: GeometryTree) -> GeometryTree """
        pass

    def GetBranch(self, node):
        """ GetBranch(self: GeometryTree, node: IGeometryNode) -> GeometryTree """
        pass

    def GetChildren(self, node):
        """ GetChildren(self: GeometryTree, node: IGeometryNode) -> IList[IGeometryNode] """
        pass

    def GetConnection(self, node1Index, node2Index):
        """ GetConnection(self: GeometryTree, node1Index: int, node2Index: int) -> IList[LineSegment] """
        pass

    def GetGeometryTreeLeafSections(self):
        """ GetGeometryTreeLeafSections(self: GeometryTree) -> IList[GeometrySection] """
        pass

    def GetNeighborSections(self, nodeIndex):
        """ GetNeighborSections(self: GeometryTree, nodeIndex: int) -> IList[GeometrySection] """
        pass

    def GetNodeByIndex(self, index):
        """ GetNodeByIndex(self: GeometryTree, index: int) -> IGeometryNode """
        pass

    def GetNodeId(self, node):
        """ GetNodeId(self: GeometryTree, node: IGeometryNode) -> int """
        pass

    def GetParentNode(self, node):
        """ GetParentNode(self: GeometryTree, node: IGeometryNode) -> IGeometryNode """
        pass

    def IsTransitivelyConnectedTo(self, fromIndex, toIndex):
        """ IsTransitivelyConnectedTo(self: GeometryTree, fromIndex: int, toIndex: int) -> bool """
        pass

    def IsValidId(self, index):
        """ IsValidId(self: GeometryTree, index: int) -> bool """
        pass

    def IsValidLeafToRemove(self, geometrySection):
        """ IsValidLeafToRemove(self: GeometryTree, geometrySection: GeometrySection) -> bool """
        pass

    def RemoveBranch(self, branchRoot):
        """ RemoveBranch(self: GeometryTree, branchRoot: IGeometryNode) """
        pass

    def RemoveEdge(self, *__args):
        """ RemoveEdge(self: GeometryTree, fromIndex: int, toIndex: int)RemoveEdge(self: GeometryTree, from: IGeometryNode, to: IGeometryNode) """
        pass

    def Split(self, nodeIndex):
        """ Split(self: GeometryTree, nodeIndex: int) -> IList[GeometryTree] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, node):
        """ __new__(cls: type, node: IGeometryNode) """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: GeometryTree) -> Dictionary[int, HashSet[int]]

"""

    NodesById = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodesById(self: GeometryTree) -> Dictionary[int, IGeometryNode]

"""

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Root(self: GeometryTree) -> IGeometryNode

Set: Root(self: GeometryTree) = value
"""


    InvalidGeometryNodeId = -1


class ICDelegate:
    # no doc
    def ExplodeBentPlate(self, partId):
        """ ExplodeBentPlate(self: ICDelegate, partId: int) -> int """
        pass

    def ExportAddComponentAttributeToStack(self, pAttr):
        """ ExportAddComponentAttributeToStack(self: ICDelegate, pAttr: dotComponentAttribute_t) -> (int, dotComponentAttribute_t) """
        pass

    def ExportAddComponentInputToStack(self, pObj):
        """ ExportAddComponentInputToStack(self: ICDelegate, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportAddToPourUnit(self, inputPour, clientId):
        """ ExportAddToPourUnit(self: ICDelegate, inputPour: dotPourObject_t, clientId: dotClientId_t) -> (bool, dotPourObject_t, dotClientId_t) """
        pass

    def ExportCalculateContourPolygon(self, pContour, pPolygon):
        """ ExportCalculateContourPolygon(self: ICDelegate, pContour: dotContour_t, pPolygon: dotPolygon_t) -> (int, dotContour_t, dotPolygon_t) """
        pass

    def ExportCalculatePourUnits(self):
        """ ExportCalculatePourUnits(self: ICDelegate) -> bool """
        pass

    def ExportChangeManagerAllowNumbering(self, NumberingFlag):
        """ ExportChangeManagerAllowNumbering(self: ICDelegate, NumberingFlag: bool) -> int """
        pass

    def ExportChangeManagerAllowSave(self, SaveFlag):
        """ ExportChangeManagerAllowSave(self: ICDelegate, SaveFlag: bool) -> int """
        pass

    def ExportCleanDrawingFiles(self, Silent, BackupPath):
        """ ExportCleanDrawingFiles(self: ICDelegate, Silent: bool, BackupPath: str) -> int """
        pass

    def ExportClearAllTemporaryStates(self):
        """ ExportClearAllTemporaryStates(self: ICDelegate) -> int """
        pass

    def ExportClearTemporaryState(self, pObjectId):
        """ ExportClearTemporaryState(self: ICDelegate, pObjectId: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportCommitChanges(self, pModelCommit):
        """ ExportCommitChanges(self: ICDelegate, pModelCommit: dotModelCommit_t) -> (int, dotModelCommit_t) """
        pass

    def ExportCompareFingerprints(self, fingerprint1, fingerprint2):
        """ ExportCompareFingerprints(self: ICDelegate, fingerprint1: str, fingerprint2: str) -> bool """
        pass

    def ExportCompareObjects(self, ObjectId, ObjectToCompareId):
        """ ExportCompareObjects(self: ICDelegate, ObjectId: int, ObjectToCompareId: int) -> int """
        pass

    def ExportConnectGeometryTrees(self, clientId):
        """ ExportConnectGeometryTrees(self: ICDelegate, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPoints(self, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPoints(self: ICDelegate, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesByPointsWithRadius(self, radius, side1Start, side1End, side2Start, side2End, clientId):
        """ ExportConnectGeometryTreesByPointsWithRadius(self: ICDelegate, radius: float, side1Start: dotPoint_t, side1End: dotPoint_t, side2Start: dotPoint_t, side2End: dotPoint_t, clientId: dotClientId_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t, dotPoint_t, dotClientId_t) """
        pass

    def ExportConnectGeometryTreesWithRadius(self, radius, clientId):
        """ ExportConnectGeometryTreesWithRadius(self: ICDelegate, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportCreateBasePoint(self, pBasePoint):
        """ ExportCreateBasePoint(self: ICDelegate, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportCreateBentPlateByFaces(self, part1Id, part2Id, face1, face2):
        """ ExportCreateBentPlateByFaces(self: ICDelegate, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByFacesAndRadius(self, part1Id, part2Id, face1, face2, radius):
        """ ExportCreateBentPlateByFacesAndRadius(self: ICDelegate, part1Id: int, part2Id: int, face1: dotPolygon_t, face2: dotPolygon_t, radius: float) -> (int, dotPolygon_t, dotPolygon_t) """
        pass

    def ExportCreateBentPlateByParts(self, part1Id, part2Id):
        """ ExportCreateBentPlateByParts(self: ICDelegate, part1Id: int, part2Id: int) -> int """
        pass

    def ExportCreateBentPlateByPartsAndRadius(self, part1Id, part2Id, radius):
        """ ExportCreateBentPlateByPartsAndRadius(self: ICDelegate, part1Id: int, part2Id: int, radius: float) -> int """
        pass

    def ExportCreateBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportCreateBoltGroup(self: ICDelegate, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportCreateBooleanPart(self, pBooleanPart):
        """ ExportCreateBooleanPart(self: ICDelegate, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportCreateClipPlane(self, pDotView, pDotClipPlane):
        """ ExportCreateClipPlane(self: ICDelegate, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportCreateComponent(self, pBaseComponent):
        """ ExportCreateComponent(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportCreateControlPlane(self, pControlObject):
        """ ExportCreateControlPlane(self: ICDelegate, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportCreateConversionLink(self, pConversionLink):
        """ ExportCreateConversionLink(self: ICDelegate, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportCreateEdgeChamfer(self, pEdgeChamfer):
        """ ExportCreateEdgeChamfer(self: ICDelegate, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportCreateFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportCreateFittingOrCutPlane(self: ICDelegate, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportCreateGrid(self, pGrid):
        """ ExportCreateGrid(self: ICDelegate, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportCreateGridPlane(self, pGridPlane):
        """ ExportCreateGridPlane(self: ICDelegate, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportCreateGuideline(self, pGuideline):
        """ ExportCreateGuideline(self: ICDelegate, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportCreateIFC(self, aIFC):
        """ ExportCreateIFC(self: ICDelegate, aIFC: dotCreateIFCFromModel_t) -> (int, dotCreateIFCFromModel_t) """
        pass

    def ExportCreateLegFace(self, pLegFace):
        """ ExportCreateLegFace(self: ICDelegate, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportCreateLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportCreateLoad(self: ICDelegate, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportCreateLoadGroup(self, pLoadGroup):
        """ ExportCreateLoadGroup(self: ICDelegate, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportCreateNC(self, aNC):
        """ ExportCreateNC(self: ICDelegate, aNC: dotCreateNCFromModel_t) -> (int, dotCreateNCFromModel_t) """
        pass

    def ExportCreateNewModel(self, pInfo):
        """ ExportCreateNewModel(self: ICDelegate, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportCreatePart(self, pPart, contour):
        """ ExportCreatePart(self: ICDelegate, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportCreatePourBreak(self, pPourBreak):
        """ ExportCreatePourBreak(self: ICDelegate, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportCreateRebarEndDetailStrip(self, pStrip):
        """ ExportCreateRebarEndDetailStrip(self: ICDelegate, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportCreateRebarGroup(self, pRebarGroup):
        """ ExportCreateRebarGroup(self: ICDelegate, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportCreateRebarMesh(self, pRebarMesh):
        """ ExportCreateRebarMesh(self: ICDelegate, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportCreateRebarPropertyStrip(self, pStrip):
        """ ExportCreateRebarPropertyStrip(self: ICDelegate, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportCreateRebarSplice(self, pRebarSplice):
        """ ExportCreateRebarSplice(self: ICDelegate, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportCreateRebarSplitter(self, pStrip):
        """ ExportCreateRebarSplitter(self: ICDelegate, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportCreateRebarStrand(self, pRebarStrand):
        """ ExportCreateRebarStrand(self: ICDelegate, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportCreateReferenceModel(self, pReferenceModel):
        """ ExportCreateReferenceModel(self: ICDelegate, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportCreateReferenceModelObjectAttribute(self, pRMOAttribute):
        """ ExportCreateReferenceModelObjectAttribute(self: ICDelegate, pRMOAttribute: dotReferenceModelObjectAttribute_t) -> (int, dotReferenceModelObjectAttribute_t) """
        pass

    def ExportCreateReferenceModelObjectAttributeEnumerator(self, pEnumerator):
        """ ExportCreateReferenceModelObjectAttributeEnumerator(self: ICDelegate, pEnumerator: dotReferenceModelObjectAttributeEnumerator_t) -> (int, dotReferenceModelObjectAttributeEnumerator_t) """
        pass

    def ExportCreateReport(self, aReport):
        """ ExportCreateReport(self: ICDelegate, aReport: dotCreateReportFromModel_t) -> (int, dotCreateReportFromModel_t) """
        pass

    def ExportCreateSingleRebar(self, pSingleRebar):
        """ ExportCreateSingleRebar(self: ICDelegate, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportCreateSurfaceByFace(self, hitPoint, faceNormal, id):
        """ ExportCreateSurfaceByFace(self: ICDelegate, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceByFaceAndAttrib(self, hitPoint, faceNormal, id, name, surfaceClass):
        """ ExportCreateSurfaceByFaceAndAttrib(self: ICDelegate, hitPoint: dotPoint_t, faceNormal: dotPoint_t, id: int, name: str, surfaceClass: str) -> (int, dotPoint_t, dotPoint_t) """
        pass

    def ExportCreateSurfaceObject(self, pSurfaceObject):
        """ ExportCreateSurfaceObject(self: ICDelegate, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportCreateSurfaceTreatment(self, pTreatment):
        """ ExportCreateSurfaceTreatment(self: ICDelegate, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportCreateTask(self, pTask):
        """ ExportCreateTask(self: ICDelegate, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportCreateTaskDependency(self, pTaskDependency):
        """ ExportCreateTaskDependency(self: ICDelegate, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportCreateTaskWorktype(self, pTaskWorktype):
        """ ExportCreateTaskWorktype(self: ICDelegate, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportCreateWeld(self, pWeld):
        """ ExportCreateWeld(self: ICDelegate, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportDasStartAction(self, ActionName, Parameter):
        """ ExportDasStartAction(self: ICDelegate, ActionName: str, Parameter: str) -> int """
        pass

    def ExportDasStartCommand(self, CommandName, Parameter):
        """ ExportDasStartCommand(self: ICDelegate, CommandName: str, Parameter: str) -> int """
        pass

    def ExportDeleteBasePoint(self, pBasePoint):
        """ ExportDeleteBasePoint(self: ICDelegate, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportDeleteClipPlane(self, pDotView, pDotClipPlane):
        """ ExportDeleteClipPlane(self: ICDelegate, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportDeleteConversionLink(self, pConversionLink):
        """ ExportDeleteConversionLink(self: ICDelegate, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportDeleteObject(self, pIdentifier):
        """ ExportDeleteObject(self: ICDelegate, pIdentifier: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportDisplayAutoDefaultSettings(self, pBaseComponent):
        """ ExportDisplayAutoDefaultSettings(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayComponentHelp(self, pBaseComponent):
        """ ExportDisplayComponentHelp(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportDisplayPrompt(self, Message):
        """ ExportDisplayPrompt(self: ICDelegate, Message: str) -> int """
        pass

    def ExportDisplayReport(self, FileName):
        """ ExportDisplayReport(self: ICDelegate, FileName: str) -> int """
        pass

    def ExportDoubleListHandler(self, pDoubleList):
        """ ExportDoubleListHandler(self: ICDelegate, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ExportDrawTemporaryPolygonSurface(self, pArgument):
        """ ExportDrawTemporaryPolygonSurface(self: ICDelegate, pArgument: dotDrawPolygonSurface_t) -> (int, dotDrawPolygonSurface_t) """
        pass

    def ExportDrawTemporaryPolyLine(self, pArgument):
        """ ExportDrawTemporaryPolyLine(self: ICDelegate, pArgument: dotDrawPolyLine_t) -> (int, dotDrawPolyLine_t) """
        pass

    def ExportDrawTemporaryPolyLineWithId(self, pArgument):
        """ ExportDrawTemporaryPolyLineWithId(self: ICDelegate, pArgument: dotGraphicPolyLine_t) -> (int, dotGraphicPolyLine_t) """
        pass

    def ExportDrawTemporaryText(self, pArgument):
        """ ExportDrawTemporaryText(self: ICDelegate, pArgument: dotDrawText_t) -> (int, dotDrawText_t) """
        pass

    def ExportEdgeListHandler(self, pEdgeList):
        """ ExportEdgeListHandler(self: ICDelegate, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ExportEnumerateObjects(self, pEnumerator):
        """ ExportEnumerateObjects(self: ICDelegate, pEnumerator: dotEnumerator_t) -> (int, dotEnumerator_t) """
        pass

    def ExportExtractBentPlateFromComponent(self, partId):
        """ ExportExtractBentPlateFromComponent(self: ICDelegate, partId: int) -> int """
        pass

    def ExportFingerprint(self, pInput, fingerprint):
        """ ExportFingerprint(self: ICDelegate, pInput: dotPolymesh_t, fingerprint: str) -> (int, dotPolymesh_t, str) """
        pass

    def ExportFormatProfile(self, profile):
        """ ExportFormatProfile(self: ICDelegate, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportGetAllProperties(self, pProperties, pNames, pValues):
        """ ExportGetAllProperties(self: ICDelegate, pProperties: dotGetProperties_t, pNames: List[object], pValues: List[object]) -> (int, dotGetProperties_t, List[object], List[object]) """
        pass

    def ExportGetAllReportProperties(self, pProperties):
        """ ExportGetAllReportProperties(self: ICDelegate, pProperties: List[dotGetProperties_t]) -> (int, List[dotGetProperties_t]) """
        pass

    def ExportGetAssociateSurfaces(self, id):
        """ ExportGetAssociateSurfaces(self: ICDelegate, id: int) -> List[int] """
        pass

    def ExportGetBasePoints(self, ClientId):
        """ ExportGetBasePoints(self: ICDelegate, ClientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportGetBentPlateMaximumRadius(self, geometryNodeId, clientId):
        """ ExportGetBentPlateMaximumRadius(self: ICDelegate, geometryNodeId: int, clientId: dotClientId_t) -> (float, dotClientId_t) """
        pass

    def ExportGetBentPlateMinimumRadius(self, partId):
        """ ExportGetBentPlateMinimumRadius(self: ICDelegate, partId: int) -> float """
        pass

    def ExportGetClipPlanes(self, pDotView, pDotGetClipPlanes):
        """ ExportGetClipPlanes(self: ICDelegate, pDotView: dotView_t, pDotGetClipPlanes: dotGetClipPlanes_t) -> (int, dotView_t, dotGetClipPlanes_t) """
        pass

    def ExportGetColorRepresentationForObject(self, pIdentifier, pColor):
        """ ExportGetColorRepresentationForObject(self: ICDelegate, pIdentifier: dotIdentifier_t, pColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportGetCommandStatus(self, TSCommand, TSCommandParam, Status):
        """ ExportGetCommandStatus(self: ICDelegate, TSCommand: str, TSCommandParam: str, Status: bool) -> (int, str, str, bool) """
        pass

    def ExportGetCommitData(self, pId, pObjectType, pObjectSubType, pCommitType):
        """ ExportGetCommitData(self: ICDelegate, pId: dotIdentifier_t, pObjectType: int, pObjectSubType: int, pCommitType: int) -> (int, dotIdentifier_t, int, int, int) """
        pass

    def ExportGetComponentAttribute(self, pIdentifier, pAttribute):
        """ ExportGetComponentAttribute(self: ICDelegate, pIdentifier: dotIdentifier_t, pAttribute: dotComponentAttribute_t) -> (int, dotIdentifier_t, dotComponentAttribute_t) """
        pass

    def ExportGetComponentInput(self, pObj):
        """ ExportGetComponentInput(self: ICDelegate, pObj: dotComponentInputObject_t) -> (int, dotComponentInputObject_t) """
        pass

    def ExportGetCoordinateSystem(self, pModelObject, pCoordinateSystem):
        """ ExportGetCoordinateSystem(self: ICDelegate, pModelObject: dotModelObject_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotModelObject_t, dotCoordinateSystem_t) """
        pass

    def ExportGetCutSolidSerialized(self, dotSolid1, dotSolid2, serializedFaceList, serializedVectorList, serializedFaceOriginPartIdList, serializedShellIndexList, serializedEdgeVertexList, serializedEdgeTypeList, serializedEdgeShellIndexList):
        """ ExportGetCutSolidSerialized(self: ICDelegate, dotSolid1: dotSolid_t, dotSolid2: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedFaceOriginPartIdList: List[int], serializedShellIndexList: List[int], serializedEdgeVertexList: List[dotPoint_t], serializedEdgeTypeList: List[int], serializedEdgeShellIndexList: List[int]) -> (int, dotSolid_t, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetDatabaseVersion(self, version):
        """ ExportGetDatabaseVersion(self: ICDelegate, version: int) -> (int, int) """
        pass

    def ExportGetDataBaseVersionInfoFromModel(self, pInfo):
        """ ExportGetDataBaseVersionInfoFromModel(self: ICDelegate, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetDetectedClash(self, pClash):
        """ ExportGetDetectedClash(self: ICDelegate, pClash: dotClash_t) -> (int, dotClash_t) """
        pass

    def ExportGetDotType(self, pModelObject):
        """ ExportGetDotType(self: ICDelegate, pModelObject: dotModelObject_t) -> (int, dotModelObject_t) """
        pass

    def ExportGetFatherComponent(self, ObjectId, FatherComponentId):
        """ ExportGetFatherComponent(self: ICDelegate, ObjectId: int, FatherComponentId: int) -> (int, int) """
        pass

    def ExportGetIntersectionBoundingBoxes(self, Identifier1, Identifier2, ClientId):
        """ ExportGetIntersectionBoundingBoxes(self: ICDelegate, Identifier1: dotIdentifier_t, Identifier2: dotIdentifier_t, ClientId: dotClientId_t) -> (int, dotIdentifier_t, dotIdentifier_t, dotClientId_t) """
        pass

    def ExportGetIntersectionPoints(self, pIntersectionPoints):
        """ ExportGetIntersectionPoints(self: ICDelegate, pIntersectionPoints: dotIntersectionPoints_t) -> (int, dotIntersectionPoints_t) """
        pass

    def ExportGetIntersectionSolid(self, pSolid):
        """ ExportGetIntersectionSolid(self: ICDelegate, pSolid: dotIntersectionSolid_t) -> (int, dotIntersectionSolid_t) """
        pass

    def ExportGetModificationStamp(self, pModStmp):
        """ ExportGetModificationStamp(self: ICDelegate, pModStmp: dotModificationStamp_t) -> (int, dotModificationStamp_t) """
        pass

    def ExportGetModificationStampGuid(self, pModStmp):
        """ ExportGetModificationStampGuid(self: ICDelegate, pModStmp: str) -> (int, str) """
        pass

    def ExportGetNumberingUpToDate(self, pNumberingQuery):
        """ ExportGetNumberingUpToDate(self: ICDelegate, pNumberingQuery: dotNumberingQuery_t) -> (int, dotNumberingQuery_t) """
        pass

    def ExportGetNumberOfClashes(self, pClashes):
        """ ExportGetNumberOfClashes(self: ICDelegate, pClashes: int) -> (int, int) """
        pass

    def ExportGetObjectLastModified(self, pIdentifier, pTime, pLocallyModified):
        """ ExportGetObjectLastModified(self: ICDelegate, pIdentifier: dotIdentifier_t, pTime: int, pLocallyModified: bool) -> (int, dotIdentifier_t, int, bool) """
        pass

    def ExportGetObjectPhase(self, pArgument):
        """ ExportGetObjectPhase(self: ICDelegate, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportGetParentObject(self, surfaceId):
        """ ExportGetParentObject(self: ICDelegate, surfaceId: int) -> int """
        pass

    def ExportGetPartLine(self, pPartLine):
        """ ExportGetPartLine(self: ICDelegate, pPartLine: dotPartLine_t) -> (int, dotPartLine_t) """
        pass

    def ExportGetPartMark(self, pPartMark):
        """ ExportGetPartMark(self: ICDelegate, pPartMark: dotPartMark_t) -> (int, dotPartMark_t) """
        pass

    def ExportGetPhaseNumbers(self, pArgument):
        """ ExportGetPhaseNumbers(self: ICDelegate, pArgument: dotPhaseNumbers_t) -> (int, dotPhaseNumbers_t) """
        pass

    def ExportGetPlane(self, pPlane):
        """ ExportGetPlane(self: ICDelegate, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportGetPolybeamCoordinateSystem(self, Id, SubId, Chamfered, pX, pY, pZ):
        """ ExportGetPolybeamCoordinateSystem(self: ICDelegate, Id: int, SubId: int, Chamfered: int, pX: dotPoint_t, pY: dotPoint_t, pZ: dotPoint_t) -> (int, dotPoint_t, dotPoint_t, dotPoint_t) """
        pass

    def ExportGetProjectInfo(self, pInfo):
        """ ExportGetProjectInfo(self: ICDelegate, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportGetProperties(self, pProperties):
        """ ExportGetProperties(self: ICDelegate, pProperties: dotGetProperties_t) -> (int, dotGetProperties_t) """
        pass

    def ExportGetReferenceModelObjectByExternalGuid(self, referenceModelId, externalGuid):
        """ ExportGetReferenceModelObjectByExternalGuid(self: ICDelegate, referenceModelId: int, externalGuid: dotIdentifier_t) -> (int, dotIdentifier_t) """
        pass

    def ExportGetReferenceModelRevisionIds(self, pReferenceModel, ClientId):
        """ ExportGetReferenceModelRevisionIds(self: ICDelegate, pReferenceModel: dotReferenceModel_t, ClientId: dotClientId_t) -> (int, dotReferenceModel_t, dotClientId_t) """
        pass

    def ExportGetSetModelInfo(self, pInfo):
        """ ExportGetSetModelInfo(self: ICDelegate, pInfo: dotModelInfo_t) -> (int, dotModelInfo_t) """
        pass

    def ExportGetSetModstamp(self, ModStampData):
        """ ExportGetSetModstamp(self: ICDelegate, ModStampData: dotModStamp_t) -> (int, dotModStamp_t) """
        pass

    def ExportGetSnapshotFromDatabase(self, Enumerator, SelectInstances):
        """ ExportGetSnapshotFromDatabase(self: ICDelegate, Enumerator: dotEnumerator_t, SelectInstances: bool) -> (Serializable[List[ModelObject]], dotEnumerator_t) """
        pass

    def ExportGetSolid(self, pSolid):
        """ ExportGetSolid(self: ICDelegate, pSolid: dotSolid_t) -> (int, dotSolid_t) """
        pass

    def ExportGetSolidBrep(self, polymeshToClean, polymeshCleaned):
        """ ExportGetSolidBrep(self: ICDelegate, polymeshToClean: dotPolymesh_t, polymeshCleaned: dotPolymesh_t) -> (bool, dotPolymesh_t, dotPolymesh_t) """
        pass

    def ExportGetSolidMerged(self, dotSolid, polymeshes):
        """ ExportGetSolidMerged(self: ICDelegate, dotSolid: dotSolid_t, polymeshes: dotPolymesh_t) -> (int, dotSolid_t, dotPolymesh_t) """
        pass

    def ExportGetSolidSerialized(self, dotSolid, serializedFaceList, serializedVectorList, serializedShellIndexList, serializedFaceOriginIdList):
        """ ExportGetSolidSerialized(self: ICDelegate, dotSolid: dotSolid_t, serializedFaceList: List[List[List[dotPoint_t]]], serializedVectorList: List[dotPoint_t], serializedShellIndexList: List[int], serializedFaceOriginIdList: List[int]) -> (int, dotSolid_t, List[List[List[dotPoint_t]]], List[dotPoint_t], List[int], List[int]) """
        pass

    def ExportGetStringPropertyFromDatabase(self, pProperty, stringValues):
        """ ExportGetStringPropertyFromDatabase(self: ICDelegate, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportGetSurfaceGeometryType(self, surfaceId):
        """ ExportGetSurfaceGeometryType(self: ICDelegate, surfaceId: int) -> int """
        pass

    def ExportGetTrackEvent(self, category, eventName, eventContent):
        """ ExportGetTrackEvent(self: ICDelegate, category: str, eventName: str, eventContent: str) -> (int, str, str, str) """
        pass

    def ExportGetTransformationPlane(self, pPlane):
        """ ExportGetTransformationPlane(self: ICDelegate, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportGetViewCamera(self, pDotView, pDotCamera):
        """ ExportGetViewCamera(self: ICDelegate, pDotView: dotView_t, pDotCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportGetViews(self, pViews):
        """ ExportGetViews(self: ICDelegate, pViews: dotViewSelector_t) -> (int, dotViewSelector_t) """
        pass

    def ExportGetWeldGeometry(self, pWeldGeometry):
        """ ExportGetWeldGeometry(self: ICDelegate, pWeldGeometry: dotWeldGeometry_t) -> (int, dotWeldGeometry_t) """
        pass

    def ExportGetWriteOutStampGuid(self, pModStmp):
        """ ExportGetWriteOutStampGuid(self: ICDelegate, pModStmp: str) -> (int, str) """
        pass

    def ExportHierarchicDefinition(self, pHierarchicDefinition):
        """ ExportHierarchicDefinition(self: ICDelegate, pHierarchicDefinition: dotHierarchicDefinition_t) -> (int, dotHierarchicDefinition_t) """
        pass

    def ExportHierarchicObject(self, pHierarchicObject):
        """ ExportHierarchicObject(self: ICDelegate, pHierarchicObject: dotHierarchicObject_t) -> (int, dotHierarchicObject_t) """
        pass

    def ExportHierarchicObjectChildrenOperation(self, pHierarchicList):
        """ ExportHierarchicObjectChildrenOperation(self: ICDelegate, pHierarchicList: dotHierarchicList_t) -> (int, dotHierarchicList_t) """
        pass

    def ExportInitializeComponentStacks(self):
        """ ExportInitializeComponentStacks(self: ICDelegate) -> int """
        pass

    def ExportInsertView(self, View):
        """ ExportInsertView(self: ICDelegate, View: dotView_t) -> (int, dotView_t) """
        pass

    def ExportIntListHandler(self, pIntList):
        """ ExportIntListHandler(self: ICDelegate, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ExportLoadComponentAttributes(self, pBaseComponent):
        """ ExportLoadComponentAttributes(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportManipulateObject(self, pArgument):
        """ ExportManipulateObject(self: ICDelegate, pArgument: dotManipulateObject_t) -> (int, dotManipulateObject_t) """
        pass

    def ExportModifyAssembly(self, pAssembly):
        """ ExportModifyAssembly(self: ICDelegate, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportModifyBasePoint(self, pBasePoint):
        """ ExportModifyBasePoint(self: ICDelegate, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportModifyBentPlate(self, pPart):
        """ ExportModifyBentPlate(self: ICDelegate, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportModifyBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportModifyBoltGroup(self: ICDelegate, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportModifyBooleanPart(self, pBooleanPart):
        """ ExportModifyBooleanPart(self: ICDelegate, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportModifyClipPlane(self, pDotView, pDotClipPlane):
        """ ExportModifyClipPlane(self: ICDelegate, pDotView: dotView_t, pDotClipPlane: dotClipPlane_t) -> (int, dotView_t, dotClipPlane_t) """
        pass

    def ExportModifyComponent(self, pBaseComponent):
        """ ExportModifyComponent(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportModifyControlPlane(self, pControlObject):
        """ ExportModifyControlPlane(self: ICDelegate, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportModifyCylindricalSurfaceNode(self, geometryNodeId, surfacePoints, clientId):
        """ ExportModifyCylindricalSurfaceNode(self: ICDelegate, geometryNodeId: int, surfacePoints: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyEdgeChamfer(self, pEdgeChamfer):
        """ ExportModifyEdgeChamfer(self: ICDelegate, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportModifyFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportModifyFittingOrCutPlane(self: ICDelegate, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeCurveType(self, geometryNodeId, newCurveType, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeCurveType(self: ICDelegate, geometryNodeId: int, newCurveType: int, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreeCylindricalNodeRadius(self, geometryNodeId, radius, clientId):
        """ ExportModifyGeometryTreeCylindricalNodeRadius(self: ICDelegate, geometryNodeId: int, radius: float, clientId: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportModifyGeometryTreePolygonNode(self, geometryNodeId, contour, clientId):
        """ ExportModifyGeometryTreePolygonNode(self: ICDelegate, geometryNodeId: int, contour: dotContour_t, clientId: dotClientId_t) -> (int, dotContour_t, dotClientId_t) """
        pass

    def ExportModifyGrid(self, pGrid):
        """ ExportModifyGrid(self: ICDelegate, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportModifyGridPlane(self, pGridPlane):
        """ ExportModifyGridPlane(self: ICDelegate, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportModifyLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportModifyLoad(self: ICDelegate, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportModifyLoadGroup(self, pLoadGroup):
        """ ExportModifyLoadGroup(self: ICDelegate, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportModifyPart(self, pPart, contour):
        """ ExportModifyPart(self: ICDelegate, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportModifyPourBreak(self, pPourBreak):
        """ ExportModifyPourBreak(self: ICDelegate, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportModifyPourObject(self, pPourObject):
        """ ExportModifyPourObject(self: ICDelegate, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportModifyProjectInfo(self, pInfo):
        """ ExportModifyProjectInfo(self: ICDelegate, pInfo: dotProjectInfo_t) -> (int, dotProjectInfo_t) """
        pass

    def ExportModifyRebarEndDetailStrip(self, pStrip):
        """ ExportModifyRebarEndDetailStrip(self: ICDelegate, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportModifyRebarGroup(self, pRebarGroup):
        """ ExportModifyRebarGroup(self: ICDelegate, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportModifyRebarMesh(self, pRebarMesh):
        """ ExportModifyRebarMesh(self: ICDelegate, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportModifyRebarPropertyStrip(self, pStrip):
        """ ExportModifyRebarPropertyStrip(self: ICDelegate, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportModifyRebarSplice(self, pRebarSplice):
        """ ExportModifyRebarSplice(self: ICDelegate, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportModifyRebarSplitter(self, pStrip):
        """ ExportModifyRebarSplitter(self: ICDelegate, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportModifyRebarStrand(self, pRebarStrand):
        """ ExportModifyRebarStrand(self: ICDelegate, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportModifyReferenceModel(self, pReferenceModel):
        """ ExportModifyReferenceModel(self: ICDelegate, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportModifySingleRebar(self, pSingleRebar):
        """ ExportModifySingleRebar(self: ICDelegate, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportModifySurfaceObject(self, pSurfaceObject):
        """ ExportModifySurfaceObject(self: ICDelegate, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportModifySurfaceTreatment(self, pTreatment):
        """ ExportModifySurfaceTreatment(self: ICDelegate, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportModifyTask(self, pTask):
        """ ExportModifyTask(self: ICDelegate, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportModifyTaskDependency(self, pTaskDependency):
        """ ExportModifyTaskDependency(self: ICDelegate, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportModifyTaskWorktype(self, pTaskWorktype):
        """ ExportModifyTaskWorktype(self: ICDelegate, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportModifyView(self, View):
        """ ExportModifyView(self: ICDelegate, View: dotView_t) -> (int, dotView_t) """
        pass

    def ExportModifyWeld(self, pWeld):
        """ ExportModifyWeld(self: ICDelegate, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportModStampCompare(self, ModStampCompare):
        """ ExportModStampCompare(self: ICDelegate, ModStampCompare: dotModStampCompare_t) -> (int, dotModStampCompare_t) """
        pass

    def ExportObjectMatchesToFilter(self, pObjectId, FileName):
        """ ExportObjectMatchesToFilter(self: ICDelegate, pObjectId: dotIdentifier_t, FileName: str) -> (int, dotIdentifier_t) """
        pass

    def ExportParseProfile(self, profile):
        """ ExportParseProfile(self: ICDelegate, profile: dotProfile_t) -> (int, dotProfile_t) """
        pass

    def ExportPointListHandler(self, pPointList):
        """ ExportPointListHandler(self: ICDelegate, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ExportProgressBarOperation(self, pProgressBar):
        """ ExportProgressBarOperation(self: ICDelegate, pProgressBar: dotProgressBar_t) -> (int, dotProgressBar_t) """
        pass

    def ExportRebarSetAdditionFunction(self, action, pRebarSet):
        """ ExportRebarSetAdditionFunction(self: ICDelegate, action: RebarSetAction, pRebarSet: dotRebarSetAddition_t) -> (int, dotRebarSetAddition_t) """
        pass

    def ExportRebarSetFunction(self, action, pRebarSet):
        """ ExportRebarSetFunction(self: ICDelegate, action: RebarSetAction, pRebarSet: dotRebarSet_t) -> (int, dotRebarSet_t) """
        pass

    def ExportRefreshReferenceFile(self, pReferenceModel):
        """ ExportRefreshReferenceFile(self: ICDelegate, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportRemoveFromPourUnit(self, clientId):
        """ ExportRemoveFromPourUnit(self: ICDelegate, clientId: dotClientId_t) -> (bool, dotClientId_t) """
        pass

    def ExportRemoveTemporaryGraphicsObjects(self, pArgument):
        """ ExportRemoveTemporaryGraphicsObjects(self: ICDelegate, pArgument: dotClientId_t) -> (int, dotClientId_t) """
        pass

    def ExportRunMacro(self, FileName):
        """ ExportRunMacro(self: ICDelegate, FileName: str) -> int """
        pass

    def ExportRunOrStopClashCheck(self, RunningClashCheck):
        """ ExportRunOrStopClashCheck(self: ICDelegate, RunningClashCheck: bool) -> int """
        pass

    def ExportSaveAsWebModel(self, pSaveAsWebModel):
        """ ExportSaveAsWebModel(self: ICDelegate, pSaveAsWebModel: dotSaveAsWebModel_t) -> (int, dotSaveAsWebModel_t) """
        pass

    def ExportSaveOperation(self, pOperation):
        """ ExportSaveOperation(self: ICDelegate, pOperation: dotSaveOperation_t) -> (int, dotSaveOperation_t) """
        pass

    def ExportSelectAssembly(self, pAssembly):
        """ ExportSelectAssembly(self: ICDelegate, pAssembly: dotAssembly_t) -> (int, dotAssembly_t) """
        pass

    def ExportSelectBasePoint(self, guid, pBasePoint):
        """ ExportSelectBasePoint(self: ICDelegate, guid: str, pBasePoint: dotBasePointData_t) -> (int, dotBasePointData_t) """
        pass

    def ExportSelectBentPlate(self, pPart):
        """ ExportSelectBentPlate(self: ICDelegate, pPart: dotPart_t) -> (int, dotPart_t) """
        pass

    def ExportSelectBoltGroup(self, pBoltShapeData, pBoltGroup):
        """ ExportSelectBoltGroup(self: ICDelegate, pBoltShapeData: dotBoltShapeData_t, pBoltGroup: dotBoltGroup_t) -> (int, dotBoltShapeData_t, dotBoltGroup_t) """
        pass

    def ExportSelectBooleanPart(self, pBooleanPart):
        """ ExportSelectBooleanPart(self: ICDelegate, pBooleanPart: dotBooleanPart_t) -> (int, dotBooleanPart_t) """
        pass

    def ExportSelectComponent(self, pBaseComponent):
        """ ExportSelectComponent(self: ICDelegate, pBaseComponent: dotBaseComponent_t) -> (int, dotBaseComponent_t) """
        pass

    def ExportSelectControlPlane(self, pControlObject):
        """ ExportSelectControlPlane(self: ICDelegate, pControlObject: dotControlObject_t) -> (int, dotControlObject_t) """
        pass

    def ExportSelectConversionLink(self, pConversionLink):
        """ ExportSelectConversionLink(self: ICDelegate, pConversionLink: dotConversionLink_t) -> (int, dotConversionLink_t) """
        pass

    def ExportSelectEdgeChamfer(self, pEdgeChamfer):
        """ ExportSelectEdgeChamfer(self: ICDelegate, pEdgeChamfer: dotEdgeChamfer_t) -> (int, dotEdgeChamfer_t) """
        pass

    def ExportSelectFittingOrCutPlane(self, pFittingOrCutPlane):
        """ ExportSelectFittingOrCutPlane(self: ICDelegate, pFittingOrCutPlane: dotFittingOrCutPlane_t) -> (int, dotFittingOrCutPlane_t) """
        pass

    def ExportSelectGrid(self, pGrid):
        """ ExportSelectGrid(self: ICDelegate, pGrid: dotGrid_t) -> (int, dotGrid_t) """
        pass

    def ExportSelectGridPlane(self, pGridPlane):
        """ ExportSelectGridPlane(self: ICDelegate, pGridPlane: dotGridPlane_t) -> (int, dotGridPlane_t) """
        pass

    def ExportSelectGuideline(self, pGuideline):
        """ ExportSelectGuideline(self: ICDelegate, pGuideline: dotGuideline_t) -> (int, dotGuideline_t) """
        pass

    def ExportSelectLegFace(self, pLegFace):
        """ ExportSelectLegFace(self: ICDelegate, pLegFace: dotLegFace_t) -> (int, dotLegFace_t) """
        pass

    def ExportSelectLoad(self, pLoadCommonAttributes, pLoadClassAttributes):
        """ ExportSelectLoad(self: ICDelegate, pLoadCommonAttributes: dotLoadCommonAttributes_t, pLoadClassAttributes: dotLoadClassAttributes_t) -> (int, dotLoadCommonAttributes_t, dotLoadClassAttributes_t) """
        pass

    def ExportSelectLoadGroup(self, pLoadGroup):
        """ ExportSelectLoadGroup(self: ICDelegate, pLoadGroup: dotLoadGroup_t) -> (int, dotLoadGroup_t) """
        pass

    def ExportSelectPart(self, pPart, contour):
        """ ExportSelectPart(self: ICDelegate, pPart: dotPart_t, contour: List[dotContourPoint_t]) -> (int, dotPart_t, List[dotContourPoint_t]) """
        pass

    def ExportSelectPourBreak(self, pPourBreak):
        """ ExportSelectPourBreak(self: ICDelegate, pPourBreak: dotPolymeshObject_t) -> (int, dotPolymeshObject_t) """
        pass

    def ExportSelectPourObject(self, pPourObject):
        """ ExportSelectPourObject(self: ICDelegate, pPourObject: dotPourObject_t) -> (int, dotPourObject_t) """
        pass

    def ExportSelectRebarBars(self, pWire):
        """ ExportSelectRebarBars(self: ICDelegate, pWire: dotWire_t) -> (int, dotWire_t) """
        pass

    def ExportSelectRebarEndDetailStrip(self, pStrip):
        """ ExportSelectRebarEndDetailStrip(self: ICDelegate, pStrip: dotRebarEndDetailStrip_t) -> (int, dotRebarEndDetailStrip_t) """
        pass

    def ExportSelectRebarGroup(self, pRebarGroup):
        """ ExportSelectRebarGroup(self: ICDelegate, pRebarGroup: dotRebarGroup_t) -> (int, dotRebarGroup_t) """
        pass

    def ExportSelectRebarMesh(self, pRebarMesh):
        """ ExportSelectRebarMesh(self: ICDelegate, pRebarMesh: dotRebarMesh_t) -> (int, dotRebarMesh_t) """
        pass

    def ExportSelectRebarPropertyStrip(self, pStrip):
        """ ExportSelectRebarPropertyStrip(self: ICDelegate, pStrip: dotRebarPropertyStrip_t) -> (int, dotRebarPropertyStrip_t) """
        pass

    def ExportSelectRebarSplice(self, pRebarSplice):
        """ ExportSelectRebarSplice(self: ICDelegate, pRebarSplice: dotRebarSplice_t) -> (int, dotRebarSplice_t) """
        pass

    def ExportSelectRebarSplitter(self, pStrip):
        """ ExportSelectRebarSplitter(self: ICDelegate, pStrip: dotRebarSplitter_t) -> (int, dotRebarSplitter_t) """
        pass

    def ExportSelectRebarStrand(self, pRebarStrand):
        """ ExportSelectRebarStrand(self: ICDelegate, pRebarStrand: dotRebarStrand_t) -> (int, dotRebarStrand_t) """
        pass

    def ExportSelectReferenceModel(self, pReferenceModel):
        """ ExportSelectReferenceModel(self: ICDelegate, pReferenceModel: dotReferenceModel_t) -> (int, dotReferenceModel_t) """
        pass

    def ExportSelectReferenceModelObject(self, pReferenceModelObject):
        """ ExportSelectReferenceModelObject(self: ICDelegate, pReferenceModelObject: dotReferenceModelObject_t) -> (int, dotReferenceModelObject_t) """
        pass

    def ExportSelectReferenceModelRevision(self, modelId, revisionId, pRevision):
        """ ExportSelectReferenceModelRevision(self: ICDelegate, modelId: int, revisionId: int, pRevision: dotReferenceModelRevision_t) -> (int, dotReferenceModelRevision_t) """
        pass

    def ExportSelectSingleRebar(self, pSingleRebar):
        """ ExportSelectSingleRebar(self: ICDelegate, pSingleRebar: dotSingleRebar_t) -> (int, dotSingleRebar_t) """
        pass

    def ExportSelectSurfaceObject(self, pSurfaceObject):
        """ ExportSelectSurfaceObject(self: ICDelegate, pSurfaceObject: dotSurfaceObject_t) -> (int, dotSurfaceObject_t) """
        pass

    def ExportSelectSurfaceTreatment(self, pTreatment):
        """ ExportSelectSurfaceTreatment(self: ICDelegate, pTreatment: dotSurfaceTreatment_t) -> (int, dotSurfaceTreatment_t) """
        pass

    def ExportSelectTask(self, pTask):
        """ ExportSelectTask(self: ICDelegate, pTask: dotTask_t) -> (int, dotTask_t) """
        pass

    def ExportSelectTaskDependency(self, pTaskDependency):
        """ ExportSelectTaskDependency(self: ICDelegate, pTaskDependency: dotTaskDependency_t) -> (int, dotTaskDependency_t) """
        pass

    def ExportSelectTaskWorktype(self, pTaskWorktype):
        """ ExportSelectTaskWorktype(self: ICDelegate, pTaskWorktype: dotTaskWorktype_t) -> (int, dotTaskWorktype_t) """
        pass

    def ExportSelectView(self, pView):
        """ ExportSelectView(self: ICDelegate, pView: dotView_t) -> (int, dotView_t) """
        pass

    def ExportSelectWeld(self, pWeld):
        """ ExportSelectWeld(self: ICDelegate, pWeld: dotWeld_t) -> (int, dotWeld_t) """
        pass

    def ExportSetAdvancedOption(self, pArgument):
        """ ExportSetAdvancedOption(self: ICDelegate, pArgument: dotGetAdvancedOption_t) -> (int, dotGetAdvancedOption_t) """
        pass

    def ExportSetAsCurrentRevision(self, modelId, revisionId):
        """ ExportSetAsCurrentRevision(self: ICDelegate, modelId: int, revisionId: int) -> int """
        pass

    def ExportSetGetPhaseProperty(self, pArgument):
        """ ExportSetGetPhaseProperty(self: ICDelegate, pArgument: dotSetGetProperty_t) -> (int, dotSetGetProperty_t) """
        pass

    def ExportSetObjectPhase(self, pArgument):
        """ ExportSetObjectPhase(self: ICDelegate, pArgument: dotPhase_t) -> (int, dotPhase_t) """
        pass

    def ExportSetPlane(self, pPlane):
        """ ExportSetPlane(self: ICDelegate, pPlane: dotPlane_t) -> (int, dotPlane_t) """
        pass

    def ExportSetProperty(self, pProperty):
        """ ExportSetProperty(self: ICDelegate, pProperty: dotSetProperty_t) -> (int, dotSetProperty_t) """
        pass

    def ExportSetRepresentation(self, Representation):
        """ ExportSetRepresentation(self: ICDelegate, Representation: str) -> int """
        pass

    def ExportSetStringPropertyToDatabase(self, pProperty, stringValues):
        """ ExportSetStringPropertyToDatabase(self: ICDelegate, pProperty: dotStringProperty_t, stringValues: List[str]) -> (int, dotStringProperty_t, List[str]) """
        pass

    def ExportSetTemporaryColor(self, pObjectId, pNewColor):
        """ ExportSetTemporaryColor(self: ICDelegate, pObjectId: dotIdentifier_t, pNewColor: dotColor_t) -> (int, dotIdentifier_t, dotColor_t) """
        pass

    def ExportSetTemporaryColors(self, pSetTemporaryColors):
        """ ExportSetTemporaryColors(self: ICDelegate, pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryColors_FAST(self, pObjects, pSetTemporaryColors):
        """ ExportSetTemporaryColors_FAST(self: ICDelegate, pObjects: List[Identifier], pSetTemporaryColors: dotSetTemporaryColors_t) -> (int, List[Identifier], dotSetTemporaryColors_t) """
        pass

    def ExportSetTemporaryState(self, pObjectId, pNewState):
        """ ExportSetTemporaryState(self: ICDelegate, pObjectId: dotIdentifier_t, pNewState: dotTemporaryStatesEnum) -> (int, dotIdentifier_t, dotTemporaryStatesEnum) """
        pass

    def ExportSetTemporaryStates(self, pSetTemporaryStates):
        """ ExportSetTemporaryStates(self: ICDelegate, pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, dotSetTemporaryStates_t) """
        pass

    def ExportSetTemporaryStates_FAST(self, pObjects, pSetTemporaryStates):
        """ ExportSetTemporaryStates_FAST(self: ICDelegate, pObjects: List[Identifier], pSetTemporaryStates: dotSetTemporaryStates_t) -> (int, List[Identifier], dotSetTemporaryStates_t) """
        pass

    def ExportSetTransformationPlane(self, pPlane):
        """ ExportSetTransformationPlane(self: ICDelegate, pPlane: dotTransformationPlane_t) -> (int, dotTransformationPlane_t) """
        pass

    def ExportSetViewCamera(self, pDotView, pDotCamera):
        """ ExportSetViewCamera(self: ICDelegate, pDotView: dotView_t, pDotCamera: dotCamera_t) -> (int, dotView_t, dotCamera_t) """
        pass

    def ExportShadowArea(self, pArgument):
        """ ExportShadowArea(self: ICDelegate, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportShadowAreaComplement(self, pArgument):
        """ ExportShadowAreaComplement(self: ICDelegate, pArgument: dotAreaPolygons_t) -> (int, dotAreaPolygons_t) """
        pass

    def ExportSharingOperation(self, pOperation):
        """ ExportSharingOperation(self: ICDelegate, pOperation: dotSharingOperation_t) -> (int, dotSharingOperation_t) """
        pass

    def ExportSingleRebarGetRebarSet(self, singleRebarId):
        """ ExportSingleRebarGetRebarSet(self: ICDelegate, singleRebarId: int) -> int """
        pass

    def ExportStartCustomComponentCreation(self, ComponentName):
        """ ExportStartCustomComponentCreation(self: ICDelegate, ComponentName: str) -> int """
        pass

    def ExportStartPluginCreation(self, ComponentName):
        """ ExportStartPluginCreation(self: ICDelegate, ComponentName: str) -> int """
        pass

    def ExportStringListHandler(self, pStringList):
        """ ExportStringListHandler(self: ICDelegate, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
        pass

    def ExportTaskObjectAttach(self, pSelector):
        """ ExportTaskObjectAttach(self: ICDelegate, pSelector: dotTaskObjectAttacher_t) -> (int, dotTaskObjectAttacher_t) """
        pass

    def ExportUIObjectPick(self, pPicker):
        """ ExportUIObjectPick(self: ICDelegate, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUIObjectSelect(self, pSelector):
        """ ExportUIObjectSelect(self: ICDelegate, pSelector: dotUIModelObjectSelector_t) -> (int, dotUIModelObjectSelector_t) """
        pass

    def ExportUIObjectsPick(self, pPicker):
        """ ExportUIObjectsPick(self: ICDelegate, pPicker: dotUIPicker_t) -> (int, dotUIPicker_t) """
        pass

    def ExportUndoOperation(self, pOperation):
        """ ExportUndoOperation(self: ICDelegate, pOperation: dotUndoOperation_t) -> (int, dotUndoOperation_t) """
        pass

    def ExportValidatePolymesh(self, checkCriteria, polymeshToValidate, invalidInfo):
        """ ExportValidatePolymesh(self: ICDelegate, checkCriteria: int, polymeshToValidate: dotPolymesh_t, invalidInfo: dotPolymeshValidateInvalidInfo_t) -> (bool, dotPolymesh_t, dotPolymeshValidateInvalidInfo_t) """
        pass

    def ExportViewHideUnselected(self, HideCompletely, DrawAsStick):
        """ ExportViewHideUnselected(self: ICDelegate, HideCompletely: bool, DrawAsStick: bool) -> int """
        pass

    def ExportWriteToSessionLog(self, Message):
        """ ExportWriteToSessionLog(self: ICDelegate, Message: str) -> int """
        pass

    def GetDSTVCoordinateSystem(self, PartId, pCoordinateSystem):
        """ GetDSTVCoordinateSystem(self: ICDelegate, PartId: dotIdentifier_t, pCoordinateSystem: dotCoordinateSystem_t) -> (int, dotCoordinateSystem_t) """
        pass

    def ImportDoubleListHandler(self, pDoubleList):
        """ ImportDoubleListHandler(self: ICDelegate, pDoubleList: dotnetDoubleList_t) -> (int, dotnetDoubleList_t) """
        pass

    def ImportEdgeListHandler(self, pEdgeList):
        """ ImportEdgeListHandler(self: ICDelegate, pEdgeList: dotnetEdgeList_t) -> (int, dotnetEdgeList_t) """
        pass

    def ImportIntListHandler(self, pIntList):
        """ ImportIntListHandler(self: ICDelegate, pIntList: dotnetIntList_t) -> (int, dotnetIntList_t) """
        pass

    def ImportPointListHandler(self, pPointList):
        """ ImportPointListHandler(self: ICDelegate, pPointList: dotnetPointList_t) -> (int, dotnetPointList_t) """
        pass

    def ImportStringListHandler(self, pStringList):
        """ ImportStringListHandler(self: ICDelegate, pStringList: dotnetStringList_t) -> (int, dotnetStringList_t) """
        pass

    def IsMacroRunning(self):
        """ IsMacroRunning(self: ICDelegate) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEventHandler:
    # no doc
    def AddListener(self, EventListener):
        """ AddListener(self: IEventHandler, EventListener: Events) """
        pass

    def RemoveListener(self, EventListener):
        """ RemoveListener(self: IEventHandler, EventListener: Events) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IntList(CollectionBase):
    """
    IntList()
    IntList(integers: IEnumerable)
    """
    def Add(self, Value):
        """ Add(self: IntList, Value: int) -> int """
        pass

    def Contains(self, Value):
        """ Contains(self: IntList, Value: int) -> bool """
        pass

    def GetRange(self, Index, Count):
        """ GetRange(self: IntList, Index: int, Count: int) -> IntList """
        pass

    def IndexOf(self, Value, StartIndex=None, Count=None):
        """
        IndexOf(self: IntList, Value: int, StartIndex: int, Count: int) -> int
        IndexOf(self: IntList, Value: int, StartIndex: int) -> int
        IndexOf(self: IntList, Value: int) -> int
        """
        pass

    def Insert(self, Index, Value):
        """ Insert(self: IntList, Index: int, Value: int) """
        pass

    def IsEqual(self, ObjectToCompare):
        """ IsEqual(self: IntList, ObjectToCompare: object) -> bool """
        pass

    def LastIndexOf(self, Value, StartIndex=None, Count=None):
        """
        LastIndexOf(self: IntList, Value: int, StartIndex: int, Count: int) -> int
        LastIndexOf(self: IntList, Value: int, StartIndex: int) -> int
        LastIndexOf(self: IntList, Value: int) -> int
        """
        pass

    def Remove(self, Value):
        """ Remove(self: IntList, Value: int) """
        pass

    def RemoveRange(self, Index, Count):
        """ RemoveRange(self: IntList, Index: int, Count: int) """
        pass

    def ToArray(self):
        """ ToArray(self: IntList) -> Array[int] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, integers=None):
        """
        __new__(cls: type)
        __new__(cls: type, integers: IEnumerable)
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class ModelExtensions(object):
    # no doc
    @staticmethod
    def GetModelObjectType(Model, ID):
        """ GetModelObjectType(Model: Model, ID: Identifier) -> Type """
        pass

    @staticmethod
    def TryGetModelObjectType(Model, ID, ObjectType):
        """ TryGetModelObjectType(Model: Model, ID: Identifier) -> (bool, Type) """
        pass

    __all__ = [
        '__reduce_ex__',
        'GetModelObjectType',
        'TryGetModelObjectType',
    ]


class ModelObjectFactory(object):
    # no doc
    @staticmethod
    def GetCorrectInstance(model, identifier, modelObjectType=None, modelObjectSubType=None):
        """
        GetCorrectInstance(model: Model, identifier: Identifier, modelObjectType: ModelObjectEnum, modelObjectSubType: int) -> ModelObject
        GetCorrectInstance(model: Model, identifier: Identifier) -> ModelObject
        """
        pass

    __all__ = [
        '__reduce_ex__',
        'GetCorrectInstance',
    ]


class NumberingQueryModeEnum(Enum):
    """ enum NumberingQueryModeEnum, values: ALL_PARTS_REBARS_ASSEMBLIES (1), SINGLE_ID (0) """
    ALL_PARTS_REBARS_ASSEMBLIES = None
    SINGLE_ID = None
    value__ = None


class Operation(object):
    # no doc
    @staticmethod
    def AddToPourUnit(inputPour, objectsToBeAdded):
        """ AddToPourUnit(inputPour: PourObject, objectsToBeAdded: List[ModelObject]) -> bool """
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
    def DeleteMacro(fileName, macroLocation):
        """ DeleteMacro(fileName: str, macroLocation: MacroLocationEnum) -> bool """
        pass

    @staticmethod
    def dotAutoSaveModel(Comment, User):
        """ dotAutoSaveModel(Comment: str, User: str) -> bool """
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
    def dotCheckObjectModifiedAfterStamp(objectGuid, ModStamp):
        """ dotCheckObjectModifiedAfterStamp(objectGuid: Guid, ModStamp: str) -> bool """
        pass

    @staticmethod
    def dotCheckProfileDefinitionsModified(ModStamp):
        """ dotCheckProfileDefinitionsModified(ModStamp: str) -> bool """
        pass

    @staticmethod
    def dotCleanDrawingFiles(Silent, BackupPath):
        """ dotCleanDrawingFiles(Silent: bool, BackupPath: str) -> bool """
        pass

    @staticmethod
    def dotClearUndoLog():
        """ dotClearUndoLog() """
        pass

    @staticmethod
    def dotConnectToNewMultiUserServerAndOpenModel(ModelFolder, ServerName):
        """ dotConnectToNewMultiUserServerAndOpenModel(ModelFolder: str, ServerName: str) -> bool """
        pass

    @staticmethod
    def dotConvertAndOpenAsMultiUserModel(ModelFolder, ServerName):
        """ dotConvertAndOpenAsMultiUserModel(ModelFolder: str, ServerName: str) -> bool """
        pass

    @staticmethod
    def dotConvertAndOpenAsSingleUserModel(ModelFolder):
        """ dotConvertAndOpenAsSingleUserModel(ModelFolder: str) -> bool """
        pass

    @staticmethod
    def dotCreateNewMultiUserModel(ModelName, ModelPath, ServerName):
        """ dotCreateNewMultiUserModel(ModelName: str, ModelPath: str, ServerName: str) -> bool """
        pass

    @staticmethod
    def dotCreateNewSharedModel(ModelName, ModelPath):
        """ dotCreateNewSharedModel(ModelName: str, ModelPath: str) -> bool """
        pass

    @staticmethod
    def dotCreateNewSingleUserModel(ModelName, ModelPath):
        """ dotCreateNewSingleUserModel(ModelName: str, ModelPath: str) -> bool """
        pass

    @staticmethod
    def dotCreateNewSingleUserModelFromTemplate(ModelName, ModelPath, ModelTemplateName):
        """ dotCreateNewSingleUserModelFromTemplate(ModelName: str, ModelPath: str, ModelTemplateName: str) -> bool """
        pass

    @staticmethod
    def dotDisplayAutoDefaultSettings(type, componentNumber, componentName):
        """ dotDisplayAutoDefaultSettings(type: ModelObjectEnum, componentNumber: int, componentName: str) -> bool """
        pass

    @staticmethod
    def dotDisplayComponentHelp(type, componentNumber, componentName):
        """ dotDisplayComponentHelp(type: ModelObjectEnum, componentNumber: int, componentName: str) -> bool """
        pass

    @staticmethod
    def dotExcludeFromSharingAndOpen(ModelFolder):
        """ dotExcludeFromSharingAndOpen(ModelFolder: str) -> bool """
        pass

    @staticmethod
    def dotExportGetColorRepresentationForObject(ID, color):
        """ dotExportGetColorRepresentationForObject(ID: int, color: Color) -> (bool, Color) """
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
    def dotGetDataBaseVersionInfoFromModel(ModelName, ModelPath, ModelVersion, CurrentVersion):
        """ dotGetDataBaseVersionInfoFromModel(ModelName: str, ModelPath: str, ModelVersion: int, CurrentVersion: int) -> (bool, int, int) """
        pass

    @staticmethod
    def dotGetDeletedObjecs(ModStamp, ObjectTypes, returnAlsoIfObjectIsCreatedAndDeletedAfterEvent):
        """ dotGetDeletedObjecs(ModStamp: str, ObjectTypes: IEnumerable[ModelObjectEnum], returnAlsoIfObjectIsCreatedAndDeletedAfterEvent: bool) -> ModelObjectEnumerator """
        pass

    @staticmethod
    def dotGetModifications(ModStamp, ObjectTypes, returnAlsoIfObjectIsCreatedAndDeletedAfterEvent):
        """ dotGetModifications(ModStamp: str, ObjectTypes: IEnumerable[ModelObjectEnum], returnAlsoIfObjectIsCreatedAndDeletedAfterEvent: bool) -> ModificationInfo """
        pass

    @staticmethod
    def dotGetModificationsByFilter(ModStamp, FilterName):
        """ dotGetModificationsByFilter(ModStamp: str, FilterName: str) -> ModelObjectEnumerator """
        pass

    @staticmethod
    def dotGetObjectsWithAnyModification(ModStamp, ObjectTypes):
        """ dotGetObjectsWithAnyModification(ModStamp: str, ObjectTypes: IEnumerable[ModelObjectEnum]) -> ModelObjectEnumerator """
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
    def dotQuitProgram(Comment, User):
        """ dotQuitProgram(Comment: str, User: str) -> bool """
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
    def dotSaveAsModel(path, Comment, User):
        """ dotSaveAsModel(path: str, Comment: str, User: str) -> bool """
        pass

    @staticmethod
    def dotSaveModel(Comment, User):
        """ dotSaveModel(Comment: str, User: str) -> bool """
        pass

    @staticmethod
    def dotSetAdvancedOption(VariableName, Value):
        """
        dotSetAdvancedOption(VariableName: str, Value: str) -> bool
        dotSetAdvancedOption(VariableName: str, Value: float) -> bool
        dotSetAdvancedOption(VariableName: str, Value: bool) -> bool
        dotSetAdvancedOption(VariableName: str, Value: int) -> bool
        """
        pass

    @staticmethod
    def dotSetUserModelRole(modelId, modelFolder, userId, role):
        """ dotSetUserModelRole(modelId: Guid, modelFolder: str, userId: Guid, role: DotSharingPrivilegeEnum) -> bool """
        pass

    @staticmethod
    def dotSharingCommandResult(commandId, success, ErrorCode, ErrorDetail):
        """ dotSharingCommandResult(commandId: int, success: bool, ErrorCode: DotSharingErrorCodeEnum, ErrorDetail: str) -> bool """
        pass

    @staticmethod
    def dotSharingCreateEmptyModel(modelName, modelPath):
        """ dotSharingCreateEmptyModel(modelName: str, modelPath: str) -> bool """
        pass

    @staticmethod
    def dotSharingCreateNewModel(modelName, modelPath):
        """ dotSharingCreateNewModel(modelName: str, modelPath: str) -> bool """
        pass

    @staticmethod
    def dotSharingCreateStartSharingBackup(backupFolder):
        """ dotSharingCreateStartSharingBackup(backupFolder: str) -> bool """
        pass

    @staticmethod
    def dotSharingGetVersionGuid(versionGuid):
        """ dotSharingGetVersionGuid(versionGuid: Guid) -> (bool, Guid) """
        pass

    @staticmethod
    def dotSharingIsEnabled():
        """ dotSharingIsEnabled() -> bool """
        pass

    @staticmethod
    def dotSharingLogPrint(type, message):
        """ dotSharingLogPrint(type: DotSharingLogTypeEnum, message: str) """
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
    def dotSharingReadIn(packetFolder, packetNumber, errorCode, errorDetail, moduleBaselines):
        """ dotSharingReadIn(packetFolder: str, packetNumber: int) -> (bool, DotSharingErrorCodeEnum, str, Dictionary[str, Tuple[str, str]]) """
        pass

    @staticmethod
    def dotSharingReadInCommit(success, joiningSharing):
        """ dotSharingReadInCommit(success: bool, joiningSharing: bool) -> bool """
        pass

    @staticmethod
    def dotSharingReadInStarting(joiningSharing):
        """ dotSharingReadInStarting(joiningSharing: bool) -> bool """
        pass

    @staticmethod
    def dotSharingRegisterPlugin(name, asynchronous):
        """ dotSharingRegisterPlugin(name: str, asynchronous: bool) -> bool """
        pass

    @staticmethod
    def dotSharingRestoreStartSharingBackup(backupFolder):
        """ dotSharingRestoreStartSharingBackup(backupFolder: str) -> bool """
        pass

    @staticmethod
    def dotSharingSaveVersionGuid(versionGuid, packetNumber, baselines):
        """ dotSharingSaveVersionGuid(versionGuid: Guid, packetNumber: int, baselines: Dictionary[str, str]) -> bool """
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
    def dotSharingWriteOut(permission, packetFolder, mode, revisionInfo, errorCode, errorDetail, moduleBaselines):
        """ dotSharingWriteOut(permission: DotSharingPrivilegeEnum, packetFolder: str, mode: DotSharingWriteOutModeEnum, revisionInfo: str) -> (bool, DotSharingErrorCodeEnum, str, Dictionary[str, Tuple[str, str]]) """
        pass

    @staticmethod
    def dotSharingWriteOutCommit(success, packetFolder, packetNumber, moduleBaselines):
        """ dotSharingWriteOutCommit(success: bool, packetFolder: str, packetNumber: int) -> (bool, Dictionary[str, Tuple[str, str]]) """
        pass

    @staticmethod
    def dotStartAction(ActionName, Parameters):
        """ dotStartAction(ActionName: str, Parameters: str) -> bool """
        pass

    @staticmethod
    def dotStartCommand(CommandName, Parameters):
        """ dotStartCommand(CommandName: str, Parameters: str) -> bool """
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
    def ExportIFCFromAll(ModelName, FullFileName, ViewType, PropertySets, BasePoint, UseTimer, CreateReport):
        """ ExportIFCFromAll(ModelName: str, FullFileName: str, ViewType: IFCExportViewTypeEnum, PropertySets: List[str], BasePoint: IFCExportBasePoint, UseTimer: bool, CreateReport: bool) -> bool """
        pass

    @staticmethod
    def ExportIFCFromFilteredObjects(ModelName, FullFileName, ViewType, PropertySets, FilterName, BasePoint, UseTimer, CreateReport):
        """ ExportIFCFromFilteredObjects(ModelName: str, FullFileName: str, ViewType: IFCExportViewTypeEnum, PropertySets: List[str], FilterName: str, BasePoint: IFCExportBasePoint, UseTimer: bool, CreateReport: bool) -> bool """
        pass

    @staticmethod
    def ExportIFCFromObjects(ModelName, FullFileName, ViewType, PropertySets, ModelObjects, BasePoint, UseTimer, CreateReport):
        """ ExportIFCFromObjects(ModelName: str, FullFileName: str, ViewType: IFCExportViewTypeEnum, PropertySets: List[str], ModelObjects: List[ModelObject], BasePoint: IFCExportBasePoint, UseTimer: bool, CreateReport: bool) -> bool """
        pass

    @staticmethod
    def ExportIFCFromSelected(ModelName, FullFileName, ViewType, PropertySets, BasePoint, UseTimer, CreateReport):
        """ ExportIFCFromSelected(ModelName: str, FullFileName: str, ViewType: IFCExportViewTypeEnum, PropertySets: List[str], BasePoint: IFCExportBasePoint, UseTimer: bool, CreateReport: bool) -> bool """
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

    DotSharingErrorCodeEnum = None
    DotSharingLogTypeEnum = None
    DotSharingPrivilegeEnum = None
    DotSharingWriteOutModeEnum = None
    IFCExportBasePoint = None
    IFCExportViewTypeEnum = None
    MacroLocationEnum = None
    OperationsMaxMessageLength = 2000
    SaveOperationEnum = None
    SharingOperationEnum = None
    UndoOperationEnum = None
    __all__ = [
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


class PointList(CollectionBase):
    """ PointList() """
    def Add(self, Value):
        """ Add(self: PointList, Value: Point) -> int """
        pass

    def Contains(self, Value):
        """ Contains(self: PointList, Value: Point) -> bool """
        pass

    def GetRange(self, Index, Count):
        """ GetRange(self: PointList, Index: int, Count: int) -> PointList """
        pass

    def IndexOf(self, Value, StartIndex=None, Count=None):
        """
        IndexOf(self: PointList, Value: Point, StartIndex: int, Count: int) -> int
        IndexOf(self: PointList, Value: Point, StartIndex: int) -> int
        IndexOf(self: PointList, Value: Point) -> int
        """
        pass

    def Insert(self, Index, Value):
        """ Insert(self: PointList, Index: int, Value: Point) """
        pass

    def IsEqual(self, ObjectToCompare):
        """ IsEqual(self: PointList, ObjectToCompare: object) -> bool """
        pass

    def LastIndexOf(self, Value, StartIndex=None, Count=None):
        """
        LastIndexOf(self: PointList, Value: Point, StartIndex: int, Count: int) -> int
        LastIndexOf(self: PointList, Value: Point, StartIndex: int) -> int
        LastIndexOf(self: PointList, Value: Point) -> int
        """
        pass

    def Remove(self, Value):
        """ Remove(self: PointList, Value: Point) """
        pass

    def RemoveRange(self, Index, Count):
        """ RemoveRange(self: PointList, Index: int, Count: int) """
        pass

    def ToArray(self):
        """ ToArray(self: PointList) -> Array[Point] """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class PolygonExtensions(object):
    # no doc
    @staticmethod
    def ToDotPolygon(polygon):
        """ ToDotPolygon(polygon: Polygon) -> dotPolygon_t """
        pass

    @staticmethod
    def ToPolygon(dotPolygon):
        """ ToPolygon(dotPolygon: dotPolygon_t) -> Polygon """
        pass

    __all__ = [
        '__reduce_ex__',
        'ToDotPolygon',
        'ToPolygon',
    ]


class RebarSetAction(Enum):
    """ enum RebarSetAction, values: BeginCreate (0), BeginModify (2), BeginSelect (4), EndCreate (1), EndModify (3), EndSelect (5) """
    BeginCreate = None
    BeginModify = None
    BeginSelect = None
    EndCreate = None
    EndModify = None
    EndSelect = None
    value__ = None


class Remoter(object):
    """ Remoter() """
    @staticmethod
    def InitializeSandBox():
        """ InitializeSandBox() -> bool """
        pass


class ScopedCDelegateSetter(object):
    """ ScopedCDelegateSetter(deleg: ICDelegate) """
    def Dispose(self):
        """ Dispose(self: ScopedCDelegateSetter) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, deleg):
        """ __new__(cls: type, deleg: ICDelegate) """
        pass


class Serializer(object):
    """ Serializer() """
    @staticmethod
    def JsonToUDAChanges(json):
        """ JsonToUDAChanges(json: Array[Byte]) -> UDAChanges """
        pass

    @staticmethod
    def JsonToUDAs(json):
        """ JsonToUDAs(json: Array[Byte]) -> Dictionary[str, object] """
        pass


class StringList(CollectionBase):
    """
    StringList(Capacity: int)
    StringList()
    """
    def Add(self, Value):
        """ Add(self: StringList, Value: str) -> int """
        pass

    def Contains(self, Value):
        """ Contains(self: StringList, Value: str) -> bool """
        pass

    def GetRange(self, Index, Count):
        """ GetRange(self: StringList, Index: int, Count: int) -> StringList """
        pass

    def IndexOf(self, Value, StartIndex=None, Count=None):
        """
        IndexOf(self: StringList, Value: str, StartIndex: int, Count: int) -> int
        IndexOf(self: StringList, Value: str, StartIndex: int) -> int
        IndexOf(self: StringList, Value: str) -> int
        """
        pass

    def Insert(self, Index, Value):
        """ Insert(self: StringList, Index: int, Value: str) """
        pass

    def IsEqual(self, ObjectToCompare):
        """ IsEqual(self: StringList, ObjectToCompare: object) -> bool """
        pass

    def LastIndexOf(self, Value, StartIndex=None, Count=None):
        """
        LastIndexOf(self: StringList, Value: str, StartIndex: int, Count: int) -> int
        LastIndexOf(self: StringList, Value: str, StartIndex: int) -> int
        LastIndexOf(self: StringList, Value: str) -> int
        """
        pass

    def Remove(self, Value):
        """ Remove(self: StringList, Value: str) """
        pass

    def RemoveRange(self, Index, Count):
        """ RemoveRange(self: StringList, Index: int, Count: int) """
        pass

    def ToArray(self):
        """ ToArray(self: StringList) -> Array[str] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Capacity=None):
        """
        __new__(cls: type, Capacity: int)
        __new__(cls: type)
        """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class SurfaceObjectCreator(object):
    """ SurfaceObjectCreator() """
    @staticmethod
    def CreateByFace(objectId, hitPoint, faceNormal, name=None, surfaceClass=None):
        """
        CreateByFace(objectId: int, hitPoint: Vector, faceNormal: Vector, name: str, surfaceClass: str) -> SurfaceObject
        CreateByFace(objectId: int, hitPoint: Vector, faceNormal: Vector) -> SurfaceObject
        """
        pass


class SyncHandler(MulticastDelegate):
    """ SyncHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: SyncHandler, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SyncHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: SyncHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class UDAChanges(object):
    # no doc
    Changed = None
    Deleted = None


