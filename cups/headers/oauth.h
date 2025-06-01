typedef enum cups_ogrant_e		
{
  CUPS_OGRANT_AUTHORIZATION_CODE,	
  CUPS_OGRANT_DEVICE_CODE,		
  CUPS_OGRANT_REFRESH_TOKEN		
} cups_ogrant_t;
void		cupsOAuthClearTokens(const char *auth_uri, const char *resource_uri);
char		*cupsOAuthCopyAccessToken(const char *auth_uri, const char *resource_uri, time_t *access_expires);
char		*cupsOAuthCopyClientId(const char *auth_uri, const char *redirect_uri);
char		*cupsOAuthCopyRefreshToken(const char *auth_uri, const char *resource_uri);
cups_jwt_t	*cupsOAuthCopyUserId(const char *auth_uri, const char *resource_uri);
char		*cupsOAuthGetAuthorizationCode(const char *auth_uri, cups_json_t *metadata, const char *resource_uri, const char *scopes, const char *redirect_uri);
char		*cupsOAuthGetClientId(const char *auth_uri, cups_json_t *metadata, const char *redirect_uri, const char *logo_uri, const char *tos_uri);
cups_json_t	*cupsOAuthGetMetadata(const char *auth_uri);
char		*cupsOAuthGetTokens(const char *auth_uri, cups_json_t *metadata, const char *resource_uri, const char *grant_code, cups_ogrant_t grant_type, const char *redirect_uri, time_t *access_expires);
char		*cupsOAuthMakeAuthorizationURL(const char *auth_uri, cups_json_t *metadata, const char *resource_uri, const char *scopes, const char *client_id, const char *code_verifier, const char *nonce, const char *redirect_uri, const char *state);
char		*cupsOAuthMakeBase64Random(size_t len);
void		cupsOAuthSaveClientData(const char *auth_uri, const char *redirect_uri, const char *client_id, const char *client_secret);
void		cupsOAuthSaveTokens(const char *auth_uri, const char *resource_uri, const char *access_token, time_t access_expires, const char *user_id, const char *refresh_token);
