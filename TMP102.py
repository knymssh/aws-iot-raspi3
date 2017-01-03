#!/usr/bin/python
# coding: utf-8

import smbus
import time

bus = smbus.SMBus(1)  # I2Cバス番号
address = 0x48  # TMP102のI2Cアドレス


# I2C data write (1byte)
def write(reg, value):
    bus.write_byte_data(address, reg, value)


# I2C data read (1byte)
def read(reg):
    value = bus.read_byte_data(address, reg)
    return value


# I2C data write (block)
def blockread(reg, value):
    value = bus.read_i2c_block_data(address, reg, value)
    return value


while 1:
    temp_raw = blockread(0x00, 2)  # I2Cで温度データ(2byte)を取得
    # 温度データを整形
    temp = ((temp_raw[0] << 8) | temp_raw[1]) >> 4
    # 分解能（0.0625℃）倍する
    temp = temp * 0.0625
    # 表示出力
    print("temp = " + str(temp) + "*C")

    time.sleep(1)  # 1秒
