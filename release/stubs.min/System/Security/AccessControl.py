# encoding: utf-8
# module System.Security.AccessControl calls itself AccessControl
# from mscorlib,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089,System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def AccessRule(*args,**kwargs): # real signature unknown
 """ Represents a combination of a user's identity,an access mask,and an access control type (allow or deny). An System.Security.AccessControl.AccessRule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated. """
 pass
def AuditRule(*args,**kwargs): # real signature unknown
 """ Represents a combination of a user's identity and an access mask. An System.Security.AccessControl.AuditRule object also contains information about how the rule is inherited by child objects,how that inheritance is propagated,and for what conditions it is audited. """
 pass
def ObjectSecurity(*args,**kwargs): # real signature unknown
 """ Provides the ability to control access to objects without direct manipulation of Access Control Lists (ACLs). This class is the abstract base class for the System.Security.AccessControl.CommonObjectSecurity and System.Security.AccessControl.DirectoryObjectSecurity classes. """
 pass
# classes
from AccessControl_parts.AccessControlActions import AccessControlActions
from AccessControl_parts.AccessControlModification import AccessControlModification
from AccessControl_parts.AccessControlSections import AccessControlSections
from AccessControl_parts.AccessControlType import AccessControlType
from AccessControl_parts.AceEnumerator import AceEnumerator
from AccessControl_parts.AceFlags import AceFlags
from AccessControl_parts.AceQualifier import AceQualifier
from AccessControl_parts.AceType import AceType
from AccessControl_parts.AuditFlags import AuditFlags
from AccessControl_parts.AuthorizationRule import AuthorizationRule
from AccessControl_parts.AuthorizationRuleCollection import AuthorizationRuleCollection
from AccessControl_parts.GenericAce import GenericAce
from AccessControl_parts.KnownAce import KnownAce
from AccessControl_parts.QualifiedAce import QualifiedAce
from AccessControl_parts.CommonAce import CommonAce
from AccessControl_parts.GenericAcl import GenericAcl
from AccessControl_parts.CommonAcl import CommonAcl
from AccessControl_parts.CommonObjectSecurity import CommonObjectSecurity
from AccessControl_parts.GenericSecurityDescriptor import GenericSecurityDescriptor
from AccessControl_parts.CommonSecurityDescriptor import CommonSecurityDescriptor
from AccessControl_parts.CompoundAce import CompoundAce
from AccessControl_parts.CompoundAceType import CompoundAceType
from AccessControl_parts.ControlFlags import ControlFlags
from AccessControl_parts.CryptoKeyAccessRule import CryptoKeyAccessRule
from AccessControl_parts.CryptoKeyAuditRule import CryptoKeyAuditRule
from AccessControl_parts.CryptoKeyRights import CryptoKeyRights
from AccessControl_parts.NativeObjectSecurity import NativeObjectSecurity
from AccessControl_parts.CryptoKeySecurity import CryptoKeySecurity
from AccessControl_parts.CustomAce import CustomAce
from AccessControl_parts.DirectoryObjectSecurity import DirectoryObjectSecurity
from AccessControl_parts.FileSystemSecurity import FileSystemSecurity
from AccessControl_parts.DirectorySecurity import DirectorySecurity
from AccessControl_parts.DiscretionaryAcl import DiscretionaryAcl
from AccessControl_parts.EventWaitHandleAccessRule import EventWaitHandleAccessRule
from AccessControl_parts.EventWaitHandleAuditRule import EventWaitHandleAuditRule
from AccessControl_parts.EventWaitHandleRights import EventWaitHandleRights
from AccessControl_parts.EventWaitHandleSecurity import EventWaitHandleSecurity
from AccessControl_parts.FileSecurity import FileSecurity
from AccessControl_parts.FileSystemAccessRule import FileSystemAccessRule
from AccessControl_parts.FileSystemAuditRule import FileSystemAuditRule
from AccessControl_parts.FileSystemRights import FileSystemRights
from AccessControl_parts.InheritanceFlags import InheritanceFlags
from AccessControl_parts.MutexAccessRule import MutexAccessRule
from AccessControl_parts.MutexAuditRule import MutexAuditRule
from AccessControl_parts.MutexRights import MutexRights
from AccessControl_parts.MutexSecurity import MutexSecurity
from AccessControl_parts.ObjectAccessRule import ObjectAccessRule
from AccessControl_parts.ObjectAce import ObjectAce
from AccessControl_parts.ObjectAceFlags import ObjectAceFlags
from AccessControl_parts.ObjectAuditRule import ObjectAuditRule
from AccessControl_parts.PrivilegeNotHeldException import PrivilegeNotHeldException
from AccessControl_parts.PropagationFlags import PropagationFlags
from AccessControl_parts.RawAcl import RawAcl
from AccessControl_parts.RawSecurityDescriptor import RawSecurityDescriptor
from AccessControl_parts.RegistryAccessRule import RegistryAccessRule
from AccessControl_parts.RegistryAuditRule import RegistryAuditRule
from AccessControl_parts.RegistryRights import RegistryRights
from AccessControl_parts.RegistrySecurity import RegistrySecurity
from AccessControl_parts.ResourceType import ResourceType
from AccessControl_parts.SecurityInfos import SecurityInfos
from AccessControl_parts.SemaphoreAccessRule import SemaphoreAccessRule
from AccessControl_parts.SemaphoreAuditRule import SemaphoreAuditRule
from AccessControl_parts.SemaphoreRights import SemaphoreRights
from AccessControl_parts.SemaphoreSecurity import SemaphoreSecurity
from AccessControl_parts.SystemAcl import SystemAcl
