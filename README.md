# EC2 Instance Tag Automation

I created a Python script to automatically add environment tags to EC2 instances in AWS. This project helped me learn AWS automation using Python and Boto3.

[Suggested image: Screenshot of successfully tagged EC2 instances in AWS Console]

## What I Used
- Python
- AWS (EC2)
- Boto3 SDK

## What I Built
A script that:
- Connects to AWS using Boto3
- Fetches all EC2 instances in my account
- Adds environment tags to instances that don't have them
- Displays successful tagging operations

[Suggested image: Code snippet showing the core tagging function]

## Running The Script
I run it with:
```python
python tag_instances.py