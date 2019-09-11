import model
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *
from os import environ

@db_session
def register_device(device_type, device_id,  device_location,  device_name,  device_description, vehicle_master ):
    model.DeviceMaster(device_type, device_id,  device_location,  device_name,  device_description, vehicle_master    )

def device_exists(device_id):
    pass