# TLS Handshake
## Objectives
* Cipher suite negotiation
* Authentication of the server and optionally, the client
* Session key information exchange.

## Handshake steps
1. The client sends a "Client hello" message to the server, along with the client's random value and supported cipher suites.
2. The server responds by sending a "Server hello" message to the client, along with the server's random value.
3. The server sends its certificate to the client for authentication and may request a certificate from the client. The server sends the "Server hello done" message.
4. If the server has requested a certificate from the client, the client sends it.
5. The client creates a random Pre-Master Secret and encrypts it with the public key from the server's certificate, sending the encrypted Pre-Master Secret to the server.
6. The server receives the Pre-Master Secret. The server and client each generate the Master Secret and session keys based on the Pre-Master Secret.
7. The client sends "Change cipher spec" notification to server to indicate that the client will start using the new session keys for hashing and encrypting messages. Client also sends "Client finished" message.
8. Server receives "Change cipher spec" and switches its record layer security state to symmetric encryption using the session keys. Server sends "Server finished" message to the client.
9. Client and server can now exchange application data over the secured channel they have established. All messages sent from client to server and from server to client are encrypted using session key.

### Resuming a Secure Session
1. The client sends a "Client hello" message using the Session ID of the session to be resumed.
2. The server checks its session cache for a matching Session ID. If a match is found, and the server is able to resume the session, it sends a "Server hello" message with the Session ID.
> If a session ID match is not found, the server generates a new session ID and the TLS client and server perform a full handshake.

3. Client and server must exchange "Change cipher spec" messages and send "Client finished" and "Server finished" messages.
4. Client and server can now resume application data exchange over the secure channel.
