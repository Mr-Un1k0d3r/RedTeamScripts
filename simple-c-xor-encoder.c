#include <windows.h>

int main() {

    DWORD key = 0x10101010;
    DWORD dwSize = 16;
    CHAR *shellcode = GlobalAlloc(GPTR, dwSize);
    strcpy(shellcode, "AAAABBBBCCCCDDDD\x00");

    DWORD *current;
    int i = 0;
    for(i; i < dwSize / 4; i++) {
        current = (DWORD*)shellcode;
        *current = *current ^ key;
        shellcode += 4;
    }
    shellcode -= dwSize;

    // print test
    for(i = 0; i < dwSize; i++) {
        printf("\\x%02x", shellcode[i]);
    }

    // execute shellcode()
    GlobalFree(shellcode);
    return 0;
}
