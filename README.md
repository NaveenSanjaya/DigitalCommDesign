# EN2130 Communication Design Project

## Project Overview

This repository contains the files and code for the **EN2130 Communication Design Project**, focused on building a point-to-point digital wireless communication system using software-defined radios (SDRs).

### Key Features

- **Transmission of Images, Voice, and Video** over a wireless channel.
- Communication in the **2.4 GHz ISM band**, adhering to power limitations.
- Utilizes **BladeRF A9 and A4 devices** for transmission and reception.
- Performance evaluation based on:
  - Distance
  - End-to-end delay

### Optional Features (to be implemented)

- **Security** features for secure communication.
- **Channel estimation** to improve transmission quality.
- **Adaptive transmission** to optimize performance under varying conditions.

## Project Structure

- `/src` - Contains source code for the system.
- `/docs` - Documentation related to system design and implementation.
- `/tests` - Test scripts for evaluating system performance.
- `/media` - Example image, voice, and video files for transmission.
- `/BPSK` - Contains BPSK modulation related files.
- `/FM` - Contains FM modulation related files.
- `/QPSK` - Contains QPSK modulation related files.
- `/temp` - Temporary files and scripts.
- **`/Transiver` - Contains the files used for the final demonstration of the system.**
- `/User interface` - User interface related files.

## Usage

### 1. Installing GNU Radio on Windows

To install GNU Radio on Windows, follow these steps:

1. Download the GNU Radio installer from [Radioconda](https://github.com/ryanvolz/radioconda?tab=readme-ov-file) or follow this [link](https://glare-sable.vercel.app/ryanvolz/radioconda/radioconda-.*-Windows-x86_64.exe).
2. Run the installer and follow the on-screen instructions to complete the installation.
3. Launch the GNU Radio Companion (GRC) graphical interface from the start menu.

For additional information and installation instructions on other operating systems, refer to the official GNU Radio documentation [here](https://wiki.gnuradio.org/index.php/InstallingGR).

### 2. Installing Drivers for BladeRF Devices (For Windows users)

This project utilizes **BladeRF A9** and **BladeRF A4** devices. Below are the separate instructions for installing drivers for each device.

#### 2.1. Installing Drivers for BladeRF A9

To install drivers for the BladeRF A9, follow these steps:

1. **Download the BladeRF A9 Driver:**
   - Visit the [Nuand BladeRF Downloads](https://github.com/Nuand/bladeRF/releases/tag/2024.05) page.
   - Locate the **BladeRF A9** section and download the appropriate Windows installer (e.g., `bladeRF-win-installer-2024.05.exe`).
    
2. **Connect the BladeRF A9 Device:**
   - Use a USB cable to connect your BladeRF A9 device to your computer.
   - Ensure the device is securely connected.
    
3. **Run the Installer:**
   - Double-click the downloaded installer file.
   - Follow the on-screen instructions to install the BladeRF A9 drivers and associated software.

#### 2.2. Installing Drivers for BladeRF A4

To install drivers for the BladeRF A4, follow these steps:

1. Download and run [Zadig](https://zadig.akeo.ie/)
2. Select your device (It may be auto-selected since it is missing a driver)
3. Ensure the target driver (middle of the interface) reads "WinUSB"
4. Click "Install Driver" or "Replace Driver"

For additional information follow this [link](https://github.com/ryanvolz/radioconda?tab=readme-ov-file#bladerf)

### 3. How to Start Working

To start working with the project, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/NaveenSanjaya/DigitalCommDesign.git
   cd DigitalCommDesign
   ```

2. **Open GNU Radio Companion (GRC)**:
   ```sh
   gnuradio-companion
   ```

3. **Load the desired flowgraph**:
   - For BPSK, open: BPSK_Pkt_Tx_Rx.grc

.
   - For QPSK, open: QPSK_Pkt_Tx_Rx.grc

.
   - For FM, open: nuand_transmitter.grc or nuand_reciver.grc

4. **Configure the flowgraph**:
   - Set the appropriate parameters such as sample rate, frequency, and gain.
   - Ensure that the BladeRF device is selected as the source or sink.

5. **Run the flowgraph**:
   - Click the "Run" button in GRC to start the flowgraph.
   - Monitor the output and make adjustments as necessary.

6. **Transmit and Receive Data**:
   - Use the provided user interface scripts in the `User interface` directory to transmit and receive data.
   - For example, run `User interface/transmitterUIDummy.py` to start the transmitter UI.

## Additional Topics

### Troubleshooting

- **GNU Radio Companion not opening**: Ensure that GNU Radio is correctly installed and added to your system's PATH.
- **BladeRF device not recognized**: Check the USB connection and ensure that the drivers are correctly installed.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the GPL-3.0 License. See the LICENSE file for more details.

### Contact

For any questions or issues, please contact the project maintainers at [email@example.com](mailto:email@example.com).
```

This `README.md` provides a comprehensive overview of the project, key features, optional features, project structure, and detailed usage instructions, including installing GNU Radio, installing BladeRF drivers, and starting to work with the project.
This `README.md` provides a comprehensive overview of the project, key features, optional features, project structure, and detailed usage instructions, including installing GNU Radio, installing BladeRF drivers, and starting to work with the project.
