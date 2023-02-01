#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a function that runs forever and returns nothing
 * Return: 0 in the end
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry to a program that creates 5 zombie process
 * Return: 0 on success
 */
int main(void)
{
	int children = 0;
	pid_t pid;

	while (children < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		children++;
	}
<<<<<<< HEAD

	infinite_while();

	return (EXIT_SUCCESS);
}
=======
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
>>>>>>> 7f123456de8039d41f57e00e36811bd794897e51
