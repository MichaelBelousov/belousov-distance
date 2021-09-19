
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
  PRINTHASH("test");
  PRINTHASH("testttq");

  // TODO: do a chi-squared test over a corpus of english words to see if this is a decent hash for identifiers
}
