# Termux Wi-Fi Scanner

A Python script for Termux that scans and displays nearby Wi-Fi networks in a clean, readable table format.

## Description

This script utilizes the Termux API to fetch information about nearby Wi-Fi networks and presents it in a terminal-friendly table. It shows the network's SSID, signal strength (visualized with bars and dBm), and Wi-Fi channel. The list is sorted by signal strength, with color-coding to quickly identify strong and weak signals.

## Features

-   **Scans and lists nearby Wi-Fi networks.**
-   **Displays SSID, Signal Strength, and Channel.**
-   **Visual signal strength indicator (▂▄▆█).**
-   **Color-coded signal strength (Green for strong, Red for weak).**
-   **Sorts networks by signal strength.**
-   **Handles hidden networks.**
-   **Truncates long SSIDs.**
-   **Error handling for missing Termux API or permissions.**

## Requirements

-   **Termux:** A terminal emulator for Android.
-   **Termux:API:** An add-on app that exposes Android functionality to the command line. Install it from F-Droid or the Play Store, and install the `termux-api` package in Termux:
    ```bash
    pkg install termux-api
    ```

## Usage

1.  Clone the repository or download the `wifi_scanner.py` script.
2.  Make the script executable:
    ```bash
    chmod +x wifi_scanner.py
    ```
3.  Run the script:
    ```bash
    ./wifi_scanner.py
    ```

## Android Permissions

For the script to work, Termux needs the following Android permissions. You can grant them via the Android settings for the Termux app:

-   `android.permission.ACCESS_FINE_LOCATION`
-   `android.permission.ACCESS_COARSE_LOCATION`
-   `android.permission.ACCESS_WIFI_STATE`
-   `android.permission.CHANGE_WIFI_STATE`

## Example Output

```
SSID                 Strength   Channel
--------------------------------------
MyHomeNetwork        █ (-52 dBm)      6
AnotherNetwork       ▆ (-63 dBm)     11
HiddenNetwork        ▄ (-70 dBm)     44
WeakSignal           ▂ (-82 dBm)      1
```
