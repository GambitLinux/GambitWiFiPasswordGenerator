#!/bin/bash
# GambitWiFiPasswordGenerator Installer for Kali Linux

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║        GambitWiFiPasswordGenerator Installer             ║"
echo "║                  for Kali Linux                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${YELLOW}[!] This script should be run as root for system-wide installation${NC}"
   echo -e "${YELLOW}    Press Enter to continue anyway or Ctrl+C to cancel${NC}"
   read
fi

# Check if running on Kali
if ! grep -i kali /etc/os-release > /dev/null 2>&1; then
    echo -e "${YELLOW}[!] Warning: This doesn't look like Kali Linux${NC}"
    echo -e "${YELLOW}    The tool will still work, but may need manual setup${NC}"
fi

# Check Python version
echo -e "${GREEN}[*] Checking Python version...${NC}"
python3_version=$(python3 --version 2>&1 | awk '{print $2}')
if [[ -z "$python3_version" ]]; then
    echo -e "${RED}[!] Python3 not found! Installing...${NC}"
    apt-get update
    apt-get install -y python3
else
    echo -e "${GREEN}[+] Python3 $python3_version found${NC}"
fi

# No dependencies needed! (pure Python)
echo -e "${GREEN}[+] No external Python packages required${NC}"

# Create directory structure
echo -e "${GREEN}[*] Setting up GambitWiFiPasswordGenerator...${NC}"
mkdir -p /opt/gambitwifi 2>/dev/null || sudo mkdir -p /opt/gambitwifi

# Copy main script
if [ -f "./gambitwifi.py" ]; then
    cp gambitwifi.py /opt/gambitwifi/
    echo -e "${GREEN}[+] Main script copied to /opt/gambitwifi/${NC}"
else
    echo -e "${RED}[!] gambitwifi.py not found in current directory${NC}"
    echo -e "${YELLOW}    Please run installer from the same directory as the script${NC}"
    exit 1
fi

# Copy additional files if they exist (optional)
[ -f "./requirements.txt" ] && cp requirements.txt /opt/gambitwifi/ 2>/dev/null
[ -f "./README.md" ] && cp README.md /opt/gambitwifi/ 2>/dev/null

# Make script executable
chmod +x /opt/gambitwifi/gambitwifi.py

# Create symlink in /usr/local/bin
if [[ $EUID -eq 0 ]]; then
    ln -sf /opt/gambitwifi/gambitwifi.py /usr/local/bin/gambitwifi
    echo -e "${GREEN}[+] Created system-wide command: gambitwifi${NC}"
else
    mkdir -p ~/.local/bin
    ln -sf /opt/gambitwifi/gambitwifi.py ~/.local/bin/gambitwifi
    echo -e "${GREEN}[+] Created user command: ~/.local/bin/gambitwifi${NC}"
    echo -e "${YELLOW}    Make sure ~/.local/bin is in your PATH${NC}"
fi

# Final message
echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════╗"
echo "║                 INSTALLATION COMPLETE!                   ║"
echo "╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}USAGE:${NC}"
echo "  gambitwifi"
echo ""
echo -e "${YELLOW}EXAMPLES:${NC}"
echo "  gambitwifi  # Run interactive menu"
echo ""
echo -e "${RED}⚠️  LEGAL DISCLAIMER:${NC}"
echo "  This tool is for EDUCATIONAL PURPOSES ONLY."
echo "  Only use on networks you own or have explicit permission to test."
echo "  Unauthorized use is illegal."
echo ""
echo -e "${GREEN}[+] Installation complete! Run 'gambitwifi' to start${NC}"