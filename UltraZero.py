#!/usr/bin/env python3

import argparse
import os
import sys
import socket
import requests
import threading
from queue import Queue
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import subprocess
import time
import json
import re
import dns.resolver
import ssl
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ========== التهيئة والألوان ==========
class Style:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# ========== النصوص متعددة اللغات ==========
class Language:
    def __init__(self, lang):
        self.lang = lang
        self.texts = {
            "ar": {
                "banner": """
 ██░ ██ ▄▄▄█████▓ ██▀███   █████▒███████▒ ██▀███  
▓██░ ██▒▓  ██▒ ▓▒▓██ ▒ ██▒▓██   ▒▒ ▒ ▒ ▄▀░▓██ ▒ ██▒
▒██▀▀██░▒ ▓██░ ▒░▓██ ░▄█ ▒▒████ ░░ ▒ ▄▀▒░ ▓██ ░▄█ ▒
░▓█ ░██ ░ ▓██▓ ░ ▒██▀▀█▄  ░▓█▒  ░  ▄▀▒   ░▒██▀▀█▄  
░▓█▒░██▓  ▒██▒ ░ ░██▓ ▒██▒░▒█░  ▒███████▒░██▓ ▒██▒
 ▒ ░░▒░▒  ▒ ░░   ░ ▒▓ ░▒▓░ ▒ ░  ░░ ▒░ ░  ░ ▒▓ ░▒▓░
 ▒ ░▒░ ░    ░      ░▒ ░ ▒░ ░    ░ ░  ░    ░▒ ░ ▒░
 ░  ░░ ░  ░        ░░   ░  ░ ░    ░       ░░   ░ 
 ░  ░  ░           ░        ░  ░ ░  ░     ░     
                """,
                "title": "                      [ أداة الأمان المتطورة ]",
                "author": "                           مطور بواسطة {Style.BOLD}munx64{Style.END}",
                "github": "                     https://github.com/munx64/UltraZero",
                "starting_scan": "بدء الفحص على {target}...",
                "port_scan": "بدء فحص المنافذ السريع...",
                "subdomain_scan": "بدء تعداد النطاقات الفرعية...",
                "vuln_scan": "بدء فحص الثغرات الأمنية...",
                "crawling": "بدء الزحف إلى الموقع...",
                "sql_injection": "فحص ثغرات SQL Injection...",
                "xss": "فحص ثغرات XSS...",
                "completed": "تم الانتهاء من الفحص في {time:.2f} ثانية",
                "vuln_found": "تم اكتشاف {count} ثغرة أمنية",
                "aborted": "تم إلغاء العملية بواسطة المستخدم!"
            },
            "en": {
                "banner": """
 ██░ ██ ▄▄▄█████▓ ██▀███   █████▒███████▒ ██▀███  
▓██░ ██▒▓  ██▒ ▓▒▓██ ▒ ██▒▓██   ▒▒ ▒ ▒ ▄▀░▓██ ▒ ██▒
▒██▀▀██░▒ ▓██░ ▒░▓██ ░▄█ ▒▒████ ░░ ▒ ▄▀▒░ ▓██ ░▄█ ▒
░▓█ ░██ ░ ▓██▓ ░ ▒██▀▀█▄  ░▓█▒  ░  ▄▀▒   ░▒██▀▀█▄  
░▓█▒░██▓  ▒██▒ ░ ░██▓ ▒██▒░▒█░  ▒███████▒░██▓ ▒██▒
 ▒ ░░▒░▒  ▒ ░░   ░ ▒▓ ░▒▓░ ▒ ░  ░░ ▒░ ░  ░ ▒▓ ░▒▓░
 ▒ ░▒░ ░    ░      ░▒ ░ ▒░ ░    ░ ░  ░    ░▒ ░ ▒░
 ░  ░░ ░  ░        ░░   ░  ░ ░    ░       ░░   ░ 
 ░  ░  ░           ░        ░  ░ ░  ░     ░     
                """,
                "title": "                      [ Ultimate Security Scanner ]",
                "author": "                           coded by {Style.BOLD}munx64{Style.END}",
                "github": "                     https://github.com/munx64/UltraZero",
                "starting_scan": "Starting scan on {target}...",
                "port_scan": "Starting Lightning Port Scan...",
                "subdomain_scan": "Starting Subdomain Enumeration...",
                "vuln_scan": "Starting Vulnerability Scan...",
                "crawling": "Launching Deep Crawler...",
                "sql_injection": "Checking for SQL Injection...",
                "xss": "Checking for XSS Vulnerabilities...",
                "completed": "Scan Completed in {time:.2f} seconds",
                "vuln_found": "Total Vulnerabilities Found: {count}",
                "aborted": "Operation aborted by user!"
            }
        }

    def get(self, key, **kwargs):
        return self.texts[self.lang].get(key, "").format(**kwargs)

# ========== الفئات الرئيسية ==========
class UltraZero:
    def __init__(self, target, output=None, threads=200, stealth=False, lang="en"):
        self.target = target
        self.output = output
        self.threads = threads
        self.stealth = stealth
        self.lang = Language(lang)
        self.lock = threading.Lock()
        self.queue = Queue()
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'UltraZero/1.0'})
        self.discovered_urls = set()
        self.vulnerabilities = []
        
        if output:
            open(output, 'w').close()

    def log(self, message, level="info"):
        color = {
            "info": Style.BLUE,
            "success": Style.GREEN,
            "warning": Style.YELLOW,
            "error": Style.RED,
            "critical": Style.MAGENTA
        }.get(level, Style.BLUE)
        
        with self.lock:
            msg = f"{color}[{level.upper()}] {message}{Style.END}"
            print(msg)
            if self.output:
                with open(self.output, 'a') as f:
                    f.write(msg + '\n')

    def show_banner(self):
        print(f"{Style.CYAN}{self.lang.get('banner')}{Style.END}")
        print(f"{Style.YELLOW}{Style.BOLD}{self.lang.get('title')}{Style.END}")
        print(f"{Style.RED}{self.lang.get('author')}{Style.END}")
        print(f"{Style.GREEN}{self.lang.get('github')}{Style.END}")

    # ========== تقنيات الفحص المتقدمة ==========
    def super_fast_port_scan(self):
        self.log(self.lang.get("port_scan"), "info")
        
        ports = [21,22,80,443,8080,8443,3306,3389]
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.check_port, port): port for port in ports}
            for future in as_completed(futures):
                result = future.result()
                if result:
                    self.log(f"Port {result} is open", "success")

    def check_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((self.target, port))
                return port if result == 0 else None
        except:
            return None

    # ... (أضف باقي الوظائف هنا)

    def execute(self):
        start_time = time.time()
        self.show_banner()
        
        self.log(self.lang.get("starting_scan", target=self.target), "info")
        self.super_fast_port_scan()
        
        self.log(self.lang.get("completed", time=time.time() - start_time), "success")
        self.log(self.lang.get("vuln_found", count=len(self.vulnerabilities)), "critical")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UltraZero - Ultimate Security Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target domain/IP")
    parser.add_argument("-o", "--output", help="Output file (JSON format)")
    parser.add_argument("--threads", type=int, default=200, help="Threads count (default: 200)")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth mode")
    parser.add_argument("--lang", choices=["ar", "en"], default="en", help="Language (ar/en)")
    
    args = parser.parse_args()
    
    scanner = UltraZero(
        target=args.target,
        output=args.output,
        threads=args.threads,
        stealth=args.stealth,
        lang=args.lang
    )
    
    try:
        scanner.execute()
    except KeyboardInterrupt:
        print(f"\n{Style.RED}{scanner.lang.get('aborted')}{Style.END}")
        sys.exit(1)
