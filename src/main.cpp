
#include <cassert>
#include <cstdint>
#include "dist_struct.h"
#include <iostream>

int main() {
  // TODO: do a chi-squared test over a corpus of english words to see if this is a decent hash for identifiers
  const auto printHash = [&](const char* str) {
    std::cout << "hash of '" << str <<  " was " << reinterpret_cast<uint64_t&&>(hash(str)) << std::endl;
  };
  printHash("sett");
  printHash("test");
  printHash("testttq");

  return 0;
}
