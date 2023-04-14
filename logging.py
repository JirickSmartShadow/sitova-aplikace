import datetime


def log(client, message, success):
    if success:
        success = 'success'
    else:
        success = 'error'
    with open('log/log.txt', 'a', encoding='utf-8') as f:
        f.write('{}:{} at {} - {} status: {}\n'
                .format(client[0], client[1], datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), message, success))
