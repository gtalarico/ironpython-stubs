# encoding: utf-8
# module Tekla.Structures.Internal calls itself Internal
# from Tekla.Structures,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Channels(object):
 # no doc
 @staticmethod
 def RegisterChannel(ChannelName):
  """ RegisterChannel(ChannelName: str) -> bool """
  pass
 __all__=[
  'RegisterChannel',
 ]


class DotAnalysisModuleManagerQuery(object):
 # no doc
 IsPresent=None
 Module=None


class dotClashCheckOptions_t(object):
 # no doc
 BoltHeadDiameter=None
 GetSet=None
 NutThickness=None


class dotComponentOptions_t(object):
 # no doc
 AssemblyLoosePartStartNumber=None
 BoltEdgeDistanceFactor=None
 BoltEdgeDistanceReference=None
 BoltSize=None
 BoltStandard=None
 FoldedPlateProfileName=None
 GetSet=None
 LoosePartStartNumber=None
 PartMaterial=None
 PartWeldedToPrimaryStartNumber=None
 PartWeldedToSecondaryStartNumber=None
 PlateProfileName=None


class dotCoordinateSystem_t(object):
 # no doc
 def FromStruct(self,P):
  """ FromStruct(self: dotCoordinateSystem_t,P: CoordinateSystem) """
  pass
 def ToStruct(self,P):
  """ ToStruct(self: dotCoordinateSystem_t,P: CoordinateSystem) """
  pass
 AxisX=None
 AxisY=None
 Origin=None


class dotGetAdvancedOption_t(object):
 """ dotGetAdvancedOption_t(OptionName: str,OptionType: int,ValueStringIteration: int) """
 @staticmethod
 def __new__(self,OptionName,OptionType,ValueStringIteration):
  """
  __new__[dotGetAdvancedOption_t]() -> dotGetAdvancedOption_t
  
  __new__(cls: type,OptionName: str,OptionType: int,ValueStringIteration: int)
  """
  pass
 aName=None
 aValueString=None
 Type=None
 ValueBool=None
 ValueDouble=None
 ValueInt=None
 ValueStringIteration=None


class dotIdentifierToGUID_t(object):
 # no doc
 @staticmethod
 def GetGuidByIdentifier(identifier):
  """ GetGuidByIdentifier(identifier: Identifier) -> str """
  pass
 @staticmethod
 def GetIdentifierByGuid(guid):
  """ GetIdentifierByGuid(guid: str) -> Identifier """
  pass
 GUID=None
 Identifier=None


class dotIdentifier_t(object):
 """ dotIdentifier_t(identifier: Identifier) """
 def FromStruct(self,identifier=None):
  """ FromStruct(self: dotIdentifier_t,identifier: Identifier)FromStruct(self: dotIdentifier_t) -> Identifier """
  pass
 def ToStruct(self,identifier):
  """ ToStruct(self: dotIdentifier_t,identifier: Identifier) """
  pass
 @staticmethod
 def __new__(self,identifier):
  """
  __new__[dotIdentifier_t]() -> dotIdentifier_t
  
  __new__(cls: type,identifier: Identifier)
  """
  pass
 aGUID=None
 ID=None
 ID2=None


class dotMatrix_t(object):
 """ dotMatrix_t(Size: int) """
 def FromStruct(self,Matrix):
  """ FromStruct(self: dotMatrix_t,Matrix: Matrix) """
  pass
 def ToStruct(self,Matrix):
  """ ToStruct(self: dotMatrix_t,Matrix: Matrix) """
  pass
 @staticmethod
 def __new__(self,Size):
  """
  __new__[dotMatrix_t]() -> dotMatrix_t
  
  __new__(cls: type,Size: int)
  """
  pass
 aMatrix=None


class dotModuleManagerQuery_t(object):
 # no doc
 aModule=None
 Configuration=None
 IsPresent=None


class dotPoint_t(object):
 """ dotPoint_t(point: Point) """
 def Equals(self,*__args):
  """
  Equals(self: dotPoint_t,obj: object) -> bool
  Equals(self: dotPoint_t,point: dotPoint_t) -> bool
  """
  pass
 def FromStruct(self,point):
  """ FromStruct(self: dotPoint_t,point: Point) """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: dotPoint_t) -> int """
  pass
 def ToString(self):
  """ ToString(self: dotPoint_t) -> str """
  pass
 def ToStruct(self,point):
  """ ToStruct(self: dotPoint_t,point: Point) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,point):
  """
  __new__[dotPoint_t]() -> dotPoint_t
  
  __new__(cls: type,point: Point)
  """
  pass
 def __ne__(self,*args):
  pass
 X=None
 Y=None
 Z=None


class dotProgramVersion_t(object):
 # no doc
 aBuildNumber=None
 aCopyRightText=None
 aProgramVersion=None
 aRevisionDate=None


class dotVector_t(object):
 """ dotVector_t(vector: Vector) """
 def Equals(self,*__args):
  """
  Equals(self: dotVector_t,obj: object) -> bool
  Equals(self: dotVector_t,point: dotVector_t) -> bool
  """
  pass
 def FromStruct(self,vector):
  """ FromStruct(self: dotVector_t,vector: Vector) """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: dotVector_t) -> int """
  pass
 def ToString(self):
  """ ToString(self: dotVector_t) -> str """
  pass
 def ToStruct(self,vector):
  """ ToStruct(self: dotVector_t,vector: Vector) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,vector):
  """
  __new__[dotVector_t]() -> dotVector_t
  
  __new__(cls: type,vector: Vector)
  """
  pass
 def __ne__(self,*args):
  pass
 Direction=None


class WrapperFunctionalityBase(object):
 # no doc
 def Invoke0(self,method):
  """ Invoke0[TResult](self: WrapperFunctionalityBase,method: TargetMethod0[TResult]) -> TResult """
  pass
 def Invoke1r(self,p0,method):
  """ Invoke1r[(T0,TResult)](self: WrapperFunctionalityBase,p0: T0,method: TargetMethod1r[T0,TResult]) -> (TResult,T0) """
  pass
 def Invoke1v(self,p0,method):
  """ Invoke1v[(T0,TResult)](self: WrapperFunctionalityBase,p0: T0,method: TargetMethod1v[T0,TResult]) -> TResult """
  pass
 def Invoke2rr(self,p0,p1,method):
  """ Invoke2rr[(T0,T1,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,method: TargetMethod2rr[T0,T1,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke2rv(self,p0,p1,method):
  """ Invoke2rv[(T0,T1,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,method: TargetMethod2rv[T0,T1,TResult]) -> (TResult,T0) """
  pass
 def Invoke2vr(self,p0,p1,method):
  """ Invoke2vr[(T0,T1,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,method: TargetMethod2vr[T0,T1,TResult]) -> (TResult,T1) """
  pass
 def Invoke2vv(self,p0,p1,method):
  """ Invoke2vv[(T0,T1,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,method: TargetMethod2vv[T0,T1,TResult]) -> TResult """
  pass
 def Invoke3rrr(self,p0,p1,p2,method):
  """ Invoke3rrr[(T0,T1,T2,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,method: TargetMethod3rrr[T0,T1,T2,TResult]) -> (TResult,T0,T1,T2) """
  pass
 def Invoke3rrv(self,p0,p1,p2,method):
  """ Invoke3rrv[(T0,T1,T2,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,method: TargetMethod3rrv[T0,T1,T2,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke3vrr(self,p0,p1,p2,method):
  """ Invoke3vrr[(T0,T1,T2,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,method: TargetMethod3vrr[T0,T1,T2,TResult]) -> (TResult,T1,T2) """
  pass
 def Invoke3vvr(self,p0,p1,p2,method):
  """ Invoke3vvr[(T0,T1,T2,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,method: TargetMethod3vvr[T0,T1,T2,TResult]) -> (TResult,T2) """
  pass
 def Invoke3vvv(self,p0,p1,p2,method):
  """ Invoke3vvv[(T0,T1,T2,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,method: TargetMethod3vvv[T0,T1,T2,TResult]) -> TResult """
  pass
 def Invoke4rrrr(self,p0,p1,p2,p3,method):
  """ Invoke4rrrr[(T0,T1,T2,T3,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,method: TargetMethod4rrrr[T0,T1,T2,T3,TResult]) -> (TResult,T0,T1,T2,T3) """
  pass
 def Invoke4vvrr(self,p0,p1,p2,p3,method):
  """ Invoke4vvrr[(T0,T1,T2,T3,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,method: TargetMethod4vvrr[T0,T1,T2,T3,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke5rrrrr(self,p0,p1,p2,p3,p4,method):
  """ Invoke5rrrrr[(T0,T1,T2,T3,T4,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5rrrrr[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1,T2,T3,T4) """
  pass
 def Invoke5rrvvv(self,p0,p1,p2,p3,p4,method):
  """ Invoke5rrvvv[(T0,T1,T2,T3,T4,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5rrvvv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke5vvrrv(self,p0,p1,p2,p3,p4,method):
  """ Invoke5vvrrv[(T0,T1,T2,T3,T4,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5vvrrv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke6rrrrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6rrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6rrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vrrrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6vrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6vrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vvvrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6vvvrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6vvvrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T3,T4,T5) """
  pass
 def Invoke9rrrrrrrrr(self,p0,p1,p2,p3,p4,p5,p6,p7,p8,method):
  """ Invoke9rrrrrrrrr[(T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult)](self: WrapperFunctionalityBase,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,p6: T6,p7: T7,p8: T8,method: TargetMethod9rrrrrrrrr[T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5,T6,T7,T8) """
  pass
 TargetMethod0`1=None
 TargetMethod1r`2=None
 TargetMethod1v`2=None
 TargetMethod2rr`3=None
 TargetMethod2rv`3=None
 TargetMethod2vr`3=None
 TargetMethod2vv`3=None
 TargetMethod3rrr`4=None
 TargetMethod3rrv`4=None
 TargetMethod3vrr`4=None
 TargetMethod3vvr`4=None
 TargetMethod3vvv`4=None
 TargetMethod4rrrr`5=None
 TargetMethod4vvrr`5=None
 TargetMethod5rrrrr`6=None
 TargetMethod5rrvvv`6=None
 TargetMethod5vvrrv`6=None
 TargetMethod6rrrrrr`7=None
 TargetMethod6vrrrrr`7=None
 TargetMethod6vvvrrr`7=None
 TargetMethod9rrrrrrrrr`10=None


class FormWrapperFunctionality(WrapperFunctionalityBase):
 """ FormWrapperFunctionality() """
 def Invoke0(self,method):
  """ Invoke0[TResult](self: FormWrapperFunctionality,method: TargetMethod0[TResult]) -> TResult """
  pass
 def Invoke1r(self,p0,method):
  """ Invoke1r[(T0,TResult)](self: FormWrapperFunctionality,p0: T0,method: TargetMethod1r[T0,TResult]) -> (TResult,T0) """
  pass
 def Invoke1v(self,p0,method):
  """ Invoke1v[(T0,TResult)](self: FormWrapperFunctionality,p0: T0,method: TargetMethod1v[T0,TResult]) -> TResult """
  pass
 def Invoke2rr(self,p0,p1,method):
  """ Invoke2rr[(T0,T1,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,method: TargetMethod2rr[T0,T1,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke2rv(self,p0,p1,method):
  """ Invoke2rv[(T0,T1,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,method: TargetMethod2rv[T0,T1,TResult]) -> (TResult,T0) """
  pass
 def Invoke2vr(self,p0,p1,method):
  """ Invoke2vr[(T0,T1,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,method: TargetMethod2vr[T0,T1,TResult]) -> (TResult,T1) """
  pass
 def Invoke2vv(self,p0,p1,method):
  """ Invoke2vv[(T0,T1,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,method: TargetMethod2vv[T0,T1,TResult]) -> TResult """
  pass
 def Invoke3rrr(self,p0,p1,p2,method):
  """ Invoke3rrr[(T0,T1,T2,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3rrr[T0,T1,T2,TResult]) -> (TResult,T0,T1,T2) """
  pass
 def Invoke3rrv(self,p0,p1,p2,method):
  """ Invoke3rrv[(T0,T1,T2,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3rrv[T0,T1,T2,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke3vrr(self,p0,p1,p2,method):
  """ Invoke3vrr[(T0,T1,T2,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3vrr[T0,T1,T2,TResult]) -> (TResult,T1,T2) """
  pass
 def Invoke3vvr(self,p0,p1,p2,method):
  """ Invoke3vvr[(T0,T1,T2,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3vvr[T0,T1,T2,TResult]) -> (TResult,T2) """
  pass
 def Invoke3vvv(self,p0,p1,p2,method):
  """ Invoke3vvv[(T0,T1,T2,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3vvv[T0,T1,T2,TResult]) -> TResult """
  pass
 def Invoke4rrrr(self,p0,p1,p2,p3,method):
  """ Invoke4rrrr[(T0,T1,T2,T3,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,method: TargetMethod4rrrr[T0,T1,T2,T3,TResult]) -> (TResult,T0,T1,T2,T3) """
  pass
 def Invoke4vvrr(self,p0,p1,p2,p3,method):
  """ Invoke4vvrr[(T0,T1,T2,T3,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,method: TargetMethod4vvrr[T0,T1,T2,T3,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke5rrrrr(self,p0,p1,p2,p3,p4,method):
  """ Invoke5rrrrr[(T0,T1,T2,T3,T4,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5rrrrr[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1,T2,T3,T4) """
  pass
 def Invoke5rrvvv(self,p0,p1,p2,p3,p4,method):
  """ Invoke5rrvvv[(T0,T1,T2,T3,T4,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5rrvvv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke5vvrrv(self,p0,p1,p2,p3,p4,method):
  """ Invoke5vvrrv[(T0,T1,T2,T3,T4,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,method: TargetMethod5vvrrv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke6rrrrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6rrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6rrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vrrrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6vrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6vrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vvvrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6vvvrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6vvvrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T3,T4,T5) """
  pass
 def Invoke9rrrrrrrrr(self,p0,p1,p2,p3,p4,p5,p6,p7,p8,method):
  """ Invoke9rrrrrrrrr[(T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult)](self: FormWrapperFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,p6: T6,p7: T7,p8: T8,method: TargetMethod9rrrrrrrrr[T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5,T6,T7,T8) """
  pass

class RemotingProxyFactory(MarshalByRefObject):
 """ RemotingProxyFactory() """
 def CreateRemotingProxy(self,assemblyName,typeName):
  """ CreateRemotingProxy(self: RemotingProxyFactory,assemblyName: str,typeName: str) -> object """
  pass

class RemotingProxyHelper(object):
 # no doc
 @staticmethod
 def CreateInstance(appUrl):
  """ CreateInstance[T](appUrl: str) -> T """
  pass
 @staticmethod
 def IsFormWrapperRequired():
  """ IsFormWrapperRequired() -> bool """
  pass
 @staticmethod
 def SetRemotingProxyFactory(factory):
  """ SetRemotingProxyFactory(factory: RemotingProxyFactory) """
  pass
 @staticmethod
 def TestInstance(instance):
  """ TestInstance(instance: object) """
  pass
 __all__=[
  'CreateInstance',
  'IsFormWrapperRequired',
  'SetRemotingProxyFactory',
  'TestInstance',
 ]


class SynchronizeInvokeFunctionality(WrapperFunctionalityBase):
 """ SynchronizeInvokeFunctionality(Instance: ISynchronizeInvoke) """
 def Invoke0(self,Method):
  """ Invoke0[TResult](self: SynchronizeInvokeFunctionality,Method: TargetMethod0[TResult]) -> TResult """
  pass
 def Invoke1r(self,P0,Method):
  """ Invoke1r[(T0,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,Method: TargetMethod1r[T0,TResult]) -> (TResult,T0) """
  pass
 def Invoke1v(self,P0,Method):
  """ Invoke1v[(T0,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,Method: TargetMethod1v[T0,TResult]) -> TResult """
  pass
 def Invoke2rr(self,P0,P1,Method):
  """ Invoke2rr[(T0,T1,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,Method: TargetMethod2rr[T0,T1,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke2rv(self,P0,P1,Method):
  """ Invoke2rv[(T0,T1,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,Method: TargetMethod2rv[T0,T1,TResult]) -> (TResult,T0) """
  pass
 def Invoke2vr(self,P0,P1,Method):
  """ Invoke2vr[(T0,T1,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,Method: TargetMethod2vr[T0,T1,TResult]) -> (TResult,T1) """
  pass
 def Invoke2vv(self,P0,P1,Method):
  """ Invoke2vv[(T0,T1,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,Method: TargetMethod2vv[T0,T1,TResult]) -> TResult """
  pass
 def Invoke3rrr(self,P0,P1,P2,Method):
  """ Invoke3rrr[(T0,T1,T2,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,Method: TargetMethod3rrr[T0,T1,T2,TResult]) -> (TResult,T0,T1,T2) """
  pass
 def Invoke3rrv(self,P0,P1,P2,Method):
  """ Invoke3rrv[(T0,T1,T2,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,Method: TargetMethod3rrv[T0,T1,T2,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke3vrr(self,p0,p1,p2,method):
  """ Invoke3vrr[(T0,T1,T2,TResult)](self: SynchronizeInvokeFunctionality,p0: T0,p1: T1,p2: T2,method: TargetMethod3vrr[T0,T1,T2,TResult]) -> (TResult,T1,T2) """
  pass
 def Invoke3vvr(self,P0,P1,P2,Method):
  """ Invoke3vvr[(T0,T1,T2,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,Method: TargetMethod3vvr[T0,T1,T2,TResult]) -> (TResult,T2) """
  pass
 def Invoke3vvv(self,P0,P1,P2,Method):
  """ Invoke3vvv[(T0,T1,T2,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,Method: TargetMethod3vvv[T0,T1,T2,TResult]) -> TResult """
  pass
 def Invoke4rrrr(self,P0,P1,P2,P3,Method):
  """ Invoke4rrrr[(T0,T1,T2,T3,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,Method: TargetMethod4rrrr[T0,T1,T2,T3,TResult]) -> (TResult,T0,T1,T2,T3) """
  pass
 def Invoke4vvrr(self,P0,P1,P2,P3,Method):
  """ Invoke4vvrr[(T0,T1,T2,T3,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,Method: TargetMethod4vvrr[T0,T1,T2,T3,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke5rrrrr(self,P0,P1,P2,P3,P4,Method):
  """ Invoke5rrrrr[(T0,T1,T2,T3,T4,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,Method: TargetMethod5rrrrr[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1,T2,T3,T4) """
  pass
 def Invoke5rrvvv(self,P0,P1,P2,P3,P4,Method):
  """ Invoke5rrvvv[(T0,T1,T2,T3,T4,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,Method: TargetMethod5rrvvv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T0,T1) """
  pass
 def Invoke5vvrrv(self,P0,P1,P2,P3,P4,Method):
  """ Invoke5vvrrv[(T0,T1,T2,T3,T4,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,Method: TargetMethod5vvrrv[T0,T1,T2,T3,T4,TResult]) -> (TResult,T2,T3) """
  pass
 def Invoke6rrrrrr(self,P0,P1,P2,P3,P4,P5,Method):
  """ Invoke6rrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,P5: T5,Method: TargetMethod6rrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vrrrrr(self,p0,p1,p2,p3,p4,p5,method):
  """ Invoke6vrrrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: SynchronizeInvokeFunctionality,p0: T0,p1: T1,p2: T2,p3: T3,p4: T4,p5: T5,method: TargetMethod6vrrrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T1,T2,T3,T4,T5) """
  pass
 def Invoke6vvvrrr(self,P0,P1,P2,P3,P4,P5,Method):
  """ Invoke6vvvrrr[(T0,T1,T2,T3,T4,T5,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,P5: T5,Method: TargetMethod6vvvrrr[T0,T1,T2,T3,T4,T5,TResult]) -> (TResult,T3,T4,T5) """
  pass
 def Invoke9rrrrrrrrr(self,P0,P1,P2,P3,P4,P5,P6,P7,P8,Method):
  """ Invoke9rrrrrrrrr[(T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult)](self: SynchronizeInvokeFunctionality,P0: T0,P1: T1,P2: T2,P3: T3,P4: T4,P5: T5,P6: T6,P7: T7,P8: T8,Method: TargetMethod9rrrrrrrrr[T0,T1,T2,T3,T4,T5,T6,T7,T8,TResult]) -> (TResult,T0,T1,T2,T3,T4,T5,T6,T7,T8) """
  pass
 @staticmethod
 def __new__(self,Instance):
  """ __new__(cls: type,Instance: ISynchronizeInvoke) """
  pass

class WrapperDelegateHelper(object):
 # no doc
 @staticmethod
 def CreateDelegate(Instance,MethodName):
  """ CreateDelegate[T](Instance: object,MethodName: str) -> T """
  pass
 __all__=[
  'CreateDelegate',
 ]


