// C++ code

//ここからは音程と周波数を紐づけている,楽譜よりは一オクターブ下の音が鳴る
#define C3 131
#define CS3 139
#define D3 147
#define DS3 156
#define E3 165
#define F3 175
#define FS3 185
#define G3 196
#define GS3 208 
#define A3 220
#define AS3 233
#define B3 247

#define C4 262
#define CS4 277
#define D4 294
#define DS4 311
#define E4 330
#define F4 349
#define FS4 370
#define G4 392
#define GS4 415
#define A4 440
#define AS4 466
#define B4 494
#define C5 523

//keyと入力場所を紐づける
#define oct_key A2
#define B_key 3
#define BF_key 4
#define A_key A5
#define G_key 6
#define GS_key 7
#define LowCS_key 9
#define F_key 10
#define E_key 11
#define D_key 12
#define DS_key 13
#define LowC_key A0
#define SideBF_key A1


void setup()
{
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(oct_key,INPUT);
  pinMode(B_key,INPUT);
  pinMode(BF_key,INPUT);
  pinMode(A_key,INPUT);
  pinMode(G_key,INPUT);
  pinMode(GS_key,INPUT);
  pinMode(LowCS_key,INPUT);
  pinMode(F_key,INPUT);
  pinMode(E_key,INPUT);
  pinMode(D_key,INPUT);
  pinMode(DS_key,INPUT);
  pinMode(LowC_key,INPUT);
  pinMode(SideBF_key,INPUT);
}

void loop()
{
  if(digitalRead(oct_key) == HIGH){
    if(digitalRead(DS_key) == HIGH){
      tone(8, DS4, 100);
      Serial.println("DS5");
      //Serial.print("DS4");
    }
     else if(digitalRead(D_key) == HIGH){
       tone(8, D4, 100);
       Serial.println("D5");
       //Serial.print("D4");
     }
     else if(digitalRead(E_key) == HIGH){
        if (digitalRead(F_key) == HIGH){
            tone(8, E4, 100);
            Serial.println("E5");
            //Serial.print("E5");
        }
        else{
            tone(8, FS4, 100);
          	Serial.println("FS5");
            //Serial.print("FS4");
        }
     }
     else if(digitalRead(F_key) == HIGH){
        tone(8, F4, 100);
       	Serial.println("F5");
        //Serial.print("F4");
     }
     else if(digitalRead(GS_key) == HIGH){
        tone(8, GS4, 100);
      	Serial.println("GS5");
        //Serial.print("GS4");
     }
     else if(digitalRead(G_key) == HIGH){
        tone(8, G4, 100);
       	Serial.println("G5");
        //Serial.print("G4");
     }
     else if(digitalRead(SideBF_key) == HIGH){
        tone(8, AS4, 100);
       	Serial.println("AS5");
        //Serial.print("AS4");
     }
     else if(digitalRead(A_key) == HIGH){
        if (digitalRead(B_key) == HIGH){
            tone(8, A4, 100);
         	Serial.println("A5");
          //Serial.print("A4");
        }
        else{
        tone(8, C5, 100);
        Serial.println("C6");
        //Serial.print("C6");
        }
     }
     else if(digitalRead(BF_key) == HIGH){
        tone(8, AS4, 100);
       	Serial.println("AS5");
        //Serial.print("AS5");
     }
     else if (digitalRead(B_key) == HIGH){
        tone(8,B4,100);
       	Serial.println("B5");
        //Serial.print("B4");
     }
     else{
  Serial.println("NoSound");
  //Serial.print("NoSound");
   }
   

  }
   else{
     if (digitalRead(LowCS_key) == HIGH){
       tone(8,CS3,100);
       Serial.println("CS4");
       //Serial.print("CS4");
     }
     else if(digitalRead(LowC_key) == HIGH){
       tone(8,C3,100);
       Serial.println("C4");
       //Serial.print("C3");
     }
     else if(digitalRead(DS_key) == HIGH){
       tone(8, DS3, 100);
       Serial.println("DS4");
       //Serial.print("DS3");
     }
     else if(digitalRead(D_key) == HIGH){
       tone(8, D3, 100);
       Serial.println("D4");
       //Serial.print("D3");
     }
     else if(digitalRead(E_key) == HIGH){
        if (digitalRead(F_key) == HIGH){
            tone(8, E3, 100);
          	Serial.println("E4");
            //Serial.print("E3");
        }
        else{
            tone(8, FS3, 100);
          	Serial.println("FS4");
            //Serial.print("FS3");
        }
     }
     else if(digitalRead(F_key) == HIGH){
        tone(8, F3, 100);
       	Serial.println("F4");
        //Serial.print("F3");
     }
     else if(digitalRead(GS_key) == HIGH){
        tone(8, GS3, 100);
      	Serial.println("GS4");
        //Serial.print("GS3");
     }	
     else if(digitalRead(G_key) == HIGH){
        if (digitalRead(A_key) == HIGH){
            tone(8, G3, 100);
          	Serial.println("G4");
            //Serial.print("G3");
        }
        else{
        tone(8, CS4, 100);
        Serial.println("CS5");
        //Serial.print("CS4");
        }
        
     }
     else if(digitalRead(SideBF_key) == HIGH){
        tone(8, AS3, 100);
       	Serial.println("AS4");
        //Serial.print("AS3");
     }
     else if(digitalRead(A_key) == HIGH){
        if (digitalRead(B_key) == HIGH){
            tone(8, A3, 100);
          	Serial.println("A4");
            //Serial.print("A3");
        }
        else{
        tone(8, C4, 100);
        Serial.println("C5");
        //Serial.print("C4");
        }
     }
     else if(digitalRead(BF_key) == HIGH){
        tone(8, AS3, 100);
       	Serial.println("AS4");
        //Serial.print("AS3");
     }
     else if (digitalRead(B_key) == HIGH){
        tone(8,B3,100);
       	Serial.println("B4");
        //Serial.print("B3");
     }
    else{
  Serial.println("NoSound");
  //Serial.print("NoSound");
   }

     }   
  
  //delay(80); // Wait for a bit
delay(150);  
}