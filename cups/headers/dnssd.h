typedef struct _cups_dnssd_s cups_dnssd_t;
enum cups_dnssd_flags_e			
{
  CUPS_DNSSD_FLAGS_NONE = 0,		
  CUPS_DNSSD_FLAGS_ADD = 1,		
  CUPS_DNSSD_FLAGS_ERROR = 2,		
  CUPS_DNSSD_FLAGS_COLLISION = 4,	
  CUPS_DNSSD_FLAGS_HOST_CHANGE = 8,	
  CUPS_DNSSD_FLAGS_NETWORK_CHANGE = 16,	
  CUPS_DNSSD_FLAGS_MORE = 128		
};
typedef unsigned cups_dnssd_flags_t;	
typedef enum cups_dnssd_rrtype_e	
{
  CUPS_DNSSD_RRTYPE_A = 1,		
  CUPS_DNSSD_RRTYPE_NS,			
  CUPS_DNSSD_RRTYPE_CNAME = 5,		
  CUPS_DNSSD_RRTYPE_WKS = 11,		
  CUPS_DNSSD_RRTYPE_PTR,		
  CUPS_DNSSD_RRTYPE_TXT = 16,		
  CUPS_DNSSD_RRTYPE_RT = 21,		
  CUPS_DNSSD_RRTYPE_SIG = 24,		
  CUPS_DNSSD_RRTYPE_KEY,		
  CUPS_DNSSD_RRTYPE_AAAA = 28,		
  CUPS_DNSSD_RRTYPE_LOC,		
  CUPS_DNSSD_RRTYPE_KX = 36,		
  CUPS_DNSSD_RRTYPE_CERT,		
  CUPS_DNSSD_RRTYPE_RRSIG = 46,		
  CUPS_DNSSD_RRTYPE_DNSKEY = 48,	
  CUPS_DNSSD_RRTYPE_DHCID,		
  CUPS_DNSSD_RRTYPE_HTTPS = 65,		
  CUPS_DNSSD_RRTYPE_SPF = 99,		
  CUPS_DNSSD_RRTYPE_ANY = 255		
} cups_dnssd_rrtype_t;
typedef struct _cups_dnssd_browse_s cups_dnssd_browse_t;
typedef void (*cups_dnssd_browse_cb_t)(cups_dnssd_browse_t *browse, void *cb_data, cups_dnssd_flags_t flags, uint32_t if_index, const char *name, const char *regtype, const char *domain);
typedef void (*cups_dnssd_error_cb_t)(void *cb_data, const char *message);
typedef struct _cups_dnssd_query_s cups_dnssd_query_t;
typedef void (*cups_dnssd_query_cb_t)(cups_dnssd_query_t *query, void *cb_data, cups_dnssd_flags_t flags, uint32_t if_index, const char *fullname, uint16_t rrtype, const void *qdata, uint16_t qlen);
typedef struct _cups_dnssd_resolve_s cups_dnssd_resolve_t;
typedef void (*cups_dnssd_resolve_cb_t)(cups_dnssd_resolve_t *res, void *cb_data, cups_dnssd_flags_t flags, uint32_t if_index, const char *fullname, const char *host, uint16_t port, size_t num_txt, cups_option_t *txt);
typedef struct _cups_dnssd_service_s cups_dnssd_service_t;
typedef void (*cups_dnssd_service_cb_t)(cups_dnssd_service_t *service, void *cb_data, cups_dnssd_flags_t flags);
char		*cupsDNSSDCopyComputerName(cups_dnssd_t *dnssd, char *buffer, size_t bufsize);
char		*cupsDNSSDCopyHostName(cups_dnssd_t *dnssd, char *buffer, size_t bufsize);
void		cupsDNSSDDelete(cups_dnssd_t *dnssd);
size_t		cupsDNSSDGetConfigChanges(cups_dnssd_t *dnssd);
cups_dnssd_t	*cupsDNSSDNew(cups_dnssd_error_cb_t error_cb, void *cb_data);
void		cupsDNSSDBrowseDelete(cups_dnssd_browse_t *browser);
cups_dnssd_t	*cupsDNSSDBrowseGetContext(cups_dnssd_browse_t *browser);
cups_dnssd_browse_t *cupsDNSSDBrowseNew(cups_dnssd_t *dnssd, uint32_t if_index, const char *types, const char *domain, cups_dnssd_browse_cb_t browse_cb, void *cb_data);
void		cupsDNSSDQueryDelete(cups_dnssd_query_t *query);
cups_dnssd_t	*cupsDNSSDQueryGetContext(cups_dnssd_query_t *query);
cups_dnssd_query_t *cupsDNSSDQueryNew(cups_dnssd_t *dnssd, uint32_t if_index, const char *fullname, uint16_t rrtype, cups_dnssd_query_cb_t query_cb, void *cb_data);
void		cupsDNSSDResolveDelete(cups_dnssd_resolve_t *res);
cups_dnssd_t	*cupsDNSSDResolveGetContext(cups_dnssd_resolve_t *res);
cups_dnssd_resolve_t *cupsDNSSDResolveNew(cups_dnssd_t *dnssd, uint32_t if_index, const char *name, const char *type, const char *domain, cups_dnssd_resolve_cb_t resolve_cb, void *cb_data);
bool		cupsDNSSDServiceAdd(cups_dnssd_service_t *service, const char *types, const char *domain, const char *host, uint16_t port, size_t num_txt, cups_option_t *txt);
void		cupsDNSSDServiceDelete(cups_dnssd_service_t *service);
cups_dnssd_t	*cupsDNSSDServiceGetContext(cups_dnssd_service_t *service);
const char	*cupsDNSSDServiceGetName(cups_dnssd_service_t *service);
cups_dnssd_service_t *cupsDNSSDServiceNew(cups_dnssd_t *dnssd, uint32_t if_index, const char *name, cups_dnssd_service_cb_t cb, void *cb_data);
bool		cupsDNSSDServicePublish(cups_dnssd_service_t *service);
bool		cupsDNSSDServiceSetLocation(cups_dnssd_service_t *service, const char *geo_uri);
bool		cupsDNSSDAssembleFullName(char *fullname, size_t fullsize, const char *name, const char *type, const char *domain);
size_t		cupsDNSSDDecodeTXT(const unsigned char *txtrec, uint16_t txtlen, cups_option_t **txt);
bool		cupsDNSSDSeparateFullName(const char *fullname, char *name, size_t namesize, char *type, size_t typesize, char *domain, size_t domainsize);
