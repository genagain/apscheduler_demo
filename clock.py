from apscheduler.schedulers.blocking import BlockingScheduler
import sendgrid
import os
from sendgrid.helpers.mail import *

def send_email():
  try:
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
  except Exception as e:
    return e

try:
  sched = BlockingScheduler()
  print("created background scheduler")
  sched.start()
  print("started background scheduler")
  sched.add_job(send_email, 'cron', day_of_week=6, hour=22, minute=20)
  print("added cron job")
except Exception as e:
  print e.message

