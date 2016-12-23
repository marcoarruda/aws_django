First deploy to amazon aws Elastic Beanstalk Django project

Follow this tutorial http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
After creating requirements.txt, remove "pkg-resources==0.0.0" from it. Otherwise, it will rises an error on EB server, because this is not a valid module.
