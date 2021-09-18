
#include <stdio.h>
#include <assert.h>
#include "dist_struct.h"

// honestly I should try using zig instead
long long unsigned dist_to_long(Dist dist) {
  return *(long long unsigned*) &dist;
}

int main() {
  assert(sizeof(Dist) == sizeof(unsigned long long));
  Dist _res;
#define PRINTHASH(x) _res = hash((x)); printf("hash of '%s' was %llu\n", (x), (long long unsigned*) &_res)
  PRINTHASH("sett");
  dist_debug(_res);
  PRINTHASH("test");
  dist_debug(_res);
}
