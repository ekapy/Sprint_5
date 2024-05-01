import faker

def get_sign_up_data():
    fake = faker.Faker()
    email_data = fake.email()
    password_data = fake.password()
    return email_data, password_data