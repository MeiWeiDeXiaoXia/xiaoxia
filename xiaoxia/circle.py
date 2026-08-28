# -*- coding: utf-8 -*-
# Copyright (c) 2026 MeiWeiDeXiaoXia
# SPDX‑License‑Identifier: MIT
# Gitee: https://gitee.com/MeiWeiDeXiaoXia
# Bilibili: https://space.bilibili.com/499985403

"""
xiaoxia 模块 - circle 子模块
自用Python小工具集合
"""

from decimal import Decimal

def circle_area(radius: Decimal) -> Decimal:
	return Decimal("3.1415926535897932384626433832795") * radius ** 2

def circle_circumference(radius: Decimal) -> Decimal:
	return Decimal("3.1415926535897932384626433832795") * radius * 2