# Appium Configuration for Real Android Devices

## Overview
This document provides detailed configuration for setting up Appium to run tests on real Android devices for the Muatrans cargo shipping app.

## Prerequisites

### Device Setup
1. Enable Developer Options on the Android device:
   - Go to Settings > About phone
   - Tap "Build number" 7 times until you see "You are now a developer!"

2. Enable USB Debugging:
   - Go to Settings > Developer options
   - Enable "USB debugging"

3. Connect the device to your machine via USB
4. Verify device connection:
   ```bash
   adb devices
   ```
   Expected output:
   ```
   List of devices attached
   <device_id>    device
   ```

### Appium Server Installation
1. Install Node.js (v14 or higher)
2. Install Appium:
   ```bash
   npm install -g appium
   ```
3. Install Appium Doctor (optional, for verification):
   ```bash
   npm install -g appium-doctor
   appium-doctor --android
   ```

## Appium Configuration

### capabilities.json
```json
{
  "platformName": "Android",
  "platformVersion": "13",
  "deviceName": "Android Device",
  "udid": "<your_device_udid>",
  "automationName": "UiAutomator2",
  "app": "/path/to/muatrans.apk",
  "appPackage": "com.muatmuat.muatrans",
  "appActivity": "com.muatmuat.muatrans.MainActivity",
  "noReset": false,
  "fullReset": false,
  "unicodeKeyboard": true,
  "resetKeyboard": true,
  "autoGrantPermissions": true,
  "newCommandTimeout": 60000,
  "connectHardwareKeyboard": false
}
```

### Configuration Parameters Explained

| Parameter | Value | Description |
|-----------|-------|-------------|
| platformName | "Android" | The mobile platform |
| platformVersion | "13" | Android version (adjust based on your device) |
| deviceName | "Android Device" | Name of the device (can be any descriptive name) |
| udid | "<device_udid>" | Unique device identifier (from `adb devices`) |
| automationName | "UiAutomator2" | Automation engine for Android |
| app | "/path/to/muatrans.apk" | Path to the APK file |
| appPackage | "com.muatmuat.muatrans" | Package name of the app |
| appActivity | "com.muatmuat.muatrans.MainActivity" | Main activity of the app |
| noReset | false | Don't reset app state before session |
| fullReset | false | Don't perform full reset |
| unicodeKeyboard | true | Enable Unicode input |
| resetKeyboard | true | Reset keyboard to original state |
| autoGrantPermissions | true | Automatically grant app permissions |
| newCommandTimeout | 60000 | Timeout for Appium commands (in milliseconds) |
| connectHardwareKeyboard | false | Don't connect hardware keyboard |

### appium_config.py
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Appium Server Configuration
APPIUM_SERVER_URL = os.getenv('APPIUM_SERVER_URL', 'http://localhost:4723/wd/hub')

# Device Configuration
DEVICE_UDID = os.getenv('DEVICE_UDID', '')
PLATFORM_VERSION = os.getenv('PLATFORM_VERSION', '13')

# App Configuration
APP_PATH = os.getenv('APP_PATH', '/path/to/muatrans.apk')
APP_PACKAGE = os.getenv('APP_PACKAGE', 'com.muatmuat.muatrans')
APP_ACTIVITY = os.getenv('APP_ACTIVITY', 'com.muatmuat.muatrans.MainActivity')

# Timeouts
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '30'))
```

### .env file (for environment variables)
```
# Appium Server
APPIUM_SERVER_URL=http://localhost:4723/wd/hub

# Device Configuration
DEVICE_UDID=your_device_udid_here
PLATFORM_VERSION=13

# App Configuration
APP_PATH=/path/to/muatrans.apk
APP_PACKAGE=com.muatmuat.muatrans
APP_ACTIVITY=com.muatmuat.muatrans.MainActivity

# Timeouts (in seconds)
IMPLICIT_WAIT=10
EXPLICIT_WAIT=30
```

## Driver Initialization

### driver_utils.py
```python
import json
import os
from appium import webdriver
from config.appium_config import APPIUM_SERVER_URL

def get_driver():
    """
    Initialize and return Appium driver for real Android device
    """
    # Load capabilities from JSON file
    caps_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'caps.json')
    
    with open(caps_file) as f:
        desired_caps = json.load(f)
    
    # Override UDID from environment variable if available
    if os.getenv('DEVICE_UDID'):
        desired_caps['udid'] = os.getenv('DEVICE_UDID')
    
    # Initialize driver
    driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    return driver

def quit_driver(driver):
    """
    Quit the Appium driver and close the app
    """
    if driver:
        driver.quit()
```

## Starting Appium Server

### Manual Start
```bash
appium --address 127.0.0.1 --port 4723
```

### Programmatic Start (Optional)
```python
import subprocess
import time
import requests

def start_appium_server():
    """
    Start Appium server programmatically
    """
    # Start Appium server
    process = subprocess.Popen(
        ['appium', '--address', '127.0.0.1', '--port', '4723'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    time.sleep(5)
    
    # Check if server is running
    try:
        response = requests.get('http://127.0.0.1:4723/wd/hub/status')
        if response.status_code == 200:
            print("Appium server started successfully")
            return process
        else:
            print("Failed to start Appium server")
            return None
    except Exception as e:
        print(f"Error starting Appium server: {e}")
        return None

def stop_appium_server(process):
    """
    Stop Appium server
    """
    if process:
        process.terminate()
        process.wait()
        print("Appium server stopped")
```

## Device Connection Verification

### verify_device_connection.py
```python
import subprocess
import re

def get_connected_devices():
    """
    Get list of connected Android devices
    """
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.split('\n')[1:]  # Skip header line
            devices = []
            for line in lines:
                if line.strip():
                    parts = line.split('\t')
                    if len(parts) >= 2 and parts[1] == 'device':
                        devices.append(parts[0])
            return devices
        else:
            print(f"Error getting devices: {result.stderr}")
            return []
    except Exception as e:
        print(f"Exception getting devices: {e}")
        return []

def verify_device_connection(udid):
    """
    Verify if a specific device is connected
    """
    devices = get_connected_devices()
    return udid in devices

def get_device_info(udid):
    """
    Get device information
    """
    try:
        # Get device model
        model_result = subprocess.run(
            ['adb', '-s', udid, 'shell', 'getprop', 'ro.product.model'],
            capture_output=True, text=True
        )
        model = model_result.stdout.strip() if model_result.returncode == 0 else "Unknown"
        
        # Get Android version
        version_result = subprocess.run(
            ['adb', '-s', udid, 'shell', 'getprop', 'ro.build.version.release'],
            capture_output=True, text=True
        )
        version = version_result.stdout.strip() if version_result.returncode == 0 else "Unknown"
        
        return {
            'model': model,
            'version': version,
            'udid': udid
        }
    except Exception as e:
        print(f"Error getting device info: {e}")
        return None
```

## Troubleshooting Common Issues

### 1. Device Not Detected
- Check USB cable connection
- Ensure USB debugging is enabled
- Try reconnecting the device
- Check if device is authorized for USB debugging

### 2. Appium Session Creation Failed
- Verify Appium server is running
- Check if device is connected via `adb devices`
- Verify app package and activity names
- Check if APK path is correct

### 3. Element Not Found
- Verify element locators using Appium Inspector
- Check if app is fully loaded
- Add explicit waits for dynamic elements
- Verify if element is within scrollable area

### 4. Permission Issues
- Ensure `autoGrantPermissions` is set to true
- Manually grant permissions on the device
- Check if app has necessary permissions in manifest

## Best Practices

1. Always verify device connection before starting tests
2. Use environment variables for sensitive configuration
3. Implement proper error handling for driver initialization
4. Take screenshots on test failures for debugging
5. Clean up app state between test runs
6. Use explicit waits instead of sleep statements
7. Organize capabilities in a separate JSON file
8. Implement proper logging for debugging

## Next Steps

1. Set up the real Android device with USB debugging
2. Install and configure Appium server
3. Create the configuration files as outlined above
4. Test the driver initialization
5. Verify app installation and launch
6. Proceed with implementing Page Object Model and test cases