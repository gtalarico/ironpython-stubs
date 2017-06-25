# encoding: utf-8
# module Revit.GeometryConversion calls itself GeometryConversion
# from RevitNodes, Version=1.3.0.875, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CurveUtils(object):
    # no doc
# Error generating skeleton for function CurvesAreSimilar: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function GetPlaneFromCurve: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function IsLineLike: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function PointArraysAreSame: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ReferencePointsAreSame: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    Tolerance = 9.9999999999999995e-07
    __all__ = [
        'CurvesAreSimilar',
        'GetPlaneFromCurve',
        'IsLineLike',
        'PointArraysAreSame',
        'ReferencePointsAreSame',
        'Tolerance',
    ]


class DynamoToRevitBRep(object):
    # no doc
# Error generating skeleton for function ToRevitType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToRevitType',
    ]


class GeometryObjectConverter(object):
    # no doc
# Error generating skeleton for function Convert: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ConvertToMany: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function InternalConvert: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'Convert',
        'ConvertToMany',
        'InternalConvert',
    ]


class GeometryPrimitiveConverter(object):
    # no doc
# Error generating skeleton for function GetPerpendicular: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToCoordinateSystem: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    @staticmethod
    def ToDegrees(degrees):
        """ ToDegrees(degrees: float) -> float """
        pass

# Error generating skeleton for function ToDoubleArray: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToPlane: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToPoint: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToPoints: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToProtoType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    @staticmethod
    def ToRadians(degrees):
        """ ToRadians(degrees: float) -> float """
        pass

# Error generating skeleton for function ToRevitBoundingBox: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToRevitType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToTransform: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToVector: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToXyz: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToXyzs: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'GetPerpendicular',
        'ToCoordinateSystem',
        'ToDegrees',
        'ToDoubleArray',
        'ToPlane',
        'ToPoint',
        'ToPoints',
        'ToProtoType',
        'ToRadians',
        'ToRevitBoundingBox',
        'ToRevitType',
        'ToTransform',
        'ToVector',
        'ToXyz',
        'ToXyzs',
    ]


class NurbsUtils(object):
    # no doc
    @staticmethod
    def ElevateBezierDegree(crv, finalDegree):
        """ ElevateBezierDegree(crv: NurbsCurve, finalDegree: int) -> NurbsCurve """
        pass

    __all__ = [
        'ElevateBezierDegree',
    ]


class PolygonContainment(object):
    # no doc
# Error generating skeleton for function AdjustDelta: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function GetQuadrant: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function GetXIntercept: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function PolygonContains: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'AdjustDelta',
        'GetQuadrant',
        'GetXIntercept',
        'PolygonContains',
    ]


class ProtoToRevitCurve(object):
    # no doc
# Error generating skeleton for function ToRevitType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToRevitType',
    ]


class ProtoToRevitMesh(object):
    # no doc
# Error generating skeleton for function CreateBoundingBoxMeshForErrors: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function ToRevitType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'CreateBoundingBoxMeshForErrors',
        'ToRevitType',
    ]


class ProtoToRevitSolid(object):
    # no doc
# Error generating skeleton for function ToRevitFamilyType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToRevitFamilyType',
    ]


class RevitToProtoCurve(object):
    # no doc
# Error generating skeleton for function ToProtoType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoFace(object):
    # no doc
# Error generating skeleton for function ToProtoType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoMesh(object):
    # no doc
# Error generating skeleton for function ToProtoType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoSolid(object):
    # no doc
# Error generating skeleton for function ToProtoType: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ToProtoType',
    ]


class SurfaceExtractor(object):
    # no doc
# Error generating skeleton for function ExtractSurface: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    __all__ = [
        'ExtractSurface',
    ]


class UnitConverter(object):
    # no doc
    @staticmethod
    def ConvertToDynamoUnits(geometry):
# Error generating skeleton for function ConvertToDynamoUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def ConvertToHostUnits(geometry):
# Error generating skeleton for function ConvertToHostUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

# Error generating skeleton for function DynamoToHostFactor: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

# Error generating skeleton for function HostToDynamoFactor: [Errno 2] Could not load file or assembly 'RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.

    @staticmethod
    def InDynamoUnits(geometry):
# Error generating skeleton for function InDynamoUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def InHostUnits(geometry):
# Error generating skeleton for function InHostUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    __all__ = [
        'ConvertToDynamoUnits',
        'ConvertToHostUnits',
        'DynamoToHostFactor',
        'HostToDynamoFactor',
        'InDynamoUnits',
        'InHostUnits',
    ]


