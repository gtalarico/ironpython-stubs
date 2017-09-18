# encoding: utf-8
# module Grasshopper.Kernel.Sorting calls itself Sorting
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_NetworkSorter(object):
    """ GH_NetworkSorter() """
    def CreateContext(self, objs):
        """ CreateContext(self: GH_NetworkSorter, objs: List[IGH_DocumentObject]) """
        pass

    def CreateNodeList(self, objs):
        """ CreateNodeList(self: GH_NetworkSorter, objs: List[IGH_DocumentObject]) """
        pass

    def Sort(self, bDamp, bLimit):
        """ Sort(self: GH_NetworkSorter, bDamp: Single, bLimit: Single) """
        pass

    m_context = None
    m_nodes = None


class GH_NetworkSorterNode(object):
    """ GH_NetworkSorterNode(obj_target: IGH_DocumentObject) """
    def AdjustTarget(self, bDamp, bLimit):
        """ AdjustTarget(self: GH_NetworkSorterNode, bDamp: Single, bLimit: Single) """
        pass

    def ConstructLinkForces(self):
        """ ConstructLinkForces(self: GH_NetworkSorterNode) """
        pass

    def ConstructNodeForces(self, objs):
        """ ConstructNodeForces(self: GH_NetworkSorterNode, objs: List[IGH_DocumentObject]) """
        pass

    def RectangleClosestPoint(self, *args): #cannot find CLR method
        """ RectangleClosestPoint(self: GH_NetworkSorterNode, rec: RectangleF, pt: PointF) -> PointF """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj_target):
        """ __new__(cls: type, obj_target: IGH_DocumentObject) """
        pass

    m_pivot = None
    m_pull_x = None
    m_pull_y = None
    m_push_x = None
    m_push_y = None
    m_target = None


