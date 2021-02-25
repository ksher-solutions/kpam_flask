# kpam
Ksher Payment Agent Module

## Introduction

KPAM is a Python module, it's an agent for Ksher Payment Services, with below features:

- Exposing simple API for application to use
- Handling the connection setup and communication encryption/protection with Ksher Services
- Logging for all the payment related information, but without the sensitive information which should not be logged

## How to run on Heroku

1. please fork this github into your own account

2. login into you heroku account or if you still don't have accout please sigh up. [here's](https://heroku.com) heroku website.

3. on [Heroku's dashboard](https://dashboard.heroku.com/apps)click "New-->Create new app" and you will leads to create app page as shown below
![alt text](/image/createAppPage.JPG)

4. In deploy Menu Choose "Connect to github"
![alt text](/image/connectToGithub.JPG)

5. Connect to you forked github
![alt text](/image/connectToYourGithub.JPG)

6. Don't forget to set your deploy method
![alt text](/image/setDeployMethod.JPG)

## Settings
before you are able to use this app you need to config some variables first

1. go to heroku's app settings menu, on Config Vars section click "Reveal Config Vars"
![alt text](/image/revealConfig.JPG)

2. Two configs that needs to be add are
- APP_ID: mchXXXXX (x is your merchant id)
- PRIVATE_KEY: that you receive from our merchant web just coppy the value and out it here
![alt text](/image/configAdd.JPG)

## How to use
1. the app is now running, you can just use postman to called it
![alt text](/image/testGatewaypay.JPG)



