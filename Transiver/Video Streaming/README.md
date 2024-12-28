# video_streaming_on_gnu_radio_with_QPSK

## Transmitter Configurations for VLC
* Bit rate :- 400kbps
* File type:- Video-MPEG-2+MPGA(TS)

## code snippett
* For Ubuntu - cmd = r'vlc v4l2:///dev/video0 --sout="#transcode{vcodec=mp2v,vb=800,scale=0.25,acodec=none,scodec=none}:duplicate{dst=file{dst=./im.ts,no-overwrite},dst=display}" --sout-all --sout-keep'
* For Windows - cmd = r'vlc dshow:///dev/video0 --sout="#transcode{vcodec=mp2v,vb=800,scale=1,acodec=none,scodec=none}:duplicate{dst=file{dst=./im.ts,no-overwrite},dst=display}" --sout-all --sout-keep'