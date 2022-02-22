#include <WiFi.h>
#include <WiFiUdp.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>



/* WiFi network name and password */
const char * ssid = "Magellanic";
const char * pwd = "3014016951";

// IP address to send UDP data to.
// it can be ip address of the server or 
// a network broadcast address
// here is broadcast address
const char * udpAddress = "192.168.1.154";
const int udpPort = 3333;

//create UDP instance
WiFiUDP udp;
// Create MPU instance
Adafruit_MPU6050 mpu; 

// Set LED Pin
#define led 2 


void setup(){
  Serial.begin(115200);

  pinMode(led, OUTPUT); // Set LED as output

  
  //Connect to the WiFi network
  WiFi.begin(ssid, pwd);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(led, HIGH);
    delay(300);
    Serial.print(".");
    digitalWrite(led, LOW);
    delay(100);
  }
  digitalWrite(led, LOW);
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  delay(500);
  digitalWrite(led, HIGH);

  // Look for MPU Chip
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  } else {
    Serial.println("Chip Found");
  }
  
  // Set MPU Chip Sensitivity Values
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
}


void loop(){
  
  // Get Data from MPU6050 Sensor
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Set Data from Sensor to variables
  float rawx = a.acceleration.x;
  float rawy = a.acceleration.y;
  float rawz = a.acceleration.z;

  // Convert floats into ints
  int x = rawx * 100;
  int y = rawy * 100;
  int z = rawz * 100;

  // Create char variables to hold sent values
  char xval[10];
  char yval[10];
  char zval[10];

  // Save integer data as ASCII Character into char variable
  itoa(x, xval, 10);
  itoa(y, yval, 10);
  itoa(z, zval, 10);
  
  /*
  // Print Values for Error Checking
  Serial.println(xval);
  Serial.println(yval);
  Serial.println(zval);
  */
  
  //Buffer Data to seperate values
  uint8_t buffer[1] = {};
  

  //This initializes udp and transfer buffer
  udp.beginPacket(udpAddress, udpPort);
  udp.write(buffer,1);
  int i = 0;
  while (xval[i] != 0) {
    //udp.write(buffer, 11);
    udp.write((uint8_t)xval[i++]);
  }
  udp.write(buffer,1);
  i = 0;
  while (yval[i] != 0) {
    udp.write((uint8_t)yval[i++]);
  }
  udp.write(buffer,1);
  i = 0;
  while (zval[i] != 0) {
    udp.write((uint8_t)zval[i++]);
  }
  //udp.write(buffer, 11);
  udp.endPacket();
  memset(buffer, 0, 50);
  //processing incoming packet, must be called before reading the buffer
  udp.parsePacket();
  //receive response from server, it will be HELLO WORLD
  if(udp.read(buffer, 50) > 0){
    Serial.print("Server to client: ");
    Serial.println((char *)buffer);
  }
  //Wait for 1 second
  delay(1);
}





