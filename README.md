# Chrome Auto Viewer

A Python script that automatically opens a URL in Chrome Incognito mode, waits for a specified duration, closes Chrome completely, and repeats for multiple cycles. Useful for automated view testing, simple automation, or personal testing.

> ⚠️ **Note:** This script is designed for **laptops and desktop PCs running Windows**. It will **not work on mobile devices**.

---

## Features

* Open a URL in Chrome Incognito.
* Wait for a custom duration per cycle.
* Fully close Chrome after viewing.
* Repeat for multiple cycles with a 1-second gap.
* Easy to update for your device’s Chrome path.

---

## Requirements

* Python 3.x
* Google Chrome installed on a laptop/PC

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chrome-auto-viewer.git
   cd chrome-auto-viewer
   ```

2. No dependencies are required. The script can run directly with Python.

---

## How to Find Your Chrome Path

The script needs the full path to your `chrome.exe`. Here’s how to find it:

### Windows

1. Find your Chrome shortcut (desktop, taskbar, or start menu).
2. Right-click the shortcut → Select **Properties**.
3. In the **Target** field, copy the full path. Example:

   ```
   C:\Users\<YourUsername>\AppData\Local\Google\Chrome\Application\chrome.exe
   ```
4. Open `viewer.py` in a text editor.
5. Replace the `chrome_path` variable with your copied path:

   ```python
   chrome_path = r"C:\Users\<YourUsername>\AppData\Local\Google\Chrome\Application\chrome.exe"
   ```
6. Save the file.

### macOS (Optional)

Chrome is usually installed at:

```
/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```

---

## Usage

Run the script in the terminal:

```bash
python viewer.py
```

You will be prompted for:

* **View Time (sec)** – How long Chrome stays open per cycle.
* **Enter URL** – URL to visit.
* **Views** – Number of times to repeat the process.

Example:

```
View Time (sec): 10
Enter URL: https://example.com
Views: 5
```

The script will:

1. Open Chrome in Incognito mode.
2. Wait 10 seconds.
3. Fully close Chrome.
4. Wait 1 second.
5. Repeat 5 times.

---

## Notes

* Make sure your Chrome path is correct before running.
* The script **kills all Chrome windows** while running, so don’t have important tabs open.
* Adjust the `timed` variable and number of `Views` as needed.
* Works **only on laptops/desktops**, not on mobile devices.

---

## License

MIT License
