#include <stdio.h>
#include <unistd.h>
int main()
{
	char buf[] = "Hello World\n";
	write(1, buf, sizeof(buf));
	return 0;
}
