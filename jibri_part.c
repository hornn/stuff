#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void usage();
void bail(char *s);

int main(int argc, char** argv)
{
	long int lines=0;
	long int cnt=0;
	long int idoff=0;

	if(argc != 3)
		usage();

			
	lines = atoi(argv[1]);
	idoff = atoi(argv[2]);

	if(lines <= 0)
		bail("invalid lines number!");	

	
	srand(time(NULL));

	for(cnt = 0; cnt < lines; cnt++)
	{
		int r = rand() % 999999;
		int c1 = rand() % 25;
		int c2 = rand() % 25;
		int c3 = rand() % 25;
		int c4 = rand() % 25;
		int c5 = rand() % 25;
		static char ca[6] = {0};
		snprintf(ca,6,"%c%c%c%c%c",65+c1, 65+c2, 65+c3, 65+c4, 65+c5);
		
		/*printf("%016ld\t%ld\t%s%s%s%ld\t%ld\n",
		       cnt+idoff, r, 
		       ca, ca, ca, c1*c2*c3,
		       r*13);
		*/
	        printf("%016ld%ld%s%s%s%ld\t%d\n",
		       cnt+idoff, r, 
		       ca, ca, ca, c1*c2*c3,
		       r*13);


	}
	
}


void usage()
{

	printf("Usage: jibri_part <number of lines> <id offset>\n");
	exit(0);

}

void bail(char *s)
{
	if(s)
		printf("%s\n",s);
	else
		printf("Fatal error!\n");

	exit(0);

}
