import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"    1. Статус код: {response.status_code}, Текст: {response.text}")


response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"HEAD"})
print(f"    2. Статус код: {response.status_code}, Текст: {response.text}")

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(f"    3.1. Статус код: {response.status_code}, Текст: {response.text}")

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print(f"    3.2. Статус код: {response.status_code}, Текст: {response.text}")

print(f"\n    4")

methods = ["GET", "POST", "PUT", "DELETE"]

for http_method in methods:
    for param_method in methods:
        print(f"\n  HTTP Method: {http_method}, Parameter method: {param_method}")

        if http_method == "GET":
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": param_method})
        elif http_method == "POST":
            response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": param_method})
        elif http_method == "PUT":
            response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": param_method})
        elif http_method == "DELETE":
            response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": param_method})

        print(f"    Статус код: {response.status_code}, Текст: {response.text}")

        if response.status_code == 200 and response.text == "Wrong method provided":
            print("    ==> Тип запроса не совпадает со значением параметра (200 OK)")

        if http_method == param_method and response.status_code != 200:
            print("    ==> Типы запроса и параметра совпадают (не 200 OK)")

        if response.status_code == 200 and response.text == "{\"success\":\"!\"}":
                print("    ==> Типы запроса и параметра совпадают (200 OK)")