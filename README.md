# EN2130 Communication Design Project

## Project Overview

This repository contains the files and code for the **EN2130 Communication Design Project**, focused on building a point-to-point digital wireless communication system using software-defined radios (SDRs).

## Watch the Project Demo

[![Project Demo](http://img.youtube.com/vi/KdEGzrJ_zQ/0.jpg)](http://www.youtube.com/watch?v=KdEGzrJ_zQ)

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

1. **Clone the Repository**:
   - Run the following command to clone the repository:
     ```sh
     git clone https://github.com/NaveenSanjaya/DigitalCommDesign.git
     cd DigitalCommDesign
     ```

2. **Set Up the Environment**:
   - Ensure that you have installed GNU Radio using the Radioconda installer as described earlier.
   - Use **Visual Studio Code (VS Code)** with the **Radioconda interpreter** to run the system.

3. **Run the Home Script**:
   - Locate the `User interface` folder:
   - Run the `home.py` script to start the system:

   - **The `home.py` script serves as the main entry point for the system. From this interface, you can navigate to different modules**:
     - **Transmitter Window**: Configure and start data transmission.
     - **Receiver Window**: Set up the receiver for incoming data.
     - **Video Stream Window**: Stream video over the wireless channel.

4. **Load Flowgraphs in GNU Radio (Optional)**:
   - If you want to directly run specific flowgraphs for debugging or analysis, open GNU Radio Companion (GRC):
   - Load the desired flowgraph:
     - For BPSK: `BPSK_Pkt_Tx_Rx.grc`
     - For QPSK: `QPSK_Pkt_Tx_Rx.grc`
     - For FM: `nuand_transmitter.grc` or `nuand_receiver.grc`

5. **Transmitter and Receiver Demonstration**:
   - **The final demonstration uses the files in the `/Transiver` folder.**

6. **Verify and Adjust**:
   - Monitor the system's performance and make adjustments to parameters (e.g., frequency, gain, sample rate) as needed.

## Additional Topics

### Troubleshooting

- **GNU Radio Companion not opening**: Ensure that GNU Radio is correctly installed and added to your system's PATH.
- **BladeRF device not recognized**: Check the USB connection and ensure that the drivers are correctly installed.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

### Contact

For any questions or issues, please contact the project maintainers at [naveensanjayab@gmail.com](naveensanjayab@gmail.com),[hpelagewatta@gmail.com](hpelagewatta@gmail.com), [nethmiamashamso1671@gmail.com](nethmiamashamso1671@gmail.com).
