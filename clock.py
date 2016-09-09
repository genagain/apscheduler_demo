from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import TwilioRestClient
import sendgrid
import os
from sendgrid.helpers.mail import *

sched = BlockingScheduler()
sched.start()

def text_gen():
  
  account_sid = "AC6e652d5e6bea5c4e494f9c7cb06be1a2"
  auth_token = "0d05da068ddc52eb021c930c27995ef0"
  client = TwilioRestClient(account_sid, auth_token)

  message = client.messages.create(to="+13479860720", from_="+16172022165", body="Hello Gen!")
  print('This job is run every two minutes.')

def send_email(recipient):
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("ohta.g@husky.neu.edu")
  subject = "Weekly update"
  # to_email = Email("j.kimani@northeastern.edu")
  to_email = Email("ohta.g@husky.neu.edu")
  content = Content("text/plain", "Hello, Email!")
  mail = Mail(from_email, subject, to_email, content)
  response = sg.client.mail.send.post(request_body=mail.get())

sched.add_cron_job(send_email, day_of_week='fri', hour=19, minute=50)
