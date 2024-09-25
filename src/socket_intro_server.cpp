#include <iostream>
#include <cstring>
#include <ratio>
#include <string>
#include <vector>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <thread>
#include <mutex>
#include <chrono>

#define port 5200

// Create Socket
// Bind Address and Port to Socket
// Request Connection // Accept Connection
// Duplicate Socket

void count_to_client(int start, int up_to, int client_socket) {
  static int client_count = 0;
  client_count ++;
  std::cout << "Client Count: " << client_count << std::endl;
  char ack_buffer[10];
  for (int i = start; i < start + up_to; i++) {
    const std::string message = "Counter is at: " + std::to_string(i);
    int send_status = send(client_socket, message.c_str(), message.size(), 0);
    if (send_status < 0) {
      std::cerr << "ERROR: Could not send packet to client " << client_socket << std::endl;
      close(client_socket);
    }

    int ack_status = recv(client_socket, ack_buffer, sizeof(ack_buffer), 0);
    if (ack_status < 0) {
      std::cerr << "ERROR: ACK Failure from client " << client_socket << std::endl;
      close(client_socket);
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(100));

  }
  close(client_socket);
}

int main()
{
	// create socket (domain, type, protocol)
  // AF_INET for IPV4, PF_INET used to be used 
  // AF (Address Family)
  // PF (Protocol Family)
  
  //TODO: Server only runs in TCP, need to make it adaptable to UDP
  // SOCK_STREAM is for TCP
  // SOCK_DGRAM for UDP
	int server_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (server_socket == -1) {
		std::cerr << "ERROR: Could not create Socket" << std::endl;
    return 1;
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
    return 1;
	} else {
		std::cout << "Successfully bound Socket" << std::endl;
	}

	int listen_status = listen(server_socket, 5);
	if (listen_status < 0) {
		std::cerr << "Listener has failed" << std::endl;
    return 1;
	} else {
		std::cout << "Listener has succeeded" << std::endl;
	}

  // we open a new client_socker for each new client
  std::vector<int> client_socket_vec;
  std::vector<std::thread> thread_vec;

	// Accept connections
	sockaddr_in client_address;
	socklen_t client_size = sizeof(client_address);
  // stops execution
  while (true) {

    int client_socket = accept(
      server_socket, (struct sockaddr *)&client_address, &client_size);

    if (client_socket == -1) {
      std::cerr << "Error accepting connection" << std::endl;
      continue;
    } 



    std::thread t1( count_to_client, 0, 100,client_socket);
    t1.detach();
    
  }

  // Get client's IP address and port
  // char clientIP[INET_ADDRSTRLEN];
  // inet_ntop(AF_INET, &(client_address.sin_addr), clientIP, INET_ADDRSTRLEN);
  // int clientPort = ntohs(client_address.sin_port);
  // std::cout << "Accepted connection from " << clientIP << ":" << clientPort
  //           << std::endl;

  // Receive data from the client
  // char buffer[1024] = {0};
  // recv(client_socket, buffer, sizeof(buffer), 0);
  // std::cout << "Client says: " << buffer << std::endl;

  // Sending data to Client
  // const char *message = "Hello from server!";
  // send(client_socket, message, strlen(message), 0);
	// while there are no connections, wait

  // Close sockets
  // close(client_socket);

  close(server_socket);
  return 0;
}
