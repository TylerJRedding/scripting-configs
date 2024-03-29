"""A class that will hold all pertinent information relating to the service
    Each instation of the class service will be made for branch of service.
        - For example uat1, prod, prod-ap, or base service properties on master
"""
import Constants


class Service:

    def __init__(self, serviceName):
        self.serviceName = serviceName
        self.propertiesDict = dict()
        self.environmentType = Constants.EnvironmentType.NA
        self.repo = "not-assigned"
        self.filePath = "not-assigned"
        # Two list that can be utilized to hold errors and warnings
        self.errorList = []
        self.warningList = []

    def setServiceName(self, serviceName):
        self.serviceName = serviceName
    def getServiceName(self):
        return self.serviceName

    def setEnvironmentType(self, environmentType):
        self.environmentType = environmentType
    def getEnvironmentType(self):
        return self.environmentType

    def setRepo(self, repo):
        self.repo = repo
    def getRepo(self):
        return self.repo

    def setFilePath(self, filePath):
        self.filePath = filePath
    def getFilePath(self):
        return self.filePath

    def getPropertiesDict(self):
        return self.propertiesDict

    def setWarningInList(self, warning):
        self.warningList.append(warning)
    def getWarningList(self):
        return self.warningList

    def setErrorInList(self, error):
        self.errorList.append(error)
    def getErrorList(self):
        return self.errorList


    def __str__(self):
        #serviceNameOutput = "ServiceName: " + self.serviceName.value
        #envTypeOutput = "EnvironmentType: " + self.environmentType.value
        filePathOutput = "filePath: " + self.filePath
        return filePathOutput #serviceNameOutput + envTypeOutput #+
