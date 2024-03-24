#include <sys/random.h>

// get the 16 bytes random number
// dd if=/dev/urandom bs=16 count=1 2 > /dev/null | xxd -p

void main(){
    uint8_t secret[16];
    int len = getrandom(secret, sizeof(secret), 0);

    if (len != sizeof(secret)){
        abort();
    }
}

