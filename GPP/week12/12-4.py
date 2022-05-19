user_info = {'id': 'software', 'pw': 'python'}

id = input()
password = input()

if id != user_info['id']:
    print('ID Mismatch!')
if password != user_info['pw']:
    print('PW Mismatch!')
if id == user_info['id'] and password == user_info['pw']:
    print('Success in Login')
