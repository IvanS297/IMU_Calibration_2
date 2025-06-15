#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hmc5883 import *

compass = hmc5883l()

# calibration data
compass.calibration_matrix = [  [1.152886, 0.024759, 0.017571],
			[0.024759, 1.132549, -0.030021],
			[0.017571, -0.030021, 1.232850]]
compass.bias = [30.797967, -93.492117, -78.505766]

while True:
	print(compass.get_calibrated())
