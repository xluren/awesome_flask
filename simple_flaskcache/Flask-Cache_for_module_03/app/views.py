import random,time

def get_number():
    s=random.randint(0,100)
    return str(s)

def get_datetime():
    return time.ctime()

def main_index():
    return """<lu>
            <li>the datetime is {datetime}</li>
            <li>the number is {random_number}</li>
            </lu>""".format(
                datetime=get_datetime(),
                random_number=get_number()
            )
