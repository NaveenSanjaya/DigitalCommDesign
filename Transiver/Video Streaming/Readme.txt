UDP server: udp://@224.2.2.1:9000

For OBS: udp://@172.26.160.1:9000?pkt_sie=1316


gstreamer upstream: gst-launch-1.0 ksvideosrc ! videoconvert ! x264enc tune=zerolatency ! mpegtsmux ! udpsink host=127.0.0.1 port=5000

gstreamer downstream: gst-launch-1.0 udpsrc port=5000 ! tsdemux ! h264parse ! avdec_h264 ! videoconvert ! autovideosink