from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *
from os import environ


db = Database()
# db.bind('postgres', user=environ.get('POSTGRES_USER'), password=environ.get('POSTGRES_PASSWORD'), host='postgres', database='postgres')
db.bind('postgres', user='postgres', password='postgres', host='localhost', database='postgres')


from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    roles = Set('Role')
    groups = Set('Group')
    full_name = Optional(str)
    username = Optional(str)
    password = Optional(str)


class Role(db.Entity):
    id = PrimaryKey(int, auto=True)
    users = Set(User)
    role_name = Optional(str)


class Group(db.Entity):
    id = PrimaryKey(int, auto=True)
    users = Set(User)
    group_name = Optional(str)


class ShipmentRequest(db.Entity):
    id = PrimaryKey(int, auto=True)
    items = Set('ShipmentItem')
    request_date = Optional(datetime)
    shipping_information = Required('ShippingInformation')
    shipping_date = Optional(datetime)
    RFID_TAG_ID = Optional(str)
    bay_area = Required('DispatchBayArea')


class ShipmentItem(db.Entity):
    id = PrimaryKey(int, auto=True)
    shipment_request = Required(ShipmentRequest)
    item_name = Optional(str)
    item_serial_no = Optional(str)
    item_type = Optional(str)
    item_category = Optional(str)


class ShippingInformation(db.Entity):
    id = PrimaryKey(int, auto=True)
    shipping_source = Optional(str)
    shipping_destination = Optional(str)
    shipping_request = Optional(ShipmentRequest)
    source_type = Optional(str)
    destination_type = Optional(str)


class DispatchBayArea(db.Entity):
    id = PrimaryKey(int, auto=True)
    bay_area_name = Optional(str)
    bay_area_code = Optional(str)
    bay_area_desc = Optional(str)
    shipment_request = Optional(ShipmentRequest)
    RFID_READER_ID = Optional(str)
    bay_lat = Optional(Decimal)
    bay_lon = Optional(str)


class DeviceMaster(db.Entity):
    id = PrimaryKey(int, auto=True)
    device_type = Optional(str)
    device_id = Optional(str)
    device_location = Optional(str)
    device_name = Optional(str)
    device_description = Optional(str)
    vehicle_master = Optional('VehicleMaster')


class VehicleMaster(db.Entity):
    id = PrimaryKey(int, auto=True)
    vehicle_type = Optional(str)
    vechile_make = Optional(str)
    GPS_ID = Optional(str)
    RFID_ID = Optional(str)
    device_master = Required(DeviceMaster)
    asset_management = Optional('TransportRequest')


class AssetTrackingLog(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    timestamp = Optional(datetime, default=lambda: datetime.now())
    payload = Optional(Json)
    parent_payload = Optional(UUID)


class TransportRequest(db.Entity):
    id = PrimaryKey(int, auto=True)
    customer_shipment_request_id = Optional(str)
    assigned_vehicle = Required(VehicleMaster)
    pickup_location = Optional(str)
    pickup_lat = Optional(Decimal)
    pickup_lon = Optional(Decimal)
    drop_lat = Optional(Decimal)
    drop_lon = Optional(Decimal)
    drop_location = Optional(str)


class Warehouse(db.Entity):
    id = PrimaryKey(int, auto=True)
    warehouse_name = Optional(str)
    warehouse_location = Optional(str)
    warehouse_lat = Optional(Decimal)
    warehouse_lon = Optional(Decimal)
    RFID_READER_ID = Optional(str)
    storages = Set('Storage')


class Storage(db.Entity):
    id = PrimaryKey(int, auto=True)
    pallet_no = Optional(int)
    pallet_section = Optional(int)
    pallet_row = Optional(int)
    RFID_ID = Optional(str)
    warehouse = Required(Warehouse)



db.generate_mapping()


@db_session()
def test_microservice1():
    print(db.execute("select now();").fetchone())
    return db.execute("select now();").fetchone()




@db_session
def users_exists(username, password):
    pass

@db_session
def auth_user(username, password):
    #    res = select(raw_sql('password = crypt($password, password) and email_verified = TRUE') for p in IdentityManagement if p.username == username and p.app_name == app_name )[:]
    pass

@db_session
def auth_register(username, password):
            # cursor = db.execute('''insert into identitymanagement (id,username, password,email,app_name) 
            # values($uuid, $username, crypt($password, gen_salt('bf')),$email,$app_name);''')        
    pass

def send_registration_event(username, password):
    pass    


@db_session
def reset_password(username, new_password, email, app_name,token):
 
        # cursor = db.execute('''update identitymanagement 
        #                        set password = crypt($new_password, gen_salt('bf')),
        #                        email_verified = TRUE,
        #                        email_verification_token = NULL,
        #                        email_digit_token = NULL
        #                        where email = $email and app_name = $app_name''')
    pass



    # if __name__ == '__main__':
    #     print('')