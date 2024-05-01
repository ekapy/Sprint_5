import faker


def get_sign_up_data():
    fake = faker.Faker()
    email_data = fake.email()
    password_data = fake.password()
    return email_data, password_data

def get_sign_in_data():
    email = 'testkate@mailinator.com'
    password = '123456'
    return email, password

def get_active_state_button():
    active_button = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    return active_button

