# Striped Library
> v. 20230221

> author: southwickio

<br>

## Overview
### This application is under development.
Sigma Wizard Writer

## Sigma Writing Considerations
Sigma is a rule format used for detecting security events and incidents. When writing Sigma rules, there are several major categories and best practices that you should follow to ensure that your rules are effective and efficient. Here are some categories and best practices to consider:

Log Sources: This category defines the log sources where the rule should be applied. This may include sources such as network traffic, system logs, application logs, etc. It's important to be specific about the log sources to avoid false positives.

Detection: This category defines the specific event or behavior that the rule is looking for. This may include indicators of compromise (IoCs), suspicious patterns of behavior, or other criteria that suggest malicious activity.

Context: This category provides additional context for the detection, such as the target of the attack, the type of malware involved, or other relevant information that helps analysts understand the scope and severity of the threat.

False Positives: This category provides guidance on how to avoid false positives by specifying conditions that should be met before triggering the rule.

Testing: This category provides instructions for testing the rule to ensure that it is working correctly and producing accurate results.

Some best practices to follow when writing Sigma rules include:

Keep the rule concise and focused on a specific detection scenario.

Use standard syntax and formatting to make the rule easy to read and maintain.

Use comments to provide additional information about the rule and its intended use.

Use test data to verify that the rule is working as intended.

Continuously update and refine the rule to ensure it remains effective and relevant.

By following these categories and best practices, you can create effective Sigma rules that help identify security incidents and protect your organization from threats.


## Resources
1. [Sigma Home](https://github.com/SigmaHQ/sigma)