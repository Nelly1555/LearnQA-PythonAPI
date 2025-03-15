import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirects_count = len(response.history)
final_url = response.url

print(f"Количество редиректов: {redirects_count}")
print(f"Итоговый URL: {final_url}")
