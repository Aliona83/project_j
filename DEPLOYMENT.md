# Table of Contents

 # [Deployment](#deployment)
  * [Creating a Clone](#creating-a-clone)
  * [Forking this repository](#forking-this-repository)
  * [Heroku Deployment](#deployment---heroku)
  * [AWS S3 Bucket setup](#aws-s3-bucket-setup)
  * AWS IAM(Identity and Access Managenent) setup ) 
  * Connecting Heroku to AWS S3

 #  Deployment


 ## AWS (S3 bucket setup):
 Sign in or create an account on AWS(l add link to AWS)
 1. Create a new S3 bucket:

 * Navigate and Click "Services" in the top left-hand corner of the landing page, click on "Storage" then click "S3."
 * Navigate and Click "Create bucket."
 * Give the bucket a unique name:
 * Will form part of the URL (in the case of this project, I called the S3 bucket pp5-blade)
 * Select the nearest location:
 My case EU (Ireland) eu-west-1.
 * Under the "Object Ownership" section, select "ACLS enabled"
 * Under the "Block Public Access settings for this bucket" section, untick "Block all public access" and tick the box to acknowledge that this will make the bucket public.
 * Navigate and Click "Create bucket."

2. Edit Bucket settings:

  * Bucket Properties: 

* Navigate and Click on the bucket name to open the bucket.
* Navigate and Click on the "Properties" tab.
* Under the "Static website hosting" section, click "Edit."
* Under the "Static website hosting" section select "Enable".
* Under the "Hosting type" section ensure "Host a static website" is selected.
* Under the "Index document" section enter "index.html".
* Navigate and Click "Save changes."

   * Bucket Permissions: -

* Navigate and Click on the "Permissions" tab.
* Scroll down to the "CORS configuration" section and click edit.

Enter the following snippet into the text box:
     [
         {
             "AllowedHeaders": [
             "Authorization"
             ],
             "AllowedMethods": [
             "GET"
             ],
             "AllowedOrigins": [
             "*"
             ],
             "ExposeHeaders": []
         }
     ]
* Navigate and Click "Save changes."
* Scroll back up to the "Bucket Policy" section and click "Edit."
* Take note of the "Bucket ARN" click on the "Policy Generator" button to open the AWS policy generator in a new tab.
* In the newly opened tab under Step 1 "Select Policy Type" select "S3 Bucket Policy." from the drop down menu.
* Under Step 2 "Add Statement(s)" enter " * " in the "Principal" text box.
* From the "s3:Action" drop down menu select "s3:GetObject".
* Enter the "ARN" noted from the bucket policy page into the "Amazon  Resource Name (ARN)" text box.
* Navigate and Click "Add Statement."
* Under Step 3 "Generate Policy" click "Generate Policy."
* Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
* In the same text box add "/*" to the end of the resource key to allow access to all resources in this bucket.
* Navigate and Click "Save changes."
* When back on the buckets permissions tab, scroll down to the "Access Control List" section and click "Edit."
enable "List" for "Everyone (public access)", tick the box to accept that "I understand the effects of these changes on my objects and buckets." and click "Save changes."

<details>
<summary>Click to see more</summary>
See Image quick guide(add screenschot images)
</details>
3. Create AWS static files User and assign to S3 Bucket:

   * Create "User Group": 

* Navigate and Click "Services" in the top left-hand corner of the landing page, from the left side of the menu click on "Security, Identity, & Compliance" and select "IAM" from the right side of the menu.
* Under "Access management" click "User Groups."
* Navigate and Click "Create Group."
* Enter a user name .
* Scroll to the bottom of the page and click "Create Group."

   * Create permissions policy for the new user group: 

* Navigate and Click "Policies" in the left-hand menu.
* Navigate and Click "Create Policy."
* Navigate and Click "Import managed policy."
* Search for "AmazonS3FullAccess", select this policy, and click "Import".
* Navigate and Click "JSON" under "Policy Document" to see the imported policy
* Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
* Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.
* Navigate and Click "Next: Tags."
* Navigate and Click "Next: Review."
* Navigate and Click "Review Policy."
* Enter a name for the policy.
* Enter a description for the policy.
* Navigate and Click "Create Policy."
    * Attach Policy to User Group: 

* Navigate and Click "User Groups" in the left-hand menu.
* Navigate and Click on the user group name created during the above step.
* Select the "Permissions" tab.
click "Attach Policy."
* Search for the policy created during the above step, and select it.
* Navigate and Click "Attach Policy."
     * Create User: 

* Navigate and Click "Users" in the left-hand menu.
* Navigate and Click "Add user."
* Enter a "User name" .
* Select "Programmatic access" and "AWS Management Console access."
Navigate and Click "Next: Permissions."
* Select "Add user to group."
* Select the user group created during the above step.
* Navigate and Click "Next: Tags."
* Navigate and Click "Next: Review."
* Navigate and Click "Create user."
* Take note of the "Access key ID" and "Secret access key" as these will be needed to connect to the S3 bucket.
* Navigate and Click "Download .csv" to download the credentials.
* Navigate and Click "Close."

4 .Connect S3 Bucket to Project by adding folloeing code t your settings.py file:(add screenschot with code)

# Deployment - Heroku

# Creating a Clone

To clone this repository follow the below steps:

* Locate the repository at this link The Wine Garden BnB.
* Under 'Code', see the different cloning options, HTTPS, SSH, and GitHub CLI. 
* Click the prefered cloning option, and then copy the link provided.
* Open Terminal.
* In Terminal, change the current working directory to the desired location of the cloned directory.
* Type 'git clone', and then paste the URL previously copied from GitHub.
* Type 'Enter' to create the local clone.

# Forking this repository

* Locate the repository at this link The Wine Garden BnB.
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
* This creates a copy of the repository

