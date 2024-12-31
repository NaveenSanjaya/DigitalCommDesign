# Video Streaming on GNU Radio with QPSK

## Overview

This section of the project focuses on video streaming using GNU Radio with QPSK modulation. The transmitter captures video from a camera, encodes it, and transmits it over the air. The receiver decodes the received signal and plays the video.

## Transmitter Configurations for VLC

- **Bit rate**: 400 kbps
- **File type**: Video-MPEG-2+MPGA (TS)

## Installation

To run the video streaming applications, you need to install the required Python packages and GNU Radio. Follow the steps below to set up your environment:

### 1. Install VLC Media Player

Download and install VLC Media Player from the [official VLC website](https://www.videolan.org/vlc/).

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

- 

VideoTransmitter.py

 - Transmitter side code for video streaming.
- 

VideoReciver.py

 - Receiver side code for video streaming.

## Additional Information

### Troubleshooting

- **Permission Issues**: Ensure you run the command prompt with elevated privileges when installing packages.
- **Missing Packages**: Verify that all required packages are installed by running 

pip list

.

### Contact

For any questions or issues, please contact the project maintainer at [email@example.com](mailto:email@example.com).
```

This `README.md` provides an overview of the video streaming part, installation instructions, running instructions, and the necessary VLC command snippets for both Ubuntu and Windows.
This `README.md` provides an overview of the video streaming part, installation instructions, running instructions, and the necessary VLC command snippets for both Ubuntu and Windows.