#include <stdio.h>
#include <sys/types.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
	if(argc != 2) {
		perror("Wrong numbers of args! Try again");
		return errno;
	}

	pid_t pid = fork();

	if(pid < 0) {
		return errno;
	} else if(pid == 0) {
		printf("%d: ", atoi(argv[1]));

		int n = atoi(argv[1]);
		while(n != 1) {
			if(n%2 == 0) n = n/2;
			else n = 3*n+1;

			printf("%d ",n);
		}

		printf("\n");
	} else {
		wait(NULL);

		printf("Child %d finished!\n", pid);
	}

	return 0;
}