group_defaults = {
    'lockbit3': [
        'Lockbit 3.0',
        'unknown', 'unknown', 'Phishing', 'Command and Scripting Interpreter',
        'Boot or Logon Autostart Execution', 'Access Token Manipulation',
        'Deobfuscate/Decode Files or Information', 'unknown', 'File and Directory Discovery',
        'Lateral Tool Transfer', 'unknown', 'unknown', 'Exfiltration Over Web Service',
        'Data Encrypted for Impact', 'SI',
        "Initial Access : Exploiting Pubblic Facing Application, Valid Accounts\n"
        "Execution : User Execution, Native API\n"
        "Privilage Escalation : Abuse Elevation Control Mechanism\n"
        "Defense Evasion : Impair Defenses, Hijack Execution Flow, System Binary Proxy Execution, Domain Policy Modification, Indicator Removal\n"
        "Discovery : Network Share Discovery, Remote System Discovery, Process Discovery\n"
        "Exfiltration : Exfiltration Over C2 Channel\n"
        "Impact : Service Stop, Defacement"
    ],
    'akira': [
        'Akira',
        'unknown', 'unknown', 'Valid Accounts', 'unknown technique',
        'Valid Accounts', 'Valid Accounts', 'Valid Accounts', 'OS Credential Dumping',
        'File and Directory Discovery', 'unknown', 'unknown', 'unknown',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Persistence : External Remote Services, Event Triggered Execution\n"
        "Initial Access : External Remote Services\n"
        "Privilege Escalation : Event Triggered Execution\n"
        "Defense Evasion : Modify Registry\n"
        "Impact : Inhibit System Recovery"
    ],
    'play': [
        'Play',
        'unknown', 'unknown', 'Exploit Public-Facing Application', 'Command and Scripting Interpreter',
        'unknown', 'unknown', 'Impair Defenses', 'OS Credential Dumping',
        'System Owner/User Discovery', 'Remote Services', 'Archive Collected Data',
        'Application Layer Protocol', 'Exfiltration Over Alternative Protocol', 'Data Encrypted for Impact', 'SI',
        "Initial Access: Valid Accounts\n"
        "Execution: Exploitation for Client Execution\n"
        "Defense Evasion: Deobfuscate/Decode Files or Information, Indicator Removal\n"
        "Credential Access: Unsecured Credentials\n"
        "Discovery: System Information Discovery, File and Directory Discovery, Network Share Discovery, Process Discovery, System Service Discovery\n"
        "Lateral Movement: Remote Services\n"
        "Impact: Service Stop, Inhibit System Recovery"
    ],
    'medusa': [
        'Medusa',
        'unknown', 'unknown', 'Phishing', 'Command and Scripting Interpreter',
        'Boot or Logon Autostart Execution', 'Abuse Elevation Control Mechanism', 'Impair Defenses', 'Brute Force',
        'File and Directory Discovery', 'Remote Services', 'Data from Local System', 'Application Layer Protocol',
        'Exfiltration Over Alternative Protocol', 'Data Encrypted for Impact', 'SI',
        "Initial Access: Valid Accounts, External Remote Services\n"
        "Discovery: Network Share Discovery, Query Registry\n"
        "Command and Control: Ingress Tool Transfer"
    ],
    'fog': [
        'Fog',
        'unknown', 'unknown', 'External Remote Services', 'Command and Scripting Interpreter',
        'Create Account', 'unknown', 'Impair Defenses', 'OS Credential Dumping',
        'Network Service Discovery', 'Remote Services', 'Data from Local System', 'unknown',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Initial Access: Valid Accounts\n"
        "Execution: System Services\n"
        "Defense Evasion: Use Alternate Authentication Material, Deobfuscate/Decode Files or Information, Indicator Removal\n"
        "Credential Access: Credentials from Password Stores, Brute Force\n"
        "Discovery: Network Share Discovery\n"
        "Lateral Movement: Lateral Tool Transfer\n"
        "Impact: Inhibit System Recovery, Service Stop"
    ],
    'rhysida': [
        'Rhysida',
        'unknown', 'unknown', 'Valid Accounts', 'Command and Scripting Interpreter',
        'Boot or Logon Autostart Execution', 'unknown', 'Valid Accounts', 'OS Credential Dumping',
        'unknown', 'unknown', 'Data from Local System', 'Application Layer Protocol',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Execution: Create or Modify System Process\n"
        "Command and Control: Remote Access Software\n"
        "Impact: Inhibit System Recovery"
    ],
    'ransomhub': [
        'Ransomhub',
        'unknown', 'unknown', 'unknown', 'Windows Management Instrumentation',
        'unknown', 'unknown', 'Indicator Removal', 'unknown',
        'unknown', 'unknown', 'Data from Local System', 'unknown',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Execution: Command and Scripting Interpreter"
    ],
    '8base': [
        '8base',
        'unknown', 'unknown', 'Phishing', 'unknown',
        'Boot or Logon Autostart Execution', 'Access Token Manipulation', 'Obfuscated Files or Information', 'unknown',
        'File and Directory Discovery', 'unknown', 'Data from Local System', 'unknown',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Privilege Escalation: Abuse Elevation Control Mechanism, Event Triggered Execution\n"
        "Defense Evasion: Virtualization/Sandbox Evasion, Impair Defenses, Deobfuscate/Decode Files or Information, Indicator Removal\n"
        "Discovery: System Information Discovery, Network Share Discovery, Process Discovery\n"
        "Impact: Inhibit System Recovery, System Binary Proxy Execution"
    ],
    'knight': [
        'Knight',
        'unknown', 'unknown', 'unknown', 'unknown',
        'unknown', 'unknown', 'unknown', 'unknown',
        'System Information Discovery', 'unknown', 'Archive Collected Data', 'unknown',
        'Exfiltration Over Alternative Protocol', 'Data Encrypted for Impact', 'SI',
        "Discovery: File and Directory Discovery, Process Discovery\n"
        "Impact: Service Stop, Inhibit System Recovery"
    ],
    'hunters': [
        'Hunters',
        'unknown', 'unknown', 'unknown', 'Command and Scripting Interpreter',
        'Boot or Logon Autostart Execution', 'Create or Modify System Process', 'Virtualization/Sandbox Evasion', 'unknown',
        'Network Share Discovery', 'unknown', 'Data from Local System', 'Application Layer Protocol',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Defense Evasion: Obfuscated Files or Information, Masquerading, Execution Guardrails, Create or Modify System Process\n"
        "Privilege Escalation: Access Token Manipulation\n"
        "Command and Control: Encrypted Channel"
    ],
    'cactus': [
        'Cactus',
        'unknown', 'unknown', 'Exploit Public-Facing Application', 'Command and Scripting Interpreter',
        'Scheduled Task/Job', 'Process Injection', 'Impair Defenses',
        'Credentials from Password Stores', 'System Network Connections Discovery', 'Remote Services',
        'Automated Collection', 'Remote Access Software',
        'Exfiltration Over Web Service', 'Data Encrypted for Impact', 'SI',
        "Execution: Windows Management Instrumentation, Shared Modules, Software Deployments Tools\n"
        "Persistence: Create Account, Hijack Execution Flow\n"
        "Defense Evasion: Obfuscated Files or Information, Process Injection, Masquerading, Virtualization/Sandbox Evasion, Hide Artifacts\n"
        "Credential Access: OS Credential Dumping, Input Capture\n"
        "Discovery: Account Discovery, Remote System Discovery, System Information Discovery, Software Discovery, Process Discovery, File and Directory Discovery\n"
        "Lateral Movement: Lateral Tool Transfer\n"
        "Collection: Input Capture\n"
        "Command and Control: Proxy, Application Layer Protocol, Non-Application Layer Protocol, Non-Standard Port, Encrypted Channel"
    ],
    'arcusmedia': [
        'Arcus Media',
        'unknown', 'unknown', 'Exploit Public-Facing Application', 'Shared Modules',
        'Hijack Execution Flow', 'Process Injection', 'Obfuscated Files or Information',
        'OS Credential Dumping', 'Network Service Discovery', 'Lateral Tool Transfer',
        'Data from Local System', 'Dynamic Resolution',
        'unknown', 'Data Encrypted for Impact', 'SI',
        "Initial Access: Replication Through Removable Media\n"
        "Execution: Command and Scripting Interpreter\n"
        "Defense Evasion: Virtualization/Sandbox Evasion, Indicator Removal\n"
        "Credential Access: Input Capture\n"
        "Discovery: Process Discovery, File and Directory Discovery, System Information Discovery, Software Discovery, File and Directory Discovery, Peripheral Device Discovery\n"
        "Command and Control: Ingress Tool Transfer\n"
        "Impact: Service Stop, Defacement"
    ]

}
