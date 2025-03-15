import requests
import time

response_new_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

response_data1 = response_new_task.json()
seconds = response_data1.get('seconds')
token = response_data1.get('token')
print(f"\nseconds: {seconds}")
print(f"token: {token}")

print("\nОжидание статуса 'Job is NOT ready'...")
payload = {"token": token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)

if response2.status_code == 200:
    response_data2 = response2.json()
    status_before = response_data2.get('status')

    if status_before == "Job is NOT ready":
            print("Статус 'Job is NOT ready' получен")
    else:
            print(f"ОШИБКА: Ожидался статус 'Job is NOT ready', получен: {status_before}")
else:
    print(f"ОШИБКА: Запрос статуса ДО не удался, код состояния: {response2.status_code}")

print(f"\nОжидание {seconds} секунд...")
time.sleep(seconds)

print("\nОжидание статуса 'Job is ready' и результата...")
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)

if response3.status_code == 200:
    response_data4 = response3.json()
    status_after = response_data4.get('status')
    result_value = response_data4.get('result')

    if status_after == "Job is ready":
        print("Статус 'Job is ready' получен")

        if result_value is not None:  # Проверяем, что результат есть
            print(f"Результат: {result_value}")
        else:
            print("ОШИБКА: Ожидался результат, но он отсутствует.")

    else:
        print(f"ОШИБКА: Ожидался статус 'Job is ready', получен: {status_after}")

else:
    print(f"ОШИБКА: Запрос статуса ПОСЛЕ не удался, код состояния: {response3.status_code}")


