This program takes a Cloudformation template and makes it pretty by using the PyYaml library. It correctly handles custom Cloudformation tags, e.g. !ImportValue. These tags are preserved in the output. The output is printed to STDOUT.

Many thanks to Anthon for this StackOverflow answer: https://stackoverflow.com/a/43768117/3101224


Before:
```
AWSTemplateFormatVersion: '2010-09-09'
Description: Repository for Docker Images
Resources:
  Repository:
    Properties:
      RepositoryName: pied_piper
      RepositoryPolicyText:
        Statement:
        - Action: ['ecr:GetDownloadUrlForLayer', 'ecr:BatchGetImage', 'ecr:BatchCheckLayerAvailability', 'ecr:PutImage', 'ecr:InitiateLayerUpload', 'ecr:UploadLayerPart', 'ecr:CompleteLayerUpload', 'ecr:GetAuthorizationToken']
          Effect: Allow
          Principal:
            AWS: 
              - !ImportValue UserArn
          Sid: AllowPushPull
        Version: '2008-10-17'
    Type: AWS::ECR::Repository
 ```


After:
```
AWSTemplateFormatVersion: '2010-09-09'
Description: Repository for Docker Images
Resources:
  Repository:
    Properties:
      RepositoryName: pied_piper
      RepositoryPolicyText:
        Statement:
        - Action:
          - ecr:GetDownloadUrlForLayer
          - ecr:BatchGetImage
          - ecr:BatchCheckLayerAvailability
          - ecr:PutImage
          - ecr:InitiateLayerUpload
          - ecr:UploadLayerPart
          - ecr:CompleteLayerUpload
          - ecr:GetAuthorizationToken
          Effect: Allow
          Principal:
            AWS:
            - !ImportValue 'UserArn'
          Sid: AllowPushPull
        Version: '2008-10-17'
    Type: AWS::ECR::Repository
```
