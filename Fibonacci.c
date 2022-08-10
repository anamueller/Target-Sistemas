#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define TAM 400

//F(n)=F(n-1)+F(n-2)

void calcularFibo(int limite, int vetor[]){
	int i = 2;
	if(limite == 0 || limite==1){
		printf("O número digitado faz parte da sequência de fibonacci\n");
		return;
	}
	while(vetor[i]<=limite){
		vetor[i] = vetor[i-1]+vetor[i-2];
		if(vetor[i]==limite){
			printf("O número digitado faz parte da sequência de fibonacci, número %d da sequência\n", i+1);
			return;
		}
		i++;
	}
	printf("O número digitado não faz parte da sequência de fibonacci\n");
}

int main(){
	int fibonacci;
	int sequence[TAM];
	sequence[0] = 0;
	sequence[1] = 1;
	printf("Digite o número:");
	scanf("%d", &fibonacci);
	calcularFibo(fibonacci, sequence);
    return 0;
}