#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A class that will hold all pertinent information relating to the service
    Each instation of the class service will be made for branch of service.
        - For example uat1, prod, prod-ap, or base service properties on master
"""
import Constants
from Constants import ServiceName
from Service import Service


# Passed 4 Service Objects that are each holding a populated dictionary
# with all properties and values mapped
def validateProduction(serviceList):
    baseDevelopService = None
    baseProdService = None
    prodService = None
    prodAPService = None

    successFlag = True

    # Loop through and create proper local variables
    for service in serviceList:
        if "Develop" in service.environmentType.name:
            baseDevelopService = service
        elif service.environmentType == Constants.EnvironmentType.MASTERProps:
            baseProdService = service
        elif service.environmentType == Constants.EnvironmentType.PRODMaster:
            prodService = service
        elif service.environmentType == Constants.EnvironmentType.PRODAPMaster:
            prodAPService = service
        else:
            pass

    # First check if all items in (develop) service-env.properties match master.properties
    # If all are there return true as criteria satisfied
    propertiesBaseCompareResults = set(baseProdService.propertiesDict) - set(baseDevelopService.propertiesDict)

    if len(propertiesBaseCompareResults) == 0:
        return True

    # Else check that any remaining properties are in both prod.properties and prod-ap.properties
    else:
        for remainingProp in propertiesBaseCompareResults:
            # Check both prod and prod-ap for this property
                # If present in both all good and it can be left
                # Else output it to a file including where it is missing
            # Create two bools for storing if its present
            prodEnvBool = remainingProp in set(prodService.propertiesDict)
            prodAPEnvBool = remainingProp in set(prodAPService.propertiesDict)
            if prodEnvBool and prodAPEnvBool:
                break
            elif prodEnvBool and not prodAPEnvBool:
                successFlag = False
                print(remainingProp + " found in prod but not prod-AP")
            elif not prodEnvBool and prodAPEnvBool:

                print(remainingProp + " found in prod but not prod-AP")
                successFlag = False
            else:
                print(remainingProp + " not found in either prod or prod-ap")
                successFlag = False
    return successFlag
    # Output all remaining variables within a csv file


# Dictionary population in the format
# Key   = anything before equal sign
# Value = anything after equal sign
def populatePropDictionary(serviceList):
    for service in serviceList:
        with open(service.filePath, "r") as fp:
            for line in fp:
                # Start inserting into dictionary after parsing and cleansing data
                line.rstrip()
                lineArray = line.split("=")
                if (lineArray[0]) in service.propertiesDict.keys():
                    # Add error for duplicate property
                    pass
                else:
                    # Insert into dictionary if key does not exist
                    service.propertiesDict.update({lineArray[0]: lineArray[1]})


def createFilePath(serviceList):
    for service in serviceList:
        if service.environmentType == Constants.EnvironmentType.NA:
            pass
        elif service.environmentType == Constants.EnvironmentType.MASTERProps:
            filePath = "./TestDocs/" + service.serviceName.value + ".properties"
            service.setFilePath(filePath)
        else:
            filePath = "./TestDocs/" + service.serviceName.value + "-" + service.environmentType.value + ".properties"
            service.setFilePath(filePath)


# Starting point into script.
# As of now manually create the 4 Service objects and send them into the logic class

if __name__ == '__main__':
    # In this case TEST would be replaced by full branch name such as cob-banking-calculation-service
    # Base properties from the develop branch
    testBase = Service(ServiceName.TEST)
    testBase.setEnvironmentType(Constants.EnvironmentType.UAT1Develop)
    # Base properties from the master service.properties
    testMaster = Service(ServiceName.TEST)
    testMaster.setEnvironmentType(Constants.EnvironmentType.MASTERProps)
    # Base properties from the master prod service.properties
    testProdMaster = Service(ServiceName.TEST)
    testProdMaster.setEnvironmentType(Constants.EnvironmentType.PRODMaster)
    # Base properties from the master prod service.properties
    testProdAPMaster = Service(ServiceName.TEST)
    testProdAPMaster.setEnvironmentType(Constants.EnvironmentType.PRODAPMaster)

    testServiceGroup = [testBase, testMaster, testProdMaster, testProdAPMaster]
    # The main logic driver portion
    # 1) Create file path string from given information of service and env.
    # 2) Populate the service object dict with above method
    # 3) Once all 4 dictionaries are populated compare them using above method

    # 1) Create File Path
    createFilePath(testServiceGroup)
    # 2) Populate
    populatePropDictionary(testServiceGroup)
    # 3) Validate
    # results will be True if no properties are missing
    # results will be False if properties are missing
    #   If False, a csv file will be outputted with the service name as the file name
    results = validateProduction(testServiceGroup)
    if results:
        print("Success: " + testBase.serviceName.value)
