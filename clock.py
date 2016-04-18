from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import TwilioRestClient

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
  
  account_sid = "AC6e652d5e6bea5c4e494f9c7cb06be1a2"
  auth_token = "0d05da068ddc52eb021c930c27995ef0"
  client = TwilioRestClient(account_sid, auth_token)

  message = client.messages.create(to="+13479860720", from_="+16172022165", body="Hello Gen!")
  print('This job is run every three minutes.')

sched.start()
