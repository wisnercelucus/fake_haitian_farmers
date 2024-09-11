import random
from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta

#from faker import Faker
#from mimesis import Person
#from mimesis import Address
#from mimesis.enums import Gender
#from mimesis import Datetime


#person = Person('en')
#person = Person()
#addess = Address()
#datetime = Datetime()

def years_between(date1: datetime, date2: datetime) -> int:
    # Ensure date1 is the earlier date
    if date1 > date2:
        date1, date2 = date2, date1
    
    # Calculate the difference
    delta = relativedelta(date2, date1)
    
    return delta.years


def random_date_between(start_date: datetime, end_date: datetime) -> datetime:
    # Calculate the difference in days between the start and end dates
    delta_days = (end_date - start_date).days
    
    # Generate a random number of days within this range
    random_days = random.randint(0, delta_days)
    
    # Create a random date by adding the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)
    
    return random_date


def random_date(start_date, end_date) -> datetime:
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    random_timestamp = random.randint(start_timestamp, end_timestamp)
    random_date = datetime.fromtimestamp(random_timestamp)
    return random_date

def random_int(min_val, max_val) -> int:
    random_int = random.randint(min_val, max_val)
    return random_int

def random_float(min_val, max_val) -> float:
    return random.uniform(min_val, max_val)

def random_item(my_list) -> str:
    random_item = random.choice(my_list)
    return random_item


def create_email(first_name: str, last_name: str, domain: str = 'example.com') -> str:
    first_name = first_name.strip()
    last_name = last_name.strip()
    email_prefix = first_name[0].lower() + last_name.lower()
    email_address = f"{email_prefix}@{domain}"
    return email_address

#def create_rows_mimesis(num=1):
#    output = [{"name":person.full_name(gender=Gender.FEMALE),
#                   "address":addess.address(),
#                   "name":person.name(),
#                   "email":person.email(),
#                   #"bs":person.bs(),
#                   "city":addess.city(),
#                   "state":addess.state(),
#                   "date_time":datetime.datetime(),
#                   #"paragraph":person.paragraph(),
#                   #"Conrad":person.catch_phrase(),
#                   "randomdata":random.randint(1000,2000)} for x in range(num)]
#    return output

#%%time
#df_mimesis = pd.DataFrame(create_rows_mimesis(5000))




if __name__=='__main__':
# Example usage:
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    print("======= random date ======")
    print(random_date(start_date, end_date))
    print("\n")
    print("======= A random Int======")
    min_val = 10
    max_val = 100
    print(random_int(min_val, max_val))
    
    print("\n")
    print("======= A random Item from list======")
    my_list = ['apple', 'banana', 'cherry', 'date']
    print(random_item(my_list))
    print("\n")
    print("======= A random Float======")

    # Generate a random float between min_val and max_val
    min_val = 1.5
    max_val = 10.5
    print(random_float(min_val, max_val))