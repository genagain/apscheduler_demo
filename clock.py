from apscheduler.schedulers.background import BackgroundScheduler
import sendgrid
import os
from sendgrid.helpers.mail import *

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
  sched.add_job(send_email, 'cron', day_of_week=6, hour=19, minute=30)
  print("added cron job")
  sched.start()
  print("started background scheduler")
except Exception as e:
  print e.message

