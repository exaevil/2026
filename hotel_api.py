import requests

# رابط API عام ومجاني
url = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=El-Alamein"

# ملاحظة: استبدل YOUR_API_KEY بمفتاح مجاني من موقع weatherapi.com
# للتدريب فقط، يمكنك تجربة هذا الرابط بدلاً منه:
url_test = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url_test)

if response.status_code == 200:
    print("اتصال ناجح! إليك البيانات:")
    print(response.json())
else:
    print("فشل الاتصال، حاول مجدداً.")