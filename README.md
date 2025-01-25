### Intelligent Vulnerability Scanner - مُسح الثغرات الذكي

# UltraZero - Ultimate Security Scanner

UltraZero is a powerful and versatile security scanning tool designed to help
security professionals and enthusiasts identify vulnerabilities in their systems.
With features like port scanning, subdomain enumeration, vulnerability scanning,
and deep crawling, UltraZero provides a comprehensive approach to security assessment.

## Features

- **Fast Port Scanning**: Quickly scan common ports to identify open services.
- **Subdomain Enumeration**: Discover subdomains associated with the target domain.
- **Vulnerability Scanning**: Detect common vulnerabilities such as SQL Injection and XSS.
- **Deep Crawling**: Crawl the target website to discover hidden pages and endpoints.
- **Multi-threading**: Utilize multiple threads for faster scanning.
- **Stealth Mode**: Enable stealth mode to reduce the likelihood of detection.
- **Multi-language Support**: Available in both English and Arabic.

## Installation

To install UltraZero, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/munx64/UltraZero.git
   cd UltraZero
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python3 UltraZero.py -t <target> [options]
   ```

## Usage

### Basic Usage

To start a basic scan on a target, use the following command:

```bash
python3 UltraZero.py -t example.com
```

### Advanced Options

- **Output Results to a File**:
  ```bash
  python3 UltraZero.py -t example.com -o output.json
  ```

- **Set Number of Threads**:
  ```bash
  python3 UltraZero.py -t example.com --threads 100
  ```

- **Enable Stealth Mode**:
  ```bash
  python3 UltraZero.py -t example.com --stealth
  ```

- **Change Language**:
  ```bash
  python3 UltraZero.py -t example.com --lang ar
  ```

### Example Commands

1. **Scan a target with 200 threads and output results to a file**:
   ```bash
   python3 UltraZero.py -t example.com --threads 200 -o results.json
   ```

2. **Scan a target in stealth mode with Arabic language support**:
   ```bash
   python3 UltraZero.py -t example.com --stealth --lang ar
   ```

## Contributing

We welcome contributions from the community! If you'd like to contribute to UltraZero, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** and push them to your fork.
4. **Submit a pull request** detailing your changes.

## License

UltraZero is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This tool is intended for educational and ethical testing purposes only. The authors are not responsible for any misuse or damage caused by this tool. Always ensure you have permission before scanning any system.

## Support

For support, questions, or feature requests, please open an issue on the [GitHub repository](https://github.com/munx64/UltraZero/issues).

If you find this tool useful and would like to support its development, you can donate Bitcoin to the following address:

**Bitcoin**: `BC1QJ3HDSK2TFKGHZLT7N9PXRV9AACKFYDHYY0TVFX5R3EJZTS7EZT3SZ8Q284`

---

**UltraZero** - Your ultimate tool for security scanning. Stay safe, stay secure!
```
```
---

# أداة الفحص الأمني المتطورة - UltraZero 

 هي أداة قوية ومتعددة الاستخدامات مصممة لمساعدة المحترفين والمهتمين بالأمن في اكتشاف الثغرات الأمنية في أنظمتهم. مع ميزات مثل فحص المنافذ، تعداد النطاقات الفرعية، فحص الثغرات الأمنية، والزحف العميق، توفر UltraZero نهجًا شاملاً لتقييم الأمان.

## الميزات

- **فحص المنافذ السريع**: فحص سريع للمنافذ الشائعة لتحديد الخدمات المفتوحة.
- **تعداد النطاقات الفرعية**: اكتشاف النطاقات الفرعية المرتبطة بالنطاق المستهدف.
- **فحص الثغرات الأمنية**: اكتشاف الثغرات الشائعة مثل حقن SQL وثغرات XSS.
- **الزحف العميق**: زحف الموقع المستهدف لاكتشاف الصفحات والنقاط المخفية.
- **تعدد المهام**: استخدام خيوط متعددة لإجراء الفحص بشكل أسرع.
- **وضع التخفي**: تفعيل وضع التخفي لتقليل احتمالية الاكتشاف.
- **دعم متعدد اللغات**: متاح باللغتين الإنجليزية والعربية.

## التثبيت

لتركيب UltraZero، اتبع الخطوات التالية:

**نسخ المستودع**:
   ```bash
   git clone https://github.com/munx64/UltraZero.git
   cd UltraZero
   ```

**تثبيت التبعيات**:
   ```bash
   pip install -r requirements.txt
   ```

**تشغيل الأداة**:
   ```bash
   python3 UltraZero.py -t <الهدف> [خيارات]
   ```

## طريقة الاستخدام

### الاستخدام الأساسي

لبدء فحص أساسي على هدف معين، استخدم الأمر التالي:

```bash
python3 UltraZero.py -t example.com
```

### الخيارات المتقدمة

**حفظ النتائج في ملف**
  ```bash
  python3 UltraZero.py -t example.com -o output.json
  ```

**تحديد عدد الخيوط**
  ```bash
  python3 UltraZero.py -t example.com --threads 100
  ```

**تفعيل وضع التخفي**
  ```bas
  python3 UltraZero.py -t example.com --stealth
  ```

**تغيير اللغة**
  ```bash
  python3 UltraZero.py -t example.com --lang ar
  ```

### أمثلة على الأوامر

**فحص هدف مع 200 خيط وحفظ النتائج في ملف**:
   ```bash
   python3 UltraZero.py -t example.com --threads 200 -o results.json
   ```

**فحص هدف في وضع التخفي مع دعم اللغة العربية**:
   ```bash
   python3 UltraZero.py -t example.com --stealth --lang ar
   ```

## المساهمة

نرحب بالمساهمات من المجتمع! إذا كنت ترغب في المساهمة في تطوير UltraZero، يرجى اتباع الخطوات التالية:

**قم بعمل fork للمستودع**.
**أنشئ فرعًا جديدًا** لميزتك أو إصلاح الخلل.
**قم بإجراء التغييرات** وادفعها إلى نسختك.
**قدم طلب سحب** يوضح التغييرات التي أجريتها.

## الترخيص

مرخصة تحت رخصة MIT. يمكنك الاطلاع على تفاصيل الرخصة في ملف UltraZero [LICENSE](LICENSE).

## إخلاء المسؤولية

هذه الأداة مخصصة لأغراض تعليمية واختبارية أخلاقية فقط. المؤلفون غير مسؤولين عن أي سوء استخدام أو ضرر ناتج عن هذه الأداة. تأكد دائمًا من الحصول على إذن قبل فحص أي نظام.

## الدعم

للحصول على الدعم أو طرح الأسئلة أو طلب ميزات جديدة، يرجى فتح طلب في [مستودع GitHub](https://github.com/munx64/UltraZero/issues).

إذا وجدت هذه الأداة مفيدة وترغب في دعم تطويرها، يمكنك التبرع بالبتكوين إلى العنوان التالي:

**البتكوين**: `BC1QJ3HDSK2TFKGHZLT7N9PXRV9AACKFYDHYY0TVFX5R3EJZTS7EZT3SZ8Q284`
