#!/usr/bin/env python
# -*- coding:utf-8 -*-
from data.push import sendToTraveler, sendToDriver
import pytest


def test_sendToTraveler():
    traveler = sendToTraveler()
    print(traveler)


def test_sendToDriver():
    diver = sendToDriver()
    print(diver)
