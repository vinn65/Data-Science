/*
This code records the temperature through testing the mV put out by the sensor.
It records in both Celcius and Fahrenheit. 
It can only detect from -40 degrees C to 125 degrees C or -40 degrees F 
to 257 degrees F
The Humidity is simulated by a potentiometer by being mapped into percentages
*/
const int temp_SENSOR_PIN = A0; // Set the analog input pin for the temp sensor
int humiditySensorOutput = 0; // Declare a variable to store the output of the humidity sensor

int Read_Value = 0; // Declare a variable to store the raw value from the temp sensor
double volt = 0; // Declare a variable to store the volt calculated from the raw value
double tempC = 0; // Declare a variable to store the temp in Celsius
double tempF = 0; // Declare a variable to store the temp in Fahrenheit

void setup() {  
  Serial.begin(9600); // Start serial communication with a baud rate of 9600
  pinMode(A1, INPUT); // Set the A1 pin as input
}

void loop() {
  Read_Value = analogRead(temp_SENSOR_PIN); // Read the raw value from the temp sensor
  volt = (Read_Value / 1023.0) * 5000; // Convert the raw value to millivolts
  tempC = (volt - 500) * 0.1; // Convert millivolts to Celsius temp with an offset of 500
  tempF = (tempC * 1.8) + 32; // Convert Celsius temp to Fahrenheit
  
  // Print the raw value, millivolts, temp in Celsius, and temp in Fahrenheit to the serial monitor
  Serial.print("Value read = " );                  
  Serial.print(Read_Value);      
  Serial.print("\t milli volts = ");
  Serial.print(volt, 0); // Print voltage without decimal places
  Serial.print("\t temperature(C)) = ");
  Serial.print(tempC, 1); // Print temp in Celsius with 1 decimal place
  Serial.print("\t temperature(F)) = ");
  Serial.println(tempF, 1); // Print temp in Fahrenheit with 1 decimal place
  
  humiditySensorOutput = analogRead(A1); // Read the output from the humidity sensor
  int humidityPercentage = map(humiditySensorOutput, 0, 1023, 10, 70); // Map the humidity output to a percentage value between 10 and 70
  // Print the humidity percentage to the serial monitor
  Serial.print("Humidity: ");
  Serial.print(humidityPercentage);
  Serial.println("%");

  delay(5000);  // Wait for 5 seconds before repeating the loop
}
