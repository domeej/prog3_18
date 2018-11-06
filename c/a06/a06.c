#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double getPositive(double x);

void calcHeron(){
	double w, newW, gap, x;

	while((scanf("%lf", &x)) && x != 0){
		w = (1+x)/2;
		newW = (w+(x/w))/2;
		gap = w-newW;
		while(gap >= 1e-7){
			newW = w;
			w = (w+(x/w))/2;
			gap = newW-w;
			
		}
		printf("Ergebnis: %6.4f\n", newW);
	}
	
}
double getPositive(double x){
	if(x<0){
		return x *= -1;
	}
	else{
		return x;
	}
}

double myPow(double x, double y){
	double result = x;
	while(y != 1){
		result *= x;
		y--;
	}	
	return result;
}

int main (int argc, char *argv[]){
	
	calcHeron();
	
	
	
	return 0;
}
