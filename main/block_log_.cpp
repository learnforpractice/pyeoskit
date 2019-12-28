#include <eosio/chain/block_log.hpp>
#include <eosio/chain/transaction.hpp>

#include <fc/io/json.hpp>

#include "block_log_.hpp"
#include "json.hpp"

using namespace eosio::chain;

int block_log_on_transaction(int block, PyObject* trx);
int block_log_on_raw_action(int block, string& act);
int block_log_on_action(int block, string& act);

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


#define FC_LOG_AND_RETURN_FALSE( ... )  \
   catch( const boost::interprocess::bad_alloc& ) {\
      throw;\
   } catch( fc::exception& er ) { \
      wlog( "${details}", ("details",er.to_detail_string()) ); \
      return false; \
   } catch( const std::exception& e ) {  \
      fc::exception fce( \
                FC_LOG_MESSAGE( warn, "rethrow ${what}: ",FC_FORMAT_ARG_PARAMS( __VA_ARGS__  )("what",e.what()) ), \
                fc::std_exception_code,\
                BOOST_CORE_TYPEID(e).name(), \
                e.what() ) ; \
      wlog( "${details}", ("details",fce.to_detail_string()) ); \
      return false; \
   } catch( ... ) {  \
      fc::unhandled_exception e( \
                FC_LOG_MESSAGE( warn, "rethrow", FC_FORMAT_ARG_PARAMS( __VA_ARGS__) ), \
                std::current_exception() ); \
      wlog( "${details}", ("details",e.to_detail_string()) ); \
      return false; \
   }

void *block_log_new(string& path) {
   eosio::chain::block_log *block_log_ptr = new eosio::chain::block_log(path);
   return (void *)block_log_ptr;
}

void block_log_free(void *block_log_ptr) {
   if (block_log_ptr == nullptr) {
      return;
   }
   delete (eosio::chain::block_log*)block_log_ptr;
}

uint32_t block_log_get_first_block_num_(void *block_log_ptr) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;
   return log.first_block_num();
}

PyObject* block_log_read_block_by_num_(void *block_log_ptr, uint32_t block_num) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;
   return python::json::to_string(fc::variant(log.read_block_by_num(block_num)));
}

PyObject* block_log_get_head_block_(void *block_log_ptr) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;
   return python::json::to_string(fc::variant(log.head()));
}

bool block_log_parse_transactions_(void *block_log_ptr, int start_block, int end_block) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;
   for (int i=start_block;i<=end_block;i++) {
      signed_block_ptr block;
      try {
         block = log.read_block_by_num(i);
         if (!block) {
            wlog("bad block number ${n}", ("n", i));
            return false;
         }
         for (auto& tr : block->transactions) {
            if (!tr.trx.contains<packed_transaction>()) {
               continue;
            }
            packed_transaction& pt = tr.trx.get<packed_transaction>();
            signed_transaction st = pt.get_signed_transaction();
            PyObject* json = python::json::to_string(fc::variant(st));
            int ret = block_log_on_transaction(i, json);
            if (!ret) {
               return false;
            }
         }
      } FC_LOG_AND_RETURN_FALSE();
   }
   return true;
}

void block_log_get_transactions_(void *block_log_ptr, int block_num) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;

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
         int ret = block_log_on_transaction(block_num, json);
         if (!ret) {
            return;
         }
      }
   } FC_LOG_AND_RETURN();

}

void block_log_parse_actions_(void *block_log_ptr, int start, int end) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;

   signed_block_ptr block;
   for (int block_num=start;block_num<=end;block_num++) {
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
               auto s = fc::json::to_string(act);
               int ret = block_log_on_action(block_num, s);
               if (!ret) {
                  return;
               }
            }
         }
      } FC_LOG_AND_RETURN();
   }
}

void block_log_parse_raw_actions_(void *block_log_ptr, int start, int end) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;

   signed_block_ptr block;
   for (int block_num=start;block_num<=end;block_num++) {
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
               int ret = block_log_on_raw_action(block_num, raw_act);
               if (!ret) {
                  return;
               }
            }
         }
      } FC_LOG_AND_RETURN();
   }
}


PyObject* block_log_get_block_(void *block_log_ptr, int block_num) {
   eosio::chain::block_log &log = *(eosio::chain::block_log*)block_log_ptr;
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
