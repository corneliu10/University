#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

int getLength(char *s) {
	int ln = 0;
	for(int i=0; s[i]; ++i)
		ln++;

	return ln;
}

void swapC(char *a, char *b) {
	char aux;

	aux = *a;
	*a = *b;
	*b = aux;
}

void *revString(void *arg) {
	char *str = (char *)arg;
	int ln = getLength(str);

	for(int i=0; i<ln/2; ++i) {
		swapC(&str[i], &str[ln-i-1]);
	}

	return str;
}

int main(int argc, char *argv[]) {
	if(argc != 2) {
		perror("Wrong number of args!");
		return errno;
	}

	pthread_t tid;

	if(pthread_create(&tid, NULL, revString, argv[1])) {
		perror(NULL);
		return errno;
	}

	void *res;
	if(pthread_join(tid, &res)) {
		perror(NULL);
		return errno;
	}

	printf("%s\n",(char *)res);

	return 0;
}