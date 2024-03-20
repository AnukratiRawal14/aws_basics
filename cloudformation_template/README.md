<h2>Cloudformation Template</h2>
Resources created:<br>
<li>VPC</li>
<li>Subnets</li>
<li>Route Tables</li>
<li>Routes</li>
<li>Transit Gateway </li>
<br>
In cloudformation template, we are using nested templates, where we are having main template and its calling other stack. <br>
<br>

AWSTemplateFormatVersion: '2010-09-09'<br>
Description: Prod infra configuration template<br>
Metadata:<br>
   &emsp;AWS::CloudFormation::Interface:<br>
    &emsp;&emsp;&emsp;ParameterGroups:<br>
       &emsp;&emsp;&emsp; &emsp; &emsp; &emsp;-<br>
           &emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp; Label:<br>
           &emsp;&emsp; &emsp; &emsp;&emsp; &emsp;&emsp; &emsp; default: "Network Configuration"<br>
        &emsp; &emsp; &emsp; &emsp;&emsp; &emsp; Parameters:<br>
     &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;-  VpcName<br>
      &emsp;&emsp;&emsp;ParameterLabels:<br>
        &emsp; &emsp;&emsp; &emsp; &emsp;VpcName:<br>
           &emsp; &emsp;&emsp; &emsp; &emsp;&emsp; default: "Specify VPC Name"<br>
Parameters:<br>
   &emsp; &emsp;&emsp; VpcName:<br>
     &emsp; &emsp;&emsp; &emsp;&emsp; Description: Enter the name of VPC<br>
     &emsp; &emsp;&emsp; &emsp; &emsp;Type: String<br>
     &emsp; &emsp;&emsp; &emsp; &emsp;Default: underlay-vpc<br>
Resources:<br>
   &emsp; &emsp;NetworkStack:<br>
     &emsp; &emsp; &emsp;Type: AWS::CloudFormation::Stack<br>
     &emsp; &emsp; &emsp;Properties:<br>
       &emsp; &emsp; &emsp; &emsp;Parameters:<br>
         &emsp; &emsp; &emsp; &emsp; &emsp; VpcName: !Ref VpcName<br>
       &emsp; &emsp; &emsp; &emsp;TemplateURL: <br>
