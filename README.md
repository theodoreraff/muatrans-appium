# Muatrans Android Automation Testing

This project contains the automation test framework for the Muatrans Android app using Python + Appium.

## Project Structure

```
muatrans-automation/
├── config/                   # Configuration files
│   ├── __init__.py
│   └── capabilities.json     # Appium capabilities for real devices
├── pages/                    # Page Object Model (POM) classes
│   └── __init__.py
├── tests/                    # Test cases
│   └── __init__.py
├── utils/                    # Utility functions
│   ├── __init__.py
│   └── driver_setup.py       # Driver initialization and management
├── screenshots/              # Failure screenshots (created automatically)
├── reports/                  # Test execution reports (created automatically)
├── requirements.txt          # Python dependencies
├── conftest.py               # Pytest fixtures
├── pytest.ini               # Pytest configuration
└── .env.example             # Environment variables template
```

## Prerequisites

1. Python 3.8 or higher
2. Appium server installed and running
3. Real Android device with USB debugging enabled
4. Muatrans APK file

## Setup Instructions

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and update with your device and app details:
   ```bash
   cp .env.example .env
   ```
4. Update `config/capabilities.json` with your app details:
   - Set the correct path to your APK file
   - Update appPackage and appActivity if needed
5. Connect your Android device and ensure USB debugging is enabled
6. Start Appium server:
   ```bash
   appium
   ```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test file:
```bash
pytest tests/test_shipment_form.py
```

To run tests with specific marker:
```bash
pytest -m smoke
```

## Configuration

### Environment Variables

You can configure the following environment variables in your `.env` file:

- `APPIUM_SERVER_URL`: Appium server URL (default: http://localhost:4723/wd/hub)
- `DEVICE_UDID`: UDID of your Android device
- `PLATFORM_VERSION`: Android version of your device
- `APP_PATH`: Path to the APK file
- `APP_PACKAGE`: Package name of the app
- `APP_ACTIVITY`: Main activity of the app

### Appium Capabilities

The `config/capabilities.json` file contains the Appium capabilities for real device testing. You can modify these as needed for your specific device and app.

## Test Reports

After running tests, HTML reports will be generated in the `reports/` directory. Screenshots of test failures will be saved in the `screenshots/` directory.

## Next Steps

1. Create Page Object Model classes in the `pages/` directory
2. Implement test cases in the `tests/` directory
3. Add additional utility functions in the `utils/` directory
4. Configure CI/CD integration as needed