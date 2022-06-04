# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\ambience_console_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\ambience_console_autogen.dir\\ParseCache.txt"
  "ambience_console_autogen"
  )
endif()
