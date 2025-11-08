#  define CUPS_VERSION			3.0000
#  define CUPS_VERSION_MAJOR		3
#  define CUPS_VERSION_MINOR		0
#  define CUPS_VERSION_PATCH		0

#  define CUPS_DATE_ANY			(time_t)-1
#  define CUPS_FORMAT_AUTO		"application/octet-stream"
#  define CUPS_FORMAT_JPEG		"image/jpeg"
#  define CUPS_FORMAT_PDF		"application/pdf"
#  define CUPS_FORMAT_TEXT		"text/plain"
#  define CUPS_HTTP_DEFAULT		(http_t *)0
#  define CUPS_JOBID_ALL		-1
#  define CUPS_JOBID_CURRENT		0
#  define CUPS_LENGTH_VARIABLE		(ssize_t)0
#  define CUPS_TIMEOUT_DEFAULT		0

// Options and values
#  define CUPS_COPIES			"copies"
#  define CUPS_COPIES_SUPPORTED		"copies-supported"

#  define CUPS_FINISHINGS		"finishings"
#  define CUPS_FINISHINGS_SUPPORTED	"finishings-supported"

#  define CUPS_FINISHINGS_BIND		"7"
#  define CUPS_FINISHINGS_COVER		"6"
#  define CUPS_FINISHINGS_FOLD		"10"
#  define CUPS_FINISHINGS_NONE		"3"
#  define CUPS_FINISHINGS_PUNCH		"5"
#  define CUPS_FINISHINGS_STAPLE	"4"
#  define CUPS_FINISHINGS_TRIM		"11"

#  define CUPS_MEDIA			"media"
#  define CUPS_MEDIA_READY		"media-ready"
#  define CUPS_MEDIA_SUPPORTED		"media-supported"

#  define CUPS_MEDIA_3X5		"na_index-3x5_3x5in"
#  define CUPS_MEDIA_4X6		"na_index-4x6_4x6in"
#  define CUPS_MEDIA_5X7		"na_5x7_5x7in"
#  define CUPS_MEDIA_8X10		"na_govt-letter_8x10in"
#  define CUPS_MEDIA_A3			"iso_a3_297x420mm"
#  define CUPS_MEDIA_A4			"iso_a4_210x297mm"
#  define CUPS_MEDIA_A5			"iso_a5_148x210mm"
#  define CUPS_MEDIA_A6			"iso_a6_105x148mm"
#  define CUPS_MEDIA_ENV10		"na_number-10_4.125x9.5in"
#  define CUPS_MEDIA_ENVDL		"iso_dl_110x220mm"
#  define CUPS_MEDIA_LEGAL		"na_legal_8.5x14in"
#  define CUPS_MEDIA_LETTER		"na_letter_8.5x11in"
#  define CUPS_MEDIA_PHOTO_L		"oe_photo-l_3.5x5in"
#  define CUPS_MEDIA_SUPERBA3		"na_super-b_13x19in"
#  define CUPS_MEDIA_TABLOID		"na_ledger_11x17in"

#  define CUPS_MEDIA_SOURCE		"media-source"
#  define CUPS_MEDIA_SOURCE_SUPPORTED	"media-source-supported"

#  define CUPS_MEDIA_SOURCE_AUTO	"auto"
#  define CUPS_MEDIA_SOURCE_MANUAL	"manual"

#  define CUPS_MEDIA_TYPE		"media-type"
#  define CUPS_MEDIA_TYPE_SUPPORTED	"media-type-supported"

#  define CUPS_MEDIA_TYPE_AUTO		"auto"
#  define CUPS_MEDIA_TYPE_ENVELOPE	"envelope"
#  define CUPS_MEDIA_TYPE_LABELS	"labels"
#  define CUPS_MEDIA_TYPE_LETTERHEAD	"stationery-letterhead"
#  define CUPS_MEDIA_TYPE_PHOTO		"photographic"
#  define CUPS_MEDIA_TYPE_PHOTO_GLOSSY	"photographic-glossy"
#  define CUPS_MEDIA_TYPE_PHOTO_MATTE	"photographic-matte"
#  define CUPS_MEDIA_TYPE_PLAIN		"stationery"
#  define CUPS_MEDIA_TYPE_TRANSPARENCY	"transparency"

#  define CUPS_NUMBER_UP		"number-up"
#  define CUPS_NUMBER_UP_SUPPORTED	"number-up-supported"

#  define CUPS_ORIENTATION		"orientation-requested"
#  define CUPS_ORIENTATION_SUPPORTED	"orientation-requested-supported"

#  define CUPS_ORIENTATION_PORTRAIT	"3"
#  define CUPS_ORIENTATION_LANDSCAPE	"4"

#  define CUPS_PRINT_COLOR_MODE		"print-color-mode"
#  define CUPS_PRINT_COLOR_MODE_SUPPORTED "print-color-mode-supported"

#  define CUPS_PRINT_COLOR_MODE_AUTO	"auto"
#  define CUPS_PRINT_COLOR_MODE_BI_LEVEL "bi-level"
#  define CUPS_PRINT_COLOR_MODE_COLOR	"color"
#  define CUPS_PRINT_COLOR_MODE_MONOCHROME "monochrome"

#  define CUPS_PRINT_QUALITY		"print-quality"
#  define CUPS_PRINT_QUALITY_SUPPORTED	"print-quality-supported"

#  define CUPS_PRINT_QUALITY_DRAFT	"3"
#  define CUPS_PRINT_QUALITY_NORMAL	"4"
#  define CUPS_PRINT_QUALITY_HIGH	"5"

#  define CUPS_SIDES			"sides"
#  define CUPS_SIDES_SUPPORTED		"sides-supported"

#  define CUPS_SIDES_ONE_SIDED		"one-sided"
#  define CUPS_SIDES_TWO_SIDED_PORTRAIT	"two-sided-long-edge"
#  define CUPS_SIDES_TWO_SIDED_LANDSCAPE "two-sided-short-edge"

enum cups_credpurpose_e
{
  CUPS_CREDPURPOSE_SERVER_AUTH = 0x01,
  CUPS_CREDPURPOSE_CLIENT_AUTH = 0x02,
  CUPS_CREDPURPOSE_CODE_SIGNING = 0x04,
  CUPS_CREDPURPOSE_EMAIL_PROTECTION = 0x08,
  CUPS_CREDPURPOSE_TIME_STAMPING = 0x10,
  CUPS_CREDPURPOSE_OCSP_SIGNING = 0x20,
  CUPS_CREDPURPOSE_ALL = 0x3f
};
typedef unsigned cups_credpurpose_t;
typedef enum cups_credtype_e
{
  CUPS_CREDTYPE_DEFAULT,
  CUPS_CREDTYPE_RSA_2048_SHA256,
  CUPS_CREDTYPE_RSA_3072_SHA256,
  CUPS_CREDTYPE_RSA_4096_SHA256,
  CUPS_CREDTYPE_ECDSA_P256_SHA256,
  CUPS_CREDTYPE_ECDSA_P384_SHA256,
  CUPS_CREDTYPE_ECDSA_P521_SHA256
} cups_credtype_t;
enum cups_credusage_e
{
  CUPS_CREDUSAGE_DIGITAL_SIGNATURE = 0x001,
  CUPS_CREDUSAGE_NON_REPUDIATION = 0x002,
  CUPS_CREDUSAGE_KEY_ENCIPHERMENT = 0x004,
  CUPS_CREDUSAGE_DATA_ENCIPHERMENT = 0x008,
  CUPS_CREDUSAGE_KEY_AGREEMENT = 0x010,
  CUPS_CREDUSAGE_KEY_CERT_SIGN = 0x020,
  CUPS_CREDUSAGE_CRL_SIGN = 0x040,
  CUPS_CREDUSAGE_ENCIPHER_ONLY = 0x080,
  CUPS_CREDUSAGE_DECIPHER_ONLY = 0x100,
  CUPS_CREDUSAGE_DEFAULT_CA = 0x061,
  CUPS_CREDUSAGE_DEFAULT_TLS = 0x005,
  CUPS_CREDUSAGE_ALL = 0x1ff
};
typedef unsigned cups_credusage_t;
enum cups_dest_flags_e
{
  CUPS_DEST_FLAGS_NONE = 0x00,
  CUPS_DEST_FLAGS_UNCONNECTED = 0x01,
  CUPS_DEST_FLAGS_MORE = 0x02,
  CUPS_DEST_FLAGS_REMOVED = 0x04,
  CUPS_DEST_FLAGS_ERROR = 0x08,
  CUPS_DEST_FLAGS_RESOLVING = 0x10,
  CUPS_DEST_FLAGS_CONNECTING = 0x20,
  CUPS_DEST_FLAGS_CANCELED = 0x40,
  CUPS_DEST_FLAGS_DEVICE = 0x80
};
typedef unsigned cups_dest_flags_t;
enum cups_media_flags_e
{
  CUPS_MEDIA_FLAGS_DEFAULT = 0x00,
  CUPS_MEDIA_FLAGS_BORDERLESS = 0x01,
  CUPS_MEDIA_FLAGS_DUPLEX = 0x02,
  CUPS_MEDIA_FLAGS_EXACT = 0x04,
  CUPS_MEDIA_FLAGS_READY = 0x08
};
typedef unsigned cups_media_flags_t;
enum cups_ptype_e
{
  CUPS_PTYPE_LOCAL = 0x0000,
  CUPS_PTYPE_CLASS = 0x0001,
  CUPS_PTYPE_REMOTE = 0x0002,
  CUPS_PTYPE_BW = 0x0004,
  CUPS_PTYPE_COLOR = 0x0008,
  CUPS_PTYPE_DUPLEX = 0x0010,
  CUPS_PTYPE_STAPLE = 0x0020,
  CUPS_PTYPE_COPIES = 0x0040,
  CUPS_PTYPE_COLLATE = 0x0080,
  CUPS_PTYPE_PUNCH = 0x0100,
  CUPS_PTYPE_COVER = 0x0200,
  CUPS_PTYPE_BIND = 0x0400,
  CUPS_PTYPE_SORT = 0x0800,
  CUPS_PTYPE_SMALL = 0x1000,
  CUPS_PTYPE_MEDIUM = 0x2000,
  CUPS_PTYPE_LARGE = 0x4000,
  CUPS_PTYPE_VARIABLE = 0x8000,
  CUPS_PTYPE_DEFAULT = 0x20000,
  CUPS_PTYPE_FAX = 0x40000,
  CUPS_PTYPE_REJECTING = 0x80000,
  CUPS_PTYPE_NOT_SHARED = 0x200000,
  CUPS_PTYPE_AUTHENTICATED = 0x400000,
  CUPS_PTYPE_COMMANDS = 0x800000,
  CUPS_PTYPE_DISCOVERED = 0x1000000,
  CUPS_PTYPE_SCANNER = 0x2000000,
  CUPS_PTYPE_MFP = 0x4000000,
  CUPS_PTYPE_FOLD = 0x10000000,
  CUPS_PTYPE_OPTIONS = 0x1006fffc
};
typedef unsigned cups_ptype_t;
typedef enum cups_whichjobs_e
{
  CUPS_WHICHJOBS_ALL = -1,
  CUPS_WHICHJOBS_ACTIVE,
  CUPS_WHICHJOBS_COMPLETED
} cups_whichjobs_t;
typedef struct cups_option_s
{
  char		*name;
  char		*value;
} cups_option_t;
typedef struct cups_dest_s
{
  char		*name,
		*instance;
  bool		is_default;
  size_t	num_options;
  cups_option_t	*options;
} cups_dest_t;
typedef struct _cups_dinfo_s cups_dinfo_t;
typedef struct cups_job_s
{
  int		id;
  char		*dest;
  char		*title;
  char		*user;
  char		*format;
  ipp_jstate_t	state;
  int		size;
  int		priority;
  time_t	completed_time;
  time_t	creation_time;
  time_t	processing_time;
} cups_job_t;
typedef struct cups_media_s
{
  char		media[128],
		color[128],
		source[128],
		type[128];
  int		width,
		length,
		bottom,
		left,
		right,
		top;
} cups_media_t;
typedef bool (*cups_cert_san_cb_t)(const char *common_name, const char *subject_alt_name, void *user_data);
typedef bool (*cups_dest_cb_t)(void *user_data, cups_dest_flags_t flags, cups_dest_t *dest);
typedef const char *(*cups_oauth_cb_t)(http_t *http, const char *realm, const char *scope, const char *resource, void *user_data);
typedef const char *(*cups_password_cb_t)(const char *prompt, http_t *http, const char *method, const char *resource, void *user_data);
size_t		cupsAddDest(const char *name, const char *instance, size_t num_dests, cups_dest_t **dests);
size_t		cupsAddDestMediaOptions(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, unsigned flags, cups_media_t *media, size_t num_options, cups_option_t **options);
size_t		cupsAddIntegerOption(const char *name, long value, size_t num_options, cups_option_t **options);
size_t		cupsAddOption(const char *name, const char *value, size_t num_options, cups_option_t **options);
bool		cupsAreCredentialsValidForName(const char *common_name, const char *credentials);
ipp_status_t	cupsCancelDestJob(http_t *http, cups_dest_t *dest, int job_id);
bool		cupsCheckDestSupported(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, const char *option, const char *value);
ipp_status_t	cupsCloseDestJob(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, int job_id);
size_t		cupsConcatString(char *dst, const char *src, size_t dstsize);
http_t		*cupsConnectDest(cups_dest_t *dest, unsigned flags, int msec, int *cancel, char *resource, size_t resourcesize, cups_dest_cb_t cb, void *user_data);
char		*cupsCopyCredentials(const char *path, const char *common_name);
char		*cupsCopyCredentialsKey(const char *path, const char *common_name);
char		*cupsCopyCredentialsPublicKey(const char *path, const char *common_name);
char		*cupsCopyCredentialsRequest(const char *path, const char *common_name);
size_t		cupsCopyDest(cups_dest_t *dest, size_t num_dests, cups_dest_t **dests);
cups_dinfo_t	*cupsCopyDestInfo(http_t *http, cups_dest_t *dest, cups_dest_flags_t dflags);
int		cupsCopyDestConflicts(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, size_t num_options, cups_option_t *options, const char *new_option, const char *new_value, size_t *num_conflicts, cups_option_t **conflicts, size_t *num_resolved, cups_option_t **resolved);
size_t		cupsCopyString(char *dst, const char *src, size_t dstsize);
bool		cupsCreateCredentials(const char *path, bool ca_cert, cups_credpurpose_t purpose, cups_credtype_t type, cups_credusage_t usage, const char *organization, const char *org_unit, const char *locality, const char *state_province, const char *country, const char *common_name, const char *email, size_t num_alt_names, const char * const *alt_names, const char *root_name, time_t expiration_date);
bool		cupsCreateCredentialsRequest(const char *path, cups_credpurpose_t purpose, cups_credtype_t type, cups_credusage_t usage, const char *organization, const char *org_unit, const char *locality, const char *state_province, const char *country, const char *common_name, const char *email, size_t num_alt_names, const char * const *alt_names);
ipp_status_t	cupsCreateDestJob(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, int *job_id, const char *title, size_t num_options, cups_option_t *options);
int		cupsCreateTempFd(const char *prefix, const char *suffix, char *filename, size_t len);
cups_file_t	*cupsCreateTempFile(const char *prefix, const char *suffix, char *filename, size_t len);
bool		cupsDoAuthentication(http_t *http, const char *method, const char *resource);
ipp_t		*cupsDoFileRequest(http_t *http, ipp_t *request, const char *resource, const char *filename);
ipp_t		*cupsDoIORequest(http_t *http, ipp_t *request, const char *resource, int infile, int outfile);
ipp_t		*cupsDoRequest(http_t *http, ipp_t *request, const char *resource);
ipp_attribute_t	*cupsEncodeOption(ipp_t *ipp, ipp_tag_t group_tag, const char *name, const char *value);
void		cupsEncodeOptions(ipp_t *ipp, size_t num_options, cups_option_t *options, ipp_tag_t group_tag);
bool		cupsEnumDests(cups_dest_flags_t flags, int msec, int *cancel, cups_ptype_t type, cups_ptype_t mask, cups_dest_cb_t cb, void *user_data);
ipp_attribute_t	*cupsFindDestDefault(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, const char *option);
ipp_attribute_t	*cupsFindDestReady(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, const char *option);
ipp_attribute_t	*cupsFindDestSupported(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, const char *option);
ipp_status_t	cupsFinishDestDocument(http_t *http, cups_dest_t *dest, cups_dinfo_t *info);
ssize_t		cupsFormatString(char *buffer, size_t bufsize, const char *format, ...);
ssize_t		cupsFormatStringv(char *buffer, size_t bufsize, const char *format, va_list ap);
void		cupsFreeDestInfo(cups_dinfo_t *dinfo);
void		cupsFreeDests(size_t num_dests, cups_dest_t *dests);
void		cupsFreeJobs(size_t num_jobs, cups_job_t *jobs);
void		cupsFreeOptions(size_t num_options, cups_option_t *options);
double		cupsGetClock(void);
time_t		cupsGetCredentialsExpiration(const char *credentials);
char		*cupsGetCredentialsInfo(const char *credentials, char *buffer, size_t bufsize);
http_trust_t	cupsGetCredentialsTrust(const char *path, const char *common_name, const char *credentials, bool require_ca);
const char	*cupsGetDefault(http_t *http);
cups_dest_t	*cupsGetDest(const char *name, const char *instance, size_t num_dests, cups_dest_t *dests);
bool		cupsGetDestMediaByIndex(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, size_t n, unsigned flags, cups_media_t *media);
bool		cupsGetDestMediaByName(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, const char *name, unsigned flags, cups_media_t *media);
bool		cupsGetDestMediaBySize(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, int width, int length, unsigned flags, cups_media_t *media);
size_t		cupsGetDestMediaCount(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, unsigned flags);
bool		cupsGetDestMediaDefault(http_t *http, cups_dest_t *dest, cups_dinfo_t *dinfo, unsigned flags, cups_media_t *media);
cups_dest_t	*cupsGetDestWithURI(const char *name, const char *uri);
size_t		cupsGetDests(http_t *http, cups_dest_t **dests);
http_encryption_t cupsGetEncryption(void);
ipp_status_t	cupsGetError(void);
const char	*cupsGetErrorString(void);
http_status_t	cupsGetFd(http_t *http, const char *resource, int fd);
http_status_t	cupsGetFile(http_t *http, const char *resource, const char *filename);
long		cupsGetIntegerOption(const char *name, size_t num_options, cups_option_t *options);
size_t		cupsGetJobs(http_t *http, cups_job_t **jobs, const char *name, bool myjobs, cups_whichjobs_t whichjobs);
cups_dest_t	*cupsGetNamedDest(http_t *http, const char *name, const char *instance);
// const char	*cupsGetOption(const char *name, size_t num_options, cups_option_t *options);
const char	*cupsGetPassword(const char *prompt, http_t *http, const char *method, const char *resource);
unsigned		cupsGetRand(void);
ipp_t		*cupsGetResponse(http_t *http, const char *resource);
const char	*cupsGetServer(void);
const char	*cupsGetUser(void);
const char	*cupsGetUserAgent(void);
ssize_t		cupsHashData(const char *algorithm, const void *data, size_t datalen, unsigned char *hash, size_t hashsize);
const char	*cupsHashString(const unsigned char *hash, size_t hashsize, char *buffer, size_t bufsize);
ssize_t		cupsHMACData(const char *algorithm, const unsigned char *key, size_t keylen, const void *data, size_t datalen, unsigned char *hash, size_t hashsize);
const char	*cupsLocalizeDestMedia(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, unsigned flags, cups_media_t *media);
const char	*cupsLocalizeDestOption(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, const char *option);
const char	*cupsLocalizeDestValue(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, const char *option, const char *value);
char		*cupsLocalizeNotifySubject(cups_lang_t *lang, ipp_t *event);
char		*cupsLocalizeNotifyText(cups_lang_t *lang, ipp_t *event);
size_t		cupsParseOptions(const char *arg, const char **end, size_t num_options, cups_option_t **options);
http_status_t	cupsPutFd(http_t *http, const char *resource, int fd);
http_status_t	cupsPutFile(http_t *http, const char *resource, const char *filename);
ssize_t		cupsReadResponseData(http_t *http, char *buffer, size_t length);
size_t		cupsRemoveDest(const char *name, const char *instance, size_t num_dests, cups_dest_t **dests);
size_t		cupsRemoveOption(const char *name, size_t num_options, cups_option_t **options);
bool		cupsSaveCredentials(const char *path, const char *common_name, const char *credentials, const char *key);
http_status_t	cupsSendRequest(http_t *http, ipp_t *request, const char *resource, size_t length);
void		cupsSetOAuthCB(cups_oauth_cb_t cb, void *data);
bool		cupsSetClientCredentials(const char *credentials, const char *key);
void		cupsSetDefaultDest(const char *name, const char *instance, size_t num_dests, cups_dest_t *dests);
bool		cupsSetDests(http_t *http, size_t num_dests, cups_dest_t *dests);
void		cupsSetEncryption(http_encryption_t e);
void		cupsSetPasswordCB(cups_password_cb_t cb, void *user_data);
void		cupsSetServer(const char *server);
bool		cupsSetServerCredentials(const char *path, const char *common_name, bool auto_create);
void		cupsSetUser(const char *user);
void		cupsSetUserAgent(const char *user_agent);
bool		cupsSignCredentialsRequest(const char *path, const char *common_name, const char *request, const char *root_name, cups_credpurpose_t allowed_purpose, cups_credusage_t allowed_usage, cups_cert_san_cb_t cb, void *cb_data, time_t expiration_date);
http_status_t	cupsStartDestDocument(http_t *http, cups_dest_t *dest, cups_dinfo_t *info, int job_id, const char *docname, const char *format, size_t num_options, cups_option_t *options, bool last_document);
http_status_t	cupsWriteRequestData(http_t *http, const char *buffer, size_t length);
