import boto3

def lambda_handler(event,context):

    ec2 = boto3.client("ec2",region_name="us-east-1")

    instance_ids = []

    try:
        response = ec2.start_instances(InstanceIds=instance_ids,DryRun=False)
        print(f"{instance_ids} : STARTED ")
        print(f"Response: {response}")

        return {
            'statusCode' : 200,
            'body' : f"{instance_ids} is/are STARTED"
        }#the return statement will be helpful if the lambda was triggered by API gateway
    
    except Exception as e:
        print("Error starting : {instance_ids}")

        return {
            'statusCode' : 500,
            'body' : f"{instance_ids} : error starting"
        }#the return statement will be helpful if the lambda was triggered by API gateway
    
