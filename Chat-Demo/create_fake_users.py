
from faker import Faker


def generate_user_data():
    fake = Faker()
    user_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }

    # save user date to csv file 
    with open('user_data.csv', 'a') as f:
        f.write(f"{user_data['first_name']},{user_data['last_name']},{user_data['email']},{user_data['password']}\n")

i = 0 
while i < 1000:
    generate_user_data()
    i += 1