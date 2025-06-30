Create a Python script for Termux that scans and displays nearby Wi-Fi networks. Requirements:

1. **Command Execution**  
   - Use `subprocess` to run:  
     `termux-wifi-scaninfo`  
   - Capture JSON output, handle errors if Termux API missing  

2. **Data Processing**  
   - Parse JSON to extract: `ssid`, `rssi` (signal strength), `frequency`  
   - Handle hidden networks (empty SSID → "[Hidden]")  
   - Convert frequency to channel:  
     ```python
     if freq < 3000:  # 2.4GHz band
         channel = (freq - 2407) // 5
     else:  # 5GHz band
         channel = (freq - 5000) // 5
     ```

3. **Signal Visualization**  
   - Map RSSI to 5-tier visual indicator:  
     ```
     RSSI >= -55: █ (strong)  
     -56 to -65: ▆  
     -66 to -75: ▄  
     -76 to -85: ▂  
     RSSI <= -86: ▁ (weak)
     ```

4. **Output Format**  
   - Table with columns: `SSID`, `Strength`, `Channel`  
   - Sort networks by signal strength (strongest first)  
   - Truncate long SSIDs (max 20 chars)  
   - Color code: strong=green, weak=red  

5. **Error Handling**  
   - Check Termux API installation  
   - Handle no Wi-Fi hardware/permissions  
   - Graceful exit on errors  

6. **Usage**  
   ```bash
   python wifi_scanner.py
   ```
7. **GitHub & Cli**  
    - Always make a new branch and push on GitHub.  
    ```
    git init
    git add .
    git commit -m "<commit-name>"
    git branch -M main
    git remote add origin https://github.com/rkstudio585/Wifi-Scan.git
    git push -u origin main
    ```

Include required Android permissions note in comments. Use only Termux-compatible libraries.
