/*
 *    NAME:frkrw 0.1 (31/07/2011)
 *    INFO:Restart Android Framework
 *
 *  AUTHOR: Stefano Viola (estebanSannin)
 * COMPANY: DroniX Dev Team
 *    SITE: www.hacklabproject.org
 *   EMAIL: stefanoviola85 [at] gmail [dot] com
 * LICENSE: GPLv3
 * 
 * 
 */

#include <sys/types.h>
#include <signal.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int killProcessByName(const char* name) {
	pid_t p;
	size_t i;
	int killed = 0;
	char* s = (char*)malloc(264);
	char buf[128];
	FILE* st;
	DIR* d = opendir("/proc");
	if (d == NULL) { free(s); return 0; }
	struct dirent* f;
	while ((f = readdir(d)) != NULL) {
		if (f->d_name[0] == '.') continue;
		for (i = 0; isdigit(f->d_name[i]); i++);
		if (i < strlen(f->d_name)) continue;
		strcpy(s, "/proc/");
		strcat(s, f->d_name);
		strcat(s, "/status");
		st = fopen(s, "r");
		if (st == NULL) { closedir(d); free(s); return 0; }
		do {
			if (fgets(buf, 128, st) == NULL) { fclose(st); closedir(d); free(s); return 0; }
		} while (strncmp(buf, "Name:", 5));
		fclose(st);
		for (i = 5; isspace(buf[i]); i++);
		*strchr(buf, '\n') = 0;
		if (!strcmp(&(buf[i]), name)) {
			sscanf(&(s[6]), "%d", &p);
			kill(p, SIGKILL);
			killed = 1;
		}
	}
	closedir(d);
	free(s);
	if(killed)
		return 1;
	else
		return 0;
}

void help(){
	printf("\nfrkrw 0.1: Restart Android Framework\n\n"
		"DroniX Dev Team\n\n"
		"OPTION:\n"
		"\t-h or --help\tthis message\n"
		"\t-v or --version\t version note\n\n");
}

void version(){
	printf("\nfrkrw 0.1 (31/07/2011)\n\n"
		"AUTHOR: DroniX Dev Team (estebanSannin)\n"
		"  SITE: www.hacklabproject.org\n"
		" EMAIL: stefanoviola85 [at] gmail [dot] com\n\n");
}

int main(int argc, char *argv[]) {
	if(argc==2){
		if(!strcmp(argv[1],"-h") || !strcmp(argv[1],"--help")){
			help();
			exit(0);
		}
		else if (!strcmp(argv[1], "-v") || !strcmp(argv[1], "--version")){
			version();
			exit(0);
		}
		else{
			help();
			exit(1);
		}
	}
	int success = killProcessByName("skype");
	//DEBUG
	//printf("success: %d\n",success);
	if(!success)
		printf("ERROR: NO FRAMEWORK STARTED!\n");
	else
		printf("Restart Framework...\n");
	
return 0;
}
