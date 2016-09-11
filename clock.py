from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import TwilioRestClient
import sendgrid
import os
from sendgrid.helpers.mail import *

def text_gen():
  account_sid = "AC6e652d5e6bea5c4e494f9c7cb06be1a2"
  auth_token = "0d05da068ddc52eb021c930c27995ef0"
  client = TwilioRestClient(account_sid, auth_token)

  message = client.messages.create(to="+13479860720", from_="+16172022165", body="Hello Gen!")
  print('This job is run every two minutes.')

def send_email():
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("ohta.g@husky.neu.edu")
  subject = "Weekly update"
  # to_email = Email("j.kimani@northeastern.edu")
  to_email = Email("ohta.g@husky.neu.edu")
  content = Content("text/plain", "Hello, Email!")
  mail = Mail(from_email, subject, to_email, content)
  response = sg.client.mail.send.post(request_body=mail.get())

try:
  sched = BackgroundScheduler()
  print("created background scheduler")
  sched.add_job(send_email, 'cron', day_of_week=6, hour=18, minute=50)
  print("added cron job")
  sched.start()
  print("started background scheduler")
except Exception as e:
  print e.message

