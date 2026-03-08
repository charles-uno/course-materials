#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
	pid_t pid = getpid();
	printf("pid=%d %s", pid, "starting.\n");
	sleep(5);
	printf("pid=%d %s", pid, "ending.\n");
	return 0;
}