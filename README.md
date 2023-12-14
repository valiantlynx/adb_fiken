
# Automated Image Processing and Uploading

## Overview
This Python script automates the process of opening receipt images in a gallery, sharing them to a specific application (Fiken.no), and performing a series of actions within that application. It utilizes the Android Debug Bridge (ADB) for simulating user interactions on an Android device.
It is used by a company to process and upload receipts to the Fiken application for bookkeeping, legal, and tax purposes.

## Prerequisites
- Python installed on your system
- Android device with USB debugging enabled
- ADB (Android Debug Bridge) installed and set up
- The specified Android applications installed
    - Google Photos(can be changed to your gallery), 
    - Fiken

## Key Functionalities
- Opens the gallery app on an Android device
- Shares images to the Fiken application
- Automates various interactions within the Fiken app

## Usage
1. Ensure your Android device is connected to your computer and USB debugging is enabled.
2. Place your image files in the designated folders (`/home/valiantlynx/projects/adb_fiken/reciepts/before` and `/home/valiantlynx/projects/adb_fiken/reciepts/after`).
3. Run the script: `python <script_name>.py`

## Configuration
- `device_id`: Set this to your Android device's ID.
- `epoch`: The number of receipts or images you want to process.
- `NAMEreszd_imgs_path` and `NAMEunreszd_imgs_path`: Paths for processed and unprocessed images.

## Note
- This script is tailored for specific screen coordinates and may require adjustments for different devices or screen resolutions.
- Handle the deletion of images carefully, as the script includes commands to delete files in specified directories.

## License
This project is licensed under the MIT License



