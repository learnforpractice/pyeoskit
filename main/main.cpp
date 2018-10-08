#include <eosio/chain/abi_serializer.hpp>
#include <vector>

using namespace std;
using namespace eosio::chain;

int main(int argc, char* argv[]) {
   abi_def abi;
   vector<char> rawabi;

   abi_serializer::to_abi(rawabi, abi);
   return 0;
}



