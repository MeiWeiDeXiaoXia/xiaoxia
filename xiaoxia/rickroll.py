# -*- coding: utf-8 -*-
# Copyright (c) 2026 MeiWeiDeXiaoXia
# SPDX‑License‑Identifier: MIT
# Gitee: https://gitee.com/MeiWeiDeXiaoXia
# Bilibili: https://space.bilibili.com/499985403

"""
你被骗了！
xiaoxia 模块 - rickroll 彩蛋
自用Python小工具集合
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.withdraw()


question = messagebox.askyesno("Rickroll", "我这里有一个很好玩的东西，你要不要来看看？")
if question:
    rick = webbrowser.open("https://www.bilibili.com/video/BV1GJ411x7h7", new=1, autoraise=True)
    if rick:
        messagebox.showinfo("Rickroll", "你被骗了")
    else:
        messagebox.showerror("RickRoll", "被反诈中心拦截力（悲）")
else:
    messagebox.showerror("Rickroll", "不看也得看")