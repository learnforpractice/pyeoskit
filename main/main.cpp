#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "cpp_object.hpp"

#define FILE_SIZE (184*10000)
int main(int argc, char ** argv) {
    char *data = (char *)malloc(FILE_SIZE);
    FILE *fp = fopen("block.bin", "rb");
    int file_size = fread(data, 1, FILE_SIZE, fp);
    int count = 0;
    for (int i=0;i<file_size;) {
        count += 1;
        int msg_len = *((uint32_t*)(data+i));
        printf("++count %d, msg_len %d\n", count, msg_len);
        if (msg_len <= 0) {
                return -1;
        }
        i += msg_len;
        i += 4;
         continue;

        if (data[i+4] != 7) {
                printf("bad type %d\n", data[i+4]);
                i+=msg_len;
                continue;
//              return -1;
        }
        string in = string((char *)data+i+5, msg_len-1);
        string out;
        unpack_cpp_object_(7, in, out);
        i += msg_len;
    }
    free(data);
    return 0;
}
