<h2>Cloudformation Template</h2>
Resources created:<br>
<li>VPC</li>
<li>Subnets</li>
<li>Route Tables</li>
<li>Routes</li>
<li>Transit Gateway </li>

In cloudformation template, we are using nested templates, where we are having main template and its calling other stack.<br>

AWSTemplateFormatVersion: '2010-09-09'<br>
Description: Description of template<br>
Metadata: <br>
    AWS::CloudFormation::Interface <br>
      Defines the grouping and ordering of input parameters when they are displayed in the AWS CloudFormation console<br>
      Properties:<br>
         ParameterGroups<br>
            list of parameter group types, where you specify group names, the parameters in each group, and the order in which the parameters are shown. <br>
         ParameterLabels<br>
            Mapping of parameters and their friendly names that the CloudFormation console shows when a stack is created or updated.<br>
Parameters:<br>
   Define the parameter type and its default value<br>
Resources:<br>
    Type: AWS::CloudFormation::Stack<br>
    Properties:<br>
      Parameters: passing all the parameters which will used by this stack<br>
    TemplateURL: passing template url<br>

