# nsITLSServerSocket (netwerk/base/nsITLSServerSocket.idl)

source: netwerk/base/nsITLSServerSocket.idl
source-hash: a3588ddce2970a0fd8dd259e74a13c7a827f7bfe

- 継承: nsIServerSocket
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `attribute nsIX509Cert serverCert`: serverCert
- `void setSessionTickets(boolean aSessionTickets)`: setSessionTickets
- `const unsigned long REQUEST_NEVER`: Values for setRequestClientCertificate
- `const unsigned long REQUEST_FIRST_HANDSHAKE`: (未記入)
- `const unsigned long REQUEST_ALWAYS`: (未記入)
- `const unsigned long REQUIRE_FIRST_HANDSHAKE`: (未記入)
- `const unsigned long REQUIRE_ALWAYS`: (未記入)
- `void setRequestClientCertificate(unsigned long aRequestClientCert)`: setRequestClientCertificate
- `void setVersionRange(unsigned short aMinVersion, unsigned short aMaxVersion)`: setVersionRange

# nsITLSClientStatus (netwerk/base/nsITLSServerSocket.idl)

source: netwerk/base/nsITLSServerSocket.idl
source-hash: a3588ddce2970a0fd8dd259e74a13c7a827f7bfe

- 継承: nsISupports
- 役割: Security summary for a given TLS client connection being handled by a
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIX509Cert peerCert`: peerCert
- `const short SSL_VERSION_3`: Values for tlsVersionUsed, as defined by TLS
- `const short TLS_VERSION_1`: (未記入)
- `const short TLS_VERSION_1_1`: (未記入)
- `const short TLS_VERSION_1_2`: (未記入)
- `const short TLS_VERSION_1_3`: (未記入)
- `const short TLS_VERSION_UNKNOWN`: (未記入)
- `readonly attribute short tlsVersionUsed`: tlsVersionUsed
- `readonly attribute ACString cipherName`: cipherName
- `readonly attribute unsigned long keyLength`: keyLength
- `readonly attribute unsigned long macLength`: macLength

# nsITLSServerConnectionInfo (netwerk/base/nsITLSServerSocket.idl)

source: netwerk/base/nsITLSServerSocket.idl
source-hash: a3588ddce2970a0fd8dd259e74a13c7a827f7bfe

- 継承: nsISupports
- 役割: Connection info for a given TLS client connection being handled by a
- 実装: (未記入)

## メソッド / 属性
- `void setSecurityObserver(nsITLSServerSecurityObserver observer)`: setSecurityObserver
- `readonly attribute nsITLSServerSocket serverSocket`: serverSocket
- `readonly attribute nsITLSClientStatus status`: status

# nsITLSServerSecurityObserver (netwerk/base/nsITLSServerSocket.idl)

source: netwerk/base/nsITLSServerSocket.idl
source-hash: a3588ddce2970a0fd8dd259e74a13c7a827f7bfe

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onHandshakeDone(nsITLSServerSocket aServer, nsITLSClientStatus aStatus)`: onHandsakeDone
