# -*- coding: utf-8 -*-
# Copyright (c) 2026 MeiWeiDeXiaoXia
# SPDX‑License‑Identifier: MIT

from decimal import Decimal

def circle_area(radius: Decimal) -> Decimal:
	return Decimal("3.1415926535897932384626433832795") * radius ** 2

def circle_circumference(radius: Decimal) -> Decimal:
	return Decimal("3.1415926535897932384626433832795") * radius * 2