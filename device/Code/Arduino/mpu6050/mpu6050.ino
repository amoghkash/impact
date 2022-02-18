#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
//#include 

Adafruit_MPU6050 mpu;

#define blue 27
#define green 23
#define integrated 2 

void setup(void) {
  Serial.begin(115200);
  pinMode(green, OUTPUT); // Green LED
  pinMode(integrated, OUTPUT); // Integrated LED
  pinMode(blue, OUTPUT); // Blue LED
  
  /*while (!Serial)
    delay(10); 
*/
  //Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
      
    }
  }
  //digitalWrite(green, HIGH); //Turn on initializer LED
  //Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  //Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    //Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    //Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    //Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    //Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  //Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    //Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    //Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    //Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    //Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  //Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    //Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    //Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    //Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    //Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    //Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    //Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    //Serial.println("5 Hz");
    break;
  }

  //Serial.println("");
  delay(100);
  
}

void loop() {
  /* Get new sensor events with the readings */
  //digitalWrite(integrated, LOW);
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  float x = a.acceleration.x;
  float y = a.acceleration.y;
  float z = a.acceleration.z;
  /* Print out the values */
  //digitalWrite(integrated, HIGH);
  double vsum;

  vsum = (sqrt(sq(x)+sq(y)+sq(z)));

  Serial.print(vsum - 8.02);

  if(vsum>40){
    digitalWrite(blue, HIGH);
  }
 
  Serial.println("");
  

  
  /*
   Serial.print("X:");
  Serial.print(x);
  Serial.print(", Y:");
  Serial.print(y);
  Serial.print(", Z:");
  Serial.print(z);
  Serial.println("");

   */
}
