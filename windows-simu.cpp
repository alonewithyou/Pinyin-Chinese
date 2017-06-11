#include <iostream>
#include <windows.h>

using namespace std;
DWORD WINAPI f_input(LPVOID );
char seq[500];
int main(int argc, char *argv[])
{
	freopen("pinyin.txt", "r", stdin); 
	CreateThread(NULL,0,f_input,NULL,0,NULL);
	Sleep(5000);
	while(gets(seq)){
		Sleep(100);
		for (int j = 0; j < strlen(seq); ++j){
			Sleep(30);
			if (seq[j] < 'a' || seq[j] > 'z')	continue;
			if (seq[j] == 'u' && seq[j+1] == ':'){
				seq[j] = 'v';
				keybd_event(65 + seq[j] - 'a', 0, 0, 0);
				keybd_event(65 + seq[j] - 'a', 0, KEYEVENTF_KEYUP, 0);
				j++; 
				continue; 
			}
			printf("Pressing %c\n", seq[j]);
			keybd_event(65 + seq[j] - 'a', 0, 0, 0);
			keybd_event(65 + seq[j] - 'a', 0, KEYEVENTF_KEYUP, 0);
		}
		for (int j = 0; j < 5; ++j){
			Sleep(20);
			keybd_event(32, 0, 0, 0);
			Sleep(20);
			keybd_event(32, 0, KEYEVENTF_KEYUP, 0);
		}
		Sleep(20);
		keybd_event(13, 0, 0, 0);
		Sleep(20);
		keybd_event(13, 0, KEYEVENTF_KEYUP, 0);
	}
	return 0; 
}

DWORD WINAPI f_input(LPVOID lpParamter){
	char a[100];
	cin>>a;
	ExitThread(0);
}
