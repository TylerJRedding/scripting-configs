from enum import Enum

"""A class that enumerates all of the environment that are available for deployment.
    Specification of what environments must be check is completed within main.py
"""


class EnvironmentType(Enum):
    NA = "not-assigned"
    UAT1Develop = "uat1"
    UAT2Develop = "uat2"
    UAT3Develop = "uat3"
    UAT4Develop = "uat4"
    MASTERProps = " master"
    PRODMaster = "prod"
    PRODAPMaster = "prod-ap"


class ServiceName(Enum):
    TEST = "test"
    COBCalculations = "cob-calculations"
    COBAudit = "cob-audit"
    COBEvaluation = "cob-evaluation"
