#include <stdlib.h>
#include <stdio.h>

int main()
{
    char cmdLine[4096];
    const char *pfile = "/Applications/MonsterKeyboard/keyboardlight-gui.py";
    sprintf(cmdLine, "/usr/local/bin/python3 %s %d %d %d %d", pfile, 255, 255, 255, 32);
    system(cmdLine);
    return 0;
}
