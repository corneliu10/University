#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>	
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>

int main(int argc, char *argv[]) {
	if(argc == 1) {
		perror("Wrong number of args!");
		return errno;
	}

	char shm_name[] = "collatz";
	int shm_fd;

	shm_fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
	if(shm_fd < 0) {
		perror(NULL);
		return errno;
	}

	size_t shm_size = argc*getpagesize();
	size_t page_size = getpagesize();
	if(ftruncate(shm_fd, shm_size) == -1) {
		perror(NULL);
		shm_unlink(shm_name);
		return errno;
	}

	printf("Starting parent %d\n", getpid());

	for(int i=1; i<argc; ++i) {
		pid_t pid = fork();

		if(pid < 0) {
			perror("Error forking!");
			return errno;
		} else if(pid==0) {
			char *shm_ptr_write = mmap(0, page_size, PROT_WRITE, MAP_SHARED, shm_fd, (i-1)*page_size);
			if (shm_ptr_write == MAP_FAILED) {
				perror(NULL);
				shm_unlink(shm_name);
				return errno;
			}

			int n = atoi(argv[i]);
			shm_ptr_write += sprintf(shm_ptr_write, "%d: ",n);

			while(n != 1) {
				if(n%2 == 0) n = n/2;
				else n = 3*n+1;

				shm_ptr_write += sprintf(shm_ptr_write, "%d ",n);
			}

			shm_ptr_write += sprintf(shm_ptr_write, "\n");
			printf("I'm done! Parent: %d Child: %d\n",getppid(), getpid());

			munmap(shm_ptr_write, page_size);
			return 0;
		}
	}

	for(int i=1;i<argc;++i)
		wait(NULL);

	char *shm_ptr_read = mmap(0, shm_size, PROT_READ, MAP_SHARED, shm_fd, 0);
		if (shm_ptr_read == MAP_FAILED) {
			perror(NULL);
			shm_unlink(shm_name);
			return errno;
		}

	printf("\n");
	for(size_t i=0; i<shm_size; ++i) {
		if(shm_ptr_read[i]) 
			printf("%c",shm_ptr_read[i]);
	}
	printf("\n");
	munmap(shm_ptr_read, shm_size);

	shm_unlink(shm_name);

	return 0;
}