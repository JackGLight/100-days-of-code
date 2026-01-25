import datetime as dt
import random
import smtplib


info = []
with open("birthdays.csv") as file:
    for line in file:
        info.append(line)


contacts = [item.split(",") for item in info]

new_list = []
for contact in contacts:
    clean_item = [x.strip() for x in contact]
    new_list.append(clean_item)


birthdays_dict = {}
for row in new_list[1:]:
    name, email, year, month, day = row

    key = (int(month), int(day))
    birthdays_dict[key] = {
        "name": name,
        "email": email,
        "year": year,
        "month": int(month),
        "day": int(day),
    }


now = dt.datetime.now()
today = (now.month, now.day)

if today in birthdays_dict:
    person = birthdays_dict[today]
    birthday_name = person["name"]
    birthday_email = person["email"]

    template_num = random.randint(1, 3)
    template_path = f"letter_templates/letter_{template_num}.txt"

    with open(template_path) as letter_file:
        letter_text = letter_file.read()

    personalized_letter = letter_text.replace("[NAME]", birthday_name)

    print("Birthday match found!")
    print("Sending to:", birthday_email)


    MY_EMAIL = "username"
    MY_PASSWORD = "password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )

else:
    print("No birthdays today.")