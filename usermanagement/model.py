from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *
from os import environ


db = Database()
db.bind('postgres', user=environ.get('POSTGRES_USER'), password=environ.get('POSTGRES_PASSWORD'), host='postgres', database='postgres')


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