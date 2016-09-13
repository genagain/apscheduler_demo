from apscheduler.schedulers.blocking import BlockingScheduler
import sendgrid
import os
from sendgrid.helpers.mail import *

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='tue', hour=9, minute=10)
def scheduled_job():
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  print("created send grid api client")
  from_email = Email("ohta.g@husky.neu.edu")
  print("created from email")
  subject = "Weekly update"
  # to_email = Email("j.kimani@northeastern.edu")
  to_email = Email("ohta.g@husky.neu.edu")
  print("created to email")
  email_content = """
  <html>
  Hi Professor Kimani,

  Here is a link to the GoogleDoc about our capstone progress.

  <a href="https://docs.google.com/document/d/1FR2Vqhe9YctfCxOrWRoOO2HKIJjEpJp-CmSBV190vwE/edit?usp=sharing"> Weekly Progress </a>

  Best,
  Gen
  </html>
  """
  content = Content("text/plain", email_content)
  print("created content")
  mail = Mail(from_email, subject, to_email, content)
  print("created mail")
  response = sg.client.mail.send.post(request_body=mail.get())

sched.start()
