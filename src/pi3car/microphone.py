#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# test_microphone.py
# Using STT to check the microphone is avaiable
#
# Author : sosorry
# Date   : 09/13/2014

import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=5)
    print('Say something>>> ')
    audio=r.listen(source)

try:
    print('Google Speech Recognition thinks you said:')
    sent = r.recognize_google(audio, language="zh-TW")

    print("\nUnicode sentence")
    print("===================================")
    print(type(sent), len(sent), sent)

    print("\nUTF-8 sentence")
    print("===================================")
    token = sent.encode('utf-8')
    print(type(token), len(token), token)
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print('No response from Google Speech Recognition service: {0}'.format(e))
