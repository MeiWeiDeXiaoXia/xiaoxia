# -*- coding: utf-8 -*-
# Copyright (c) 2026 MeiWeiDeXiaoXia
# SPDX‑License‑Identifier: MIT
# Gitee: https://gitee.com/MeiWeiDeXiaoXia/xiaoxia
# Bilibili: https://space.bilibili.com/499985403

"""
xiaoxia 模块主入口
自用Python小工具集合
"""

import time
import webbrowser
from pynput import keyboard
import subprocess

# ==============================================================================
# Nuke() 函数：完整复制自 B站视频 BV1Tc9FYQEx6，作者 Alanbecker
# 原始视频链接：https://www.bilibili.com/video/BV1Tc9FYQEx6
# 说明：视频未提供明确开源许可证，仅限学习、演示用途，禁止商用
# 详见仓库根目录 THIRD_PARTY_LICENSES.md
# ==============================================================================
def Nuke(n):
	a = []
	for i in range(10):
		if n > 1:
			a.append(Nuke(n - 1))
		else:
			a.append(i)
	return a

import math


def isPrime(n: int) -> bool:
    """
    综合素数判断：
    小数用优化试除法，大数自动切换Miller-Rabin(2^64以内完全准确)
    兼容 Python 3.6+
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    TRIAL_THRESHOLD = 1000000
    if n <= TRIAL_THRESHOLD:
        max_div = int(math.sqrt(n))
        # 校正浮点数平方根误差
        while (max_div + 1) * (max_div + 1) <= n:
            max_div += 1
        while max_div * max_div > n:
            max_div -= 1

        for i in range(3, max_div + 1, 2):
            if n % i == 0:
                return False
        return True
    else:
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for a in bases:
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

def DepSaak():
	while True:
		str = input("你想说什么？\n")
		if str == "exit":
			break
		else:
			time.sleep(5)
			print("服务器繁忙，请稍后再试")
			subprocess.run("pause", shell=True)
			

def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fact(n - 1)
	
def pow(a, b):
	if b == 0:
		return 1
	else:
		return a * pow(a, b - 1)

def fib(n):
	if not isinstance(n, int) or n < 0:
		raise ValueError("n 必须是非负整数")
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

def hello():
	print("Hello, World!")

def openurl(url):
	webbrowser.open(url)

def myspace(site: str):
	if site == "bili":
		webbrowser.open("https://space.bilibili.com/499985403")
	elif site == "gitee":
		webbrowser.open("https://gitee.com/MeiWeiDeXiaoXia")
	else:
		webbrowser.open("https://space.bilibili.com/499985403")

def timeout(sec: int):
	stop_flag = False

	# 按键回调函数
	def on_press(key):
		nonlocal stop_flag
		stop_flag = True
		return False
	remain = sec
	listener = keyboard.Listener(on_press=on_press)
	listener.start()
	while remain > 0:
		if stop_flag:
			listener.stop()
			print()  # 换行防止文字重叠
			return
		print(f"等待 {remain} 秒，按任意键继续", end="\r")
		time.sleep(1)
		remain -= 1
	listener.stop()
	print(f"\r等待 0 秒，按任意键继续")
	return

def mathMachine1(n):
	return 0

def mathMachine2(n):
	return n

def mathMachine3(n):
	return n * n

def sigma(start, stop, step, expr: str):
    total = 0
    x = start
    while x <= stop:
        total += eval(expr)
        x += step
    return total
