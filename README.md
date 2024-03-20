<h2>Automating S3 Data Replication Between AWS Accounts</h2>

Considering: <br>
Account-A as Source Account<br>
Account-B as Destination Account

Refer files : <br>
Account-A : File to create replication rule<br>
Account-B : To edit bucket policy

To Verify :<br>
	     First upload file in source bucket and click on the object and check whether its completed or not 
	     then go to destination account and check the object and see the status replica
      
In case of failure:<br>
        Check bucket policy which is in destination bucket, iam role attached to s3 source bucket
