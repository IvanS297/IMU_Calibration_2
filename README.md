# IMU Calibration 2

Calibration and orientation estimation for the **HMC5883L** magnetometer and **MPU6050** IMU using Python. This project provides scripts to calibrate the magnetometer, compute heading, fuse sensor data with a Kalman filter, and visualize the results with Pygame.

---

## Files Overview

- **hmc5883.py** – Basic driver for HMC5883L magnetometer.
- **hmc5883_calibr.py** – Performs hard‑iron calibration and saves parameters.
- **hmc5883_calibrated.py** – Reads calibration data and outputs corrected magnetometer readings.
- **hmc5883_heading.py** – Computes heading (yaw) from calibrated magnetometer data.
- **hmc5883_mpu6050.py** – Combines magnetometer with MPU6050 accelerometer/gyroscope.
- **mpu6050.py** – Basic driver for MPU6050.
- **kfs360.py** – Kalman filter implementation for sensor fusion.
- **pygame_hmc5883.py** – Visualises raw/calibrated magnetometer data with Pygame.
- **pygame_hmc5883_mpu6050.py** – Visualises combined data from magnetometer and MPU6050.
- **pygame_hmc5883_mpu6050_kfs360.py** – Visualises fused orientation using Kalman filter.
- **HMC5883L_calibr.txt** – Example calibration data file (hard‑iron offsets).
- **compas.png** – Compass image used in Pygame visualisations.

---

## Dependencies

Install the required Python libraries:

```bash
pip install smbus2 pygame numpy
```
For Raspberry Pi, smbus2 provides I²C communication. On other platforms, adjust the I²C library accordingly.

---

## Usage
- Calibrate the magnetometer:
Run hmc5883_calibr.py and rotate the sensor slowly in all directions. The script will compute hard‑iron offsets and save them to calibration_data.npy.
- Test calibrated heading:
Execute hmc5883_calibrated.py to verify the calibration. Then hmc5883_heading.py will display the heading angle.
- Visualise with Pygame:
Choose one of the Pygame scripts, e.g.:
```bash
python pygame_hmc5883_mpu6050_kfs360.py
```
This will show a real‑time compass needle fused with gyroscope data using the Kalman filter.

---

## Hardware Setup
- Connect HMC5883L to I²C pins (SDA, SCL) and power (3.3V/5V).
- Connect MPU6050 to the same I²C bus.
- Ensure I²C is enabled on your platform (e.g. raspi-config on Raspberry Pi).

---

## Notes
- The I²C address for HMC5883L is typically 0x1E; for MPU6050 it is 0x68. Change them in the scripts if different.
- Calibration must be done before using the fused orientation scripts.

---

## License
This project is open source. Feel free to use and modify the code.
