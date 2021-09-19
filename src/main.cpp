
#include <cassert>
#include <cstdint>
#include "dist_struct.h"
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

int main() {
  // TODO: do a chi-squared test over a corpus of english words to see if this is a decent hash for identifiers
  const auto printHash = [&](const char* str) {
    const auto hashed = hash(str);
    std::cout << "hash of '" << str <<  " was " << static_cast<uint64_t>(hashed) << std::endl;
    std::cout << "debug: " << hashed << std::endl;
  };
  printHash("sett");
  printHash("test");
  printHash("testttq");
  
  std::ifstream words_file;
  words_file.open("words_alpha.txt");
  
  std::unordered_map<std::string, Dist> hashes;
  for (std::string line; std::getline(words_file, line);) {
    hashes[line] = hash(line.c_str());
  }

  std::cout << "hash count: " << hashes.size() << std::endl;
  std::cout << "enter word> ";
  for (std::string word; std::getline(std::cin, word);) {
    const auto word_hash = hash(word.c_str());
    for (const auto& [k, v] : hashes)
      if (v == word_hash)
        std::cout << k << std::endl;
    std::cout << "next word> ";
  }

  return 0;
}
