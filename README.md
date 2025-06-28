# أداة استخراج معلومات مستخدمي Snapchat

## نظرة عامة
هذه الأداة مصممة للاتصال بسيرفر Snapchat واستخراج معلومات المستخدم مثل البريد الإلكتروني، عنوان IP، الموقع الجغرافي وغيرها من المعلومات. الأداة تعمل من خلال واجهة سطر أوامر بسيطة وفعالة.

**ملاحظة مهمة**: هذه الأداة مخصصة للأغراض التعليمية فقط. استخدامها للوصول غير المصرح به إلى حسابات الآخرين يعد انتهاكًا لشروط خدمة Snapchat وقد يكون غير قانوني.

## المطور
- **المطور**: Saudi Linux
- **البريد الإلكتروني**: SaudiLinux7@gmail.com

## المتطلبات
- Python 3.6 أو أحدث
- المكتبات المذكورة في ملف `requirements.txt`

## هيكل المشروع
- `snapchat_tool.py`: الملف الرئيسي للأداة
- `advanced_features.py`: وحدة تحتوي على الميزات المتقدمة
- `utils.py`: وحدة تحتوي على وظائف مساعدة
- `requirements.txt`: قائمة بالمكتبات المطلوبة
- `run_tool.bat`: سكريبت لتشغيل الأداة على نظام ويندوز
- `run_tool.sh`: سكريبت لتشغيل الأداة على نظام لينكس
- `LICENSE`: ملف الترخيص
- `README.md`: ملف التوثيق

## التثبيت

### 1. تثبيت Python
تأكد من تثبيت Python 3.6 أو أحدث على جهازك. يمكنك تنزيله من [الموقع الرسمي لـ Python](https://www.python.org/downloads/).

### 2. تنزيل المشروع
قم بتنزيل المشروع أو استنساخه:

```bash
git clone https://github.com/SaudiLinux/snapchat-tool.git
cd snapchat-tool
```

### 3. تثبيت المتطلبات
قم بتثبيت المكتبات المطلوبة باستخدام pip:

```bash
pip install -r requirements.txt
```

## الاستخدام

### الخيارات المتاحة
```
python snapchat_tool.py [-h] [-u USERNAME] [-t TARGET] [-a] [-s] [-c] [-f] [-r] [-v]
```

### الوسائط
- `-h, --help`: عرض رسالة المساعدة
- `-u USERNAME, --username USERNAME`: اسم المستخدم الخاص بك على Snapchat
- `-t TARGET, --target TARGET`: اسم المستخدم المستهدف على Snapchat
- `-a, --advanced`: تفعيل الميزات المتقدمة (معلومات IP، معلومات الأمان، نشاط الحساب)
- `-s, --save`: حفظ النتائج في ملف JSON
- `-c, --check`: عرض معلومات النظام قبل البدء
- `-f, --friend`: إرسال طلب إضافة للمستخدم المستهدف
- `-r, --request-status`: التحقق من حالة طلب الإضافة (إذا تم قبوله، سيتم عرض البريد الإلكتروني وكلمة المرور)
- `-v, --version`: عرض إصدار الأداة

### أمثلة على الاستخدام

#### استخدام تفاعلي
```bash
python snapchat_tool.py
```

#### تحديد اسم المستخدم الخاص بك
```bash
python snapchat_tool.py -u your_username
```

#### تحديد اسم المستخدم الخاص بك والمستخدم المستهدف
```bash
python snapchat_tool.py -u your_username -t target_username
```

#### استخدام الميزات المتقدمة
```bash
python snapchat_tool.py -u your_username -t target_username -a
```

#### حفظ النتائج في ملف
```bash
python snapchat_tool.py -u your_username -t target_username -s
```

#### استخدام جميع الميزات
```bash
python snapchat_tool.py -u your_username -t target_username -a -s -c
```

#### إرسال طلب إضافة للمستخدم المستهدف
```bash
python snapchat_tool.py -u your_username -t target_username -f
```

#### التحقق من حالة طلب الإضافة
```bash
python snapchat_tool.py -u your_username -t target_username -r
```

#### إرسال طلب إضافة وحفظ المعلومات المستخرجة
```bash
python snapchat_tool.py -u your_username -t target_username -f -s
```

## إخلاء المسؤولية
هذه الأداة مخصصة للأغراض التعليمية والبحثية فقط. المطور غير مسؤول عن أي استخدام غير قانوني أو غير أخلاقي لهذه الأداة. استخدام هذه الأداة للوصول غير المصرح به إلى حسابات الآخرين يعد انتهاكًا لشروط خدمة Snapchat وقد يكون غير قانوني في العديد من البلدان.

## الترخيص
هذا المشروع مرخص بموجب رخصة MIT. راجع ملف `LICENSE` للحصول على مزيد من المعلومات.