import boto3

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

# Creates empty list to store instance IDs
instances_ids = []

# Retrieve all EC2 instances
# describe_instances() returns a dictionary with 'Reservations' key
reservations = ec2_client.describe_instances()['Reservations']

# Iterate through each reservation
for reservation in reservations:
    instances = reservation['Instances']
    # Iterate through each instance in the reservation
    for instance in instances:
        # Add the instance ID to the list
        instances_ids.append(instance['InstanceId'])
        
# Create tags for all collected instance IDs
response = ec2_resource.create_tags(
    DryRun=False,
    Resources=instances_ids,  # List of instance IDs to tag
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'          
        },
    ]
)
