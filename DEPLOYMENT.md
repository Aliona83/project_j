# Table of Contents

 # [Deployment](#deployment)
  * [Creating a Clone](#creating-a-clone)
  * [Forking this repository](#forking-this-repository)
  * [Heroku Deployment](#deployment---heroku)
  * [AWS S3 Bucket setup](#aws-s3-bucket-setup)
  * [Connecting Django to AWS S3](#connecting-django-to-aws-s3)
  * [Stripe Setting Up](#stripe-setting-up)

 
 # Creating a Clone

To clone this repository follow the below steps:

* Locate the repository at this link project_j.
* Under 'Code', see the different cloning options, HTTPS, SSH, and GitHub CLI. 
* Click the prefered cloning option, and then copy the link provided.
* Open Terminal.
* In Terminal, change the current working directory to the desired location of the cloned directory.
* Type 'git clone', and then paste the URL previously copied from GitHub.
* Type 'Enter' to create the local clone.

# Forking this repository

* Locate the repository at this link project_j
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
* This creates a copy of the repository

# Deployment - Heroku

1. Deploying to Heroku

 * Install gunicorn and freeze into requirements.txt
     * pip3 install gunicorn
     * pip3 freeze > requirements.txt
 * Create a Procfile in the root directory for Heroku to read:
      * web: gunicorn jewelry_shop.wsgi:application
* Temporarily disable collectstatic by logging into the Heroku CLI in the terminal or on Heroku.com and set DISABLE_COLLECTSTATIC to 1:
      * heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
 * Add the hostname of the Heroku app to allowed hosts in settings.py:
      * ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
* Save the settings.py file, and add and commit the changes:
      * git push Heroku main
* To enable automatic deploys on Heroku, go to the app in Heroku. On the deploy tab, connect to GitHub. Search for the repository and then click connect. Then click Enable Automatic Deploys.
2. Generate SECRET_KEY

* Django creates a Secret Key for each project upon creation. Unless you immediately added this to your env.py file, the key may now be compromised. 
* We can create a new one with the link below.
* Go to miniwebtool's Django Secret Key Generator, click on the Generate Django Secret Key button and copy the value.
* In Heroku, add a new Config Var SECRET_KEY and give it the value of the newly generated secret key and then click add.
* In the settings.py file add:
     * SECRET_KEY = os.environ.get('SECRET_KEY', '')
     * Change the DEBUG
     * DEBUG = 'DEVELOPMENT' in os.environ

* Save the settings.py file, add, commit and then git push these changes.

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

# Connecting Django to AWS S3

* Connecting Heroku to AWS S3
  pip3 install boto3
  pip3 install django-storages
  pip3 freeze > requirements.txt

* Add storages to the installed apps in settings.py
* Add the bucket configuration:

       if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

* Add the Secret Keys from the downloaded CSV file to Heroku: | AWS_ACCESS_KEY_ID | | AWS_SECRET_ACCESS_KEY | | USE_AWS | True |
* Remove COLLECTSTATIC variable from the Config Vars
* Create custom_storages.py file and add:    

     from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

* In settings.py, set the static locations as follows.

         # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

* Git add . and git push to save these changes.
* Go to s3 and create a new folder called media then click upload. Add the product images files, click next and under manage public permissions, * * * select grant public read access to these objects. Then click next through to the end and finally, click upload.

# Stripe Setting Up

 * We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.

 * Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.

 * Now we need to add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
 * Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.

 * Now we can add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.

 * In settings.py:

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')



