/*Author: Chymion*/
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <ios>
#include <sstream>
#include <limits>
#include <regex>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

using namespace std;


int main(int argc, char** argv)
{
	system("clear");
	string s;
	cout << "=============\nSCRAPCHAN\n=============\n\n";
	cout << "Enter Thread URL: ";
	cin >> s;
	
	int num;
	cout <<"Which filetype do you want to retrieve?\n";
	cout <<"1- Video(mp4,webm)\n2- Gif\n3- Image(jpg,png)\n\n";
	cout << "Choice(1,2,3): ";
	cin >> num;

	switch (num)
	{
		case 1:
		{
			system((string("lynx -dump -listonly "+s+" | grep 'webm\\|mp4' > /tmp/links.temp").c_str()));
		}break;
		case 2:
		{
			system((string("lynx -dump -listonly "+s+" | grep '\\.gif' > /tmp/links.temp").c_str()));
		}break;
		case 3:
		{
			system((string("lynx -dump -listonly "+s+" | grep 'jpg\\|png' > /tmp/links.temp").c_str()));
		}break;
		default:
		{
			cout << "Wrong entry!\n";
			exit(0);
		}break;
	}

	struct stat st = {0};

	if (stat("./output", &st) == -1) {
    	mkdir("./output", 777);
	}
	
	string text;
	ifstream MyRead("/tmp/links.temp");
	while (getline(MyRead, text)){
		string s =  regex_replace(text, regex("\\d+.\\s"),"");
		system(string("cd output && wget -N " + s).c_str());
	}

	MyRead.close();

	if (remove("/tmp/links.temp") != 0)
	{
		cerr << "Temporary file deletion failed!" << endl;
		return -1;
	}else
	{
		cout << "Transfer completed!" << endl;
	}
	
	return 0;
}
