# ssb
<img src="assets/app.svg" alt="ssb" width="100px">

**simple server blocker** - A simple desktop tool built generate and apply outbound firewall rules based on a dataset of IP addresses.

## How to Use

1. **Load a dataset**

    Select a JSON file containing categorized server/IP data.

2. **(Optional) Select an executable**

   Choose a program if you want the firewall rules to apply only to a specific application, if left empty, rules will apply system-wide.

3. **Select which servers you want to use(everything else will be blacklisted)**

4. **Apply the rules**

   Click **`Select Servers`**

5. **Toggle rules on/off**

   The button will switch to **`Unselect Servers`**, allowing you to quickly remove the applied rules.

6. **Clean up all server rules**

   Click **`Cleanup all Server Rules`** to remove all rules created by the tool.

7. **Monitor active rules**

   The UI displays the number of currently active custom firewall rules.

## Dataset Samples
<a href="https://pastebin.com/Zmh02Gnk">https://pastebin.com/Zmh02Gnk</a>

<a href="https://pastebin.com/wx0ubK5q">https://pastebin.com/wx0ubK5q</a>
## Build
Make sure you have [python3](https://www.python.org/downloads/) installed on your system.
### 1. Install PyInstaller

```bat
pip install pyinstaller
```

---

### 2. Run the build script

```bat
build.bat
```

---

### 3. Output

```text
dist\
└── ssb.exe
```

## Screenshots
![Selecting dataset](assets/screenshot1.png)
![Selecting EU Servers (Blocking US ones)](assets/screenshot2.png)
![Activating rules](assets/screenshot3.png)
## Donate
Donate to support me and my projects

### PayPal
<a href="https://paypal.me/raafaa99">
   <img src="https://www.paypalobjects.com/marketing/web/logos/paypal-mark-color_new.svg" alt="PayPal" width="100px">
</a>

### Bitcoin
<a href="assets/bitcoin.png">
   <img src="assets/bitcoin.png" alt="Bitcoin" width="100px">
</a>

(1MvzcDqAVfuQLYZKNCcBoVNYe2neta3pkM)

### Monero
<a href="assets/monero.png">
   <img src="assets/monero.png" alt="Monero" width="100px">
</a>

(4254FmcCGBNbaq9CcqkUSk8eY3cqACjrGXRWkxXxXbjD1Up3Nu4BsCA1YCkrnrzG4SUmwDJQnBYJoeLrucWSDRhyRchRAHP)

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

ssb is Free Software: You can use, study, share, and improve it at will. Specifically you can redistribute and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl.html) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
