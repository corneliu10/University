#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>

#define SIZE_BUF 1024

int main(int argc, char **argv) {
	if(argc != 3) {
		write(1, "Error arguments\n", sizeof("Error arguments\n"));
		return 0;
	}
	int fd;
	fd = open(argv[1], O_RDONLY);
	char buf[SIZE_BUF];
	
	if( fd < 0) {
		//write(1, "File could not be opened!");
		perror("open");
		return -1;
	} else {
		int fdw = open(argv[2], O_WRONLY | O_CREAT, 0644);
		if (fdw < 0) {
			return -1;
		}

		ssize_t bytes;
		while(bytes = read(fd, buf, sizeof(buf)))
			write(fdw, buf, bytes);
	}

	return 0;
}