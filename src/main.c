
#include <stdio.h>
#include <assert.h>
#include "dist_struct.h"

// honestly I should try using zig instead

int main() {
  assert(sizeof(Dist) == sizeof(unsigned));
  const char* word = "test";
  const Dist dist = hash(word);
  printf("hash of '%s' was %lld\n", word, dist);
}
