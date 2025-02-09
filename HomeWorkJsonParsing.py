from json.decoder import JSONDecodeError
import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

messages = obj['messages']

second_message = messages[1]

try:
    second_message_text = second_message['message']
    print(second_message_text)
except JSONDecodeError:
    print("Response is not in JSON format")

