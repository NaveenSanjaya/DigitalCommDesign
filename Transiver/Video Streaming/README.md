# Video Streaming on GNU Radio with QPSK

## Overview

This section of the project focuses on video streaming using GNU Radio with QPSK modulation. The transmitter captures video feed from a webcam using VLC, saves it to a file, and repeatedly reads the file using a custom Python block for transmission. The receiver decodes the received signal and directs the video feed to VLC via a UDP sink block for playback.

## Transmitter Configurations for VLC

- **Bit rate**: 400 kbps
- **File type**: Video-MPEG-2+MPGA (TS)

## Installation

To set up your environment for video streaming, install the required software:

### 1. Install VLC Media Player

Download and install VLC Media Player from the [official VLC website](https://www.videolan.org/vlc/).

### 2. Add VLC to System Path

Ensure that VLC is added to your system's PATH so it can be accessed from the command line:
- **Windows**:
  1. Locate the installation directory (e.g., `C:\Program Files\VideoLAN\VLC`).
  2. Add this directory to the system's PATH environment variable.
- **Linux/Mac**:
  VLC is usually added to the PATH by default. If not, ensure the directory containing the `vlc` executable is included in your PATH.


## Running the Applications

Navigate to the `Transiver/Video Streaming` directory and run the desired application:

### Transmitter

To start the video transmitter, run:

```sh
python VideoTransmitter.py
```

### Receiver

To start the video receiver, run:

```sh
python VideoReciver.py
```

## Code Snippet for VLC

### For Ubuntu

```python
cmd = r'vlc v4l2:///dev/video0 --sout="#transcode{vcodec=mp2v,vb=800,scale=0.25,acodec=none,scodec=none}:duplicate{dst=file{dst=./im.ts,no-overwrite},dst=display}" --sout-all --sout-keep'
```

### For Windows

```python
cmd = r'vlc dshow:///dev/video0 --sout="#transcode{vcodec=mp2v,vb=800,scale=1,acodec=none,scodec=none}:duplicate{dst=file{dst=./im.ts,no-overwrite},dst=display}" --sout-all --sout-keep'
```

## Directory Structure

VideoTransmitter.py - Transmitter side code for video streaming.
VideoReciver.py - Receiver side code for video streaming.

## Additional Information

### Troubleshooting

- **Permission Issues**: Ensure you run the command prompt with elevated privileges when installing packages.
- **Missing Packages**: Verify that all required packages are installed by running 

### Contact

For any questions or issues, please contact the project maintainer at [naveensanjayab@gmail.com](naveensanjayab@gmail.com).
