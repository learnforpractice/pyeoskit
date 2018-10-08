#include "eosapi.hpp"

static fc::microseconds abi_serializer_max_time = fc::microseconds(100*1000);

static variant action_abi_to_variant( const abi_def& abi, type_name action_type ) {
   variant v;
   auto it = std::find_if(abi.structs.begin(), abi.structs.end(), [&](auto& x){return x.name == action_type;});
   if( it != abi.structs.end() )
      to_variant( it->fields,  v );
   return v;
};

void pack_args(string& _rawabi, uint64_t code, uint64_t action, string& _args, string& _binargs) {
   abi_def abi;
   fc::variant args = fc::json::from_string(_args);
   bytes rawabi = bytes(_rawabi.data(), _rawabi.data() + _rawabi.size());

   if( abi_serializer::to_abi(rawabi, abi) ) {
      abi_serializer abis( abi, abi_serializer_max_time );
      auto action_type = abis.get_action_type(action);
      EOS_ASSERT(!action_type.empty(), action_validate_exception, "Unknown action ${action} in contract ${contract}", ("action", action)("contract", code));
      try {
         auto binargs = abis.variant_to_binary(action_type, args, abi_serializer_max_time);
         _binargs = string(binargs.begin(), binargs.end());
      } EOS_RETHROW_EXCEPTIONS(chain::invalid_action_args_exception,
                                "'${args}' is invalid args for action '${action}' code '${code}'. expected '${proto}'",
                                ("args", args)("action", action)("code", code)("proto", action_abi_to_variant(abi, action_type)))
   }
}

void unpack_args( string& _rawabi, uint64_t code, uint64_t action, string& _binargs, string& _args ) {
   abi_def abi;
   bytes rawabi = bytes(_rawabi.data(), _rawabi.data() + _rawabi.size());
   bytes binargs = bytes(_binargs.data(), _binargs.data() + _binargs.size());

   if( abi_serializer::to_abi(rawabi, abi) ) {
      abi_serializer abis( abi, abi_serializer_max_time );
      auto args = abis.binary_to_variant( abis.get_action_type( action ), binargs, abi_serializer_max_time );
      _args = fc::json::to_string(args);
   } else {
      EOS_ASSERT(false, abi_not_found_exception, "No ABI found for ${contract}", ("contract", code));
   }
}
