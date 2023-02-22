
# Striped Library

> v. 20230221

> author: southwickio

<br>

## Overview
Sigma Writer Wizard is a quick console Wizard for helping you write Sigma rules. [Sigma](https://github.com/SigmaHQ/sigma) is a rule format used for detecting security events and incidents. This format can be used to implement rules and alerts across a wide variety of cyber security tools.

## Striped Library Usage
1. Run sww.py
2. Follow wizard
3. Save yaml and json files
4. Make sure to test your rule before deploying it in a production environment.

## Sigma Writing Considerations
1. When writing Sigma rules, there are several major categories and best practices that you should follow to ensure that your rules are effective and efficient. Here are some categories to consider:
   - `logsource`: This category defines the log sources where the rule should be applied. This may include sources such as network traffic, system logs, application logs, etc. It's important to be specific about the log sources to avoid false positives.
   - `detection`: This category defines the specific event or behavior that the rule is looking for. This may include indicators of compromise (IOCs), suspicious patterns of behavior, or other criteria that suggest malicious activity.
   - `fields`: specifies the field to be checked and provides a brief description of it. This category is used to define the specific information within a log entry that should be evaluated to determine if a security event has occurred.
   - `threat`: provides additional information about the threat that the rule is detecting. This category can be used to specify the name of the threat, a brief description of it, and other relevant information such as the confidence level and severity level.
   - `context`: This category provides additional context for the detection, such as the target of the attack, the type of malware involved, or other relevant information that helps analysts understand the scope and severity of the threat.
   - `falsepositives`: This category provides guidance on how to avoid false positives by specifying conditions that should be met before triggering the rule.
   - `testing`: This category provides instructions for testing the rule to ensure that it is working correctly and producing accurate results.
2. The required fields for a Sigma rule are `logsource`, `detection`, and `fields`. These three categories provide the minimum information required to define a detection scenario.
3. While the `threat` and `falsepositives` categories are not required, they are highly recommended as they can provide valuable information for analysts. 
4. The `threat` category can be used to specify information about the threat that the rule is detecting, such as the name, description, confidence level, and severity level. 
5. The `falsepositives` category can be used to specify conditions that can cause a false positive and how to avoid them.
6. The `meta`, `custom`, and `version` categories are all optional and can be used to provide additional information about the rule, such as metadata, custom fields, and version information.

## Sigma Rule Best Practices:
1. Keep the rule concise and focused on a specific detection scenario.
2. Use standard syntax and formatting to make the rule easy to read and maintain.
3. Use comments to provide additional information about the rule and its intended use.
4. Use test data to verify that the rule is working as intended.
5. Continuously update and refine the rule to ensure it remains effective and relevant.

## Sigma Rule in JSON Format Example
```
{
  "title": "Detect suspicious network traffic",
  "status": "experimental",
  "tags": [
    "network-traffic",
    "suspicious"
  ],
  "author": "John Doe",
  "version": {
    "number": "1.0",
    "date": "2022-12-31"
  },
  "references": [
    "https://example.com/threat-reports/remote-access-trojan"
  ],
  "notes": "This rule is still in development and may produce false positives",
  "logsource": {
    "category": "network",
    "subcategory": "firewalls"
  },
  "detection": {
    "condition": "source.ip in ('192.168.1.1', '192.168.2.2') and destination.port = 4444",
    "description": "Detects traffic to suspicious IP addresses on port 4444",
    "level": "high"
  },
  "fields": {
    "destination.port": "Port used by the destination"
  },
  "threat": {
    "name": "Suspicious Remote Access Trojan (RAT)",
    "description": "Detects traffic to known command and control server associated with the RAT",
    "confidence": "high",
    "severity": "medium"
  },
  "falsepositives": {
    "condition": "Traffic to legitimate server on port 4444",
    "description": "Verify that the destination is a known good IP address"
  }
}
```

## Sigma Rule in YAML Format Example
```
title: Detect suspicious network traffic
status: experimental
tags:
  - network-traffic
  - suspicious
author: John Doe
version:
  number: 1.0
  date: 2022-12-31
references:
  - https://example.com/threat-reports/remote-access-trojan
notes: This rule is still in development and may produce false positives
logsource:
  category: network
  subcategory: firewalls
detection:
  condition: "source.ip in ('192.168.1.1', '192.168.2.2') and destination.port = 4444"
  description: Detects traffic to suspicious IP addresses on port 4444
  level: high
fields:
  destination.port: Port used by the destination
threat:
  name: Suspicious Remote Access Trojan (RAT)
  description: Detects traffic to known command and control server associated with the RAT
  confidence: high
  severity: medium
falsepositives:
  condition: "Traffic to legitimate server on port 4444"
  description: Verify that the destination is a known good IP address
```
In this example, the Sigma rule is designed to detect suspicious network traffic to known malicious IP addresses associated with a remote access Trojan (RAT). The rule looks for traffic to specific IP addresses on port 4444 and specifies the severity and confidence levels of the threat. It also includes information on how to avoid false positives and provides references to external sources for further information.

Note that in YAML format, the dash notation is used to indicate a list or an array of items. Therefore, you would typically use the dash notation when defining a list of subcategories within a category. So, the dash notation is typically used for subcategories when defining a list of items, but it is not required for categories or subcategories that only have a single item.

## Resources
1. [Sigma Home](https://github.com/SigmaHQ/sigma)
2. [YAML](https://yaml.org/)