"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import os
from gnuradio import gr
import time
import subprocess

class blk(gr.sync_block):  
    """Play video using VLC while it is being written"""

    def __init__(self, video_path="/home/gnuradio/Documents/DigitalCommDesign/video/video_rx.ts"):  
        gr.sync_block.__init__(
            self,
            name='Real-time VLC Video Player', 
            in_sig=None, 
            out_sig=None
        )
        self.video_path = video_path
        self.playing = False

    def work(self, input_items, output_items):
        if not self.playing and os.path.exists(self.video_path):
            self.playing = True
            print(f"Opening VLC to play: {self.video_path}")
            try:
                subprocess.Popen(["cvlc", "--play-and-exit", self.video_path])
            except Exception as e:
                print(f"Failed to open VLC: {e}")
                self.playing = False
        time.sleep(1)
        return len(output_items[0]) if output_items else 0
