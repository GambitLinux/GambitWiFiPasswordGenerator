# GambitWiFiPasswordGenerator

**Smart WiFi Password Generator for Kali Linux**

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-kali%20linux-red)](https://www.kali.org/)
[![GitHub stars](https://img.shields.io/badge/stars-100%2B-brightgreen)](https://github.com/gambit/gambitwifi)
[![GitHub issues](https://img.shields.io/badge/issues-0%20open-success)](https://github.com/gambit/gambitwifi/issues)
                                                     
made by Gambit

## ⚠️ IMPORTANT LEGAL DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY.**

- Only use on networks you **OWN** or have **EXPLICIT WRITTEN PERMISSION** to test
- Unauthorized access to computer networks is **ILLEGAL** in most countries
- The author does **NOT** condone any illegal activity
- You are solely responsible for your actions
- Misuse may result in **criminal charges** and **severe penalties**

**I DO NOT CONDOONE ANY ILLEGAL ACTIVITY. USE RESPONSIBLY.**

---

## 📋 Description

GambitWiFiPasswordGenerator is an intelligent, interactive wordlist generator designed specifically for WiFi security testing. Unlike generic password lists like rockyou.txt, this tool creates **targeted, context-aware wordlists** based on your input, dramatically increasing the chances of successful penetration testing on authorized systems.

The tool combines:
- **Your keywords** (business names, locations, personal info)
- **Year variations** (automatically generated)
- **Common WiFi password patterns** (admin, guest, password)
- **Leet speak substitutions** (a→4, e→3, o→0, s→5)
- **ALL capitalization variations** (keyword, Keyword, KEYWORD, kEyWoRd)
- **Common affixes** (123, !, @, #, $, etc.)
- **Word combinations** (keyword1+keyword2, keyword1+keyword2+keyword3)

---

## 🚀 Features

✅ **Smart Generation** - Creates context-aware passwords based on your specific input  
✅ **FULL Capitalization Control** - Generates EVERY possible case variation (2^n combinations)  
✅ **Interactive Menu** - No command-line arguments needed - just run and follow prompts  
✅ **Complete Edit Control** - Add/remove individual keywords and years anytime  
✅ **Year Selection** - Choose from 2016-2026 with easy number selection  
✅ **Leet Speak** - Automatic substitutions: a→4, e→3, o→0, s→5, t→7, etc.  
✅ **Common Affixes** - Automatically adds 123, !, @, #, $, and more  
✅ **Common Passwords** - Built-in database of 50+ common WiFi passwords  
✅ **Pure Python** - No external dependencies - works out of the box  
✅ **Fast & Efficient** - Generates thousands of passwords in seconds  
✅ **Kali Optimized** - Works perfectly on Kali Linux with install script  
✅ **Single File** - Easy to audit, modify, and distribute  
✅ **Export to TXT** - Saves wordlist with timestamp for easy organization  
✅ **Sample Display** - Shows first 20 generated passwords for quick verification  

---

## 🔧 Installation

### Quick Install (Kali Linux)

```bash
# Download the tool
git clone https://github.com/GambitLinux/GambitWiFiPasswordGenerator.git
cd GambitWiFiPasswordGenerator

# Run installer (as root)
chmod +x install.sh
sudo ./install.sh

# Run the tool
gambitwifi
