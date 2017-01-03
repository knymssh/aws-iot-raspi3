#!/usr/bin/python
# coding: utf-8

import smbus
import time

bus = smbus.SMBus(1)  # I2Cバス番号
address = 0x49  # ADS1015のI2Cアドレス


# I2C data write (1byte)
def write(reg, value):
    bus.write_byte_data(address, reg, value)


# I2C data write (block)
def blockwrite(reg, s):
    bus.write_i2c_block_data(address, reg, s[0:])


# I2C data read (1byte)
def read(reg):
    value = bus.read_byte_data(address, reg)
    return value


# I2C data write (block)
def blockread(reg, value):
    value = bus.read_i2c_block_data(address, reg, value)
    return value


while 1:
    # 初期設定（single,+/-4.096V range(GAIN=1),single-shot mode,1600 sample per sec）
    blockwrite(0x01, [0xC3, 0x83])  # CONFIGレジスタに0xC383を書き込む(AIN0)
    #    blockwrite(0x01, [0xD3,0x83])   #CONFIGレジスタに0xD383を書き込む(AIN1)
    #    blockwrite(0x01, [0xE3,0x83])   #CONFIGレジスタに0xE383を書き込む(AIN2)
    #    blockwrite(0x01, [0xF3,0x83])   #CONFIGレジスタに0xF383を書き込む(AIN3)

    time.sleep(0.01)  # 10ms（A/D変換処理待ちを少しいれる）

    # データ取得
    ad_raw = blockread(0x00, 2)
    # データ整形
    ad_val = ((ad_raw[0] & 0xFF) << 8) | (ad_raw[1] & 0xFF)
    ad_val = ad_val >> 4
    # +/- 4.096Vで11bit分解能（GAIN=1設定）
    ad = ad_val * 4.096 / 2048

    # 表示出力
    print "ad = " + str(ad) + " V"

    time.sleep(1)  # 1秒
