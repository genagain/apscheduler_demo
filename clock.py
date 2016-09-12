from apscheduler.schedulers.blocking import BlockingScheduler
import sendgrid
import os
from sendgrid.helpers.mail import *

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='tue', hour=0)
def scheduled_job():
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  print("created send grid api client")
  from_email = Email("ohta.g@husky.neu.edu")
  print("created from email")
  subject = "Weekly update"
  # to_email = Email("j.kimani@northeastern.edu")
  to_email = Email("ohta.g@husky.neu.edu")
  print("created to email")
  content = Content("text/plain", "Hello, Email!")
  print("created content")
  mail = Mail(from_email, subject, to_email, content)
  print("created mail")
  response = sg.client.mail.send.post(request_body=mail.get())

sched.start()
