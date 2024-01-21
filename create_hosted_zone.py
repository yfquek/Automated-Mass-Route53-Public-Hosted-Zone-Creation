#!/usr/bin/env python

import sys
import subprocess
import json

def create_hosted_zone(domain):
    stack_name = f"HostedZoneStack-{domain.replace('.', '-')}"

    cloudformation_script = f"""
    {{
        "AWSTemplateFormatVersion": "2010-09-09",
        "Resources": {{
            "HostedZone": {{
                "Type": "AWS::Route53::HostedZone",
                "Properties": {{
                    "Name": "{domain}"
                }}
            }}
        }}
    }}
    """

    # Save the CloudFormation script to a temporary file
    with open("cloudformation_template.json", "w") as template_file:
        template_file.write(cloudformation_script)

    # Execute the AWS CLI command to create the CloudFormation stack
    subprocess.run(["aws", "cloudformation", "create-stack",
                    "--stack-name", stack_name,
                    "--template-body", "file://cloudformation_template.json",
                    "--capabilities", "CAPABILITY_IAM"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: create_hosted_zone.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    create_hosted_zone(domain)
