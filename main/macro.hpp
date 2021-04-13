#pragma once

void set_last_error_(const string& error);
void get_last_error_(string& error);

#undef FC_LOG_AND_DROP
#define FC_LOG_AND_DROP( ... )  \
   catch( const boost::interprocess::bad_alloc& ) {\
      throw;\
   } catch( fc::exception& er ) { \
      set_last_error_(er.to_detail_string()); \
   } catch( const std::exception& e ) {  \
      fc::exception fce( \
                FC_LOG_MESSAGE( warn, "rethrow ${what}: ",FC_FORMAT_ARG_PARAMS( __VA_ARGS__  )("what",e.what()) ), \
                fc::std_exception_code,\
                BOOST_CORE_TYPEID(e).name(), \
                e.what() ) ; \
      set_last_error_(fce.to_detail_string()); \
   } catch( ... ) {  \
      fc::unhandled_exception e( \
                FC_LOG_MESSAGE( warn, "rethrow", FC_FORMAT_ARG_PARAMS( __VA_ARGS__) ), \
                std::current_exception() ); \
      set_last_error_(e.to_detail_string()); \
   }
