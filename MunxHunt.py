#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import socket
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import dns.resolver
import ssl
import time
import re
import json

# ========== التهيئة والألوان ==========
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

BANNER = f"""{Colors.RED}
███╗   ███╗██╗   ██╗███╗   ██╗██╗  ██╗{Colors.CYAN}██╗  ██╗██╗   ██╗███╗   ██╗████████╗
████╗ ████║██║   ██║████╗  ██║╚██╗██╔╝{Colors.CYAN}██║ ██╔╝██║   ██║████╗  ██║╚══██╔══╝
██╔████╔██║██║   ██║██╔██╗ ██║ ╚███╔╝ {Colors.CYAN}█████╔╝ ██║   ██║██╔██╗ ██║   ██║   
██║╚██╔╝██║██║   ██║██║╚██╗██║ ██╔██╗ {Colors.CYAN}██╔═██╗ ██║   ██║██║╚██╗██║   ██║   
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██╔╝ ██╗{Colors.CYAN}██║  ██╗╚██████╔╝██║ ╚████║   ██║   
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝{Colors.CYAN}╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
{Colors.END}
{Colors.YELLOW}{Colors.BOLD}                    [ أداة مونكس هنت للأمن السيبراني ]{Colors.END}
{Colors.CYAN}             إصدار 2.0 | مطور بواسطة {Colors.BOLD}Munx64{Colors.END}
{Colors.BLUE}         روابط التحميل: {Colors.UNDERLINE}https://github.com/munx64/MunxHunt{Colors.END}
"""

# ===================================================
class MunxHunt:
    def __init__(self, args):
        self.target = args.target
        self.output = args.output
        self.threads = args.threads
        self.stealth = args.stealth
        self.vuln_scan = args.vuln_scan
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'MunxHunt/2.0'})
        self.found = {
            'subdomains': [],
            'open_ports': [],
            'vulnerabilities': []
        }

    def log(self, message, level="info"):
        """نظام تسجيل الأحداث مع التنسيق الملون"""
        color = {
            "info": Colors.BLUE,
            "success": Colors.GREEN,
            "warning": Colors.YELLOW,
            "error": Colors.RED,
            "critical": Colors.MAGENTA
        }.get(level, Colors.BLUE)
        
        msg = f"{color}[{level.upper()}] {message}{Colors.END}"
        print(msg)
        
        if self.output:
            with open(self.output, 'a', encoding='utf-8') as f:
                f.write(f"[{level.upper()}] {message}\n")

    def subdomain_storm(self):
        """تعداد النطاقات الفرعية باستخدام DNS Brute-force"""
        self.log("بدء عملية تعداد النطاقات الفرعية...", "info")
        try:
            with open('subdomains.txt', 'r') as f:
                subdomains = f.read().splitlines()
            
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                futures = [executor.submit(self.resolve_subdomain, sub) for sub in subdomains]
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        self.found['subdomains'].append(result)
                        self.log(f"تم اكتشاف النطاق: {result}", "success")
        except Exception as e:
            self.log(f"خطأ في تعداد النطاقات: {str(e)}", "error")

    def resolve_subdomain(self, subdomain):
        """حل النطاقات الفرعية باستخدام DNS"""
        full_domain = f"{subdomain}.{self.target}"
        try:
            answers = dns.resolver.resolve(full_domain, 'A')
            if answers:
                return full_domain
        except:
            return None

    def port_lightning(self):
        """فحص المنافذ فائق السرعة"""
        self.log("بدء فحص المنافذ السريع...", "info")
        common_ports = [21, 22, 80, 443, 8080, 8443, 3306, 3389]
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.check_port, port): port for port in common_ports}
            for future in as_completed(futures):
                port = futures[future]
                try:
                    if future.result():
                        self.found['open_ports'].append(port)
                        self.log(f"المنفذ {port} مفتوح", "success")
                except:
                    pass

    def check_port(self, port):
        """فحص منفذ واحد مع إدارة الوقت"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.target, port))
            sock.close()
            return result == 0
        except:
            return False

    def vulnerability_scan(self):
        """فحص الثغرات الأمنية المتقدم"""
        if not self.vuln_scan:
            return
            
        self.log("بدء الفحص الأمني المتقدم...", "critical")
        urls = self.crawl_site()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for url in urls:
                futures.append(executor.submit(self.check_sqli, url))
                futures.append(executor.submit(self.check_xss, url))
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    self.found['vulnerabilities'].append(result)
                    self.log(result, "warning")

    def crawl_site(self):
        """زحف الموقع لاكتشاف الصفحات"""
        self.log("جاري زحف الموقع...", "info")
        try:
            response = self.session.get(f"http://{self.target}")
            soup = BeautifulSoup(response.text, 'html.parser')
            urls = set()
            
            for link in soup.find_all('a', href=True):
                url = urljoin(response.url, link['href'])
                if self.target in url:
                    urls.add(url)
            
            return list(urls)
        except Exception as e:
            self.log(f"فشل الزحف: {str(e)}", "error")
            return []

    def check_sqli(self, url):
        """كشف ثغرات SQL Injection"""
        payloads = ["'", "\"", "' OR 1=1--", "') OR 1=1--"]
        for payload in payloads:
            try:
                response = self.session.get(f"{url}?id={payload}", timeout=3)
                if 'error' in response.text.lower():
                    return f"ثغرة SQLi موجودة في: {url}"
            except:
                pass
        return None

    def check_xss(self, url):
        """كشف ثغرات XSS"""
        payload = "<script>alert('MunxHunt_XSS')</script>"
        try:
            response = self.session.get(f"{url}?q={payload}", timeout=3)
            if payload in response.text:
                return f"ثغرة XSS موجودة في: {url}"
        except:
            pass
        return None

    def generate_report(self):
        """إنشاء تقرير بالنتائج"""
        if self.output:
            with open(self.output, 'w', encoding='utf-8') as f:
                json.dump(self.found, f, indent=4, ensure_ascii=False)
            self.log(f"تم حفظ التقرير في: {self.output}", "success")

    def run(self):
        """الدالة الرئيسية لتشغيل الأداة"""
        start_time = time.time()
        print(BANNER)
        
        try:
            self.subdomain_storm()
            self.port_lightning()
            self.vulnerability_scan()
            
            # عرض النتائج الختامية
            self.log("\n----- النتائج النهائية -----", "info")
            self.log(f"النطاقات الفرعية: {len(self.found['subdomains'])}", "success")
            self.log(f"المنافذ المفتوحة: {len(self.found['open_ports'])}", "success")
            self.log(f"الثغرات المكتشفة: {len(self.found['vulnerabilities'])}", "critical")
            self.log(f"الوقت المستغرق: {time.time() - start_time:.2f} ثانية", "info")
            
            self.generate_report()
            
        except KeyboardInterrupt:
            self.log("\nتم إيقاف العملية بواسطة المستخدم!", "error")
            sys.exit(1)
        except Exception as e:
            self.log(f"خطأ غير متوقع: {str(e)}", "error")
            sys.exit(1)

# ===================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"{Colors.BOLD}MunxHunt - أداة متقدمة لاختبار الاختراق{Colors.END}",
        epilog=f"{Colors.YELLOW}أمثلة:{Colors.END}\n  MunxHunt -t example.com\n  MunxHunt -t 192.168.1.1 -v --threads 300",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # الإعدادات الأساسية
    parser.add_argument('-t', '--target', required=True,
                        help='(EN) Target domain or IP address\n(AR) النطاق أو العنوان IP المستهدف')
    parser.add_argument('-o', '--output',
                        help='(EN) Output file for results (JSON format)\n(AR) ملف لحفظ النتائج بصيغة JSON')
    parser.add_argument('--threads', type=int, default=100,
                        help='(EN) Number of parallel threads (default: 100)\n(AR) عدد الخيوط المتوازية (افتراضي: 100)')
    parser.add_argument('-v', '--vuln-scan', action='store_true',
                        help='(EN) Enable advanced vulnerability scanning\n(AR) تفعيل الفحص المتقدم للثغرات')
    parser.add_argument('--stealth', action='store_true',
                        help='(EN) Enable stealth mode to avoid detection\n(AR) تفعيل الوضع التخفي لتجنب الكشف')
    
    # إذا لم يتم إدخال أي أوامر
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    # بدء التشغيل
    scanner = MunxHunt(args)
    scanner.run()
