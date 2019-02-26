#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>

int main() {
	int pid = fork();

	if(pid < 0)
		return errno;
	else if(pid==0) {
		char *cmd = "/bin/ls";
		char *argv[] = {"ls", "-l", NULL};
		execve(cmd, argv, NULL);
	} else {
		printf("My:%d Child:%d\n",getpid(), pid);

		wait(NULL);
		printf("Child %d finished!\n", pid);
	}
}

