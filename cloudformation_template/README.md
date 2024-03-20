<h2>Cloudformation Template</h2>
Resources created:<br>
<li>
    VPC
    Subnets
    Route Tables
    Routes
    Transit Gateway 
</li>

In cloudformation template, we are using nested templates, where we are having main template and its calling other stack.

AWSTemplateFormatVersion: '2010-09-09'
Description: Description of template
Metadata: 
    AWS::CloudFormation::Interface 
      Defines the grouping and ordering of input parameters when they are displayed in the AWS CloudFormation console
      Properties:
         ParameterGroups
            list of parameter group types, where you specify group names, the parameters in each group, and the order in which the parameters are shown. 
         ParameterLabels
            Mapping of parameters and their friendly names that the CloudFormation console shows when a stack is created or updated.
Parameters:
   Define the parameter type and its default value
Resources:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters: passing all the parameters which will used by this stack
    TemplateURL: passing template url

