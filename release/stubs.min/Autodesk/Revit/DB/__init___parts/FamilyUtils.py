class FamilyUtils(object):
 """ Contains utilities related to family operations. """
 @staticmethod
 def ConvertFamilyToFaceHostBased(document,familyId):
  """
  ConvertFamilyToFaceHostBased(document: Document,familyId: ElementId)

   Converts a family to be face host based.

  

   document: The document containing the family to be converted.

   familyId: The family id.
  """
  pass
 @staticmethod
 def FamilyCanConvertToFaceHostBased(document,familyId):
  """
  FamilyCanConvertToFaceHostBased(document: Document,familyId: ElementId) -> bool

  

   Indicates whether the family can be converted to face host based.

  

   document: The document.

   familyId: The element id of the family.

   Returns: True if the family can be converted to face-based.

     Otherwise false,which 

    will be returned if there any family instances exist in the project,the family 

    is already face-based,or the family does not have a host.

     Also,false is 

    returned if the family does not belong to one of the following categories:

     

    OST_CommunicationDevicesOST_DataDevicesOST_DuctTerminalOST_ElectricalEquipmentOS

    T_ElectricalFixturesOST_FireAlarmDevicesOST_LightingDevicesOST_LightingFixturesO

    ST_MechanicalEquipmentOST_NurseCallDevicesOST_PlumbingFixturesOST_SecurityDevice

    sOST_SprinklersOST_TelephoneDevices
  """
  pass
 @staticmethod
 def GetProfileSymbols(document,profileFamilyUsage,oneCurveLoopOnly):
  """
  GetProfileSymbols(document: Document,profileFamilyUsage: ProfileFamilyUsage,oneCurveLoopOnly: bool) -> ICollection[ElementId]

  

   Gets the profile Family Symbols of the document.

  

   document: The document.

   profileFamilyUsage: The profile family usage.

   oneCurveLoopOnly: Whether or not to return only profiles with one curve loop.

   Returns: The set of profile Family Symbol element ids.
  """
  pass
 __all__=[
  'ConvertFamilyToFaceHostBased',
  'FamilyCanConvertToFaceHostBased',
  'GetProfileSymbols',
 ]

