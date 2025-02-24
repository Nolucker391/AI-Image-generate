import requests
import json

# URL API
url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# Данные запроса
payload = {
    "prompt": "Monkey on a beautiful sunset background",
    "negative_prompt": "",
    "steps": 20,
    "sampler_name": "Euler a",
    "width": 512,
    "height": 512,
    "cfg_scale": 7.5,
    "seed": -1,
    "n_iter": 1
}

# Отправка POST-запроса
response = requests.post(url, json=payload)

# Проверяем, есть ли ответ
if response.status_code == 200:
    data = response.json()
    # Сохраняем изображение
    with open("output.png", "wb") as f:
        f.write(bytes.fromhex(data["images"][0]))
    print("✅ Изображение сохранено как output.png")
else:
    print("❌ Ошибка:", response.text)
