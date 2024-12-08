import boto3

def lambda_handler(event,context):
    ec2 = boto3.client("ec2",region_name="us-east-1")

    instance_ids = []

    try:
        response = ec2.stop_instances(InstanceIds=instance_ids,DryRun=False)
        print(f"{instance_ids} : STOPPED ")
        print(f"Response: {response}")
        return {
            'statusCode' : 200,
            'body' : f"{instance_ids} is/are STOPPED"
        }#the return statement will be helpful if the lambda was triggered by API gateway
    
    except Exception as e:
        print("Error stopping : {instance_ids}")

        return {
            'statusCode' : 500,
            'body' : f"{instance_ids} : error stopping"
        }#the return statement will be helpful if the lambda was triggered by API gateway
    

        