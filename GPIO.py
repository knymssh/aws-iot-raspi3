#!/usr/bin/python
# coding: utf-8

# モジュールをインポート
import RPi.GPIO as GPIO
import time

# GPIO番号で指定
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)  # 21 - LED1
GPIO.setup(20, GPIO.OUT)  # 20 - LED2
GPIO.setup(7, GPIO.IN)  # 7  - SW1
GPIO.setup(8, GPIO.IN)  # 8  - SW2

while 1:
    GPIO.output(21, 1)  # 21番ピンをH（3.3V）にする＝LED1点灯
    GPIO.output(20, 0)  # 20番ピンをL（0.0V）にする＝LED2消灯
    print "SW1=",
    print GPIO.input(7)  # 7番ピンの状態を出力
    print "SW2=",
    print GPIO.input(8)  # 8番ピンの状態を出力

    time.sleep(1)  # 1秒待つ

    GPIO.output(21, 0)  # 21番ピンをH（3.3V）にする＝LED1点灯
    GPIO.output(20, 1)  # 20番ピンをL（0.0V）にする＝LED2点灯

    time.sleep(1)  # 1秒待つ
