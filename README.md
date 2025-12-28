# Variance Calculator - Python

مشروع بايثون بسيط لحساب **التباين (variance)** لقائمة من الأرقام.

## الوصف
الكود يأخذ قائمة من الأرقام، يحسب المتوسط، ثم يحسب التباين باستخدام الصيغة:
variance = sum((x - mean)^2) / n

makefile
Copy code

## الكود
```python
data = [1, 2, 3]

mdata = sum(data) / len(data)

sdata = [(x - mdata) for x in data]
edata = [x**2 for x in sdata]

ndata = sum(edata) / len(data)

print(ndata)
طريقة الاستخدام
افتح الملف test.py.

عدّل قائمة data بالأرقام اللي عايز تحسب لها التباين.

شغّل الكود باستخدام بايثون:

bash
Copy code
python test.py
المتطلبات
بايثون 3.x

المؤلف
عبد الرحمن ياسر

markdown
Copy code
