#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>   // For struct sockaddr_in and related constants
#include <arpa/inet.h>    // For inet_pton(), htons(), etc. (optional, but often needed)
#include <unistd.h>

#define port 5200

// Create Socket
// Bind Address and Port to Socket
// Request Connection // Accept Connection
// Duplicate Socket


int main() {

  // create socket
  int server_socket = socket(AF_INET, SOCK_STREAM, 0);
  if (server_socket == -1) {
    std::cerr << "ERROR: Could not create Socket" << std::endl;
  } else {
    std::cout << "Successfully created Socket" << std::endl;
  }

  // bind ip address and port to socket
  struct sockaddr_in server_addr, client_addr;
  server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
  server_addr.sin_port = htons(port);
  // server_addr.sin_zero = ;
  server_addr.sin_family = AF_INET;
  int bind_server = bind(server_socket, (struct sockaddr *)&server_addr,
      sizeof(server_addr));

  if (bind_server < 0) {
    std::cerr << "ERROR: Could not bind socket" << std::endl;
  } else {
    std::cout << "Successfully bound Socket" << std::endl;
  }

  int listen_status = listen(server_socket, 5);
  if (listen_status < 0) {
    std::cerr << "Listener has failed" << std::endl;
  } else {
    std::cout << listen_status << std::endl;
  }

  // while there are no connections, wait

  
  return 0;
}
