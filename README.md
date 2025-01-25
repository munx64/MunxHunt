### Intelligent Vulnerability Scanner - مُسح الثغرات الذكي 
```markdown
# UltraZero - Ultimate Security Scanner

UltraZero is a powerful and versatile security scanning tool designed to help security professionals and enthusiasts identify vulnerabilities in their systems. With features like port scanning, subdomain enumeration, vulnerability scanning, and deep crawling, UltraZero provides a comprehensive approach to security assessment.

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

**Bitcoin Address**: `BC1QJ3HDSK2TFKGHZLT7N9PXRV9AACKFYDHYY0TVFX5R3EJZTS7EZT3SZ8Q284`

---

**UltraZero** - Your ultimate tool for security scanning. Stay safe, stay secure!
```

This update includes the Bitcoin address in the **Support** section, allowing users to contribute financially to the project if they wish.
