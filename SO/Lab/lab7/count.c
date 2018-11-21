#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#define MAX_RESOURCES 5
#define MAX_THREADS   10

int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx;

void* increase_count(void *arg) {
	int *val = (int*)arg;

	pthread_mutex_lock(&mtx);
	/// critical section

	available_resources += *val;
	if(available_resources > MAX_RESOURCES)
		available_resources = MAX_RESOURCES;
	pthread_mutex_unlock(&mtx);

	printf("Got %d resources %d remaining\n", *val, available_resources);
	fflush(stdout);

	free(val);
	return 0;
}

void* decrease_count(void *arg) {
	int *val = (int*)arg;

	pthread_mutex_lock(&mtx);
	/// critical section
	if (available_resources < -(*val)) {
		pthread_mutex_unlock(&mtx);
		return -1;
	}
	else {
		available_resources += *val;

		pthread_mutex_unlock(&mtx);
		printf("Released %d resources %d remaining\n", -(*val), available_resources);
		fflush(stdout);
	}

	free(val);
	return 0;
}

int main() {
	printf("MAX_RESOURCES = %d\n", MAX_RESOURCES);

	if (pthread_mutex_init(&mtx, NULL)) {
		perror(NULL);
		return errno;
	}

	srand(time(NULL));
	pthread_t tids[MAX_THREADS];

	for(int i=0; i<MAX_THREADS; ++i) {
		int *val = (int*)malloc(sizeof(int));
		*val = rand() % (2 * MAX_RESOURCES) - MAX_RESOURCES;

		if(*val < 0) {
			if(pthread_create(&tids[i], NULL, decrease_count, val)) {
				perror(NULL);
				return errno;
			}
		} else {
			if(pthread_create(&tids[i], NULL, increase_count, val)) {
				perror(NULL);
				return errno;
			}
		}
	}

	for(int i=0; i<MAX_THREADS; ++i)
		if(pthread_join(tids[i], NULL)) {
			perror(NULL);
			return errno;
		}

	pthread_mutex_destroy(&mtx);

	return 0;
}