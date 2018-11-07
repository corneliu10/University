#include <stdio.h>
#include <sys/types.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
	if(argc == 1) {
		perror("Wrong numbers of args! Try again");
		return errno;
	}

	printf("Starting parent %d\n", getpid());

	for(int i=1; i<argc; ++i) {

		pid_t pid = fork();

		if(pid < 0) {
			return errno;
		} else if(pid == 0) {
			printf("%d: ", atoi(argv[i]));

			int n = atoi(argv[i]);
			while(n != 1) {
				if(n%2 == 0) n = n/2;
				else n = 3*n+1;

				printf("%d ",n);
			}

			printf("\nDone Parent %d Me %d\n",getppid(), getpid());
			return;
		}
	}

	for(int i=1;i<argc; ++i)
		wait(NULL);

	return 0;
}