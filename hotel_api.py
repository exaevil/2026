import requests
import time

# رابط تجريبي آخر (أكثر استقراراً)
url = "https://jsonplaceholder.typicode.com/posts/1"

# "خدعة" الـ Headers: نجعل السيرفر يظن أن الطلب قادم من متصفح كروم
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("جاري محاولة الاتصال...")

try:
    # أضفنا الـ headers والـ timeout لزيادة الاستقرار
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    print("نجح الاتصال! إليك البيانات:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"حدث خطأ أثناء الاتصال: {e}")