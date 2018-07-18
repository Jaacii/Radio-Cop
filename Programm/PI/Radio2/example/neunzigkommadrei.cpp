#include "../Si4703_Breakout.h"
#include <stdio.h>

int main() {
	//Variabeln
	int selectStation =0;
	int volume =7;
	int resetPin = 23; //GPIO2_3
	int sdaPin =0; //GPIO0_0
	Si4703_Breakout radio (resetPin, sdaPin);
	
	//radio init
	radio.powerOn();
	radio.setVolume(volume);
	radio.setChannel(903);	//NDR 90,3
	
	
	
	
	//Daten aus geben für Konsole 
	printf (Listening to station: NDR 90,3);
	
	
	//quittiere
	return 0;
	



}