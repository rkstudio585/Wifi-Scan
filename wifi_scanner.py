#!/usr/bin/env python3
# Android permissions required:
# android.permission.ACCESS_FINE_LOCATION
# android.permission.ACCESS_COARSE_LOCATION
# android.permission.CHANGE_WIFI_STATE
# android.permission.ACCESS_WIFI_STATE

import json
import subprocess
import sys

def get_wifi_data():
    """
    Runs the termux-wifi-scaninfo command and returns the parsed JSON output.
    Handles errors if the Termux API is not installed or if there are
    permissions issues.
    """
    try:
        # Execute the Termux command to scan for Wi-Fi networks
        output = subprocess.check_output(
            ['termux-wifi-scaninfo'],
            stderr=subprocess.PIPE,  # Capture stderr to check for errors
            text=True
        )
        # If the output is empty or just whitespace, no networks were found
        if not output.strip():
            print("[33m[!] No Wi-Fi networks found.[0m")
            sys.exit(0)
        return json.loads(output)
    except FileNotFoundError:
        # This error occurs if the 'termux-wifi-scaninfo' command is not found
        print("[31m[!] Error: Termux API is not installed.[0m")
        print("Please install it by running: pkg install termux-api")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        # This error occurs if the command returns a non-zero exit code
        error_message = e.stderr.strip()
        if "Location is disabled" in error_message:
            print("[31m[!] Error: Location services are disabled.[0m")
            print("Please enable location services to scan for Wi-Fi networks.")
        else:
            print(f"[31m[!] An unexpected error occurred: {error_message}[0m")
        sys.exit(1)
    except json.JSONDecodeError:
        # This error occurs if the output is not valid JSON
        print("[31m[!] Error: Failed to parse Wi-Fi scan data.[0m")
        print("The command output was not valid JSON.")
        sys.exit(1)

def rssi_to_bars(rssi):
    """Converts RSSI signal strength to a 5-tier visual indicator with color."""
    if rssi >= -55:
        return "[32m█[0m"  # Strong (Green)
    elif -65 <= rssi < -55:
        return "[32m▆[0m"  # Good (Green)
    elif -75 <= rssi < -65:
        return "▄"               # Fair (Default color)
    elif -85 <= rssi < -75:
        return "[31m▂[0m"  # Weak (Red)
    else:
        return "[31m [0m"  # Very Weak (Red)

def freq_to_channel(freq):
    """Converts frequency (MHz) to a Wi-Fi channel number."""
    if freq < 3000:  # 2.4 GHz band
        # Formula for 2.4 GHz channels
        return (freq - 2407) // 5
    else:  # 5 GHz band
        # Formula for 5 GHz channels
        return (freq - 5000) // 5

def main():
    """
    Main function to scan, process, and display Wi-Fi network information.
    """
    networks = get_wifi_data()

    # Sort networks by signal strength (RSSI) in descending order
    sorted_networks = sorted(networks, key=lambda x: x['rssi'], reverse=True)

    # Print the table header
    print(f"[1m{'SSID':<20} {'Strength':<10} {'Channel':>7}[0m")
    print("-" * 38)

    # Print each network's information in a formatted table
    for net in sorted_networks:
        # Truncate SSID to 20 characters, handle hidden networks
        ssid = (net['ssid'][:20] if net['ssid'] else "[Hidden]")
        strength_bars = rssi_to_bars(net['rssi'])
        channel = freq_to_channel(net['frequency'])

        # Format the output string for the table row
        print(f"{ssid:<20} {strength_bars} ({net['rssi']} dBm) {channel:>5}")

if __name__ == "__main__":
    main()
