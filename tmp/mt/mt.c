#include <stdio.h> 
#include <time.h>       
#include <math.h>
 
int main( int argc, char **argv)
{

    time_t rawtime = time(NULL);
    
    struct tm *ptm = localtime(&rawtime);
    
	float ms =(ptm->tm_min*60 + ptm->tm_hour*3600 + ptm->tm_sec)/.864;
	float sec =fmod(ms,100);
	float min =fmod(((ms-sec)/100),100);
	float hour =(ms-sec-min*100)/10000;

	while ((++argv)[0]) {
		if (argv[0][0] == '-' ) {

			switch (argv[0][1])  {
				case 'm':
					printf("%.0f:%.0f\n", hour, min);
					break;
				case 's':
					printf("%f\n", ms);
					break;
				default:
					printf("mt: Unknown option argument: %s\n", argv[1]);
			}
		}
	}

	if ( argc == 1) {
		printf("%.0f:%.0f:%.0f\n", hour, min, sec);
	}

	/* printf("%.0f:%.0f:%.0f\n", hour, min, sec); */
    return 0;
}
