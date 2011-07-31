/*
 *
 * DroniX Web Manager: Upload Module
 *
 * AUTHOR:	Stefano Viola aka estebanSannin
 * EMAIL:	stefanoviola85@gmail.com
 * SITE: 	http://hacklabproject.org
 *
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include "cgic.h"
#define BufferLen 1024
#define PERMS 0777

void File()
{
	cgiFilePtr file;
	char name[1024];
	char contentType[1024];
	char buffer[1024];
	int size, fout;
	int got;
	if (cgiFormFileName("file", name, sizeof(name)) !=
			cgiFormSuccess)
	{
		printf("<p>No file was uploaded.<p>\n");
		return;
	}
	fprintf(cgiOut, "<h3>Upload Successfull!</h3>");
	fprintf(cgiOut, "The filename submitted was: ");
	cgiHtmlEscape(name);
	fprintf(cgiOut, "<p>\n");
	cgiFormFileSize("file", &size);
	fprintf(cgiOut, "The file size was: %d bytes<p>\n", size);
	cgiFormFileContentType("file", contentType, sizeof(contentType));

	fprintf(cgiOut, "The alleged content type of the file was: ");
	cgiHtmlEscape(contentType);

	if (cgiFormFileOpen("file", &file) != cgiFormSuccess) {
		fprintf(cgiOut, "Could not open the file.<p>\n");
		return;
	}
	fprintf(cgiOut, "<br><br><br><br><br><a href='upload.html'>---> Return to Upload Page</a>");
	fprintf(cgiOut, "<pre>\n");



	char downloadDir[1024];
	strcpy(downloadDir, "/mnt/sdcard/");
	strcat (downloadDir, name);
	if ((fout = creat(downloadDir, PERMS)) == -1){
		fprintf(cgiOut, "can't create %s, mode %03o",downloadDir, PERMS);
		exit(1);
	}


	while (cgiFormFileRead(file, buffer, sizeof(buffer), &got) ==
			cgiFormSuccess)
	{
		write(fout, &buffer, sizeof(buffer));
	}
	close(fout);
	fprintf(cgiOut, "</pre>\n");
	cgiFormFileClose(file);
}

int cgiMain() {
	cgiHeaderContentType("text/html");
	/* Top of the page */

	fprintf(cgiOut, "<html>");
	fprintf(cgiOut, "<link rel='stylesheet' href='style.css' type='text/css'>");
	fprintf(cgiOut, "<head>");
	fprintf(cgiOut, "<title>Monitor Tools</title>");
	fprintf(cgiOut, "<script src='js/ajaxsbmt.js' type='text/javascript'></script>");
	fprintf(cgiOut, "<script language='javascript' src='dinamic.js' type=text/javascript></script>");
	fprintf(cgiOut, "</head>");
	fprintf(cgiOut, "<body>");
	fprintf(cgiOut, "<!-- onload='setInterval(mostraOra, 1000);'> -->");

	fprintf(cgiOut, "<div id='footer'><font color=red>DroniX Web Manager</font> by <font color=yellow><a href='http://esteban.homelinux.org'>Stefano Viola (EstebanSannin)</a></font></div>");

	fprintf(cgiOut, "<div id='header'><img src='image/dronixlogo2.png'>");
	fprintf(cgiOut, "<table border='0'><tr>");
	fprintf(cgiOut, "<td class='headitem'><a href='index.html'>home</a></td>");
	fprintf(cgiOut, "<td class='headitem'><a href='versionNote.html'>versionNote</a></td>");
	fprintf(cgiOut, "<td class='headitem'><a href='modules.html'>modules</a></td>");
	fprintf(cgiOut, "<td class='headitem'><a href='sdcard'>SD-Card</a></td>");
	fprintf(cgiOut, "<td class='headitem'><a href='https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ZCZJMRK7UGHH6&lc=GB&item_name=DroniX\%20Development&currency_code=EUR&bn=PP\%2dDonationsBF\%3abtn_donate_LG\%2egif\%3aNonHosted'>donate</a></td></tr></table>");
	fprintf(cgiOut, "</div>");
	fprintf(cgiOut, "<div id='content'>");
	fprintf(cgiOut, "<br>");


	File();
	fprintf(cgiOut, "</div></BODY></HTML>\n");
	return 0;
}
