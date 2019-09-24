#include <eosio/chain/block_log.hpp>
#include <eosio/chain/transaction.hpp>
#include "block_log_.hpp"
#include "json.hpp"

using namespace eosio::chain;

int block_on_action(int block, PyObject* trx);
int block_on_raw_action(int block, string act);

#define FC_LOG_AND_RETURN( ... )  \
   catch( const boost::interprocess::bad_alloc& ) {\
      throw;\
   } catch( fc::exception& er ) { \
      wlog( "${details}", ("details",er.to_detail_string()) ); \
      return; \
   } catch( const std::exception& e ) {  \
      fc::exception fce( \
                FC_LOG_MESSAGE( warn, "rethrow ${what}: ",FC_FORMAT_ARG_PARAMS( __VA_ARGS__  )("what",e.what()) ), \
                fc::std_exception_code,\
                BOOST_CORE_TYPEID(e).name(), \
                e.what() ) ; \
      wlog( "${details}", ("details",fce.to_detail_string()) ); \
      return; \
   } catch( ... ) {  \
      fc::unhandled_exception e( \
                FC_LOG_MESSAGE( warn, "rethrow", FC_FORMAT_ARG_PARAMS( __VA_ARGS__) ), \
                std::current_exception() ); \
      wlog( "${details}", ("details",e.to_detail_string()) ); \
      return; \
   }

void block_log_parse_transactions_(string& path, int start_block, int end_block) {
   eosio::chain::block_log log(path);
   for (int i=start_block;i<=end_block;i++) {
      signed_block_ptr block;
      try {
         block = log.read_block_by_num(i);
         if (!block) {
            wlog("bad block number ${n}", ("n", i));
            break;
         }
         for (auto& tr : block->transactions) {
            if (!tr.trx.contains<packed_transaction>()) {
               continue;
            }
            packed_transaction& pt = tr.trx.get<packed_transaction>();
            signed_transaction st = pt.get_signed_transaction();
            PyObject* json = python::json::to_string(fc::variant(st));
            int ret = block_on_action(i, json);
            if (!ret) {
               return;
            }
         }
      } FC_LOG_AND_RETURN();
   }
}

void block_log_get_transactions_(string& path, int block_num) {
   eosio::chain::block_log log(path);

   signed_block_ptr block;
   try {
      block = log.read_block_by_num(block_num);
      if (!block) {
         wlog("bad block number ${n}", ("n", block_num));
         return;
      }
      for (auto& tr : block->transactions) {
         if (!tr.trx.contains<packed_transaction>()) {
            continue;
         }
         packed_transaction& pt = tr.trx.get<packed_transaction>();
         signed_transaction st = pt.get_signed_transaction();
         PyObject* json = python::json::to_string(fc::variant(st));
         int ret = block_on_action(block_num, json);
         if (!ret) {
            return;
         }
      }
   } FC_LOG_AND_RETURN();

}

void block_log_parse_raw_transactions_(string& path, int start, int end) {
   eosio::chain::block_log log(path);

   signed_block_ptr block;
   for (int block_num=start;block_num<end;block_num++) {
      try {
         block = log.read_block_by_num(block_num);
         if (!block) {
            wlog("bad block number ${n}", ("n", block_num));
            return;
         }
         for (auto& tr : block->transactions) {
            if (!tr.trx.contains<packed_transaction>()) {
               continue;
            }
            packed_transaction& pt = tr.trx.get<packed_transaction>();
            signed_transaction st = pt.get_signed_transaction();
            for (auto& act: st.actions) {
               auto v = fc::raw::pack(act);
               string raw_act(v.begin(), v.end());
               int ret = block_on_raw_action(block_num, raw_act);
               if (!ret) {
                  return;
               }
            }
         }
      } FC_LOG_AND_RETURN();
   }
}


PyObject* block_log_get_block_(string& path, int block_num) {
   eosio::chain::block_log log(path);
   signed_block_ptr block;
   try {
      block = log.read_block_by_num(block_num);
      if (!block) {
         wlog("bad block number ${n}", ("n", block_num));
         return py_new_none();
      }
      return python::json::to_string(fc::variant(block));
   } FC_LOG_AND_DROP();
   return py_new_none();
}
