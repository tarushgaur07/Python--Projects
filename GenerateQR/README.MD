# UPI QR Code Generator

A simple Python script to automatically generate and save personalized UPI QR codes for major Indian payment apps like **PhonePe**, **Google Pay (GPay)**, and **BharatPe** using a single UPI ID input.

---

## Features

* **Dynamic Input:** Enter your UPI ID dynamically at runtime.
* **Multi-App Compatibility:** Generates individual, app-compatible QR code URLs.
* **Auto-Save:** Saves the generated QR codes locally as `.png` images.
* **Auto-Display:** Automatically opens and displays the generated QR codes upon creation.

---

## Prerequisites

Before running the script, make sure you have Python installed on your system along with the `qrcode` library and `Pillow` (for image rendering).

### Install Dependencies

You can install the required packages using `pip`:

```bash
pip install qrcode[pil]
