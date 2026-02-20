typedef enum cups_jwa_e
{
  CUPS_JWA_NONE,
  CUPS_JWA_HS256,
  CUPS_JWA_HS384,
  CUPS_JWA_HS512,
  CUPS_JWA_RS256,
  CUPS_JWA_RS384,
  CUPS_JWA_RS512,
  CUPS_JWA_ES256,
  CUPS_JWA_ES384,
  CUPS_JWA_ES512,
  CUPS_JWA_MAX
} cups_jwa_t;
typedef enum cups_jws_format_e
{
  CUPS_JWS_FORMAT_COMPACT,
  CUPS_JWS_FORMAT_JSON
} cups_jws_format_t;
typedef struct _cups_jwt_s cups_jwt_t;
void		cupsJWTDelete(cups_jwt_t *jwt);
char		*cupsJWTExportString(cups_jwt_t *jwt, cups_jws_format_t format);
cups_jwa_t	cupsJWTGetAlgorithm(cups_jwt_t *jwt);
double		cupsJWTGetClaimNumber(cups_jwt_t *jwt, const char *claim);
const char	*cupsJWTGetClaimString(cups_jwt_t *jwt, const char *claim);
cups_jtype_t	cupsJWTGetClaimType(cups_jwt_t *jwt, const char *claim);
cups_json_t	*cupsJWTGetClaimValue(cups_jwt_t *jwt, const char *claim);
cups_json_t	*cupsJWTGetClaims(cups_jwt_t *jwt);
double		cupsJWTGetHeaderNumber(cups_jwt_t *jwt, const char *claim);
const char	*cupsJWTGetHeaderString(cups_jwt_t *jwt, const char *claim);
cups_jtype_t	cupsJWTGetHeaderType(cups_jwt_t *jwt, const char *claim);
cups_json_t	*cupsJWTGetHeaderValue(cups_jwt_t *jwt, const char *claim);
cups_json_t	*cupsJWTGetHeaders(cups_jwt_t *jwt);
bool		cupsJWTHasValidSignature(cups_jwt_t *jwt, cups_json_t *keys);
cups_jwt_t	*cupsJWTImportString(const char *s, cups_jws_format_t format);
cups_json_t	*cupsJWTLoadCredentials(const char *path, const char *common_name);
cups_json_t	*cupsJWTMakePrivateKey(cups_jwa_t alg);
cups_json_t	*cupsJWTMakePublicKey(cups_json_t *jwk);
cups_jwt_t	*cupsJWTNew(const char *type, cups_json_t *claims);
void		cupsJWTSetClaimNumber(cups_jwt_t *jwt, const char *claim, double value);
void		cupsJWTSetClaimString(cups_jwt_t *jwt, const char *claim, const char *value);
void		cupsJWTSetClaimValue(cups_jwt_t *jwt, const char *claim, cups_json_t *value);
void		cupsJWTSetHeaderNumber(cups_jwt_t *jwt, const char *claim, double value);
void		cupsJWTSetHeaderString(cups_jwt_t *jwt, const char *claim, const char *value);
void		cupsJWTSetHeaderValue(cups_jwt_t *jwt, const char *claim, cups_json_t *value);
bool		cupsJWTSign(cups_jwt_t *jwt, cups_jwa_t alg, cups_json_t *keys);
