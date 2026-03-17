#!/usr/bin/env python3
"""
GambitWiFiGenerator - Complete Control Edition
Add, remove, and edit everything interactively
"""

import os
import sys
from datetime import datetime
from typing import Set, List

class GambitWiFiGenerator:
    def __init__(self):
        self.version = "4.0"
        
        # Common WiFi passwords
        self.common_wifi = [
            "password", "admin", "guest", "wifi", "wireless", "internet",
            "network", "router", "linksys", "netgear", "tp-link", "d-link",
            "belkin", "cisco", "huawei", "vodafone", "comcast", "xfinity",
            "att", "verizon", "spectrum", "cox", "charter", "optimum",
            "default", "changeme", "123456", "12345678", "123456789",
            "qwerty", "qwertyuiop", "asdfgh", "zxcvbn", "111111", "000000",
            "iloveyou", "monkey", "dragon", "master", "super", "hello",
            "letmein", "trustno1", "secret", "password1", "abc123",
            "wifi123", "wlan", "wpa2", "hotspot", "mobile",
            "connect", "access", "secure", "private", "guest123",
            "admin123", "root", "toor", "administrator"
        ]
        
        # Common affixes
        self.common_affixes = [
            "", "123", "1234", "12345", "123456", "1234567", "12345678",
            "123456789", "0", "00", "000", "0000", "1", "11", "111", "1111",
            "!", "!!", "@", "@@", "#", "##", "$", "$$", "%", "%%",
            "&", "*", "?", "!@#", "123!", "123@", "123#", "!123", "@123", "#123",
            "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
            "20", "21", "22", "23", "24", "25", "26", "27"
        ]
        
        # Leet speak substitutions
        self.leet_map = {
            'a': ['4', '@'], 'b': ['8'], 'c': ['('], 'e': ['3'],
            'g': ['9'], 'i': ['1', '!'], 'l': ['1'], 'o': ['0'],
            's': ['5', '$'], 't': ['7'], 'z': ['2']
        }
    
    def generate_case_variations(self, text: str) -> List[str]:
        """Generate ALL possible capitalization variations."""
        if not text:
            return [text]
        
        variations = set()
        
        variations.add(text.lower())
        variations.add(text.upper())
        variations.add(text.capitalize())
        variations.add(text.title())
        variations.add(text[0].upper() + text[1:].lower() if text else text)
        
        alt1 = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))
        alt2 = ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text))
        variations.add(alt1)
        variations.add(alt2)
        
        if len(text) <= 6:
            for bits in range(1 << len(text)):
                variant = ''
                for i, c in enumerate(text):
                    if (bits >> i) & 1:
                        variant += c.upper()
                    else:
                        variant += c.lower()
                variations.add(variant)
        
        return list(variations)
    
    def generate_leet(self, word: str) -> List[str]:
        """Generate leet speak variations."""
        leet_set = set()
        leet_set.add(word)
        
        word_lower = word.lower()
        
        for char, subs in self.leet_map.items():
            if char in word_lower:
                for sub in subs:
                    leet_set.add(word_lower.replace(char, sub))
        
        if 'a' in word_lower and 'e' in word_lower:
            leet_set.add(word_lower.replace('a', '4').replace('e', '3'))
        if 'o' in word_lower and 's' in word_lower:
            leet_set.add(word_lower.replace('o', '0').replace('s', '5'))
        
        return list(leet_set)[:20]
    
    def generate(self, keywords: List[str], years: List[int], 
                 use_leet: bool = True, use_affixes: bool = True,
                 use_caps: bool = True, use_common: bool = True,
                 max_count: int = 10000) -> Set[str]:
        """Generate ALL possible password combinations."""
        passwords = set()
        
        base_words = set(keywords)
        if use_common:
            base_words.update(self.common_wifi)
        
        base_list = list(base_words)
        
        print(f"\n[*] Generating from {len(base_list)} base words...")
        print(f"[*] Creating combinations...")
        
        # Basic combinations
        print("   ├─ Basic combinations...")
        for word in base_list:
            if len(passwords) >= max_count:
                break
            
            if use_caps:
                for variant in self.generate_case_variations(word):
                    if len(passwords) >= max_count:
                        break
                    passwords.add(variant)
            else:
                passwords.add(word)
            
            for year in years:
                if len(passwords) >= max_count:
                    break
                combos = [f"{word}{year}", f"{year}{word}", f"{word}_{year}", f"{word}-{year}"]
                for combo in combos:
                    if use_caps:
                        for variant in self.generate_case_variations(combo):
                            if len(passwords) >= max_count:
                                break
                            passwords.add(variant)
                    else:
                        passwords.add(combo)
            
            if use_affixes:
                for affix in self.common_affixes[:15]:
                    if len(passwords) >= max_count:
                        break
                    if affix:
                        combos = [f"{word}{affix}", f"{affix}{word}"]
                        for combo in combos:
                            if use_caps:
                                for variant in self.generate_case_variations(combo):
                                    if len(passwords) >= max_count:
                                        break
                                    passwords.add(variant)
                            else:
                                passwords.add(combo)
        
        # Word+Word combinations
        print("   ├─ Word+Word combinations...")
        for word1 in base_list[:30]:
            if len(passwords) >= max_count:
                break
            for word2 in base_list[:30]:
                if len(passwords) >= max_count:
                    break
                if word1 != word2:
                    base_combo = f"{word1}{word2}"
                    
                    if use_caps:
                        for variant in self.generate_case_variations(base_combo):
                            if len(passwords) >= max_count:
                                break
                            passwords.add(variant)
                            
                            for year in years[:3]:
                                if len(passwords) >= max_count:
                                    break
                                year_combo = f"{variant}{year}"
                                for year_variant in self.generate_case_variations(year_combo):
                                    if len(passwords) >= max_count:
                                        break
                                    passwords.add(year_variant)
                    else:
                        passwords.add(base_combo)
        
        print(f"   └─ Complete! Generated {len(passwords)} unique passwords")
        return passwords

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = r"""
_    _ _______ _______             _____            
| |  | (_)  ___(_) ___ \           |  __ \           
| |  | |_| |_   _| |_/ /_ _ ___ ___| |  \/ ___ _ __  
| |/\| | |  _| | |  __/ _` / __/ __| | __ / _ \ '_ \ 
\  /\  / | |   | | | | (_| \__ \__ \ |_\ \  __/ | | |
 \/  \/|_\_|   |_\_|  \__,_|___/___/\____/\___|_| |_|
                                                     
                    made by Gambit
              FOR EDUCATIONAL USE ONLY
    """
    print(header)

def print_menu(keywords, years, use_leet, use_affixes, use_caps, use_common, max_count):
    print("\n" + "="*70)
    print("                    CURRENT CONFIGURATION")
    print("="*70)
    
    # Keywords with numbers
    print(f"\n📝 KEYWORDS ({len(keywords)}):")
    if keywords:
        for i, kw in enumerate(keywords, 1):
            print(f"   {i:2}. {kw}")
    else:
        print("   None")
    print("   [K] Add keyword   [R] Remove keyword   [C] Clear all keywords")
    
    # Years with numbers
    print(f"\n📅 YEARS ({len(years)}):")
    if years:
        for i, year in enumerate(years, 1):
            print(f"   {i:2}. {year}")
    else:
        print("   None")
    print("   [Y] Add years   [Z] Remove year   [X] Clear all years")
    
    print(f"\n⚙️  OPTIONS:")
    print(f"   [L] Leet speak: {'✅ ON' if use_leet else '❌ OFF'}")
    print(f"   [A] Affixes (123, !, @): {'✅ ON' if use_affixes else '❌ OFF'}")
    print(f"   [P] Capitalization: {'✅ ON' if use_caps else '❌ OFF'}")
    print(f"   [M] Common passwords: {'✅ ON' if use_common else '❌ OFF'}")
    
    print(f"\n📊 MAX PASSWORDS: {max_count}")
    print(f"   [N] Change max count")
    
    print("\n🎯 ACTIONS:")
    print("   [G] GENERATE wordlist")
    print("   [Q] Quit")
    print("="*70)

def add_keywords():
    keywords = []
    print("\n" + "-"*40)
    print("ADD KEYWORDS (one at a time)")
    print("-"*40)
    print("Enter keywords one by one. Press ENTER with no text to finish.")
    print("Type 'b' to go back without saving.")
    
    while True:
        kw = input("\nKeyword: ").strip()
        if kw.lower() == 'b':
            if keywords:
                print(f"\n[+] Saved {len(keywords)} keywords")
                return keywords
            return None
        elif kw == "":
            if keywords:
                print(f"\n[+] Saved {len(keywords)} keywords")
                return keywords
            print("No keywords entered")
            return None
        else:
            keywords.append(kw)
            print(f"   Added: {kw} ({len(keywords)} total)")

def remove_keyword(keywords):
    """Remove a specific keyword by number."""
    if not keywords:
        print("\n[!] No keywords to remove")
        input("Press Enter to continue...")
        return keywords
    
    print("\n" + "-"*40)
    print("REMOVE KEYWORD")
    print("-"*40)
    for i, kw in enumerate(keywords, 1):
        print(f"   {i}. {kw}")
    
    try:
        choice = input("\nEnter number to remove (or 'b' to go back): ").strip()
        if choice.lower() == 'b':
            return keywords
        
        idx = int(choice) - 1
        if 0 <= idx < len(keywords):
            removed = keywords.pop(idx)
            print(f"\n[+] Removed: {removed}")
        else:
            print("\n[!] Invalid number")
    except:
        print("\n[!] Invalid input")
    
    input("Press Enter to continue...")
    return keywords

def clear_keywords():
    """Clear all keywords."""
    print("\n" + "-"*40)
    print("CLEAR ALL KEYWORDS")
    print("-"*40)
    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == 'y':
        print("\n[+] All keywords cleared")
        return []
    return None

def add_years():
    """Add years interactively."""
    current_year = datetime.now().year
    available_years = list(range(current_year - 10, current_year + 2))
    
    print("\n" + "-"*40)
    print("ADD YEARS")
    print("-"*40)
    print("Available years:")
    for i, year in enumerate(available_years, 1):
        print(f"   {i}. {year}")
    
    print("\nEnter year numbers separated by spaces (e.g., '1 3 5')")
    print("Or type 'all' for all years, 'b' to go back")
    
    while True:
        choice = input("\nSelect: ").strip().lower()
        
        if choice == 'b':
            return None
        
        if choice == 'all':
            return available_years
        
        try:
            indices = [int(x)-1 for x in choice.split()]
            selected = [available_years[i] for i in indices if 0 <= i < len(available_years)]
            if selected:
                print(f"✓ Selected: {', '.join(map(str, selected))}")
                return selected
            else:
                print("No valid years selected")
        except:
            print("Invalid input. Try again.")

def remove_year(years):
    """Remove a specific year by number."""
    if not years:
        print("\n[!] No years to remove")
        input("Press Enter to continue...")
        return years
    
    print("\n" + "-"*40)
    print("REMOVE YEAR")
    print("-"*40)
    for i, year in enumerate(years, 1):
        print(f"   {i}. {year}")
    
    try:
        choice = input("\nEnter number to remove (or 'b' to go back): ").strip()
        if choice.lower() == 'b':
            return years
        
        idx = int(choice) - 1
        if 0 <= idx < len(years):
            removed = years.pop(idx)
            print(f"\n[+] Removed: {removed}")
        else:
            print("\n[!] Invalid number")
    except:
        print("\n[!] Invalid input")
    
    input("Press Enter to continue...")
    return years

def clear_years():
    """Clear all years."""
    print("\n" + "-"*40)
    print("CLEAR ALL YEARS")
    print("-"*40)
    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == 'y':
        print("\n[+] All years cleared")
        return []
    return None

def change_max_count():
    """Change maximum password count."""
    print("\n" + "-"*40)
    print("MAXIMUM PASSWORDS")
    print("-"*40)
    print("Enter new maximum (100-1,000,000) or 'b' to go back")
    
    while True:
        choice = input("\nMax count: ").strip().lower()
        
        if choice == 'b':
            return None
        
        try:
            count = int(choice)
            if 100 <= count <= 1000000:
                return count
            else:
                print("Please enter a number between 100 and 1,000,000")
        except:
            print("Invalid number. Try again.")

def main():
    clear_screen()
    print_header()
    
    # Default configuration
    keywords = []
    years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
    use_leet = True
    use_affixes = True
    use_caps = True
    use_common = True
    max_count = 10000
    
    while True:
        print_menu(keywords, years, use_leet, use_affixes, use_caps, use_common, max_count)
        
        choice = input("\nEnter choice: ").strip().upper()
        
        # Keyword management
        if choice == 'K':
            new_keywords = add_keywords()
            if new_keywords is not None:
                keywords.extend(new_keywords)
            clear_screen()
            print_header()
            
        elif choice == 'R':
            keywords = remove_keyword(keywords)
            clear_screen()
            print_header()
            
        elif choice == 'C':  # Clear keywords
            result = clear_keywords()
            if result is not None:
                keywords = result
            clear_screen()
            print_header()
        
        # Year management
        elif choice == 'Y':
            new_years = add_years()
            if new_years is not None:
                # Add only new years (avoid duplicates)
                for year in new_years:
                    if year not in years:
                        years.append(year)
                years.sort()
            clear_screen()
            print_header()
            
        elif choice == 'Z':
            years = remove_year(years)
            clear_screen()
            print_header()
            
        elif choice == 'X':  # Clear years
            result = clear_years()
            if result is not None:
                years = result
            clear_screen()
            print_header()
        
        # Toggle options
        elif choice == 'L':
            use_leet = not use_leet
            clear_screen()
            print_header()
            print(f"\n[+] Leet speak {'enabled' if use_leet else 'disabled'}")
            
        elif choice == 'A':
            use_affixes = not use_affixes
            clear_screen()
            print_header()
            print(f"\n[+] Affixes {'enabled' if use_affixes else 'disabled'}")
            
        elif choice == 'P':
            use_caps = not use_caps
            clear_screen()
            print_header()
            print(f"\n[+] Capitalization {'enabled' if use_caps else 'disabled'}")
            
        elif choice == 'M':
            use_common = not use_common
            clear_screen()
            print_header()
            print(f"\n[+] Common passwords {'enabled' if use_common else 'disabled'}")
        
        # Change max count
        elif choice == 'N':
            new_max = change_max_count()
            if new_max is not None:
                max_count = new_max
            clear_screen()
            print_header()
        
        # Generate
        elif choice == 'G':
            if not keywords:
                print("\n[!] You need to add at least one keyword first!")
                input("\nPress Enter to continue...")
                clear_screen()
                print_header()
                continue
            
            print("\n" + "="*60)
            print("                    GENERATING PASSWORDS")
            print("="*60)
            
            generator = GambitWiFiGenerator()
            passwords = generator.generate(
                keywords=keywords,
                years=years,
                use_leet=use_leet,
                use_affixes=use_affixes,
                use_caps=use_caps,
                use_common=use_common,
                max_count=max_count
            )
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gambit_wordlist_{timestamp}.txt"
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    for pwd in sorted(passwords):
                        f.write(pwd + '\n')
                
                print(f"\n✅ SUCCESS!")
                print(f"   Generated: {len(passwords)} passwords")
                print(f"   Saved to: {filename}")
                print(f"   File size: {os.path.getsize(filename)} bytes")
                
                # Show sample
                print("\n📋 Sample passwords:")
                sample = list(sorted(passwords))[:20]
                for i, pwd in enumerate(sample, 1):
                    print(f"   {i:2}. {pwd}")
                
            except Exception as e:
                print(f"\n❌ Error saving file: {e}")
            
            input("\nPress Enter to continue...")
            clear_screen()
            print_header()
        
        # Quit
        elif choice == 'Q':
            print("\n[+] Goodbye!")
            sys.exit(0)
        
        # Invalid
        else:
            print("\n[!] Invalid choice. Please try again.")
            input("\nPress Enter to continue...")
            clear_screen()
            print_header()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[+] Goodbye!")
        sys.exit(0)