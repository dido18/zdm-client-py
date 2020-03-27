"""
jobs.py

Show a simple example of how to define a custom job and pass it to the ZdmClient.

"""
import json
import time

from zdm import ZDMClient

device_id = '!!! PUT YOU DEVICE_ID HERE !!!'
password = '!!! PUT YOU PASSWORD HERE !!!'


def set_temp(client, args):
    print("Setting temperature. Received args: {}".format(args))
    #  DO SOMETHING

    # return the result of the job
    return json.dumps({"msg": "Temperature set correctly."})


# define the list of custom Jobs offered by the device
my_jobs = {
    "set_temp": set_temp,
}

device = ZDMClient(device_id=device_id, jobs=my_jobs)
device.set_password(password)
device.connect()

while True:
    time.sleep(1)
