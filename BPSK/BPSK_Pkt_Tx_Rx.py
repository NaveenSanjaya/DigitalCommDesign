#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BPSK_Pkt_Tx_Rx
# Author: tharoosha
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import filter
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import BPSK_Pkt_Tx_Rx_epy_block_0 as epy_block_0  # embedded python block
import sip



class BPSK_Pkt_Tx_Rx(gr.top_block, Qt.QWidget):

    def __init__(self, MTU=1500, puncpat='11'):
        gr.top_block.__init__(self, "BPSK_Pkt_Tx_Rx", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK_Pkt_Tx_Rx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "BPSK_Pkt_Tx_Rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Parameters
        ##################################################
        self.MTU = MTU
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 600000
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.access_key = access_key = '11100001010110101110100010010011'
        self.usrp_rate = usrp_rate = 768000
        self.thresh = thresh = 1
        self.sps = sps = 4
        self.rs_ratio = rs_ratio = 1.040
        self.phase_bw = phase_bw = 0.0628
        self.low_pass_filter_taps = low_pass_filter_taps = firdes.low_pass(1.0, samp_rate, 20000,2000, window.WIN_HAMMING, 6.76)
        self.hdr_format = hdr_format = digital.header_format_default(access_key, 0)
        self.file_name = file_name = ''
        self.excess_bw = excess_bw = 1
        self.enc_cc = enc_cc = fec.cc_encoder_make((MTU*8),k, rate, polys, 0, fec.CC_TAILBITING, True)
        self.dec_cc = dec_cc = list(map( (lambda a: fec.cc_decoder.make((MTU*8),k, rate, polys, 0, (-1), fec.CC_TAILBITING, True)),range(0,1)))
        self.bpsk = bpsk = digital.constellation_bpsk().base()
        self.arity = arity = 2

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self._file_name_tool_bar = Qt.QToolBar(self)
        self._file_name_tool_bar.addWidget(Qt.QLabel("'file_name'" + ": "))
        self._file_name_line_edit = Qt.QLineEdit(str(self.file_name))
        self._file_name_tool_bar.addWidget(self._file_name_line_edit)
        self._file_name_line_edit.returnPressed.connect(
            lambda: self.set_file_name(str(str(self._file_name_line_edit.text()))))
        self.top_layout.addWidget(self._file_name_tool_bar)
        self.fec_extended_tagged_encoder_0_1 = fec.extended_tagged_encoder(encoder_obj_list=enc_cc, puncpat='11', lentagname="packet_len", mtu=MTU)
        self.fec_extended_tagged_decoder_2 = self.fec_extended_tagged_decoder_2 = fec_extended_tagged_decoder_2 = fec.extended_tagged_decoder(decoder_obj_list=dec_cc, ann=None, puncpat=puncpat, integration_period=10000, lentagname="packet_len", mtu=MTU)
        self.epy_block_0 = epy_block_0.blk(FileName='tx.jpg', Pkt_len=60)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_MUELLER_AND_MULLER,
            sps,
            phase_bw,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [12])
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_map_bb_0_0 = digital.map_bb([-1, 1])
        self.digital_map_bb_0 = digital.map_bb([0,1])
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_crc32_bb_0_0 = digital.crc32_bb(True, "packet_len", True)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, "packet_len", True)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, True)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts("11100001010110101110100010010011",
          thresh, 'packet_len')
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=bpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(bpsk)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=0.0,
            frequency_offset=0.0,
            epsilon=1.0,
            taps=[1.0 + 1.0j],
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_repack_bits_bb_1_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, './output.tmp', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_char_to_float_1_1 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_1, 0), (self.fec_extended_tagged_decoder_2, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_extended_tagged_encoder_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0, 0), (self.digital_crc32_bb_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_1_1, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.fec_extended_tagged_decoder_2, 0), (self.blocks_repack_bits_bb_1_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.blocks_repack_bits_bb_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BPSK_Pkt_Tx_Rx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_low_pass_filter_taps(firdes.low_pass(1.0, self.samp_rate, 20000, 2000, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_hdr_format(digital.header_format_default(self.access_key, 0))

    def get_usrp_rate(self):
        return self.usrp_rate

    def set_usrp_rate(self, usrp_rate):
        self.usrp_rate = usrp_rate

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_rs_ratio(self):
        return self.rs_ratio

    def set_rs_ratio(self, rs_ratio):
        self.rs_ratio = rs_ratio

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0.set_loop_bandwidth(self.phase_bw)

    def get_low_pass_filter_taps(self):
        return self.low_pass_filter_taps

    def set_low_pass_filter_taps(self, low_pass_filter_taps):
        self.low_pass_filter_taps = low_pass_filter_taps

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name
        Qt.QMetaObject.invokeMethod(self._file_name_line_edit, "setText", Qt.Q_ARG("QString", str(self.file_name)))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk
        self.digital_constellation_decoder_cb_0.set_constellation(self.bpsk)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--MTU", dest="MTU", type=intx, default=1500,
        help="Set MTU [default=%(default)r]")
    return parser


def main(top_block_cls=BPSK_Pkt_Tx_Rx, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(MTU=options.MTU)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()