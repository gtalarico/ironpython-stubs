# encoding: utf-8
# module Tekla.Structures.DrawingInternal calls itself DrawingInternal
# from Tekla.Structures.Drawing,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AreWeUnitTesting(object):
 # no doc
 Value=False
 __all__=[]


class AssociativityRule(DrawingObject):
 """
 AssociativityRule(view: ViewBase)
 AssociativityRule(view: ViewBase,follow: Followable,rotation: Followable)
 AssociativityRule(view: ViewBase,follow: Followable,rotation: Followable,updateMode: AssociativityUpdateMode)
 """
 def AddRule(self,rule):
  """ AddRule(self: AssociativityRule,rule: FitRule) -> bool """
  pass
 def Delete(self):
  """ Delete(self: AssociativityRule) -> bool """
  pass
 def Insert(self):
  """ Insert(self: AssociativityRule) -> bool """
  pass
 def IsEqual(self,ObjectToCompare):
  """ IsEqual(self: AssociativityRule,ObjectToCompare: object) -> bool """
  pass
 def Modify(self):
  """ Modify(self: AssociativityRule) -> bool """
  pass
 def RemoveRule(self,rule):
  """ RemoveRule(self: AssociativityRule,rule: FitRule) -> bool """
  pass
 def Select(self):
  """ Select(self: AssociativityRule) -> bool """
  pass
 @staticmethod
 def __new__(self,view,follow=None,rotation=None,updateMode=None):
  """
  __new__(cls: type,view: ViewBase)
  __new__(cls: type,view: ViewBase,follow: Followable,rotation: Followable)
  __new__(cls: type,view: ViewBase,follow: Followable,rotation: Followable,updateMode: AssociativityUpdateMode)
  """
  pass
 Follow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Follow(self: AssociativityRule) -> Followable

Set: Follow(self: AssociativityRule)=value
"""

 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Rotation(self: AssociativityRule) -> Followable

Set: Rotation(self: AssociativityRule)=value
"""

 Rules=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Rules(self: AssociativityRule) -> List[FitRule]

Set: Rules(self: AssociativityRule)=value
"""

 UpdateMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UpdateMode(self: AssociativityRule) -> AssociativityUpdateMode

Set: UpdateMode(self: AssociativityRule)=value
"""


 AssociativityUpdateMode=None
 DirectionEnum=None
 FitRule=None
 Followable=None
 PlaneNameEnum=None
 RuleTypeEnum=None
 _Attributes=None


class CDelegateSetter(object):
 # no doc
 @staticmethod
 def SetInstanceForUnitTesting(cdelegate):
  """ SetInstanceForUnitTesting(cdelegate: ICDelegate) """
  pass
 __all__=[
  '__reduce_ex__',
  'SetInstanceForUnitTesting',
 ]


class dak_dndeffect_t(Enum):
 """ enum dak_dndeffect_t,values: DAK_DNDEFFECT_COPY (1),DAK_DNDEFFECT_COPYORMOVE (3),DAK_DNDEFFECT_MOVE (2),DAK_DNDEFFECT_MOVEINFIELD (4),DAK_DNDEFFECT_NONE (0) """
 DAK_DNDEFFECT_COPY=None
 DAK_DNDEFFECT_COPYORMOVE=None
 DAK_DNDEFFECT_MOVE=None
 DAK_DNDEFFECT_MOVEINFIELD=None
 DAK_DNDEFFECT_NONE=None
 value__=None


class dak_eventtype_t(Enum):
 """ enum dak_eventtype_t,values: DAK_EVENT_ACTIVATE (21),DAK_EVENT_BUTTONPRESS (40),DAK_EVENT_BUTTONRELEASE (42),DAK_EVENT_CANCEL (11),DAK_EVENT_CLICK1 (7),DAK_EVENT_CLICK2 (8),DAK_EVENT_DIALOGPOPUPMENU (51),DAK_EVENT_DIGIT (50),DAK_EVENT_DOUBLECLICK (41),DAK_EVENT_DOWN1 (1),DAK_EVENT_DOWN2 (2),DAK_EVENT_DRAG1 (3),DAK_EVENT_DRAG2 (4),DAK_EVENT_DRAGNDROP (54),DAK_EVENT_ENTER (44),DAK_EVENT_EXPOSE (10),DAK_EVENT_EXTEND (13),DAK_EVENT_HIDE (38),DAK_EVENT_INDRAGNDROP (53),DAK_EVENT_INMOVE (29),DAK_EVENT_INRESIZE (32),DAK_EVENT_INROTATE (35),DAK_EVENT_KEYPRESS (46),DAK_EVENT_LEAVE (45),DAK_EVENT_MOUSEMOVE (43),DAK_EVENT_MOUSEWHEEL (49),DAK_EVENT_MOVE (30),DAK_EVENT_MULTIEXTEND (18),DAK_EVENT_MULTISELECT (16),DAK_EVENT_MULTITOGGLE (20),DAK_EVENT_NONE (0),DAK_EVENT_POLYEND (37),DAK_EVENT_POLYEXTEND (25),DAK_EVENT_POLYSELECT (23),DAK_EVENT_POLYTOGGLE (27),DAK_EVENT_POPUPMENU (47),DAK_EVENT_QUERYDRAGNDROP (52),DAK_EVENT_QUERYMOVE (15),DAK_EVENT_QUERYRESIZE (17),DAK_EVENT_QUERYROTATE (19),DAK_EVENT_RESIZE (33),DAK_EVENT_ROTATE (36),DAK_EVENT_SELECT (12),DAK_EVENT_SHOW (39),DAK_EVENT_STARTMOVE (28),DAK_EVENT_STARTPOLYEXTEND (24),DAK_EVENT_STARTPOLYSELECT (22),DAK_EVENT_STARTPOLYTOGGLE (26),DAK_EVENT_STARTRESIZE (31),DAK_EVENT_STARTROTATE (34),DAK_EVENT_TABLECLICK (9),DAK_EVENT_TIMER (48),DAK_EVENT_TOGGLE (14),DAK_EVENT_UP1 (5),DAK_EVENT_UP2 (6) """
 DAK_EVENT_ACTIVATE=None
 DAK_EVENT_BUTTONPRESS=None
 DAK_EVENT_BUTTONRELEASE=None
 DAK_EVENT_CANCEL=None
 DAK_EVENT_CLICK1=None
 DAK_EVENT_CLICK2=None
 DAK_EVENT_DIALOGPOPUPMENU=None
 DAK_EVENT_DIGIT=None
 DAK_EVENT_DOUBLECLICK=None
 DAK_EVENT_DOWN1=None
 DAK_EVENT_DOWN2=None
 DAK_EVENT_DRAG1=None
 DAK_EVENT_DRAG2=None
 DAK_EVENT_DRAGNDROP=None
 DAK_EVENT_ENTER=None
 DAK_EVENT_EXPOSE=None
 DAK_EVENT_EXTEND=None
 DAK_EVENT_HIDE=None
 DAK_EVENT_INDRAGNDROP=None
 DAK_EVENT_INMOVE=None
 DAK_EVENT_INRESIZE=None
 DAK_EVENT_INROTATE=None
 DAK_EVENT_KEYPRESS=None
 DAK_EVENT_LEAVE=None
 DAK_EVENT_MOUSEMOVE=None
 DAK_EVENT_MOUSEWHEEL=None
 DAK_EVENT_MOVE=None
 DAK_EVENT_MULTIEXTEND=None
 DAK_EVENT_MULTISELECT=None
 DAK_EVENT_MULTITOGGLE=None
 DAK_EVENT_NONE=None
 DAK_EVENT_POLYEND=None
 DAK_EVENT_POLYEXTEND=None
 DAK_EVENT_POLYSELECT=None
 DAK_EVENT_POLYTOGGLE=None
 DAK_EVENT_POPUPMENU=None
 DAK_EVENT_QUERYDRAGNDROP=None
 DAK_EVENT_QUERYMOVE=None
 DAK_EVENT_QUERYRESIZE=None
 DAK_EVENT_QUERYROTATE=None
 DAK_EVENT_RESIZE=None
 DAK_EVENT_ROTATE=None
 DAK_EVENT_SELECT=None
 DAK_EVENT_SHOW=None
 DAK_EVENT_STARTMOVE=None
 DAK_EVENT_STARTPOLYEXTEND=None
 DAK_EVENT_STARTPOLYSELECT=None
 DAK_EVENT_STARTPOLYTOGGLE=None
 DAK_EVENT_STARTRESIZE=None
 DAK_EVENT_STARTROTATE=None
 DAK_EVENT_TABLECLICK=None
 DAK_EVENT_TIMER=None
 DAK_EVENT_TOGGLE=None
 DAK_EVENT_UP1=None
 DAK_EVENT_UP2=None
 value__=None


class dak_modifier_t(Enum):
 """ enum dak_modifier_t,values: DAK_MODIFIER_CONTROL (2),DAK_MODIFIER_NONE (0),DAK_MODIFIER_SHIFT (1) """
 DAK_MODIFIER_CONTROL=None
 DAK_MODIFIER_NONE=None
 DAK_MODIFIER_SHIFT=None
 value__=None


class DelegateFake(object):
 """ DelegateFake() """
 def ExportAngleDimensionAttributesHandler(self,AngleDimAttr):
  """ ExportAngleDimensionAttributesHandler(self: DelegateFake,AngleDimAttr: dotGrAngleDimensionAttributes_t) -> (int,dotGrAngleDimensionAttributes_t) """
  pass
 def ExportAngleDimensionHandler(self,pAngleDimension):
  """ ExportAngleDimensionHandler(self: DelegateFake,pAngleDimension: dotGrAngleDimension_t) -> (int,dotGrAngleDimension_t) """
  pass
 def ExportArcHandler(self,pArc):
  """ ExportArcHandler(self: DelegateFake,pArc: dotGrArc_t) -> (int,dotGrArc_t) """
  pass
 def ExportAssociativityRuleHandler(self,pAssociativity):
  """ ExportAssociativityRuleHandler(self: DelegateFake,pAssociativity: dotGrAssociativity_t) -> (ReturnValuesEnum,dotGrAssociativity_t) """
  pass
 def ExportAutomationHandler(self,pAutomation):
  """ ExportAutomationHandler(self: DelegateFake,pAutomation: dotGrAutomation_t) -> (int,dotGrAutomation_t) """
  pass
 def ExportBoltAttributesHandler(self,pBoltAttributes):
  """ ExportBoltAttributesHandler(self: DelegateFake,pBoltAttributes: dotGrBoltAttributes_t) -> (int,dotGrBoltAttributes_t) """
  pass
 def ExportBoltHandler(self,pBolt):
  """ ExportBoltHandler(self: DelegateFake,pBolt: dotGrBolt_t) -> (int,dotGrBolt_t) """
  pass
 def ExportCircleHandler(self,pCircle):
  """ ExportCircleHandler(self: DelegateFake,pCircle: dotGrCircle_t) -> (int,dotGrCircle_t) """
  pass
 def ExportClosedGraphicObjectAttributesHandler(self,pClosedGraphicObjectAttributes,ObjectType):
  """ ExportClosedGraphicObjectAttributesHandler(self: DelegateFake,pClosedGraphicObjectAttributes: dotGrClosedGraphicObjectAttributes_t,ObjectType: int) -> (int,dotGrClosedGraphicObjectAttributes_t) """
  pass
 def ExportCloudHandler(self,pCloud):
  """ ExportCloudHandler(self: DelegateFake,pCloud: dotGrCloud_t) -> (int,dotGrCloud_t) """
  pass
 def ExportConnectionHandler(self,pConnection):
  """ ExportConnectionHandler(self: DelegateFake,pConnection: dotGrConnection_t) -> (int,dotGrConnection_t) """
  pass
 def ExportCurvedDimensionOrthogonalHandler(self,CurvedDimension):
  """ ExportCurvedDimensionOrthogonalHandler(self: DelegateFake,CurvedDimension: dotGrCurvedDimensionOrthogonal_t) -> (int,dotGrCurvedDimensionOrthogonal_t) """
  pass
 def ExportCurvedDimensionRadialHandler(self,CurvedDimension):
  """ ExportCurvedDimensionRadialHandler(self: DelegateFake,CurvedDimension: dotGrCurvedDimensionRadial_t) -> (int,dotGrCurvedDimensionRadial_t) """
  pass
 def ExportCurvedDimensionSetOrthogonalAttributesHandler(self,CurvedDimAttr):
  """ ExportCurvedDimensionSetOrthogonalAttributesHandler(self: DelegateFake,CurvedDimAttr: dotGrCurvedDimensionSetOrthogonalAttributes_t) -> (int,dotGrCurvedDimensionSetOrthogonalAttributes_t) """
  pass
 def ExportCurvedDimensionSetOrthogonalHandler(self,CurvedDimensionSet):
  """ ExportCurvedDimensionSetOrthogonalHandler(self: DelegateFake,CurvedDimensionSet: dotGrCurvedDimensionSetOrthogonal_t) -> (int,dotGrCurvedDimensionSetOrthogonal_t) """
  pass
 def ExportCurvedDimensionSetRadialAttributesHandler(self,CurvedDimAttr):
  """ ExportCurvedDimensionSetRadialAttributesHandler(self: DelegateFake,CurvedDimAttr: dotGrCurvedDimensionSetRadialAttributes_t) -> (int,dotGrCurvedDimensionSetRadialAttributes_t) """
  pass
 def ExportCurvedDimensionSetRadialHandler(self,CurvedDimensionSet):
  """ ExportCurvedDimensionSetRadialHandler(self: DelegateFake,CurvedDimensionSet: dotGrCurvedDimensionSetRadial_t) -> (int,dotGrCurvedDimensionSetRadial_t) """
  pass
 def ExportDetailMarkAttributesHandler(self,pDetailMarkAttributes):
  """ ExportDetailMarkAttributesHandler(self: DelegateFake,pDetailMarkAttributes: dotGrDetailMarkAttributes_t) -> (int,dotGrDetailMarkAttributes_t) """
  pass
 def ExportDetailMarkHandler(self,pDetailMark):
  """ ExportDetailMarkHandler(self: DelegateFake,pDetailMark: dotGrDetailMark_t) -> (ReturnValuesEnum,dotGrDetailMark_t) """
  pass
 def ExportDimensionLinkHandler(self,DimensionLink):
  """ ExportDimensionLinkHandler(self: DelegateFake,DimensionLink: dotGrDimensionLink_t) -> (int,dotGrDimensionLink_t) """
  pass
 def ExportDoubleListHandler(self,pDoubleList):
  """ ExportDoubleListHandler(self: DelegateFake,pDoubleList: dotGrDoubleList_t) -> (int,dotGrDoubleList_t) """
  pass
 def ExportDrawingHandler(self,pDrawing):
  """ ExportDrawingHandler(self: DelegateFake,pDrawing: dotGrDrawingAttributes_t) -> (ReturnValuesEnum,dotGrDrawingAttributes_t) """
  pass
 def ExportDrawingHandlerHandler(self,pHandler):
  """ ExportDrawingHandlerHandler(self: DelegateFake,pHandler: dotGrDrawingHandler_t) -> (int,dotGrDrawingHandler_t) """
  pass
 def ExportDrawingObjectSelectorHandler(self,selectorData):
  """ ExportDrawingObjectSelectorHandler(self: DelegateFake,selectorData: dotDrawingObjectSelector_t) -> (ReturnValuesEnum,dotDrawingObjectSelector_t) """
  pass
 def ExportEdgeChamferAttributesHandler(self,pEdgeChamferAttributes):
  """ ExportEdgeChamferAttributesHandler(self: DelegateFake,pEdgeChamferAttributes: dotGrEdgeChamferAttributes_t) -> (int,dotGrEdgeChamferAttributes_t) """
  pass
 def ExportEdgeChamferHandler(self,pEdgeChamfer):
  """ ExportEdgeChamferHandler(self: DelegateFake,pEdgeChamfer: dotGrEdgeChamfer_t) -> (int,dotGrEdgeChamfer_t) """
  pass
 def ExportEmbeddedObjectAttributesHandler(self,pEmbeddedObjectAttributes):
  """ ExportEmbeddedObjectAttributesHandler(self: DelegateFake,pEmbeddedObjectAttributes: dotGrEmbeddedObjectAttributes_t) -> (ReturnValuesEnum,dotGrEmbeddedObjectAttributes_t) """
  pass
 def ExportEmbeddedObjectHandler(self,pEmbeddedObject):
  """ ExportEmbeddedObjectHandler(self: DelegateFake,pEmbeddedObject: dotGrEmbeddedObject_t) -> (ReturnValuesEnum,dotGrEmbeddedObject_t) """
  pass
 def ExportEnumerateCustomLineTypes(self,pDotCustomLineTypes):
  """ ExportEnumerateCustomLineTypes(self: DelegateFake,pDotCustomLineTypes: dotGrCustomLineTypes_t) -> (ReturnValuesEnum,dotGrCustomLineTypes_t) """
  pass
 def ExportEnumerateObjects(self,pEnumerator):
  """ ExportEnumerateObjects(self: DelegateFake,pEnumerator: dotEnumerator_t) -> (int,dotEnumerator_t) """
  pass
 def ExportGetDotType(self,pModelObject):
  """ ExportGetDotType(self: DelegateFake,pModelObject: dotGrDrawingObject_t) -> (int,dotGrDrawingObject_t) """
  pass
 def ExportGetSnapshotFromDatabase(self,Enumerator,SerializedObjects,SelectInstances):
  """ ExportGetSnapshotFromDatabase(self: DelegateFake,Enumerator: dotEnumerator_t,SerializedObjects: List[object],SelectInstances: bool) -> (int,dotEnumerator_t,List[object]) """
  pass
 def ExportGridAttributesHandler(self,pGridAttributes):
  """ ExportGridAttributesHandler(self: DelegateFake,pGridAttributes: dotGrGridAttributes_t) -> (int,dotGrGridAttributes_t) """
  pass
 def ExportGridHandler(self,pGrid):
  """ ExportGridHandler(self: DelegateFake,pGrid: dotGrGrid_t) -> (int,dotGrGrid_t) """
  pass
 def ExportGridLineAttributesHandler(self,pGridLineAttributes):
  """ ExportGridLineAttributesHandler(self: DelegateFake,pGridLineAttributes: dotGrGridLineAttributes_t) -> (int,dotGrGridLineAttributes_t) """
  pass
 def ExportGridLineHandler(self,pGridLine):
  """ ExportGridLineHandler(self: DelegateFake,pGridLine: dotGrGridLine_t) -> (int,dotGrGridLine_t) """
  pass
 def ExportIntListHandler(self,pIntList):
  """ ExportIntListHandler(self: DelegateFake,pIntList: dotGrIntList_t) -> (int,dotGrIntList_t) """
  pass
 def ExportLayoutHandler(self,pPrintDrawing):
  """ ExportLayoutHandler(self: DelegateFake,pPrintDrawing: dotGrLayoutHandler_t) -> (int,dotGrLayoutHandler_t) """
  pass
 def ExportLeaderLineHandler(self,pLeaderLine):
  """ ExportLeaderLineHandler(self: DelegateFake,pLeaderLine: dotGrLeaderLine_t) -> (ReturnValuesEnum,dotGrLeaderLine_t) """
  pass
 def ExportLineHandler(self,pLine):
  """ ExportLineHandler(self: DelegateFake,pLine: dotGrLine_t) -> (int,dotGrLine_t) """
  pass
 def ExportLinkAttributesHandler(self,pLinkAttributes):
  """ ExportLinkAttributesHandler(self: DelegateFake,pLinkAttributes: dotGrLinkAttributes_t) -> (ReturnValuesEnum,dotGrLinkAttributes_t) """
  pass
 def ExportLinkHandler(self,pLink):
  """ ExportLinkHandler(self: DelegateFake,pLink: dotGrLink_t) -> (ReturnValuesEnum,dotGrLink_t) """
  pass
 def ExportMarkAttributesHandler(self,pMarkBaseAttributes):
  """ ExportMarkAttributesHandler(self: DelegateFake,pMarkBaseAttributes: dotGrMarkBaseAttributes_t) -> (int,dotGrMarkBaseAttributes_t) """
  pass
 def ExportMarkElementListHandler(self,pElementList):
  """ ExportMarkElementListHandler(self: DelegateFake,pElementList: dotGrElementList_t) -> (ReturnValuesEnum,dotGrElementList_t) """
  pass
 def ExportMarkHandler(self,pMarkBase):
  """ ExportMarkHandler(self: DelegateFake,pMarkBase: dotGrMarkBase_t) -> (ReturnValuesEnum,dotGrMarkBase_t) """
  pass
 def ExportModelDatabaseUserPropertyHandler(self,pProperty):
  """ ExportModelDatabaseUserPropertyHandler(self: DelegateFake,pProperty: dotGrUserProperty_t) -> (ReturnValuesEnum,dotGrUserProperty_t) """
  pass
 def ExportOpenGraphicObjectAttributesHandler(self,pOpenGraphicObjectAttributes,ObjectType):
  """ ExportOpenGraphicObjectAttributesHandler(self: DelegateFake,pOpenGraphicObjectAttributes: dotGrOpenGraphicObjectAttributes_t,ObjectType: int) -> (int,dotGrOpenGraphicObjectAttributes_t) """
  pass
 def ExportPartAttributesHandler(self,pPartAttributes):
  """ ExportPartAttributesHandler(self: DelegateFake,pPartAttributes: dotGrPartAttributes_t) -> (int,dotGrPartAttributes_t) """
  pass
 def ExportPartHandler(self,pPart):
  """ ExportPartHandler(self: DelegateFake,pPart: dotGrPart_t) -> (int,dotGrPart_t) """
  pass
 def ExportPickerCommandHandler(self,pPickerCommand):
  """ ExportPickerCommandHandler(self: DelegateFake,pPickerCommand: dotGrPickerCommand_t) -> (ReturnValuesEnum,dotGrPickerCommand_t) """
  pass
 def ExportPickerHandler(self,pickerData):
  """ ExportPickerHandler(self: DelegateFake,pickerData: dotDrawingUIPicker_t) -> (ReturnValuesEnum,dotDrawingUIPicker_t) """
  pass
 def ExportPluginHandler(self,Plugin):
  """ ExportPluginHandler(self: DelegateFake,Plugin: dotGrPlugin_t) -> (ReturnValuesEnum,dotGrPlugin_t) """
  pass
 def ExportPluginQueueHandler(self,pPluginQueue):
  """ ExportPluginQueueHandler(self: DelegateFake,pPluginQueue: dotGrPluginQueue_t) -> (ReturnValuesEnum,dotGrPluginQueue_t) """
  pass
 def ExportPointListHandler(self,pPointList):
  """ ExportPointListHandler(self: DelegateFake,pPointList: dotGrPointList_t) -> (int,dotGrPointList_t) """
  pass
 def ExportPolygonHandler(self,pPolygon):
  """ ExportPolygonHandler(self: DelegateFake,pPolygon: dotGrPolygon_t) -> (int,dotGrPolygon_t) """
  pass
 def ExportPolylineHandler(self,pPolyline):
  """ ExportPolylineHandler(self: DelegateFake,pPolyline: dotGrPolyline_t) -> (int,dotGrPolyline_t) """
  pass
 def ExportPourAttributesHandler(self,pPourAttributes):
  """ ExportPourAttributesHandler(self: DelegateFake,pPourAttributes: dotGrPourAttributes_t) -> (int,dotGrPourAttributes_t) """
  pass
 def ExportPourBreakAttributesHandler(self,pPourBreakAttributes):
  """ ExportPourBreakAttributesHandler(self: DelegateFake,pPourBreakAttributes: dotGrPourBreakAttributes_t) -> (ReturnValuesEnum,dotGrPourBreakAttributes_t) """
  pass
 def ExportPourBreakHandler(self,pPourBreak):
  """ ExportPourBreakHandler(self: DelegateFake,pPourBreak: dotGrPourBreak_t) -> (ReturnValuesEnum,dotGrPourBreak_t) """
  pass
 def ExportPourHandler(self,pPour):
  """ ExportPourHandler(self: DelegateFake,pPour: dotGrPour_t) -> (int,dotGrPour_t) """
  pass
 def ExportPrintDrawingHandler(self,pPrintDrawing):
  """ ExportPrintDrawingHandler(self: DelegateFake,pPrintDrawing: dotGrPrintDrawing_t) -> (int,dotGrPrintDrawing_t) """
  pass
 def ExportRadiusDimensionAttributesHandler(self,RadiusDimAttr):
  """ ExportRadiusDimensionAttributesHandler(self: DelegateFake,RadiusDimAttr: dotGrRadiusDimensionAttributes_t) -> (int,dotGrRadiusDimensionAttributes_t) """
  pass
 def ExportRadiusDimensionHandler(self,pRadiusDimension):
  """ ExportRadiusDimensionHandler(self: DelegateFake,pRadiusDimension: dotGrRadiusDimension_t) -> (int,dotGrRadiusDimension_t) """
  pass
 def ExportRectangleHandler(self,pRectangle):
  """ ExportRectangleHandler(self: DelegateFake,pRectangle: dotGrRectangle_t) -> (int,dotGrRectangle_t) """
  pass
 def ExportReferenceModelAttributesHandler(self,pReferenceModelAttributes):
  """ ExportReferenceModelAttributesHandler(self: DelegateFake,pReferenceModelAttributes: dotGrReferenceModelAttributes_t) -> (ReturnValuesEnum,dotGrReferenceModelAttributes_t) """
  pass
 def ExportReferenceModelHandler(self,pReferenceModel):
  """ ExportReferenceModelHandler(self: DelegateFake,pReferenceModel: dotGrReferenceModel_t) -> (ReturnValuesEnum,dotGrReferenceModel_t) """
  pass
 def ExportReinforcementBaseAttributesHandler(self,ReinforcementBaseAttributes):
  """ ExportReinforcementBaseAttributesHandler(self: DelegateFake,ReinforcementBaseAttributes: dotGrReinforcementBaseAttributes_t) -> (ReturnValuesEnum,dotGrReinforcementBaseAttributes_t) """
  pass
 def ExportReinforcementHandler(self,pReinforcement):
  """ ExportReinforcementHandler(self: DelegateFake,pReinforcement: dotGrReinforcementBase_t) -> (ReturnValuesEnum,dotGrReinforcementBase_t) """
  pass
 def ExportReinforcementSetGroupGetModelIdentifiers(self,pIdentifiers,modelIds):
  """ ExportReinforcementSetGroupGetModelIdentifiers(self: DelegateFake,pIdentifiers: dotGrReinforcementSetGroupIdentifiers_t,modelIds: List[int]) -> (ReturnValuesEnum,dotGrReinforcementSetGroupIdentifiers_t,List[int]) """
  pass
 def ExportSectionMarkAttributesHandler(self,pSectionMarkAttributes):
  """ ExportSectionMarkAttributesHandler(self: DelegateFake,pSectionMarkAttributes: dotGrSectionMarkAttributes_t) -> (ReturnValuesEnum,dotGrSectionMarkAttributes_t) """
  pass
 def ExportSectionMarkHandler(self,pSectionMark):
  """ ExportSectionMarkHandler(self: DelegateFake,pSectionMark: dotGrSectionMark_t) -> (ReturnValuesEnum,dotGrSectionMark_t) """
  pass
 def ExportStraightDimensionHandler(self,StraightDimension):
  """ ExportStraightDimensionHandler(self: DelegateFake,StraightDimension: dotGrStraightDimension_t) -> (int,dotGrStraightDimension_t) """
  pass
 def ExportStraightDimensionSetAttributesHandler(self,StraightDimensionSetAttributes):
  """ ExportStraightDimensionSetAttributesHandler(self: DelegateFake,StraightDimensionSetAttributes: dotGrStraightDimensionSetAttributes_t) -> (int,dotGrStraightDimensionSetAttributes_t) """
  pass
 def ExportStraightDimensionSetExcludePartsAccordingToFilter(self,drawingObject):
  """ ExportStraightDimensionSetExcludePartsAccordingToFilter(self: DelegateFake,drawingObject: dotGrDrawingObject_t) -> (int,dotGrDrawingObject_t) """
  pass
 def ExportStraightDimensionSetHandler(self,StraightDimensionSet):
  """ ExportStraightDimensionSetHandler(self: DelegateFake,StraightDimensionSet: dotGrStraightDimensionSet_t) -> (int,dotGrStraightDimensionSet_t) """
  pass
 def ExportStringListHandler(self,pStringList):
  """ ExportStringListHandler(self: DelegateFake,pStringList: dotGrStringList_t) -> (int,dotGrStringList_t) """
  pass
 def ExportSurfacingAttributesHandler(self,pSurfacingAttributes):
  """ ExportSurfacingAttributesHandler(self: DelegateFake,pSurfacingAttributes: dotGrSurfacingAttributes_t) -> (int,dotGrSurfacingAttributes_t) """
  pass
 def ExportSurfacingHandler(self,pSurfacing):
  """ ExportSurfacingHandler(self: DelegateFake,pSurfacing: dotGrSurfacing_t) -> (int,dotGrSurfacing_t) """
  pass
 def ExportSymbolAttributesHandler(self,pSymbolAttributes):
  """ ExportSymbolAttributesHandler(self: DelegateFake,pSymbolAttributes: dotGrSymbolAttributes_t) -> (int,dotGrSymbolAttributes_t) """
  pass
 def ExportSymbolHandler(self,pSymbol):
  """ ExportSymbolHandler(self: DelegateFake,pSymbol: dotGrSymbol_t) -> (ReturnValuesEnum,dotGrSymbol_t) """
  pass
 def ExportTextAttributesHandler(self,pTextAttributes):
  """ ExportTextAttributesHandler(self: DelegateFake,pTextAttributes: dotGrTextAttributes_t) -> (int,dotGrTextAttributes_t) """
  pass
 def ExportTextFileAttributesHandler(self,pTextFileAttributes):
  """ ExportTextFileAttributesHandler(self: DelegateFake,pTextFileAttributes: dotGrTextFileAttributes_t) -> (ReturnValuesEnum,dotGrTextFileAttributes_t) """
  pass
 def ExportTextFileHandler(self,pTextFile):
  """ ExportTextFileHandler(self: DelegateFake,pTextFile: dotGrTextFile_t) -> (ReturnValuesEnum,dotGrTextFile_t) """
  pass
 def ExportTextHandler(self,pText):
  """ ExportTextHandler(self: DelegateFake,pText: dotGrText_t) -> (ReturnValuesEnum,dotGrText_t) """
  pass
 def ExportUserPropertyHandler(self,pProperty):
  """ ExportUserPropertyHandler(self: DelegateFake,pProperty: dotGrUserProperty_t) -> (ReturnValuesEnum,dotGrUserProperty_t) """
  pass
 def ExportViewAttributesHandler(self,pViewAttributes):
  """ ExportViewAttributesHandler(self: DelegateFake,pViewAttributes: dotGrViewAttributes_t) -> (int,dotGrViewAttributes_t) """
  pass
 def ExportViewCommandHandler(self,pViewCommand):
  """ ExportViewCommandHandler(self: DelegateFake,pViewCommand: dotGrViewCommand_t) -> (ReturnValuesEnum,dotGrViewCommand_t) """
  pass
 def ExportViewHandler(self,pView):
  """ ExportViewHandler(self: DelegateFake,pView: dotGrView_t) -> (ReturnValuesEnum,dotGrView_t) """
  pass
 def ExportWeldHandler(self,pWeld):
  """ ExportWeldHandler(self: DelegateFake,pWeld: dotGrWeld_t) -> (ReturnValuesEnum,dotGrWeld_t) """
  pass
 def ExportWeldMarkHandler(self,pWeldMark):
  """ ExportWeldMarkHandler(self: DelegateFake,pWeldMark: dotGrWeldMark_t) -> (int,dotGrWeldMark_t) """
  pass
 def GetSheet(self):
  """ GetSheet(self: DelegateFake) -> ContainerView """
  pass
 def ImportDoubleListHandler(self,pDoubleList):
  """ ImportDoubleListHandler(self: DelegateFake,pDoubleList: dotGrDoubleList_t) -> (int,dotGrDoubleList_t) """
  pass
 def ImportIntListHandler(self,pIntList):
  """ ImportIntListHandler(self: DelegateFake,pIntList: dotGrIntList_t) -> (int,dotGrIntList_t) """
  pass
 def ImportMarkElementListHandler(self,pElementList):
  """ ImportMarkElementListHandler(self: DelegateFake,pElementList: dotGrElementList_t) -> (int,dotGrElementList_t) """
  pass
 def ImportPointListHandler(self,pPointList):
  """ ImportPointListHandler(self: DelegateFake,pPointList: dotGrPointList_t) -> (int,dotGrPointList_t) """
  pass
 def ImportStringListHandler(self,pStringList):
  """ ImportStringListHandler(self: DelegateFake,pStringList: dotGrStringList_t) -> (int,dotGrStringList_t) """
  pass

class dotClientId_t(object):
 # no doc
 ProcessId=None
 ThreadId=None


class dotDrawingObjectSelector_t(object):
 # no doc
 ClientId=None
 SelectorType=None


class dotDrawingUIPicker_t(object):
 # no doc
 ClientId=None
 Interrupted=None
 PickCommandStarted=None
 PickCount=None
 PickType=None
 PickViewId=None
 SyncCallback=None


class dotEnumerator_t(object):
 # no doc
 aFilterName=None
 aObjectIDs=None
 aObjectTypes=None
 ClientId=None
 DrawingId=None
 FatherId=None
 Filter=None
 MoreObjectsLeft=None
 nObjects=None
 nObjectToStart=None
 SubFilter=None


class dotGrAngleDimensionAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrAngleDimensionAttributes_t,attributes: AngleDimensionAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrAngleDimensionAttributes_t,attributes: AngleDimensionAttributes) """
  pass
 AngleType=None
 DimensionSetBaseAttributes=None
 TriangleBase=None


class dotGrAngleDimension_t(object):
 # no doc
 def FromStruct(self,angleDimension):
  """ FromStruct(self: dotGrAngleDimension_t,angleDimension: AngleDimension) """
  pass
 def ToStruct(self,angleDimension):
  """ ToStruct(self: dotGrAngleDimension_t,angleDimension: AngleDimension) """
  pass
 Attributes=None
 DimensionBase=None
 Distance=None
 Origin=None
 Point1=None
 Point2=None


class dotGrArcAttributes_t(object):
 # no doc
 def FromStruct(self,arcAttributes):
  """ FromStruct(self: dotGrArcAttributes_t,arcAttributes: ArcAttributes) """
  pass
 def ToStruct(self,arcAttributes):
  """ ToStruct(self: dotGrArcAttributes_t,arcAttributes: ArcAttributes) """
  pass
 OpenGraphicObjectAttributes=None


class dotGrArc_t(object):
 # no doc
 def FromStruct(self,arc):
  """ FromStruct(self: dotGrArc_t,arc: Arc) """
  pass
 def ToStruct(self,arc):
  """ ToStruct(self: dotGrArc_t,arc: Arc) """
  pass
 ArcAttributes=None
 EndPoint=None
 OpenGraphicObject=None
 Radius=None
 StartPoint=None


class dotGrArrowheadAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrArrowheadAttributes_t,attributes: ArrowheadAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrArrowheadAttributes_t,attributes: ArrowheadAttributes) """
  pass
 ArrowPosition=None
 Head=None
 Height=None
 Width=None


class dotGrAssociativity_t(object):
 # no doc
 DrawingObject=None


class dotGrAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrAttributes_t,Attributes: AttributesBase) """
  pass
 def ToStruct(self,Attributes):
  """ ToStruct(self: dotGrAttributes_t,Attributes: AttributesBase) """
  pass
 AttributeFilename=None


class dotGrAutomation_t(object):
 # no doc
 ClientId=None
 FileName=None
 ModelObjectId=None
 QueryType=None
 ReturnValue=None


class dotGrBoltAttributes_t(object):
 # no doc
 def FromStruct(self,BoltAttributes):
  """ FromStruct(self: dotGrBoltAttributes_t,BoltAttributes: BoltAttributes) """
  pass
 def ToStruct(self,BoltAttributes):
  """ ToStruct(self: dotGrBoltAttributes_t,BoltAttributes: BoltAttributes) """
  pass
 Color=None
 CommonAttributes=None
 Symbol=None
 SymbolContents=None


class dotGrBolt_t(object):
 # no doc
 def FromStruct(self,Bolt):
  """ FromStruct(self: dotGrBolt_t,Bolt: Bolt) """
  pass
 def ToStruct(self,Bolt):
  """ ToStruct(self: dotGrBolt_t,Bolt: Bolt) """
  pass
 BoltAttributes=None
 ModelObject=None


class dotGrCircleAttributes_t(object):
 # no doc
 def FromStruct(self,CircleAttributes):
  """ FromStruct(self: dotGrCircleAttributes_t,CircleAttributes: CircleAttributes) """
  pass
 def ToStruct(self,CircleAttributes):
  """ ToStruct(self: dotGrCircleAttributes_t,CircleAttributes: CircleAttributes) """
  pass
 ClosedGraphicObjectAttributes=None


class dotGrCircle_t(object):
 # no doc
 def FromStruct(self,Circle):
  """ FromStruct(self: dotGrCircle_t,Circle: Circle) """
  pass
 def ToStruct(self,Circle):
  """ ToStruct(self: dotGrCircle_t,Circle: Circle) """
  pass
 CenterPoint=None
 CircleAttributes=None
 ClosedGraphicObject=None
 Radius=None


class dotGrClosedGraphicObjectAttributes_t(object):
 # no doc
 def FromStruct(self,ClosedGraphicObject):
  """ FromStruct(self: dotGrClosedGraphicObjectAttributes_t,ClosedGraphicObject: ClosedGraphicObjectAttributes) """
  pass
 def ToStruct(self,ClosedGraphicObject):
  """ ToStruct(self: dotGrClosedGraphicObjectAttributes_t,ClosedGraphicObject: ClosedGraphicObjectAttributes) """
  pass
 GraphicObjectAttributes=None
 HatchAttributes=None


class dotGrClosedGraphicObject_t(object):
 # no doc
 def FromStruct(self,ClosedGraphicObject):
  """ FromStruct(self: dotGrClosedGraphicObject_t,ClosedGraphicObject: ClosedGraphicObject) """
  pass
 def ToStruct(self,ClosedGraphicObject):
  """ ToStruct(self: dotGrClosedGraphicObject_t,ClosedGraphicObject: ClosedGraphicObject) """
  pass
 GraphicObject=None


class dotGrCloudAttributes_t(object):
 # no doc
 def FromStruct(self,CloudAttributes):
  """ FromStruct(self: dotGrCloudAttributes_t,CloudAttributes: CloudAttributes) """
  pass
 def ToStruct(self,CloudAttributes):
  """ ToStruct(self: dotGrCloudAttributes_t,CloudAttributes: CloudAttributes) """
  pass
 ClosedGraphicObjectAttributes=None


class dotGrCloud_t(object):
 # no doc
 def FromStruct(self,cloud):
  """ FromStruct(self: dotGrCloud_t,cloud: Cloud) """
  pass
 def ToStruct(self,cloud):
  """ ToStruct(self: dotGrCloud_t,cloud: Cloud) """
  pass
 Bulge=None
 ClosedGraphicObject=None
 CloudAttributes=None


class dotGrCombinedDimensionAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrCombinedDimensionAttributes_t,attributes: CombinedDimensionAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrCombinedDimensionAttributes_t,attributes: CombinedDimensionAttributes) """
  pass
 Format=None
 MinimumNumberToCombine=None


class dotGrConnection_t(object):
 # no doc
 def FromStruct(self,part):
  """ FromStruct(self: dotGrConnection_t,part: Connection) """
  pass
 def ToStruct(self,part):
  """ ToStruct(self: dotGrConnection_t,part: Connection) """
  pass
 ModelObject=None


class dotGrCurvedDimensionOrthogonal_t(object):
 # no doc
 def FromStruct(self,CurvedDimension):
  """ FromStruct(self: dotGrCurvedDimensionOrthogonal_t,CurvedDimension: CurvedDimensionOrthogonal) """
  pass
 def ToStruct(self,CurvedDimension):
  """ ToStruct(self: dotGrCurvedDimensionOrthogonal_t,CurvedDimension: CurvedDimensionOrthogonal) """
  pass
 ArcPoint1=None
 ArcPoint2=None
 ArcPoint3=None
 Attributes=None
 DimensionBase=None
 Distance=None
 EndPoint=None
 StartPoint=None


class dotGrCurvedDimensionRadial_t(object):
 # no doc
 def FromStruct(self,CurvedDimension):
  """ FromStruct(self: dotGrCurvedDimensionRadial_t,CurvedDimension: CurvedDimensionRadial) """
  pass
 def ToStruct(self,CurvedDimension):
  """ ToStruct(self: dotGrCurvedDimensionRadial_t,CurvedDimension: CurvedDimensionRadial) """
  pass
 ArcPoint1=None
 ArcPoint2=None
 ArcPoint3=None
 Attributes=None
 DimensionBase=None
 Distance=None
 EndPoint=None
 StartPoint=None


class dotGrCurvedDimensionSetBaseAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrCurvedDimensionSetBaseAttributes_t,attributes: CurvedDimensionSetBaseAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrCurvedDimensionSetBaseAttributes_t,attributes: CurvedDimensionSetBaseAttributes) """
  pass
 DimensionSetBaseAttributes=None


class dotGrCurvedDimensionSetOrthogonalAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrCurvedDimensionSetOrthogonalAttributes_t,attributes: CurvedDimensionSetOrthogonalAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrCurvedDimensionSetOrthogonalAttributes_t,attributes: CurvedDimensionSetOrthogonalAttributes) """
  pass
 DimensionSetBaseAttributes=None


class dotGrCurvedDimensionSetOrthogonal_t(object):
 # no doc
 def FromStruct(self,CurvedDimension):
  """ FromStruct(self: dotGrCurvedDimensionSetOrthogonal_t,CurvedDimension: CurvedDimensionSetOrthogonal) """
  pass
 def ToStruct(self,CurvedDimension):
  """ ToStruct(self: dotGrCurvedDimensionSetOrthogonal_t,CurvedDimension: CurvedDimensionSetOrthogonal) """
  pass
 ArcPoint1=None
 ArcPoint2=None
 ArcPoint3=None
 Attributes=None
 DimensionSetBase=None
 Distance=None


class dotGrCurvedDimensionSetRadialAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrCurvedDimensionSetRadialAttributes_t,attributes: CurvedDimensionSetRadialAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrCurvedDimensionSetRadialAttributes_t,attributes: CurvedDimensionSetRadialAttributes) """
  pass
 CurvedDimensionType=None
 DimensionSetBaseAttributes=None
 DimensionType=None


class dotGrCurvedDimensionSetRadial_t(object):
 # no doc
 def FromStruct(self,CurvedDimension):
  """ FromStruct(self: dotGrCurvedDimensionSetRadial_t,CurvedDimension: CurvedDimensionSetRadial) """
  pass
 def ToStruct(self,CurvedDimension):
  """ ToStruct(self: dotGrCurvedDimensionSetRadial_t,CurvedDimension: CurvedDimensionSetRadial) """
  pass
 ArcPoint1=None
 ArcPoint2=None
 ArcPoint3=None
 Attributes=None
 DimensionSetBase=None
 Distance=None


class dotGrCustomLineTypes_t(object):
 # no doc
 def FromStruct(self):
  """ FromStruct(self: dotGrCustomLineTypes_t) """
  pass
 def ToStruct(self):
  """ ToStruct(self: dotGrCustomLineTypes_t) """
  pass
 ClientId=None


class dotGrDakDoubleList_t(object):
 """ dotGrDakDoubleList_t(List: Array[float]) """
 @staticmethod
 def __new__(self,List):
  """
  __new__[dotGrDakDoubleList_t]() -> dotGrDakDoubleList_t
  
  __new__(cls: type,List: Array[float])
  """
  pass
 aDoubleList=None
 ClientId=None
 iCurrentItem=None
 nItems=None
 nItemsInSet=None


class dotGrDakEvent_t(object):
 # no doc
 Action=None
 aX=None
 aY=None
 Button=None
 Modifier=None
 nPoints=None
 Workarea=None
 WorkareaId=None
 World=None
 WorldId=None


class dotGrDatabaseObject_t(object):
 # no doc
 def FromStruct(self,databaseObject):
  """ FromStruct(self: dotGrDatabaseObject_t,databaseObject: DatabaseObject) """
  pass
 def ToStruct(self,databaseObject):
  """ ToStruct(self: dotGrDatabaseObject_t,databaseObject: DatabaseObject) """
  pass
 ClientData=None
 ClientId=None
 DrawingIdentifier=None
 Identifier=None
 QueryType=None
 ReturnValue=None
 ViewIdentifier=None


class dotGrDate_t(object):
 # no doc
 def FromStruct(self,Date):
  """ FromStruct(self: dotGrDate_t,Date: DateTime) -> DateTime """
  pass
 Day=None
 Month=None
 Year=None


class dotGrDetailMarkAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrDetailMarkAttributes_t,Attributes: DetailMarkAttributes) """
  pass
 def ToStruct(self,Attributes):
  """ ToStruct(self: dotGrDetailMarkAttributes_t,Attributes: DetailMarkAttributes) """
  pass
 BoundaryLineType=None
 BoundaryShape=None
 ClientId=None
 CommonAttributes=None
 MarkName=None
 MarkSymbolAttributes=None
 MarkSymbolColor=None
 TagsAttributes=None


class dotGrDetailMarkTagsAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDetailMarkTagsAttributes_t,attributes: DetailMarkTagsAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDetailMarkTagsAttributes_t,attributes: DetailMarkTagsAttributes) """
  pass
 TagA1=None
 TagA2=None
 TagA3=None
 TagA4=None
 TagA5=None


class dotGrDetailMark_t(object):
 # no doc
 def FromStruct(self,detailMark):
  """ FromStruct(self: dotGrDetailMark_t,detailMark: DetailMark) """
  pass
 def ToStruct(self,detailMark):
  """ ToStruct(self: dotGrDetailMark_t,detailMark: DetailMark) """
  pass
 Attributes=None
 BoundaryPoint=None
 CenterPoint=None
 DrawingObject=None
 LabelPoint=None


class dotGrDimensionBase_t(object):
 # no doc
 def FromStruct(self,dimension):
  """ FromStruct(self: dotGrDimensionBase_t,dimension: DimensionBase) """
  pass
 def ToStruct(self,dimension):
  """ ToStruct(self: dotGrDimensionBase_t,dimension: DimensionBase) """
  pass
 DimensionSetIdentifier=None
 DrawingObject=None
 Hideable=None


class dotGrDimensionExaggerationAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDimensionExaggerationAttributes_t,attributes: DimensionExaggerationAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDimensionExaggerationAttributes_t,attributes: DimensionExaggerationAttributes) """
  pass
 ExaggerationDirection=None
 ExaggerationEnabled=None
 ExaggerationHeight=None
 ExaggerationOrigin=None
 ExaggerationPosition=None
 ExaggerationWidth=None


class dotGrDimensionFormatAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDimensionFormatAttributes_t,attributes: DimensionFormatAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDimensionFormatAttributes_t,attributes: DimensionFormatAttributes) """
  pass
 Format=None
 Precision=None
 Unit=None
 UseDigitGrouping=None


class dotGrDimensionLink_t(object):
 # no doc
 def FromStruct(self,Link):
  """ FromStruct(self: dotGrDimensionLink_t,Link: DimensionLink) """
  pass
 def ToStruct(self,Link):
  """ ToStruct(self: dotGrDimensionLink_t,Link: DimensionLink) """
  pass
 Dimension1=None
 Dimension2=None
 Object=None


class dotGrDimensionPlacingAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDimensionPlacingAttributes_t,attributes: DimensionPlacingAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDimensionPlacingAttributes_t,attributes: DimensionPlacingAttributes) """
  pass
 Direction=None
 Distance=None
 Placing=None


class dotGrDimensionSetBaseAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDimensionSetBaseAttributes_t,attributes: DimensionSetBaseAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDimensionSetBaseAttributes_t,attributes: DimensionSetBaseAttributes) """
  pass
 Arrowhead=None
 ClientId=None
 Color=None
 CommonAttributes=None
 Format=None
 Placing=None
 Text=None


class dotGrDimensionSetBase_t(object):
 # no doc
 def FromStruct(self,dimension):
  """ FromStruct(self: dotGrDimensionSetBase_t,dimension: DimensionSetBase) """
  pass
 def ToStruct(self,dimension):
  """ ToStruct(self: dotGrDimensionSetBase_t,dimension: DimensionSetBase) """
  pass
 DrawingObject=None
 Hideable=None


class dotGrDimensionTextAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrDimensionTextAttributes_t,attributes: DimensionTextAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrDimensionTextAttributes_t,attributes: DimensionTextAttributes) """
  pass
 Font=None
 Frame=None
 TextPlacing=None


class dotGrDoubleList_t(object):
 """ dotGrDoubleList_t(size: int) """
 def FromStruct(self,doubleList):
  """ FromStruct(self: dotGrDoubleList_t,doubleList: List[float]) -> List[float] """
  pass
 def ToStruct(self,doubleList):
  """ ToStruct(self: dotGrDoubleList_t,doubleList: List[float]) """
  pass
 @staticmethod
 def __new__(self,size):
  """
  __new__[dotGrDoubleList_t]() -> dotGrDoubleList_t
  
  __new__(cls: type,size: int)
  """
  pass
 aDoubleList=None
 ClientId=None
 iCurrentDouble=None
 nDoubles=None
 nDoublesInSet=None


class dotGrDrawingAttributes_t(object):
 # no doc
 def FromStruct(self,Drawing):
  """ FromStruct(self: dotGrDrawingAttributes_t,Drawing: Drawing) """
  pass
 def ToStruct(self,Drawing):
  """ ToStruct(self: dotGrDrawingAttributes_t,Drawing: Drawing) """
  pass
 AttributeFile=None
 CreationDate=None
 DrawingType=None
 Identifier=None
 InternalSheetNumber=None
 IsFrozen=None
 IsIssued=None
 IsLocked=None
 IsMasterDrawing=None
 IsReadyForIssue=None
 IsReadyForIssueBy=None
 IssuingDate=None
 LayoutAttributes=None
 Mark=None
 ModelObjectIdentifier=None
 ModificationDate=None
 Name=None
 QueryType=None
 ReturnValue=None
 SectionViewStartLabel=None
 Sheet=None
 Title1=None
 Title2=None
 Title3=None
 UpToDateStatus=None


class dotGrDrawingHandler_t(object):
 # no doc
 Parameter1=None
 Parameter2=None
 QueryType=None
 ReturnValue=None


class dotGrDrawingObject_t(object):
 # no doc
 def FromStruct(self,drawingObject):
  """ FromStruct(self: dotGrDrawingObject_t,drawingObject: DrawingObject) """
  pass
 def ToStruct(self,drawingObject):
  """ ToStruct(self: dotGrDrawingObject_t,drawingObject: DrawingObject) """
  pass
 DatabaseObject=None
 ObjectType=None


class dotGrEdgeChamferAttributes_t(object):
 # no doc
 def FromStruct(self,chamferAttributes):
  """ FromStruct(self: dotGrEdgeChamferAttributes_t,chamferAttributes: EdgeChamferAttributes) """
  pass
 def ToStruct(self,chamferAttributes):
  """ ToStruct(self: dotGrEdgeChamferAttributes_t,chamferAttributes: EdgeChamferAttributes) """
  pass
 CommonAttributes=None
 VisibleLines=None


class dotGrEdgeChamfer_t(object):
 # no doc
 def FromStruct(self,chamfer):
  """ FromStruct(self: dotGrEdgeChamfer_t,chamfer: EdgeChamfer) """
  pass
 def ToStruct(self,chamfer):
  """ ToStruct(self: dotGrEdgeChamfer_t,chamfer: EdgeChamfer) """
  pass
 ChamferAttributes=None
 ModelObject=None


class dotGrElementList_t(object):
 # no doc
 ClientId=None
 CurrentElement=None
 iCurrentElement=None


class dotGrElement_t(object):
 # no doc
 Font=None
 FrameId=None
 FrameType=None
 GroupId=None
 Hidden=None
 IsUnitAvailable=None
 Label=None
 MaxPoint=None
 MergeParam=None
 MinPoint=None
 Name=None
 ObjectId=None
 PullOutParam=None
 Type=None
 Unit=None
 Value=None


class dotGrEmbeddedObjectAttributes_t(object):
 # no doc
 def FromStruct(self,EmbeddedObjectAttributes):
  """ FromStruct(self: dotGrEmbeddedObjectAttributes_t,EmbeddedObjectAttributes: EmbeddedObjectAttributes) """
  pass
 def ToStruct(self,EmbeddedObjectAttributes):
  """ ToStruct(self: dotGrEmbeddedObjectAttributes_t,EmbeddedObjectAttributes: EmbeddedObjectAttributes) """
  pass
 Attributes=None
 Frame=None
 Scaling=None
 XScale=None
 YScale=None


class dotGrEmbeddedObject_t(object):
 # no doc
 def FromStruct(self,obj):
  """ FromStruct(self: dotGrEmbeddedObject_t,obj: EmbeddedObjectBase) """
  pass
 def ToStruct(self,obj):
  """ ToStruct(self: dotGrEmbeddedObject_t,obj: EmbeddedObjectBase) """
  pass
 Angle=None
 Attributes=None
 DrawingObject=None
 InsertionPoint=None
 Path=None
 Size=None


class dotGrFontAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrFontAttributes_t,attributes: FontAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrFontAttributes_t,attributes: FontAttributes) """
  pass
 Bold=None
 Color=None
 Height=None
 Italic=None
 Name=None
 Underlined=None


class dotGrFrame_t(object):
 # no doc
 def FromStruct(self,Frame):
  """ FromStruct(self: dotGrFrame_t,Frame: LinkFrameAttributes)FromStruct(self: dotGrFrame_t,Frame: EmbeddedObjectFrame)FromStruct(self: dotGrFrame_t,Frame: Frame) """
  pass
 def ToStruct(self,Frame):
  """ ToStruct(self: dotGrFrame_t,Frame: LinkFrameAttributes)ToStruct(self: dotGrFrame_t,Frame: EmbeddedObjectFrame)ToStruct(self: dotGrFrame_t,Frame: Frame) """
  pass
 FrameAngle=None
 FrameHeight=None
 FrameInsertionPoint=None
 FrameWidth=None
 LineType=None
 Type=None


class dotGrGraphicObjectAttributes_t(object):
 # no doc
 def FromStruct(self,graphicObjectAttributes):
  """ FromStruct(self: dotGrGraphicObjectAttributes_t,graphicObjectAttributes: GraphicObjectAttributes) """
  pass
 def ToStruct(self,graphicObjectAttributes):
  """ ToStruct(self: dotGrGraphicObjectAttributes_t,graphicObjectAttributes: GraphicObjectAttributes) """
  pass
 Bulge=None
 CommonAttributes=None
 CoordinateSystem=None
 LineAttributes=None


class dotGrGraphicObjectHatchAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrGraphicObjectHatchAttributes_t,attributes: GraphicObjectHatchAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrGraphicObjectHatchAttributes_t,attributes: GraphicObjectHatchAttributes) """
  pass
 CommonAttributes=None
 OffsetX=None
 OffsetY=None


class dotGrGraphicObject_t(object):
 # no doc
 def FromStruct(self,graphicObject):
  """ FromStruct(self: dotGrGraphicObject_t,graphicObject: GraphicObject) """
  pass
 def ToStruct(self,graphicObject):
  """ ToStruct(self: dotGrGraphicObject_t,graphicObject: GraphicObject) """
  pass
 DrawingObject=None
 Hideable=None


class dotGrGridAttributes_t(object):
 # no doc
 def FromStruct(self,grid):
  """ FromStruct(self: dotGrGridAttributes_t,grid: GridAttributes) """
  pass
 def ToStruct(self,grid):
  """ ToStruct(self: dotGrGridAttributes_t,grid: GridAttributes) """
  pass
 AttributeFilename=None
 CommonAttributes=None
 FontAttributes=None
 Frame=None
 LineAttributes=None
 OffsetAtEndOfLine=None
 OffsetAtStartOfLine=None
 TextPosition=None


class dotGrGridLabel_t(object):
 # no doc
 def FromStruct(self,gridLabel):
  """ FromStruct(self: dotGrGridLabel_t,gridLabel: GridLabel) """
  pass
 def ToStruct(self,gridLabel):
  """ ToStruct(self: dotGrGridLabel_t,gridLabel: GridLabel) """
  pass
 CenterPoint=None
 FrameHeight=None
 FrameWidth=None
 GridLabelPoint=None
 GridLabelText=None
 GridPoint=None
 OffsetGridPoint=None
 TextHeight=None
 TextWidth=None


class dotGrGridLineAttributes_t(object):
 # no doc
 def FromStruct(self,gridLine):
  """ FromStruct(self: dotGrGridLineAttributes_t,gridLine: GridLineAttributes) """
  pass
 def ToStruct(self,gridLine):
  """ ToStruct(self: dotGrGridLineAttributes_t,gridLine: GridLineAttributes) """
  pass
 CommonAttributes=None
 FontAttributes=None
 Frame=None
 LineAttributes=None
 OffsetAtEndOfLine=None
 OffsetAtStartOfLine=None
 TextPosition=None


class dotGrGridLine_t(object):
 # no doc
 def FromStruct(self,gridLine):
  """ FromStruct(self: dotGrGridLine_t,gridLine: GridLine) """
  pass
 def ToStruct(self,gridLine):
  """ ToStruct(self: dotGrGridLine_t,gridLine: GridLine) """
  pass
 EndLabel=None
 GridLineAttributes=None
 ModelObject=None
 StartLabel=None


class dotGrGrid_t(object):
 # no doc
 def FromStruct(self,grid):
  """ FromStruct(self: dotGrGrid_t,grid: Grid) """
  pass
 def ToStruct(self,grid):
  """ ToStruct(self: dotGrGrid_t,grid: Grid) """
  pass
 GridAttributes=None
 ModelObject=None


class dotGrHatchAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrHatchAttributes_t,attributes: HatchAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrHatchAttributes_t,attributes: HatchAttributes) """
  pass
 Angle=None
 BackgroundColor=None
 Color=None
 FactorType=None
 Name=None
 ScaleX=None
 ScaleY=None


class dotGrHideable_t(object):
 # no doc
 def FromStruct(self,pObject):
  """ FromStruct(self: dotGrHideable_t,pObject: Hideable) """
  pass
 def ToStruct(self,pObject):
  """ ToStruct(self: dotGrHideable_t,pObject: Hideable) """
  pass
 HiddenFlags=None
 ShouldBeHiddenFlags=None


class dotGrIntList_t(object):
 """ dotGrIntList_t(size: int) """
 def FromStruct(self,intList):
  """ FromStruct(self: dotGrIntList_t,intList: List[int]) -> List[int] """
  pass
 def ToStruct(self,intList):
  """ ToStruct(self: dotGrIntList_t,intList: List[int]) """
  pass
 @staticmethod
 def __new__(self,size):
  """
  __new__[dotGrIntList_t]() -> dotGrIntList_t
  
  __new__(cls: type,size: int)
  """
  pass
 aIntList=None
 ClientId=None
 iCurrentInt=None
 nInts=None
 nIntsInSet=None


class dotGrLayoutAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrLayoutAttributes_t,attributes: LayoutAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrLayoutAttributes_t,attributes: LayoutAttributes) """
  pass
 AutoSizeOptions=None
 CommonAttributes=None
 Layout=None
 ListHiddenObjectsInTemplates=None
 SheetSize=None
 SizeDefinitionMode=None
 TableLayoutId=None


class dotGrLayoutHandler_t(object):
 # no doc
 ClientId=None
 Command=None
 Parameter=None
 QueryType=None
 ReturnValue=None
 TableToOperate=None


class dotGrLayTable_t(object):
 # no doc
 def FromStruct(self,Table):
  """ FromStruct(self: dotGrLayTable_t,Table: LayoutTable) """
  pass
 def ToStruct(self,Table):
  """ ToStruct(self: dotGrLayTable_t,Table: LayoutTable) """
  pass
 Angle=None
 FileName=None
 Id=None
 Name=None
 OverlapVithViews=None
 RefCorner=None
 RefTableId=None
 Scale=None
 TableCorner=None
 TableLayoutId=None
 TableType=None
 XOffset=None
 YOffset=None


class dotGrLeaderLine_t(object):
 # no doc
 def FromStruct(self,LeaderLine):
  """ FromStruct(self: dotGrLeaderLine_t,LeaderLine: LeaderLine) """
  pass
 def ToStruct(self,LeaderLine):
  """ ToStruct(self: dotGrLeaderLine_t,LeaderLine: LeaderLine) """
  pass
 ArrowHead=None
 DrawingObject=None
 EndPoint=None
 LeaderLineType=None
 StartPoint=None


class dotGrLineAttributesStruct_t(object):
 # no doc
 def FromStruct(self,lineAttributes):
  """ FromStruct(self: dotGrLineAttributesStruct_t,lineAttributes: LineAttributes) """
  pass
 def ToStruct(self,lineAttributes):
  """ ToStruct(self: dotGrLineAttributesStruct_t,lineAttributes: LineAttributes) """
  pass
 OpenGraphicObjectAttributes=None


class dotGrLineAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrLineAttributes_t,attributes: LineTypeAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrLineAttributes_t,attributes: LineTypeAttributes) """
  pass
 Color=None
 Type=None


class dotGrLineTypes_t(object):
 # no doc
 def FromStruct(self,lineTypes):
  """ FromStruct(self: dotGrLineTypes_t) -> LineTypes """
  pass
 def ToStruct(self,lineTypes):
  """ ToStruct(self: dotGrLineTypes_t,lineTypes: LineTypes) """
  pass
 CustomLineTypeId=None
 CustomLineTypeName=None
 LineType=None


class dotGrLine_t(object):
 # no doc
 def FromStruct(self,line):
  """ FromStruct(self: dotGrLine_t,line: Line) """
  pass
 def ToStruct(self,line):
  """ ToStruct(self: dotGrLine_t,line: Line) """
  pass
 Bulge=None
 EndPoint=None
 LineAttributes=None
 OpenGraphicObject=None
 StartPoint=None


class dotGrLinkAttributes_t(object):
 # no doc
 def FromStruct(self,obj):
  """ FromStruct(self: dotGrLinkAttributes_t,obj: LinkAttributes) """
  pass
 def ToStruct(self,obj):
  """ ToStruct(self: dotGrLinkAttributes_t,obj: LinkAttributes) """
  pass
 Attributes=None
 Font=None
 Frame=None
 Scaling=None


class dotGrLink_t(object):
 # no doc
 def FromStruct(self,obj):
  """ FromStruct(self: dotGrLink_t,obj: DrawingLink)FromStruct(self: dotGrLink_t,obj: HyperLink) """
  pass
 def ToStruct(self,obj):
  """ ToStruct(self: dotGrLink_t,obj: DrawingLink)ToStruct(self: dotGrLink_t,obj: HyperLink) """
  pass
 Angle=None
 Attributes=None
 DrawingId=None
 DrawingObject=None
 DrawingType=None
 InsertionPoint=None
 Size=None
 Target=None
 Text=None


class dotGrMarkBaseAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrMarkBaseAttributes_t,attributes: MarkBaseAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrMarkBaseAttributes_t,attributes: MarkBaseAttributes) """
  pass
 Angle=None
 ArrowHead=None
 ClientId=None
 CommonAttributes=None
 FontAttributes=None
 Frame=None
 ModelObjectId=None
 PlacingAttributes=None
 PreferredPlacingType=None


class dotGrMarkBase_t(object):
 # no doc
 def FromStruct(self,mark):
  """ FromStruct(self: dotGrMarkBase_t,mark: MarkBase) """
  pass
 def ToStruct(self,mark):
  """ ToStruct(self: dotGrMarkBase_t,mark: MarkBase) """
  pass
 ChangeSymbol=None
 DrawingObject=None
 Hideable=None
 InsertionPoint=None
 IsAssociativeNote=None
 MarkBaseAttributes=None
 ModelObjectId=None
 Placing=None
 TextHeight=None
 TextWidth=None


class dotGrModelObjectHatchAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrModelObjectHatchAttributes_t,attributes: ModelObjectHatchAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrModelObjectHatchAttributes_t,attributes: ModelObjectHatchAttributes) """
  pass
 AutomaticScaling=None
 CommonAttributes=None


class dotGrModelObject_t(object):
 # no doc
 def FromStruct(self,pObject):
  """ FromStruct(self: dotGrModelObject_t,pObject: ModelObject) """
  pass
 def ToStruct(self,pObject):
  """ ToStruct(self: dotGrModelObject_t,pObject: ModelObject) """
  pass
 DrawingObject=None
 Hideable=None
 Identifier=None


class dotGrOpenGraphicObjectAttributes_t(object):
 # no doc
 def FromStruct(self,openGraphicObject):
  """ FromStruct(self: dotGrOpenGraphicObjectAttributes_t,openGraphicObject: OpenGraphicObjectAttributes) """
  pass
 def ToStruct(self,openGraphicObject):
  """ ToStruct(self: dotGrOpenGraphicObjectAttributes_t,openGraphicObject: OpenGraphicObjectAttributes) """
  pass
 Arrowhead=None
 GraphicObjectAttributes=None


class dotGrOpenGraphicObject_t(object):
 # no doc
 def FromStruct(self,openGraphicObject):
  """ FromStruct(self: dotGrOpenGraphicObject_t,openGraphicObject: OpenGraphicObject) """
  pass
 def ToStruct(self,openGraphicObject):
  """ ToStruct(self: dotGrOpenGraphicObject_t,openGraphicObject: OpenGraphicObject) """
  pass
 GraphicObject=None


class dotGrPartAttributes_t(object):
 # no doc
 def FromStruct(self,partAttributes):
  """ FromStruct(self: dotGrPartAttributes_t,partAttributes: PartAttributes) """
  pass
 def ToStruct(self,partAttributes):
  """ ToStruct(self: dotGrPartAttributes_t,partAttributes: PartAttributes) """
  pass
 CommonAttributes=None
 FaceHatch=None
 Flags=None
 HiddenLines=None
 ReferenceLine=None
 Representation=None
 SectionFaceHatch=None
 SymbolOffset=None
 VisibleLines=None


class dotGrPart_t(object):
 # no doc
 def FromStruct(self,part):
  """ FromStruct(self: dotGrPart_t,part: Part) """
  pass
 def ToStruct(self,part):
  """ ToStruct(self: dotGrPart_t,part: Part) """
  pass
 ModelObject=None
 PartAttributes=None


class dotGrPath_t(object):
 # no doc
 def FromStruct(self,path):
  """ FromStruct(self: dotGrPath_t,path: str) -> str """
  pass
 def ToStruct(self,path):
  """ ToStruct(self: dotGrPath_t,path: str) """
  pass
 DOT_MAX_PATH_LEN=1024
 Value=None


class dotGrPickerCommand_t(object):
 # no doc
 def GetIsInteractivePicker(self):
  """ GetIsInteractivePicker(self: dotGrPickerCommand_t) -> bool """
  pass
 def ToStruct(self):
  """ ToStruct(self: dotGrPickerCommand_t) """
  pass
 ClientId=None
 IsInteractivePicker=None


class dotGrPlacingAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrPlacingAttributes_t,attributes: PlacingAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrPlacingAttributes_t,attributes: PlacingAttributes) """
  pass
 IsFixed=None
 PlacingDistance=None
 PlacingQuarter=None


class dotGrPlacingDirectionAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrPlacingDirectionAttributes_t,attributes: PlacingDirectionAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrPlacingDirectionAttributes_t,attributes: PlacingDirectionAttributes) """
  pass
 Direction=None


class dotGrPlacingDistanceAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrPlacingDistanceAttributes_t,attributes: PlacingDistanceAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrPlacingDistanceAttributes_t,attributes: PlacingDistanceAttributes) """
  pass
 MinimalDistance=None
 SearchMargin=None


class dotGrPlacingQuarterAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrPlacingQuarterAttributes_t,attributes: PlacingQuarterAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrPlacingQuarterAttributes_t,attributes: PlacingQuarterAttributes) """
  pass
 BottomLeft=None
 BottomRight=None
 TopLeft=None
 TopRight=None


class dotGrPlacing_t(object):
 # no doc
 def FromStruct(self,PlacingBase):
  """ FromStruct(self: dotGrPlacing_t) -> PlacingBase """
  pass
 def ToStruct(self,PlacingBase,preferredPlacingTypeBase):
  """ ToStruct(self: dotGrPlacing_t,PlacingBase: PlacingBase,preferredPlacingTypeBase: PreferredPlacingTypeBase) """
  pass
 EndPoint=None
 LeaderLinePoint=None
 Placing=None
 StartPoint=None


class dotGrPluginQueue_t(object):
 # no doc

class dotGrPlugin_t(object):
 # no doc
 def FromStruct(self,plugin):
  """ FromStruct(self: dotGrPlugin_t,plugin: Plugin) """
  pass
 def ToStruct(self,plugin):
  """ ToStruct(self: dotGrPlugin_t,plugin: Plugin) """
  pass
 DrawingObject=None
 Name=None


class dotGrPointList_t(object):
 """ dotGrPointList_t(size: int) """
 def FromStruct(self,pointList):
  """ FromStruct(self: dotGrPointList_t,pointList: List[Point]) -> List[Point] """
  pass
 def ToStruct(self,pointList):
  """ ToStruct(self: dotGrPointList_t,pointList: List[Point]) """
  pass
 @staticmethod
 def __new__(self,size):
  """
  __new__[dotGrPointList_t]() -> dotGrPointList_t
  
  __new__(cls: type,size: int)
  """
  pass
 aPointList=None
 ClientId=None
 iCurrentPoint=None
 nPoints=None
 nPointsInSet=None


class dotGrPolygonAttributes_t(object):
 # no doc
 def FromStruct(self,PolygonAttributes):
  """ FromStruct(self: dotGrPolygonAttributes_t,PolygonAttributes: PolygonAttributes) """
  pass
 def ToStruct(self,PolygonAttributes):
  """ ToStruct(self: dotGrPolygonAttributes_t,PolygonAttributes: PolygonAttributes) """
  pass
 ClosedGraphicObjectAttributes=None


class dotGrPolygon_t(object):
 # no doc
 def FromStruct(self,polygon):
  """ FromStruct(self: dotGrPolygon_t,polygon: Polygon) """
  pass
 def ToStruct(self,polygon):
  """ ToStruct(self: dotGrPolygon_t,polygon: Polygon) """
  pass
 Bulge=None
 ClosedGraphicObject=None
 PolygonAttributes=None


class dotGrPolylineAttributes_t(object):
 # no doc
 def FromStruct(self,polylineAttributes):
  """ FromStruct(self: dotGrPolylineAttributes_t,polylineAttributes: PolylineAttributes) """
  pass
 def ToStruct(self,polylineAttributes):
  """ ToStruct(self: dotGrPolylineAttributes_t,polylineAttributes: PolylineAttributes) """
  pass
 OpenGraphicObjectAttributes=None


class dotGrPolyline_t(object):
 # no doc
 def FromStruct(self,polyline):
  """ FromStruct(self: dotGrPolyline_t,polyline: Polyline) """
  pass
 def ToStruct(self,polyline):
  """ ToStruct(self: dotGrPolyline_t,polyline: Polyline) """
  pass
 Bulge=None
 OpenGraphicObject=None
 PolylineAttributes=None


class dotGrPourAttributes_t(object):
 # no doc
 def FromStruct(self,pourAttributes):
  """ FromStruct(self: dotGrPourAttributes_t,pourAttributes: PourAttributes) """
  pass
 def ToStruct(self,pourAttributes):
  """ ToStruct(self: dotGrPourAttributes_t,pourAttributes: PourAttributes) """
  pass
 CommonAttributes=None
 DrawChamfers=None
 DrawHiddenLines=None
 DrawOwnHiddenLines=None
 FaceHatch=None
 HiddenLines=None
 SectionFaceHatch=None
 VisibleLines=None


class dotGrPourBreakAttributes_t(object):
 # no doc
 def FromStruct(self,pourBreakAttributes):
  """ FromStruct(self: dotGrPourBreakAttributes_t,pourBreakAttributes: PourBreakAttributes) """
  pass
 def ToStruct(self,pourBreakAttributes):
  """ ToStruct(self: dotGrPourBreakAttributes_t,pourBreakAttributes: PourBreakAttributes) """
  pass
 CommonAttributes=None
 DrawHiddenLines=None
 HiddenLines=None
 VisibleLines=None


class dotGrPourBreak_t(object):
 # no doc
 def FromStruct(self,pourBreak):
  """ FromStruct(self: dotGrPourBreak_t,pourBreak: PourBreak) """
  pass
 def ToStruct(self,pourBreak):
  """ ToStruct(self: dotGrPourBreak_t,pourBreak: PourBreak) """
  pass
 ModelObject=None
 PourBreakAttributes=None


class dotGrPour_t(object):
 # no doc
 def FromStruct(self,pour):
  """ FromStruct(self: dotGrPour_t,pour: PourObject) """
  pass
 def ToStruct(self,pour):
  """ ToStruct(self: dotGrPour_t,pour: PourObject) """
  pass
 ModelObject=None
 PourAttributes=None


class dotGrPreferredPlacingType_t(object):
 # no doc
 def FromStruct(self,Placing):
  """ FromStruct(self: dotGrPreferredPlacingType_t) -> PreferredPlacingTypeBase """
  pass
 def ToStruct(self,preferredPlacingType):
  """ ToStruct(self: dotGrPreferredPlacingType_t,preferredPlacingType: PreferredPlacingTypeBase) """
  pass
 PreferredPlacingType=None


class dotGrPrintAttributes_t(object):
 # no doc
 def ToStruct(self,attributes,FileName):
  """ ToStruct(self: dotGrPrintAttributes_t,attributes: PrintAttributes,FileName: str) """
  pass
 aFileName=None
 aPrinterInstance=None
 NumberOfCopies=None
 Orientation=None
 PrintArea=None
 PrintToMultipleSheet=None
 Scale=None
 ScalingType=None


class dotGrPrintDrawing_t(object):
 # no doc
 DrawingId=None
 PrintAttributes=None
 ReturnValue=None


class dotGrRadiusDimensionAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrRadiusDimensionAttributes_t,attributes: RadiusDimensionAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrRadiusDimensionAttributes_t,attributes: RadiusDimensionAttributes) """
  pass
 DimensionSetBaseAttributes=None


class dotGrRadiusDimension_t(object):
 # no doc
 def FromStruct(self,RadiusDimension):
  """ FromStruct(self: dotGrRadiusDimension_t,RadiusDimension: RadiusDimension) """
  pass
 def ToStruct(self,RadiusDimension):
  """ ToStruct(self: dotGrRadiusDimension_t,RadiusDimension: RadiusDimension) """
  pass
 ArcPoint1=None
 ArcPoint2=None
 ArcPoint3=None
 Attributes=None
 DimensionBase=None
 Distance=None


class dotGrRectangleAttributes_t(object):
 # no doc
 def FromStruct(self,RectangleAttributes):
  """ FromStruct(self: dotGrRectangleAttributes_t,RectangleAttributes: RectangleAttributes) """
  pass
 def ToStruct(self,RectangleAttributes):
  """ ToStruct(self: dotGrRectangleAttributes_t,RectangleAttributes: RectangleAttributes) """
  pass
 Bulge=None
 ClosedGraphicObjectAttributes=None


class dotGrRectangle_t(object):
 # no doc
 def FromStruct(self,rectangle):
  """ FromStruct(self: dotGrRectangle_t,rectangle: Rectangle) """
  pass
 def ToStruct(self,rectangle):
  """ ToStruct(self: dotGrRectangle_t,rectangle: Rectangle) """
  pass
 Angle=None
 ClosedGraphicObject=None
 EndPoint=None
 RectangleAttributes=None
 StartPoint=None


class dotGrReferenceModelAttributes_t(object):
 # no doc
 def FromStruct(self,attr):
  """ FromStruct(self: dotGrReferenceModelAttributes_t,attr: ReferenceModelAttributes) """
  pass
 def ToStruct(self,attr):
  """ ToStruct(self: dotGrReferenceModelAttributes_t,attr: ReferenceModelAttributes) """
  pass
 Attributes=None
 LineType=None


class dotGrReferenceModel_t(object):
 # no doc
 def FromStruct(self,model):
  """ FromStruct(self: dotGrReferenceModel_t,model: ReferenceModel) """
  pass
 def ToStruct(self,model):
  """ ToStruct(self: dotGrReferenceModel_t,model: ReferenceModel) """
  pass
 Attributes=None
 ModelObject=None


class dotGrReinforcementBaseAttributes_t(object):
 # no doc
 def FromStruct(self,reinforcementAttributes):
  """ FromStruct(self: dotGrReinforcementBaseAttributes_t,reinforcementAttributes: ReinforcementBaseAttributes) """
  pass
 def ToStruct(self,reinforcementAttributes):
  """ ToStruct(self: dotGrReinforcementBaseAttributes_t,reinforcementAttributes: ReinforcementBaseAttributes) """
  pass
 CommonAttributes=None
 HiddenLines=None
 HideLinesHiddenByPart=None
 HideLinesHiddenByReinforcement=None
 HookedEndSymbolType=None
 MeshReinforcementSymbolIndex=None
 MeshReinforcementSymbolSize=None
 MeshReinforcementVisibilityCrossing=None
 MeshReinforcementVisibilityLongitudinal=None
 ReinforcementRepresentation=None
 ReinforcementVisibility=None
 StraightEndSymbolType=None
 VisibleLines=None


class dotGrReinforcementBase_t(object):
 # no doc
 def FromStruct(self,reinforcement):
  """ FromStruct(self: dotGrReinforcementBase_t,reinforcement: ReinforcementBase) """
  pass
 def ToStruct(self,reinforcement):
  """ ToStruct(self: dotGrReinforcementBase_t,reinforcement: ReinforcementBase) """
  pass
 ModelObject=None
 RebarCustomPosition=None
 RebarCustomPositionCrossing=None
 RebarCustomPositionLongitudinal=None
 ReinforcementBaseAttributes=None


class dotGrReinforcementSetGroupIdentifiers_t(object):
 # no doc
 DrawingIdentifier=None
 DrawingObjectIdentifier=None
 Identifiers=None
 NumberOfIdentifiers=None


class dotGrSectionMarkAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrSectionMarkAttributes_t,Attributes: SectionMarkAttributes) """
  pass
 def ToStruct(self,Attributes):
  """ ToStruct(self: dotGrSectionMarkAttributes_t,Attributes: SectionMarkAttributes) """
  pass
 ClientId=None
 CommonAttributes=None
 LeftSymbol=None
 LineColor=None
 LineLength=None
 LineLengthOffset=None
 LineWidth=None
 LineWidthOffsetLeft=None
 LineWidthOffsetRight=None
 MarkName=None
 RightSymbol=None
 SymbolColor=None
 TagsAttributes=None


class dotGrSectionMarkSymbol_t(object):
 # no doc
 def FromStruct(self,MarkSymbol):
  """ FromStruct(self: dotGrSectionMarkSymbol_t,MarkSymbol: SectionMarkSymbol) """
  pass
 def ToStruct(self,MarkSymbol):
  """ ToStruct(self: dotGrSectionMarkSymbol_t,MarkSymbol: SectionMarkSymbol) """
  pass
 Position=None
 Shape=None
 Size=None


class dotGrSectionMarkTagAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrSectionMarkTagAttributes_t,attributes: SectionMarkTagAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrSectionMarkTagAttributes_t,attributes: SectionMarkTagAttributes) """
  pass

class dotGrSectionMarkTagsAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrSectionMarkTagsAttributes_t,attributes: SectionMarkTagsAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrSectionMarkTagsAttributes_t,attributes: SectionMarkTagsAttributes) """
  pass
 TagA1=None
 TagA2=None
 TagA3=None
 TagA4=None
 TagA5=None


class dotGrSectionMark_t(object):
 # no doc
 def FromStruct(self,sectionMark):
  """ FromStruct(self: dotGrSectionMark_t,sectionMark: CurvedSectionMark)FromStruct(self: dotGrSectionMark_t,sectionMark: SectionMark) """
  pass
 def ToStruct(self,sectionMark):
  """ ToStruct(self: dotGrSectionMark_t,sectionMark: CurvedSectionMark)ToStruct(self: dotGrSectionMark_t,sectionMark: SectionMark) """
  pass
 Attributes=None
 DrawingObject=None
 IsCurved=None
 LeftPoint=None
 MiddlePoint=None
 RightPoint=None


class dotGrSheet_t(object):
 # no doc
 Height=None
 Width=None


class dotGrSize_t(object):
 # no doc
 def FromStruct(self,Size):
  """ FromStruct(self: dotGrSize_t,Size: Size) """
  pass
 def ToStruct(self,Size):
  """ ToStruct(self: dotGrSize_t,Size: Size) """
  pass
 Height=None
 Width=None


class dotGrSnapSettings_t(object):
 # no doc
 CenterPoints=None
 EndPoints=None
 Extension=None
 Free=None
 GeometryPoints=None
 Grid=None
 Intersections=None
 Lines=None
 MidPoints=None
 Near=None
 Perpendicular=None
 Points=None
 ReferencePoints=None


class dotGrStraightDimensionAttributes_t(object):
 # no doc
 def FromStruct(self,straightDimensionAttributes):
  """ FromStruct(self: dotGrStraightDimensionAttributes_t,straightDimensionAttributes: StraightDimensionAttributes) """
  pass
 def ToStruct(self,straightDimensionAttributes):
  """ ToStruct(self: dotGrStraightDimensionAttributes_t,straightDimensionAttributes: StraightDimensionAttributes) """
  pass
 Exaggeration=None


class dotGrStraightDimensionSetAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrStraightDimensionSetAttributes_t,attributes: StraightDimensionSetAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrStraightDimensionSetAttributes_t,attributes: StraightDimensionSetAttributes) """
  pass
 CombinedDimension=None
 DimensionSetBaseAttributes=None
 DimensionType=None
 Exaggeration=None
 ExcludePartsAccordingToFilter=None
 ExtensionLine=None
 IncludePartCountInTag=None
 ModelObjectId=None
 ShortDimension=None
 UpdateGrouping=None


class dotGrStraightDimensionSet_t(object):
 # no doc
 def FromStruct(self,straightDimension):
  """ FromStruct(self: dotGrStraightDimensionSet_t,straightDimension: StraightDimensionSet) """
  pass
 def ToStruct(self,straightDimension):
  """ ToStruct(self: dotGrStraightDimensionSet_t,straightDimension: StraightDimensionSet) """
  pass
 Attributes=None
 DimensionSetBase=None
 Distance=None
 LeftTagLineOffset=None
 RightTagLineOffset=None
 UpDirection=None


class dotGrStraightDimension_t(object):
 # no doc
 def FromStruct(self,straightDimension):
  """ FromStruct(self: dotGrStraightDimension_t,straightDimension: StraightDimension) """
  pass
 def ToStruct(self,straightDimension):
  """ ToStruct(self: dotGrStraightDimension_t,straightDimension: StraightDimension) """
  pass
 Attributes=None
 DimensionBase=None
 DimSetAttributes=None
 Distance=None
 EndPoint=None
 Mark=None
 StartPoint=None
 UpDirection=None


class dotGrStringList_t(object):
 """ dotGrStringList_t(size: int) """
 def FromStruct(self,stringList):
  """ FromStruct(self: dotGrStringList_t,stringList: List[str]) -> List[str] """
  pass
 def ToStruct(self,stringList):
  """ ToStruct(self: dotGrStringList_t,stringList: List[str]) """
  pass
 @staticmethod
 def __new__(self,size):
  """
  __new__[dotGrStringList_t]() -> dotGrStringList_t
  
  __new__(cls: type,size: int)
  """
  pass
 aStringList=None
 ClientId=None
 iCurrentItem=None
 nItems=None
 nItemsInSet=None


class dotGrString_t(object):
 # no doc
 def FromStruct(self,String):
  """ FromStruct(self: dotGrString_t,String: str) -> str """
  pass
 def ToStruct(self,String):
  """ ToStruct(self: dotGrString_t,String: str) """
  pass
 DOT_MAX_STRING_LEN=1024
 Value=None


class dotGrSurfacingAttributes_t(object):
 # no doc
 def FromStruct(self,SurfacingAttributes):
  """ FromStruct(self: dotGrSurfacingAttributes_t,SurfacingAttributes: SurfacingAttributes) """
  pass
 def ToStruct(self,SurfacingAttributes):
  """ ToStruct(self: dotGrSurfacingAttributes_t,SurfacingAttributes: SurfacingAttributes) """
  pass
 CommonAttributes=None
 Flags=None
 HiddenLines=None
 Representation=None
 VisibleLines=None


class dotGrSurfacing_t(object):
 # no doc
 def FromStruct(self,Surfacing):
  """ FromStruct(self: dotGrSurfacing_t,Surfacing: Surfacing) """
  pass
 def ToStruct(self,Surfacing):
  """ ToStruct(self: dotGrSurfacing_t,Surfacing: Surfacing) """
  pass
 ModelObject=None
 SurfacingAttributes=None


class dotGrSymbolAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrSymbolAttributes_t,Attributes: SymbolAttributes) """
  pass
 def ToStruct(self,Attributes):
  """ ToStruct(self: dotGrSymbolAttributes_t,Attributes: SymbolAttributes) """
  pass
 Angle=None
 Color=None
 CommonAttributes=None
 Frame=None
 Height=None
 PreferredPlacingType=None


class dotGrSymbol_t(object):
 # no doc
 def FromStruct(self,symbol):
  """ FromStruct(self: dotGrSymbol_t,symbol: Symbol) """
  pass
 def ToStruct(self,symbol):
  """ ToStruct(self: dotGrSymbol_t,symbol: Symbol) """
  pass
 DrawingObject=None
 Hideable=None
 InsertionPoint=None
 Placing=None
 SymbolAttributes=None
 SymbolFile=None
 SymbolIndex=None


class dotGrTextAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrTextAttributes_t,Attributes: TextAttributes) """
  pass
 def ToStruct(self,Attributes):
  """ ToStruct(self: dotGrTextAttributes_t,Attributes: TextAttributes) """
  pass
 Angle=None
 ArrowHead=None
 CommonAttributes=None
 FontAttributes=None
 Frame=None
 PlacingAttributes=None
 PreferredPlacingType=None
 RulerWidth=None
 TextAlignment=None
 UseWordWrapping=None


class dotGrTextFileAttributes_t(object):
 # no doc
 def FromStruct(self,ObjectAttributes):
  """ FromStruct(self: dotGrTextFileAttributes_t,ObjectAttributes: TextFileAttributes) """
  pass
 def ToStruct(self,ObjectAttributes):
  """ ToStruct(self: dotGrTextFileAttributes_t,ObjectAttributes: TextFileAttributes) """
  pass
 Attributes=None
 Font=None
 Frame=None
 Scaling=None


class dotGrTextFile_t(object):
 # no doc
 def FromStruct(self,obj):
  """ FromStruct(self: dotGrTextFile_t,obj: TextFile) """
  pass
 def ToStruct(self,obj):
  """ ToStruct(self: dotGrTextFile_t,obj: TextFile) """
  pass
 Angle=None
 Attributes=None
 DrawingObject=None
 InsertionPoint=None
 Path=None
 Size=None


class dotGrText_t(object):
 # no doc
 def FromStruct(self,pText):
  """ FromStruct(self: dotGrText_t,pText: Text) """
  pass
 def ToStruct(self,pText):
  """ ToStruct(self: dotGrText_t,pText: Text) """
  pass
 Attributes=None
 DrawingObject=None
 FrameHeight=None
 FrameWidth=None
 Hideable=None
 InsertionPoint=None
 Placing=None
 TextString=None


class dotGrUnitAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrUnitAttributes_t,attributes: UnitAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrUnitAttributes_t,attributes: UnitAttributes) """
  pass
 Format=None
 Precision=None
 Unit=None


class dotGrUserProperty_t(object):
 # no doc
 aName=None
 aStringValue=None
 DatabaseObject=None
 DoubleValue=None
 IntValue=None
 Type=None


class dotGrViewAttributes_t(object):
 # no doc
 ClientId=None
 CommonAttributes=None
 DatumLevel=None
 FixedViewPlacing=None
 LabelPositionHorizontal=None
 LabelPositionVertical=None
 MarkSymbolAttributes=None
 MarkSymbolColor=None
 PourView=None
 ReflectedView=None
 Scale=None
 ShorteningAttributes=None
 ShowPartOpeningsOrRecessSymbol=None
 TagsAttributes=None
 UndeformedView=None
 UnfoldedView=None
 ViewExtensionForNeighbourParts=None
 ViewPlaneDatumPointForElevations=None


class dotGrViewCommand_t(object):
 # no doc
 CreatedViewId=None
 CreatedViewMarkId=None
 DetailMarkAttributes=None
 DisplayPlane=None
 ParentView=None
 Point1=None
 Point2=None
 Point3=None
 RestrictionBoxMaxPoint=None
 RestrictionBoxMinPoint=None
 SectionMarkAttributes=None
 ViewAttributes=None
 ViewCommandType=None
 ViewInsertionPoint=None
 ViewPlane=None
 ViewRotation=None


class dotGrViewMarkBasicSymbolAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrViewMarkBasicSymbolAttributes_t,attributes: ViewMarkBasicSymbolAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewMarkBasicSymbolAttributes_t,attributes: ViewMarkBasicSymbolAttributes) """
  pass
 Shape=None
 Size=None


class dotGrViewMarkBasicTagAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrViewMarkBasicTagAttributes_t,attributes: ViewMarkBasicTagAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewMarkBasicTagAttributes_t,attributes: ViewMarkBasicTagAttributes) """
  pass
 Location=None
 Offset=None


class dotGrViewMarkSymbolAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrViewMarkSymbolAttributes_t,attributes: ViewMarkSymbolAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewMarkSymbolAttributes_t,attributes: ViewMarkSymbolAttributes) """
  pass
 BasicAttributes=None
 LineLength=None
 LineLengthType=None


class dotGrViewMarkTagAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrViewMarkTagAttributes_t,attributes: ViewMarkTagAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewMarkTagAttributes_t,attributes: ViewMarkTagAttributes) """
  pass
 BasicAttributes=None
 TagAlignment=None


class dotGrViewMarkTagsAttributes_t(object):
 # no doc
 def FromStruct(self,attributes):
  """ FromStruct(self: dotGrViewMarkTagsAttributes_t,attributes: ViewMarkTagsAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewMarkTagsAttributes_t,attributes: ViewMarkTagsAttributes) """
  pass
 TagA1=None
 TagA2=None
 TagA3=None
 TagA4=None
 TagA5=None


class dotGrViewRotation_t(object):
 # no doc
 RotateOnDrawingPlane=None
 RotateX=None
 RotateY=None
 RotateZ=None
 RotationOnDrawingPlane=None
 RotationX=None
 RotationY=None
 RotationZ=None
 ViewObject=None


class dotGrViewShorteningAttributes_t(object):
 # no doc
 def FromStruct(self,Attributes):
  """ FromStruct(self: dotGrViewShorteningAttributes_t,Attributes: ViewShorteningAttributes) """
  pass
 def ToStruct(self,attributes):
  """ ToStruct(self: dotGrViewShorteningAttributes_t,attributes: ViewShorteningAttributes) """
  pass
 CutParts=None
 CutPartType=None
 CutSkewParts=None
 MinimumLength=None
 Offset=None


class dotGrView_t(object):
 # no doc
 def FromStruct(self,view):
  """ FromStruct(self: dotGrView_t,view: ContainerView)FromStruct(self: dotGrView_t,view: View) """
  pass
 def ToStruct(self,view):
  """ ToStruct(self: dotGrView_t,view: ContainerView)ToStruct(self: dotGrView_t,view: View) """
  pass
 Attributes=None
 DisplayCoordinateSystem=None
 DrawingObject=None
 ExtremaCenterPoint=None
 FrameOrigin=None
 Height=None
 LinkedDrawingId=None
 MaxPoint=None
 MinPoint=None
 OriginInSheet=None
 ViewCoordinateSystem=None
 ViewName=None
 ViewType=None
 Width=None


class dotGrWeldAttributes_t(object):
 # no doc
 CommonAttributes=None
 VisibleLines=None


class dotGrWeldMark_t(object):
 # no doc
 def FromStruct(self,Mark):
  """ FromStruct(self: dotGrWeldMark_t,Mark: WeldMark) """
  pass
 def ToStruct(self,Mark):
  """ ToStruct(self: dotGrWeldMark_t,Mark: WeldMark) """
  pass
 DrawingObject=None
 InsertionPoint=None
 ModelObjectId=None


class dotGrWeld_t(object):
 # no doc
 def FromStruct(self,Part):
  """ FromStruct(self: dotGrWeld_t,Part: Weld) """
  pass
 def ToStruct(self,Part):
  """ ToStruct(self: dotGrWeld_t,Part: Weld) """
  pass
 ModelObject=None
 WeldAttributes=None


class dotLblMergeParam_t(object):
 # no doc
 aBlockPrefixMulti=None
 aBlockPrefixSingle=None
 aBlockSeparator=None
 aCCPrefix=None
 aCCSeparator=None
 CCShowAlways=None


class dotLblPullOutParam_t(object):
 # no doc
 aRebarGUID=None
 BendingAngle=None
 BendingRadius=None
 Dimensions=None
 EndMarks=None
 Exaggeration=None
 MarkId=None
 RotationAxis=None
 ScaleType=None
 Scaling=None
 ScalingX=None
 ScalingY=None


class DotNetDrawingProxy(object):
 """ DotNetDrawingProxy() """
 @staticmethod
 def Run(Param):
  """ Run(Param: str) -> int """
  pass

class dotOBB_t(object):
 # no doc
 def FromStruct(self,obb):
  """ FromStruct(self: dotOBB_t,obb: OBB) """
  pass
 def ToStruct(self,obb):
  """ ToStruct(self: dotOBB_t,obb: OBB) """
  pass
 axis0=None
 axis1=None
 axis2=None
 center=None
 extent0=None
 extent1=None
 extent2=None


class DrawingHandler(object):
 """ DrawingHandler() """
 def PrintDrawing(self,drawing,printAttributes,outputFile=None):
  """
  PrintDrawing(self: DrawingHandler,drawing: Drawing,printAttributes: DPMPrinterAttributes,outputFile: str) -> bool
  PrintDrawing(self: DrawingHandler,drawing: Drawing,printAttributes: DPMPrinterAttributes) -> bool
  """
  pass
 def PrintDrawings(self,drawings,printAttributes):
  """ PrintDrawings(self: DrawingHandler,drawings: List[Drawing],printAttributes: DPMPrinterAttributes) -> bool """
  pass

class EventHandlerWrapper(MarshalByRefObject):
 """ EventHandlerWrapper(Instance: IEventHandler,Functionality: WrapperFunctionalityBase) """
 def AddListener(self,EventListener):
  """ AddListener(self: EventHandlerWrapper,EventListener: Events)AddListener(self: EventHandlerWrapper,EventListener: Events) """
  pass
 def RemoveListener(self,EventListener):
  """ RemoveListener(self: EventHandlerWrapper,EventListener: Events)RemoveListener(self: EventHandlerWrapper,EventListener: Events) """
  pass
 @staticmethod
 def __new__(self,Instance,Functionality):
  """ __new__(cls: type,Instance: IEventHandler,Functionality: WrapperFunctionalityBase) """
  pass
 Functionality=None
 Instance=None


class ICDelegate:
 # no doc
 def ExportAngleDimensionAttributesHandler(self,AngleDimAttr):
  """ ExportAngleDimensionAttributesHandler(self: ICDelegate,AngleDimAttr: dotGrAngleDimensionAttributes_t) -> (int,dotGrAngleDimensionAttributes_t) """
  pass
 def ExportAngleDimensionHandler(self,pAngleDimension):
  """ ExportAngleDimensionHandler(self: ICDelegate,pAngleDimension: dotGrAngleDimension_t) -> (int,dotGrAngleDimension_t) """
  pass
 def ExportArcHandler(self,pArc):
  """ ExportArcHandler(self: ICDelegate,pArc: dotGrArc_t) -> (int,dotGrArc_t) """
  pass
 def ExportAssociativityRuleHandler(self,pAssociativity):
  """ ExportAssociativityRuleHandler(self: ICDelegate,pAssociativity: dotGrAssociativity_t) -> (ReturnValuesEnum,dotGrAssociativity_t) """
  pass
 def ExportAutomationHandler(self,pAutomation):
  """ ExportAutomationHandler(self: ICDelegate,pAutomation: dotGrAutomation_t) -> (int,dotGrAutomation_t) """
  pass
 def ExportBoltAttributesHandler(self,pBoltAttributes):
  """ ExportBoltAttributesHandler(self: ICDelegate,pBoltAttributes: dotGrBoltAttributes_t) -> (int,dotGrBoltAttributes_t) """
  pass
 def ExportBoltHandler(self,pBolt):
  """ ExportBoltHandler(self: ICDelegate,pBolt: dotGrBolt_t) -> (int,dotGrBolt_t) """
  pass
 def ExportCircleHandler(self,pCircle):
  """ ExportCircleHandler(self: ICDelegate,pCircle: dotGrCircle_t) -> (int,dotGrCircle_t) """
  pass
 def ExportClosedGraphicObjectAttributesHandler(self,pClosedGraphicObjectAttributes,ObjectType):
  """ ExportClosedGraphicObjectAttributesHandler(self: ICDelegate,pClosedGraphicObjectAttributes: dotGrClosedGraphicObjectAttributes_t,ObjectType: int) -> (int,dotGrClosedGraphicObjectAttributes_t) """
  pass
 def ExportCloudHandler(self,pCloud):
  """ ExportCloudHandler(self: ICDelegate,pCloud: dotGrCloud_t) -> (int,dotGrCloud_t) """
  pass
 def ExportConnectionHandler(self,pConnection):
  """ ExportConnectionHandler(self: ICDelegate,pConnection: dotGrConnection_t) -> (int,dotGrConnection_t) """
  pass
 def ExportCurvedDimensionOrthogonalHandler(self,CurvedDimension):
  """ ExportCurvedDimensionOrthogonalHandler(self: ICDelegate,CurvedDimension: dotGrCurvedDimensionOrthogonal_t) -> (int,dotGrCurvedDimensionOrthogonal_t) """
  pass
 def ExportCurvedDimensionRadialHandler(self,CurvedDimension):
  """ ExportCurvedDimensionRadialHandler(self: ICDelegate,CurvedDimension: dotGrCurvedDimensionRadial_t) -> (int,dotGrCurvedDimensionRadial_t) """
  pass
 def ExportCurvedDimensionSetOrthogonalAttributesHandler(self,CurvedDimAttr):
  """ ExportCurvedDimensionSetOrthogonalAttributesHandler(self: ICDelegate,CurvedDimAttr: dotGrCurvedDimensionSetOrthogonalAttributes_t) -> (int,dotGrCurvedDimensionSetOrthogonalAttributes_t) """
  pass
 def ExportCurvedDimensionSetOrthogonalHandler(self,CurvedDimensionSet):
  """ ExportCurvedDimensionSetOrthogonalHandler(self: ICDelegate,CurvedDimensionSet: dotGrCurvedDimensionSetOrthogonal_t) -> (int,dotGrCurvedDimensionSetOrthogonal_t) """
  pass
 def ExportCurvedDimensionSetRadialAttributesHandler(self,CurvedDimAttr):
  """ ExportCurvedDimensionSetRadialAttributesHandler(self: ICDelegate,CurvedDimAttr: dotGrCurvedDimensionSetRadialAttributes_t) -> (int,dotGrCurvedDimensionSetRadialAttributes_t) """
  pass
 def ExportCurvedDimensionSetRadialHandler(self,CurvedDimensionSet):
  """ ExportCurvedDimensionSetRadialHandler(self: ICDelegate,CurvedDimensionSet: dotGrCurvedDimensionSetRadial_t) -> (int,dotGrCurvedDimensionSetRadial_t) """
  pass
 def ExportDetailMarkAttributesHandler(self,pDetailMarkAttributes):
  """ ExportDetailMarkAttributesHandler(self: ICDelegate,pDetailMarkAttributes: dotGrDetailMarkAttributes_t) -> (int,dotGrDetailMarkAttributes_t) """
  pass
 def ExportDetailMarkHandler(self,pDetailMark):
  """ ExportDetailMarkHandler(self: ICDelegate,pDetailMark: dotGrDetailMark_t) -> (ReturnValuesEnum,dotGrDetailMark_t) """
  pass
 def ExportDimensionLinkHandler(self,DimensionLink):
  """ ExportDimensionLinkHandler(self: ICDelegate,DimensionLink: dotGrDimensionLink_t) -> (int,dotGrDimensionLink_t) """
  pass
 def ExportDoubleListHandler(self,pDoubleList):
  """ ExportDoubleListHandler(self: ICDelegate,pDoubleList: dotGrDoubleList_t) -> (int,dotGrDoubleList_t) """
  pass
 def ExportDrawingHandler(self,pDrawing):
  """ ExportDrawingHandler(self: ICDelegate,pDrawing: dotGrDrawingAttributes_t) -> (ReturnValuesEnum,dotGrDrawingAttributes_t) """
  pass
 def ExportDrawingHandlerHandler(self,pHandler):
  """ ExportDrawingHandlerHandler(self: ICDelegate,pHandler: dotGrDrawingHandler_t) -> (int,dotGrDrawingHandler_t) """
  pass
 def ExportDrawingObjectSelectorHandler(self,selectorData):
  """ ExportDrawingObjectSelectorHandler(self: ICDelegate,selectorData: dotDrawingObjectSelector_t) -> (ReturnValuesEnum,dotDrawingObjectSelector_t) """
  pass
 def ExportEdgeChamferAttributesHandler(self,pEdgeChamferAttributes):
  """ ExportEdgeChamferAttributesHandler(self: ICDelegate,pEdgeChamferAttributes: dotGrEdgeChamferAttributes_t) -> (int,dotGrEdgeChamferAttributes_t) """
  pass
 def ExportEdgeChamferHandler(self,pEdgeChamfer):
  """ ExportEdgeChamferHandler(self: ICDelegate,pEdgeChamfer: dotGrEdgeChamfer_t) -> (int,dotGrEdgeChamfer_t) """
  pass
 def ExportEmbeddedObjectAttributesHandler(self,pEmbeddedObjectAttributes):
  """ ExportEmbeddedObjectAttributesHandler(self: ICDelegate,pEmbeddedObjectAttributes: dotGrEmbeddedObjectAttributes_t) -> (ReturnValuesEnum,dotGrEmbeddedObjectAttributes_t) """
  pass
 def ExportEmbeddedObjectHandler(self,pEmbeddedObject):
  """ ExportEmbeddedObjectHandler(self: ICDelegate,pEmbeddedObject: dotGrEmbeddedObject_t) -> (ReturnValuesEnum,dotGrEmbeddedObject_t) """
  pass
 def ExportEnumerateCustomLineTypes(self,pDotCustomLineTypes):
  """ ExportEnumerateCustomLineTypes(self: ICDelegate,pDotCustomLineTypes: dotGrCustomLineTypes_t) -> (ReturnValuesEnum,dotGrCustomLineTypes_t) """
  pass
 def ExportEnumerateObjects(self,pEnumerator):
  """ ExportEnumerateObjects(self: ICDelegate,pEnumerator: dotEnumerator_t) -> (int,dotEnumerator_t) """
  pass
 def ExportGetDotType(self,pModelObject):
  """ ExportGetDotType(self: ICDelegate,pModelObject: dotGrDrawingObject_t) -> (int,dotGrDrawingObject_t) """
  pass
 def ExportGetSnapshotFromDatabase(self,Enumerator,SerializedObjects,SelectInstances):
  """ ExportGetSnapshotFromDatabase(self: ICDelegate,Enumerator: dotEnumerator_t,SerializedObjects: List[object],SelectInstances: bool) -> (int,dotEnumerator_t,List[object]) """
  pass
 def ExportGridAttributesHandler(self,pGridAttributes):
  """ ExportGridAttributesHandler(self: ICDelegate,pGridAttributes: dotGrGridAttributes_t) -> (int,dotGrGridAttributes_t) """
  pass
 def ExportGridHandler(self,pGrid):
  """ ExportGridHandler(self: ICDelegate,pGrid: dotGrGrid_t) -> (int,dotGrGrid_t) """
  pass
 def ExportGridLineAttributesHandler(self,pGridLineAttributes):
  """ ExportGridLineAttributesHandler(self: ICDelegate,pGridLineAttributes: dotGrGridLineAttributes_t) -> (int,dotGrGridLineAttributes_t) """
  pass
 def ExportGridLineHandler(self,pGridLine):
  """ ExportGridLineHandler(self: ICDelegate,pGridLine: dotGrGridLine_t) -> (int,dotGrGridLine_t) """
  pass
 def ExportIntListHandler(self,pIntList):
  """ ExportIntListHandler(self: ICDelegate,pIntList: dotGrIntList_t) -> (int,dotGrIntList_t) """
  pass
 def ExportLayoutHandler(self,pHandler):
  """ ExportLayoutHandler(self: ICDelegate,pHandler: dotGrLayoutHandler_t) -> (int,dotGrLayoutHandler_t) """
  pass
 def ExportLeaderLineHandler(self,pLeaderLine):
  """ ExportLeaderLineHandler(self: ICDelegate,pLeaderLine: dotGrLeaderLine_t) -> (ReturnValuesEnum,dotGrLeaderLine_t) """
  pass
 def ExportLineHandler(self,pLine):
  """ ExportLineHandler(self: ICDelegate,pLine: dotGrLine_t) -> (int,dotGrLine_t) """
  pass
 def ExportLinkAttributesHandler(self,pLinkAttributes):
  """ ExportLinkAttributesHandler(self: ICDelegate,pLinkAttributes: dotGrLinkAttributes_t) -> (ReturnValuesEnum,dotGrLinkAttributes_t) """
  pass
 def ExportLinkHandler(self,pLink):
  """ ExportLinkHandler(self: ICDelegate,pLink: dotGrLink_t) -> (ReturnValuesEnum,dotGrLink_t) """
  pass
 def ExportMarkAttributesHandler(self,pMarkBaseAttributes):
  """ ExportMarkAttributesHandler(self: ICDelegate,pMarkBaseAttributes: dotGrMarkBaseAttributes_t) -> (int,dotGrMarkBaseAttributes_t) """
  pass
 def ExportMarkElementListHandler(self,pElementList):
  """ ExportMarkElementListHandler(self: ICDelegate,pElementList: dotGrElementList_t) -> (ReturnValuesEnum,dotGrElementList_t) """
  pass
 def ExportMarkHandler(self,pMarkBase):
  """ ExportMarkHandler(self: ICDelegate,pMarkBase: dotGrMarkBase_t) -> (ReturnValuesEnum,dotGrMarkBase_t) """
  pass
 def ExportModelDatabaseUserPropertyHandler(self,pProperty):
  """ ExportModelDatabaseUserPropertyHandler(self: ICDelegate,pProperty: dotGrUserProperty_t) -> (ReturnValuesEnum,dotGrUserProperty_t) """
  pass
 def ExportOpenGraphicObjectAttributesHandler(self,pOpenGraphicObjectAttributes,ObjectType):
  """ ExportOpenGraphicObjectAttributesHandler(self: ICDelegate,pOpenGraphicObjectAttributes: dotGrOpenGraphicObjectAttributes_t,ObjectType: int) -> (int,dotGrOpenGraphicObjectAttributes_t) """
  pass
 def ExportPartAttributesHandler(self,pPartAttributes):
  """ ExportPartAttributesHandler(self: ICDelegate,pPartAttributes: dotGrPartAttributes_t) -> (int,dotGrPartAttributes_t) """
  pass
 def ExportPartHandler(self,pPart):
  """ ExportPartHandler(self: ICDelegate,pPart: dotGrPart_t) -> (int,dotGrPart_t) """
  pass
 def ExportPickerCommandHandler(self,pPickerCommand):
  """ ExportPickerCommandHandler(self: ICDelegate,pPickerCommand: dotGrPickerCommand_t) -> (ReturnValuesEnum,dotGrPickerCommand_t) """
  pass
 def ExportPickerHandler(self,pickerData):
  """ ExportPickerHandler(self: ICDelegate,pickerData: dotDrawingUIPicker_t) -> (ReturnValuesEnum,dotDrawingUIPicker_t) """
  pass
 def ExportPluginHandler(self,Plugin):
  """ ExportPluginHandler(self: ICDelegate,Plugin: dotGrPlugin_t) -> (ReturnValuesEnum,dotGrPlugin_t) """
  pass
 def ExportPluginQueueHandler(self,pPluginQueue):
  """ ExportPluginQueueHandler(self: ICDelegate,pPluginQueue: dotGrPluginQueue_t) -> (ReturnValuesEnum,dotGrPluginQueue_t) """
  pass
 def ExportPointListHandler(self,pPointList):
  """ ExportPointListHandler(self: ICDelegate,pPointList: dotGrPointList_t) -> (int,dotGrPointList_t) """
  pass
 def ExportPolygonHandler(self,pPolygon):
  """ ExportPolygonHandler(self: ICDelegate,pPolygon: dotGrPolygon_t) -> (int,dotGrPolygon_t) """
  pass
 def ExportPolylineHandler(self,pPolyline):
  """ ExportPolylineHandler(self: ICDelegate,pPolyline: dotGrPolyline_t) -> (int,dotGrPolyline_t) """
  pass
 def ExportPourAttributesHandler(self,pPourAttributes):
  """ ExportPourAttributesHandler(self: ICDelegate,pPourAttributes: dotGrPourAttributes_t) -> (int,dotGrPourAttributes_t) """
  pass
 def ExportPourBreakAttributesHandler(self,pPourBreakAttributes):
  """ ExportPourBreakAttributesHandler(self: ICDelegate,pPourBreakAttributes: dotGrPourBreakAttributes_t) -> (ReturnValuesEnum,dotGrPourBreakAttributes_t) """
  pass
 def ExportPourBreakHandler(self,pPourBreak):
  """ ExportPourBreakHandler(self: ICDelegate,pPourBreak: dotGrPourBreak_t) -> (ReturnValuesEnum,dotGrPourBreak_t) """
  pass
 def ExportPourHandler(self,pPour):
  """ ExportPourHandler(self: ICDelegate,pPour: dotGrPour_t) -> (int,dotGrPour_t) """
  pass
 def ExportPrintDrawingHandler(self,pPrintDrawing):
  """ ExportPrintDrawingHandler(self: ICDelegate,pPrintDrawing: dotGrPrintDrawing_t) -> (int,dotGrPrintDrawing_t) """
  pass
 def ExportRadiusDimensionAttributesHandler(self,RadiusDimAttr):
  """ ExportRadiusDimensionAttributesHandler(self: ICDelegate,RadiusDimAttr: dotGrRadiusDimensionAttributes_t) -> (int,dotGrRadiusDimensionAttributes_t) """
  pass
 def ExportRadiusDimensionHandler(self,pRadiusDimension):
  """ ExportRadiusDimensionHandler(self: ICDelegate,pRadiusDimension: dotGrRadiusDimension_t) -> (int,dotGrRadiusDimension_t) """
  pass
 def ExportRectangleHandler(self,pRectangle):
  """ ExportRectangleHandler(self: ICDelegate,pRectangle: dotGrRectangle_t) -> (int,dotGrRectangle_t) """
  pass
 def ExportReferenceModelAttributesHandler(self,pReferenceModelAttributes):
  """ ExportReferenceModelAttributesHandler(self: ICDelegate,pReferenceModelAttributes: dotGrReferenceModelAttributes_t) -> (ReturnValuesEnum,dotGrReferenceModelAttributes_t) """
  pass
 def ExportReferenceModelHandler(self,pReferenceModel):
  """ ExportReferenceModelHandler(self: ICDelegate,pReferenceModel: dotGrReferenceModel_t) -> (ReturnValuesEnum,dotGrReferenceModel_t) """
  pass
 def ExportReinforcementBaseAttributesHandler(self,ReinforcementBaseAttributes):
  """ ExportReinforcementBaseAttributesHandler(self: ICDelegate,ReinforcementBaseAttributes: dotGrReinforcementBaseAttributes_t) -> (ReturnValuesEnum,dotGrReinforcementBaseAttributes_t) """
  pass
 def ExportReinforcementHandler(self,pReinforcement):
  """ ExportReinforcementHandler(self: ICDelegate,pReinforcement: dotGrReinforcementBase_t) -> (ReturnValuesEnum,dotGrReinforcementBase_t) """
  pass
 def ExportReinforcementSetGroupGetModelIdentifiers(self,pIdentifiers,modelIds):
  """ ExportReinforcementSetGroupGetModelIdentifiers(self: ICDelegate,pIdentifiers: dotGrReinforcementSetGroupIdentifiers_t,modelIds: List[int]) -> (ReturnValuesEnum,dotGrReinforcementSetGroupIdentifiers_t,List[int]) """
  pass
 def ExportSectionMarkAttributesHandler(self,pSectionMarkAttributes):
  """ ExportSectionMarkAttributesHandler(self: ICDelegate,pSectionMarkAttributes: dotGrSectionMarkAttributes_t) -> (ReturnValuesEnum,dotGrSectionMarkAttributes_t) """
  pass
 def ExportSectionMarkHandler(self,pSectionMark):
  """ ExportSectionMarkHandler(self: ICDelegate,pSectionMark: dotGrSectionMark_t) -> (ReturnValuesEnum,dotGrSectionMark_t) """
  pass
 def ExportStraightDimensionHandler(self,StraightDimension):
  """ ExportStraightDimensionHandler(self: ICDelegate,StraightDimension: dotGrStraightDimension_t) -> (int,dotGrStraightDimension_t) """
  pass
 def ExportStraightDimensionSetAttributesHandler(self,StraightDimensionSetAttributes):
  """ ExportStraightDimensionSetAttributesHandler(self: ICDelegate,StraightDimensionSetAttributes: dotGrStraightDimensionSetAttributes_t) -> (int,dotGrStraightDimensionSetAttributes_t) """
  pass
 def ExportStraightDimensionSetExcludePartsAccordingToFilter(self,drawingObject):
  """ ExportStraightDimensionSetExcludePartsAccordingToFilter(self: ICDelegate,drawingObject: dotGrDrawingObject_t) -> (int,dotGrDrawingObject_t) """
  pass
 def ExportStraightDimensionSetHandler(self,StraightDimensionSet):
  """ ExportStraightDimensionSetHandler(self: ICDelegate,StraightDimensionSet: dotGrStraightDimensionSet_t) -> (int,dotGrStraightDimensionSet_t) """
  pass
 def ExportStringListHandler(self,pStringList):
  """ ExportStringListHandler(self: ICDelegate,pStringList: dotGrStringList_t) -> (int,dotGrStringList_t) """
  pass
 def ExportSurfacingAttributesHandler(self,pSurfacingAttributes):
  """ ExportSurfacingAttributesHandler(self: ICDelegate,pSurfacingAttributes: dotGrSurfacingAttributes_t) -> (int,dotGrSurfacingAttributes_t) """
  pass
 def ExportSurfacingHandler(self,pSurfacing):
  """ ExportSurfacingHandler(self: ICDelegate,pSurfacing: dotGrSurfacing_t) -> (int,dotGrSurfacing_t) """
  pass
 def ExportSymbolAttributesHandler(self,pSymbolAttributes):
  """ ExportSymbolAttributesHandler(self: ICDelegate,pSymbolAttributes: dotGrSymbolAttributes_t) -> (int,dotGrSymbolAttributes_t) """
  pass
 def ExportSymbolHandler(self,pSymbol):
  """ ExportSymbolHandler(self: ICDelegate,pSymbol: dotGrSymbol_t) -> (ReturnValuesEnum,dotGrSymbol_t) """
  pass
 def ExportTextAttributesHandler(self,pTextAttributes):
  """ ExportTextAttributesHandler(self: ICDelegate,pTextAttributes: dotGrTextAttributes_t) -> (int,dotGrTextAttributes_t) """
  pass
 def ExportTextFileAttributesHandler(self,pTextFileAttributes):
  """ ExportTextFileAttributesHandler(self: ICDelegate,pTextFileAttributes: dotGrTextFileAttributes_t) -> (ReturnValuesEnum,dotGrTextFileAttributes_t) """
  pass
 def ExportTextFileHandler(self,pTextFile):
  """ ExportTextFileHandler(self: ICDelegate,pTextFile: dotGrTextFile_t) -> (ReturnValuesEnum,dotGrTextFile_t) """
  pass
 def ExportTextHandler(self,pText):
  """ ExportTextHandler(self: ICDelegate,pText: dotGrText_t) -> (ReturnValuesEnum,dotGrText_t) """
  pass
 def ExportUserPropertyHandler(self,pProperty):
  """ ExportUserPropertyHandler(self: ICDelegate,pProperty: dotGrUserProperty_t) -> (ReturnValuesEnum,dotGrUserProperty_t) """
  pass
 def ExportViewAttributesHandler(self,pViewAttributes):
  """ ExportViewAttributesHandler(self: ICDelegate,pViewAttributes: dotGrViewAttributes_t) -> (int,dotGrViewAttributes_t) """
  pass
 def ExportViewCommandHandler(self,pViewCommand):
  """ ExportViewCommandHandler(self: ICDelegate,pViewCommand: dotGrViewCommand_t) -> (ReturnValuesEnum,dotGrViewCommand_t) """
  pass
 def ExportViewHandler(self,pView):
  """ ExportViewHandler(self: ICDelegate,pView: dotGrView_t) -> (ReturnValuesEnum,dotGrView_t) """
  pass
 def ExportWeldHandler(self,pWeld):
  """ ExportWeldHandler(self: ICDelegate,pWeld: dotGrWeld_t) -> (ReturnValuesEnum,dotGrWeld_t) """
  pass
 def ExportWeldMarkHandler(self,pWeldMark):
  """ ExportWeldMarkHandler(self: ICDelegate,pWeldMark: dotGrWeldMark_t) -> (int,dotGrWeldMark_t) """
  pass
 def ImportDoubleListHandler(self,pDoubleList):
  """ ImportDoubleListHandler(self: ICDelegate,pDoubleList: dotGrDoubleList_t) -> (int,dotGrDoubleList_t) """
  pass
 def ImportIntListHandler(self,pIntList):
  """ ImportIntListHandler(self: ICDelegate,pIntList: dotGrIntList_t) -> (int,dotGrIntList_t) """
  pass
 def ImportMarkElementListHandler(self,pElementList):
  """ ImportMarkElementListHandler(self: ICDelegate,pElementList: dotGrElementList_t) -> (int,dotGrElementList_t) """
  pass
 def ImportPointListHandler(self,pPointList):
  """ ImportPointListHandler(self: ICDelegate,pPointList: dotGrPointList_t) -> (int,dotGrPointList_t) """
  pass
 def ImportStringListHandler(self,pStringList):
  """ ImportStringListHandler(self: ICDelegate,pStringList: dotGrStringList_t) -> (int,dotGrStringList_t) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class IEventHandler:
 # no doc
 def AddListener(self,EventListener):
  """ AddListener(self: IEventHandler,EventListener: Events)AddListener(self: IEventHandler,EventListener: Events) """
  pass
 def RemoveListener(self,EventListener):
  """ RemoveListener(self: IEventHandler,EventListener: Events)RemoveListener(self: IEventHandler,EventListener: Events) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class LayoutManager(object):
 # no doc
 @staticmethod
 def CloseEditor():
  """ CloseEditor() """
  pass
 @staticmethod
 def DoesTableLayoutExist(name):
  """ DoesTableLayoutExist(name: str) -> bool """
  pass
 @staticmethod
 def HiddenTableVisibility():
  """ HiddenTableVisibility() -> bool """
  pass
 @staticmethod
 def RefreshUI():
  """ RefreshUI() """
  pass
 @staticmethod
 def SetHiddenTableVisibility(Visibility):
  """ SetHiddenTableVisibility(Visibility: bool) """
  pass
 @staticmethod
 def SetNameVisibility(Visibility):
  """ SetNameVisibility(Visibility: bool) """
  pass
 @staticmethod
 def TableNameVisibility():
  """ TableNameVisibility() -> bool """
  pass
 __all__=[
  'CloseEditor',
  'DoesTableLayoutExist',
  'HiddenTableVisibility',
  'RefreshUI',
  'SetHiddenTableVisibility',
  'SetNameVisibility',
  'TableNameVisibility',
 ]


class LayoutTable(object):
 """ LayoutTable() """
 def GetDrawingNames(self):
  """ GetDrawingNames(self: LayoutTable) -> List[str] """
  pass
 def Insert(self,PickedPoint):
  """ Insert(self: LayoutTable,PickedPoint: Point) -> bool """
  pass
 def IsTableDwg(self):
  """ IsTableDwg(self: LayoutTable) -> bool """
  pass
 def IsTableKeyplan(self):
  """ IsTableKeyplan(self: LayoutTable) -> bool """
  pass
 def Modify(self):
  """ Modify(self: LayoutTable) -> bool """
  pass
 def Select(self):
  """ Select(self: LayoutTable) -> bool """
  pass
 def SetTableDwgDxf(self):
  """ SetTableDwgDxf(self: LayoutTable) """
  pass
 def SetTableKeyPlan(self):
  """ SetTableKeyPlan(self: LayoutTable) """
  pass
 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Angle(self: LayoutTable) -> float

Set: Angle(self: LayoutTable)=value
"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FileName(self: LayoutTable) -> str

Set: FileName(self: LayoutTable)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: LayoutTable) -> int

Set: Id(self: LayoutTable)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: LayoutTable) -> str

Set: Name(self: LayoutTable)=value
"""

 OverlapVithViews=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OverlapVithViews(self: LayoutTable) -> bool

Set: OverlapVithViews(self: LayoutTable)=value
"""

 RefCorner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RefCorner(self: LayoutTable) -> int

Set: RefCorner(self: LayoutTable)=value
"""

 RefTableId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RefTableId(self: LayoutTable) -> int

Set: RefTableId(self: LayoutTable)=value
"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Scale(self: LayoutTable) -> float

Set: Scale(self: LayoutTable)=value
"""

 TableCorner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TableCorner(self: LayoutTable) -> int

Set: TableCorner(self: LayoutTable)=value
"""

 TableLayoutId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TableLayoutId(self: LayoutTable) -> int

Set: TableLayoutId(self: LayoutTable)=value
"""

 TableType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TableType(self: LayoutTable) -> int

Set: TableType(self: LayoutTable)=value
"""

 XOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: XOffset(self: LayoutTable) -> float

Set: XOffset(self: LayoutTable)=value
"""

 YOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: YOffset(self: LayoutTable) -> float

Set: YOffset(self: LayoutTable)=value
"""



class PropertyType(Enum):
 """ enum PropertyType,values: TYPE_DOUBLE (1),TYPE_INT (0),TYPE_STRING (2) """
 TYPE_DOUBLE=None
 TYPE_INT=None
 TYPE_STRING=None
 value__=None


class QueryTypeEnum(Enum):
 """ enum QueryTypeEnum,values: ATTRIBUTES_LOAD (50),AUTOMATION_RUN_AUTODRAWINGS (300),DRAWING_CHECK_PART_TYPE (104),DRAWING_COMMIT_CHANGES (100),DRAWING_LOAD_LAYOUT_ATTRIBUTES (102),DRAWING_PLACE_VIEWS (101),DRAWING_UPDATE (103),HANDLER_CHECK_MODEL_STATUS (250),HANDLER_GET_ACTIVE_DRAWING_ID (203),HANDLER_GET_ACTIVE_DRAWING_TYPE (204),HANDLER_GET_DRAWING_TYPE (205),HANDLER_LAYOUT_EDITOR_OPERATION (211),HANDLER_LAYOUT_EDITOR_QUERY (210),HANDLER_SAVE_AND_CLOSE_ACTIVE_DRAWING (202),HANDLER_SET_ACTIVE_DRAWING (201),HANDLER_TABLELAYOUT_OPERATION (215),HANDLER_TABLELAYOUT_QUERY (214),HANDLER_TABLELAYOUT_TABLE_OPERATION (213),HANDLER_TABLELAYOUT_TABLE_QUERY (212),LOAD_SYMBOL_LIBRARIES (55),QUERY_CACHED_SELECT (4),QUERY_DELETE (0),QUERY_INSERT (1),QUERY_SELECT (3),QUERY_UPDATE (2),RETRIEVE_ATTRIBUTES (56),UDA_QUERY_ALL_DOUBLES (403),UDA_QUERY_ALL_INTEGERS (404),UDA_QUERY_ALL_STRINGS (402),UDA_QUERY_GET (400),UDA_QUERY_SET (401) """
 ATTRIBUTES_LOAD=None
 AUTOMATION_RUN_AUTODRAWINGS=None
 DRAWING_CHECK_PART_TYPE=None
 DRAWING_COMMIT_CHANGES=None
 DRAWING_LOAD_LAYOUT_ATTRIBUTES=None
 DRAWING_PLACE_VIEWS=None
 DRAWING_UPDATE=None
 HANDLER_CHECK_MODEL_STATUS=None
 HANDLER_GET_ACTIVE_DRAWING_ID=None
 HANDLER_GET_ACTIVE_DRAWING_TYPE=None
 HANDLER_GET_DRAWING_TYPE=None
 HANDLER_LAYOUT_EDITOR_OPERATION=None
 HANDLER_LAYOUT_EDITOR_QUERY=None
 HANDLER_SAVE_AND_CLOSE_ACTIVE_DRAWING=None
 HANDLER_SET_ACTIVE_DRAWING=None
 HANDLER_TABLELAYOUT_OPERATION=None
 HANDLER_TABLELAYOUT_QUERY=None
 HANDLER_TABLELAYOUT_TABLE_OPERATION=None
 HANDLER_TABLELAYOUT_TABLE_QUERY=None
 LOAD_SYMBOL_LIBRARIES=None
 QUERY_CACHED_SELECT=None
 QUERY_DELETE=None
 QUERY_INSERT=None
 QUERY_SELECT=None
 QUERY_UPDATE=None
 RETRIEVE_ATTRIBUTES=None
 UDA_QUERY_ALL_DOUBLES=None
 UDA_QUERY_ALL_INTEGERS=None
 UDA_QUERY_ALL_STRINGS=None
 UDA_QUERY_GET=None
 UDA_QUERY_SET=None
 value__=None


class Remoter(object):
 """ Remoter() """
 @staticmethod
 def InitializeSandBox():
  """ InitializeSandBox() -> bool """
  pass
 @staticmethod
 def PublishTypes():
  """ PublishTypes() """
  pass

class ReturnValuesEnum(Enum):
 """ enum ReturnValuesEnum,values: DOT_GR_DRAWING_CANNOT_DELETE_ACTIVE (201),DOT_GR_DRAWING_CANNOT_INSERT (202),DOT_GR_DRAWING_CANNOT_MODIFY (200),DOT_GR_ERROR_DRAWING_EDITOR_MUST_BE_CLOSED (4),DOT_GR_ERROR_DRAWING_IS_ACTIVE (5),DOT_GR_ERROR_ILLEGAL_QUERYTYPE (2),DOT_GR_ERROR_ILLEGAL_VIEW_TYPE (6),DOT_GR_ERROR_INVALID_ATTRIBUTES_GIVEN (2000),DOT_GR_ERROR_INVALID_PICKER_INPUT (7),DOT_GR_ERROR_NUMBERING_NOT_UPTODATE (3),DOT_GR_OPERATION_FAILED (1),DOT_GR_OPERATION_NOT_SUPPORTED (500),DOT_GR_OPERATION_OK (0) """
 DOT_GR_DRAWING_CANNOT_DELETE_ACTIVE=None
 DOT_GR_DRAWING_CANNOT_INSERT=None
 DOT_GR_DRAWING_CANNOT_MODIFY=None
 DOT_GR_ERROR_DRAWING_EDITOR_MUST_BE_CLOSED=None
 DOT_GR_ERROR_DRAWING_IS_ACTIVE=None
 DOT_GR_ERROR_ILLEGAL_QUERYTYPE=None
 DOT_GR_ERROR_ILLEGAL_VIEW_TYPE=None
 DOT_GR_ERROR_INVALID_ATTRIBUTES_GIVEN=None
 DOT_GR_ERROR_INVALID_PICKER_INPUT=None
 DOT_GR_ERROR_NUMBERING_NOT_UPTODATE=None
 DOT_GR_OPERATION_FAILED=None
 DOT_GR_OPERATION_NOT_SUPPORTED=None
 DOT_GR_OPERATION_OK=None
 value__=None


class ScopedCDelegateSetter(object):
 """ ScopedCDelegateSetter(deleg: ICDelegate) """
 def Dispose(self):
  """ Dispose(self: ScopedCDelegateSetter) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 @staticmethod
 def __new__(self,deleg):
  """ __new__(cls: type,deleg: ICDelegate) """
  pass

class SyncHandler(MulticastDelegate):
 """ SyncHandler(object: object,method: IntPtr) """
 def BeginInvoke(self,callback,object):
  """ BeginInvoke(self: SyncHandler,callback: AsyncCallback,object: object) -> IAsyncResult """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: SyncHandler,result: IAsyncResult) """
  pass
 def Invoke(self):
  """ Invoke(self: SyncHandler) """
  pass
 @staticmethod
 def __new__(self,object,method):
  """ __new__(cls: type,object: object,method: IntPtr) """
  pass

class TableLayout(object):
 # no doc
 @staticmethod
 def GetAllTemplates():
  """ GetAllTemplates() -> List[str] """
  pass
 @staticmethod
 def GetCurrentTables():
  """ GetCurrentTables() -> List[int] """
  pass
 @staticmethod
 def GetSelectedTables():
  """ GetSelectedTables() -> List[int] """
  pass
 @staticmethod
 def IsValid():
  """ IsValid() -> bool """
  pass
 @staticmethod
 def Save():
  """ Save() -> bool """
  pass
 @staticmethod
 def SaveAs(name):
  """ SaveAs(name: str) -> bool """
  pass
 @staticmethod
 def SelectTable(table):
  """ SelectTable(table: LayoutTable) """
  pass
 @staticmethod
 def UnselectTables():
  """ UnselectTables() """
  pass
 __all__=[
  'GetAllTemplates',
  'GetCurrentTables',
  'GetSelectedTables',
  'IsValid',
  'Save',
  'SaveAs',
  'SelectTable',
  'UnselectTables',
 ]


