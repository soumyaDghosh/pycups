typedef int... time_t;
typedef enum http_encoding_e		
{
  HTTP_ENCODING_LENGTH,			
  HTTP_ENCODING_CHUNKED,		
  HTTP_ENCODING_FIELDS			
} http_encoding_t;
typedef enum http_encryption_e		
{
  HTTP_ENCRYPTION_IF_REQUESTED,		
  HTTP_ENCRYPTION_NEVER,		
  HTTP_ENCRYPTION_REQUIRED,		
  HTTP_ENCRYPTION_ALWAYS		
} http_encryption_t;
typedef enum http_field_e		
{
  HTTP_FIELD_UNKNOWN = -1,		
  HTTP_FIELD_ACCEPT,			
  HTTP_FIELD_ACCEPT_CH,			
  HTTP_FIELD_ACCEPT_ENCODING,		
  HTTP_FIELD_ACCEPT_LANGUAGE,		
  HTTP_FIELD_ACCEPT_RANGES,		
  HTTP_FIELD_ACCESS_CONTROL_ALLOW_CREDENTIALS,
  HTTP_FIELD_ACCESS_CONTROL_ALLOW_HEADERS,
  HTTP_FIELD_ACCESS_CONTROL_ALLOW_METHODS,
  HTTP_FIELD_ACCESS_CONTROL_ALLOW_ORIGIN,
  HTTP_FIELD_ACCESS_CONTROL_EXPOSE_HEADERS,
  HTTP_FIELD_ACCESS_CONTROL_MAX_AGE,	
  HTTP_FIELD_ACCESS_CONTROL_REQUEST_HEADERS,
  HTTP_FIELD_ACCESS_CONTROL_REQUEST_METHOD,
  HTTP_FIELD_AGE,			
  HTTP_FIELD_ALLOW,			
  HTTP_FIELD_AUTHENTICATION_CONTROL,	
  HTTP_FIELD_AUTHENTICATION_INFO,	
  HTTP_FIELD_AUTHORIZATION,		
  HTTP_FIELD_CACHE_CONTROL,		
  HTTP_FIELD_CACHE_STATUS,		
  HTTP_FIELD_CERT_NOT_AFTER,		
  HTTP_FIELD_CERT_NOT_BEFORE,		
  HTTP_FIELD_CONNECTION,		
  HTTP_FIELD_CONTENT_DISPOSITION,	
  HTTP_FIELD_CONTENT_ENCODING,		
  HTTP_FIELD_CONTENT_LANGUAGE,		
  HTTP_FIELD_CONTENT_LENGTH,		
  HTTP_FIELD_CONTENT_LOCATION,		
  HTTP_FIELD_CONTENT_RANGE,		
  HTTP_FIELD_CONTENT_SECURITY_POLICY,	
  HTTP_FIELD_CONTENT_SECURITY_POLICY_REPORT_ONLY,
  HTTP_FIELD_CONTENT_TYPE,		
  HTTP_FIELD_CROSS_ORIGIN_EMBEDDER_POLICY,
  HTTP_FIELD_CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY,
  HTTP_FIELD_CROSS_ORIGIN_OPENER_POLICY,
  HTTP_FIELD_CROSS_ORIGIN_OPENER_POLICY_REPORT_ONLY,
  HTTP_FIELD_CROSS_ORIGIN_RESOURCE_POLICY,
  HTTP_FIELD_DASL,			
  HTTP_FIELD_DATE,			
  HTTP_FIELD_DAV,			
  HTTP_FIELD_DEPTH,			
  HTTP_FIELD_DESTINATION,		
  HTTP_FIELD_ETAG,			
  HTTP_FIELD_EXPIRES,			
  HTTP_FIELD_FORWARDED,			
  HTTP_FIELD_FROM,			
  HTTP_FIELD_HOST,			
  HTTP_FIELD_IF,			
  HTTP_FIELD_IF_MATCH,			
  HTTP_FIELD_IF_MODIFIED_SINCE,		
  HTTP_FIELD_IF_NONE_MATCH,		
  HTTP_FIELD_IF_RANGE,			
  HTTP_FIELD_IF_SCHEDULE_TAG_MATCH,	
  HTTP_FIELD_IF_UNMODIFIED_SINCE,	
  HTTP_FIELD_KEEP_ALIVE,		
  HTTP_FIELD_LAST_MODIFIED,		
  HTTP_FIELD_LINK,			
  HTTP_FIELD_LOCATION,			
  HTTP_FIELD_LOCK_TOKEN,		
  HTTP_FIELD_MAX_FORWARDS,		
  HTTP_FIELD_OPTIONAL_WWW_AUTHENTICATE,	
  HTTP_FIELD_ORIGIN,			
  HTTP_FIELD_OSCORE,			
  HTTP_FIELD_OVERWRITE,			
  HTTP_FIELD_PRAGMA,			
  HTTP_FIELD_PROXY_AUTHENTICATE,	
  HTTP_FIELD_PROXY_AUTHENTICATION_INFO,	
  HTTP_FIELD_PROXY_AUTHORIZATION,	
  HTTP_FIELD_PROXY_STATUS,		
  HTTP_FIELD_PUBLIC,			
  HTTP_FIELD_RANGE,			
  HTTP_FIELD_REFERER,			
  HTTP_FIELD_REFRESH,			
  HTTP_FIELD_REPLAY_NONCE,		
  HTTP_FIELD_RETRY_AFTER,		
  HTTP_FIELD_SCHEDULE_REPLY,		
  HTTP_FIELD_SCHEDULE_TAG,		
  HTTP_FIELD_SERVER,			
  HTTP_FIELD_STRICT_TRANSPORT_SECURITY,	
  HTTP_FIELD_TE,			
  HTTP_FIELD_TIMEOUT,			
  HTTP_FIELD_TRAILER,			
  HTTP_FIELD_TRANSFER_ENCODING,		
  HTTP_FIELD_UPGRADE,			
  HTTP_FIELD_USER_AGENT,		
  HTTP_FIELD_VARY,			
  HTTP_FIELD_VIA,			
  HTTP_FIELD_WWW_AUTHENTICATE,		
  HTTP_FIELD_X_CONTENT_OPTIONS,		
  HTTP_FIELD_X_FRAME_OPTIONS,		
  HTTP_FIELD_MAX			
} http_field_t;
typedef enum http_keepalive_e		
{
  HTTP_KEEPALIVE_OFF = 0,		
  HTTP_KEEPALIVE_ON			
} http_keepalive_t;
enum http_resolve_e			
{
  HTTP_RESOLVE_DEFAULT = 0,		
  HTTP_RESOLVE_FQDN = 1,		
  HTTP_RESOLVE_FAXOUT = 2		
};
typedef unsigned http_resolve_t;	
typedef enum http_state_e		
{
  HTTP_STATE_ERROR = -1,		
  HTTP_STATE_WAITING,			
  HTTP_STATE_CONNECT,			
  HTTP_STATE_COPY,			
  HTTP_STATE_COPY_SEND,			
  HTTP_STATE_DELETE,			
  HTTP_STATE_DELETE_SEND,		
  HTTP_STATE_GET,			
  HTTP_STATE_GET_SEND,			
  HTTP_STATE_HEAD,			
  HTTP_STATE_LOCK,			
  HTTP_STATE_LOCK_RECV,			
  HTTP_STATE_LOCK_SEND,			
  HTTP_STATE_MKCOL,			
  HTTP_STATE_MOVE,			
  HTTP_STATE_MOVE_SEND,			
  HTTP_STATE_OPTIONS,			
  HTTP_STATE_POST,			
  HTTP_STATE_POST_RECV,			
  HTTP_STATE_POST_SEND,			
  HTTP_STATE_PROPFIND,			
  HTTP_STATE_PROPFIND_RECV,		
  HTTP_STATE_PROPFIND_SEND,		
  HTTP_STATE_PROPPATCH,			
  HTTP_STATE_PROPPATCH_RECV,		
  HTTP_STATE_PROPPATCH_SEND,		
  HTTP_STATE_PUT,			
  HTTP_STATE_PUT_RECV,			
  HTTP_STATE_TRACE,			
  HTTP_STATE_UNLOCK,			
  HTTP_STATE_STATUS,			
  HTTP_STATE_UNKNOWN_METHOD,		
  HTTP_STATE_UNKNOWN_VERSION,		
  HTTP_STATE_MAX			
} http_state_t;
typedef enum http_status_e		
{
  HTTP_STATUS_ERROR = -1,		
  HTTP_STATUS_NONE = 0,			
  HTTP_STATUS_CONTINUE = 100,		
  HTTP_STATUS_SWITCHING_PROTOCOLS,	
  HTTP_STATUS_OK = 200,			
  HTTP_STATUS_CREATED,			
  HTTP_STATUS_ACCEPTED,			
  HTTP_STATUS_NOT_AUTHORITATIVE,	
  HTTP_STATUS_NO_CONTENT,		
  HTTP_STATUS_RESET_CONTENT,		
  HTTP_STATUS_PARTIAL_CONTENT,		
  HTTP_STATUS_MULTI_STATUS,		
  HTTP_STATUS_ALREADY_REPORTED,		
  HTTP_STATUS_MULTIPLE_CHOICES = 300,	
  HTTP_STATUS_MOVED_PERMANENTLY,	
  HTTP_STATUS_FOUND,			
  HTTP_STATUS_SEE_OTHER,		
  HTTP_STATUS_NOT_MODIFIED,		
  HTTP_STATUS_USE_PROXY,		
  HTTP_STATUS_TEMPORARY_REDIRECT = 307,	
  HTTP_STATUS_PERMANENT_REDIRECT,	
  HTTP_STATUS_BAD_REQUEST = 400,	
  HTTP_STATUS_UNAUTHORIZED,		
  HTTP_STATUS_PAYMENT_REQUIRED,		
  HTTP_STATUS_FORBIDDEN,		
  HTTP_STATUS_NOT_FOUND,		
  HTTP_STATUS_METHOD_NOT_ALLOWED,	
  HTTP_STATUS_NOT_ACCEPTABLE,		
  HTTP_STATUS_PROXY_AUTHENTICATION_REQUIRED,
  HTTP_STATUS_REQUEST_TIMEOUT,		
  HTTP_STATUS_CONFLICT,			
  HTTP_STATUS_GONE,			
  HTTP_STATUS_LENGTH_REQUIRED,		
  HTTP_STATUS_PRECONDITION_FAILED,	
  HTTP_STATUS_CONTENT_TOO_LARGE,	
  HTTP_STATUS_URI_TOO_LONG,		
  HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE,	
  HTTP_STATUS_RANGE_NOT_SATISFIABLE,	
  HTTP_STATUS_EXPECTATION_FAILED,	
  HTTP_STATUS_MISDIRECTED_REQUEST = 421,
  HTTP_STATUS_UNPROCESSABLE_CONTENT,	
  HTTP_STATUS_LOCKED,			
  HTTP_STATUS_FAILED_DEPENDENCY,	
  HTTP_STATUS_TOO_EARLY,		
  HTTP_STATUS_UPGRADE_REQUIRED,		
  HTTP_STATUS_PRECONDITION_REQUIRED = 428,
  HTTP_STATUS_TOO_MANY_REQUESTS,	
  HTTP_STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE = 431,
  HTTP_STATUS_UNAVAILABLE_FOR_LEGAL_REASONS = 451,
  HTTP_STATUS_SERVER_ERROR = 500,	
  HTTP_STATUS_NOT_IMPLEMENTED,		
  HTTP_STATUS_BAD_GATEWAY,		
  HTTP_STATUS_SERVICE_UNAVAILABLE,	
  HTTP_STATUS_GATEWAY_TIMEOUT,		
  HTTP_STATUS_HTTP_VERSION_NOT_SUPPORTED,
  HTTP_STATUS_INSUFFICIENT_STORAGE = 507,
  HTTP_STATUS_LOOP_DETECTED,		
  HTTP_STATUS_NETWORK_AUTHENTICATION_REQUIRED = 511,
  HTTP_STATUS_CUPS_AUTHORIZATION_CANCELED = 1000,
  HTTP_STATUS_CUPS_PKI_ERROR		
} http_status_t;
typedef enum http_trust_e		
{
  HTTP_TRUST_OK = 0,			
  HTTP_TRUST_INVALID,			
  HTTP_TRUST_CHANGED,			
  HTTP_TRUST_EXPIRED,			
  HTTP_TRUST_RENEWED,			
  HTTP_TRUST_UNKNOWN			
} http_trust_t;
typedef enum http_uri_status_e		
{
  HTTP_URI_STATUS_OVERFLOW = -8,	
  HTTP_URI_STATUS_BAD_ARGUMENTS = -7,	
  HTTP_URI_STATUS_BAD_RESOURCE = -6,	
  HTTP_URI_STATUS_BAD_PORT = -5,	
  HTTP_URI_STATUS_BAD_HOSTNAME = -4,	
  HTTP_URI_STATUS_BAD_USERNAME = -3,	
  HTTP_URI_STATUS_BAD_SCHEME = -2,	
  HTTP_URI_STATUS_BAD_URI = -1,		
  HTTP_URI_STATUS_OK = 0,		
  HTTP_URI_STATUS_MISSING_SCHEME,	
  HTTP_URI_STATUS_UNKNOWN_SCHEME,	
  HTTP_URI_STATUS_MISSING_RESOURCE	
} http_uri_status_t;
typedef enum http_uri_coding_e		
{
  HTTP_URI_CODING_NONE = 0,		
  HTTP_URI_CODING_USERNAME = 1,		
  HTTP_URI_CODING_HOSTNAME = 2,		
  HTTP_URI_CODING_RESOURCE = 4,		
  HTTP_URI_CODING_MOST = 7,		
  HTTP_URI_CODING_QUERY = 8,		
  HTTP_URI_CODING_ALL = 15,		
  HTTP_URI_CODING_RFC6874 = 16		
} http_uri_coding_t;
typedef enum http_version_e		
{
  HTTP_VERSION_0_9 = 9,			
  HTTP_VERSION_1_0 = 100,		
  HTTP_VERSION_1_1 = 101		
} http_version_t;
typedef union _http_addr_u http_addr_t;
typedef struct http_addrlist_s http_addrlist_t;
typedef struct _http_s http_t;		
typedef bool (*http_resolve_cb_t)(void *data);
typedef bool (*http_timeout_cb_t)(http_t *http, void *user_data);
http_t		*httpAcceptConnection(int fd, bool blocking);
bool		httpAddrClose(http_addr_t *addr, int fd);
http_addrlist_t	*httpAddrConnect(http_addrlist_t *addrlist, int *sock, int msec, int *cancel);
http_addrlist_t	*httpAddrCopyList(http_addrlist_t *src);
void		httpAddrFreeList(http_addrlist_t *addrlist);
int		httpAddrGetFamily(http_addr_t *addr);
size_t		httpAddrGetLength(const http_addr_t *addr);
http_addrlist_t	*httpAddrGetList(const char *hostname, int family, const char *service);
int		httpAddrGetPort(http_addr_t *addr);
char		*httpAddrGetString(const http_addr_t *addr, char *s, size_t slen);
bool		httpAddrIsAny(const http_addr_t *addr);
bool		httpAddrIsEqual(const http_addr_t *addr1, const http_addr_t *addr2);
bool		httpAddrIsLocalhost(const http_addr_t *addr);
int		httpAddrListen(http_addr_t *addr, int port);
char		*httpAddrLookup(const http_addr_t *addr, char *name, size_t namelen);
void		httpAddrSetPort(http_addr_t *addr, int port);
http_uri_status_t httpAssembleURI(http_uri_coding_t encoding, char *uri, size_t urilen, const char *scheme, const char *username, const char *host, int port, const char *resource);
http_uri_status_t httpAssembleURIf(http_uri_coding_t encoding, char *uri, size_t urilen, const char *scheme, const char *username, const char *host, int port, const char *resourcef, ...);
char		*httpAssembleUUID(const char *server, int port, const char *name, int number, char *buffer, size_t bufsize);
void		httpClearFields(http_t *http);
void		httpClose(http_t *http);
void		httpClearCookie(http_t *http);
http_t		*httpConnect(const char *host, int port, http_addrlist_t *addrlist, int family, http_encryption_t encryption, bool blocking, int msec, int *cancel);
bool		httpConnectAgain(http_t *http, int msec, int *cancel);
http_t		*httpConnectURI(const char *uri, char *host, size_t hsize, int *port, char *resource, size_t rsize, bool blocking, int msec, int *cancel, bool require_ca);
char		*httpCopyPeerCredentials(http_t *http);
char		*httpDecode64(char *out, size_t *outlen, const char *in, const char **end);
char		*httpEncode64(char *out, size_t outlen, const char *in, size_t inlen, bool url);
http_field_t	httpFieldValue(const char *name);
void		httpFlush(http_t *http);
int		httpFlushWrite(http_t *http);
time_t		httpGetActivity(http_t *http);
http_addr_t	*httpGetAddress(http_t *http);
const char	*httpGetAuthString(http_t *http);
bool		httpGetBlocking(http_t *http);
const char	*httpGetContentEncoding(http_t *http);
const char	*httpGetCookie(http_t *http);
const char	*httpGetDateString(time_t t, char *s, size_t slen);
time_t		httpGetDateTime(const char *s);
http_encryption_t httpGetEncryption(http_t *http);
int		httpGetError(http_t *http);
http_status_t	httpGetExpect(http_t *http);
int		httpGetFd(http_t *http);
const char	*httpGetField(http_t *http, http_field_t field);
const char	*httpGetHostname(http_t *http, char *s, size_t slen);
http_keepalive_t	httpGetKeepAlive(http_t *http);
off_t		httpGetLength(http_t *http);
size_t		httpGetPending(http_t *http);
size_t		httpGetReady(http_t *http);
size_t		httpGetRemaining(http_t *http);
http_state_t	httpGetState(http_t *http);
http_status_t	httpGetStatus(http_t *http);
char		*httpGetSubField(http_t *http, http_field_t field, const char *name, char *value, size_t valuelen);
http_version_t	httpGetVersion(http_t *http);
char		*httpGets(http_t *http, char *line, size_t length);
void		httpInitialize(void);
bool		httpIsChunked(http_t *http);
bool		httpIsEncrypted(http_t *http);
ssize_t		httpPeek(http_t *http, char *buffer, size_t length);
ssize_t		httpPrintf(http_t *http, const char *format, ...);
ssize_t		httpRead(http_t *http, char *buffer, size_t length);
http_state_t	httpReadRequest(http_t *http, char *resource, size_t resourcelen);
const char	*httpResolveHostname(http_t *http, char *buffer, size_t bufsize);
const char	*httpResolveURI(const char *uri, char *resolved_uri, size_t resolved_size, http_resolve_t options, http_resolve_cb_t cb, void *cb_data);
http_uri_status_t httpSeparateURI(http_uri_coding_t decoding, const char *uri, char *scheme, size_t schemelen, char *username, size_t usernamelen, char *host, size_t hostlen, int *port, char *resource, size_t resourcelen);
void		httpSetAuthString(http_t *http, const char *scheme, const char *data);
void		httpSetBlocking(http_t *http, bool b);
void		httpSetCookie(http_t *http, const char *cookie);
//bool		httpSetCredentialsAndKey(http_t *http, const char *credentials, const char *key);
void		httpSetDefaultField(http_t *http, http_field_t field, const char *value);
bool		httpSetEncryption(http_t *http, http_encryption_t e);
void		httpSetExpect(http_t *http, http_status_t expect);
void		httpSetField(http_t *http, http_field_t field, const char *value);
void		httpSetKeepAlive(http_t *http, http_keepalive_t keep_alive);
void		httpSetLength(http_t *http, size_t length);
void		httpSetTimeout(http_t *http, double timeout, http_timeout_cb_t cb, void *user_data);
void		httpShutdown(http_t *http);
const char	*httpStateString(http_state_t state);
const char	*httpStatusString(http_status_t status);
http_status_t	httpUpdate(http_t *http);
const char	*httpURIStatusString(http_uri_status_t status);
bool		httpWait(http_t *http, int msec);
ssize_t		httpWrite(http_t *http, const char *buffer, size_t length);
bool		httpWriteRequest(http_t *http, const char *method, const char *uri);
bool		httpWriteResponse(http_t *http, http_status_t status);
