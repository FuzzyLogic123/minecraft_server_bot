import os
from time import sleep
import boto3
# from instance_wrapper import InstanceWrapper
from pprint import pprint
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()


my_config = Config(
    region_name = 'ap-southeast-4',
)

ec2 = boto3.resource('ec2')
client = boto3.client('ec2', config=my_config)


def start_server(id=os.getenv("INSTANCE_ID")) -> dict:

    while True:
        ec2_instances = client.describe_instances()
        for instance in ec2_instances["Reservations"][0]["Instances"]:
            if instance["InstanceId"] == id:
                if instance["State"]["Code"] == 80:
                    client.start_instances(InstanceIds=[id], DryRun=False) 

                elif instance["State"]["Code"] == 16:
                    return {
                        "message": "Server launched at:",
                        "ip": instance["PublicIpAddress"]
                    }
        sleep(1)

def stop_server(id=os.getenv("INSTANCE_ID")) -> dict:
    ec2_instances = client.describe_instances()
    for instance in ec2_instances["Reservations"][0]["Instances"]:
        if instance["InstanceId"] == id:
            if instance["State"]["Code"] == 16:
                client.stop_instances(InstanceIds=[id], DryRun=False)
                return {
                    "message": "Shutting down Server",
                    "ip": None
                }
            elif instance["State"]["Code"] == 32 or instance["State"]["Code"] == 64:
                return {
                    "message": "Server already shutting down",
                    "ip": None
                }
    return {
        "message": "Server already closed",
        "ip": None
    }
