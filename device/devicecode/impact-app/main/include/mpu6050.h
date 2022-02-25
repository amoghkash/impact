#pragma once

#include "driver/i2c.h"


#define mpu6050_address 0x68
#define WHO_AM_I 0x75
#define config 0x1A
#define gyroconfig 0x1B
#define axlconfig 0x1C
#define	ACCEL_XOUT_H 0x3B	
#define	ACCEL_XOUT_L 0x3C
#define	ACCEL_YOUT_H 0x3D
#define	ACCEL_YOUT_L 0x3E
#define	ACCEL_ZOUT_H 0x3F
#define	ACCEL_ZOUT_L 0x40
#define	TEMP_OUT_H 0x41
#define	TEMP_OUT_L 0x42
#define	GYRO_XOUT_H	0x43
#define	GYRO_XOUT_L	0x44	
#define	GYRO_YOUT_H	0x45
#define	GYRO_YOUT_L	0x46
#define	GYRO_ZOUT_H 0x47
#define	GYRO_ZOUT_L 0x48
