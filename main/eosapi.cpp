#include "eosapi.hpp"

static fc::microseconds abi_serializer_max_time = fc::microseconds(100*1000);

uint64_t s2n_(string& str) {
   try {
      return name(str).value;
   } catch (...) {
   }
   return 0;
}

void n2s_(uint64_t n, string& s) {
   s = name(n).to_string();
}

static variant action_abi_to_variant( const abi_def& abi, type_name action_type ) {
   variant v;
   auto it = std::find_if(abi.structs.begin(), abi.structs.end(), [&](auto& x){return x.name == action_type;});
   if( it != abi.structs.end() )
      to_variant( it->fields,  v );
   return v;
}

void pack_args_(string& _rawabi, uint64_t action, string& _args, string& _binargs) {
   fc::variant args = fc::json::from_string(_args);
   bytes rawabi = bytes(_rawabi.data(), _rawabi.data() + _rawabi.size());

   try {
      abi_def abi = fc::json::from_string(_rawabi).as<abi_def>();
      abi_serializer abis( abi, abi_serializer_max_time );
      auto action_type = abis.get_action_type(action);
      EOS_ASSERT(!action_type.empty(), action_validate_exception, "Unknown action ${action}", ("action", action));

      auto binargs = abis.variant_to_binary(action_type, args, abi_serializer_max_time);
      _binargs = string(binargs.begin(), binargs.end());
   } FC_LOG_AND_DROP();
}

void unpack_args_( string& _rawabi, uint64_t action, string& _binargs, string& _args ) {
   bytes rawabi = bytes(_rawabi.data(), _rawabi.data() + _rawabi.size());
   bytes binargs = bytes(_binargs.data(), _binargs.data() + _binargs.size());

   try {
      abi_def abi = fc::json::from_string(_rawabi).as<abi_def>();
      abi_serializer abis( abi, abi_serializer_max_time );
      auto args = abis.binary_to_variant( abis.get_action_type( action ), binargs, abi_serializer_max_time );
      _args = fc::json::to_string(args);
   } FC_LOG_AND_DROP();
}

