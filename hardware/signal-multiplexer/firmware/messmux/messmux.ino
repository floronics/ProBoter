


#define LED1 A2 //Green
#define LED2 A3 // RED
#define LED3 A4 // GREEN

#define A_SELECT A0 //Switches Channel Analog Output A
#define B_SELECT 3 //Switches Channel Analog Output B

#define I1_SELECT A1   //Switches Input 1 to A or to Digital
#define I2_SELECT 13  //Switches Input 2 to A or to Digital
#define I3_SELECT 4   //Switches Input 3 to B or to Digital
#define I4_SELECT 2   //Switches Input 4 to B or to Digital87978

#define PULL_D4 9
#define PULL_D3 10
#define PULL_D2 11
#define PULL_D1 12

#define TEST1 8
#define TEST2 7
#define TEST3 6
#define TEST4 5

const char* str = "switchA";


void setup() {
  // put your setup code here, to run once:
  pinMode(LED1, OUTPUT); 
  digitalWrite(LED1,HIGH); 
  
   pinMode(LED2, OUTPUT); 
  digitalWrite(LED2,LOW);

   pinMode(LED3, OUTPUT); 
  digitalWrite(LED3,HIGH);

  pinMode(A_SELECT, OUTPUT); 
  pinMode(B_SELECT, OUTPUT); 
  pinMode(I1_SELECT, OUTPUT); 
  pinMode(I2_SELECT, OUTPUT); 
  pinMode(I3_SELECT, OUTPUT); 
  pinMode(I4_SELECT, OUTPUT);

  digitalWrite(A_SELECT, LOW); 
  digitalWrite(B_SELECT, LOW); 
  digitalWrite(I1_SELECT, HIGH); 
  digitalWrite(I2_SELECT, LOW); 
  digitalWrite(I3_SELECT, HIGH); 
  digitalWrite(I4_SELECT, LOW);

  pinMode(PULL_D1, OUTPUT);
  pinMode(PULL_D2, OUTPUT); 
  pinMode(PULL_D3, OUTPUT); 
  pinMode(PULL_D4, OUTPUT); 
  
  digitalWrite(PULL_D1,LOW);
  digitalWrite(PULL_D2,LOW);
  digitalWrite(PULL_D3,LOW); 
  digitalWrite(PULL_D4,LOW); 
   

  pinMode(TEST1, INPUT); 
  pinMode(TEST2, INPUT); 
  pinMode(TEST3, INPUT); 
  pinMode(TEST4, INPUT); 



  Serial.begin(9600);
   Serial.print("Funkyswitch 1.0 ready\r\n");
}


String readLine(){
  String readString;
    while (1) {
    delay(3);  //delay to allow buffer to fill
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      if(c == '\r' || c == '\n'){
        Serial.print("\r\n");
        return readString;
      }else{
        Serial.write(c);
      }
      readString += c; //makes the string readString
    }
  }
}

int cmp(String s1, String s2){
  int len = min(s1.length(),s2.length());
  for(int i = 0; i < len; i++){
    if(s1[i] != s2[i]){
      return 0;
    }
  }
  return 1;
}


void loop() {
  while(true){
  delay(100);
  String line = readLine();
  if(line[0] == '\n' || line[0] == '\r'){
    continue;
  }
  if(cmp(line,"switchA")){
    if(line[8] == '1'){
      digitalWrite(I1_SELECT, LOW);
      digitalWrite(I2_SELECT, LOW);
      digitalWrite(A_SELECT,HIGH);
      Serial.print("done\r\n");
      continue;
    }else if(line[8] == '2'){
      digitalWrite(I1_SELECT, HIGH);
      digitalWrite(I2_SELECT, HIGH); 
      digitalWrite(A_SELECT,LOW);
      Serial.print("done\r\n");
      continue;
    }else{
      Serial.print("invalid command\r\n");
      continue;
    }  
  }

  else if(cmp(line,"switchB")){
    if(line[8] == '3'){
      digitalWrite(I3_SELECT, LOW);
      digitalWrite(I4_SELECT, LOW);
      digitalWrite(B_SELECT,HIGH);
      Serial.print("done\r\n");
      continue;
    }else if(line[8] == '4'){
      digitalWrite(I3_SELECT, HIGH);
      digitalWrite(I4_SELECT, HIGH);
      digitalWrite(B_SELECT,LOW);
      Serial.print("done\r\n");
      continue;
    }else{
      Serial.print("invalid command\r\n");
      continue;
    }  
  }

  else if(cmp(line,"switchDigital")){
    switch(line[14]) {
      case '1': 
            digitalWrite(I1_SELECT, HIGH);
            Serial.print("done\r\n");
            break;
      case '2':
            digitalWrite(I2_SELECT, LOW);
            Serial.print("done\r\n");
            break;
      case '3':
            digitalWrite(I3_SELECT, HIGH);
            Serial.print("done\r\n");
            break;
      case '4':
            digitalWrite(I4_SELECT, LOW);
            Serial.print("done\r\n");
            break;
      default:
            Serial.print("invalid command\r\n");
            break;
    }
    continue;
  }

    else if(cmp(line,"getSwitchStates")){
      if(digitalRead(I1_SELECT)){
        Serial.print("D ");
      }else{
        if(digitalRead(A_SELECT)){
          Serial.print("A ");
        }else{
          Serial.print("N ");
        }
      }

      if(!digitalRead(I2_SELECT)){
        Serial.print("D ");
      }else{
        if(!digitalRead(A_SELECT)){
          Serial.print("A ");
        }else{
          Serial.print("N ");
        }
      }

      if(digitalRead(I3_SELECT)){
        Serial.print("D ");
      }else{
        if(digitalRead(B_SELECT)){
          Serial.print("B ");
        }else{
          Serial.print("N ");
        }
      }

      if(!digitalRead(I4_SELECT)){
        Serial.print("D");
      }else{
        if(!digitalRead(B_SELECT)){
          Serial.print("B");
        }else{
          Serial.print("N");
        }
      }
      
    Serial.print("\r\n");
    }

    else if(cmp(line,"getDigitalStates")){

      Serial.print(digitalRead(TEST1));
      Serial.print(" ");
      Serial.print(digitalRead(TEST2));
      Serial.print(" ");
      Serial.print(digitalRead(TEST3));
      Serial.print(" ");
      Serial.print(digitalRead(TEST4));
      Serial.print("\r\n");
    
    }

    else if(cmp(line,"getPullStates")){

      Serial.print(digitalRead(PULL_D1));
      Serial.print(" ");
      Serial.print(digitalRead(PULL_D2));
      Serial.print(" ");
      Serial.print(digitalRead(PULL_D3));
      Serial.print(" ");
      Serial.print(digitalRead(PULL_D4));
      Serial.print("\r\n");
    
   }

   else if(cmp(line,"release")){

    switch(line[8]){
      case '1':
        digitalWrite(PULL_D1, LOW);
        Serial.print("done\r\n");
        break;
      case '2':
        digitalWrite(PULL_D2, LOW);
        Serial.print("done\r\n");
        break;
      case '3':
        digitalWrite(PULL_D3, LOW);
        Serial.print("done\r\n");
        break;
      case '4':
         digitalWrite(PULL_D4, LOW);
        Serial.print("done\r\n");
        break;

      default:
        Serial.print("invalid command\r\n");
        break;
      
    }
    continue;

   }
   
   else if(cmp(line,"releaseAll")){
    digitalWrite(PULL_D1, LOW);
    digitalWrite(PULL_D2, LOW);
    digitalWrite(PULL_D3, LOW);
    digitalWrite(PULL_D4, LOW);
    Serial.print("done\r\n");
    continue;
   }

   else if(cmp(line,"pull")){
        if(line[5] == '1'){
      digitalWrite(PULL_D1, HIGH);
      Serial.print("done\r\n");
      continue;
    }else if(line[5] == '2'){
      digitalWrite(PULL_D2, HIGH);
      Serial.print("done\r\n");
      continue;
    }else if(line[5] == '3'){
      digitalWrite(PULL_D3, HIGH);
      Serial.print("done\r\n");
      continue;
    }else if(line[5] == '4'){
      digitalWrite(PULL_D4, HIGH);
      Serial.print("done\r\n");
      
    }else{
      Serial.print("invalid command\r\n");
      continue;
    }  
   }


   else if(cmp(line,"test")){
      if(line[5] == '1'){
      Serial.print(digitalRead(TEST1));
      Serial.print("\r\n");
      continue;
    }else if(line[5] == '2'){
      Serial.print(digitalRead(TEST2));
      Serial.print("\r\n");
      continue;
    }else if(line[5] == '3'){
      Serial.print(digitalRead(TEST3));
      Serial.print("\r\n");
      continue;
    }else if(line[5] == '4'){
      Serial.print(digitalRead(TEST4));
      Serial.print("\r\n");
      
    }else{
      Serial.print("invalid command\r\n");
      continue;
    }  
   }

   else if(cmp(line,"help")){
    Serial.print("Funkyswitch 1.0\r\n");
    Serial.print("switchDigital <1/2/3/4> switches an input to digital\r\n");
    Serial.print("switchA <1/2>           switches input 1 or 2 to analog channel A\r\n");
    Serial.print("switchB <3/4>           switches input 3 or 4 to analog channel B\r\n");
    Serial.print("getSwitchStates         outputs the connected output for each input\r\n");
    Serial.print("getDigitalStates        outputs the measured states of each digital input\r\n");
    Serial.print("getPullStates           outputs the pull states for each digital channel\r\n");
    Serial.print("test <1/2/3/4>          outputs the digital level of the given input\r\n");
    Serial.print("pull <1/2/3/4>          pulls the given input to high (5V)\r\n");
    Serial.print("release  <1/2/3/4>      sets the given input to high impedance mode\r\n");
    Serial.print("releaseAll              sets all inputs to high impedance mode\r\n");
   }

  
  else{
    Serial.print("invalid command\r\n");
  }
  }
}
