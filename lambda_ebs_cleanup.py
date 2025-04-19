import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all EC2 instances (running & stopped)
    instances = ec2.describe_instances(Filters=[
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ])
    
    # Get all volume IDs in use
    used_volume_ids = set()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for mapping in instance.get('BlockDeviceMappings', []):
                volume_id = mapping.get('Ebs', {}).get('VolumeId')
                if volume_id:
                    used_volume_ids.add(volume_id)

    # Get all snapshots owned by this account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    # Find and delete unused snapshots
    deleted = 0
    for snapshot in snapshots:
        if 'VolumeId' in snapshot:
            volume_id = snapshot['VolumeId']
            if volume_id not in used_volume_ids:
                print(f"Deleting snapshot {snapshot['SnapshotId']} - volume {volume_id} not in use.")
                ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
                deleted += 1

    return {
        'statusCode': 200,
        'body': f'Deleted {deleted} unused snapshots.'
    }
