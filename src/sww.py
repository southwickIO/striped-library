#!/usr/bin/env python3



###############################################################################
# NAME: sww.py                                                                #
#                                                                             #
# VERSION: 20230221                                                           #
#                                                                             #
# SYNOPSIS: Sigma Rule Wizard that provides console steps for users to create #
#           their sigma rules                                                 #
#                                                                             #
#                                                                             #
# DESCRIPTION: This script provides a clean format for the user to create     #
#              Sigma rules.                                                   #
#                                                                             #
# INPUT: User input prompts                                                   #
#                                                                             #
# OUTPUT: STDOUT                                                              #
#                                                                             #
# PRE-RUNTIME NOTES: None.                                                    #
#                                                                             #
# AUTHORS: @southwickio                                                       #
#                                                                             #
# LICENSE: GPLv3                                                              #
#                                                                             #
# DISCLAIMER: All work produced by Authors is provided “AS IS”. Authors make  #
#             no warranties, express or implied, and hereby disclaims any and #
#             all warranties, including, but not limited to, any warranty of  #
#             fitness, application, et cetera, for any particular purpose,    #
#             use case, or application of this script.                        #
#                                                                             #
###############################################################################



#import dependencies
import yaml
import json



#declare Sigma rule fields and other variables
title = ""
status = ""
tags = []
author = ""
version = {"number": "", "date":""}
references = []
notes = ""
logsource = {"category": "", "subcategory": ""}
detection = {"condition": "", "description": "", "level": ""}
fields = {}
threat = {"name": "", "description": "", "confidence": "", "severity": ""}
falsepositive = {"condition": "", "description": ""}
sigmarule = {"title": title, \
    "status": status, \
    "tags": tags, \
    "author": author, \
    "version": version, \
    "references": references, \
    "notes": notes, \
    "logsource": logsource, \
    "detection": detection, \
    "fields": fields, \
    "threat": threat, \
    "falsepositive": falsepositive}



#entry point
try:

    #print banner
    print('''


          ___           ___           ___           ___               
         /\__\         /\  \         /\  \         /\  \              
        /:/ _/_       _\:\  \       _\:\  \       /::\  \       ___   
       /:/ /\  \     /\ \:\  \     /\ \:\  \     /:/\:\__\     /|  |  
      /:/ /::\  \   _\:\ \:\  \   _\:\ \:\  \   /:/ /:/  /    |:|  |  
     /:/_/:/\:\__\ /\ \:\ \:\__\ /\ \:\ \:\__\ /:/_/:/  /     |:|  |  
     \:\/:/ /:/  / \:\ \:\/:/  / \:\ \:\/:/  / \:\/:/  /    __|:|__|  
      \::/ /:/  /   \:\ \::/  /   \:\ \::/  /   \::/__/    /::::\  \  
       \/_/:/  /     \:\/:/  /     \:\/:/  /     \:\  \    ~~~~\:\  \ 
         /:/  /       \::/  /       \::/  /       \:\__\        \:\__\\
         \/__/         \/__/         \/__/         \/__/         \/__/

         Sigma Writer Wizard

         author: southwickio
         version: 20230221



         ''')


    #determine if user wants to create a new rule
    while True:

        wantnewrule = input("Would you like to create a Sigma rule [y/n]? ")
        
        if wantnewrule == 'y':
            wantnewrule = True
            break
        
        elif wantnewrule == 'n':
            wantnewrule = False
            break
        
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")



    # begin rule creation
    if wantnewrule:

        #stdout
        print("\n\nPlease follow the wizard to have your Sigma rule created.")
        print("Optional categories can be skipped by pressing enter.\n\n")
        


        #get Sigma rule title
        while True:

            title = input("Enter your Sigma Rule title ([e]xample): ")

            if title == 'e':
                print('Example: Detect suspicious network traffic')
                continue
            elif title:
                print('\n\n')
                break
            else:
                print("Invalid input. Please enter a title for your rule.")



        #get Sigma rule status
        while True:

            status = input("Enter your Sigma Rule status ([e]xample): ")

            if status == 'e':
                print('Example: experimental')
                continue
            elif status:
                print('\n\n')
                break
            else:
                print("Invalid input. Please enter a title for your rule.")



        #get Sigma rule tags
        while True:

            tag = input("Enter a tag for your Sigma Rule ([e]xample): ")

            if tag == 'e':
                print('Example: network-traffic')
                print('Example: suspicious')
                continue

            elif tag:    

                #append new tag
                tags.append(tag)

                #check if user wants another tag added
                anothertag = ""
                while True:
                    anothertag = input("Would you like to enter another tag [y/n]? ")

                    if anothertag == 'y':
                        break
                    elif anothertag == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

                #loop around if user wanted another tag
                if anothertag == 'y':
                    continue
                else:
                    print('\n\n')
                    break

            else:
                print('\n\n')
                break



        #get Sigma rule author
        while True:

            author = input("Enter your Sigma Rule author ([e]xample): ")

            if author == 'e':
                print('Example: southwickio')
                continue

            else:
                print('\n\n')
                break



        #get Sigma rule version number
        while True:

            versionnumber = input("Enter your Sigma rule version number ([e]xample): ")

            if versionnumber == 'e':
                print("Example: 1.0")
                continue
            elif versionnumber:
                version["number"] = versionnumber
                print('\n\n')
                break
            else:
                print('\n\n')
                break



        #get Sigma rule version date
        while True:

            versiondate = input("Enter your Sigma Rule version date ([e]xample): ")
            
            if versiondate == 'e':
                print("Example: 2023-02-21")
                continue
            elif versiondate:
                version["date"] = versiondate
                print('\n\n')
                break
            else:
                print('\n\n')
                break



        #get Sigma rule references
        while True:

            reference = input("Enter a reference for your Sigma Rule ([e]xample): ")

            if reference == 'e':
                print("Example: https://example.com/threat-reports/remote-access-trojan")
                continue

            elif reference:    

                #append new tag
                references.append(reference)

                #check if user wants another tag added
                anotherreference = ""
                while True:
                    anotherreference = input("Would you like to enter another reference [y/n]? ")

                    if anotherreference == 'y':
                        break
                    elif anotherreference == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

                #loop around if user wanted another tag
                if anotherreference == 'y':
                    continue
                else:
                    print('\n\n')
                    break

            else:
                print('\n\n')
                break



        #get Sigma rule notes
        while True:

            notes = input("Enter your Sigma Rule notes ([e]xample): ")

            if notes == 'e':
                print('Example: This rule is still in development and may produce false positives')
                continue
            else:
                print('\n\n')
                break



        #get Sigma rule logsource category
        while True:

            logsourcecategory = input("Enter your Sigma Rule logsource category ([e]xample): ")

            if logsourcecategory == 'e':
                print("Example: network")
                continue
            elif logsourcecategory:
                logsource["category"] = logsourcecategory
                print('\n\n')
                break
            else:
                print("This category is required. Please enter a logsource category for your rule.")



        #get Sigma rule logsource subcategory
        while True:

            logsoursubcecategory = input("Enter your Sigma Rule logsource subcategory ([e]xample): ")

            if logsoursubcecategory == 'e':
                print("Example: firewalls")
                continue
            else:
                logsource["subcategory"] = logsoursubcecategory
                print('\n\n')
                break



        #get Sigma rule detection condition
        while True:

            detectioncondition = input("Enter your Sigma Rule detection condition ([e]xample): ")

            if detectioncondition == 'e':
                print("Example: source.ip in ('192.168.1.1', '192.168.2.2') and destination.port = 4444")
                continue
            elif detectioncondition:
                detection["condition"] = detectioncondition
                print('\n\n')
                break
            else:
                print("This category is required. Please enter a detection condition for your rule.")



        #get Sigma rule detection description
        while True:

            detectiondescription = input("Enter your Sigma Rule detection description ([e]xample): ")

            if detectiondescription == 'e':
                print("Example: Detects traffic to suspicious IP addresses on port 4444")
                continue
            elif detectiondescription:
                detection["description"] = detectiondescription
                print('\n\n')
                break
            else:
                print("This category is required. Please enter a detection description for your rule.")



        #get Sigma rule detection level
        while True:

            detectionlevel = input("Enter your Sigma Rule detection level ([e]xample): ")

            if detectionlevel == 'e':
                print("Example: high")
                continue
            elif detectionlevel:
                detection["level"] = detectionlevel
                print('\n\n')
                break
            else:
                print("This category is required. Please enter a detection level for your rule.")



        #get Sigma rule fields
        while True:

            fieldname = input("Enter your Sigma Rule field name ([e]xample): ")
            fieldrule = input("Enter your Sigma Rule field rule ([e]xample): ")

            if fieldname == 'e' or fieldrule == 'e':
                print("Example name: destination.port")
                print("Example rule: Port used by the destination")
                continue

            elif fieldname and fieldrule:
                fields[fieldname] = fieldrule
                print('\n\n')

                #check if user wants another tag added
                anotherfield = ""
                while True:
                    anotherfield = input("Would you like to enter another field [y/n]? ")

                    if anotherfield == 'y':
                        break
                    elif anotherfield == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

                #loop around if user wanted another field
                if anotherfield == 'y':
                    continue
                else:
                    print('\n\n')
                    break

            else:
                print("This category is required. Please enter a field for your rule.")



        #get Sigma threat name
        while True:

            threatname = input("Enter your Sigma Rule threat name ([e]xample): ")

            if threatname == 'e':
                print("Example: Suspicious Remote Access Trojan (RAT)")
                continue
            else:
                threat["name"] = threatname
                print('\n\n')
                break



        #get Sigma rule threat description
        while True:

            threatdescription = input("Enter your Sigma Rule threat description ([e]xample): ")

            if threatdescription == 'e':
                print("Example: high")
                continue
            else:
                threat["description"] = threatdescription
                print('\n\n')
                break



        #get Sigma rule threat confidence
        while True:

            threatconfidence = input("Enter your Sigma Rule threat confidence ([e]xample): ")

            if threatconfidence == 'e':
                print("Example: high")
                continue
            else:
                threat["confidence"] = threatconfidence
                print('\n\n')
                break



        #get Sigma rule threat severity
        while True:

            threatseverity = input("Enter your Sigma Rule threat severity ([e]xample): ")

            if threatseverity == 'e':
                print("Example: medium")
                continue
            else:
                threat["severity"] = threatseverity
                print('\n\n')
                break



        #get Sigma rule falsepositive condition
        while True:

            fpcondition = input("Enter your Sigma Rule false positive condition ([e]xample): ")

            if fpcondition == 'e':
                print("Example: Traffic to legitimate server on port 4444")
                continue
            else:
                falsepositive["condition"] = fpcondition
                print('\n\n')
                break

     

        #get Sigma rule falsepositive description
        while True:

            fpdescription = input("Enter your Sigma Rule false positive description ([e]xample): ")

            if fpdescription == 'e':
                print("Example: Verify that the destination is a known good IP address")
                continue
            else:
                falsepositive["description"] = fpdescription
                print('\n\n')
                break



    else:

        #exit
        print("\n\nExiting.\n\n")
        exit()



    #prepare file title
    #yamlfilename = title.replace(" ","-") + ".yaml"
    #jsonfilename = title.replace(" ","-") + ".json"



    #print YAML
    print("\n\nYAML Format (save to file)")
    print("--------------------------\n\n")
    print(yaml.dump(sigmarule), '\n\n')



    #print JSON
    print("\n\nJSON Format (save to file)")
    print("--------------------------\n\n")
    print(json.dumps(sigmarule, indent=4), '\n\n')



    #exit 0
    print("\n\nExiting.\n\n")



except KeyboardInterrupt:
	print("\n\nExiting.\n\n")