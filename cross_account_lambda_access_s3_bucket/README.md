<h2> Cross Account S3 Access in lambda </h2>

Account-A :<br> Create role, policy to access Account-B s3 bucket, create lambda and attach role to it. <br>
Account-B :<br> Create bucket policy in Account B by specifying role arn created in Account A and upload file in s3<br>

To check : <br>
     Run the lambda function after deploying it.

