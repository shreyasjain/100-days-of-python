##################### Extra Hard Starting Project ######################
import smtplib
from datetime import datetime
import random
import pandas

# 1. Update the birthdays.csv
# file = pandas.read_csv('birthdays.csv')
# new_rows = pandas.DataFrame(
#     [{"name": "Shreyas", "email": "shreyasjain4all@gmail.com", "year": 1998, "month": 9, "day": 19}])
# new_data = pandas.concat([file, new_rows], ignore_index=True)
# new_data.to_csv('birthdays.csv', index=False)

file = pandas.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
day = datetime.today().day
month = datetime.today().month
search_results = file[(file['day'] == day) & (file['month'] == month)]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def send_mails(row):
    print(row)


if len(search_results) > 0:
    for row in search_results.itertuples(index=False):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            file_name = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            content = ""
            with open(file_name, 'r') as file:
                content = f"Subject:Happy Birthday\n\n{file.read().replace('[NAME]', row.name)}"
            connection.login('13sjain4ur7@gmail.com', 'kdja tdlq xzkv dsvi')
            connection.sendmail('13sjain4ur7@gmail.com', 'shreyasjain4all@gmail.com', content)

# 4. Send the letter generated in step 3 to that person's email address.
