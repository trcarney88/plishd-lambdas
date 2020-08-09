# plishd-lamdas
Contains the Lambda Functions used in the notification system for Plishd

# Plishd Notification System
Plishd uses a combination of AWS resources(API Gateway, Lambda Functions, Step Functions) to create a severless notification system. When a user opts into notifications, they select a period (daily, weekly, monthly, quarterly, semi-annually, and annually), a time of day to recieve a notification, and the method in which they will receive the notification. Currently only email and text notifications are available. Once they have selected their options, an API request is sent out which calls the proper scheduling lambda function. The identifier, either the email address or phone number, of the user and the ARN of the step funciton that is created are saved in a DynamoDB database. These are used when the user wishes to change or opt out of notifications. When a user changes their notification settings, the current Step Function is deleted and a new one is created and saved to the database.

## Email Notifications
AWS SES is used to send out email notifications. When a user starts email notifications an API request is made to the notification system. This API request calls the ScheduleEmailNotification Lambda Function. This lambda creates a new instance of the SendEmail Step function with the users parameters and calculates the wait time for the step function. The ScheduleEmailNotification lambda also stores the email address of the user and the ARN of the newly created Step Function to a database. This is used to delete the Step Function if a user edits their notification settings or no longer wishes to receive notifications.

The step function, pictured below, waits for the alloted time and then calls the SendEmail lambda. This function Sends the reminder email based on a predefined template and calulates the wait time for the next email to be sent. The Step Fuctcion will run forever unless stopped by the DeleteScheduledReminder lambda or aborted manually by an administrator.

![Image of Email Step Function](https://github.com/trcarney88/plishd-lambdas/blob/master/Documentation/Images/stepfunctions_graph_email.png)

The continue block of the Step Function is there because AWS requires that all Step Functions to have an END block. The continue block makes it so the END block is never reached.

## Text Notifications
Text notifications work the same way as email notifications except Twilio is used to send the text messages. The Step Function and other mechanisms work in the same way as email notifications. The Step Function for Text notifications is shown below.

![Image of Text Step Function](https://github.com/trcarney88/plishd-lambdas/blob/master/Documentation/Images/stepfunctions_graph_sms.png)
