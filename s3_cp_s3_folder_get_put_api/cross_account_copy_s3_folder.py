
import boto3
import datetime
import os


# using sts to get access keys
def lambda_handler(event, context):
    source_bucket = "sftp-enterprise-production"
    destination_bucket = "cbtl-my-bronze-data"
    destination_subfolder = "cbtl/downloads/data_dump"
    sessionM_key = "cbtl/downloads/data_dump/"

    # Creating prefix
    current_date = datetime.datetime.now()
    prev_date = current_date - datetime.timedelta(days=1)
    formatted_date = prev_date.strftime("%Y_%m_%d")
    source_prefix = sessionM_key + formatted_date
    destination_prefix = destination_subfolder + formatted_date
    # print(destination_prefix)
    destination_subfolder_with_date = f'cbtl/downloads/data_dump/{formatted_date}'
    sts_client = boto3.client("sts")
    sessionM_response = sts_client.assume_role(
        RoleArn="arn:aws:iam::415747287921:role/cbtl_partner-external",
        RoleSessionName="TestingSTS",
    )

    access_key = sessionM_response["Credentials"]["AccessKeyId"]
    secret_key = sessionM_response["Credentials"]["SecretAccessKey"]
    session_token = sessionM_response["Credentials"]["SessionToken"]

    sessionM_s3_client = boto3.client(
        "s3",
        region_name="us-east-1",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
    )

    list_object_response = sessionM_s3_client.list_objects_v2(
        Bucket=source_bucket, Prefix="cbtl/downloads/data_dump/" + formatted_date
    )
    # print(list_object_response)
    if "Contents" in list_object_response:
        # logic for copy folder without copy command
        for list_object in list_object_response['Contents']:
            source_key = list_object['Key']
            relative_key = source_key[len(source_prefix):]
            destination_key = os.path.join(destination_prefix, relative_key)
            print(destination_key)
            try:
                s3_object_response = sessionM_s3_client.get_object(Bucket=source_bucket, Key=source_key)
                object_body_data = s3_object_response['Body'].read()
            except Exception as e:
                print(e)

            cbtl_assume_role_response = sts_client.assume_role(
                RoleArn="arn:aws:iam::447228726790:role/lambda-storage-to-cbtl-put-sts-role",
                RoleSessionName="TestingSTS",
            )

            access_key = cbtl_assume_role_response["Credentials"]["AccessKeyId"]
            secret_key = cbtl_assume_role_response["Credentials"]["SecretAccessKey"]
            session_token = cbtl_assume_role_response["Credentials"]["SessionToken"]

            cbtl_s3_client = boto3.client(
                "s3",
                region_name="ap-southeast-1",
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                aws_session_token=session_token,
            )
            try:
                cbtl_s3_client.put_object(Bucket=destination_bucket,
                                          Key=(destination_subfolder_with_date + destination_key), Body=object_body_data)
            except Exception as e:
                print(e)
        raise Exception("Condition not met, Lambda function failed.")